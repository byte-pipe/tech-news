---
title: I Built a Self-Hosted AI Agent That Runs on a Raspberry Pi - DEV Community
url: https://dev.to/thegdsks/i-built-a-self-hosted-ai-agent-that-runs-on-a-raspberry-pi-161e
site_name: devto
content_file: devto-i-built-a-self-hosted-ai-agent-that-runs-on-a-rasp
fetched_at: '2026-04-06T19:26:55.590321'
original_url: https://dev.to/thegdsks/i-built-a-self-hosted-ai-agent-that-runs-on-a-raspberry-pi-161e
author: GDS K S
date: '2026-04-05'
description: profClaw is an open-source AI agent engine that runs on your hardware. 35 providers, 72 tools, 22 chat channels, and a full TUI. Tagged with ai, opensource, devtools, selfhosted.
tags: '#ai, #opensource, #devtools, #selfhosted'
---

Most AI coding tools live in someone else's cloud. Cursor, Devin, GitHub Copilot: useful, but your context and conversations flow through a third-party server. For some teams that's fine. For others it's a non-starter.

I wanted an AI agent engine I could deploy on my own hardware, connect to whatever model I wanted, and extend without waiting for a vendor to ship the feature. So I builtprofClaw.

## The problem with the current landscape

There are roughly two categories of AI dev tools right now:

Cloud-only agents(Cursor, Devin, Claude Code web, Copilot Chat): polished and easy to start, but you're locked into their infra, their model selection, and their pricing. No offline mode, no control over what gets logged.

Single-purpose CLIs(Aider, shell wrappers around OpenAI): simpler and self-hosted, but narrow. They do one thing, usually code editing, and don't compose well with the rest of your workflow.

profClaw sits in a different spot: a self-hosted, multi-provider agent engine with a proper TUI, a task queue, multi-agent orchestration, and integrations across 22 chat platforms.

## What profClaw actually is

profClaw is a Node.js agent runtime you install and run yourself. Here's the short version of what it ships with:

* 35 AI providers: Anthropic, OpenAI, Google, Ollama, Groq, DeepSeek, Bedrock, Azure, xAI, OpenRouter, Together, Fireworks, Mistral, LM Studio, and 21 more. Switch between them per-task, not per-account.
* 72 built-in tools: file operations, git, browser automation, cron scheduling, web search, canvas, voice I/O — all available to agents without writing glue code.
* 50 skills(slash commands):/commit,/review-pr,/deploy,/summarize,/web-research,/analyze-code,/ticket,/image, and more. These are composable, repeatable agent workflows you run with a single command.
* 22 chat channels: Slack, Discord, Telegram, WhatsApp, iMessage, Matrix, Teams, Google Chat, Signal, and 13 more. Your agent can receive tasks from wherever your team already works.
* MCP server: connects profClaw as a tool provider to Claude Desktop, Cursor, or any MCP-compatible client.
* Voice I/O: Whisper for speech-to-text, ElevenLabs or OpenAI TTS for responses, plus a Talk Mode for hands-free use.
* REST API + headless mode: for CI/CD pipelines and scripting.
* Plugin SDK: extend with third-party plugins via npm.

The task queue is backed by BullMQ with dead-letter queues, retry logic, and priority scheduling — not an in-memory queue that drops work if the process restarts.

Cost tracking is built in. You can set per-token budgets per provider and get alerts when you're approaching limits.

## The TUI

The interactive terminal UI is where most of my daily use happens. Streaming markdown with syntax highlighting, a slash command picker, a live model selector, and a tool execution panel that shows what the agent is doing in real time.

┌─────────────────────────────────────────────────────────────────┐
│ profClaw [claude-sonnet] [tools: 72] [$0.0023 / $5.00] │
├─────────────────────────────────────────────────────────────────┤
│ │
│ > /review-pr 142 │
│ │
│ Fetching PR #142... │
│ ✓ git fetch origin pull/142/head │
│ ✓ git diff main...FETCH_HEAD (847 lines) │
│ Running analysis... │
│ │
│ ## PR Review: feat/user-auth │
│ │
│ **Risk: Medium** │
│ │
│ The JWT signing key is read from `process.env.SECRET` without │
│ a fallback check. If the env var is missing in production... │
│ │
├─────────────────────────────────────────────────────────────────┤
│ [/] commands [tab] models [ctrl+t] tools [ctrl+v] voice │
└─────────────────────────────────────────────────────────────────┘

