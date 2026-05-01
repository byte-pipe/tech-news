---
title: 'GitHub - simstudioai/sim: Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce. · GitHub'
url: https://github.com/simstudioai/sim
site_name: github
content_file: github-github-simstudioaisim-build-deploy-and-orchestrate
fetched_at: '2026-05-01T11:58:24.445623'
original_url: https://github.com/simstudioai/sim
author: simstudioai
description: Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce. - simstudioai/sim
---

simstudioai

 

/

sim

Public

* NotificationsYou must be signed in to change notification settings
* Fork3.5k
* Star28k

 
 
 
 
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

4,427 Commits
4,427 Commits
.agents/
skills
.agents/
skills
 
 
.claude
.claude
 
 
.cursor
.cursor
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.husky
.husky
 
 
apps
apps
 
 
docker
docker
 
 
helm/
sim
helm/
sim
 
 
packages
packages
 
 
scripts
scripts
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
biome.json
biome.json
 
 
bun.lock
bun.lock
 
 
bunfig.toml
bunfig.toml
 
 
docker-compose.local.yml
docker-compose.local.yml
 
 
docker-compose.ollama.yml
docker-compose.ollama.yml
 
 
docker-compose.prod.yml
docker-compose.prod.yml
 
 
package.json
package.json
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

The open-source platform to build AI agents and run your agentic workforce. Connect 1,000+ integrations and LLMs to orchestrate agentic workflows.

 

### Build Workflows with Ease

Design agent workflows visually on a canvas—connect agents, tools, and blocks, then run them instantly.

### Supercharge with Copilot

Leverage Copilot to generate nodes, fix errors, and iterate on flows directly from natural language.

### Integrate Vector Databases

Upload documents to a vector store and let agents answer questions grounded in your specific content.

## Quickstart

### Cloud-hosted:sim.ai

### Self-hosted: NPM Package

npx simstudio

→http://localhost:3000

#### Note

Docker must be installed and running on your machine.

#### Options

Flag

Description

-p, --port <port>

Port to run Sim on (default 
3000
)

--no-pull

Skip pulling latest Docker images

### Self-hosted: Docker Compose

git clone https://github.com/simstudioai/sim.git 
&&
 
cd
 sim
docker compose -f docker-compose.prod.yml up -d

Openhttp://localhost:3000

Sim also supports local models viaOllamaandvLLM— see theDocker self-hosting docsfor setup details.

### Self-hosted: Manual Setup

Requirements:Bun,Node.jsv20+, PostgreSQL 12+ withpgvector

1. Clone and install:

git clone https://github.com/simstudioai/sim.git

cd
 sim
bun install
bun run prepare 
#
 Set up pre-commit hooks

1. Set up PostgreSQL with pgvector:

docker run --name simstudio-db -e POSTGRES_PASSWORD=your_password -e POSTGRES_DB=simstudio -p 5432:5432 -d pgvector/pgvector:pg17

Or install manually via thepgvector guide.

1. Configure environment:

cp apps/sim/.env.example apps/sim/.env

#
 Create your secrets

perl -i -pe 
"
s/your_encryption_key/
$(
openssl rand -hex 32
)
/
"
 apps/sim/.env
perl -i -pe 
"
s/your_internal_api_secret/
$(
openssl rand -hex 32
)
/
"
 apps/sim/.env
perl -i -pe 
"
s/your_api_encryption_key/
$(
openssl rand -hex 32
)
/
"
 apps/sim/.env

#
 DB configs for migration

cp packages/db/.env.example packages/db/.env

#
 Edit both .env files to set DATABASE_URL="postgresql://postgres:your_password@localhost:5432/simstudio"

1. Run migrations:

cd
 packages/db 
&&
 bun run db:migrate

1. Start development servers:

bun run dev:full 
#
 Starts Next.js app and realtime socket server

Or run separately:bun run dev(Next.js) andcd apps/sim && bun run dev:sockets(realtime).

## Copilot API Keys

Copilot is a Sim-managed service. To use Copilot on a self-hosted instance:

* Go tohttps://sim.ai→ Settings → Copilot and generate a Copilot API key
* SetCOPILOT_API_KEYenvironment variable in your self-hosted apps/sim/.env file to that value

## Environment Variables

See theenvironment variables referencefor the full list, orapps/sim/.env.examplefor defaults.

## Tech Stack

* Framework:Next.js(App Router)
* Runtime:Bun
* Database: PostgreSQL withDrizzle ORM
* Authentication:Better Auth
* UI:Shadcn,Tailwind CSS
* Streaming Markdown:Streamdown
* State Management:Zustand,TanStack Query
* Flow Editor:ReactFlow
* Docs:Fumadocs
* Monorepo:Turborepo
* Realtime:Socket.io
* Background Jobs:Trigger.dev
* Remote Code Execution:E2B
* Isolated Code Execution:isolated-vm

## Contributing

We welcome contributions! Please see ourContributing Guidefor details.

## License

This project is licensed under the Apache License 2.0 - see theLICENSEfile for details.

Made with ❤️ by the Sim Team

## About

Build, deploy, and orchestrate AI agents. Sim is the central intelligence layer for your AI workforce.

www.sim.ai

### Topics

 react

 automation

 typescript

 ai

 nextjs

 chatbot

 artificial-intelligence

 gemini

 openai

 agents

 low-code

 no-code

 rag

 anthropic

 deepseek

 aiagents

 agentic-workflow

 agent-workflow

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

28k

 stars
 

### Watchers

132

 watching
 

### Forks

3.5k

 forks
 

 Report repository

 

## Releases261

v0.6.61

 Latest

 

Apr 29, 2026

 

+ 260 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript71.0%
* MDX25.9%
* JavaScript2.7%
* CSS0.2%
* Python0.1%
* HTML0.1%