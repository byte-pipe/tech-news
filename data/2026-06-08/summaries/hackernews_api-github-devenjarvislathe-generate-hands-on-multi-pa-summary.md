---
title: GitHub - devenjarvis/lathe: Generate hands-on, multi-part technical tutorials on demand, with LLM skills tuned to make content approachable. Then you...
url: https://github.com/devenjarvis/lathe
date: 2026-06-07
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-08T11:01:02.820427
---

# GitHub - devenjarvis/lathe: Generate hands-on, multi-part technical tutorials on demand, with LLM skills tuned to make content approachable. Then you...

# Lathe – Hands‑on Technical Tutorials Powered by LLMs

## What Lathe Is
- Generates single‑part or multi‑part technical tutorials on demand from any prompt.  
- Provides a purpose‑built local UI where you work through the tutorial manually.  
- Includes LLM “skills” to ask questions, verify content, and extend tutorials with new parts.  
- Allows searching, filtering, and managing a personal tutorial library.  
- Each tutorial records its sources, the model used, and the original prompt.

## Quick Start Workflow
1. Install the binary (Homebrew, install script, Go, or build from source).  
2. In a supported LLM session (Claude Code, Cursor, Codex) run a prompt such as:  
   `/lathe build a 3D Slicer in Erlang`.  
3. Open the UI from any terminal: `latge serve` (starts a web server and opens the browser).  
4. Use the UI to read, interact with, and extend the tutorial; dark mode is available.

## Installation Options
- **Homebrew (macOS, recommended)**: `brew install devenjarvis/tap/lathe` (distributed as a cask).  
- **Install script**: `curl -sSf https://raw.githubusercontent.com/devenjarvis/lathe/main/install.sh | sh`.  
- **Go**: `go install github.com/devenjarvis/lathe@latest`.  
- **From source**: clone the repo, `go build -o lathe`.  

### Installing LLM Skills
- Skills are bundled in the binary; install them into a project or user directory:  
  - `lathe skills install` → `./.claude/skills/<name>/SKILL.md`.  
  - `lathe skills install --user` → `~/.claude/skills/<name>/SKILL.md`.  
  - `lathe skills install --agent cursor` → `./.cursor/commands/<slug>.md`.  
  - `lathe skills install --agent codex` → `./.agents/skills/<name>/SKILL.md`.  
  - `lathe skills install --agent all` installs for Claude Code, Cursor, and Codex.  
- `lathe skills list` shows bundled skills.

## Motivation Behind Lathe
- Author learned programming via hands‑on homebrew projects and community tutorials.  
- Hands‑on tutorials provided the “aha” moments needed to progress from zero to competence.  
- Modern LLMs can generate code quickly but often remove the learning process.  
- Lathe aims to combine LLM generation with manual execution, recreating the learning curve while leveraging LLM expertise.  
- Useful for obscure or emerging domains lacking human‑written tutorials (e.g., 3D slicer software, embedded Zig development).

## Handling Hallucinations
- LLM‑generated tutorials are not as polished or architecturally sound as human‑written ones.  
- Lathe mitigates risks by allowing the user to interact with the LLM writer to ask questions, request fixes, or add parts.  
- Recommendation: use the most capable “thinking” model available (e.g., Opus, GPT‑5 Codex) because the task emphasizes research, design, and explanation rather than repetitive code generation.  
- The author believes hallucination risk is relatively low in this guided, interactive context.