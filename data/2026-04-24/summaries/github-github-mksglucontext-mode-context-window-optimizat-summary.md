---
title: GitHub - mksglu/context-mode: Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 12 platforms · GitHub
url: https://github.com/mksglu/context-mode
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-04-24T06:02:56.627224
---

# GitHub - mksglu/context-mode: Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 12 platforms · GitHub

# Context Mode – Optimizing the AI Coding Agent’s Context Window  

## The Problem  
- MCP tool calls dump raw data directly into the model’s context (e.g., a Playwright snapshot = 56 KB, 20 GitHub issues = 59 KB, an access log = 45 KB).  
- After ~30 minutes, 40 % of the context is consumed, and compacting the conversation makes the agent forget which files are being edited, which tasks are in progress, and the last user request.  

## How Context Mode Solves It  

1. **Context Saving**  
   - Sandbox tools keep raw data out of the context.  
   - Typical 315 KB payload is reduced to 5.4 KB (≈ 98 % reduction).  

2. **Session Continuity**  
   - Every file edit, git operation, task, error, and user decision is stored in SQLite.  
   - Data is indexed with FTS5 and retrieved on demand via BM25 search, so compacting the conversation does not re‑inject large blobs.  
   - When a session ends, all indexed data is deleted, giving a clean slate for the next session.  

3. **Think in Code**  
   - The LLM should generate code to perform analysis instead of loading many files into context.  
   - One script can replace dozens of tool calls, saving up to 100× context.  
   - This paradigm is enforced across all 12 supported platforms.  

## Installation Overview  

### Claude Code (plugin marketplace, fully automatic)  
- Prerequisite: Claude Code v1.0.33+ (`claude --version`).  
- Install via plugin marketplace:  
  ```
  /plugin marketplace add mksglu/context-mode
  /plugin install context-mode@context-mode
  ```  
- Verify with `/context-mode:ctx-doctor`.  
- Automatic routing through the `SessionStart` hook; registers all hooks and six sandbox tools (`ctx_batch_execute`, `ctx_execute`, `ctx_execute_file`, `ctx_index`, `ctx_search`, `ctx_fetch_and_index`) plus meta‑tools (`ctx_stats`, `ctx_doctor`, `ctx_upgrade`, `ctx_purge`, `ctx_insight`).  

### Gemini CLI (single config file, hooks included)  
- Prerequisites: Node 18+, Gemini CLI installed.  
- Global install: `npm install -g context-mode`.  
- Add a `settings.json` entry under `~/.gemini/` that defines the MCP server and four hooks (`BeforeTool`, `AfterTool`, `PreCompress`, `SessionStart`).  
- Restart Gemini CLI and confirm with `/mcp list`.  

### VS Code Copilot (hooks with SessionStart)  
- Prerequisites: Node 18+, VS Code with Copilot Chat v0.32+.  
- Global install: `npm install -g context-mode`.  
- Create `.vscode/mcp.json` to register the server and `.github/hooks/context-mode.json` to define `PreToolUse`, `PostToolUse`, and `SessionStart` hooks.  
- Restart VS Code and test with `ctx stats` in Copilot Chat.  

### Cursor (hooks with stop support)  
- Prerequisites: Node 18+, Cursor in agent mode.  
- Global install: `npm install -g context-mode`.  
- Add `cursor/mcp.json` (or global `~/.cursor/mcp.json`) to register the server and `cursor/hooks.json` (or `~/.cursor/hooks.json`) for `PreToolUse`, `PostToolUse`, `PreCompact`, and `SessionStart` hooks.  

## Core Slash / Utility Commands  

| Command | Purpose |
|--------|---------|
| `/context-mode:ctx-stats` | Shows per‑tool token usage, savings ratio, and overall context reduction. |
| `/context-mode:ctx-doctor` | Runs diagnostics on runtimes, hooks, FTS5 availability, and plugin registration. |
| `/context-mode:ctx-upgrade` | Pulls the latest version, rebuilds, migrates cache, and fixes hooks. |
| `/context-mode:ctx-purge` | Deletes all indexed knowledge‑base content permanently. |
| `/context-mode:ctx-insight` | Opens a local web UI with a personal analytics dashboard (15+ metrics on tool usage, session activity, error rate, parallel work patterns, mastery curve). |

*On platforms without slash‑command support, the same commands can be typed directly in the chat (e.g., `ctx stats`).*  

## Alternative MCP‑Only Install (no automatic routing)  
```
claude mcp add context-mode -- npx -y context-mode
```  
- Provides the six sandbox tools without hook‑based routing, useful for trial runs before committing to full plugin integration.  

---  

**Key Takeaway:** Context Mode dramatically reduces context bloat, preserves session state, and enforces a “code‑first” workflow, making AI‑assisted coding agents far more efficient across a wide range of development environments.