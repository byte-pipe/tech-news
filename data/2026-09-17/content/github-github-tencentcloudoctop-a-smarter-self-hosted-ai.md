---
title: 'GitHub - TencentCloud/Octop: A smarter, self-hosted AI assistant — multi-user, multi-agent. · GitHub'
url: https://github.com/TencentCloud/Octop
site_name: github
content_file: github-github-tencentcloudoctop-a-smarter-self-hosted-ai
fetched_at: '2026-09-17T15:26:50.899913'
original_url: https://github.com/TencentCloud/Octop
author: TencentCloud
description: A smarter, self-hosted AI assistant — multi-user, multi-agent. - TencentCloud/Octop
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 TencentCloud

 

/

Octop

Public

* NotificationsYou must be signed in to change notification settings
* Fork344
* Star3.3k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

481 Commits
481 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.cursor/
skills/
publish
.cursor/
skills/
publish
 
 
.githooks
.githooks
 
 
.github
.github
 
 
dashboard
dashboard
 
 
desktop
desktop
 
 
docker
docker
 
 
docs
docs
 
 
fnos
fnos
 
 
plugins
plugins
 
 
scripts
scripts
 
 
src/
octop
src/
octop
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
README_CN.md
README_CN.md
 
 
SECURITY.md
SECURITY.md
 
 
conftest.py
conftest.py
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

A smarter, self-hosted AI assistant — multi-user, multi-agent.

Highlights·Overview·Core Technology·Features·Roadmap·Quick Start·Contents

English·中文

Octopis an open-source, self-hosted AI assistant. It's not just a tool — it's a digital life form that can operate in parallel. Through its multi-agent architecture, it builds an intelligent environment that is both independent and collaborative for teams, families, and individuals. Best of all, it runs entirely on your machine — the fully self-hosted design means privacy is never a compromise, while single-process startup makes the powerful web console, CLI, and IM integrations readily accessible.

Chat through the Web Dashboard, Feishu, DingTalk, QQ, Discord, WeCom, or programmatic HTTP/SSE/WebSocket. Extend capabilities with theexpert library,Connectors(OAuth + MCP), andACPintegration for IDE workflows.

## ✨ Highlights

Feature

Description

👥

Multi-user expert team

One admin, shared household; built-in expert library — switch specialists per scenario

🎭

MBTI personas

16 personality templates plus an interactive quiz — give each agent a distinct character

🔒

Security built-in

JWT multi-user isolation, tool approval, shell command guardrails, and PII redaction — data stays local

🔌

Connector ecosystem

Tencent suite (Docs, Weibo trends, News, …); OAuth and MCP gateway extend resource boundaries

💾

Pluggable backends

Local disk, Docker containers, PostgreSQL, or COS/S3 — AI operates inside isolated boundaries

🧠

Portable memory

Powered by harness-memory; memory migrates with the workspace

📚

Knowledge base

RAG over your documents; semantic retrieval grounds agent answers in your private corpus

🧩

Plugins

Extend Octop with third-party plugins; bundled plugins are seeded and toggled on demand

↔️

ACP bidirectional

octop acp
 for IDE/terminal AI; delegate to OpenCode / Claude Code with permission gates

💻

Terminal AI+

Interactive shell in the browser — AI-assisted command execution and troubleshooting

🌐

Browser AI+

Headless Chromium sessions for web automation, screenshots, and remote browsing

🖥️

Remote desktop

Live screen and input from the dashboard on Linux, Windows, and macOS — remote office work and GUI apps; one-click isolated desktop on headless Linux

🏠

Self-hosted

Dashboard, CLI, IM channels, and cron in one 
octop run
 — all data under 
~/.octop/

## 📌 Overview

Octop is a self-hosted AI assistant platform for households and small teams. It runs a single process that serves a web dashboard, a CLI, IM channels (Feishu, DingTalk, QQ, Discord, WeCom, and more), and cron automation — all sharing one control-plane database under~/.octop/(SQLite by default; PostgreSQL optional).

Octop's design goal: keep every conversation, workspace, and credential on your own machine, while giving each user a personal team of specialized agents they can switch between per task.

🐾 What can you do with Octop

