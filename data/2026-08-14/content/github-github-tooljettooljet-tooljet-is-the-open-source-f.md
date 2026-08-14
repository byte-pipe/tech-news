---
title: 'GitHub - ToolJet/ToolJet: ToolJet is the open-source foundation of ToolJet AI - the enterprise app generation platform for building internal tools, dashboard, business applications, workflows and AI agents 🚀 · GitHub'
url: https://github.com/ToolJet/ToolJet
site_name: github
content_file: github-github-tooljettooljet-tooljet-is-the-open-source-f
fetched_at: '2026-08-14T11:42:59.742031'
original_url: https://github.com/ToolJet/ToolJet
author: ToolJet
description: ToolJet is the open-source foundation of ToolJet AI - the enterprise app generation platform for building internal tools, dashboard, business applications, workflows and AI agents 🚀 - ToolJet/ToolJet
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 ToolJet

 

/

ToolJet

Public

* NotificationsYou must be signed in to change notification settings
* Fork5.2k
* Star38.7k

 
 
 
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

17,095 Commits
17,095 Commits
.do
.do
 
 
.github
.github
 
 
.husky
.husky
 
 
.vscode
.vscode
 
 
cli
cli
 
 
cypress-tests
cypress-tests
 
 
deploy
deploy
 
 
docker
docker
 
 
docs
docs
 
 
frontend
frontend
 
 
marketplace
marketplace
 
 
plans
plans
 
 
plugins
plugins
 
 
queryPanel
queryPanel
 
 
release-scripts
release-scripts
 
 
server
server
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitconfig
.gitconfig
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.node-version
.node-version
 
 
.nvmrc
.nvmrc
 
 
.slugignore
.slugignore
 
 
.version
.version
 
 
CODEOWNERS
CODEOWNERS
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY-INCIDENT-RESPONSE.md
SECURITY-INCIDENT-RESPONSE.md
 
 
SECURITY.md
SECURITY.md
 
 
THIRD-PARTY-NOTICES
THIRD-PARTY-NOTICES
 
 
db-git-sync.drawio.svg
db-git-sync.drawio.svg
 
 
dependabot.yml
dependabot.yml
 
 
docker-compose-debug.yaml
docker-compose-debug.yaml
 
 
docker-compose.yaml
docker-compose.yaml
 
 
eslint.config.mjs
eslint.config.mjs
 
 
netlify.toml
netlify.toml
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
render.yaml
render.yaml
 
 
update-version.js
update-version.js
 
 
View all files

## Repository files navigation

ToolJet is the open-source foundation of ToolJet AI - the AI-native platform for building and deploying internal tools, workflows and AI agents. The community edition provides a powerful visual builder, drag-and-drop UI, and integrations with databases, APIs, SaaS apps, and object storage. For AI-powered UI generation, query building, debugging, and enterprise features, see ToolJet AI.

⭐ If you find ToolJet useful, please consider giving us a star on GitHub! Your support helps us continue to innovate and deliver exciting features.

## Features

### Community Edition (CE)

* Visual App Builder:60+ responsive components (Tables, Charts, Forms, Lists, Progress Bars, and more).
* ToolJet Database:Built-in no-code database.
* Multi-page Apps & Multiplayer Editing:Build complex apps collaboratively.
* 80+ Data Sources:Connect to databases, APIs, cloud storage, and SaaS tools.
* Flexible Deployment:Self-host with Docker, Kubernetes, AWS, GCP, Azure, and more.
* Collaboration Tools:Inline comments, mentions, and granular access control.
* Extensibility:Create plugins and connectors with theToolJet CLI.
* Code Anywhere:Run JavaScript and Python inside your apps.
* Secure by Design:AES-256-GCM encryption, proxy-only data flow, SSO support.

### ToolJet AI (Enterprise)

Everything in CE, plus:

* AI App Generation:Create apps instantly from natural language prompts.
* AI Query Builder:Generate and transform queries with AI assistance.
* AI Debugging:Identify and fix issues with one click.
* Agent Builder:Create intelligent agents to automate workflows and orchestrate processes.
* Enterprise-grade Security & Compliance:SOC 2 and GDPR readiness, audit logs, and advanced access control.
* User Management:Role-based access (RBAC), custom groups, and granular app/data permissions.
* Multi-environment Management:Seamless dev/stage/prod environments.
* GitSync & CI/CD:Integrate with GitHub/GitLab for version control and streamlined deployments.
* Branding & Customization:White-labeling, and custom theming for organizational branding.
* Fine-Grained Access Control:Secure data and actions at the row, component, page, and query levels.
* Embedded Apps:Embed ToolJet apps securely within other applications or portals.
* Enterprise Support:SLAs, priority bug fixes, and onboarding assistance.

## Quickstart

The easiest way to get started with ToolJet is by creating aToolJet Cloudaccount. ToolJet Cloud offers a hosted solution of ToolJet. If you want to self-host ToolJet, kindly proceed todeployment documentation.

### Try using Docker

Want to give ToolJet a quick spin on your local machine? You can run the following command from your terminal to have ToolJet up and running right away.

docker run \
 --name tooljet \
 --restart unless-stopped \
 -p 80:80 \
 --platform linux/amd64 \
 -v tooljet_data:/var/lib/postgresql/13/main \
 tooljet/try:ee-lts-latest

For users upgrading their ToolJet version, we recommend choosing the LTS version over the latest version. The LTS version ensures stability with production bug fixes, security patches, and performance enhancements.

## Tutorials and examples

Time Tracker ApplicationBuild your own CMS using low-codeAWS S3 Browser

## Documentation

Documentation is available athttps://docs.tooljet.com.

* Getting Started
* Data source Reference
* Component Reference

## Self-hosted

You can use ToolJet Cloud for a fully managed solution. If you want to self-host ToolJet, we have guides on deploying ToolJet on Kubernetes, AWS EC2, Docker, and more.

Provider

Documentation

Digital Ocean

Link

Docker

Link

AWS EC2

Link

AWS ECS

Link

OpenShift

Link

Helm

Link

AWS EKS (Kubernetes)

Link

GCP GKE (Kubernetes)

Link

Azure AKS (Kubernetes)

Link

Azure Container

Link

Google Cloud Run

Link

Deploying ToolJet client

Link

Deploying ToolJet on a Subpath

Link

## Marketplace

ToolJet can now be found on both AWS and Azure Marketplaces, making it simpler than ever to access and deploy our app-building platform.

Find ToolJet on AWS Marketplacehereand explore seamless integration on Azure Marketplacehere.

## Community support

For general help using ToolJet, please refer to the officialdocumentation. For additional help, you can use one of these channels to ask a question:

* Slack- Discussions with the community and the team.
* GitHub- For bug reports and feature requests.
* 𝕏 (Twitter)- Get the product updates quickly.

## Roadmap

Check out ourroadmapto stay updated on recently released features and learn about what's coming next.

## Branching model

We use the git-flow branching model. The base branch isdevelop. If you are looking for a stable version, please use the main branch or tags labeled as v1.x.x.

## Contributing

Kindly read ourContributing Guideto familiarize yourself with ToolJet's development process, how to suggest bug fixes and improvements, and the steps for building and testing your changes.

## Contributors

## License

ToolJet © 2023, ToolJet Solutions Inc - Released under the GNU Affero General Public License v3.0.