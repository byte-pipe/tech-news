---
title: 'GitHub - InsForge/InsForge: Give agents everything they need to ship fullstack apps. The backend built for agentic development. · GitHub'
url: https://github.com/InsForge/InsForge
site_name: github
content_file: github-github-insforgeinsforge-give-agents-everything-the
fetched_at: '2026-03-12T11:15:50.433032'
original_url: https://github.com/InsForge/InsForge
author: InsForge
description: 'Give agents everything they need to ship fullstack apps. The backend built for agentic development. - GitHub - InsForge/InsForge: Give agents everything they need to ship fullstack apps. The backend built for agentic development.'
---

InsForge

 

/

InsForge

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork299
* Star2.6k

 
 
 
 
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

2,953 Commits
2,953 Commits
.claude-plugin
.claude-plugin
 
 
.github
.github
 
 
assets
assets
 
 
auth
auth
 
 
backend
backend
 
 
deploy
deploy
 
 
docs
docs
 
 
examples
examples
 
 
frontend
frontend
 
 
functions
functions
 
 
i18n
i18n
 
 
openapi
openapi
 
 
shared-schemas
shared-schemas
 
 
ui
ui
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.prettierignore
.prettierignore
 
 
.prettierrc
.prettierrc
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE_PLUGIN.md
CLAUDE_PLUGIN.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
GITHUB_OAUTH_SETUP.md
GITHUB_OAUTH_SETUP.md
 
 
GOOGLE_OAUTH_SETUP.md
GOOGLE_OAUTH_SETUP.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
docker-compose.prod.yml
docker-compose.prod.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
eslint.config.js
eslint.config.js
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
test-google-id-token.html
test-google-id-token.html
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

The backend built for agentic development.

## InsForge

InsForge is a backend development platform built for AI coding agents and AI code editors. It exposes backend primitives like databases, auth, storage, and functions through a semantic layer that agents can understand, reason about, and operate end to end.

InsForge-readme.mp4

### How it works

InsForge acts as a semantic layer between AI coding agents and backend primitives. It performs backend context engineering so agents can understand, operate, and inspect backend systems.

* Fetch backend context: Agents can fetch documentation and available operations for the backend primitives they use.
* Configure primitives: Agents can configure backend primitives directly.
* Inspect backend state: Backend state and logs are exposed through structured schemas.

graph TB

 subgraph TOP[" "]
 AG[AI Coding Agents]
 end

 subgraph MID[" "]
 SL[InsForge Semantic Layer]
 end

 AG --> SL

 SL --> AUTH[Authentication]
 SL --> DB[Database]
 SL --> ST[Storage]
 SL --> EF[Edge Functions]
 SL --> MG[Model Gateway]
 SL --> DEP[Deployment]

 classDef bar fill:#0b0f14,stroke:#30363d,stroke-width:1px,color:#ffffff
 classDef card fill:#161b22,stroke:#30363d,stroke-width:1px,color:#ffffff

 class AG,SL bar
 class AUTH,DB,ST,EF,MG,DEP card

 style TOP fill:transparent,stroke:transparent
 style MID fill:transparent,stroke:transparent

 linkStyle default stroke:#30363d,stroke-width:1px

 
Loading

### Core Products:

* Authentication: User management, authentication, and sessions
* Database: Postgres relational database
* Storage: S3 compatible file storage
* Model Gateway: OpenAI compatible API across multiple LLM providers
* Edge Functions: Serverless code running on the edge
* Site Deployment: Site build and deployment

## ⭐️ Star the Repository

If you find InsForge useful or interesting, a GitHub Star ⭐️ would be greatly appreciated.

## Quickstart

### Cloud-hosted:insforge.dev

### Self-hosted: Docker Compose

Prerequisites:Docker+Node.js

#### 1. Setup

You can run InsForge locally using Docker Compose. This will start a local InsForge instance on your machine.

Or run from source:

#
 Run with Docker

git clone https://github.com/insforge/insforge.git

cd
 insforge
cp .env.example .env
docker compose -f docker-compose.prod.yml up

#### 2. Connect InsForge MCP

Openhttp://localhost:7130

Follow the steps to connect InsForge MCP Server

#### 3. Verify installation

To verify the connection, send the following prompt to your agent:

I'm using InsForge as my backend platform, call InsForge MCP's fetch-docs tool to learn about InsForge instructions.

### One-click Deployment

In addition to running InsForge locally, you can also launch InsForge using a pre-configured setup. This allows you to get up and running quickly with InsForge without installing Docker on your local machine.

Railway

Zeabur

Sealos

## Contributing

Contributing: If you're interested in contributing, you can check our guide hereCONTRIBUTING.md. We truly appreciate pull requests, all types of help are appreciated!

Support: If you need any help or support, we're responsive on ourDiscord channel, and also feel free to email usinfo@insforge.devtoo!

## Documentation & Support

### Documentation

* Official Docs- Comprehensive guides and API references

### Community

* Discord- Join our vibrant community
* Twitter- Follow for updates and tips

### Contact

* Email:info@insforge.dev

## License

This project is licensed under the Apache License 2.0 - see theLICENSEfile for details.

## Badges

Show your project is built with InsForge.

### Made with InsForge

Markdown:

[
![
Made with InsForge
]
(
https://insforge.dev/badge-made-with-insforge.svg
)]
(
https://insforge.dev
)

HTML:

<
a
 
href
="
https://insforge.dev
"
>

 
<
img

 
width
="
168
"
 
height
="
30
"
 
src
="
https://insforge.dev/badge-made-with-insforge.svg
"
 
alt
="
Made with InsForge
"
 
/>

</
a
>

### Made with InsForge (dark)

Markdown:

[
![
Made with InsForge
]
(
https://insforge.dev/badge-made-with-insforge-dark.svg
)]
(
https://insforge.dev
)

HTML:

<
a
 
href
="
https://insforge.dev
"
>

 
<
img

 
width
="
168
"
 
height
="
30
"
 
src
="
https://insforge.dev/badge-made-with-insforge-dark.svg
"
 
alt
="
Made with InsForge
"
 
/>

</
a
>

⭐Star us on GitHubto get notified about new releases!

## About

Give agents everything they need to ship fullstack apps. The backend built for agentic development.

insforge.dev

### Topics

 oauth2

 ai

 nextjs

 websockets

 realtime

 postgresql

 embeddings

 coding

 vectors

 ai-agents

 deno

 pgvector

 insforge

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

2.6k

 stars
 

### Watchers

30

 watching
 

### Forks

299

 forks
 

 Report repository

 

## Releases25

Release v2.0.1

 Latest

 

Mar 9, 2026

 

+ 24 releases

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors45

+ 31 contributors

## Languages

* TypeScript87.9%
* Shell8.3%
* PLpgSQL2.2%
* JavaScript0.8%
* CSS0.5%
* Dockerfile0.2%
* HTML0.1%