---
title: Claude Code Cheat Sheet
url: https://cc.storyfox.cz
site_name: hackernews_api
content_file: hackernews_api-claude-code-cheat-sheet
fetched_at: '2026-03-24T20:00:15.980692'
original_url: https://cc.storyfox.cz
author: phasE89
date: '2026-03-24'
description: Claude Code Cheat Sheet
tags:
- hackernews
- trending
---

⌨️ Keyboard Shortcuts

General Controls

Ctrl
C
 
Cancel input/generation

Ctrl
D
 
Exit session

Ctrl
L
 
Clear screen

Ctrl
O
 
Toggle verbose output

Ctrl
R
 
Reverse search history

Ctrl
G
 
Open prompt in editor

Ctrl
B
 
Background running task

Ctrl
T
 
Toggle task list

Ctrl
V
 
Paste image

Ctrl
F
 
Kill background agents (×2)

Esc
Esc
 
Rewind / undo

Mode Switching

Shift
Tab
 
Cycle permission modes

Alt
P
 
Switch model

Alt
T
 
Toggle thinking

Input

\
Enter
 
Newline (quick)

Ctrl
J
 
Newline (control seq)

Prefixes

/
 
Slash command

!
 
Direct bash

@
 
File mention + autocomplete

Session Picker

↑↓
 
Navigate

←→
 
Expand/collapse

P
 
Preview

R
 
Rename

/
 
Search

A
 
All projects

B
 
Current branch

🔌 MCP Servers

Add Servers

--transport http
 
Remote HTTP (recommended)

--transport stdio
 
Local process

--transport sse
 
Remote SSE

Scopes

Local
 
~/.claude.json (per project)

Project
 
.mcp.json (shared/VCS)

User
 
~/.claude.json (global)

Manage

/mcp
 
Interactive UI

claude mcp list
 
List all servers

claude mcp serve
 
CC as MCP server

Elicitation
 
Servers request input mid-task
NEW

⚡ Slash Commands

Session

/clear
 
Clear conversation

/compact [focus]
 
Compact context

/resume
 
Resume/switch session

/rename [name]
 
Name current session

/branch [name]
 
Branch conversation (/fork alias)

/cost
 
Token usage stats

/context
 
Visualize context (grid)

/diff
 
Interactive diff viewer

/copy
 
Copy last response

/export
 
Export conversation

Config

/config
 
Open settings

/model [model]
 
Switch model (←→ effort)

/fast [on|off]
 
Toggle fast mode

/vim
 
Toggle vim mode

/theme
 
Change color theme

/permissions
 
View/update permissions

/effort [level]
 
Set effort (low/med/high)
NEW

/color [color]
 
Set prompt-bar color

Tools

/init
 
Create CLAUDE.md

/memory
 
Edit CLAUDE.md files

/mcp
 
Manage MCP servers

/hooks
 
Manage hooks

/skills
 
List available skills

/agents
 
Manage agents

/chrome
 
Chrome integration

/reload-plugins
 
Hot-reload plugins

Special

/btw <question>
 
Side question (no context)

/plan [desc]
 
Plan mode (+ auto-start)

/loop [interval]
 
Schedule recurring task

/voice
 
Push-to-talk voice (20 langs)

/doctor
 
Diagnose installation

/rc
 
Enable remote control

/pr-comments [PR]
 
Fetch GitHub PR comments

/stats
 
Usage streaks & prefs

/insights
 
Analyze sessions report

/desktop
 
Continue in Desktop app

/remote-control
 
Bridge terminal to claude.ai/code
NEW

/stickers
 
Order stickers! 🎉

📁 Memory & Files

CLAUDE.md Locations

./CLAUDE.md
 
Project (team-shared)

~/.claude/CLAUDE.md
 
Personal (all projects)

/etc/claude-code/
 
Managed (org-wide)

Rules & Import

