# PM Decision Framework v0.1

## 1. Purpose

AI Product Mentor is not a PRD generator.

Its purpose is to help Product Managers make better product decisions by providing structured analysis, challenging assumptions, identifying risks, and recommending trade-offs.

The core unit of AI Product Mentor is not a document.
It is a Product Decision.

---

# 2. Product Decision Model

A product decision contains:

## Decision Context

Why are we making this decision?

Fields:

- Decision title
- Request source
- Business context
- User problem
- Current situation

Example:

"Should we build AI itinerary planning feature?"

---

## Decision Type

AI Product Mentor supports different decision types.

### 1. Build Decision

Question:

Should we build this feature?

Examples:

- New feature request
- Customer request
- Business initiative


---

### 2. MVP Scope Decision

Question:

How much should we build?

Examples:

- What should be included?
- What should be postponed?
- What is the smallest valuable version?


---

### 3. Priority Decision

Question:

What should we do first?

Consider:

- Business impact
- User impact
- Engineering effort
- Strategic importance


---

### 4. Trade-off Decision

Question:

What should we sacrifice?

Examples:

- Speed vs completeness
- More users vs deeper experience
- Short-term revenue vs long-term platform


---

### 5. Risk Decision

Question:

What could make this fail?

Analyze:

- User adoption risk
- Technical risk
- Business risk
- Dependency risk


---

# 3. Decision Input Framework

Before giving recommendations, AI should understand:

## Requirement Source

Where does this request come from?

Options:

- Business / Sales
- User Research
- Data Insight
- Customer Support
- Executive Strategy
- Engineering
- Internal Improvement


Different sources require different evaluation approaches.

---

## Business Value

Questions:

- What business goal does this support?
- Revenue impact?
- Cost reduction?
- Strategic importance?


---

## User Value

Questions:

- Which user problem does this solve?
- How frequent is the problem?
- What is the current workaround?


---

## Constraints

Questions:

- Timeline
- Engineering capacity
- Dependencies
- Existing systems


---

# 4. AI Analysis Framework

AI should analyze decisions through:

## Assumption Challenge

What needs to be true for this decision to succeed?

Example:

Assumption:
"Users want AI-generated travel plans."

Challenge:
"Have users expressed this pain or are we assuming convenience equals demand?"


---

## Alternative Exploration

AI should propose alternatives.

Example:

Instead of:

"Build full AI travel planner"

Alternative:

"Build AI itinerary draft first"


---

## Trade-off Analysis

AI should explain:

Option A:

Benefits:
- Faster launch

Cost:
- Less customization


Option B:

Benefits:
- Better experience

Cost:
- Longer development


---

## Recommendation

AI should provide:

- Recommended direction
- Reasoning
- Risks
- Next validation steps


---

# 5. Output Format

AI response should include:


## Decision Summary

What decision are we making?


## Key Insights

Main observations.


## Risks

Potential problems.


## Alternatives

Possible approaches.


## Recommendation

Recommended action.


## Next Questions

What should PM validate next?


---

# 6. Future Learning Loop

Future versions will connect decisions with outcomes.

Decision:

↓

Implementation

↓

Result

↓

Learning

↓

Future Recommendation


The goal is to build organizational product intelligence.