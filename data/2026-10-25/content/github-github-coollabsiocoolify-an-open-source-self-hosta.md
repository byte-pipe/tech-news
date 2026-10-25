---
title: 'GitHub - coollabsio/coolify: An open-source, self-hostable PaaS alternative to Vercel, Heroku & Netlify that lets you easily deploy static sites, databases, full-stack applications and 360+ one-click services on your own servers. · GitHub'
url: https://github.com/coollabsio/coolify
site_name: github
content_file: github-github-coollabsiocoolify-an-open-source-self-hosta
fetched_at: '2026-10-25T14:48:46.631275'
original_url: https://github.com/coollabsio/coolify
author: coollabsio
description: An open-source, self-hostable PaaS alternative to Vercel, Heroku & Netlify that lets you easily deploy static sites, databases, full-stack applications and 360+ one-click services on your own servers. - coollabsio/coolify
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

18,278 Commits
18,278 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
skills
.agents/
skills
 
 
.ai
.ai
 
 
.claude/
skills
.claude/
skills
 
 
.codex
.codex
 
 
.cursor
.cursor
 
 
.dev
.dev
 
 
.github
.github
 
 
app
app
 
 
bootstrap
bootstrap
 
 
changelogs
changelogs
 
 
config
config
 
 
database
database
 
 
docker
docker
 
 
docs
docs
 
 
lang
lang
 
 
other
other
 
 
public
public
 
 
resources
resources
 
 
routes
routes
 
 
scripts
scripts
 
 
storage
storage
 
 
svgs
svgs
 
 
templates
templates
 
 
tests
tests
 
 
.coolify-logo
.coolify-logo
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.env.development.example
.env.development.example
 
 
.env.dusk.ci
.env.dusk.ci
 
 
.env.production
.env.production
 
 
.env.testing
.env.testing
 
 
.env.windows-docker-desktop.example
.env.windows-docker-desktop.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.mcp.json
.mcp.json
 
 
.phpactor.json
.phpactor.json
 
 
AGENTS.md
AGENTS.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
DESIGN.md
DESIGN.md
 
 
DEVELOPMENT.md
DEVELOPMENT.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
RELEASE.md
RELEASE.md
 
 
SECURITY.md
SECURITY.md
 
 
SECURITY_ADVISORY.md
SECURITY_ADVISORY.md
 
 
TECH_STACK.md
TECH_STACK.md
 
 
artisan
artisan
 
 
boost.json
boost.json
 
 
bun.lock
bun.lock
 
 
cliff.toml
cliff.toml
 
 
composer.json
composer.json
 
 
composer.lock
composer.lock
 
 
docker-compose-maxio.dev.yml
docker-compose-maxio.dev.yml
 
 
docker-compose.dev-multi.yml
docker-compose.dev-multi.yml
 
 
docker-compose.dev-side-by-side.yml
docker-compose.dev-side-by-side.yml
 
 
docker-compose.dev.yml
docker-compose.dev.yml
 
 
docker-compose.prod.yml
docker-compose.prod.yml
 
 
docker-compose.windows.yml
docker-compose.windows.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
jean.json
jean.json
 
 
openapi.json
openapi.json
 
 
openapi.yaml
openapi.yaml
 
 
opencode.json
opencode.json
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
phpunit.dusk.xml
phpunit.dusk.xml
 
 
phpunit.xml
phpunit.xml
 
 
pint.json
pint.json
 
 
postcss.config.cjs
postcss.config.cjs
 
 
rector.php
rector.php
 
 
skills-lock.json
skills-lock.json
 
 
versions.json
versions.json
 
 
vet.json
vet.json
 
 
vite.config.js
vite.config.js
 
 
View all files

## Repository files navigation

# Coolify

An open-source platform to deploy applications, databases, and services on your own servers.

Open source & free forever, backed by ourphilosophy.

Website·Documentation·Cloud·Discord·Community

## What is Coolify?

Coolify is an open-source and self-hostable alternative to Heroku, Netlify, and Vercel. It helps you manage servers, applications, and databases on your own hardware. You only need an SSH connection.

You can use a VPS, a bare-metal server, a Raspberry Pi, or any other server that accepts SSH connections. Coolify gives you the convenience of a cloud platform while you keep control of your infrastructure.

Your configurations stay on your servers. If you stop using Coolify, your running resources continue to work and remain manageable.

## What can Coolify do?

