---
title: GitHub - kennethwolters/litelm: litellm without the bloat · GitHub
url: https://github.com/kennethwolters/litelm
date: 2026-09-12
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-13T02:07:00.418755
---

# GitHub - kennethwolters/litelm: litellm without the bloat · GitHub

# litelm – lightweight LiteLLM core

## Overview
- Extracts LiteLLM’s routing, message translation, streaming, tool use, and embeddings into ~2,900 lines with only two dependencies (`openai`, `httpx`).
- Removes all extra layers such as routers, proxies, caching, cost tracking, and other rarely‑used features.
- Provides a drop‑in replacement for LiteLLM’s API (same function names, arguments, and response types).

## Installation
- Base package: `pip install litelm` (adds `openai` + `httpx`).
- Optional extras:
  - `litelm[anthropic]` – adds Anthropic SDK.
  - `litelm[bedrock]` – adds `boto3`.
  - `litelm[all]` – installs all supported provider SDKs.

## Basic Usage
```python
import litelm

# Completion
resp = litelm.completion(
    "openai/gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(resp.choices[0].message.content)

# Streaming
for chunk in litelm.completion(
    "groq/llama-3.1-70b-versatile",
    messages=[...],
    stream=True,
):
    print(chunk.choices[0].delta.content or "", end="")

# Embeddings
emb = litelm.embedding(
    "openai/text-embedding-3-small",
    input=["hello world"]
)
```
- Async equivalents are available (`acompletion`, `aembedding`, etc.).

## Feature Comparison (litelm vs. LiteLLM)
| Feature | litelm | LiteLLM |
|---------|--------|---------|
| Model routing | ✓ | ✓ |
| Message translation | ✓ | ✓ |
| Streaming | ✓ | ✓ |
| Tool use (function calling) | ✓ | ✓ |
| Embeddings | ✓ | ✓ |
| Text completions | ✓ | ✓ |
| OpenAI Responses API | ✓ | ✓ |
| Mock responses | ✓ | ✓ |
| Router (load balancing, fallbacks) | ✗ | ✓ |
| Proxy server | ✗ | ✓ |
| Caching / budgeting / cost tracking | ✗ | ✓ |
| Token counting | ✗ | ✓ |
| Image, audio, OCR, fine‑tuning | ✗ | ✓ |
| Agents, guardrails, scheduler | ✗ | ✓ |

## Supported Providers
- 19 providers reachable via `"provider/model-name"` syntax.
- OpenAI‑compatible endpoints can be used with a custom `api_base`.
- Example environment variables: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GROQ_API_KEY`, etc.

## API Keys
- Set via environment variables (e.g., `export OPENAI_API_KEY=sk-...`).
- Or pass directly in function calls with `api_key=` or `api_base=` for local servers.

## Error Handling
All provider‑specific errors are mapped to litelm’s unified exception hierarchy:
```python
from litelm import ContextWindowExceededError, RateLimitError, AuthenticationError

try:
    resp = litelm.completion("openai/gpt-4o", messages=messages)
except ContextWindowExceededError:
    # truncate and retry
except RateLimitError:
    # back‑off
except AuthenticationError:
    # invalid key
```

## Tool Calling
```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}}
        }
    }
}]
resp = litelm.completion(
    "openai/gpt-4o",
    messages=[{"role": "user", "content": "Weather in Paris?"}],
    tools=tools,
    tool_choice="required",
)
tool_call = resp.choices[0].message.tool_calls[0]
print(tool_call.function.name, tool_call.function.arguments)
```

## Custom / Local Providers
Any OpenAI‑compatible server works by specifying `api_base`:
- vLLM: `api_base="http://localhost:8000/v1"`
- Ollama: `api_base="http://localhost:11434/v1"`
- LM Studio: `api_base="http://localhost:1234/v1"`

## Development & Compatibility
- Code largely AI‑assisted (Claude Opus, later GPT‑5.5).
- Upstream audit (2026‑09‑11) reviewed core routing/formatting changes; 262 core‑path tests passed, plus live provider and DSPy smoke tests.
- Declared compatibility limited to routing, formatting, and DSPy surface, not full LiteLLM feature set.

## Project Status
- Alpha release.
- 262 internal tests passing; 45 live provider tests and 10 DSPy integration tests also pass.
- No remaining actionable assertion or runtime failures.

## Testing Commands
```bash
uv run --extra all pytest tests/ -x --ignore=tests/ported --timeout=10   # 262 non‑live tests
bash scripts/ported_contract.sh                                            # 49 fast upstream contract tests
uv run --extra all pytest tests/test_live.py -m live --timeout=30        # 45 live provider tests
uv run pytest tests/test_dspy_smoke.py -m live --timeout=60              # 10 DSPy integration tests
```
Live tests require API keys in `.env.test` and are skipped by default.