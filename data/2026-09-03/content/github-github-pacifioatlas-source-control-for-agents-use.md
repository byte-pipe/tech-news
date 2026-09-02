---
title: 'GitHub - pacifio/atlas: Source control for agents. Use multiple coding agents, track their changes and query them in one place · GitHub'
url: https://github.com/pacifio/atlas
site_name: github
content_file: github-github-pacifioatlas-source-control-for-agents-use
fetched_at: '2026-09-03T07:20:25.233448'
original_url: https://github.com/pacifio/atlas
author: pacifio
description: Source control for agents. Use multiple coding agents, track their changes and query them in one place - pacifio/atlas
---

pacifio

 

/

atlas

Public

* NotificationsYou must be signed in to change notification settings
* Fork185
* Star2.8k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

612 Commits
612 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
.husky
.husky
 
 
crates
crates
 
 
docs
docs
 
 
landing
landing
 
 
scripts
scripts
 
 
src-tauri
src-tauri
 
 
src
src
 
 
tests
tests
 
 
vendor/
codex
vendor/
codex
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.lintstagedrc.json
.lintstagedrc.json
 
 
.oxfmtrc.json
.oxfmtrc.json
 
 
.oxlintrc.json
.oxlintrc.json
 
 
ARCHITECTURE.md
ARCHITECTURE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTEXT.md
CONTEXT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
TELEMETRY.md
TELEMETRY.md
 
 
bump.sh
bump.sh
 
 
bun.lock
bun.lock
 
 
debump.sh
debump.sh
 
 
index.html
index.html
 
 
package.json
package.json
 
 
postcss.config.js
postcss.config.js
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.test.json
tsconfig.test.json
 
 
vite.config.ts
vite.config.ts
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

Download·Discord·Docs·Contributing·Issues

# Atlas

Atlas is source control for coding agents. Every agent run produces checkpoints: commits are linked back to the session that made it alongside the prompts, tool calls, and reasoning. You see which agent did exactly what and why.

Run Claude Code, Codex, Atlas's own agent, or anything from the ACP registry side by side against the same codebase, with shared memory so switching agents mid-task doesn't mean starting over.

* Every commit, explained.A checkpoint links a commit back to the session that produced it: prompts, tool calls, and file changes kept together, queryable months later.
* Run any agent, side by side.Claude Code, Codex, Atlas's own agent, and the wider ACP registry, all in the same window, against the same codebase. Switching agents mid-task doesn't mean starting over.
* One memory, every agent.A decision Claude Code made shows up in Codex's next prompt. Plans, file changes, failures, and architecture notes are shared automatically, matched on-device against what you're asking about.
* Your notes are agent context.Markdown in.atlas/knowledge/, plus theCLAUDE.mdandAGENTS.mdyou already wrote, feed every agent in the project.
* @anything into a prompt.Files, folders, symbols, branches, commits, notes, papers, and past sessions resolve locally before the prompt is sent.
* Local by default.Code, notes, and sessions stay on your machine. Sign in and create an organisation when you want to sync across a team.

Join the Discord·#generalchat ·#devbuild questions ·#feature-requestsideas ·#bugsreport breakage

Start withCONTRIBUTING.mdto send a change, oropen an issuefor anything you hit.

## Table of contents

* Why Atlas
* How it works
* Checkpoints
* Features
* Download
* Build from source
* Contributing
* Local by default
* Links

## Why Atlas

Agents now write a large share of the code and keep none of the reasoning behind it. Atlas records both, and makes them queryable: what changed, by whose agent, at what point in time.

* Agents start from zero every session.Atlas keeps a persistent on-device memory of decisions, plans, and changes, and pushes the relevant parts into every turn.
* Switching agents loses the thread.The first message of a new session carries a curated fact pack and the tail of your last one, even when that session ran on a different agent.
* You can't review what you can't see.Every session is stored and searchable, next to a real commit graph and file-level diffs of what actually landed.
* Context lives in ten places.The knowledge base,CLAUDE.md,AGENTS.md, Claude Code's memory files, and Codex's history fold into one index every agent reads from.
* Nothing is locked in.Notes are markdown, canvases are JSON, sessions are JSONL, and the editor is a file on disk. Close Atlas and pick up in vim. The one exception is the checkpoint record (which agent session produced which commit), which is SQLite in the project's gitignored.atlas/, because it is queried, not read.
* Built for agents from the ground up.The agent runtime, shared memory, and session history are the foundation the rest of the app is built on.

