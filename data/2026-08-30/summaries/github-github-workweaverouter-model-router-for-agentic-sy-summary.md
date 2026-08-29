---
title: GitHub - workweave/router: Model router for agentic systems. Routes every prompt to the right model in <50ms. Cut costs 40-70% with just an endpoint c...
url: https://github.com/workweave/router
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-08-30T06:01:30.531660
---

# GitHub - workweave/router: Model router for agentic systems. Routes every prompt to the right model in <50ms. Cut costs 40-70% with just an endpoint c...

# workweave/router – Model router for agentic systems

## Overview
- Drop‑in proxy for Anthropic, OpenAI, Gemini, and many open‑source LLMs.  
- Routes each request to the most suitable model in <50 ms using an on‑box embedder (cluster scorer).  
- Cuts LLM costs by 40‑70 % by selecting the cheapest adequate model.  
- Provider API keys stay on‑premise, encrypted (BYOK).  

## Core Features
- Per‑action routing: selects a model for every upstream API request, not per session.  
- Unified API: supports Anthropic messages, OpenAI chat completions, Gemini native, streaming, tools, vision, etc.  
- Broad model support: DeepSeek, Kimi, GLM, Qwen, Llama, Mistral via OpenRouter or any OpenAI‑compatible endpoint.  
- Observability: OTLP traces exported out of the box; viewable in the local dashboard or external systems (Honeycomb, Datadog, Grafana).  

## 30‑second Quick‑start
```bash
npx @workweave/router
```
- Installer asks which client (Claude Code, Codex, opencode, pi) and scope (user vs project), obtains a router key, and writes the config file.  
- Flags for specific clients, local self‑host, custom base URL, version pinning, etc.  
- Requires Node ≥ 18 (Claude Code, opencode, pi also need `jq`).  

## Self‑hosted Deployment
1. Add a provider key (e.g., OpenRouter) to `.env.local`:
   ```
   OPENROUTER_API_KEY=sk-or-v1-...
   ```
2. Start Postgres and the router, seed an `rk_` key:
   ```bash
   make full-setup
   ```
3. Router runs at `http://localhost:8080`; dashboard at `http://localhost:8080/ui/` (admin/password).  
4. Example calls:  

   ```bash
   curl -sS http://localhost:8080/v1/messages \
        -H "Authorization: Bearer rk_..." \
        -d '{"model":"claude-sonnet-4-5","max_tokens":256,"messages":[{"role":"user","content":"hi"}]}'
   ```

   ```bash
   curl -sS http://localhost:8080/v1/chat/completions \
        -H "Authorization: Bearer rk_..." \
        -d '{"model":"gpt-4o-mini","messages":[{"role":"user","content":"hi"}]}'
   ```

5. Inspect routing decision without proxying via `/v1/route`.  

## Architecture (textual flow)
- **Client** → Router (`/v1/messages`, `/v1/chat/completions`, `/v1/route`)  
- Router embeds request, scores with **Cluster Scorer** (ONNX embedder)  
- Optional **HMM policy sidecar** (`:8093`)  
- Auth, config, usage stored in **Postgres** (encrypted keys)  
- Provider keys supplied from env or BYOK → external LLM providers  
- OTLP spans sent to external collector (Honeycomb, Datadog, Grafana)  
- Dashboard UI for self‑hosted mode only  

## Optional HMM Policy Sidecar
- Add `GOOGLE_API_KEY=...` to `.env.local` and run `make up-hmm`.  
- Runs a frozen Hidden Markov Model policy in a separate container; does not replace the default scorer.  

## Integration with Tools
- **Claude Code** – `make install-ccto` wires the router automatically.  
- **Codex (OpenAI CLI)** – `npx @workweave/router --codex` patches `~/.codex/config.toml` with `model_provider = "weave"` and adds custom Codex skills for forcing models, checking router status, and enabling/disabling routing.  
- **opencode** – similar patching via `--opencode`.  
- **pi + Loom UI** – `--pi` flag sets up routing for the Pi tool.  

## License & Contributions
- Open source under the repository’s LICENSE.  
- Contributions welcomed; see `CONTRIBUTING.md`.