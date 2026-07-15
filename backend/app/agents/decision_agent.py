from app.services.openai_client import generate_response
from app.models.decision import ProductDecision
from app.services.prompt_loader import load_prompt


def analyze_decision(decision: ProductDecision):

    prompt = load_prompt("challenge-agent")

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

Constraints:
{decision.constraints}
"""

    response = generate_response(
        f"""
You are an AI Product Mentor.

Help a Product Manager make a product decision.

Analyze this decision:

{decision_context}

Provide:

1. Key assumptions
2. Risks
3. Alternatives
4. Trade-offs
5. Recommendation
6. Next questions for validation
"""
    )

    return response