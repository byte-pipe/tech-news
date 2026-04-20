---
title: Claude Code Unpacked
url: https://ccunpacked.dev/
site_name: hackernews_api
content_file: hackernews_api-claude-code-unpacked
fetched_at: '2026-04-01T11:24:18.949956'
original_url: https://ccunpacked.dev/
author: Claude Code Unpacked
date: '2026-04-01'
description: What actually happens when you type a message into Claude Code? The agent loop, 50+ tools, multi-agent orchestration, and unreleased features, mapped from source.
tags:
- hackernews
- trending
---

# Claude CodeUnpacked

Y
Featured on Hacker News

What actually happens when you type a message into Claude Code?The agent loop, 50+ tools, multi-agent orchestration, and unreleased features, mapped straight from the source.

0
+
Files
0
K+
Lines of Code
0
+
Tools
0
+
Commands
Start exploring
↓

01

## The Agent Loop

From keypress to rendered response, step by step through the source.

1
Input
2
Message
3
History
4
System
5
API
6
Tokens
7
Tools?
8
Loop
9
Render
10
Hooks
11
Await
1
Input
2
Message
3
History
4
System
5
API
6
Tokens
7
Tools?
8
Loop
9
Render
10
Hooks
11
Await

Watch what happens when you send a message to Claude Code

### 1User Input

src/components/TextInput.tsx

User types a message or pipes input throughstdin

●
 claude-code
$

Keyboard input comes from Ink'sTextInputcomponent. In non-interactive mode, it reads from pipedstdininstead.

1
/
11
0.5
x
1
x
2
x

02

## Architecture Explorer

Click around the source tree to explore what's inside.

Tools & Commands
Core Processing
UI Layer
Infrastructure
Support & Utilities
Personality & UX
utils
/
564
 files
components
/
389
 files
commands
/
189
 files
tools
/
184
 files
services
/
130
 files
hooks
/
104
 files
ink
/
96
 files
bridge
/
31
 files
constants
/
21
 files
skills
/
20
 files
cli
/

03

## Tool System

Every built-in tool Claude Code can call, sorted by what it does.

File Operations
6
 tools
FileRead
FileEdit
FileWrite
Glob
Grep
NotebookEdit
Execution
3
 tools
Bash
PowerShell
REPL
Search & Fetch
4
 tools
WebBrowser
🔒
WebFetch
WebSearch
ToolSearch
Agents & Tasks
11
 tools
Agent
SendMessage
TaskCreate
TaskGet
TaskList
TaskUpdate
TaskStop
TaskOutput
TeamCreate
TeamDelete
ListPeers
🔒
Planning
5
 tools
EnterPlanMode
ExitPlanMode
EnterWorktree
ExitWorktree
VerifyPlanExecution
🔒
MCP
4
 tools
mcp
ListMcpResources
ReadMcpResource
McpAuth
System
11
 tools
AskUserQuestion
TodoWrite
Skill
Config
RemoteTrigger
🔒
CronCreate
🔒
CronDelete
🔒
CronList
🔒
Snip
🔒
Workflow
🔒
TerminalCapture
🔒
Experimental
8
 tools
Sleep
Brief
StructuredOutput
🔒
LSP
🔒
SendUserFile
🔒
PushNotification
🔒
Monitor
🔒
SubscribePR
🔒

Click a tool to see details and source code


04

## Command Catalog

Every slash command available in Claude Code, sorted by what it does.

Setup & Config
12
/init
/login
/logout
/config
/permissions
/model
/theme
/terminal-setup
/doctor
/onboarding
/mcp
/hooks
Daily Workflow
24
/compact
/memory
/context
/plan
/resume
/session
/files
/add-dir
/copy
/export
/summary
/clear
/brief
/output-style
/color
/vim
/keybindings
/skills
/tasks
/agents
/fast
/effort
/extra-usage
/rate-limit-options
Code Review & Git
13
/review
/commit
/commit-push-pr
/diff
/pr_comments
/branch
/issue
/security-review
/autofix-pr
🔒
/share
/install-github-app
🔒
/install-slack-app
🔒
/tag
Debugging & Diagnostics
23
/status
/stats
/cost
/usage
/version
/feedback
/thinkback
/thinkback-play
/rewind
/ctx_viz
/debug-tool-call
/perf-issue
/heapdump
/ant-trace
/backfill-sessions
🔒
/break-cache
🔒
/bridge-kick
🔒
/mock-limits
🔒
/oauth-refresh
🔒
/reset-limits
🔒
/env
/bughunter
🔒
/passes
🔒
Advanced & Experimental
23
/advisor
/ultraplan
🔒
/bridge
🔒
/teleport
/voice
🔒
/desktop
🔒
/chrome
🔒
/mobile
🔒
/sandbox-toggle
/plugin
/reload-plugins
/remote-setup
/remote-env
/ide
/stickers
/good-claude
/btw
/upgrade
/release-notes
/privacy-settings
/help
/exit
/rename

Click a command to see details and source code


05

## Hidden Features

Stuff that's in the code but not shipped yet. Feature-flagged, env-gated, or just commented out.

### Buddy

A virtual pet that lives in your terminal. Species and rarity are derived from your account ID.

### Kairos

Persistent mode with daily logs, memory consolidation between sessions, and autonomous background actions.

### UltraPlan

Long planning sessions on Opus-class models, up to 30-minute execution windows.

### Coordinator Mode

A lead agent breaks tasks apart, spawns parallel workers in isolated git worktrees, collects results.

### Bridge

Control Claude Code from your phone or a browser. Full remote session with permission approvals.

### Daemon Mode

Run sessions in the background with--bg. Usestmuxunder the hood.

### UDS Inbox

Sessions talk to each other over Unix domain sockets.

### Auto-Dream

Between sessions, the AI reviews what happened and organizes what it learned.

Click a feature to explore