* Personal assistant— let a dedicated agent write weekly reports, organize notes, and manage your schedule; memory persists with the workspace.
* Family sharing— one admin account, the whole household; assign different agents and experts per member.
* Team helper— multiple agents collaborate in parallel, bridging Feishu / DingTalk / WeCom to route tasks into group chats.
* Developer boost— delegate coding tasks to OpenCode / Claude Code via ACP, or troubleshoot from the terminal with AI assistance.
* Web automation— use Browser AI+ to fill forms, capture screenshots, and gather public info.
* Scheduled tasks— configure cron in natural language so the agent pushes or runs jobs on time every day.

## 🧠 Core Technology

Layer

Technology

Language

Python 3.12+

Web framework

FastAPI + uvicorn

Agent runtime

harness-agent

Gateway

harness-gateway

Control plane DB

SQLite (WAL, default) or PostgreSQL (optional)

Frontend

React 18 + TypeScript + Vite + Ant Design

Scheduling

APScheduler

ACP

agent-client-protocol

Build / quality

hatchling · ruff · mypy · pytest

Octop is built on the Harness stack — a set of focused runtimes that Octop composes into one process:

* harness-agent— Agent runtime: model routing, tools, skills, and conversation checkpointing.
* harness-gateway— multi-platform IM channel bridge that normalizes incoming messages into a single processing pipeline.
* harness-memory— hierarchical recall with full-text search, so an agent's memory travels with its workspace.
* harness-browser— CDP-based browser automation with persistent profiles for web tasks.

Instead of an external queue or message broker, Octop routes every surface — Web UI, IM, and cron — through one in-processHarnessProcessor. The result is a single, restart-safe process whose entire state is rebuilt from the control-plane database on boot (local SQLite by default; PostgreSQL optional).

## 🤔 Features

### Server & auth

* Multi-user JWT authentication with admin role
* First-run setup wizard (octop init)
* Interactive API docs at/api/docs(off by default — set"enable_api_docs": trueinconfig.jsonto enable)

### Agents

* Multiple agents per user; each has its own workspace, providers, channels, and cron
* 16 MBTI persona templates + custom system prompt
* Expert library scanned at boot (infra/agents/experts/library/)
* Workspace backends: local disk, COS, S3, and other remote stores

### Channels & automation

* IM channels: Feishu, DingTalk, QQ, Discord, WeCom, and more
* Proactive cron jobs with natural-language and slash-command triggers
* Unified message processing across Web UI, IM, and cron surfaces

### Surfaces

* Web dashboard— chat, agents, connectors, channels, cron, settings
* CLI—octop run,octop chat,octop acp, admin commands
* HTTP/SSE/WebSocket API— full programmatic access

### Knowledge & plugins

* Knowledge base— RAG over your documents; upload files and let semantic retrieval ground agent answers in your private corpus
* Plugins— install and manage third-party plugins (octop plugin); bundled plugins are seeded and toggled on demand from the dashboard

### ACP (Agent Client Protocol)

Octop supports ACP in two directions:

1. Inbound— external tools useyourOctop agentoctop acp --agent main#stdio ACP server for Zed, OpenCode, …
2. Outbound— Octop delegates to external coding agents* Dashboard →ACP(/acp): configure runners (global per user)
* Enableacp_runnerper agent, then delegate in chat

Built-in outbound runners include OpenCode, CodeBuddy, Claude Code, and Codex.

Full setup:docs/acp.md.

## 🧭 Roadmap

Here are our mid-to-long term plans:

* Shared resource pool— a central pool of skills and sub-agents that any user can drop into a new expert without rebuilding from scratch.
* Expert sharing— publish your experts to other users in the same deployment, so good configurations are reused instead of recreated.
* Browser & terminal polishing— browser skillrecording(capture a workflow and replay it as a skill) and a more capable terminal AI assistant.
* AgentTeams— let one coordinator autonomously schedule and orchestrate multiple experts to tackle multi-step tasks.
* Self-evolution— automatically distill everyday conversations into reusable skills, so the assistant grows with you.
* PC / mobile clients— native desktop and mobile apps alongside the web dashboard and IM channels.

This roadmap may shift as the community grows; treat it as indicative only.

## 🚀 Quick Start

