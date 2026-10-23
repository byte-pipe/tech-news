---
title: 'GitHub - elie222/rakazo: Open-source Grok Bot alternative. Choose your own model and sandbox. · GitHub'
url: https://github.com/elie222/rakazo
site_name: github
content_file: github-github-elie222rakazo-open-source-grok-bot-alternat
fetched_at: '2026-10-23T15:39:49.587756'
original_url: https://github.com/elie222/rakazo
author: elie222
description: Open-source Grok Bot alternative. Choose your own model and sandbox. - elie222/rakazo
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,718 Commits
1,718 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
skills
.agents/
skills
 
 
.github
.github
 
 
apps
apps
 
 
docs
docs
 
 
infra
infra
 
 
packages
packages
 
 
patches
patches
 
 
scripts
scripts
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
SECURITY.md
SECURITY.md
 
 
SETUP_PROMPT.md
SETUP_PROMPT.md
 
 
VISION.md
VISION.md
 
 
biome.json
biome.json
 
 
greptile.json
greptile.json
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
railway.json
railway.json
 
 
skills-lock.json
skills-lock.json
 
 
tsconfig.base.json
tsconfig.base.json
 
 
turbo.json
turbo.json
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

# Rakazo

English|简体中文

Rakazo is an open source AI agent for persistent teammates, and a self-hosted AI assistant you
can run on your own machine. It is available on the web, as an Electron desktop app, and oniPhoneandAndroid. Bring your own model
and computer provider, or run the complete stack locally.

It is an open source, self-hosted alternative to Grok Bot, Meta Muse, OpenAI Dots, Instinct,
OpenClaw, and Hermes Agent.

Rakazo is in beta. Learn more atrakazo.com.

## Features

* Persistent bots with their own conversations, memory, routines, and history
* Voice mode: speak replies, dictate, and call a bot. Bring your own ElevenLabs, OpenAI, Cartesia, or Fish Audio key
* Shared Team Computers and isolated Private computers
* Browser, terminal, file, and graphical desktop access
* Bots that can delegate to peer bots or short-lived subagents
* Bring-your-own model credentials through Pi
* App integrations through Composio or Pipedream Connect, plus user-installed Treg, remote MCP, and OpenAPI tool sources
* Docker, E2B, Daytona, CreateOS, Boat, and trusted local-computer support

## Demo

demo.mp4

## Thanks

* PromptLayer
* Inbox Zero
* CodeRabbit
* Greptile
* Snyk

## Stack

* TypeScript
* React 19, Vite, and Tailwind CSS
* Electron and Expo
* Hono and oRPC
* PostgreSQL and Prisma
* Better Auth
* Graphile Worker
* Pi
* Docker, E2B, Daytona, CreateOS, and Boat
* Composio, Pipedream Connect, MCP, and OpenAPI integrations

## Quick start (published images)

You need Docker Engine, the Compose plugin, curl, and OpenSSL. No clone or Node install.

mkdir -p rakazo 
&&
 
cd
 rakazo 
&&

curl -fsSLO https://raw.githubusercontent.com/elie222/rakazo/main/infra/compose/install-images.sh 
&&

bash install-images.sh

The installer downloads the Compose files, creates.envwith random secrets, and starts Rakazo.
It preserves an existing.envwhen rerun.

Openhttp://127.0.0.1:5173, create an account, and connect a model.
Local Docker computers are on by default. Optional remote providers:e2b,daytona,createos,boat, orrailwaywith the matching API key.

Default image tag isedge(main builds,linux/amd64+linux/arm64). Details and tags:self-hosting guide.

On restricted networks, override the installer download base (RAKAZO_DOWNLOAD_BASE), skip
existing Compose files (--local/RAKAZO_DOWNLOAD_SKIP_EXISTING), or mirror the bootstrap
script URL — seeRestricted networks / mirror downloads.

For an agent-assisted install, useSETUP_PROMPT.md.

## Run on a server

Bots stay on when the backend runs on a server. Use the same installer on a VPS, then connect from
the desktop app, the mobile app, or a browser.

bash install-images.sh --prepare-only

#
 edit .env: SANDBOX_PROVIDER=boat (or e2b / daytona / createos) with its API key, RAKAZO_HOST=your.domain

bash install-images.sh

