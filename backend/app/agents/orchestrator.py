"""Route a mentor message to the product-thinking mode that best fits it."""

from enum import Enum


class MentorMode(str, Enum):
    CHALLENGE = "challenge"
    DECISION = "decision"
    MENTOR = "mentor"


DECISION_SIGNALS = (
    "decision",
    "decide",
    "prioritize",
    "priority",
    "trade-off",
    "tradeoff",
    "should we build",
    "whether to",
    "選擇",
    "決策",
    "優先",
    "取捨",
    "是否要",
)

CHALLENGE_SIGNALS = (
    "idea",
    "mvp",
    "validate",
    "assumption",
    "product concept",
    "想做",
    "構想",
    "點子",
    "驗證",
    "假設",
)


def route_message(message: str) -> MentorMode:
    """Use transparent rules so routing is predictable and easy to improve."""

    normalized = message.lower()
    if any(signal in normalized for signal in DECISION_SIGNALS):
        return MentorMode.DECISION
    if any(signal in normalized for signal in CHALLENGE_SIGNALS):
        return MentorMode.CHALLENGE
    return MentorMode.MENTOR
