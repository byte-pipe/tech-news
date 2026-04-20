---
title: Stop Burning Your Context Window — We Built Context Mode | Mert Köseoğlu
url: https://mksg.lu/blog/context-mode
date: 2026-02-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-01T10:17:26.507587
---

# Stop Burning Your Context Window — We Built Context Mode | Mert Köseoğlu

# Stop Burning Your Context Window — We Built Context Mode

## The Problem
- MCP tool calls dump raw data into Claude Code’s 200 K token context window.
- Typical outputs (Playwright snapshot, GitHub issues, logs) consume tens of kilobytes each.
- With 81+ tools active, 72 % of tokens are used before the first user message, leading to rapid context exhaustion (≈30 min sessions).

## How the Sandbox Works
- Each `execute` call runs in an isolated subprocess with its own memory space.
- Only the subprocess’s stdout is injected into the conversation; raw data stays in the sandbox.
- Supports ten runtimes (JS/TS, Python, Shell, Ruby, Go, Rust, PHP, Perl, R); Bun auto‑detects for faster JS/TS.
- Authenticated CLIs (gh, aws, gcloud, kubectl, docker) inherit credentials via environment passthrough without exposing them to the model.

## How the Knowledge Base Works
- `index` tool chunks markdown by headings, preserving code blocks, and stores them in a SQLite FTS5 virtual table.
- Uses BM25 ranking with Porter stemming for relevance.
- `search` returns exact code blocks with heading hierarchy, not summaries.
- `fetch_and_index` extends indexing to URLs by converting HTML to markdown; raw pages never enter the context.

## The Numbers
- Across 11 real‑world scenarios, output size drops to under 1 KB each.
  - Playwright snapshot: 56 KB → 299 B
  - 20 GitHub issues: 59 KB → 1.1 KB
  - Access log (500 requests): 45 KB → 155 B
  - Analytics CSV (500 rows): 85 KB → 222 B
  - Git log (153 commits): 11.6 KB → 107 B
  - Repo research (sub‑agent): 986 KB → 62 KB (5 calls vs 37)
- Full session compression: 315 KB raw output → 5.4 KB.
- Session duration before slowdown extends from ~30 min to ~3 h; after 45 min, 99 % of context remains versus 60 % without Context Mode.

## Install
- **Plugin Marketplace** (auto‑routing hooks, slash commands):
  ```
  /plugin marketplace add mksglu/claude-context-mode
  /plugin install context-mode@claude-context-mode
  ```
- **MCP‑only** (tools only):
  ```
  claude mcp add context-mode -- npx -y context-mode
  ```
- Restart Claude Code to activate.

## What Actually Changes
- No workflow changes required.
- A `PreToolUse` hook automatically routes all tool outputs through the sandbox.
- Sub‑agents adopt `batch_execute` as their primary tool; Bash sub‑agents gain general‑purpose capabilities to access MCP tools.
- Result: context window no longer fills up, allowing sessions to run up to 3 hours on the same 200 K token budget.

## Why We Built This
- As maintainer of the MCP Directory & Hub (100 K+ daily requests), I observed that every tool dumps raw data into context, while no solution existed for the output side.
- Inspired by Cloudflare’s Code Mode (compressing tool definitions), we applied the same principle to tool outputs.
- Built initially for my own Claude Code sessions, achieving a 6× longer usable session time.
- Open‑sourced under MIT: https://github.com/mksglu/claude-context-mode

*Mert Köseoğlu, Senior Software Engineer, AI consultant*
