---
title: 'GitHub - chaitanyagiri/munder-difflin: local multi-agent harness · GitHub'
url: https://github.com/chaitanyagiri/munder-difflin
site_name: github
content_file: github-github-chaitanyagirimunder-difflin-local-multi-age
fetched_at: '2026-08-18T11:22:57.541416'
original_url: https://github.com/chaitanyagiri/munder-difflin
author: chaitanyagiri
description: local multi-agent harness. Contribute to chaitanyagiri/munder-difflin development by creating an account on GitHub.
---

chaitanyagiri

 

/

munder-difflin

Public

* NotificationsYou must be signed in to change notification settings
* Fork208
* Star1.6k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

707 Commits
707 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
blog
blog
 
 
build
build
 
 
docs
docs
 
 
hive/
docs
hive/
docs
 
 
landing-remotion
landing-remotion
 
 
prototypes/
vde
prototypes/
vde
 
 
resources
resources
 
 
scripts
scripts
 
 
seo
seo
 
 
src
src
 
 
test
test
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
DESIGN.md
DESIGN.md
 
 
HIVE.md
HIVE.md
 
 
LICENSE
LICENSE
 
 
MEMORY_GRAPH_SPEC.md
MEMORY_GRAPH_SPEC.md
 
 
README.md
README.md
 
 
RELEASE.md
RELEASE.md
 
 
SECURITY.md
SECURITY.md
 
 
SPEC.md
SPEC.md
 
 
TELEMETRY.md
TELEMETRY.md
 
 
electron-builder.yml
electron-builder.yml
 
 
electron.vite.config.ts
electron.vite.config.ts
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.node.json
tsconfig.node.json
 
 
tsconfig.web.json
tsconfig.web.json
 
 
View all files

## Repository files navigation

# Munder Difflin

### Agent harness to run an office of your clones

Free, open source and performant— a multi-agent harness that works with the
subscriptions you already pay for, on their hourly limits. It turns the terminal coding CLI
you already run into a clone of you, one that keeps working while you're away and
coordinates a whole office of agents on your own machine.

WrapsClaude Code, Antigravity (Gemini), OpenAI Codex,xAI Grok,Kimi Code,Qwen,OpenCode,Crush,pi.dev, andGitHub Copilot CLI— with bring-your-own keys and local LLMs.
Agents that message, route, and remember, coordinated byyour clone(Michael) and
visualized as avatars at work on a shared office floor.

Electron · React · TypeScript · Pixi.js · xterm.js · node-pty

Note

The world's best agents. The world's worst paper company.Munder Difflin takes the terminal-agent CLIs you already run —claude,agy,codex,grok,kimi,qwen,opencode,crush,pi, andcopilot— and turns them
into a self-coordinating team: each agent gets long-term memory, a mailbox, and a desk on a 2D
office floor — andyour clone(Michael) routes work between them while you watch. He's the
boss of the floor; you're still the boss of him.

## Contents

* What it is
* How it works
* Features
* Getting started
* Architecture
* Project structure
* Design system
* Roadmap
* Contributing
* Telemetry
* License
* Acknowledgements

## What it is

Munder Difflin is a desktop app that wrapsreal terminal-agent CLIsas fully-capable agents,
wires them into ahive mind, and putsyour clonein charge — Michael, the one agentyoutalk to in order to get things done. Under the hood it runs thefastest memory layer in the
worldso every agent remembers what it learns and recalls it instantly.

* Every terminal is an agent.Eachclaude,agy,codex,grok,kimi,qwen,opencode,crush,pi,copilot, or custom session runs as a real
process in a pseudo-terminal (node-pty), byte-for-byte authentic, rendered with xterm.js.
* Every agent is an avatar.Sessions appear as characters on a Pixi.js office floor — they walk
to stations as they work, and envelopes fly desk-to-desk when they message each other.
* The hive coordinates them.Agents read their memory and drain a mailbox; the router moves
messages between inboxes; the GOD agent adjudicates, assigns, and escalates only when it needs you.
* Memory that's instant.A markdown-first memory layer with a semantic recall index means agents
remember across sessions and recall in milliseconds.

