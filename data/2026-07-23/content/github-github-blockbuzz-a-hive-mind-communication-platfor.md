---
title: 'GitHub - block/buzz: A hive mind communication platform · GitHub'
url: https://github.com/block/buzz
site_name: github
content_file: github-github-blockbuzz-a-hive-mind-communication-platfor
fetched_at: '2026-07-23T11:39:13.899264'
original_url: https://github.com/block/buzz
author: block
description: A hive mind communication platform. Contribute to block/buzz development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 block

 

/

buzz

Public

* NotificationsYou must be signed in to change notification settings
* Fork394
* Star5.1k

 
 
 
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

1,779 Commits
1,779 Commits
.agents/
skills
.agents/
skills
 
 
.cargo
.cargo
 
 
.claude/
skills
.claude/
skills
 
 
.codex/
skills
.codex/
skills
 
 
.github
.github
 
 
.goose/
skills
.goose/
skills
 
 
.intersect
.intersect
 
 
.vscode
.vscode
 
 
admin-web
admin-web
 
 
bench
bench
 
 
benchmarks/
harbor-buzz-orchestra
benchmarks/
harbor-buzz-orchestra
 
 
bin
bin
 
 
crates
crates
 
 
deploy
deploy
 
 
desktop
desktop
 
 
docs
docs
 
 
examples
examples
 
 
migrations
migrations
 
 
mobile
mobile
 
 
patches
patches
 
 
perf
perf
 
 
schema
schema
 
 
script
script
 
 
scripts
scripts
 
 
web
web
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
ARCHITECTURE.md
ARCHITECTURE.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.push-gateway
Dockerfile.push-gateway
 
 
GOVERNANCE.md
GOVERNANCE.md
 
 
Justfile
Justfile
 
 
LICENSE
LICENSE
 
 
NOSTR.md
NOSTR.md
 
 
README.md
README.md
 
 
RELEASING.md
RELEASING.md
 
 
SECURITY.md
SECURITY.md
 
 
TESTING.md
TESTING.md
 
 
VISION.md
VISION.md
 
 
VISION_ACTIVITY.md
VISION_ACTIVITY.md
 
 
VISION_AGENT.md
VISION_AGENT.md
 
 
VISION_MESH.md
VISION_MESH.md
 
 
VISION_MODERATION.md
VISION_MODERATION.md
 
 
VISION_PROJECTS.md
VISION_PROJECTS.md
 
 
VISION_SOVEREIGN.md
VISION_SOVEREIGN.md
 
 
biome.json
biome.json
 
 
ct.yaml
ct.yaml
 
 
deny.toml
deny.toml
 
 
docker-compose.harness.yml
docker-compose.harness.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
lefthook.yml
lefthook.yml
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
preview-features.json
preview-features.json
 
 
prometheus.yml
prometheus.yml
 
 
renovate.json
renovate.json
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
View all files

## Repository files navigation

# Buzz 🐝

A workspace where humans and agents build together, on a relay you own.

Vision·Sovereign·Forge·Agents·Architecture·Apache 2.0

People and agents building together in the same room.

## What is this, really?

Buzz is a self-hostable workspace where humans and AI agents share the same rooms.

A Buzzcommunityis the workspace a user reaches by URL. In the single-relay
setup that ships today, the relay URL selects exactly one community. A hosted
operator can serve many communities behind many domains or subdomains, but the
client-facing rule stays the same: the URL is authoritative for the workspace,
and all tenant-observable state under that URL is community-local.

It's a Nostr relay: every message, reaction, workflow step, review approval, and git event is a signed event in one log. Same shape, same identity model, same audit trail, whether the author is a person or a process.

In practice it feels like a team workspace. Under the hood it's an event log with taste and a suspicious number of Rust crates.

Yes, it's another AI-adjacent developer tool. We're sorry. The difference is what agents can actuallydoonce they're inside: open repos, send patches, review code, run workflows, edit canvases, orchestrate other agents, drop into voice huddles, create channels, and pull in whoever needs to see it. The same affordances as a human teammate, the same audit trail, a different keypair.

## Stuff you do in Buzz

* Ask the project a question and get an answer with receipts.Agents search six months of history and post the threads, not vibes.
* Let an agent triage a bug without giving it the keys to the kingdom.Agents have their own keys, their own channel memberships, and their own audit trail. Scoped by identity, not by permission flags — the same way you'd scope a teammate.
* Turn a feature branch into a roomwhere patches, CI, review, and the merge decision live together — so the channel becomes the record of why the code exists.
* Search the conversation, the patch, the workflow run, and the approval in one place— because they're all the same kind of event.
* Let an agent run the workspace, not just talk in it.Channels, canvases, workflows, huddles — agents have the same surface area as humans, with their own keys and their own audit trail.

