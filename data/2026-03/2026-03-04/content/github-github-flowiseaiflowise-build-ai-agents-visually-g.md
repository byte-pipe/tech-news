---
title: 'GitHub - FlowiseAI/Flowise: Build AI Agents, Visually · GitHub'
url: https://github.com/FlowiseAI/Flowise
site_name: github
content_file: github-github-flowiseaiflowise-build-ai-agents-visually-g
fetched_at: '2026-03-04T11:13:05.663682'
original_url: https://github.com/FlowiseAI/Flowise
author: FlowiseAI
description: Build AI Agents, Visually. Contribute to FlowiseAI/Flowise development by creating an account on GitHub.
---

FlowiseAI



/

Flowise

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork23.8k
* Star49.8k




 
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

3,378 Commits
3,378 Commits
.github
.github
 
 
.husky
.husky
 
 
assets
assets
 
 
docker
docker
 
 
i18n
i18n
 
 
images
images
 
 
metrics
metrics
 
 
packages
packages
 
 
.dockerignore
.dockerignore
 
 
.eslintrc.js
.eslintrc.js
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
.nvmrc
.nvmrc
 
 
.prettierignore
.prettierignore
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE.md
LICENSE.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
artillery-load-test.yml
artillery-load-test.yml
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

English |繁體中文|简体中文|日本語|한국어

### Build AI Agents, Visually

## 📚 Table of Contents

* ⚡ Quick Start
* 🐳 Docker
* 👨‍💻 Developers
* 🌱 Env Variables
* 📖 Documentation
* 🌐 Self Host
* ☁️ Flowise Cloud
* 🙋 Support
* 🙌 Contributing
* 📄 License

## ⚡Quick Start

Download and InstallNodeJS>= 18.15.0

1. Install Flowisenpm install -g flowise
2. Start Flowisenpx flowise start
3. Openhttp://localhost:3000

## 🐳 Docker

### Docker Compose

1. Clone the Flowise project
2. Go todockerfolder at the root of the project
3. Copy.env.examplefile, paste it into the same location, and rename to.envfile
4. docker compose up -d
5. Openhttp://localhost:3000
6. You can bring the containers down bydocker compose stop

### Docker Image

1. Build the image locally:docker build --no-cache -t flowise.
2. Run image:docker run -d --name flowise -p 3000:3000 flowise
3. Stop image:docker stop flowise

## 👨‍💻 Developers

Flowise has 3 different modules in a single mono repository.

* server: Node backend to serve API logics
* ui: React frontend
* components: Third-party nodes integrations
* api-documentation: Auto-generated swagger-ui API docs from express

### Prerequisite

* InstallPNPMnpm i -g pnpm

### Setup

1. Clone the repository:git clone https://github.com/FlowiseAI/Flowise.git
2. Go into repository folder:cdFlowise
3. Install all dependencies of all modules:pnpm install
4. Build all the code:pnpm buildExit code 134 (JavaScript heap out of memory)If you get this error when running the above `build` script, try increasing the Node.js heap size and run the script again:#macOS / Linux / Git BashexportNODE_OPTIONS="--max-old-space-size=4096"#Windows PowerShell$env:NODE_OPTIONS="--max-old-space-size=4096"#Windows CMDsetNODE_OPTIONS=--max-old-space-size=4096Then run:pnpm build
5. Start the app:pnpm startYou can now access the app onhttp://localhost:3000
6. For development build:* Create.envfile and specify theVITE_PORT(refer to.env.example) inpackages/ui
* Create.envfile and specify thePORT(refer to.env.example) inpackages/server
* Run:pnpm devAny code changes will reload the app automatically onhttp://localhost:8080

## 🌱 Env Variables

Flowise supports different environment variables to configure your instance. You can specify the following variables in the.envfile insidepackages/serverfolder. Readmore

## 📖 Documentation

You can view the Flowise Docshere

## 🌐 Self Host

Deploy Flowise self-hosted in your existing infrastructure, we support variousdeployments

* AWS
* Azure
* Digital Ocean
* GCP
* Alibaba Cloud
* OthersRailwayNorthflankRenderHuggingFace SpacesElestioSealosRepoCloud
* Railway
* Northflank
* Render
* HuggingFace Spaces
* Elestio
* Sealos
* RepoCloud

## ☁️ Flowise Cloud

Get Started withFlowise Cloud.

## 🙋 Support

Feel free to ask any questions, raise problems, and request new features inDiscussion.

## 🙌 Contributing

Thanks go to these awesome contributors

SeeContributing Guide. Reach out to us atDiscordif you have any questions or issues.

## 📄 License

Source code in this repository is made available under theApache License Version 2.0.

## About

Build AI Agents, Visually

flowiseai.com

### Topics

 react

 javascript

 typescript

 chatbot

 artificial-intelligence

 openai

 multiagent-systems

 agents

 workflow-automation

 low-code

 no-code

 rag

 large-language-models

 chatgpt

 langchain

 agentic-workflow

 agentic-ai

### Resources

 Readme



### License

 View license


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

49.8k

 stars


### Watchers

342

 watching


### Forks

23.8k

 forks


 Report repository



## Releases80

flowise@3.0.13

 Latest



Feb 3, 2026



+ 79 releases

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





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* TypeScript56.7%
* JavaScript31.3%
* HTML6.1%
* Handlebars5.6%
* CSS0.2%
* SCSS0.1%
