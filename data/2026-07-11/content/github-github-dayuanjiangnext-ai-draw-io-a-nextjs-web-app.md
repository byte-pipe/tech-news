---
title: 'GitHub - DayuanJiang/next-ai-draw-io: A next.js web application that integrates AI capabilities with draw.io diagrams. This app allows you to create, modify, and enhance diagrams through natural language commands and AI-assisted visualization. · GitHub'
url: https://github.com/DayuanJiang/next-ai-draw-io
site_name: github
content_file: github-github-dayuanjiangnext-ai-draw-io-a-nextjs-web-app
fetched_at: '2026-07-11T11:24:38.366264'
original_url: https://github.com/DayuanJiang/next-ai-draw-io
author: DayuanJiang
description: A next.js web application that integrates AI capabilities with draw.io diagrams. This app allows you to create, modify, and enhance diagrams through natural language commands and AI-assisted visualization. - DayuanJiang/next-ai-draw-io
---

DayuanJiang

 

/

next-ai-draw-io

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork3.6k
* Star33.2k

 
 
 
 
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

686 Commits
686 Commits
.github
.github
 
 
.husky
.husky
 
 
.vscode
.vscode
 
 
app
app
 
 
components
components
 
 
contexts
contexts
 
 
docs
docs
 
 
edge-functions/
api/
edgeai/
chat
edge-functions/
api/
edgeai/
chat
 
 
electron
electron
 
 
hooks
hooks
 
 
lib
lib
 
 
packages
packages
 
 
public
public
 
 
resources
resources
 
 
scripts
scripts
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.eslintrc.json
.eslintrc.json
 
 
.gitignore
.gitignore
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
biome.json
biome.json
 
 
components.json
components.json
 
 
docker-compose.yml
docker-compose.yml
 
 
edgeone.json
edgeone.json
 
 
env.example
env.example
 
 
instrumentation.ts
instrumentation.ts
 
 
next.config.ts
next.config.ts
 
 
open-next.config.ts
open-next.config.ts
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
playwright.config.ts
playwright.config.ts
 
 
postcss.config.mjs
postcss.config.mjs
 
 
proxy.ts
proxy.ts
 
 
tsconfig.json
tsconfig.json
 
 
vercel.json
vercel.json
 
 
vitest.config.mts
vitest.config.mts
 
 
wrangler.jsonc
wrangler.jsonc
 
 
View all files

## Repository files navigation

# Next AI Draw.io

AI-Powered Diagram Creation Tool - Chat, Draw, Visualize

English |中文|日本語

A Next.js web application that integrates AI capabilities with draw.io diagrams. Create, modify, and enhance diagrams through natural language commands and AI-assisted visualization.

Note: Thanks toByteDance Doubaosponsorship, the demo site now uses the powerful glm-4.7 model!

20251211_drawio.mp4

## Table of Contents

* Next AI Draw.ioTable of ContentsExamplesFeaturesMCP ServerClaude Code CLIGetting StartedTry it OnlineDesktop ApplicationRun with DockerInstallationDeploymentDeploy to EdgeOne PagesDeploy on VercelDeploy on Cloudflare WorkersMulti-Provider SupportServer-Side Multi-Model ConfigurationAdmin PanelHow It WorksSupport & ContactFAQStar History
* Table of Contents
* Examples
* Features
* MCP ServerClaude Code CLI
* Claude Code CLI
* Getting StartedTry it OnlineDesktop ApplicationRun with DockerInstallation
* Try it Online
* Desktop Application
* Run with Docker
* Installation
* DeploymentDeploy to EdgeOne PagesDeploy on VercelDeploy on Cloudflare Workers
* Deploy to EdgeOne Pages
* Deploy on Vercel
* Deploy on Cloudflare Workers
* Multi-Provider SupportServer-Side Multi-Model ConfigurationAdmin Panel
* Server-Side Multi-Model Configuration
* Admin Panel
* How It Works
* Support & Contact
* FAQ
* Star History

## Examples

Here are some example prompts and their generated diagrams:

Animated transformer connectors

Prompt:Give me a **animated connector** diagram of transformer's architecture.

RAG Technique Diagram

Prompt:Generate a RAG architecture diagram for **chat application**. Use connected diagram for data ingestion

Authentication using React and AWS

Prompt:Generate authentication process using React with **AWS**. Use Serverless architecture.

Open Innovation

Prompt:Create visualization of Henry Chesbrough's Open Innovation model.

Cat sketch

Prompt:Draw a cute cat for me.

## Features

* LLM-Powered Diagram Creation: Leverage Large Language Models to create and manipulate draw.io diagrams directly through natural language commands
* Image-Based Diagram Replication: Upload existing diagrams or images and have the AI replicate and enhance them automatically
* PDF & Text File Upload: Upload PDF documents and text files to extract content and generate diagrams from existing documents
* AI Reasoning Display: View the AI's thinking process for supported models (OpenAI o1/o3, Gemini, Claude, etc.)
* Diagram History: Comprehensive version control that tracks all changes, allowing you to view and restore previous versions of your diagrams before the AI editing.
* Interactive Chat Interface: Communicate with AI to refine your diagrams in real-time
* Cloud Architecture Diagram Support: Specialized support for generating cloud architecture diagrams (AWS, GCP, Azure)
* Animated Connectors: Create dynamic and animated connectors between diagram elements for better visualization