### Prerequisites

* macOS / Linux / Windows
* No pre-installed Python required — the installer usesuvto provision Python 3.12 in an isolated venv under~/.octop/
* A modern multi-core CPU with a few GB of RAM for the process plus model/embedding caches; enough disk for the database, agent workspaces, and document corpora

### 1. Install

macOS / Linux— one-line installer (recommended):

curl -fsSL https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.sh 
|
 bash

Windows (PowerShell):

irm https:
//
finnie-1258344699.cos.ap-guangzhou.myqcloud.com
/
octop
/
install.ps1 
|
 iex

Windows (cmd)— download and run, or from a cloned repo:

curl -fsSL https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.bat -o install.bat
install.bat

After installation, open anew terminalor reload your shell:

source
 
~
/.zshrc 
#
 Zsh

#
 or

source
 
~
/.bashrc 
#
 Bash

The installer placesoctopon your PATH via~/.octop/bin. Optional extras:

#
 Browser automation (Playwright Chromium)

curl -fsSL https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.sh 
|
 bash -s -- --extras browser

#
 Feishu channel support

curl -fsSL https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.sh 
|
 bash -s -- --extras channels-feishu

Seescripts/README.mdfor all install options (--version,--from-source,--mirror, Windows flags).

Desktop app(GUI, no terminal) — grab the artifact for your platform fromGitHub Releases:

Platform

Artifact

Windows

Octop-desktop-windows-amd64-<version>.exe
 (64-bit) / 
Octop-desktop-windows-arm64-<version>.exe
 (ARM64) — NSIS installer

macOS

Octop-desktop-darwin-arm64-<version>.dmg
 (Apple Silicon) / 
Octop-desktop-darwin-amd64-<version>.dmg
 (Intel)

Linux

Octop-desktop-linux-amd64-<version>.tar.gz
 / 
Octop-desktop-linux-arm64-<version>.tar.gz

FnOS NAS

Octop-fnos-docker-<version>.fpk
 (Docker-backed) / 
Octop-fnos-native-<version>.fpk
 (no Docker) — install via App Center

Seedesktop/README.mdfor the desktop shell andfnos/README.mdfor the FnOS packaging guide.

Alternative — PyPI(if you already manage Python yourself):

pip install octop

#
 optional: pip install "octop[browser]"

#
 optional local ONNX embedding model cache (Models → Local): pip install "octop[local-embedding]"

#
 Downloads catalog weights under ~/.octop/embedding_models; not chat, not Memory.

From a source checkout with uv:

uv sync --extra local-embedding

### 2. Initialize

octop init

The interactive wizard creates the SQLite database, JWT secret, and first admin account under~/.octop/.

### 3. Run

#
 Foreground (API + Web dashboard)

octop run

#
 Custom host / port

octop run --host 0.0.0.0 --port 8088

#
 Register as a system service (systemd / launchd / Windows service)

octop service start

Openhttp://127.0.0.1:8088. With Docker, the first init generates a random admin password (written to/data/.octop/credential.txt) unlessOCTOP_DEFAULT_PASSWORDis set. Interactiveoctop init/ the setup wizard asks you to choose a password (≥8 characters, letters and digits).

### Docker (recommended for production)

#
 Build and start

docker compose -f docker/docker-compose.yml up -d

#
 Or build manually

bash docker/docker_build.sh
docker run -d \
 -p 8088:8088 \
 -v octop-data:/data/.octop \
 -e HOME=/data \
 -e OCTOP_DEFAULT_PASSWORD=
"
<strong-password-or-omit-for-random>
"
 \
 octop:latest

Openhttp://localhost:8088. First boot creates the admin account and writes the credentials to/data/.octop/credential.txtin the container. WithOCTOP_DEFAULT_PASSWORDunset a strong random password is generated; a password you set must be ≥8 characters with letters and digits (weak/common passwords are rejected by the app password policy and fall back to a random one). Override the username viaOCTOP_ADMIN_USERNAME.

Password policy:at least 8 characters with letters and digits.

Variable

Default

Description

OCTOP_PORT

8088

HTTP listen port

OCTOP_DEFAULT_PASSWORD

(unset)

First-run admin password (Docker bootstrap). Unset = random password written to 
credential.txt

