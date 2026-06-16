---
title: Running local models is good now | ✰Vicki Boykis✰
url: https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/
date: 2026-06-17
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-17T06:02:31.017892
---

# Running local models is good now | ✰Vicki Boykis✰

# Running local models is good now

## Overview
- Local LLMs have progressed from slow, inaccurate tools to reliable assistants for development tasks.
- Personal “vibe metric” shows modern local models rarely need verification against API‑based models.
- Recent releases (e.g., Gemma 4 family) achieve ~75 % of frontier model accuracy/speed for agentic coding.

## Models and runtimes experimented with
- **Models:** Mistral 7B, Gemma 3, OpenAI OSS‑20B, Qwen 3 MOE, Qwen 2.5 Coder, Gemma‑4‑26b‑a4b, Gemma‑4‑12b‑qat.
- **Inference engines:** raw `llama.cpp` with Open WebUI, `llama-cpp-python`, Ollama, llamafiles, LM Studio.

## Current capabilities
- Refactoring notebooks into multi‑module Python repos, adding correct type hints.
- Proofreading blog posts, generating unit tests, bootstrapping recommendation‑model codebases.
- Running agentic workflows inside Docker containers with restricted permissions.
- Handling tasks that were impossible locally only six months ago, even with modest hardware (M2 Mac, 64 GB RAM).

## Practical use cases
- Fast, personalized “Google” for development questions that don’t require up‑to‑date web data.
- Automating repetitive coding chores (refactoring, linting, test generation).
- Experimenting with research pipelines (e.g., trending Arxiv topics) while keeping execution sandboxed.

## Running agentic models locally today
1. **Model choice:** Gemma‑4‑12b‑qat offers a good trade‑off between size, speed, and accuracy compared to the larger 26B variant.
2. **Security:** Execute each agent session in a Docker container with only bash access; optionally allow `curl` for specific research needs.
3. **Agent harness:** Use Pi as the agent framework, pointing it to an LM Studio inference endpoint (or `llama.cpp` for higher speed).
4. **Configuration:** Adjust `models.json` so Pi contacts the local server (`http://host.docker.internal:1234/v1`) using the OpenAI‑compatible API schema.

## Minimal setup sketch
- **Docker‑Compose service** for Pi with mounted `models.json`, workspace directory, and environment variables for API keys (mostly placeholders for local inference).
- **Startup script** builds the container, resolves the workspace path, optionally adds a sandbox compose file, and runs Pi with passed arguments.
- The container isolates file system access, preventing the agent from modifying the host’s hard drive while still allowing it to read the custom model config.

## Limitations
- Inference latency can still be noticeable on consumer hardware.
- Context windows remain limited by available RAM (KV cache can grow to ~64 GB).
- Early model releases may have prompt‑template mismatches, though community patches appear quickly.
- Not yet ready for production‑grade software development without additional safeguards.

## Outlook
- Continued improvements in model architecture (e.g., Gemma‑4‑qat) raise questions about optimal performance‑price trade‑offs.
- Ecosystem tools like LM Studio and Hugging Face’s “Use This Model” button are lowering entry barriers.
- Investing in local‑model tooling now positions developers to benefit from faster, cheaper, and more private AI assistance as the technology matures.