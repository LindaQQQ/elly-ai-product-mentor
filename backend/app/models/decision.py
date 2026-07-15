from enum import Enum
from pydantic import BaseModel
from typing import Optional, List


class DecisionType(str, Enum):
    BUILD = "build"
    MVP_SCOPE = "mvp_scope"
    PRIORITY = "priority"
    TRADE_OFF = "trade_off"
    RISK = "risk"


class RequestSource(str, Enum):
    BUSINESS = "business"
    USER_RESEARCH = "user_research"
    DATA = "data"
    EXECUTIVE = "executive"
    ENGINEERING = "engineering"
    INTERNAL = "internal"


class ProductDecision(BaseModel):
    title: str

    request_source: RequestSource

    decision_type: DecisionType

    problem: Optional[str] = None

    business_context: Optional[str] = None

    user_value: Optional[str] = None

    constraints: Optional[List[str]] = None

    expected_output: Optional[str] = None