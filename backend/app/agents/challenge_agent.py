from app.services.openai_client import generate_response
from app.services.prompt_loader import load_prompt


def challenge_idea(idea: str):

    system_prompt = load_prompt(
        "challenge-agent.md"
    )

    result = generate_response(
        system_prompt,
        idea
    )

    return result