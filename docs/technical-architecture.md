# Technical Architecture

## Current Runtime

```text
Browser
  ├─ Static HTML/CSS/JavaScript UI
  │    └─ AI Planning mock analysis (frontend only)
  │
  └─ POST /mentor/chat
         ↓
      FastAPI
         ↓
      Mentor Orchestrator
         ├─ Challenge mode
         ├─ Decision mode
         └─ General mentor mode
         ↓
      OpenAI client

ConversationMemory retains the current chat context in the backend process.
```

## Frontend

The dependency-free frontend is served from `backend/app/static/index.html` at
`GET /app`.

- Challenge Idea and Product Decision call `POST /mentor/chat`.
- AI Planning collects structured inputs and renders a fixed mock assessment.
- AI Spec and AI Evaluation are navigation placeholders.

## Existing APIs

- `POST /mentor/analyze` — challenge an idea
- `POST /mentor/decision` — analyze a structured product decision
- `POST /mentor/chat` — routed Mentor conversation with Memory v0.1

## Not Implemented Yet

- `POST /mentor/planning`
- Planning request and response schemas
- AI Planning Agent and prompt
- Persisted planning sessions
- Generated Readiness score and architecture recommendation
- AI Spec and Evaluation services

## Recommended Next Architecture Step

Only add a Planning API after prototype feedback confirms that the input fields
and output structure are useful. Keep the first implementation deterministic:
one structured request, one structured response schema, and a single Planning
Agent before considering a multi-agent workflow.
