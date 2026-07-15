from fastapi import FastAPI
from pydantic import BaseModel

from app.agents.challenge_agent import challenge_idea

app = FastAPI(
    title="AI Product Mentor"
)


class IdeaRequest(BaseModel):
    idea: str


@app.get("/")
def health_check():

    return {
        "status": "AI Product Mentor running"
    }


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