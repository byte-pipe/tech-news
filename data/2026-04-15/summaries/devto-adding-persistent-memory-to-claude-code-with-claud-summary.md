---
title: Adding Persistent Memory to Claude Code with claude-mem — Plus a DIY Lightweight Alternative - DEV Community
url: https://dev.to/kanta13jp1/adding-persistent-memory-to-claude-code-with-claude-mem-plus-a-diy-lightweight-alternative-4gha
date: 2026-04-13
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-04-15T06:03:42.196879
---

# Adding Persistent Memory to Claude Code with claude-mem — Plus a DIY Lightweight Alternative - DEV Community

# Adding Persistent Memory to Claude Code with claude‑mem — Plus a DIY Lightweight Alternative

## The Problem
- Claude Code forgets everything between sessions, forcing repeated reminders about project specifics (e.g., Supabase vs. Firebase, folder structure, dummy data).

## What is claude‑mem?
- A GitHub plugin (thedotmack/claude‑mem) that gives Claude Code long‑term memory.
- Captures actions during a session and injects relevant context into future conversations.

### Architecture
- Five lifecycle hooks: SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd.
- Hybrid search using SQLite (keyword) + Chroma (vector similarity).
- Runs as a Bun HTTP worker on `localhost:37777`.
- MCP tools provide three‑layer progressive disclosure (search → timeline → get_observations).
- Web UI for visual memory browsing.

### Installation
```bash
npx claude-mem install
npx claude-mem start   # requires Bun
```

## The DIY Alternative I Built First
- Implemented with two PowerShell scripts hooked into Claude Code’s native hooks API.

### PostToolUse Hook (`auto-capture.ps1`)
- Fires after every Bash or Write tool use.
- Logs git commits and newly created files to a daily markdown file (`memory/auto-capture/YYYY-MM-DD.md`).

### SessionStart Hook (`session-resume.ps1`)
- Reads the last three days of capture files and injects them as context at session start.

### Registration in `settings.json`
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Bash|Write",
      "hooks": [{ "type": "command", "command": "powershell -File auto-capture.ps1" }]
    }],
    "SessionStart": [{
      "hooks": [{ "type": "command", "command": "powershell -File session-resume.ps1" }]
    }]
  }
}
```

## Head‑to‑Head Comparison

| Feature            | claude‑mem                              | DIY Hooks                              |
|--------------------|----------------------------------------|----------------------------------------|
| Setup              | `npx install` (one command)            | Two scripts, manual configuration      |
| Auto‑capture       | All tool usage                         | Only git commits and Write tool         |
| Search             | Vector similarity + keyword            | Simple grep (text search)              |
| Web UI             | `localhost:37777`                     | None                                    |
| Dependencies       | Bun, SQLite, Chroma                    | None                                    |
| Token cost         | LLM compression (Claude/Gemini)        | Zero                                    |
| Git‑friendly       | DB file (git‑ignored)                  | Markdown files (shareable)             |
| Multi‑instance     | Session‑scoped isolation                | File sharing for coordination          |

## Running Both Together
- They coexist without conflict: claude‑mem registers as a plugin, DIY hooks live in `settings.json`.

### When claude‑mem shines
- Smart LLM compression of tool outputs.
- Semantic search across sessions (e.g., “What did I do with the auth system last week?”).
- Visual dashboard for captured observations.

### When DIY hooks shine
- Zero external dependencies.
- Memory files can be committed to Git and shared across team members.
- Full control over what is captured.
- No token consumption.

## Cost‑Optimization Tip
- claude‑mem defaults to Claude API for compression (uses tokens).
- Switch to free Gemini provider:

```json
// ~/.claude-mem/settings.json
{
  "CLAUDE_MEM_PROVIDER": "gemini",
  "CLAUDE_MEM_GEMINI_API_KEY": "your‑free‑key‑from‑aistudio.google.com"
}
```

## Our 3‑Layer Memory Architecture
| Layer | Tool                | Purpose |
|------|---------------------|---------|
| L1: Intra‑session | claude‑mem (SQLite) | Auto‑record all tool usage, semantic search within a session |
| L2: Inter‑session | DIY hooks (markdown) | Persist git commit history, share across instances |
| L3: Cross‑project | NotebookLM Master Brain | Deep research and long‑term architectural knowledge |

## Verdict
- claude‑mem transforms Claude Code from a disposable tool into a growing partner, thanks to semantic vector search and a handy Web UI.
- For teams that need zero dependencies, zero token cost, and Git‑friendly sharing, the DIY hook approach is a solid starter.
- Recommended workflow: begin with DIY hooks for minimal memory, then add claude‑mem when semantic search and automatic compression become necessary.
