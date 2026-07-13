---
title: Claude Code Sends 4.7x More Tokens Than OpenCode Before Reading Your Prompt | Systima Blog
url: https://systima.ai/blog/claude-code-vs-opencode-token-overhead
date: 2026-07-13
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-13T12:29:08.274857
---

# Claude Code Sends 4.7x More Tokens Than OpenCode Before Reading Your Prompt | Systima Blog

# Claude Code Sends 4.7x More Tokens Than OpenCode Before Reading Your Prompt

## Why the measurement matters
- Token overhead directly impacts cost, latency, and the usable context window.  
- In production, especially under regulations like the EU AI Act, knowing exactly what an agent sends is essential.

## Methodology
- Inserted a logging proxy between each harness (Claude Code 2.1.207, OpenCode 1.17.18) and the model endpoint.  
- Captured the full JSON payload (system prompt, tool schemas, messages) and the API usage block (input tokens, cache reads/writes, output tokens).  
- Tested on a fresh configuration, then added variables (instruction files, MCP servers, sub‑agents).  
- Tasks:
  1. **T1** – simple “OK” reply (fixed overhead).  
  2. **T2** – read a file and summarize it.  
  3. **T3** – write‑run‑test‑fix loop (FizzBuzz).  
- Subtracted a constant 6,200‑token envelope added by the local LLM gateway.

## Key findings

### 1. Fixed overhead (T1)
- **Claude Code**: ~32,800 tokens total.  
  - System prompt ≈ 27 k chars (3 blocks).  
  - Tool schemas ≈ 27 tools, ≈ 100 k chars.  
  - First‑message scaffolding ≈ 8 k chars.  
- **OpenCode**: ~6,900 tokens total.  
  - System prompt ≈ 9 k chars (1 block).  
  - Tool schemas ≈ 10 tools, ≈ 21 k chars.  
- Tool definitions dominate both payloads; Claude Code’s are ~4× larger.

### 2. Zero‑tool baseline
- Removing all tools isolates the system prompt.  
- Claude Code: ~6.5 k tokens.  
- OpenCode: ~2.0 k tokens.  
- Even without tools, Claude Code’s instruction set is >3× larger (tone, safety, task‑management rules).

### 3. Cache efficiency
- OpenCode’s request prefix is byte‑identical across runs, allowing a single cache write per session and cheap reads.  
- Claude Code rewrites tens of thousands of cache‑tokens each turn, writing up to **54×** more cache tokens than OpenCode.  
- Cache writes are billed at a premium, inflating Claude Code’s usage dashboard.

### 4. Configuration bloat
- Production instruction file (≈72 KB) adds ~20 k tokens per request.  
- Five modest MCP servers contribute another 5–7 k tokens.  
- A real deployment can start a request with **75–85 k** tokens before any user input.

### 5. Sub‑agent cost
- A task that costs 121 k tokens when run directly jumps to **513 k** tokens when fanned out to two sub‑agents, because each sub‑agent incurs its own bootstrap cost and the parent consumes the transcript.

### 6. Multi‑step task where Claude Code wins (T3)
- Claude Code batches all tool calls into a single parallel request (3 model calls total).  
- OpenCode makes one tool call per turn (9 model calls total).  
- Cumulative input tokens:  
  - Claude Code ≈ 121 k tokens.  
  - OpenCode ≈ 132 k tokens.  
- Because the baseline payload is re‑sent each turn, a large‑baseline harness that batches aggressively can match or beat a small‑baseline harness that serialises.

## Overall conclusion
- Claude Code’s baseline (system prompt + tool schemas) is **3–5×** larger than OpenCode’s, leading to higher token consumption on most tasks.  
- Claude Code is far less cache‑efficient, writing many more cache tokens and incurring higher billed usage.  
- Configuration files and sub‑agents further amplify Claude Code’s token overhead.  
- The only scenario where Claude Code can be cheaper is when it aggressively batches tool calls, reducing the number of requests and thus the number of baseline retransmissions.  

Understanding these token dynamics is crucial for cost‑effective, compliant deployment of agentic AI systems.