---
title: 'GitHub - Yeachan-Heo/oh-my-claudecode: Teams-first Multi-agent orchestration for Claude Code · GitHub'
url: https://github.com/Yeachan-Heo/oh-my-claudecode
site_name: github
content_file: github-github-yeachan-heooh-my-claudecode-teams-first-mul
fetched_at: '2026-03-26T11:22:34.490476'
original_url: https://github.com/Yeachan-Heo/oh-my-claudecode
author: Yeachan-Heo
description: Teams-first Multi-agent orchestration for Claude Code - Yeachan-Heo/oh-my-claudecode
---

Yeachan-Heo



/

oh-my-claudecode

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork803
* Star11.9k




 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

2,039 Commits
2,039 Commits
.claude-plugin
.claude-plugin
 
 
.github
.github
 
 
agents
agents
 
 
assets
assets
 
 
benchmark
benchmark
 
 
benchmarks
benchmarks
 
 
bridge
bridge
 
 
dist
dist
 
 
docs
docs
 
 
examples
examples
 
 
hooks
hooks
 
 
research
research
 
 
scripts
scripts
 
 
seminar
seminar
 
 
skills
skills
 
 
src
src
 
 
templates
templates
 
 
tests/
fixtures/
typescript-pnpm
tests/
fixtures/
typescript-pnpm
 
 
.eslintignore
.eslintignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.mcp.json
.mcp.json
 
 
.npmignore
.npmignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.de.md
README.de.md
 
 
README.es.md
README.es.md
 
 
README.fr.md
README.fr.md
 
 
README.it.md
README.it.md
 
 
README.ja.md
README.ja.md
 
 
README.ko.md
README.ko.md
 
 
README.md
README.md
 
 
README.pt.md
README.pt.md
 
 
README.ru.md
README.ru.md
 
 
README.tr.md
README.tr.md
 
 
README.vi.md
README.vi.md
 
 
README.zh.md
README.zh.md
 
 
eslint.config.js
eslint.config.js
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
typos.toml
typos.toml
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

English |한국어|中文|日本語|Español|Tiếng Việt|Português

# oh-my-claudecode

For Codex users:Check outoh-my-codex— the same orchestration experience for OpenAI Codex CLI.

Multi-agent orchestration for Claude Code. Zero learning curve.

Don't learn Claude Code. Just use OMC.

Get Started•Documentation•CLI Reference•Workflows•Migration Guide•Discord

## Quick Start

Step 1: Install

/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode
/plugin install oh-my-claudecode

Step 2: Setup

/setup
/omc-setup

Step 3: Build something

autopilot: build a REST API for managing tasks

That's it. Everything else is automatic.

### Not Sure Where to Start?

If you're uncertain about requirements, have a vague idea, or want to micromanage the design:

/deep-interview "I want to build a task management app"

The deep interview uses Socratic questioning to clarify your thinking before any code is written. It exposes hidden assumptions and measures clarity across weighted dimensions, ensuring you know exactly what to build before execution begins.

## Team Mode (Recommended)

Starting inv4.1.7,Teamis the canonical orchestration surface in OMC. The legacyswarmkeyword/skill has been removed; useteamdirectly.

/team 3:executor
"
fix all TypeScript errors
"

Team runs as a staged pipeline:

team-plan → team-prd → team-exec → team-verify → team-fix (loop)

Enable Claude Code native teams in~/.claude/settings.json:

{

"env"
: {

"CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS"
:
"
1
"

 }
}

If teams are disabled, OMC will warn you and fall back to non-team execution where possible.

### tmux CLI Workers — Codex & Gemini (v4.4.0+)

v4.4.0 removes the Codex/Gemini MCP servers(x,gproviders). Use the CLI-first Team runtime (omc team ...) to spawn real tmux worker panes:

omc team 2:codex
"
review auth module for security issues
"

omc team 2:gemini
"
redesign UI components for accessibility
"

omc team 1:claude
"
implement the payment flow
"

omc team status auth-review
omc team shutdown auth-review

/omc-teamsremains as a legacy compatibility skill and now routes toomc team ....

For mixed Codex + Gemini work in one command, use the/ccgskill (routes via/ask codex+/ask gemini, then Claude synthesizes):

/ccg Review this PR — architecture (Codex) and UI components (Gemini)

Surface

Workers

Best For

omc team N:codex "..."

N Codex CLI panes

Code review, security analysis, architecture

omc team N:gemini "..."

N Gemini CLI panes

UI/UX design, docs, large-context tasks

omc team N:claude "..."

N Claude CLI panes

General tasks via Claude CLI in tmux

/ccg

