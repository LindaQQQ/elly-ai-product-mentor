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

## Chat API and Memory v0.1

`POST /mentor/chat` starts a product-mentoring conversation. Reuse the returned
`conversation_id` to continue it; Memory v0.1 retains the conversation and
retrieves relevant prior product context. See [Memory v0.1](docs/memory-v0.1.md)
for the request and response flow.

The Mentor Orchestrator selects a `challenge`, `decision`, or general `mentor`
mode for each chat message, while retaining the same conversation context.

## Run the MVP chat app

From `backend`, start the API with `uvicorn app.main:app --reload`, then open
`http://127.0.0.1:8000/app`. Challenge Idea and Product Decision use the Mentor
chat API. AI Planning is currently evaluated with frontend mock data.

For the recommended presentation story, sample inputs, talk track, and fallback
plan, see [Demo Flow](docs/demo-flow.md).

---

## Philosophy

> Before we build anything, let's make sure we are solving the right problem.