## How it works

 you ── talk to ──► ┌─────────────┐
 │ GOD agent │ orchestrator / supervisor
 │ (Michael's │ roster · routing · adjudication
 │ office) │ blackboard · task ledger
 └──────┬──────┘
 │ assigns · routes · escalates
 ┌────────────────────────┼────────────────────────┐
 ▼ ▼ ▼
 ┌───────────┐ ┌───────────┐ ┌───────────┐
 │ agent A │ message │ agent B │ message │ agent C │
 │ provider │ ─────────► │ provider │ ─────────► │ provider │
 │ + memory │ │ + memory │ │ + memory │
 └───────────┘ └───────────┘ └───────────┘
 └──────── shared hive: memory · mailbox · blackboard · log ───────┘

1. You spawn agents— each is a normal terminal process (claude,agy,codex, or custom)
with its own working directory, identity, and provider-specific lifecycle.
2. Agents collaborate through the hive— a local git repo of plain files. They write to their ownoutbox/; the harness's router delivers into recipients'inbox/. No agent ever touches git
(single-committer design avoidsindex.lockcorruption).
3. The GOD agent runs the floor— it reads every request, resolves routine ones itself (keeping
the system fully autonomous), and only escalatescriticalitems (spend, destructive ops, scope
changes) into an approvals queue you act on.
4. Everything is visible— you watch avatars move, envelopes fly, and the live terminal stream;
you can type back into any session, browse its files, and read its git history.

SeeHIVE.mdfor the full multi-agent design,SPEC.mdfor the
terminal/event plane, andDESIGN.mdfor the visual system.

## Features

The floor

* Every terminal is a real agent.Claude Code, Antigravity (Gemini), OpenAI Codex, xAI Grok, Kimi Code, Qwen, OpenCode, Crush, pi.dev, GitHub Copilot CLI, or a custom command — each in its ownnode-ptyPTY, rendered with xterm.js.
* Every agent is an avatar.A Pixi.js office floor where agents walk to stations, envelopes fly desk to desk, and avatar state reflects real work.
* A GOD orchestrator you talk to.It routes tasks, adjudicates traffic, and escalates only what needs a human. Or pressTalkand run the floor by voice.
* Per-agent git worktrees.Optional isolation so parallel agents never collide on branches.

Memory & coordination

* The hive— per-agent memory, atomic-file mailboxes, a shared blackboard, an append-only event log, single-committer git.
* Semantic recall— markdown memory mined into a shared palace, searchable from the UI, with condensation so it doesn't grow forever.
* Enterprise Knowledge Graph— your own documents and policies, queryable by any agent.

Control & safety

* Human gates— spend, scope, and destructive ops escalate to you. Steer mid-run or stop gracefully.
* Circuit breaker— a steer → constrain → stop ladder for agents that loop, storm errors, or blow their budget.
* Budgets & telemetry— per-agent token budgets, real cost from transcripts, a durable ledger, OTel spans, and a tool waterfall.

Command Center

* Kanban tasks with dependencies, scheduled missions + heartbeat, live fleet monitoring, memory search, activity log, and a CI watcher.
* Skills— what every agent can already do across Claude Code, OpenCode and Codex, plus a browsable catalog of 227 more with search, filters, install and uninstall.
* Built-in Monaco IDE— file tree, editor tabs, save, plus CHANGES · HISTORY · COMPARE git rails with commit graph, diffs, branch compare, and guarded checkout. All fs/git access brokered through main.

Getting work in and out

* Slack & webhooks— message a channel or POST a webhook; Michael can spawn an ephemeral worker, reply in-thread, and tear it down.
* Shareable hires + Agent Gallery— import a role from amunderdifflin://hirelink; import only pre-fills the form, a human still spawns it. Browse roles at theAgent Gallery.
* BYOK keys + local LLMs— per-provider keys in a write-only secret broker, plus Ollama / LM Studio / vLLM base URLs. Guides:open models·Mac Mini.
* Auto-update— new releases download in the background; you click restart, and the notes arrive as a designed page rather than a version number.
* Prerequisites— one Settings page showing which supporting tools (uv, git, Node, MemPalace, each agent CLI) you have, what each is for, and a button that asks Michael to install what is missing.

Note

Status: v0.4.4 — Windows agents can finally talk to each other.On Windows, agents were
never told they could message one another: the protocol reaches them as a multi-line command
line, andcmd.execut it at the first newline. They started, looked healthy, and ignored each
other forever. If you tried Munder Difflin on Windows and your team just sat there, that was
this bug. Also fixed: a fresh install now starts its own message router instead of waiting for a
restart, the setup wizard can be finished, and dark mode is rebuilt for readability. New in this
release:Skills,Prerequisites, and release notes that carry their own page.If you're on 0.3.8, update:that build's usage-limit guard never released the agents it held,
and it has been removed entirely.
macOS (signed & notarized), Windows, and Linux builds are on thereleases page.

