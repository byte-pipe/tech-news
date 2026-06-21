---
title: GitHub - tashfeenahmed/freellmapi: OpenAI-compatible proxy that stacks the free tiers of 16 LLM providers (~1.7B tokens/month) behind one /v1 endpoint...
url: https://github.com/tashfeenahmed/freellmapi
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-06-22T00:54:40.647714
---

# GitHub - tashfeenahmed/freellmapi: OpenAI-compatible proxy that stacks the free tiers of 16 LLM providers (~1.7B tokens/month) behind one /v1 endpoint...

# FreeLLMAPI – OpenAI‑compatible proxy for free LLM tiers  

## Why it exists  
- Individual free tiers from many AI providers are tiny; combined they offer ~1.7 B tokens/month across 100+ models.  
- Manually managing 17 SDKs, rate limits, and failures is cumbersome.  
- FreeLLMAPI consolidates all free tiers behind a single OpenAI‑compatible `/v1/chat/completions` endpoint.

## Supported providers  
- Google Gemini 2.5 Flash, Groq (Llama 3.3, Llama 4, GPT‑OSS, Qwen3), Cerebras (Qwen3 235B)  
- OpenCode Zen (DeepSeek V4 Flash, Nemotron), Mistral (Large 3, Medium 3.5, Codestral, Devstral)  
- OpenRouter (21 free models), GitHub Models (GPT‑4.1, GPT‑4o)  
- Cloudflare (Kimi K2, GLM‑4.7, GPT‑OSS, Granite 4)  
- Cohere (Command R+, Command‑A trial), Z.ai (GLM‑4.5, GLM‑4.7 Flash)  
- NVIDIA NIM (40 RPM free), HuggingFace router, Ollama Cloud, Kilo Gateway, Pollinations, LLM7, OVH AI Endpoints  
- Any custom OpenAI‑compatible endpoint (llama.cpp, LM Studio, vLLM, local/remote Ollama)

## Core features  
- OpenAI‑compatible API (`POST /v1/chat/completions`, `GET /v1/models`) works with official SDKs and LangChain, LlamaIndex, etc.  
- Streaming and non‑streaming responses; tool calling supported.  
- Embeddings endpoint with model‑specific failover only.  
- Automatic fallback on 429/5xx/timeout, up to 20 attempts.  
- Per‑key rate tracking (RPM, RPD, TPM, TPD) to stay under free‑tier caps.  
- Sticky sessions keep the same model for 30 min to reduce hallucinations.  
- Encrypted key storage (AES‑256‑GCM) and unified bearer token for client auth.  
- Admin dashboard (React + Vite) for key management, fallback ordering, analytics, and playground.  
- Health checks mark keys as healthy, rate‑limited, invalid, or error.  
- Optional context handoff when switching models.  
- Runs on any Node 20+ environment (Windows, macOS, Linux, ARM SBC); ~40 MB idle memory.

## Not yet supported  
- Image generation, audio/speech, legacy completions, moderation, multiple completions per request, multi‑tenant billing/auth.

## Quick start (Docker)  
```bash
curl -fsSL https://freellmapi.co/install.sh | bash
# or manual:
git clone https://github.com/tashfeenahmed/freellmapi.git
cd freellmapi
openssl rand -hex 32 > .env   # set ENCRYPTION_KEY, PORT=3001
docker compose up -d
```
- Access dashboard at `http://localhost:3001`, add provider keys, arrange fallback chain, copy unified API key.  
- Point any OpenAI client’s `base_url` to the proxy and use the unified key.

## Additional notes  
- Desktop installer available for Windows.  
- Container binds to `127.0.0.1` by default; adjust publishing settings for remote access.  
- License: MIT; contributions welcome via PRs.