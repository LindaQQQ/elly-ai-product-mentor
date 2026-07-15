import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
print(
    "API KEY loaded:",
    bool(os.getenv("OPENAI_API_KEY"))
)

client = OpenAI(
    api_key=os.getenv(
        "OPENAI_API_KEY"
    )
)


def generate_response(
    system_prompt: str,
    user_input: str
):

    response = client.responses.create(
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

    