Enter fullscreen mode

Exit fullscreen mode

You can switch models mid-conversation without losing context. The tool panel on the right shows tool calls as they execute so you can see exactly what the agent is doing.

## The Raspberry Pi angle

This is the part people find surprising. profClaw has three deployment modes:

Mode

RAM

Use case

Pico

~140MB

Raspberry Pi Zero 2W, $5 VPS, constrained environments

Mini

~145MB

General low-resource use

Pro

Full

All features enabled

Pico mode runs the core agent loop, tool execution, and API — just without some of the heavier integrations. It fits on a Raspberry Pi Zero 2W with headroom to spare. I run a personal instance on a Pi 4 that handles Slack messages from my team and runs scheduled git tasks overnight.

It also runs on old laptops, Docker, and Android phones via Termux if you want to go that route.

## Concrete usage examples

Install and start chatting:

npm
install

-g
 profclaw
profclaw init
profclaw chat
--tui

Enter fullscreen mode

Exit fullscreen mode

One-liner install:

curl
-fsSL
 https://raw.githubusercontent.com/profclaw/profclaw/main/install.sh | bash

Enter fullscreen mode

Exit fullscreen mode

Docker:

docker run
-it

--rm

\


-v
 ~/.profclaw:/root/.profclaw
\

 ghcr.io/profclaw/profclaw:latest chat
--tui

Enter fullscreen mode

Exit fullscreen mode

Run a skill from the CLI:

profclaw run /review-pr 142
profclaw run /web-research
"best practices for database connection pooling in 2025"

profclaw run /summarize
--file
 ./meeting-notes.txt

Enter fullscreen mode

Exit fullscreen mode

Headless for CI/CD:

profclaw
exec

--prompt

"Analyze test failures in the last run and open issues for regressions"

\


--provider
 anthropic
--model
 claude-sonnet-4-5
--no-tty

Enter fullscreen mode

Exit fullscreen mode

Multi-agent routing— profClaw can route subtasks to different models based on capability scoring. Send the cheap fast model to handle file reads and the stronger model to handle reasoning:

profclaw chat
--tui

--orchestrate

Enter fullscreen mode

Exit fullscreen mode

## How it compares

Tool

Self-hosted

Multi-provider

TUI

Chat channels

Task queue

profClaw

Yes

35 providers

Yes

22

BullMQ

Claude Code

No

No

Yes (basic)

No

No

Cursor

No

Limited

No (editor)

No

No

Aider

Yes

Yes

No

No

No

Devin

No

No

No

Limited

No

Aider is the closest comparison — open source, works with multiple providers, self-hosted. The differences: profClaw has a full TUI, chat channel integrations, the task queue, voice I/O, the plugin SDK, and the MCP server. Aider is focused on code editing. profClaw is trying to be a general-purpose agent runtime.

Claude Code is the strongest single-session coding agent I've used. But it requires Anthropic's API, doesn't run a persistent server, and doesn't integrate with Slack or your other tooling. profClaw isn't trying to beat it at pair programming. It's trying to be the agent infrastructure layer that ties everything together.

## Architecture notes

Under the hood:

* Runtime: Node.js, TypeScript
* Task queue: BullMQ (Redis-backed)
* MCP: Model Context Protocol server for tool exposure to external clients
* Plugin system: npm packages with a defined SDK — install a plugin, it registers its tools and skills automatically
* Storage: local-first, your data stays on disk unless you configure otherwise
* License: AGPL-3.0

The multi-agent orchestration layer scores tasks by required capability (reasoning depth, tool use, context length) and routes to the configured model that best fits. You define the model pool; profClaw handles routing.

## Current state

This is an early open-source release. The core loop is stable — I use it daily. Some integrations are more polished than others. The plugin SDK is functional but the documentation is still thin.

If you run into issues, the GitHub issues tracker is the right place. There's also a Discord if you want to ask questions or share what you're building with it.

## Getting started

npm
install

-g
 profclaw
&&
 profclaw init
&&
 profclaw chat
--tui

Enter fullscreen mode

Exit fullscreen mode

* GitHub:github.com/profclaw/profclaw
* Docs:docs.profclaw.ai
* Site:profclaw.ai

If you're building something with it or have questions, drop them in the comments or open an issue.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