OCTOP_ADMIN_USERNAME

admin

First-run admin username

OCTOP_DATA

~/.octop

Host data directory (compose bind mount)

See.env.examplefor the full list.

## 📑 Contents

* Highlights
* Overview
* Core Technology
* Features
* Roadmap
* Quick Start
* Deploy & UseInstall optionsConfigurationCLI referenceWeb dashboardData directory
* Install options
* Configuration
* CLI reference
* Web dashboard
* Data directory
* Architecture & DevArchitectureProject layoutDevelopment
* Architecture
* Project layout
* Development
* Project InfoSecurity & privacyContributingChangelogRelated projectsWeCom customer groupLicense
* Security & privacy
* Contributing
* Changelog
* Related projects
* WeCom customer group
* License

## 📦 Install options

Method

Platform

Description

Remote one-liner

macOS / Linux

curl …/octop/install.sh | bash

Remote one-liner

Windows

irm …/octop/install.ps1 | iex
 or 
install.bat

Local script

macOS / Linux

bash scripts/install.sh

Local script

Windows

scripts\install.bat
 or 
install.ps1

PyPI

Any

pip install octop
 or 
pip install "octop[browser]"

Docker

Any

docker/docker-compose.yml

All install scripts provision an isolated environment at~/.octop/venvand a~/.octop/bin/octopwrapper — they do not touch system Python.

### Upgrade

octop updatereplaces only the wheel/binary — your~/.octop/database, workspaces, secrets, andconfig.jsonare preserved:

octop update 
#
 fetch and install the latest octop, then restart the service if one is registered

The schema migrates automatically on next boot; runoctop initonly if the setup wizard prompts for a migration. Always back up first (octop backup) before a cross-version upgrade.

## ⚙️ Configuration

All runtime state lives in~/.octop/. Manage it via CLI or edit files directly.

#
 LLM providers and models

octop models
octop provider list

#
 IM channels

octop channel list
octop channel install

#
 Skills (per agent)

octop skills list --agent main

#
 Cron jobs

octop cron list
octop cron create --help

#
 Users (admin)

octop user list

### Supported LLM providers

OpenAI-compatible APIs, DashScope (Qwen), Ollama, and other presets — configure per agent in the dashboard or viaoctop provider.

### Supported channels

Channel

Credentials

Feishu

App ID, App Secret

DingTalk

App Key, App Secret

QQ

Bot AppID, Token

Discord

Bot Token

WeCom

Corp ID, Agent Secret

Web Dashboard

Enabled by default

## 📖 CLI reference

Command

Description

octop init

Bootstrap 
~/.octop/
 (DB, admin, JWT secret)

octop run

Start Octop in the foreground

octop service start

Install and start as a system service

octop service stop

Stop the system service

octop agent

Create, list, start/stop agents

octop channel

Install and manage IM channels

octop chats

REPL and session management

octop acp

Stdio ACP server for IDE integration

octop cron

Manage scheduled tasks

octop models

Provider presets and model resolution

octop skills

Enable/disable per-agent skills

octop plugin

Install and manage third-party plugins

octop backup

Export / restore backups

octop clean

Remove CLI state or wipe 
~/.octop/

octop update

Check for and install updates

Full reference:docs/cli.md.

## 🖥️ Web dashboard

Afteroctop run, openhttp://127.0.0.1:8088.

* Chat— real-time conversation with agents
* Agents— create agents, pick experts / MBTI personas, configure providers
* Connectors— OAuth apps and MCP gateways
* Channels— IM platform setup
* Cron— visual cron job management
* Knowledge base— manage document corpora and semantic retrieval
* Plugins— install, enable, and configure plugins
* ACP— configure outbound coding-agent runners
* Settings— users, security, TLS, system

Interactive API docs:http://127.0.0.1:8088/api/docs(disabled by default — enable by setting"enable_api_docs": trueinconfig.json)

## 📁 Data directory

~/.octop/ ← install & data root
├── config.json # process config (optional database section)
├── octop.db # SQLite — users, agents, channels, cron, …
├── secrets/ # JWT secret, channel tokens
├── agents/<agent_id>/ # per-agent workspace (SOUL.md, skills, …)
├── security/tool_guard/ # shell command allow/deny rules
├── logs/ # runtime logs
├── venv/ # uv-managed Python (installer layout)
└── bin/octop # PATH wrapper → venv/bin/octop

