from app.services.openai_client import generate_response
from app.models.decision import ProductDecision
from app.services.prompt_loader import load_prompt


def analyze_decision(decision: ProductDecision):

    system_prompt = load_prompt("decision-agent.md")

    decision_context = f"""
Decision Title:
{decision.title}

Request Source:
{decision.request_source}

Decision Type:
{decision.decision_type}

Problem:
{decision.problem}

Business Context:
{decision.business_context}

User Value:
{decision.user_value}

Constraints:
{decision.constraints}

Expected Output:
{decision.expected_output}
"""

    response = generate_response(
        system_prompt,
        decision_context
    )

    return response