Put HTTPS in front of port 5173;docs/self-host.mdcovers the Caddy setup and host hardening. In the desktop app chooseExisting instanceand enter
thehttps://address.

Ordeploy on Railway; see theRailway setup guide.

## Local development (source checkout)

You need Node.js 22.22.2 or newer in the 22.x line, Node.js 24.x, or Node.js 26+;
pnpm 9; and Docker. Node.js 23.x and 25.x are not supported.

git clone https://github.com/elie222/rakazo.git

cd
 rakazo
cp .env.example .env

SetPOSTGRES_PASSWORDandPOSTGRES_APP_PASSWORDto two values fromopenssl rand -hex 16,
then put them inDATABASE_MIGRATION_URLandDATABASE_URL. The app connects as its ownrakazo_applogin, which row-level security applies to; migrations run as the owner
(database roles). SetBETTER_AUTH_SECRET,ENCRYPTION_KEY, andSCREEN_PROXY_SECRETto
independent long random values. Docker sandboxes also need a dedicatedSANDBOX_SUPERVISOR_TOKEN. You can also setOPENROUTER_API_KEY, or connect a supported
model provider during onboarding.

For host-side development with Docker Desktop, setSANDBOX_CONTROL_VIA_LOOPBACK=truein.env. The supervisor discovers Docker Desktop's user socket automatically;DOCKER_HOSTorDOCKER_SOCKETcan override it for another Docker runtime.

Managed app catalogs are optional. SetCOMPOSIO_API_KEYfor Composio, or thePIPEDREAM_CLIENT_ID,PIPEDREAM_CLIENT_SECRET, andPIPEDREAM_PROJECT_IDtrio for Pipedream
Connect. Users can add an HTTPS MCP server, Treg endpoint, or OpenAPI JSON document fromIntegrationswithout enabling either managed catalog. Connector credentials are encrypted on the
server and are never returned by the API.

Treg is usage-metered. Self-hosters supply their own Treg token; operators embedding Treg in a
hosted product should reviewTreg's integration terms, which require
a written agreement for hosted resale.

docker compose --env-file .env \
 -f infra/compose/docker-compose.yml \
 -f infra/compose/docker-compose.postgres-host.yml \
 up postgres -d
pnpm install
pnpm db:generate
pnpm db:migrate
pnpm sandbox:build
pnpm dev

Postgres stays network-internal in the default Compose file (same as published images). Thepostgres-hostoverlay publishes loopback127.0.0.1:5433for host-sidepnpmand DB tools.
If that port is occupied, changePOSTGRES_HOST_PORTand the ports inDATABASE_URLandDATABASE_MIGRATION_URLin.env.
Without the overlay, open a shell withdocker compose --env-file .env -f infra/compose/docker-compose.yml exec postgres sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"'.
Use a URI-safePOSTGRES_PASSWORD(openssl rand -hex 16). An existingpgdatavolume keeps the
user, password, and database from first init, so keep those values in.env, or change them in
place withALTER ROLE/ rename. Recreate the volume only after a backup (or when the data is
disposable);docker compose down -vdeletes all Postgres state.

Openhttp://127.0.0.1:5173, create an account, connect a model, and create
your first bot.

For deployment, provider selection, backups, and upgrades, see theself-hosting guide.

To use CreateOS, setSANDBOX_PROVIDER=createosandCREATEOS_SANDBOX_API_KEY.
OptionalCREATEOS_SANDBOX_BASE_URL,CREATEOS_SANDBOX_SHAPE, andCREATEOS_SANDBOX_ROOTFSdefault tohttps://api.sb.createos.sh,s-2vcpu-2gb,
anddesktop:1.

To use Railway computers, setSANDBOX_PROVIDER=railway,RAILWAY_API_TOKENandRAILWAY_ENVIRONMENT_IDon the API and worker. Choose the sandbox environment
explicitly; Railway's automatic environment ID identifies the hosted app's environment.
Use the narrowest Railway API token that works: prefer a project token if sufficient
for sandbox operations and supported by the client's authentication. This provider
currently uses bearer authentication, so use a team/workspace token rather than a
personal account token.
The live screen and desktop requirePRIVATEnetworking so Railway's public domain
can serve the screen. Computers use this mode and can reach other services in the
same Railway project/environment, as well as the public internet. We recommend a
dedicated Railway project (or at least a separate environment) for sandboxes,
separate from the app and database. Recreate existingISOLATEDcomputers before use.
The desktop is installed on first start. Stopping a computer saves its portable
home and destroys the sandbox; the next start restores that home in a new sandbox.
Railway sandbox usage is metered.
New computers start in Railway's default region. SetRAILWAY_SANDBOX_REGION(for exampleasia-southeast1-eqsg3a) to keep them near the API; a running computer moves on its next start.
Workspace exports reject files above 64 MiB without truncating them. SetRAILWAY_MAX_WORKSPACE_FILE_BYTESto change this limit.

## Desktop and mobile

The Electron and Expo apps are clients of the same Rakazo API used by the web app.

With the development stack running, launch Electron with:

pnpm --filter @rakazo/desktop dev

On first run the desktop app asks whether to run Rakazo on this computer or connect to an existing
server.This computerinstalls and starts the published images with Docker Compose (the same
files asinfra/compose/install-images.sh) under the app's data directory, so Docker Desktop,
OrbStack, or Docker Engine must be installed; the app links to them when it is not. Installed
builds pin the image tag to their own version; unpackaged builds pulledge. Developers runningpnpm devshould pickExisting instancewithhttp://127.0.0.1:5173instead. Public servers
must use HTTPS; HTTP is accepted only for loopback and private LAN addresses (not link-local). The
app verifies Rakazo's health endpoint before saving, and later launches go straight to that
instance. The stack keeps running after the app quits;Stop Local Stackin the application
menu turns it off.

On Linux the desktop app ships as an AppImage, which needs FUSE 2 (libfuse.so.2). Distributions
that only include FUSE 3, such as Fedora Silverblue or Ubuntu 24.04, showdlopen(): error loading libfuse.so.2. Install the FUSE 2 library (fuse-libson Fedora,libfuse2t64on Ubuntu 24.04,libfuse2on older Ubuntu and Debian), or run the AppImage without
FUSE:

chmod +x Rakazo-
*
.AppImage
./Rakazo-
*
.AppImage --appimage-extract-and-run

This computerlooks for thedockerCLI and does not detect Podman. To try another
Docker-compatible CLI that supports thecomposecommands, setRAKAZO_DOCKER_BINARYto its path
before starting the app.

UseChange Rakazo Server…in the application menu to reconnect. Closing that window without
saving returns to the previous instance. For development automation, setRAKAZO_WEB_URLto point
the shell somewhere else without changing the saved instance, orRAKAZO_FORCE_SETUP=1to run
setup again.

Mobile build and release instructions live indocs/mobile-release.md.

## UI language

The web (and Electron-hosted) UI supports English, Deutsch, 한국어, Türkçe, हिन्दी,
Português (Brasil), 简体中文, Español, Русский, Français, עברית, and Nederlands underSettings → Language. The Expo app ships English, 简体中文, Русский, Deutsch, and
Nederlands catalogs, andAccount → Languagelists all five. A device language orEXPO_PUBLIC_DEFAULT_UI_LOCALEstill selects the starting catalog before a saved choice.
The marketing
homepage (apps/www) is available in en/de/ko/zh via footer language links (/,/de/,/ko/,/zh/); other marketing pages stay English. The Russian marketing homepage and
native Electron setup/menu remain separate follow-up work.

## Development

apps/ web, api, worker, desktop, mobile, and public website
packages/ domain, contracts, persistence, adapters, UI, and test tooling
infra/ local services and computer images
docs/ architecture, operations, and release guides

Common checks:

pnpm lint
pnpm check
pnpm 
test

pnpm test:integration
pnpm test:e2e

SeeCONTRIBUTING.mdfor the development workflow and test matrix.

## Documentation

* Self-hosting
* Self-host secrets
* Computer runtime and isolation
* Desktop releases
* Mobile releases
* Performance testing
* Manage the bots it creates

## How Rakazo compares

* Grok Bot
* Muse
* Dots
* Instinct
* OpenClaw
* Hermes Agent
* All comparisons

## Contributing

Contributions are welcome. Please readCONTRIBUTING.mdbefore opening a pull
request. For security vulnerabilities, followSECURITY.mdinstead of filing a public
issue.

Rakazo is licensed under theApache License 2.0.

Questions and ideas are welcome in theRakazo Discord community.