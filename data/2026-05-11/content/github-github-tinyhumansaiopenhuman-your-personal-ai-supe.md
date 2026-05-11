---
title: 'GitHub - tinyhumansai/openhuman: Your Personal AI super intelligence. Private, Simple and extremely powerful. · GitHub'
url: https://github.com/tinyhumansai/openhuman
site_name: github
content_file: github-github-tinyhumansaiopenhuman-your-personal-ai-supe
fetched_at: '2026-05-11T13:46:44.645412'
original_url: https://github.com/tinyhumansai/openhuman
author: tinyhumansai
description: Your Personal AI super intelligence. Private, Simple and extremely powerful. - tinyhumansai/openhuman
---

tinyhumansai

 

/

openhuman

Public

* NotificationsYou must be signed in to change notification settings
* Fork144
* Star1k

 
 
 
 
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

1,660 Commits
1,660 Commits
.agents/
agents
.agents/
agents
 
 
.claude
.claude
 
 
.codex/
commands
.codex/
commands
 
 
.do
.do
 
 
.github
.github
 
 
.husky
.husky
 
 
.vscode
.vscode
 
 
app
app
 
 
docs
docs
 
 
e2e
e2e
 
 
examples
examples
 
 
gitbooks
gitbooks
 
 
packages
packages
 
 
remotion
remotion
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
AGENTS.md
AGENTS.md
 
 
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
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
docker-compose.yml
docker-compose.yml
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
View all files

## Repository files navigation

# OpenHuman

OpenHuman is your Personal AI super intelligence. Private, Simple and extremely powerful.

Discord•Reddit•X/Twitter•Docs•Follow @senamakel (Creator)

Early Beta: Under active development. Expect rough edges.

To install or get started, either download from the website over attinyhumans.ai/openhumanor run

# Download DMG, EXEs over at https://tinyhumans.ai/openhuman or run in from your terminal

# For MacOS/Linux
curl -fsSL https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.sh | bash

# For Windows
irm https://raw.githubusercontent.com/tinyhumansai/openhuman/main/scripts/install.ps1 | iex

# What is OpenHuman?

OpenHuman is an open-source agentic assistant designed to integrate with you in your daily life. Each bullet links to the deeper writeup in thedocs.

* Simple, UI-first & HumanA clean desktop experience and short onboarding paths take you from install to a working agent in a few clicks — no config-first setup, no terminal required. The agent hasa face: a desktop mascot that speaks, reacts to its surroundings,joins your Google Meetsas a real participant, remembers you across weeks, and keeps thinking in the background even when you've stopped typing.
* 118+ third-party integrationswithauto-fetch: plug into Gmail, Notion, GitHub, Slack, Stripe, Calendar, Drive, Linear, Jira and the rest of your stack withone-click OAuth. Every connection is exposed to the agent as a typed tool, and every twenty minutes the core walks each active connection and pulls fresh data into thememory tree. No prompts, no polling loops you have to write, so the agent already has tomorrow's context this morning.
* Memory Tree+Obsidian Wiki: a local-first knowledge base built from your data and your activity. Everything you connect is canonicalized into ≤3k-token Markdown chunks, scored, and folded into hierarchical summary trees stored inSQLite on your machine. The same chunks land as.mdfiles in an Obsidian-compatible vault you can open, browse and edit, inspired by Karpathy'sobsidian-wiki workflow.
* Batteries included: web search, a web-fetchscraper, a full coder toolset (filesystem, git, lint, test, grep), andnative voice(STT in, ElevenLabs TTS out, mascot lip-sync, live Google Meet agent) are wired in by default.Model routingsends each task to the right LLM (reasoning, fast, or vision) under one subscription. No "install a plugin to read files" friction.Optional local AI via Ollamafor on-device workloads.
* Smart token compression (TokenJuice): every tool call, scrape result, email body, and search payload is run through a token compression layer before it touches any LLM Model. HTML is converted to Markdown, long URLs are shortened, non-Asccii characters are removed etc... You get the same information but at a fraction of the tokens. Reducing costs & increasing latency by upto 80%.
* Messaging channelsandprivacy & security: inbound/outbound across the channels you already use, with workflow data that stays on device, encrypted locally, treated as yours.

For contributors: Read theArchitecture·Getting Set Up·Cloud Deploy·CONTRIBUTING.md.

## Context in minutes, not weeks

OpenHuman is the first agent harness that gets to know you in minutes. Inspired byKarpathy's LLM Knowledgebase. Most agents start cold. Hermes learns by watching you work; OpenClaw waits for plugins to ferry context in. Either way, you spend days or weeks before the agent knows enough about your stack to be genuinely useful.

OpenHuman summarizes and compresses all your documents, emails & chats; and creates a memory graph that lets your agent remember everything about you.

OpenHuman skips the wait. Connect your accounts, letauto-fetchpull data locally on a 20-minute loop, and then haveMemory Treescompresses everything into Markdown files stored intelligently in aKarpathy-style Obsidian wiki.

In just one sync pass and the agent has full (compressed) context your inbox, your calendar, your repos, your docs, your messages. No training period. No "give it a few weeks.". It becomes you, controlled by you.

## OpenHuman vs Other Agent Harnesses

High-level comparison (products evolve, so verify against each vendor). OpenHuman is built tominimize vendor sprawl, keepworkflow knowledge on-device, and give the agent apersistent memoryof your data, not only chat.

Claude Cowork

OpenClaw

Hermes Agent

OpenHuman

Open-source

🚫 Proprietary

✅ MIT

✅ MIT

✅ GNU

Simple to start

✅ Desktop + CLI

⚠️
 Terminal-first

⚠️
 Terminal-first

✅ Clean UI, minutes

Cost

⚠️
 Sub + add-ons

⚠️
 BYO models

⚠️
 BYO models

✅ One sub + TokenJuice

Memory

✅ Chat-scoped

⚠️
 Plugin-reliant

✅ Self-learning

🚀 Memory Tree + Obsidian vault

Integrations

⚠️
 Few connectors

⚠️
 BYO

⚠️
 BYO

🚀 118+ via OAuth

Auto-fetch

🚫 None

🚫 None

🚫 None

✅ 20-min sync into memory

API sprawl

🚫 Extra keys

🚫 BYOK

🚫 Multi-vendor

✅ One account

Model routing

🚫 Single model

⚠️
 Manual

⚠️
 Manual

✅ Built-in

Native tools

✅ Code-only

✅ Code-only

✅ Code-only

✅ Code + search + scraper + voice

# Star us on GitHub

Building toward AGI and artificial consciousness? Star the repo and help others find the path.

# Contributors Hall of Fame

Show some love and end up in the hall of fame. Contributors get free merch and special access to ourDiscord.

## About

Your Personal AI super intelligence. Private, Simple and extremely powerful.

tinyhumans.ai/openhuman

### Resources

 Readme

 

### License

 GPL-3.0 license
 

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

1k

 stars
 

### Watchers

18

 watching
 

### Forks

144

 forks
 

 Report repository

 

## Releases31

OpenHuman v0.53.22

 Latest

 

May 9, 2026

 

+ 30 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust69.6%
* TypeScript26.4%
* JavaScript2.1%
* Shell1.6%
* CSS0.2%
* PowerShell0.1%