* Deploy any application:Build from GitHub, GitLab, Bitbucket, or Gitea with Nixpacks, Railpack, Dockerfile, Docker Compose, or a prebuilt Docker image.
* Run databases and services:Deploy managed databases and more than 360 one-click services with persistent storage and generated credentials.
* Automate deployments:Deploy on every Git push, create pull-request previews, call deployment webhooks, and roll back to retained application images.
* Manage networking:Configure custom domains, automatic HTTPS certificates, reverse proxies, health checks, and container networks.
* Operate your infrastructure:Manage multiple servers, inspect deployment and runtime logs, open container terminals, and monitor resource status.
* Protect your workloads:Configure database and storage backups, scheduled tasks, environment variables, secrets, and notifications.
* Integrate with your workflow:Manage resources through the dashboard, API, CLI, MCP, and team-based access controls.

## Quick start

Install Coolify on a supported server with one command:

curl -fsSL https://cdn.coollabs.io/coolify/install.sh 
|
 bash

Read theinstallation guidefor requirements and detailed instructions. You can also review theinstallation scriptbefore you run it.

## Self-hosted or Cloud

Self-hosted

Coolify Cloud

Install Coolify on your own server.

Use a Coolify instance that we maintain.

Control and maintain the complete platform.

Get high availability and less maintenance.

Free and open source.

Paid service with email notifications and additional support.

The recommended self-hosted setup uses one server for Coolify and one or more servers for deployed resources. If you do not want to maintain the Coolify server, useCoolify Cloud. Seecoolify.iofor current pricing.

## Community and support

* Read thedocumentation.
* Join the community onDiscord.
* Ask questions inGitHub Discussions.
* Read thecontribution guidebefore you submit a change.
* Review thecode of conduct.
* Contact the team through thesupport page.

## Donations

To stay completely free and open-source, with no feature behind the paywall and evolve the project, we need your help. If you like Coolify, please consider donating to help us fund the project's future development.

coolify.io/sponsorships

Thank you so much!

### Huge Sponsors

* Context.dev- Web scraping API for AI agents
* Ginernet- Hosting powerful servers in Spain
* SerpAPI- Google Search API — Scrape Google and other search engines from our fast, easy, and complete API.
* MVPS- Cheap VPS servers at the highest possible quality
* ScreenshotOne- Screenshot API for devs
* PrivateAlps- Cloud Services Provider, VPS, servers infrastructure for people who care about privacy and control
* Seibert Group- Boost productivity company-wide with AI agents like Claude Code
* Contabo- Cloud VPS & dedicated servers at unbeatable prices

### Big Sponsors

* Vanaways- New vans for sale and lease across the UK
* Cloudways- Managed cloud hosting platform by DigitalOcean
* ByteBase- Database CI/CD and Security at Scale
* Ramnode- High Performance Cloud VPS Hosting
* 23M- Your experts for high-availability hosting solutions!
* Macarne- Best IP Transit & Carrier Ethernet Solutions for Simplified Network Connectivity
* Hetzner- Server, cloud, hosting, and data center solutions
* Logto- The better identity infrastructure for developers
* Supadata- Scrape YouTube, web, and files. Get AI-ready, clean data for your next project.
* Tolgee- The open source localization platform
* Best Consultant- Your trusted technology consulting partner
* ArcJet- Advanced web security and performance solutions
* SupaGuide- Your comprehensive guide to Supabase
* CodeRabbit- Cut Code Review Time & Bugs in Half
* Convex- Convex is the open-source reactive database for web app developers.
* GoldenVM- Premium virtual machine hosting solutions
* Comit International- New York Times award–winning contractor!
* Compai- The open source compliance automation platform that does everything you need to get compliant, fast. Open source alternative to Drata & Vanta.
* Tigris- Modern S3 Alternative
* Blacksmith- Infrastructure automation platform
* JobsCollider- 30,000+ remote jobs for developers
* Darweb- Design. Develop. Deliver. Specialized in 3D CPQ Solutions for eCommerce.
* Hostinger- Web hosting and VPS solutions
* Mobb- Secure Your AI-Generated Code to Unlock Dev Productivity
* Ubicloud- Open source cloud infrastructure platform
* PFGLabs- Build Real Projects with Golang
* JuxtDigital- Digital PR & AI Authority Building Agency
* SaasyKit- Complete SaaS starter kit for developers
* American Cloud- US-based cloud infrastructure services
* Greptile- The AI Code Reviewer
* VPSDime- Cheap VPS Hosting - 4GB for $5/month
* dataforest Cloud- Deploy cloud servers as seeds independently in seconds. Enterprise hardware, premium network, 100% made in Germany.
* ISHosting- Hosting and VPS solutions
* NodePlus.ai- AI that reads every system your business runs on

### Small Sponsors

...and many more atGitHub Sponsors

## Star History