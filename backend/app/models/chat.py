from typing import Optional

from pydantic import BaseModel, Field, validator

from app.agents.orchestrator import MentorMode


class ChatRequest(BaseModel):
    message: str = Field(..., max_length=12_000)
    conversation_id: Optional[str] = Field(
        default=None,
        description="Omit to start a new product discussion; reuse to continue one.",
    )

    @validator("message")
    def message_must_contain_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("message must not be blank")
        return value


class MemoryUsage(BaseModel):
    conversation_messages: int
    retrieved_messages: int


class ChatResponse(BaseModel):
    conversation_id: str
    mode: MentorMode
    reply: str
    memory: MemoryUsage