.claude/rules/*.md
 
Project rules

~/.claude/rules/*.md
 
User rules

paths: frontmatter
 
Path-specific rules

@path/to/file
 
Import in CLAUDE.md

Auto Memory

~/.claude/projects/<proj>/memory/

MEMORY.md + topic files, auto-loaded

🧠 Workflows & Tips

Plan Mode

Shift
Tab
 
Normal → Auto → Plan

--permission-mode plan
 
Start in plan mode

Thinking & Effort

Alt
T
 
Toggle thinking on/off

"ultrathink"
 
Max effort for turn

Ctrl
O
 
See thinking (verbose)

/effort
 
○ low · ◐ med · ● high
NEW

Git Worktrees

--worktree name
 
Isolated branch per feature

isolation: worktree
 
Agent in own worktree

sparsePaths
 
Checkout only needed dirs
NEW

/batch
 
Auto-creates worktrees

Voice Mode

/voice
 
Enable push-to-talk

Space
 (hold)
 
Record, release to send

20 languages
 
EN, ES, FR, DE, CZ, PL…

Context Management

/context
 
Usage + optimization tips

/compact [focus]
 
Compress with focus

Auto-compact
 
~95% capacity

1M context
 
Opus 4.6 (Max/Team/Ent)

CLAUDE.md
 
Survives compaction!

Session Power Moves

claude -c
 
Continue last conv

claude -r "name"
 
Resume by name

/btw question
 
Side Q, no context cost

SDK / Headless

claude -p "query"
 
Non-interactive

--output-format json
 
Structured output

--max-budget-usd 5
 
Cost cap

cat file | claude -p
 
Pipe input

Scheduling & Remote

/loop 5m msg
 
Recurring task

/rc
 
Remote control

--remote
 
Web session on claude.ai

⚙️ Config & Env

Config Files

~/.claude/settings.json
 
User settings

.claude/settings.json
 
Project (shared)

.claude/settings.local.json
 
Local only

~/.claude.json
 
OAuth, MCP, state

.mcp.json
 
Project MCP servers

Key Settings

modelOverrides
 
Map model picker → custom IDs

autoMemoryDirectory
 
Custom memory dir

worktree.sparsePaths
 
Sparse checkout dirs
NEW

Key Env Vars

ANTHROPIC_API_KEY

ANTHROPIC_MODEL

CLAUDE_CODE_EFFORT_LEVEL
 
low/med/high

MAX_THINKING_TOKENS
 
0=off

ANTHROPIC_CUSTOM_MODEL_OPTION
 
Custom /model entry

CLAUDE_CODE_PLUGIN_SEED_DIR
 
Multiple plugin seed dirs

🔧 Skills & Agents

Built-in Skills

/simplify
 
Code review (3 parallel agents)

/batch
 
Large parallel changes (5-30 worktrees)

/debug [desc]
 
Troubleshoot from debug log

/loop [interval]
 
Recurring scheduled task

/claude-api
 
Load API + SDK reference

Custom Skill Locations

.claude/skills/<name>/
 
Project skills

~/.claude/skills/<name>/
 
Personal skills

Skill Frontmatter

description
 
Auto-invocation trigger

allowed-tools
 
Skip permission prompts

model
 
Override model for skill

effort
 
Override effort level
NEW

context: fork
 
Run in subagent

$ARGUMENTS
 
User input placeholder

${CLAUDE_SKILL_DIR}
 
Skill's own directory

!`cmd`
 
Dynamic context injection

Built-in Agents

Explore
 
Fast read-only (Haiku)

Plan
 
Research for plan mode

General
 
Full tools, complex tasks

Bash
 
Terminal separate context

Agent Frontmatter

permissionMode
 
default/acceptEdits/dontAsk/plan

isolation: worktree
 
Run in git worktree

memory: user|project
 
Persistent memory

background: true
 
Background task

maxTurns
 
Limit agentic turns

SendMessage
 
Resume agents (replaces resume)
NEW

🖥️ CLI & Flags

Core Commands

claude
 
Interactive

claude "q"
 
With prompt

claude -p "q"
 
Headless

claude -c
 
Continue last

claude -r "n"
 
Resume

claude update
 
Update

Key Flags

--model
 
Set model

-w
 
Git worktree

-n / --name
 
Session name

--add-dir
 
Add dir

--agent
 
Use agent

--allowedTools
 
Pre-approve

--output-format
 
json/stream

--json-schema
 
Structured

--max-turns
 
Limit turns

--max-budget-usd
 
Cost cap

--console
 
Auth via Anthropic Console

--verbose
 
Verbose

--bare
 
Minimal headless (no hooks/LSP)
NEW

--channels
 
Permission relay / MCP push
NEW

--remote
 
Web session

--chrome
 
Chrome