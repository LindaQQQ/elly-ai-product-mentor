from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.agents.challenge_agent import challenge_idea
from app.agents.decision_agent import analyze_decision
from app.agents.mentor_agent import mentor_chat
from app.agents.orchestrator import route_message
from app.models.chat import ChatRequest, ChatResponse, MemoryUsage
from app.models.decision import ProductDecision
from app.services.memory import ConversationMemory

app = FastAPI(
    title="Elly — AI Product Mentor"
)
memory = ConversationMemory()
static_directory = Path(__file__).parent / "static"


class IdeaRequest(BaseModel):
    idea: str


@app.get("/")
def health_check():

    return {
        "status": "Elly running"
    }


@app.get("/app", include_in_schema=False)
def mentor_app():
    """Serve the dependency-free MVP chat interface."""

    return FileResponse(static_directory / "index.html")


@app.post("/mentor/analyze")
def analyze(
    request: IdeaRequest
):

    result = challenge_idea(
        request.idea
    )

    return {
        "idea": request.idea,
        "analysis": result
    }


@app.post("/mentor/decision")
def analyze_product_decision(
    decision: ProductDecision
):

    result = analyze_decision(
        decision
    )

    return {
        "decision": decision,
        "analysis": result
    }


@app.post("/mentor/chat", response_model=ChatResponse)
def chat_with_mentor(request: ChatRequest):
    """Start or continue a product-mentoring conversation."""

    conversation_id = memory.get_or_create_conversation(request.conversation_id)
    relevant_memory = memory.retrieve(conversation_id, request.message)
    mode = route_message(request.message)
    memory.add_message(conversation_id, "user", request.message)

    try:
        reply = mentor_chat(request.message, relevant_memory, mode)
    except Exception as error:
        # Do not leave a user message without exposing a useful API error.
        raise HTTPException(status_code=502, detail="The mentor could not respond.") from error

    memory.add_message(conversation_id, "assistant", reply)
    return ChatResponse(
        conversation_id=conversation_id,
        mode=mode,
        reply=reply,
        memory=MemoryUsage(
            conversation_messages=memory.message_count(conversation_id),
            retrieved_messages=len(relevant_memory),
        ),
    )
