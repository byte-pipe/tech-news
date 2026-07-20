---
title: 'GitHub - oblien/openship: Self-hosted deployment platform · GitHub'
url: https://github.com/oblien/openship
site_name: github
content_file: github-github-oblienopenship-self-hosted-deployment-platf
fetched_at: '2026-07-20T11:57:58.738496'
original_url: https://github.com/oblien/openship
author: oblien
description: Self-hosted deployment platform. Contribute to oblien/openship development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 oblien

 

/

openship

Public

* NotificationsYou must be signed in to change notification settings
* Fork270
* Star3.9k

 
 
 
 
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

164 Commits
164 Commits
.github/
workflows
.github/
workflows
 
 
apps
apps
 
 
docs
docs
 
 
fixtures/
deploy
fixtures/
deploy
 
 
packages
packages
 
 
scripts
scripts
 
 
.bun-version
.bun-version
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.nvmrc
.nvmrc
 
 
.prettierrc
.prettierrc
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
bun.lock
bun.lock
 
 
docker-compose.yml
docker-compose.yml
 
 
openship.code-workspace
openship.code-workspace
 
 
package.json
package.json
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
release-advisories.json
release-advisories.json
 
 
tsconfig.base.json
tsconfig.base.json
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

# Openship

Open-source, self-hostable deployment platform with built-in CI/CD.Push code, ship containers, manage infrastructure — from a desktop app, web dashboard, or CLI.

Quick Start·Features·Interfaces·Docs·Contributing

## Quick Start

npm i -g openship 
#
 or: curl -fsSL https://get.openship.io | sh

openship up 
#
 installs Openship as a background service (starts on boot, auto-restarts)

openship openopens the dashboard;openship stopstops the service. Want a one-off attached run instead?openship up --foreground. To deploy a project:

cd
 your-project
openship init 
#
 link this directory to a project

openship deploy

Prefer Docker? Clone the repo and use the compose stack:

git clone https://github.com/oblien/openship.git 
&&
 
cd
 openship
cp .env.example .env
docker compose up -d

Or grab the desktop app (openship install, or download fromopenship.io).

## What It Does

Point it at a repo. Openship detects your stack, builds it, configures everything, and ships it — zero config files, zero pipelines, zero YAML.

Databases, domains, SSL, CDN, mail, backups — all managed from one place.

Works withOpenship Cloud(managed) orany Linux serveryou own. Solo devs shipping side projects and teams running production use the same tool.

## Features

Built-in CI/CD

Push-to-deploy, preview environments, staging/prod flows, rollbacks

Any stack

Node, Python, Go, Rust, PHP, Ruby, Java, .NET, Docker, monorepos

Full backend

Postgres, MySQL, MongoDB, Redis, workers, WebSockets, storage

Domains & SSL

Automatic Let's Encrypt, wildcards, unlimited domains, auto-renewal

CDN

Edge caching, HTTP/3, Brotli compression, instant purge

Mail server

Built-in SMTP with DKIM/SPF/DMARC — no Mailgun or SES needed

Backups

Scheduled, databases + volumes, one-click restore, export anytime

Real-time monitoring

Live build logs, container metrics, and resource usage streamed to your screen

Scaling

Auto-scaling on cloud, multi-node ready on self-hosted

Portability

Standard Docker containers — move between providers freely

Docker Compose

Deploy existing compose files as-is

## Deploy Anywhere

* Openship Cloud— managed, auto-scaling, zero setup
* Any VPS— Hetzner, DigitalOcean, Linode, OVH, and the rest
* Dedicated servers— bare metal, colo, homelab
* Multi-server— spread workloads across machines

Same interface regardless of where you deploy.

## Three Interfaces

* Desktop app— full GUI, real-time logs, one-click everything.
* Web dashboard— the same UI in the browser, built for teams.
* CLI— scriptable and CI-friendly.

AREST APIandMCP(AI agent protocol) round it out for automation and tooling integration. Full command and API reference atopenship.io/docs.

Note

The docs are still a work in progress — we're actively filling them out. If something's missing or unclear,contributionsare hugely welcome and help us get there faster.

## Status

Production-ready core, actively developed.

Coming next:multi-node clusters, load-balancing UI, private networking, advanced monitoring, and visual CI/CD pipelines.

## Contributing

SeeCONTRIBUTING.md.

## License

Openship isopen-sourcesoftware, licensed under theApache License 2.0.

You may use, run, modify, self-host, and distribute it — including in commercial
and closed-source products — under the terms of the Apache 2.0 license. SeeLICENSEfor the full text.

## About

Self-hosted deployment platform

openship.io

### Topics

 ai

 deployments

 self-hosted

 agents

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

3.9k

 stars
 

### Watchers

15

 watching
 

### Forks

270

 forks
 

 Report repository

 

## Releases7

Openship v0.1.11

 Latest

 

Jul 18, 2026

 

+ 6 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript88.3%
* MDX6.3%
* Shell2.9%
* CSS1.4%
* PLpgSQL0.4%
* Python0.2%
* Other0.5%