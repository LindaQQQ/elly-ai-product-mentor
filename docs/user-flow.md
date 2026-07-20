# AI Product Mentor User Flow

## Product Navigation

```text
Challenge Idea
Product Decision
AI Planning
AI Spec       (Coming Soon)
AI Evaluation (Coming Soon)
```

## Challenge Idea

```text
Describe an idea
  → Mentor asks questions and challenges assumptions
  → User refines the problem and validation plan
```

## Product Decision

```text
Describe options, constraints, and desired outcome
  → Mentor evaluates trade-offs
  → User receives a recommendation and decision rationale
```

## AI Planning Prototype

```text
Enter requirement description
  + Product goal
  + Primary user
  + Acceptable error risk
  + Knowledge source
        ↓
Select Analyze
        ↓
Review AI Readiness and AI suitability
        ↓
Review recommended solution
(Workflow / RAG / Agent / Memory / Tools)
        ↓
Review architecture, main risks, and next questions
        ↓
Refine the inputs or continue toward AI Spec
```

## Prototype Boundary

AI Planning currently runs entirely in the browser with mock output. It is
designed to validate the questions, information hierarchy, and usefulness of
the result before implementing a Planning Agent and API.
