"""Small, local conversation memory for the Mentor chat endpoint."""

import os
import re
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from uuid import uuid4


@dataclass(frozen=True)
class MemoryMessage:
    role: str
    content: str
    created_at: str


class ConversationMemory:
    """Persist product conversations and retrieve relevant prior context.

    Memory v0.1 deliberately stores only the conversation a caller sends to the
    product. It does not infer or retain personal-profile attributes.
    """

    def __init__(self, database_path: Optional[str] = None) -> None:
        default_path = Path(__file__).parents[2] / "data" / "mentor_memory.db"
        self.database_path = Path(
            database_path or os.getenv("MENTOR_MEMORY_DB", str(default_path))
        )
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self) -> None:
        with self._connect() as connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS conversations (
                    id TEXT PRIMARY KEY,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    conversation_id TEXT NOT NULL,
                    role TEXT NOT NULL CHECK(role IN ('user', 'assistant')),
                    content TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    FOREIGN KEY(conversation_id) REFERENCES conversations(id)
                );

                CREATE INDEX IF NOT EXISTS idx_messages_conversation
                ON messages(conversation_id, id);
                """
            )

    def get_or_create_conversation(self, conversation_id: Optional[str] = None) -> str:
        conversation_id = conversation_id or str(uuid4())
        now = self._now()
        with self._connect() as connection:
            connection.execute(
                """
                INSERT INTO conversations (id, created_at, updated_at)
                VALUES (?, ?, ?)
                ON CONFLICT(id) DO NOTHING
                """,
                (conversation_id, now, now),
            )
        return conversation_id

    def add_message(self, conversation_id: str, role: str, content: str) -> None:
        if role not in {"user", "assistant"}:
            raise ValueError("Only user and assistant messages may be stored")

        now = self._now()
        with self._connect() as connection:
            connection.execute(
                """
                INSERT INTO messages (conversation_id, role, content, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (conversation_id, role, content, now),
            )
            connection.execute(
                "UPDATE conversations SET updated_at = ? WHERE id = ?",
                (now, conversation_id),
            )

    def retrieve(self, conversation_id: str, query: str, limit: int = 8) -> list[MemoryMessage]:
        """Return a compact mix of recent and keyword-relevant messages."""

        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT role, content, created_at, id
                FROM messages
                WHERE conversation_id = ?
                ORDER BY id ASC
                """,
                (conversation_id,),
            ).fetchall()

        if not rows:
            return []

        recent = rows[-4:]
        query_terms = set(self._terms(query))
        scored = []
        for index, row in enumerate(rows[:-4]):
            overlap = len(query_terms.intersection(self._terms(row["content"])))
            if overlap:
                scored.append((overlap, index, row))

        relevant = [row for _, _, row in sorted(scored, key=lambda item: (-item[0], -item[1]))]
        selected_ids = {row["id"] for row in recent}
        for row in relevant:
            if len(selected_ids) >= limit:
                break
            selected_ids.add(row["id"])

        selected = [row for row in rows if row["id"] in selected_ids]
        return [MemoryMessage(row["role"], row["content"], row["created_at"]) for row in selected]

    def message_count(self, conversation_id: str) -> int:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT COUNT(*) AS count FROM messages WHERE conversation_id = ?",
                (conversation_id,),
            ).fetchone()
        return int(row["count"])

    @staticmethod
    def _terms(value: str) -> list[str]:
        normalized = value.lower()
        terms = re.findall(r"[\w'-]{2,}", normalized)
        # Chinese and Japanese are often written without word separators. Adding
        # character pairs gives related product statements a useful retrieval
        # signal without introducing another dependency in v0.1.
        for sequence in re.findall(r"[\u3400-\u9fff]+", normalized):
            terms.extend(sequence[index : index + 2] for index in range(len(sequence) - 1))
        return terms

    @staticmethod
    def _now() -> str:
        return datetime.now(timezone.utc).isoformat()
