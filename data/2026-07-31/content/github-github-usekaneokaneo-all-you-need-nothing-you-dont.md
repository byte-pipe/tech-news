---
title: 'GitHub - usekaneo/kaneo: 🎯 All you need. Nothing you don''t. Open source project management that works for you, not against you. · GitHub'
url: https://github.com/usekaneo/kaneo
site_name: github
content_file: github-github-usekaneokaneo-all-you-need-nothing-you-dont
fetched_at: '2026-07-31T11:44:08.030538'
original_url: https://github.com/usekaneo/kaneo
author: usekaneo
description: 🎯 All you need. Nothing you don't. Open source project management that works for you, not against you. - usekaneo/kaneo
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 usekaneo

 

/

kaneo

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork423
* Star4.6k

 
 
 
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

2,312 Commits
2,312 Commits
.agents/
skills/
coss
.agents/
skills/
coss
 
 
.claude/
skills
.claude/
skills
 
 
.cursor/
rules
.cursor/
rules
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.husky
.husky
 
 
.vscode
.vscode
 
 
apps
apps
 
 
charts/
kaneo
charts/
kaneo
 
 
deploy
deploy
 
 
i18n
i18n
 
 
packages
packages
 
 
plans
plans
 
 
scripts/
i18n
scripts/
i18n
 
 
skills
skills
 
 
tests
tests
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.env.sample
.env.sample
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTORS.svg
CONTRIBUTORS.svg
 
 
Dockerfile.kaneo
Dockerfile.kaneo
 
 
ENVIRONMENT_SETUP.md
ENVIRONMENT_SETUP.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
biome.json
biome.json
 
 
commitlint.config.js
commitlint.config.js
 
 
compose.local.yml
compose.local.yml
 
 
compose.yml
compose.yml
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
skills-lock.json
skills-lock.json
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

### Quick Start|Website|Cloud|Discord

## Why Kaneo?

After years of using bloated, overcomplicated project management platforms that distracted from actual work, we built Kaneo to be different.

The problem with most tools isn't that they lack features—it's that they havetoo many. Every notification, every unnecessary button, every complex workflow pulls your team away from what matters:building great products.

We believe the best tools areinvisible. They should amplify your team's natural workflow, not force you to adapt to theirs. Kaneo is built on the principle thatless is more—every feature exists because it solves a real problem, not because it looks impressive in a demo.

What makes it different:

* Clean interfacethat focuses on your work, not the tool
* Self-hostedso your data stays yours
* Actually fastbecause we care about performance
* Open sourcewith a permissive MIT license

Learn more about Kaneo's features and capabilities in ourdocumentation.

## Sponsors

Kaneo is open source. If you find it useful, considersponsoring the projectto help support ongoing development.

## Getting Started

### One-Click Deployment with drim

For straightforward deployments, usedrim- a CLI tool that handles everything for you:

curl -fsSL https://assets.kaneo.app/install.sh 
|
 sh
drim setup

That's it. Your Kaneo instance will be running with automatic HTTPS, database setup, and all services configured.

Perfect for quick deployments and production setups where you want things to just work.

### Quick Start with Docker Compose

The fastest way to try Kaneo is with Docker Compose. This sets up Kaneo and PostgreSQL with a single Kaneo container:

services
:
 
postgres
:
 
image
: 
postgres:16-alpine

 
env_file
:
 - 
.env

 
ports
:
 - 
"
5432:5432
"

 
volumes
:
 - 
postgres_data:/var/lib/postgresql/data

 
restart
: 
unless-stopped

 
healthcheck
:
 
test
: 
["CMD-SHELL", "pg_isready -U kaneo -d kaneo"]

 
interval
: 
10s

 
timeout
: 
5s

 
retries
: 
5

 
kaneo
:
 
image
: 
ghcr.io/usekaneo/kaneo:latest

 
ports
:
 - 
"
5173:5173
"

 
env_file
:
 - 
.env

 
depends_on
:
 
postgres
:
 
condition
: 
service_healthy

 
restart
: 
unless-stopped

volumes
:
 
postgres_data
:

Save this ascompose.yml, copy.env.sampleto.env, uncommentKANEO_CLIENT_URL=http://localhost:5173, and setPOSTGRES_PASSWORD=<password>andAUTH_SECRET=<output of openssl rand -hex 32>, rundocker compose up -d, and openhttp://localhost:5173.

In Docker Compose, the bundled Kaneo container reaches PostgreSQL at the service hostnamepostgres.
If you run the API on your host instead of inside Compose, uselocalhostor setDATABASE_URLexplicitly.

Important:See ourfull documentationfor detailed setup instructions, environment variable configuration, and troubleshooting guides.

### Development Setup

For development, see ourEnvironment Setup Guidefor detailed instructions on configuring environment variables and troubleshooting common issues like CORS problems.

### Configuration

Kaneo requires several environment variables to be configured. The Docker Compose setup above handles the database automatically, but you'll need to configure environment variables for the API and web services.

For complete configuration instructions, including all required environment variables, database setup for non-Docker deployments, and advanced settings, see thedocumentation. Advanced deployments can still use the separateghcr.io/usekaneo/apiandghcr.io/usekaneo/webimages.

## Kubernetes Deployment

If you're running Kubernetes, we provide a comprehensive Helm chart. Check out theHelm chart documentationfor detailed installation instructions, production configuration examples, TLS setup, and more.

## Development

Want to hack on Kaneo? See ourEnvironment Setup Guidefor detailed instructions on configuring environment variables and troubleshooting common issues like CORS problems.

Quick start:

#
 Clone and install dependencies

git clone https://github.com/usekaneo/kaneo.git

cd
 kaneo
pnpm install

#
 Create a .env file in the root with required environment variables

#
 See ENVIRONMENT_SETUP.md for detailed instructions

#
 Start development servers

pnpm dev

For contributing guidelines, code structure, and development best practices, check out ourcontributing guideanddocumentation.

## Community

* Discord- Chat with users and contributors
* GitHub Issues- Bug reports and feature requests
* Documentation- Detailed guides, API docs, and tutorials

## Contributing

We're always looking for help, whether that's:

* Reporting bugs or suggesting features
* Improving documentation
* Contributing code
* Helping other users on Discord

Check outCONTRIBUTING.mdfor the details on how to get involved.

## License

MIT License - seeLICENSEfor details.

Built with ❤️ by the Kaneo team andcontributors