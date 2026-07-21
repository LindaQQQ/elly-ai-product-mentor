# Elly — AI Product Mentor

An AI product thinking partner that helps PMs challenge ideas, make product
decisions, and plan AI features before teams build them.

## Overview

Elly is an AI-powered product thinking ally for PMs.

Instead of helping PMs write PRDs faster, it helps teams make better product decisions before development begins.

The goal is to simulate the thinking process of a senior product manager and
AI product coach:

- Understand the real problem
- Challenge assumptions
- Evaluate opportunities
- Identify risks
- Recommend MVP scope
- Evaluate whether a problem is suitable for AI
- Recommend a controllable AI solution and identify its risks

---

## Problem

Many AI tools today help product teams produce artifacts:

- PRDs
- User stories
- Requirements
- Documentation

However, great products are not built by writing faster.

They are built by making better decisions.

Common product failures happen because teams:

- Build solutions before validating problems
- Prioritize features without clear impact
- Underestimate dependencies and risks
- Create overly large MVP scopes

---

## Solution

AI Product Mentor acts as a senior product partner before teams start building.

The workflow:
Product Idea

↓

AI Questions

↓

Challenge Assumptions

↓

Product Assessment

↓

MVP Recommendation

---

## Core Capabilities

### 1. Problem Validation

AI helps identify:

- Who has this problem?
- How painful is it?
- How is it solved today?

---

### 2. Product Challenge

AI challenges:

- Hidden assumptions
- Weak differentiation
- Unclear value propositions

---

### 3. MVP Strategy

AI recommends:

- What to build first
- What to postpone
- How to validate value quickly

---

### 4. Risk Analysis

AI evaluates:

- User risk
- Product risk
- Technical risk
- Dependency risk

---

## Product Surfaces

- **Challenge Idea** — challenge assumptions and define the smallest validation
- **Product Decision** — clarify options, trade-offs, and decision criteria
- **AI Planning** — collect product context and show an AI Readiness assessment,
  recommended solution, risks, and next questions
- **AI Spec** — planned
- **AI Evaluation** — planned

AI Planning is currently an interactive frontend prototype. Its Analyze action
uses mock data and does not call a planning API or AI agent yet.

## MVP Scope

The first version focuses on:
Idea
↓
Challenge Session
↓
Product Assessment
↓
MVP Recommendation

Not included initially:

- Full PRD generation
- Team collaboration
- Complex integrations
- Long-term memory system

---

## Architecture

Current MVP architecture:
Frontend
|
|
FastAPI Backend
|
|
AI Agent Orchestrator
|
|
OpenAI API

---

## Agent Design

The system uses role-based AI agents:
Product Mentor Orchestrator

    |
    |

Problem Analyst

    |

Challenge Mentor

    |

MVP Strategist


---

## Project Status

Build Week Project 🚀

Current focus:

- Product framework
- Agent design
- Prompt engineering
- Prototype implementation

## Live Demo

Try Elly at <https://elly-ai-product-mentor.onrender.com/app>.

The demo runs on Render's free tier, so the first request after a period of
inactivity may take about 60 seconds. No account or test credentials are
required.

## Chat API and Memory v0.1

`POST /mentor/chat` starts a product-mentoring conversation. Reuse the returned
`conversation_id` to continue it; Memory v0.1 retains the conversation and
retrieves relevant prior product context. See [Memory v0.1](docs/memory-v0.1.md)
for the request and response flow.

The Mentor Orchestrator selects a `challenge`, `decision`, or general `mentor`
mode for each chat message, while retaining the same conversation context.

## Run the MVP chat app locally

### Requirements

- Python 3.11
- An OpenAI API key for Challenge Idea and Product Decision

### Setup

```bash
git clone https://github.com/LindaQQQ/elly-ai-product-mentor.git
cd elly-ai-product-mentor/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Add your API key to `backend/.env`:

```text
OPENAI_API_KEY=your_openai_api_key
```

Start the application:

```bash
uvicorn app.main:app --reload
```

Then open <http://127.0.0.1:8000/app>.

Challenge Idea and Product Decision use the Mentor chat API and therefore
require the API key. AI Planning is an interactive frontend prototype that uses
mock analysis data and does not send the entered data to an API.

For the recommended presentation story, sample inputs, talk track, and fallback
plan, see [Demo Flow](docs/demo-flow.md).

## How I built Elly with Codex and GPT-5.6

Elly was built during OpenAI Build Week with Codex using GPT-5.6. I used Codex
throughout the project as a product and engineering collaborator—not only to
generate code, but to inspect the repository, compare implementation options,
revise prompts, test user flows, and keep the implemented scope aligned with the
product hypothesis.

Codex and GPT-5.6 helped me:

- turn the product vision into a small, runnable FastAPI application
- implement the Mentor chat endpoint, transparent mode routing, specialized
  prompts, and SQLite conversation memory
- create and refine the responsive HTML, CSS, and JavaScript product experience
- review the repository and document the architecture, decisions, evaluation
  approach, demo flow, and known prototype boundaries
- test the health endpoint, application page, and the main product flows

I made the key product and scope decisions. In particular, I chose to keep
Challenge Idea and Product Decision as the working AI flows, make routing rules
transparent, use a compact Memory v0.1 instead of expanding into personal
long-term memory, and present AI Planning honestly as a frontend prototype
rather than imply that its Planning Agent was already implemented.

GPT-5.6 was used through Codex to build and review the project. The running
application separately uses the OpenAI Responses API with the `gpt-5` model;
API credits are only needed when running the AI-backed chat flows.

### Build Week evidence

- Development commits are dated July 15–20, 2026, within the official Build
  Week submission period.
- The commit history records the product foundation, prompt design, agents,
  decision framework, memory, frontend, and final prototype work.
- Primary Codex `/feedback` Session ID:
  `019f6f82-1121-75b3-9f49-248531263cbc`

---

## Philosophy

> Before we build anything, let's make sure we are solving the right problem.