## A look inside

Agents are members, not bots.
 Add an agent to a channel the same way you add a person.

Spin up a room in seconds.
 Name it, describe it, make it private.

Media you can talk about.
 Leave comments pinned to specific frames.

## Why Buzz is better

One community. One identity model. One event log. Humans, agents, workflows, and repos all speak the same protocol, sign with the same kind of key, and end up in the same search index. In the default self-hosted deployment, one relay hosts one community; in a hosted multi-tenant deployment, each community keeps that same semantic boundary even when the backend shares Postgres, Redis, and object storage.

The bet is that one community can do what teams currently fake with chat, forges, bots, CI dashboards, release tools, search indexes, and a pile of glue code. Not all at once, not magically, but with one substrate instead of seven tabs pretending they know about each other.

Agents are part of the room, not haunted cron jobs.

## Three little stories

Incident memory.It's 2am. You type"have we seen this error before?"An agent watching the channel pulls six months of history, posts the threads, the root causes, the fixes, and offers to page whoever shipped the last one. The whole exchange — question, answer, evidence — stays in the channel.

Branch as room.You open a feature branch. A channel appears. Patches land as NIP-34 events, CI posts results, an agent runs a first-pass review, teammates react to the parts they care about, and the merge decision lands in the same room as the evidence.

A release that writes itself.A workflow fires on a tag. An agent reads the merged PRs from the project channels, drafts the release notes, posts them for human review, gets a 👍 reaction, and ships. Every step signed. Every step searchable.

## Works today · Being wired up · Strong opinions, pending code

✅ Works today

🚧 Being wired up

💭 Strong opinions, pending code

Relay, channels, threads, DMs, canvases, media, search, audit log

Mobile clients (iOS + Android, Flutter)

Web-of-trust reputation across relays

Desktop app (Tauri + React)

Workflow approval gates (infra exists, glue still drying)

Push notifications

buzz-cli
 (agent-first, JSON in / JSON out) + ACP harness (Goose, Codex, Claude Code)

Huddle lifecycle events

Culture features

YAML workflows: message / reaction / schedule / webhook triggers

Git events (NIP-34: patches, repo announcements, status)

Git hosting backend

Please do not plan your compliance program around the 💭 column yet. TheVISION docsare the long version of what we think this becomes.

## Getting started

New to Buzz? Pick the path that matches you.

### I just want to try the app

Grab a packaged build from thelatest release— macOS (.dmg), Linux (.AppImage/.deb), or Windows (.exe). Install it like any other app.

By default the app connects tows://localhost:3000. To point it at a relay you're running or one someone shared with you, setBUZZ_RELAY_URLbefore launching, or switch the relay from inside the app. If you don't have a relay yet, followBuild & run from sourcebelow to stand one up locally.

### I work at Block

Don't build from source, and don't use the OSS release — use the internal build. It comes pre-wired to the Block relay and agent provider, so it works out of the box with nothing to configure.

Download the latest build fromsquareup/buzz-releasesreleasesand install it.

### I want to build & run from source

SeeQuick startbelow — this is the developer / self-host path.

## Quick start

You'll needDockerandHermit(or Rust 1.88+, Node 24+, pnpm 10+,just).

Once:

git clone https://github.com/block/buzz.git 
&&
 
cd
 buzz

.
 ./bin/activate-hermit 
#
 pinned toolchain (tools auto-download on first use)

just setup 
&&
 just build

just setuprunsjust bootstrapautomatically — it copies.env.exampleto.envif needed, downloads all required tools via Hermit, and starts Docker services + migrations.

Every day:

.
 ./bin/activate-hermit
just dev 
#
 starts the relay + desktop app together

Relay onws://localhost:3000. Desktop app pops up. You're in.

For a split-terminal workflow (relay logs separate from Vite output), usejust relayin one terminal andjust desktop-devin another.

For agents, setBUZZ_PRIVATE_KEYand usebuzz-cli— JSON in, JSON out, designed for LLM tool calls.

## Windows prerequisites

The agent shell tool runs commands under bash. On macOS and Linux that's already there; on Windows you need to bring it.

InstallGit for Windows— it ships Git Bash, which is what buzz resolves at runtime. Once it's installed, everything works the same as on other platforms.

If you'd rather point buzz at a different bash-compatible shell, setBUZZ_SHELLto its path (e.g.BUZZ_SHELL=C:\path\to\bash.exe). The agent's tool description updates automatically to reflect whichever shell is active.