## How it works

Atlas runs your agents as they are, and enriches what they see.

Claude Code and Codex run as external subprocesses overACP, the most-used, most-tested path. The Atlas agent runs in-process onCersei, our Rust agent framework.

Beyond those, Atlas can spawn any agent in the ACP registry (Cursor, OpenCode, Kilo Code, and more), pulling in each one's official binary automatically. All of them go through the same send path, so everything below applies whichever one you pick.

Note

QA on the long tail of registry agents is ongoing.

Before your message reaches the agent, Atlas assembles context around it:

Injected

Where it comes from

When

@
 mentions

Resolved locally in Rust before the prompt is sent. Notes, skills, papers, and past sessions are inlined; files and folders resolve to a path

Every turn

Shared agent memory

Active plan, decisions, file changes, failures, and architecture notes, written by any agent

Every turn

Semantic matches

Your message is embedded on-device and matched against the project's memory index

Every turn

Session handoff

A curated fact pack plus the tail of your last session in this project, including one from a different agent

First message

What you already wrote

Knowledge notes, 
CLAUDE.md
, 
AGENTS.md
, Claude Code's memory files, and Codex's history, folded into one index

Continuously

* One path, no per-agent special-casing.Run your existing Claude Code or Codex subscription through Atlas and the session gets more context, with no change to how you work.
* Claude Code's memory is visible to Codex, and the reverse.Neither agent can read the other's history on its own.
* Folders resolve to a pointer, not a paste.@-ing a 5000-line file sends a path the agent reads on demand, so one mention doesn't occupy the context window for the rest of the session.
* Embedding runs on your machine.Retrieval never leaves the device.

## Checkpoints

A checkpoint is what a commit doesn't tell you on its own: which session produced it, what the agent was asked, the tool calls it made, and the reasoning behind the change, kept together instead of lost the moment the terminal scrolls.

Atlas records every agent session locally in.atlas/sessions.db, with secrets scrubbed before anything touches disk. When you commit (from any tool, even with Atlas closed), the commit is linked back to the session that produced it as a checkpoint, and links survive rebases and amends.

You don't have to read the raw transcript to get the context back: select a checkpoint and chat with it directly, and it answers from what actually happened in that session. Local mode works fully offline with no account.

## Features

### Agents

Capability

Description

Link

Multi-agent sessions

Claude Code, Codex, and Atlas's native agent, selectable per session and running in parallel across tabs. Sessions are independent of tabs, so switching never drops a run in flight

Chat & Sessions

Shared agent memory

On-device semantic index (local embeddings, HNSW search) that every agent reads from and writes to

Memory

@ mentions

Local resolution of files, folders, symbols, branches, commits, notes, skills, papers, and past sessions

Chat & Sessions

Skills

SKILL.md files scoped globally or per project, enabled per agent by symlinking into that agent's own skills directory

Skills

Packs

Install a GitHub repo of skills, subagents, commands, hooks, rules, and scripts, discovered through the skills.sh index

Skills

Model chat

Talk to a model directly in its own tab, with no agent loop around it

Chat & Sessions

Organisations

Sign in, create an organisation, and sync across devices and teammates

Organisations

### Agent history

Capability

Description

Session capture

Every session recorded to 
.atlas/sessions.db
: prompts, messages, tool calls, the files each one touched, and the patches it applied

Checkpoints

Each session linked to the commits it produced. Commits are observed rather than intercepted, so one made from a terminal, from another editor, or while Atlas was closed still finds its session

Survives history rewrites

Links re-point through amend and rebase by patch-id reconciliation. When a squash makes the link genuinely ambiguous, it orphans instead of guessing