/ask codex + /ask gemini

Tri-model advisor synthesis

Workers spawn on-demand and die when their task completes — no idle resource usage. Requirescodex/geminiCLIs installed and an active tmux session.

Note: Package naming— The project is branded asoh-my-claudecode(repo, plugin, commands), but the npm package is published asoh-my-claude-sisyphus. If you install or upgrade the CLI tools via npm/bun, usenpm i -g oh-my-claude-sisyphus@latest.

### Updating

If you installed OMC via npm, upgrade with the published package name:

npm i -g oh-my-claude-sisyphus@latest

Package naming note:the repo, plugin, and commands are brandedoh-my-claudecode, but the published npm package name remainsoh-my-claude-sisyphus.

If you installed OMC via the Claude Code marketplace/plugin flow, update with:

#
 1. Update the marketplace clone

/plugin marketplace update omc

#
 2. Re-run setup to refresh configuration

/omc-setup

Note:If marketplace auto-update is not enabled, you must manually run/plugin marketplace update omcto sync the latest version before running setup.

If you experience issues after updating, clear the old plugin cache:

/omc-doctor

# Your Claude Just Have been Steroided.

## Why oh-my-claudecode?

* Zero configuration required- Works out of the box with intelligent defaults
* Team-first orchestration- Team is the canonical multi-agent surface
* Natural language interface- No commands to memorize, just describe what you want
* Automatic parallelization- Complex tasks distributed across specialized agents
* Persistent execution- Won't give up until the job is verified complete
* Cost optimization- Smart model routing saves 30-50% on tokens
* Learn from experience- Automatically extracts and reuses problem-solving patterns
* Real-time visibility- HUD statusline shows what's happening under the hood

## Features

### Orchestration Modes

Multiple strategies for different use cases — from Team-backed orchestration to token-efficient refactoring.Learn more →

Mode

What it is

Use For

Team (recommended)

Canonical staged pipeline (
team-plan → team-prd → team-exec → team-verify → team-fix
)

Coordinated Claude agents on a shared task list

omc team (CLI)

tmux CLI workers — real
claude
/
codex
/
gemini
 processes in split-panes

Codex/Gemini CLI tasks; on-demand spawn, die when done

ccg

Tri-model advisors via
/ask codex
 +
/ask gemini
, Claude synthesizes

Mixed backend+UI work needing both Codex and Gemini

Autopilot

Autonomous execution (single lead agent)

End-to-end feature work with minimal ceremony

Ultrawork

Maximum parallelism (non-team)

Burst parallel fixes/refactors where Team isn't needed

Ralph

Persistent mode with verify/fix loops

Tasks that must complete fully (no silent partials)

Pipeline

Sequential, staged processing

Multi-step transformations with strict ordering

Ultrapilot (legacy)

Deprecated compatibility mode (autopilot pipeline alias)

Existing workflows and older docs

### Intelligent Orchestration

* 32 specialized agentsfor architecture, research, design, testing, data science
* Smart model routing- Haiku for simple tasks, Opus for complex reasoning
* Automatic delegation- Right agent for the job, every time

### Developer Experience

* Magic keywords-ralph,ulw,ralplan; Team stays explicit via/team
* HUD statusline- Real-time orchestration metrics in your status bar
* Skill learning- Extract reusable patterns from your sessions
* Analytics & cost tracking- Understand token usage across all sessions

### Custom Skills

Learn once, reuse forever. OMC extracts hard-won debugging knowledge into portable skill files that auto-inject when relevant.

Project Scope

User Scope

Path

.omc/skills/

~/.omc/skills/

Shared with

Team (version-controlled)

All your projects

Priority

Higher (overrides user)

Lower (fallback)

#
 .omc/skills/fix-proxy-crash.md

---

name
:
Fix Proxy Crash

description
:
aiohttp proxy crashes on ClientDisconnectedError

triggers
:
["proxy", "aiohttp", "disconnected"]

source
:
extracted

---

Wrap handler at server.py:42 in try/except ClientDisconnectedError...

Manage skills:/skill list | add | remove | edit | searchAuto-learn:/learnerextracts reusable patterns with strict quality gatesAuto-inject:Matching skills load into context automatically — no manual recall needed

Full feature list →

## Magic Keywords

Optional shortcuts for power users. Natural language works fine without them. Team mode is explicit: use/team ...oromc team ...rather than a keyword trigger.

Keyword

Effect

Example

team

Canonical Team orchestration

/team 3:executor "fix all TypeScript errors"

omc team

tmux CLI workers (codex/gemini/claude)

omc team 2:codex "security review"

ccg

/ask codex
 +
/ask gemini
 synthesis

/ccg review this PR

autopilot

Full autonomous execution

autopilot: build a todo app

ralph

Persistence mode

ralph: refactor auth

ulw

Maximum parallelism

ulw fix all errors

ralplan

Iterative planning consensus

ralplan this feature

deep-interview

Socratic requirements clarification

deep-interview "vague idea"

deepsearch

Codebase-focused search routing

deepsearch for auth middleware

ultrathink

Deep reasoning mode

ultrathink about this architecture

cancelomc
,
stopomc

Stop active OMC modes

stopomc

Notes:

* ralph includes ultrawork: when you activate ralph mode, it automatically includes ultrawork's parallel execution.
* swarmcompatibility alias has been removed; migrate existing prompts to/teamsyntax.
* plan this/plan thekeyword triggers were removed; useralplanor explicit/oh-my-claudecode:omc-plan.

## Utilities

### Provider Advisor (omc ask)

Run local provider CLIs and save a markdown artifact under.omc/artifacts/ask/:

omc ask claude
"
review this migration plan
"

omc ask codex --prompt
"
identify architecture risks
"

omc ask gemini --prompt
"
propose UI polish ideas
"

omc ask claude --agent-prompt executor --prompt
"
draft implementation steps
"

Canonical env vars:

* OMC_ASK_ADVISOR_SCRIPT
* OMC_ASK_ORIGINAL_TASK

Phase-1 aliasesOMX_ASK_ADVISOR_SCRIPTandOMX_ASK_ORIGINAL_TASKare accepted with deprecation warnings.

### Rate Limit Wait

Auto-resume Claude Code sessions when rate limits reset.

omc
wait

#
 Check status, get guidance

omc
wait
 --start
#
 Enable auto-resume daemon

omc
wait
 --stop
#
 Disable daemon

Requires:tmux (for session detection)

### Monitoring & Observability

Use the HUD for live observability and the current session/replay artifacts for post-session inspection:

* HUD preset:/oh-my-claudecode:hud setupthen use a supported preset such as"omcHud": { "preset": "focused" }
* Session summaries:.omc/sessions/*.json
* Replay logs:.omc/state/agent-replay-*.jsonl
* Live HUD rendering:omc hud

### Notification Tags (Telegram/Discord/Slack)

You can configure who gets tagged when stop callbacks send session summaries.

#
 Set/replace tag list

omc config-stop-callback telegram --enable --token
<
bot_token
>
 --chat
<
chat_id
>
 --tag-list
"
@alice,bob
"

omc config-stop-callback discord --enable --webhook
<
url
>
 --tag-list
"
@here,123456789012345678,role:987654321098765432
"

omc config-stop-callback slack --enable --webhook
<
url
>
 --tag-list
"
<!here>,<@U1234567890>
"

#
 Incremental updates

omc config-stop-callback telegram --add-tag charlie
omc config-stop-callback discord --remove-tag @here
omc config-stop-callback discord --clear-tags

Tag behavior:

* Telegram:alicebecomes@alice
* Discord: supports@here,@everyone, numeric user IDs, androle:<id>
* Slack: supports<@MEMBER_ID>,<!channel>,<!here>,<!everyone>,<!subteam^GROUP_ID>
* filecallbacks ignore tag options

### OpenClaw Integration

Forward Claude Code session events to anOpenClawgateway to enable automated responses and workflows via your OpenClaw agent.

Quick setup (recommended):

/oh-my-claudecode:configure-notifications

#
 → When prompted, type "openclaw" → choose "OpenClaw Gateway"

Manual setup:create~/.claude/omc_config.openclaw.json:

{

"enabled"
:
true
,

"gateways"
: {

"my-gateway"
: {

"url"
:
"
https://your-gateway.example.com/wake
"
,

"headers"
: {
"Authorization"
:
"
Bearer YOUR_TOKEN
"
 },

"method"
:
"
POST
"
,

"timeout"
:
10000

 }
 },

"hooks"
: {

"session-start"
: {
"gateway"
:
"
my-gateway
"
,
"instruction"
:
"
Session started for {{projectName}}
"
,
"enabled"
:
true
 },

"stop"
: {
"gateway"
:
"
my-gateway
"
,
"instruction"
:
"
Session stopping for {{projectName}}
"
,
"enabled"
:
true
 }
 }
}

Environment variables:

Variable

Description

OMC_OPENCLAW=1

Enable OpenClaw

OMC_OPENCLAW_DEBUG=1

Enable debug logging

OMC_OPENCLAW_CONFIG=/path/to/config.json

Override config file path

Supported hook events (6 active in bridge.ts):

Event

Trigger

Key template variables

session-start

Session begins

{{sessionId}}
,
{{projectName}}
,
{{projectPath}}

stop

Claude response completes

{{sessionId}}
,
{{projectName}}

keyword-detector

Every prompt submission

{{prompt}}
,
{{sessionId}}

ask-user-question

Claude requests user input

{{question}}
,
{{sessionId}}

pre-tool-use

Before tool invocation (high frequency)

{{toolName}}
,
{{sessionId}}

post-tool-use

After tool invocation (high frequency)

{{toolName}}
,
{{sessionId}}

Reply channel environment variables:

Variable

Description

OPENCLAW_REPLY_CHANNEL

Reply channel (e.g.
discord
)

OPENCLAW_REPLY_TARGET

Channel ID

OPENCLAW_REPLY_THREAD

Thread ID

Seescripts/openclaw-gateway-demo.mjsfor a reference gateway that relays OpenClaw payloads to Discord via ClawdBot.

## Documentation

* Full Reference- Complete feature documentation
* CLI Reference- Allomccommands, flags, and tools
* Notifications Guide- Discord, Telegram, Slack, and webhook setup
* Recommended Workflows- Battle-tested skill chains for common tasks
* Release Notes- What's new in each version
* Website- Interactive guides and examples
* Migration Guide- Upgrade from v2.x
* Architecture- How it works under the hood
* Performance Monitoring- Agent tracking, debugging, and optimization

## Requirements

* Claude CodeCLI
* Claude Max/Pro subscription OR Anthropic API key

### Platform & tmux

OMC features likeomc teamand rate-limit detection requiretmux:

Platform

tmux provider

Install

macOS

tmux

brew install tmux

Ubuntu/Debian

tmux

sudo apt install tmux

Fedora

tmux

sudo dnf install tmux

Arch

tmux

sudo pacman -S tmux

Windows

psmux
 (native)

winget install psmux

Windows (WSL2)

tmux (inside WSL)

sudo apt install tmux

Windows users:psmuxprovides a nativetmuxbinary for Windows with 76 tmux-compatible commands. No WSL required.

### Optional: Multi-AI Orchestration

OMC can optionally orchestrate external AI providers for cross-validation and design consistency. These arenot required— OMC works fully without them.

Provider

Install

What it enables

Gemini CLI

npm install -g @google/gemini-cli

Design review, UI consistency (1M token context)

Codex CLI

npm install -g @openai/codex

Architecture validation, code review cross-check

Cost:3 Pro plans (Claude + Gemini + ChatGPT) cover everything for ~$60/month.

## License

MIT

Inspired by:oh-my-opencode•claude-hud•Superpowers•everything-claude-code•Ouroboros

Zero learning curve. Maximum power.

## Featured by OmC Contributors

Top personal non-fork, non-archived repos from all-time OMC contributors (100+ GitHub stars).

* @Yeachan-Heo—oh-my-claudecode(⭐ 11k)
* @junhoyeo—tokscale(⭐ 1.3k)
* @psmux—psmux(⭐ 695)
* @BowTiedSwan—buildflow(⭐ 284)
* @alohays—awesome-visual-representation-learning-with-transformers(⭐ 268)
* @jcwleo—random-network-distillation-pytorch(⭐ 260)
* @emgeee—mean-tutorial(⭐ 200)
* @anduinnn—HiFiNi-Auto-CheckIn(⭐ 172)
* @Znuff—consolas-powerline(⭐ 145)
* @shaun0927—openchrome(⭐ 144)

## Star History

## 💖 Support This Project

If Oh-My-ClaudeCode helps your workflow, consider sponsoring:

### Why sponsor?

* Keep development active
* Priority support for sponsors
* Influence roadmap & features
* Help maintain free & open source

### Other ways to help

* ⭐ Star the repo
* 🐛 Report bugs
* 💡 Suggest features
* 📝 Contribute code

## About

Teams-first Multi-agent orchestration for Claude Code

yeachan-heo.github.io/oh-my-claudecode-website

### Topics

 automation

 opencode

 multi-agent-systems

 ai-agents

 claude

 parallel-execution

 vibe-coding

 claude-code

 agentic-coding

 oh-my-opencode

### Resources

 Readme



### License

 MIT license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

11.9k

 stars


### Watchers

38

 watching


### Forks

803

 forks


 Report repository



## Releases203

v4.9.1

 Latest



Mar 24, 2026



+ 202 releases

## Sponsor this project

 



 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.







Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors69

+ 55 contributors

## Languages

* TypeScript56.6%
* JavaScript41.5%
* Other1.9%
