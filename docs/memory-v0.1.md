# Memory v0.1

`POST /mentor/chat` keeps product-discussion context in a local SQLite database.

## What is retained

- A generated `conversation_id` for each new discussion
- User and mentor messages in that discussion
- Creation and update timestamps

The API does not infer a personal profile or store information outside the
conversation supplied to the product.

## Retrieval

For each new message, the mentor receives up to eight previous messages: the
four most recent messages plus older messages that share keywords with the new
question. This keeps current goals, earlier decisions, and trade-offs available
without sending the entire transcript on every request.

## API

```json
POST /mentor/chat
{
  "message": "We want to build an AI onboarding assistant. What should we validate first?"
}
```

The response includes a `conversation_id`. Send it in later requests to continue
the same product discussion:

```json
POST /mentor/chat
{
  "conversation_id": "returned-id",
  "message": "Our target user is new workspace admins. Does that change the MVP?"
}
```

Every response also includes `mode`, indicating the product-thinking framework
selected by the Mentor Orchestrator: `challenge`, `decision`, or `mentor`.

Set `MENTOR_MEMORY_DB` to use a different SQLite database path. By default the
database is `backend/data/mentor_memory.db`.
