# examples/simple-chatbot

Minimal PydanticAI Agent example — wraps a structured-output Agent in a `chat` domain with two REST endpoints. No RAG, no conversation history, no streaming.

## What this example demonstrates

- A `ChatService` that calls a PydanticAI `Agent` and persists the result
- Structured output via `ChatReply(reply: str, confidence: float)`
- `POST /v1/chat` — send a prompt, get a reply back
- `GET /v1/chat/{id}` — retrieve a historical message
- Tests using `MockChatAgent` — no real API key required

## Copy to src/ to run

Auto-discovery only scans `src/`. Copy this example there first:

```bash
cp -r examples/simple-chatbot/src/simple_chatbot src/
```

## Configuration

Edit `_env/quickstart.env`:

```env
LLM_PROVIDER=openai
LLM_API_KEY=sk-...
```

If `LLM_API_KEY` is not set, falls back to `StubChatAgent`.

## Start the server

```bash
rm -f quickstart.db
uv run python run_server_local.py --env quickstart
```

## Try it

```bash
curl -sS -X POST http://127.0.0.1:8001/v1/chat \
  -H 'Content-Type: application/json' \
  -d '{"prompt": "What is the capital of France?"}'

curl -sS http://127.0.0.1:8001/v1/chat/1
```

## Run tests

```bash
pytest examples/simple-chatbot/tests/ -v
```

## Reference

- PydanticAI Agent pattern: `src/classification/`
- DDD domain tutorial: `docs/tutorial/first-domain.md`
