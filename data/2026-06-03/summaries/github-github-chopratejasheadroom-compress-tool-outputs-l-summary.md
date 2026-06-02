---
title: GitHub - chopratejas/headroom: Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, same answers. Librar...
url: https://github.com/chopratejas/headroom
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-06-03T01:53:54.772454
---

# GitHub - chopratejas/headroom: Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, same answers. Librar...

# Headroom – Context Compression Layer for AI Agents

## Overview
- Compresses tool outputs, logs, files, RAG chunks, and conversation history before they reach LLMs.  
- Reduces token count by 60–95 % while preserving answer quality.  
- Provides a library, a proxy, an MCP server, and cross‑agent memory.

## Core Capabilities
- Library: `compress(messages)` for Python or TypeScript, usable inline in any application.  
- Proxy: `headroom proxy --port 8787` – zero‑code changes, works with any language.  
- Agent wrap: `headroom wrap <agent>` – wraps Claude, Codex, Cursor, Aider, Copilot, etc., in a single command.  
- MCP server: `headroom_compress`, `headroom_retrieve`, `headroom_stats` for any MCP client.  
- Cross‑agent memory: shared store with automatic deduplication across agents.  
- Learn: mines failed sessions and writes corrections to `CLAUDE.md` / `AGENTS.md`.  
- Reversible compression (CCR): originals are kept locally; the LLM can retrieve them on demand.

## Architecture (30‑second flow)
1. Agent or application produces prompts, tool outputs, logs, RAG results, files.  
2. Headroom (runs locally) processes the data through:  
   - ContentRouter – detects content type and selects the appropriate compressor.  
   - SmartCrusher (JSON), CodeCompressor (AST), Kompress‑base (text/HF).  
   - CacheAligner – stabilizes prefixes so provider KV caches hit.  
   - CCR – stores originals for later retrieval.  
3. The compressed payload is sent to the LLM provider (Anthropic, OpenAI, Bedrock, …).

## Quick Start (≈60 seconds)
1. Install  
   ```bash
   pip install "headroom-ai[all]"
   npm install headroom-ai
   ```
2. Choose a mode  
   - `headroom wrap claude` – wrap a coding agent.  
   - `headroom proxy --port 8787` – drop‑in proxy, zero code changes.  
   - Or import `compress` directly in code.  
3. View token savings: `headroom stats`.

## Performance Evidence
| Workload                | Tokens Before | Tokens After | Savings |
|-------------------------|---------------|--------------|---------|
| Code search (100 results) | 17,765 | 1,408 | 92 % |
| SRE incident debugging   | 65,694 | 5,118 | 92 % |
| GitHub issue triage       | 54,174 | 14,761 | 73 % |
| Codebase exploration      | 78,502 | 41,254 | 47 % |

Accuracy on standard benchmarks remains unchanged (e.g., GSM8K 0.870 → 0.870, TruthfulQA +0.030).

## Agent Compatibility
- Claude Code, Codex (shares memory with Claude), Cursor, Aider, Copilot CLI, OpenClaw.  
- Any OpenAI‑compatible client works via the proxy.  
- MCP‑native clients via `headroom mcp install`.

## When to Use / When to Skip
**Use if** you run AI coding agents daily, want token savings without code changes, need shared memory, or require reversible compression.  
**Skip if** you rely solely on a single provider’s native compaction or operate in a sandboxed environment where local processes cannot run.

## Integration Points
- Python / TypeScript libraries: `compress(messages, model=…)`.  
- Anthropic / OpenAI SDK wrappers: `withHeadroom(new Anthropic())`.  
- Vercel AI SDK middleware, LiteLLM callbacks, LangChain, Agno, Strands, ASGI middleware.  
- Multi‑agent shared context via `SharedContext().put/.get`.  
- MCP clients via `headroom mcp install`.

## Internal Components
- SmartCrusher – universal JSON compressor.  
- CodeCompressor – AST‑aware for Python, JavaScript, Go, Rust, Java, C++.  
- Kompress‑base – HuggingFace model trained on agentic traces.  
- Image compression – 40–90 % reduction via trained ML router.  
- CacheAligner – stabilizes prefixes for better KV‑cache hits.  
- IntelligentContext – score‑based context fitting with learned importance.  
- CCR – reversible compression with on‑demand retrieval.  
- Cross‑agent memory, SharedContext, headroom learn plugin.