## MCP Server

Use Next AI Draw.io with AI agents like Claude Desktop, Cursor, and VS Code via MCP (Model Context Protocol).

{
 
"mcpServers"
: {
 
"drawio"
: {
 
"command"
: 
"
npx
"
,
 
"args"
: [
"
@next-ai-drawio/mcp-server@latest
"
]
 }
 }
}

### Claude Code CLI

claude mcp add drawio -- npx @next-ai-drawio/mcp-server@latest

Then ask Claude to create diagrams:

"Create a flowchart showing user authentication with login, MFA, and session management"

The diagram appears in your browser in real-time!

See theMCP Server READMEfor VS Code, Cursor, and other client configurations.

## Getting Started

### Try it Online

No installation needed! Try the app directly on our demo site:

Bring Your Own API Key: You can use your own API key to bypass usage limits on the demo site. Click the Settings icon in the chat panel to configure your provider and API key. Your key is stored locally in your browser and is never stored on the server.

### Desktop Application

Download the native desktop app for your platform from theReleases page:

Supported platforms: Windows, macOS, Linux.

### Run with Docker

Go to Docker Guide

### Installation

1. Clone the repository:

git clone https://github.com/DayuanJiang/next-ai-draw-io

cd
 next-ai-draw-io
npm install
cp env.example .env.local

See theProvider Configuration Guidefor detailed setup instructions for each provider.

1. Run the development server:

npm run dev

1. Openhttp://localhost:6002in your browser to see the application.

## Deployment

### Deploy to EdgeOne Pages

You can deploy with one click usingTencent EdgeOne Pages.

Deploy by this button:

Check out theTencent EdgeOne Pages documentationfor more details.

Additionally, deploying through Tencent EdgeOne Pages will also grant you adaily free quota for DeepSeek models.

### Deploy on Vercel

The easiest way to deploy is usingVercel, the creators of Next.js. Be sure toset the environment variablesin the Vercel dashboard as you did in your local.env.localfile.

See theNext.js deployment documentationfor more details.

### Deploy on Cloudflare Workers

Go to Cloudflare Deploy Guide

## Multi-Provider Support

* ByteDance Doubao
* AWS Bedrock (default)
* OpenAI
* Anthropic
* Google AI
* Google Vertex AI
* Azure OpenAI
* Ollama
* OpenRouter
* AIHubMix
* DeepSeek
* SiliconFlow
* ModelScope
* SGLang
* Vercel AI Gateway

All providers except AWS Bedrock and OpenRouter support custom endpoints.

📖Detailed Provider Configuration Guide- See setup instructions for each provider.

### Server-Side Multi-Model Configuration

Administrators can configure multiple server-side models that are available to all users without requiring personal API keys. Configure viaAI_MODELS_CONFIGenvironment variable (JSON string) orai-models.jsonfile. For a single-provider quick setup, list comma-separated model IDs inAI_MODEL.

### Admin Panel

Set theADMIN_PASSWORDenvironment variable and visit/adminto manage server settings (models, access codes, features, observability, quota) from a web panel instead of hand-editing.env.

📖Admin Panel Guide— setup, precedence rules, and notes.

Model Requirements: This task requires strong model capabilities for generating long-form text with strict formatting constraints (draw.io XML). Recommended models include Claude Sonnet 4.5, GPT-5.1, Gemini 3 Pro, and DeepSeek V3.2/R1.

Note that theclaudeseries has been trained on draw.io diagrams with cloud architecture logos like AWS, Azure, GCP. So if you want to create cloud architecture diagrams, this is the best choice.

## How It Works

The application uses the following technologies:

* Next.js: For the frontend framework and routing
* Vercel AI SDK(ai+@ai-sdk/*): For streaming AI responses and multi-provider support
* react-drawio: For diagram representation and manipulation

Diagrams are represented as XML that can be rendered in draw.io. The AI processes your commands and generates or modifies this XML accordingly.

## Support & Contact

Special thanks toByteDance Doubaofor sponsoring the API token usage of the demo site!Register on the ARK platform to get 500K free tokens for all models!

If you find this project useful, please considersponsoringto help me host the live demo site!

For support or inquiries, please open an issue on the GitHub repository or contact the maintainer at:

* Email: me[at]jiang.jp

## FAQ

SeeFAQfor common issues and solutions.

## Star History

## About

A next.js web application that integrates AI capabilities with draw.io diagrams. This app allows you to create, modify, and enhance diagrams through natural language commands and AI-assisted visualization.

next-ai-drawio.jiang.jp/

### Topics

 productivity

 ai

 diagrams

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

33.2k

 stars
 

### Watchers

186

 watching
 

### Forks

3.6k

 forks
 

 Report repository

 

## Releases18

0.4.16

 Latest

 

May 21, 2026

 

+ 17 releases

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript92.6%
* JavaScript5.9%
* CSS1.1%
* Other0.4%