The control plane can also use PostgreSQL — setdatabaseinconfig.json, orOCTOP_DATABASE_*/ the first-run wizard. With PostgreSQL, agent memory reuses the same DSN by default (per-agent schema); to keep file-based memory, set"memory": { "backend": { "type": "sqlite" } }in the agent config. Seedocs/configuration.mdanddocs/adr/002-database-backends.md.

Seedocs/configuration.mdfor env vars andconfig.json.

## 🏗️ Architecture

OctopServer
 ├─ DatabasePool SQLite (WAL) or PostgreSQL
 ├─ SharedServices DI root — every repo + config
 ├─ ExpertCatalog scans agents/experts/library/ at boot
 ├─ UserManager
 │ └─ HarnessAgentManager (per user)
 │ └─ AgentRuntime (per agent)
 │ ├─ HarnessAgent Agent runtime (harness-agent)
 │ ├─ HarnessProcessor IM / UI / cron entry point
 │ ├─ ChannelManager IM connections (harness-gateway)
 │ └─ CronManager APScheduler
 └─ FastAPI app (uvicorn)

Single process. Restart rebuilds state from the control-plane database (local SQLite by default; PostgreSQL optional).

Seedocs/architecture.md,docs/adr/001-single-process-model.md, anddocs/adr/002-database-backends.md.

## 📁 Project layout

src/octop/
 config.py env-var config
 launch.py OctopServer boot + uvicorn
 infra/ business core (agents, gateway, cron, db, users, …)
 api/ HTTP layer — FastAPI app, routers, JWT, SSE
 cli/ CLI layer — Click commands
 dashboard/ built React SPA (wheel artifact)

dashboard/ frontend source (Vite) — edit here, run make build-frontend

docker/ Docker Compose, entrypoint, build & deploy scripts
tests/ unit/ + integration/

## 🛠️ Development

Prerequisites:Python 3.12+, Node 18+,uv

#
 Backend

make install 
#
 pip install -e ".[dev]"

make all 
#
 format-all + lint + typecheck + test (ship bar)

#
 Frontend (separate terminal)

make dev-frontend 
#
 Vite dev server on :5173 (override with VITE_DEV_PORT)

make build-frontend 
#
 production build → src/octop/dashboard/

cd
 dashboard 
&&
 npx tsc --noEmit

Individual targets:make test,make lint,make typecheck,make format.

## 🔒 Security & privacy

* Local-first: Config, chats, workspaces, and credentials live under~/.octop/on your machine.
* Multi-user isolation: JWT auth with per-user agents and workspaces.
* PII redaction & tool approval: sensitive data is redacted before it leaves the workspace, and risky tools or shell commands require explicit approval under the guardrail rules.
* Tool guardrails: User-editable shell command rules under~/.octop/security/tool_guard/.
* No vendor lock-in: Swap LLM providers, storage backends, and channels without rewriting agents.

## 🤝 Contributing

Contributions are welcome:

1. Fork the repository
2. Create a feature branch (git checkout -b feature/amazing-feature)
3. Runmake all(backend) ormake check-all(full stack) before submitting
4. Open a Pull Request

SeeCONTRIBUTING.mdfor the full guide. Security issues:SECURITY.md.

Module boundaries and coding conventions:AGENTS.md.

## 📋 Changelog

SeeCHANGELOG.mdfor release history.

## 🔗 Related projects

Project

Description

harness-agent

Agent runtime — model routing, tools, skills, checkpointing

harness-gateway

Multi-platform IM channel bridge

harness-memory

Hierarchical recall and FTS search

harness-browser

CDP browser automation with persistent profiles

Theseharness-*projects are being prepared for open-sourcing; repository links will be added once they are published.

## 💬 WeCom Customer Group (CN)

For the customer WeCom support group, scan:

Please scan the QR code to join the group. For any questions or assistance, please contact the group admin directly.

## 📄 License

This project is licensed under theMIT License.

## ✨ Contributors

Thanks to all contributors: