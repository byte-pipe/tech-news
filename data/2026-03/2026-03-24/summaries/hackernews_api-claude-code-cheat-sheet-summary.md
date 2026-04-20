---
title: Claude Code Cheat Sheet
url: https://cc.storyfox.cz
date: 2026-03-24
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-24T20:02:31.161536
---

# Claude Code Cheat Sheet

# Claude Code Cheat Sheet Summary

## Keyboard Shortcuts
- **General Controls**
  - `Ctrl+C`: Cancel input/generation
  - `Ctrl+D`: Exit session
  - `Ctrl+L`: Clear screen
  - `Ctrl+O`: Toggle verbose output
  - `Ctrl+R`: Reverse search history
  - `Ctrl+G`: Open prompt in editor
  - `Ctrl+B`: Background running task
  - `Ctrl+T`: Toggle task list
  - `Ctrl+V`: Paste image
  - `Ctrl+F`: Kill background agents (×2)
  - `Esc Esc`: Rewind / undo

- **Mode Switching**
  - `Shift+Tab`: Cycle permission modes
  - `Alt+P`: Switch model
  - `Alt+T`: Toggle thinking

- **Input**
  - `\` + `Enter`: Newline (quick)
  - `Ctrl+J`: Newline (control sequence)

- **Navigation & UI**
  - Arrow keys: Navigate, expand/collapse
  - `P`: Preview
  - `R`: Rename
  - `/`: Search

## MCP Server Management
- **Adding Servers**
  - `--transport http`: Remote HTTP (recommended)
  - `--transport stdio`: Local process
  - `--transport sse`: Remote SSE

- **Scopes**
  - Local: `~/.claude.json` (per project)
  - Project: `.mcp.json` (shared/VCS)
  - User: `~/.claude.json` (global)

- **Commands**
  - `/mcp`: Interactive UI
  - `claude mcp list`: List all servers
  - `claude mcp serve`: Run as MCP server

## Slash Commands
- **Session**
  - `/clear`, `/compact [focus]`, `/resume`, `/rename [name]`, `/branch [name]`, `/cost`, `/context`, `/diff`, `/copy`, `/export`

- **Config**
  - `/config`, `/model [model]`, `/fast [on|off]`, `/vim`, `/theme`, `/permissions`, `/effort [level]`, `/color [color]`

- **Tools**
  - `/init`, `/memory`, `/mcp`, `/hooks`, `/skills`, `/agents`, `/chrome`, `/reload-plugins`

- **Special**
  - `/btw <question>`, `/plan [desc]`, `/loop [interval]`, `/voice`, `/doctor`, `/rc`, `/pr-comments [PR]`, `/stats`, `/insights`, `/desktop`, `/remote-control`, `/stickers`

## Memory & Files
- **CLAUDE.md Locations**
  - Project: `./CLAUDE.md`
  - Personal: `~/.claude/CLAUDE.md`
  - Org‑wide: `/etc/claude-code/`

- **Rules & Import**
  - Project rules: `.claude/rules/*.md`
  - User rules: `~/.claude/rules/*.md`
  - Path‑specific rules via frontmatter `paths:`

- **Auto Memory**
  - `~/.claude/projects/<proj>/memory/` contains `MEMORY.md` and topic files, auto‑loaded

## Workflows & Tips
- **Plan Mode**
  - `Shift+Tab` cycles Normal → Auto → Plan
  - Start with `--permission-mode plan`

- **Thinking & Effort**
  - `Alt+T` toggles thinking
  - `Ctrl+O` shows verbose thinking
  - Effort levels: low, medium, high (`/effort`)

- **Git Worktrees**
  - `--worktree name` creates isolated branch per feature
  - `sparsePaths` for checkout of needed directories
  - `/batch` auto‑creates worktrees

- **Voice Mode**
  - `/voice` enables push‑to‑talk (hold Space)
  - Supports 20 languages (EN, ES, FR, …)

- **Context Management**
  - `/context` shows usage & optimization tips
  - `/compact [focus]` compresses context (auto‑compact ~95% capacity)
  - 1 M token context with Opus 4.6 (Max/Team/Ent)

## Configuration & Environment
- **Config Files**
  - User: `~/.claude/settings.json`
  - Project: `.claude/settings.json` & `.claude/settings.local.json`
  - Global state/OAuth: `~/.claude.json`
  - Project MCP servers: `.mcp.json`

- **Key Settings**
  - `modelOverrides`, `autoMemoryDirectory`, `worktree.sparsePaths`

- **Environment Variables**
  - `ANTHROPIC_API_KEY`, `ANTHROPIC_MODEL`
  - `CLAUDE_CODE_EFFORT_LEVEL` (low/med/high)
  - `MAX_THINKING_TOKENS`, `ANTHROPIC_CUSTOM_MODEL_OPTION`
  - `CLAUDE_CODE_PLUGIN_SEED_DIR`

## Skills & Agents
- **Built‑in Skills**
  - `/simplify` (code review), `/batch` (large parallel changes), `/debug`, `/loop`, `/claude-api`

- **Custom Skill Locations**
  - Project: `.claude/skills/<name>/`
  - Personal: `~/.claude/skills/<name>/`

- **Skill Frontmatter**
  - `description`, `allowed-tools`, `model`, `effort`, `context: fork`, `$ARGUMENTS`, `${CLAUDE_SKILL_DIR}`, dynamic injection with ``!`cmd` ``

- **Built‑in Agents**
  - `Explore` (fast read‑only), `Plan` (research), `General` (full tools), `Bash` (terminal)

- **Agent Frontmatter**
  - `permissionMode`, `isolation: worktree`, `memory`, `background`, `maxTurns`, `SendMessage`

## CLI & Flags
- **Core Commands**
  - `claude` (interactive)
  - `claude "q"` (prompt)
  - `claude -p "q"` (headless)
  - `claude -c` (continue last)
  - `claude -r "name"` (resume)
  - `claude update` (update)

- **Key Flags**
  - `--model`, `-w` (git worktree), `-n/--name`, `--add-dir`, `--agent`, `--allowedTools`, `--output-format`, `--json-schema`, `--max-turns`, `--max-budget-usd`, `--console`, `--verbose`, `--bare`, `--channels`, `--remote`, `--chrome`

- **Usage Examples**
  - `claude -p "query"` for non‑interactive calls
  - `cat file | claude -p` to pipe input
  - `claude -c` to continue the last conversation
  - `claude -r "name"` to resume a named session

This summary captures the essential shortcuts, commands, configuration options, and workflow tips needed to work efficiently with Claude Code.