(
↑ back to top
)

## Getting started

### Prerequisites

* macOS, Windows, or Linux.
* Node.js 18+and npm.
* AC/C++ toolchainfornode-pty's native addon — on macOS, install Xcode Command Line Tools:xcode-select --install
* At least one supported agent CLI on yourPATH—Claude Code(claude, the default),Antigravity(agy),OpenAI Codex(codex),xAI Grok(grok),Kimi Code(kimi),Qwen(qwen),OpenCode(opencode),Crush(crush),pi.dev(pi), orGitHub Copilot(copilot). Most missing CLIs self-heal: the harness runs the installer in the
terminal and continues into the new binary.
* Optional:your own API keys and local LLMsinSettings → AI Engines(Ollama / LM Studio / vLLM).
* Optional:the semantic memory index for instant cross-session recall — markdown memory works without it.

### Install & run

git clone https://github.com/chaitanyagiri/munder-difflin.git

cd
 munder-difflin
npm install 
#
 postinstall rebuilds node-pty against Electron's ABI

npm run dev 
#
 launches the Electron app with hot reload

On first launch you'll go through the onboarding wizard, then land on the floor. UseAdd agentto
spawn your first session — the GOD agent seats itself in Michael's office automatically.

### Other scripts

npm run build 
#
 production build via electron-vite

npm run preview 
#
 preview the production build

npm run typecheck 
#
 type-check the node (main/preload) and web (renderer) projects

Ifnode-ptyfails to load after an Electron upgrade, re-runnpm install(thepostinstallhook
runselectron-rebuildagainst the current Electron ABI).

## Architecture

Two data planes feed one renderer:

┌───────────────────────────────────────────────────────────────┐
│ Electron Renderer (React) │
│ ┌──────────────────┐ ┌──────────────────────────────┐ │
│ │ Office Floor │ │ Terminal + Command Bar │ │
│ │ (Pixi.js) │ │ Files + Git tabs (xterm.js) │ │
│ └─────────▲────────┘ └────────────▲─────────────────┘ │
│ │ avatar state │ pty bytes / fs / git │
└─────────────┼──────────────────────────┼───────────────────────┘
 │ IPC (contextBridge: window.cth)
 ┌──────┴──────────┐ ┌──────┴─────────────┐
 │ Event Plane │ │ Terminal Plane │
 │ hooks / hive │ │ node-pty PTYs │
 │ router + GOD │ │ + fs + git │
 └────────▲────────┘ └──────▲─────────────┘
 │ hook payloads │ stdin / stdout
 └─────────┬──────────────┘
 ┌──────┴──────────────┐
 │ claude / agy / codex│
 └─────────────────────┘

* Terminal plane.The main process owns aPtyManagerthat spawns each agent as anode-ptyprocess and streams output over per-id IPC (pty:data:<id>). The renderer talks only through a
typedwindow.cthbridge (src/preload/index.ts), which also exposes
sandboxed filesystem and git helpers.
* Hive / event plane.hive.tsis the on-disk multi-agent layer;hooks.tsruns the hook
server that provider bridges POST lifecycle payloads to (cth-hookfor Claude Code,agy-hookfor Antigravity).memory.tswraps the semantic memory CLI. The router delivers messages, drains
provider outboxes, the GOD agent adjudicates, and idle/inbox wakeups keep workers draining mail.

## Project structure

src/
 main/ Electron main process (Node)
 index.ts window, IPC handlers, quit guard
 pty.ts node-pty manager (spawn/write/resize/kill/stream)
 hive.ts on-disk multi-agent layer (memory, mailboxes, router)
 hooks.ts hook server + provider hook shims (`cth-hook`, `agy-hook`)
 memory.ts semantic memory layer (CLI wrapper, degrade-to-noop)
 config.ts harness config persistence + home setup
 transcript.ts reads ~/.claude/projects/ JSONL transcripts for real token/cost telemetry
 telemetry.ts live OTel collector + usage/cost feed for observability
 usage.ts / pricing.ts UsageProvider seam + per-model cost attribution
 breaker.ts / control.ts cost/runaway circuit breaker (steer/constrain/stop) + HITL gate / steer / stop
 reflect.ts MemoryReflector — memory condensation
 db.ts SQLite durable store (window bounds + history) + durable cost ledger
 github.ts GitHub issue + CI run ingestion via the gh CLI
 shellEnv.ts resolve PATH and shell env for child processes
 fs.ts / git.ts sandboxed filesystem + git bridges
 preload/ contextBridge → typed window.cth API
 renderer/src/
 App.tsx top-level layout + wiring
 design/ tokens.css / tokens.ts / global.css (design source of truth)
 components/ PixelPanel, AgentDetailPanel, CommandBar, ApprovalsPanel, MemoryPanel, …
 CommandCenterPanel, Michael's control surface (Terminal/Floor/Memory/Activity/Tasks/Triggers/Handbook tabs)
 ToolWaterfall, per-agent tool-span waterfall for the observability view
 TasksKanban, dependency-aware kanban board (Tasks tab)
 ThreadsPanel, hive message conversation viewer (Messages tab)
 MessageQueueComposer, park messages for a busy agent
 scene/office/ Pixi office floor: OfficeFloor, Character, Camera, cast, pathfinding, …
 store/ · hooks/ zustand store, event loop, PTY parser, typewriter
 assets/ tilesets, maps, character sheets (see ATTRIBUTION.md)