Transcript import

Backfills your existing Claude Code history, so the record starts before you installed Atlas

Secrets scrubbed on write

Redaction runs before anything is persisted, so the local store is never itself a disclosure risk

Capture health

One signal per workspace, OK, Degraded, or Stopped, each with a reason and the next step

Mission control

Dashboard for agent activity: usage over time, consumption breakdown, timelines, and a filterable log table

Works with no account and no network.

### The workspace

Capability

Description

Link

Editor

CodeMirror editing surface, with per-project editor state restored across restarts

Editor

Git

Real commit graph with lane assignment, stage/unstage/commit, branch operations, and file-level diffs

Git & Diff

Terminal

Block terminal where each command carries its own output, exit code, and duration, plus a full interactive surface for 
vim
, 
htop
, and friends

Terminal

Knowledge base

Plain markdown notes in 
.atlas/knowledge/
, versioned next to the code, with backlinks, a link graph, and export to HTML or a standalone server binary

Knowledge base

Research

Search arXiv and Semantic Scholar, pull papers in, read them in-app, and 
@
-mention them into a prompt

Research

Browser

Native WebKit webview in a tab, with real logins, cookies, and a reader mode

Explorer

Spaces

Spatial board for notes and their connections, persisted as JSON in the project

Chat & Sessions

Split view

Up to three resizable columns, each with its own tabs

Editor

Activity log

Every significant event in the project, filterable, with rows you can pin across restarts

Timeline

## Download

Grab the latest.dmgfromtryatlas.ccor thereleases page.

Note

macOS is the supported platform.

## Build from source

Note

Linux and Windows build from the same Tauri codebase but are untested.

To use the Claude Code agent, install theclaudeCLI and put it on yourPATH. Atlas's native agent needs no external CLI.

RequiresBun,Rust(stable, viarustup), andXcode Command Line Tools.

Linux system dependencies (GTK 3, WebKit2GTK 4.1, GLib headers)

* Debian / Ubuntu / Linux Mint:sudo apt install -y libglib2.0-dev libgtk-3-dev libwebkit2gtk-4.1-dev
* Fedora / RHEL:sudo dnf install glib2-devel gtk3-devel webkit2gtk4.1-devel
* Arch Linux / Manjaro:sudo pacman -S glib2 gtk3 webkit2gtk-4.1
* openSUSE:sudo zypper install glib2-devel gtk3-devel webkit2gtk3-devel

git clone https://github.com/pacifio/atlas

cd
 atlas
bun install
bun run dev:app

The first Rust compile takes a few minutes; after that it is seconds. Usebun run devfor frontend-only iteration, though anything callinginvoke()needsdev:app.

Production builds:

bun run build:app 
#
 .app bundle

bun run build:app:dmg 
#
 .app + .dmg installer

## Contributing

SeeCONTRIBUTING.md. One thing catches people out:

* Feature work targets the current version branch, notmain.mainonly receives a finished version branch, and that merge is the release.

ARCHITECTURE.mdcovers how Atlas is built.SECURITY.mdcovers reporting vulnerabilities.

## Local by default

* Your code, notes, and sessions stay on your machine.Nothing is uploaded to run an agent.
* Secrets are scrubbed before anything is written to disk.Not before upload, before persistence.
* Session capture is local-only by default.TheCheckpointsrecord of your agent sessions is written to.atlas/sessions.dbon your machine and stays there. No account required, and nothing sent anywhere until you explicitly opt in to sync.
* Accounts are opt-in.Sign in to create an organisation and sync across devices and teammates.
* Anonymous usage analytics are on by default.Coarse metadata, never code or prompts.What's collected, and how to turn it off.

## Links

* Website:tryatlas.cc
* Docs:docs.tryatlas.cc
* Discord:discord.gg/GmnFggaPfP
* Issues:github.com/pacifio/atlas/issues
* Telemetry:what Atlas collects, and how to turn it off

## Contributors

## License

MIT. SeeLICENSE.