---
title: 'GitHub - activeloopai/hivemind: One brain for all your agents · GitHub'
url: https://github.com/activeloopai/hivemind
site_name: github
content_file: github-github-activeloopaihivemind-one-brain-for-all-your
fetched_at: '2026-06-10T12:07:33.382671'
original_url: https://github.com/activeloopai/hivemind
author: activeloopai
description: One brain for all your agents. Contribute to activeloopai/hivemind development by creating an account on GitHub.
---

activeloopai

 

/

hivemind

Public

* NotificationsYou must be signed in to change notification settings
* Fork42
* Star625

 
 
 
 
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

1,537 Commits
1,537 Commits
.claude-plugin
.claude-plugin
 
 
.github
.github
 
 
.husky
.husky
 
 
claude-code
claude-code
 
 
codex
codex
 
 
docs
docs
 
 
embeddings
embeddings
 
 
hermes/
skills
hermes/
skills
 
 
openclaw
openclaw
 
 
pi/
extension-source
pi/
extension-source
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.jscpd.json
.jscpd.json
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
esbuild.config.mjs
esbuild.config.mjs
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

# Hivemind

#### One brain for all your agents

Auto-learning, cloud-backed shared brain forClaude Code • OpenClaw • Codex • Cursor • Hermes • piagents.

One engineer's agent figures out a tricky migration on Monday.

Tuesday, every agent on the team can execute the pattern.

OnLoCoMo, the public long-context memory benchmark, Hivemind is25% cheaper, 1.7× fewer tokens, and 31% fewer turnsthan running without shared memory. (See the numbers below.)

Beyond memory.Hivemind doesn't just remember. It mines your team's traces for repeated patterns and codifies them into reusable skills that propagate back into every agent on the team. The agent your junior engineer used this morning is sharper because of what your senior engineer's agent figured out last week.

* 📥Capturesevery session's prompts, tool calls, and responses as structured traces in Deeplake
* 🧠Codifiespatterns into reusableSKILL.mdfiles, available to every agent on your team
* 🔍Searchestraces and skills with hybrid lexical + semantic retrieval (BM25 fallback when embeddings off)
* 🔗Propagatescapability across sessions, agents, teammates, and machines in real time
* 📁Interceptsfile operations on~/.deeplake/memory/through a virtual filesystem backed by SQL
* 📝Summarizessessions into AI-generated wiki pages via a background worker at session end
* ☁️BYOC: keep data in your own GCS, Azure, S3, or on-prem bucket.See Security & storage

## Benchmarks

On theLoCoMolong-context memory benchmark (100 QA pairs, Claude Haiku viaclaude -p, hybrid lexical + semantic retrieval), Hivemind cuts cost, tokens, and turns versus a no-memory baseline:

Metric

Baseline

Hivemind

Improvement

Cost / 100 QA

$8.94

$6.65

25% cheaper

Tokens / question

1,700

1,008

1.7× fewer

Turns / question

8.9

6.2

31% fewer

The agent reaches the answer in fewer turns with less context, because the prior work is already in scope at recall time, not re-derived per session.

## Quick start

One command, all your agents:

npm install -g @deeplake/hivemind 
&&
 hivemind install

The installer detects every supported assistant on your machine (table below), wires up the hooks, and shows a one-line consent prompt before opening a browser for sign-in. Restart your assistants after install.

Headless / CI installs:pass an API token instead of using the browser flow:

HIVEMIND_TOKEN=
<
your-token
>
 hivemind install

#
 or

hivemind install --token 
<
your-token
>

Get a token from your account settings onhttps://deeplake.ai. With no token in a non-interactive shell, the install completes with hooks but skips sign-in; runhivemind loginlater to enable shared memory.

Install for a specific assistant only:

hivemind install --only claude
hivemind claude install 
#
 equivalent

hivemind codex install
hivemind claw install
hivemind cursor install
hivemind hermes install
hivemind pi install

Check what's wired up:

hivemind status

Supported assistants:

Platform

Integration

Auto-capture

Auto-recall

Claude Code

Marketplace plugin

✅

✅

OpenClaw

Native extension

✅