docs/ `logo.png`, `banner.png`, landing page (GitHub Pages → munderdiffl.in)
docs/media/ `og.png` (social previews) + rendered Remotion clips
landing-remotion/ Remotion project that renders the landing page's "how it works" clips
HIVE.md · SPEC.md · DESIGN.md multi-agent · terminal/event · visual design
docs/message-queue.md who may type into an agent's terminal, and when

(
↑ back to top
)

## Design system

The aesthetic isAnimal Crossing × Earthbound × SNES menu UI— pixel-snapped, chunky, friendly.DESIGN.mdis canonical; every component derives from its tokens. The Munder Difflin
brand layers aDunder-Mifflin maroon(#6E1423) andgold(#F4D35E) on top for logo and
chrome. The 15 avatars are the cast ofThe Office, differentiated by hair/skin/shirt recipes.

## Roadmap

Shipped throughv0.4.3— ten agent engines with BYOK keys and local LLMs, voice orchestration,
the hive (memory · mailboxes · blackboard · event log), Command Center with kanban and schedules,
a built-in Monaco IDE with git rails, integrations registry + secret broker, Slack-spawned workers,
shareable hires and the Agent Gallery, observability and the circuit breaker, durable persistence,
session resume, multi-window floors, and working auto-update.
Full history inCHANGELOG.md.

Next up:

* More chat integrations— Telegram and richer chat bridges that pipe a channel into Michael's queue and route replies back out.
* More engines & integration templates— keep growing the engine roster and the integrations registry.
* Fuller avatar coverage— drive the remaining station visits and tool-bubbles entirely from real hook events.
* Durable layout & command history— extend persistence to agent layout and per-session history.

(
↑ back to top
)

## Contributing

Contributions are welcome — this is an early prototype with a lot of surface area. Start withCONTRIBUTING.md. The short version: fork,npm install && npm run dev, keepnpm run typecheckgreen, andderive any new UI fromDESIGN.mdtokens. Good
first areas: wiring real hook events, the add-agent flow, the config drawer, and cross-platform work.

## Telemetry

Official builds send asmall set of anonymous usage events(app opened, agent spawned, feature
used) — never prompts, code, file paths, or agent output. The complete event list, the anonymity
guarantees, and the three ways to opt out (Settings toggle,DO_NOT_TRACK, or building from
source — forks compile with no key and send nothing) are documented inTELEMETRY.md.

## License

Important

Asset licensing.The bundled pixel art (tilesets, maps, and the base character sheets the
Office cast is recolored from) comes fromLimeZuviashahar061/the-officeunder theLimeZu FREE VERSION
license — non-commercial use only. The recolored sprites inherit that restriction. Seesrc/renderer/src/assets/ATTRIBUTION.md.To
commercialize, replace these assets or obtain a paid LimeZu license.

Thesource codeis licensed under theMIT License— seeLICENSE. The MIT grant
covers the code only; the non-commercial asset restriction above is carved out in theLICENSEscope
note.Munder Difflinis an affectionate parody and is not affiliated with NBC'sThe Officeor
Dunder Mifflin.

## Acknowledgements

* LimeZu— pixel-art tilesets and character base sheets.
* shahar061/the-office— office tileset/map vendoring.
* Pixi.js·xterm.js·node-pty·electron-vite·CodeMirror— the libraries this is built on.
* Remotion— the landing page's animated "how it works" clips (landing-remotion/).
* The Office(US) — for Munder Difflin, Inc.