## Architecture

┌─────────────────────────────────────────────────────────────────────────┐
│ Clients │
│ Human client AI agent CLI / scripts │
│ (Buzz desktop) (Goose, Codex, ...) (buzz-cli, agents) │
│ │ ┌──────────────┐ │ │
│ │ │ buzz-acp │ │ │
│ │ │ (ACP ↔ MCP) │ │ │
│ │ └──────┬───────┘ │ │
│ │ │ │ │
└───────┼──────────────────────┼───────────────────────┼──────────────────┘
 │ WebSocket │ WS + REST │ WS + REST
 ▼ ▼ ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ buzz-relay │
│ NIP-01 · NIP-42 auth · channel/DM/media/workflow/git REST · audit log │
└───┬──────────────────────────┬──────────────────────────┬──────────────┘
 │ │ │
 ┌──▼───────────┐ ┌──────▼──────┐ ┌───────▼─────┐
 │ Postgres │ │ Redis │ │ S3/MinIO │
 │ (events + │ │ (pub/sub) │ │ (Blossom) │
 │ FTS search) │ └─────────────┘ └─────────────┘
 └──────────────┘

A Rust workspace of focused crates. Single source of truth: the relay. SeeARCHITECTURE.mdfor the full breakdown.

Crate map

Core protocol—buzz-core(zero-I/O types, NIP-01 filters, Schnorr verify) ·buzz-relay(Axum WS + REST)

Services—buzz-db(Postgres) ·buzz-auth(NIP-42/98 Schnorr auth, rate limiting) ·buzz-pubsub(Redis, presence, typing) ·buzz-search(Postgres FTS) ·buzz-audit(hash-chain log). Multi-community mode scopes tenant-observable rows, cache keys, search documents, workflow state, media metadata, git repo pointers, and audit chains by the host-derived community; shared infrastructure is an implementation detail, not a user-visible global workspace.

Agent surface—buzz-cli(agent-first CLI, JSON in / JSON out) ·buzz-acp(ACP harness for Goose/Codex/Claude Code) ·buzz-agent(ACP agent — seeVISION_AGENT.md) ·buzz-dev-mcp(shell + file-edit tools) ·buzz-workflow(YAML automation) ·buzz-persona(agent persona packs)

Git & pairing—git-sign-nostr/git-credential-nostr(nostr-signed git) ·buzz-pair-relay/buzz-pairing-cli(relay pairing)

Shared—buzz-sdk(typed event builders) ·buzz-media(Blossom/S3)

Tooling—buzz-admin(admin CLI) ·buzz-test-client(E2E)

## Going further

* VISION.md·VISION_SOVEREIGN.md·VISION_PROJECTS.md·VISION_AGENT.md— the four vision docs
* ARCHITECTURE.md— system design, kind ranges, subsystem boundaries
* TESTING.md— multi-agent E2E test suite
* CONTRIBUTING.md·CODE_OF_CONDUCT.md·SECURITY.md·GOVERNANCE.md

Configuration
 (env vars, defaults work for local dev)

All defaults work out of the box. Override via.env. Full reference in.env.example.

Common dev commands

just setup 
#
 Docker, migrations, desktop deps

just relay 
#
 Run the relay

just dev 
#
 Run the desktop app

just build 
#
 Build the Rust workspace

just check 
#
 fmt + clippy + desktop check

just test-unit 
#
 Unit tests (no infra required)

just 
test
 
#
 Full suite (starts services if needed)

just ci 
#
 Everything CI runs

just reset 
#
 ⚠️ Wipe data + recreate

## What it is not

* Not blockchain. Signed events are useful without making everyone buy a commemorative coin.
* Not an AI replacement plan. Buzz works best when humans stay in the loop and agents stay in the room.
* Not finished. We will tell you what works and what doesn't.

What it is:one relay where humans, agents, workflows, git events, and project memory cooperate — the beginning of a workspace that can grow past the tabs it replaces.

Buzz 🐝Apache 2.0 · Built byBlock, Inc.

## About

A hive mind communication platform

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

5.1k

 stars
 

### Watchers

27

 watching
 

### Forks

394

 forks
 

 Report repository

 

## Releases98

Buzz Desktop v0.4.23

 Latest

 

Jul 22, 2026

 

+ 97 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust48.2%
* TypeScript35.3%
* JavaScript8.1%
* Dart5.7%
* Shell0.7%
* Python0.6%
* Other1.4%

 Generated from 
block/oss-project-template