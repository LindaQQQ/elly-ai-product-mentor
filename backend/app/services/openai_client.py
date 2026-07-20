import os
from typing import Sequence

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def get_client() -> OpenAI:
    """Create the API client only when an AI endpoint is used."""

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured")
    return OpenAI(api_key=api_key)


def generate_response(
    system_prompt: str,
    user_input: str
):

    response = get_client().responses.create(
        model="gpt-5",
        input=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    return response.output_text


def generate_chat_response(messages: Sequence[dict[str, str]]) -> str:
    """Generate a response from a prepared multi-turn chat transcript."""

    response = get_client().responses.create(
        model="gpt-5",
        input=list(messages),
        # A chat mentor should be scannable; deeper analysis is opt-in in prompts.
        max_output_tokens=4000,
    )

    output = response.output_text.strip()
    if not output:
        raise RuntimeError("The model returned an empty chat response")
    return output
