---
title: 'GitHub - BenedictKing/ccx: Claude / Codex / Gemini API Proxy - CCX · GitHub'
url: https://github.com/BenedictKing/ccx
site_name: github
content_file: github-github-benedictkingccx-claude-codex-gemini-api-pro
fetched_at: '2026-05-28T12:11:33.243678'
original_url: https://github.com/BenedictKing/ccx
author: BenedictKing
description: Claude / Codex / Gemini API Proxy - CCX. Contribute to BenedictKing/ccx development by creating an account on GitHub.
---

BenedictKing

 

/

ccx

Public

* NotificationsYou must be signed in to change notification settings
* Fork171
* Star2.3k

 
 
 
 
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

1,397 Commits
1,397 Commits
.agents/
skills
.agents/
skills
 
 
.claude/
skills
.claude/
skills
 
 
.github
.github
 
 
backend-go
backend-go
 
 
desktop
desktop
 
 
docs
docs
 
 
frontend
frontend
 
 
scripts
scripts
 
 
.claudeignore
.claudeignore
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.prettierrc
.prettierrc
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile_China
Dockerfile_China
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
VERSION
VERSION
 
 
docker-compose.watchtower.yml
docker-compose.watchtower.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
package-lock.json
package-lock.json
 
 
View all files

## Repository files navigation

# Claude / OpenAI Chat / OpenAI Images / Codex Responses / Gemini API Proxy - CCX

English |简体中文

CCX is a high-performance AI API proxy and protocol translation gateway for Claude, OpenAI Chat, OpenAI Images, Codex Responses, and Gemini. It provides a unified entrypoint, built-in web administration, channel orchestration, failover, multi-key management, and model routing.

## Features

* Integrated backend + frontend architecture with single-port deployment
* Dual-key authentication withPROXY_ACCESS_KEYand optionalADMIN_ACCESS_KEY
* Web admin console for channel management, testing, logs, and monitoring
* Support for Claude Messages, OpenAI Chat Completions, OpenAI Images, Codex Responses, and Gemini APIs
* Smart scheduling with priorities, promotion windows, health checks, failover, and circuit recovery
* Per-channel API key rotation, proxy support, custom headers, model allowlists, and route prefixes
* Responses session tracking for multi-turn workflows
* Embedded frontend assets for simple binary deployment

## Sponsor

Thanks to 
Youyun Zhisuan
 for sponsoring this project! Youyun Zhisuan is UCloud's AI cloud platform, offering cost-effective domestic AI model Agent Plan packages by monthly subscription or pay-as-you-go, starting from 49 CNY/month. It also provides stable access to official overseas models, supports Claude Code, Codex, and API integrations, and offers enterprise-grade high concurrency, 24/7 technical support, and self-service invoicing. Users who register through 
this link
 can receive a free 5 CNY platform trial credit.

## Screenshots

### Channel Orchestration

Visual channel management with drag-and-drop priority adjustment and real-time health monitoring.

### Add Channel

Supports multiple upstream service types and flexible API key, model mapping, and request parameter configuration.

### Traffic Stats

Real-time monitoring of per-channel request traffic, success rate, and latency.

## Architecture

CCX exposes one backend entrypoint:

Client -> backend :3000 ->
 |- / -> Web UI
 |- /api/* -> Admin API
 |- /v1/messages -> Claude Messages proxy
 |- /v1/chat/completions -> OpenAI Chat proxy
 |- /v1/responses -> Codex Responses proxy
 |- /v1/images/{...} -> OpenAI Images proxy
 |- /v1/models -> Models API
 `- /v1beta/models/* -> Gemini proxy

Images endpoints currently include:

* POST /v1/images/generations
* POST /v1/images/edits
* POST /v1/images/variations

SeeARCHITECTURE.mdfor the detailed design.

## Quick Start

### Option 0: CCX Desktop

If you prefer a desktop experience, start withCCX Desktop.

### Option 1: Binary

1. Download the latest binary fromReleases. Windows users can prefer the Microsoft Store build once published; Store handles signing and updates.
2. Create a.envfile next to the binary:

PROXY_ACCESS_KEY=your-proxy-access-key
PORT=3000
ENABLE_WEB_UI=true
APP_UI_LANGUAGE=en

1. Run the binary and openhttp://localhost:3000

On Windows, if the client runs from cmd, PowerShell, WSL, or Docker andlocalhostdoes not reach CCX, use the Windows host IPv4 address instead, for examplehttp://192.168.1.23:3000. CCX listens on all interfaces by default through:PORT.

For background startup without Docker, seeService Startup.

### Option 2: Docker

docker run -d \
 --name ccx \
 -p 3000:3000 \
 -e PROXY_ACCESS_KEY=your-proxy-access-key \
 -e APP_UI_LANGUAGE=en \
 -v 
$(
pwd
)
/.config:/app/.config \
 crpi-i19l8zl0ugidq97v.cn-hangzhou.personal.cr.aliyuncs.com/bene/ccx:latest

Run in the background with Docker Compose:

docker compose up -d

Enable Watchtower auto-update:

docker compose -f docker-compose.yml -f docker-compose.watchtower.yml up -d

Pull the latest image immediately after setup if needed:

docker compose pull ccx
docker compose up -d ccx

### Option 3: Build From Source

git clone https://github.com/BenedictKing/ccx

cd
 ccx
cp backend-go/.env.example backend-go/.env
make run

Useful commands:

make dev
make run
make build
make frontend-dev

## Core Environment Variables

PORT=3000
ENV=production
ENABLE_WEB_UI=true
PROXY_ACCESS_KEY=your-proxy-access-key
ADMIN_ACCESS_KEY=your-admin-secret-key
APP_UI_LANGUAGE=en
LOG_LEVEL=info
REQUEST_TIMEOUT=300000

## Main Endpoints

* Web UI:GET /
* Health:GET /health
* Admin API:/api/*
* Claude Messages:POST /v1/messages
* OpenAI Chat:POST /v1/chat/completions
* Codex Responses:POST /v1/responses
* OpenAI Images:POST /v1/images/generations,POST /v1/images/edits,POST /v1/images/variations
* Gemini:POST /v1beta/models/{model}:generateContent
* Models API:GET /v1/models

## Development

Recommended local workflow:

make dev

Frontend only:

cd
 
"
frontend
"

bun install
bun run dev

Backend only:

cd
 
"
backend-go
"

make dev

## Additional Docs

* CCX Desktop
* Client Setup
* CCX Desktop (中文)
* Client Setup (中文)
* README.zh-CN.md
* backend-go/README.md
* ARCHITECTURE.md
* DEVELOPMENT.md
* ENVIRONMENT.md
* docs/service/README.md- non-Docker service startup
* RELEASE.md

## Community

Join the QQ group for discussion:642217364

## Star History

## License

MIT

## About

Claude / Codex / Gemini API Proxy - CCX

benedictking.github.io/ccx/

### Topics

 gemini

 codex

 claude

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

2.3k

 stars
 

### Watchers

9

 watching
 

### Forks

171

 forks
 

 Report repository

 

## Releases82

v2.8.10

 Latest

 

May 28, 2026

 

+ 81 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go72.2%
* Vue15.3%
* TypeScript11.3%
* CSS0.3%
* NSIS0.3%
* Makefile0.2%
* Other0.4%