✅

Codex

Hooks (
hooks.json
)

✅

✅

Cursor

Hooks (
hooks.json
 1.7+)

✅

✅

Hermes Agent

Shell hooks (
config.yaml
) + skill + MCP server

✅

✅

pi

Extension API (
pi.on(...)
) + skill + AGENTS.md

✅

✅

### Alternative install paths

Claude Code plugin marketplace

If you prefer Claude Code's native plugin marketplace:

/plugin marketplace add activeloopai/hivemind
/plugin install hivemind
/reload-plugins
/hivemind:login

Auto-updates on each session start. Manual update:/hivemind:update.

OpenClaw ClawHub

openclaw plugins install clawhub:hivemind

Then type/hivemind_loginin chat, click the auth link, and sign in.

#### Commands

Command

Description

/hivemind_login

Sign in via device flow

/hivemind_capture

Toggle capture on/off

/hivemind_whoami

Show current org and workspace

/hivemind_orgs

List organizations

/hivemind_switch_org <name>

Switch organization

/hivemind_workspaces

List workspaces

/hivemind_switch_workspace <id>

Switch workspace

/hivemind_update

Check for plugin updates

Auto-recall and auto-capture are enabled by default. Data is stored in the samesessionstable as Claude Code and Codex.

#### Coexistence withmemory-core

Hivemind runsalongsideOpenClaw's built-inmemory-coreplugin. It doesnotclaim the memory slot, somemory-core's dreaming cron ("0 3 * * *") and other memory-slot-dependent jobs keep working. Hivemind captures session activity and exposes its own commands;memory-corekeeps owning recall/promotion/dreaming.

#### Troubleshooting

* Hivemind seems slow or unresponsive.Check the agent model in~/.openclaw/openclaw.jsonunderagents.defaults.model. Hivemind makes many small tool calls per turn; a large reasoning model like Opus will feel sluggish. Recommended default:anthropic/claude-haiku-4-5-20251001.
* openclaw model <id>says "plugins.allow excludes model".Themodelplugin CLI is disabled by default. Edit~/.openclaw/openclaw.jsondirectly (keyagents.defaults.model) and restart the gateway:systemctl --user restart openclaw-gateway.service.
* Model switch rejected as "not allowed".Use the exact dated provider-prefixed ID (anthropic/claude-haiku-4-5-20251001,anthropic/claude-sonnet-4-6). Legacy IDs likeclaude-3-5-haiku-latestand unprefixed bare IDs are not on OpenClaw's allowlist.
* Self-update via Telegram fails with "elevated is not available".tools.elevated.allowFrommust includetelegrambefore elevated commands work from that channel. Safer alternative: run the upgrade in a local shell withopenclaw plugins update hivemind.
* npm error EACCESduring self-update.OpenClaw was installed under a root-owned npm prefix (e.g./usr/lib/node_modules/openclaw). Reinstall under a user-writable prefix, or run the update with appropriate privileges locally, not via a channel.

Codex (manual)

Tell Codex to fetch and follow the install instructions:

Fetch and follow instructions from https://raw.githubusercontent.com/activeloopai/hivemind/main/codex/INSTALL.md

Or run the installer script directly:

git clone https://github.com/activeloopai/hivemind.git 
~
/.codex/hivemind

~
/.codex/hivemind/codex/install.sh

Restart Codex to activate.

First launch — trust the hooks.Codex shows a"Hooks need review"prompt before it will run hivemind's hooks:

Hooks need review
2 hooks are new or changed.
Hooks can run outside the sandbox after you trust them.

 1. Review hooks
 › 2. Trust all and continue
 3. Continue without trusting (hooks won't run)

Choose2. Trust all and continue— otherwise the hooks won't run and hivemind stays inactive.

Cursor (1.7+)

The unified installer wires six lifecycle events in~/.cursor/hooks.json: sessionStart, beforeSubmitPrompt, postToolUse, afterAgentResponse, stop, sessionEnd. Hooks fork a Node bundle at~/.cursor/hivemind/bundle/per event. Restart Cursor after install to load.

hivemind cursor install

Auto-capture is enabled the same way as Claude Code / Codex / OpenClaw.

Hermes Agent

Wires shell hooks into~/.hermes/config.yaml(pre_llm_call/post_tool_call/post_llm_call/on_session_end) for auto-capture, drops the bundle at~/.hermes/hivemind/bundle/, registers the shared MCP server (~/.hivemind/mcp/server.js) undermcp_servers.hivemind, and installs anagentskills.io-compatible skill at~/.hermes/skills/hivemind-memory/for recall.

hivemind hermes install

pi (badlogic/pi-mono coding-agent)

Upserts an idempotent BEGIN/END marker block into~/.pi/agent/AGENTS.md(auto-loaded every turn) and drops a TypeScript extension at~/.pi/agent/extensions/hivemind.ts. The extension subscribes to pi's lifecycle events (session_start/input/tool_result/message_end) for auto-capture and registershivemind_search,hivemind_read,hivemind_indexas first-class pi tools.

hivemind pi install

Note: no per-agent SKILL.md is dropped under~/.pi/agent/skills/; pi reads skills from both that directory AND the shared~/.agents/skills/location. If the codex installer has run on the same machine, pi picks up the hivemind skill from the shared~/.agents/skills/hivemind-memorysymlink automatically. The AGENTS.md block plus the registered tools cover the action surface in either case.

### Uninstall

hivemind uninstall 
#
 remove from every detected assistant

hivemind codex uninstall 
#
 remove from one

## How it works

Capture → Codify → Propagate → Compound.Every coding-agent interaction (prompt, tool call, response) is captured as a structured trace in Deeplake. A background worker mines traces for repeated patterns and codifies them intoSKILL.mdfiles, scoped to your workspace. Codified skills propagate into every Hivemind-connected agent's context at inference time. The agent your junior engineer used this morning is sharper because of what your senior engineer's agent figured out last week.

## Features

### 🔍 Natural search

Just ask your agent naturally:

"What was Emanuele working on?"
"Search traces for authentication bugs we've solved"
"What did we decide about the API design?"
"Show me skills my team has codified for handling migrations"

### 🔒 Privacy controls

Disable capture entirely:

HIVEMIND_CAPTURE=false claude

Enable debug logging:

HIVEMIND_DEBUG=1 claude

## ⚠️Data collection notice

This plugin captures session activity and stores it in your Deeplake workspace:

Data

What's captured

User prompts

Every message you send

Tool calls

Tool name + full input

Tool responses

Full tool output

Assistant responses

The agent's final response

Subagent activity

Subagent tool calls and responses

Codified skills

Patterns extracted from traces

All users in your Deeplake workspace can read this data.That's the design. Shared capability requires shared substrate. A DATA NOTICE is displayed at the start of every session. Workspace-level isolation prevents data leakage between orgs.

## Configuration

Variable

Default

Description

HIVEMIND_TOKEN

(none)

API token (auto-set by login)

HIVEMIND_ORG_ID

(none)

Organization ID (auto-set by login)

HIVEMIND_WORKSPACE_ID

default

Workspace name

HIVEMIND_API_URL

https://api.deeplake.ai

API endpoint

HIVEMIND_TABLE

memory

SQL table for summaries and virtual FS

HIVEMIND_SESSIONS_TABLE

sessions

SQL table for per-event session capture

HIVEMIND_MEMORY_PATH

~/.deeplake/memory

Path that triggers interception

HIVEMIND_CAPTURE

true

Set to 
false
 to disable capture

HIVEMIND_CAPTURE_ONLY_CLI

(none)

Set to 
true
 to capture only interactive CLI sessions. Sessions spawned by the Claude Agent SDK (Python/TypeScript) are skipped; their 
CLAUDE_CODE_ENTRYPOINT
 is 
sdk-py
 / 
sdk-ts
, so they fail the substring check for 
cli
.

HIVEMIND_SKILLIFY_EVERY_N_TURNS

20

Assistant turns between auto skill-mining attempts. Lower = more frequent mining (cheaper sessions, noisier output); higher = fewer attempts on longer histories.

HIVEMIND_EMBEDDINGS

true

Set to 
false
 to force lexical-only mode

HIVEMIND_DEBUG

(none)

Set to 
1
 for verbose hook debug logs

## Semantic search (optional)

Hivemind ships with a local embedding daemon (nomic-embed-text-v1.5) for hybrid semantic + lexical search over~/.deeplake/memory/.Off by defaultbecause the dependency footprint is ~600 MB. Enable withhivemind embeddings install(orhivemind install --with-embeddings). Without it, search degrades silently to BM25/lexical-only.

Full guide:docs/EMBEDDINGS.md.

## Summaries

After each session, a background worker generates an AI-written wiki summary and stores it in thememorytable alongside its 768-dim embedding. Long sessions checkpoint mid-session every 50 messages or 2 hours (configurable). The wiki worker shells out to the host agent's own CLI (claude -p,codex exec,pi --print, …) so no separate API key is needed. Browse summaries at~/.deeplake/memory/summaries/.

Triggers, generation flow, and env-var reference:docs/SUMMARIES.md.

## Skills (skillify)

Hivemindcodifies recurring patterns from your team's recent sessions into reusable skillsthat propagate to every agent on your team, automatically. An async background worker fires on Stop / SessionEnd, mines recent sessions in scope, asks Haiku whether the activity contains something worth keeping, and writes aSKILL.mdto<project>/.claude/skills/<name>/.

hivemind skillify 
#
 show current scope, team, install, per-project state

hivemind skillify scope 
<
me
|
team
>
 
#
 who counts as "in scope" for mining

hivemind skillify pull 
#
 install teammates' skills locally

hivemind skillify unpull 
#
 remove pulled skills

Triggers, generation flow, fullpull/unpullsemantics, gate-CLI table per agent, env vars, logs:docs/SKILLIFY.md.

## Codebase graph

Hivemind builds a live graph of your codebase from the same traces it captures: files, symbols, imports, and the edges your agents actually traverse during real sessions. Search and recall walk this graph, not just plain text, so "where do we handle auth?" lands on the actual files the team's agents have touched, not just every file that mentions "auth".

Above: the Hivemind codebase rendered through its own graph feature.

## Rules (cross-agent team principles)

Hivemindshares team rules across every agent in the org, injected at SessionStart so every claude-code / cursor / hermes session starts knowing them. For personal or team work items with progress tracking, useGoals + KPIs(VFS-backed) instead.

hivemind rules add 
"
no DROP TABLE on prod creds
"

hivemind rules list 
#
 latest 10 active

hivemind rules edit 
<
rule-id
>
 
"
<new text>
"
 
#
 bumps version

hivemind rules 
done
 
<
rule-id
>
 
#
 mark closed

#
 Cross-agent diagnostic / pi/openclaw fallback

hivemind context 
#
 print the injection block on demand

What's injected at SessionStart(claude-code, cursor, hermes. Codex is
deliberately excluded to keep its user-visible TUI clean; pi/openclaw
fall back tohivemind context):

=== HIVEMIND RULES (N active) ===
- <rule_id>: <text>
(X more, run 'hivemind rules list' to see all)

=== HIVEMIND HOW-TO ===
- Rules above are team principles. Treat any action that would violate one as a critical error and surface it to the user before proceeding.
- Run 'hivemind rules list' for the full inventory beyond what's shown here.

Env vars:

* HIVEMIND_RULES_TABLE: table name (defaulthivemind_rules).
* HIVEMIND_CAPTURE=false: full read-only mode. Skips placeholder + ensure DDL; renderer still injects.

## Goals + KPIs

Personal / team objectives + measurable targets live in the Deeplake virtual filesystem under~/.deeplake/memory/goal/<owner>/<status>/<uuid>.mdand~/.deeplake/memory/kpi/<goal_id>/<kpi-slug>.md. Path encodes structure (owner, status, goal_id); the file body holds the human-readable description.

#
 CLI fallback for runtimes that can't route VFS writes (cursor/hermes/pi)

hivemind goal add 
"
ship the search bar
"

hivemind goal list [--all
|
--mine]
hivemind goal 
done
 
<
goal_id
>

hivemind goal progress 
<
goal_id
>
 opened
|
in_progress
|
closed

For VFS-capable runtimes (claude-code/codex) thehivemind-goalsskill creates and edits goals/KPIs directly via Bash heredoc against the VFS path.mvbetweenopened/,in_progress/, andclosed/is the canonical status transition. KPIs are manual files; the body format is documented in the skill (target:,current:,unit:).

## Architecture

Per-agent integration mechanisms (marketplace plugin, hooks, skills, native extension) and monorepo structure:docs/ARCHITECTURE.md.

## Roadmap

* Trajectory export for fine-tuning.Because traces are stored in Deeplake's tensor format, they're export-ready as PyTorch datasets. Teams running their own open-source models can fine-tune on their org's accumulated trajectories. A handful of advanced customers are already doing this against the trajectories their Claude Code and Codex agents generated.
* GPU-accelerated dense retrieval at scale.Local CPU embeddings already ship via the optional nomic-embed daemon (seeSemantic search). Next: GPU-accelerated vector search over the full trace store, on by default.
* Skill versioning and review.Pre-release human review for codified skills before they propagate org-wide, for teams that want a curation step.
* More agents.If your team uses an agent that isn't on the supported-assistants list above, open an issue.

## Security & storage

### Tenant isolation & encryption

* TLS between every agent and Deep Lake. AES-256 on the bytes once they land. Your cloud credentials live in Deep Lake's vault, and Hivemind never sees the raw keys.
* Org and workspace boundaries enforced at the storage layer, not just the API. Sessions never share a row, a partition, or an index with another workspace.
* Disable capture per session withHIVEMIND_CAPTURE=false. Delete a workspace and the underlying objects go with it.

### Code-level controls

* SQL values escaped withsqlStr(),sqlLike(),sqlIdent()
* ~70 allowlisted builtins run in the virtual FS; unrecognized commands are denied
* Credentials stored with mode0600, config dir with mode0700
* Device flow login: no tokens in environment or code

### Bring your own cloud (BYOC)

Hivemind Cloud is the default. When that isn't enough, point Hivemind at storage in your own cloud. We handle the orchestration, data never leaves your perimeter.

Provider

Status

Setup

Google Cloud Storage

Available

docs

Azure Blob Storage

Available

docs

Amazon S3

Available

contact us

S3-compatible on-prem

On request

contact us

## Who builds Hivemind

Hivemind is built and maintained byActiveloop, the open-source team behindDeeplake, backed by Y Combinator.

We run Hivemind ourselves, all day, across Claude Code, OpenClaw, Codex, and Cursor. Every benchmark number above came from our own internal eval against the LoCoMo public benchmark. If you're running coding agents at a team or org and want to talk through your setup, drop us a line:hello@activeloop.ai.

## Got questions?

Setup, BYOC, agent integrations, or workflow. Come ask in the community. We hang out on both:

  
 

## Development

git clone https://github.com/activeloopai/hivemind.git

cd
 hivemind
npm install
npm run build 
#
 tsc + esbuild → claude-code/bundle/ + codex/bundle/ + cursor/bundle/ + openclaw/dist/ + mcp/bundle/ + bundle/cli.js

npm 
test
 
#
 vitest

Test locally with Claude Code:

claude --plugin-dir claude-code

Interactive shell against Deeplake:

npm run shell

## Star history

## License

Apache License 2.0, © Activeloop, Inc. SeeLICENSEfor details.

## About

One brain for all your agents

deeplake.ai/hivemind

### Topics

 postgres

 ai

 embeddings

 artificial-intelligence

 codex

 ai-agents

 claude

 memory-engine

 long-term-memory

 rag

 anthropic

 ai-memory

 claude-agents

 claude-agent-sdk

 claude-code-plugin

 claude-skills

 openclaw

 openclaw-skills

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

625

 stars
 

### Watchers

6

 watching
 

### Forks

42

 forks
 

 Report repository

 

## Releases157

v0.7.86 — fix(wiki-worker): make summary generation work on Windows

 Latest

 

Jun 10, 2026

 

+ 156 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript91.2%
* JavaScript8.6%
* Shell0.2%