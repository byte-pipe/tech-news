---
title: 'GitHub - HKUDS/nanobot: Lightweight, open-source AI agent for your tools, chats, and workflows. · GitHub'
url: https://github.com/HKUDS/nanobot
site_name: github
content_file: github-github-hkudsnanobot-lightweight-open-source-ai-age
fetched_at: '2026-07-21T11:37:17.908614'
original_url: https://github.com/HKUDS/nanobot
author: HKUDS
description: Lightweight, open-source AI agent for your tools, chats, and workflows. - HKUDS/nanobot
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 HKUDS

 

/

nanobot

Public

* NotificationsYou must be signed in to change notification settings
* Fork8.1k
* Star46k

 
 
 
 
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

3,553 Commits
3,553 Commits
.agent
.agent
 
 
.github
.github
 
 
case
case
 
 
docs
docs
 
 
images
images
 
 
nanobot
nanobot
 
 
scripts
scripts
 
 
tests
tests
 
 
webui
webui
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
COMMUNICATION.md
COMMUNICATION.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
THIRD_PARTY_NOTICES.md
THIRD_PARTY_NOTICES.md
 
 
conftest.py
conftest.py
 
 
core_agent_lines.sh
core_agent_lines.sh
 
 
docker-compose.bwrap.yml
docker-compose.bwrap.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
entrypoint.sh
entrypoint.sh
 
 
hatch_build.py
hatch_build.py
 
 
pyproject.toml
pyproject.toml
 
 
render-config.json
render-config.json
 
 
render.yaml
render.yaml
 
 
View all files

## Repository files navigation

English|简体中文|繁體中文|Español|Français|Bahasa Indonesia|日本語|한국어|Русский|Tiếng Việt

🐈nanobotis an open-source, ultra-lightweight personal AI agent you can truly own. It keeps the agent core small and readable while giving you the practical pieces for real long-running work: WebUI, chat channels, tools, memory, MCP, model routing, automation, and deployment.

## Start Here

You want to...

Go to

Install nanobot with no terminal/config background

Start Without Technical Background

Install quickly and get one CLI reply

Install
 and 
Quick Start

Open the bundled browser UI

WebUI

Connect Telegram, Discord, WeChat, Slack, Email, Mattermost, or another chat app

Chat Apps

Configure providers, fallback models, Langfuse, MCP, web tools, or security

Docs
 and 
Configuration

Understand or extend the internals

Architecture
 and 
Development

Deploy to the cloud in one click

Deploy to Render

## Deploy to Render

Deploy nanobot's gateway and bundled WebUI as a single web service with persistent memory. Render readsrender.yamland prompts for two secrets on deploy:ANTHROPIC_API_KEYandNANOBOT_WEB_TOKEN(the password that gates the public WebUI — generate a strong random value, e.g.openssl rand -hex 32).

Note:The blueprint attaches a persistent disk so sessions, memory, and WebUI history survive restarts. Persistent disks require a paid service (they are not available on Render's free tier).

## What can nanobot do?

nanobot is a self-hosted personal AI agent runtime. It can:

* run in a browser WebUI or terminal
* connect to Telegram, Discord, Slack, WeChat, Email, Mattermost, and other chat apps
* use tools such as files, shell, web search, web fetch, MCP, cron, image generation, and subagents
* keep session history and long-term memory through Dream
* run long-horizon goals and scheduled automations
* expose a Python SDK and OpenAI-compatible API for integrations
* deploy as a long-running local or server-side agent gateway

## Latest Release

v0.2.2 - Durability Release

Highlights:

* Segmented WebUI transcripts
* Python SDK runtime controls
* Automation management
* Search/STT provider improvements
* Gateway/session/provider reliability

See full changelog

## Open Source Partners

## Recent Updates

* 2026-07-12Explicit/goalactivation, safer runtime and workspace access.
* 2026-07-11Syntax-highlighted previews and diffs, queued prompts, safer edits.
* 2026-07-10Stable model routing, multiline CLI input, new automation guide.
* 2026-07-09Live file-edit diffs, safer localhost setup, Matrix image fixes.
* 2026-07-08Safer WebUI/API setup, onboard refresh, responsive prompt rail.

For older updates, see therelease archiveorGitHub releases.

## 💡 Why nanobot

* Persistent workflows: goals, memory, tools, and chat context survive long-running work.
* Chat-native reach: WebUI, API, Telegram, Feishu, Slack, Discord, Teams, email, and Mattermost.
* Model freedom: OpenAI-compatible APIs, local LLMs, image generation, search, and fallbacks.
* Small core: readable internals with MCP, memory, deployment, and automation built in.
* Own your stack: inspect, customize, self-host, and extend without a giant platform.

## 📦 Install

Important

If you want the newest features and experiments, install from source.

If you want the most stable day-to-day experience, install from PyPI or withuv.

Pickoneinstall method:

Prerequisites: Python 3.11 or newer. Git is only needed for a source install. Published packages already include the WebUI; a current-source install needsbunornpmto build it.

If terminals, API keys, or config files are new to you, use the guided zero-background walkthrough inStart Without Technical Backgroundinstead of this compact README path.

One-command setup

macOS / Linux:

curl -fsSL https://raw.githubusercontent.com/HKUDS/nanobot/main/scripts/install.sh 
|
 sh

Windows PowerShell:

irm https:
//
raw.githubusercontent.com
/
HKUDS
/
nanobot
/
main
/
scripts
/
install.ps1 
|
 iex

The default command installs or upgradesnanobot-aifrom PyPI, then startsnanobot onboard --wizard. It avoids system-wide pip installs by using an active virtual environment,uv,pipx, or a managed venv under~/.nanobot/venv. If Quick Start finishes, skip the manual initialize/configure steps below and go straight toOpen the WebUI. The installer also prints the exact command it used to run nanobot; reuse that full command below ifnanobotis not onPATH.

To preview the plan without changing your environment, pass--dry-run; combine it with--devwhen you want to preview the main-branch install.

curl -fsSL https://raw.githubusercontent.com/HKUDS/nanobot/main/scripts/install.sh 
|
 sh -s -- --dry-run

&
 ([
scriptblock
]::Create((irm https:
//
raw.githubusercontent.com
/
HKUDS
/
nanobot
/
main
/
scripts
/
install.ps1))) 
--
dry
-
run

To install the currentmainbranch instead, pass--dev:

curl -fsSL https://raw.githubusercontent.com/HKUDS/nanobot/main/scripts/install.sh 
|
 sh -s -- --dev

&
 ([
scriptblock
]::Create((irm https:
//
raw.githubusercontent.com
/
HKUDS
/
nanobot
/
main
/
scripts
/
install.ps1))) 
--
dev

If you prefer to inspect the script first, openscripts/install.shorscripts/install.ps1.

Install withuv

uv tool install nanobot-ai

Install from PyPI with pip

python -m pip install nanobot-ai

If pip reportsexternally-managed-environmenton macOS or Linux, use the one-command installer,uv tool install nanobot-ai,pipx install nanobot-ai, or install inside a virtual environment.

Install from source

bunornpmmust be available. From an activated virtual environment:

git clone https://github.com/HKUDS/nanobot.git

cd
 nanobot
python -m pip install 
.

On Windows, if pip reports that it cannot launchnpm, runcd webui,npm.cmd install --package-lock=false,npm.cmd run build, andcd ..in order, then retry the install. Contributors who need an editable checkout should followCONTRIBUTING.mdandwebui/README.md.

Verify the install:

nanobot --version

Ifnanobotis not onPATH, invoke it through the method that installed it: reuse the recommended installer's command, useuv tool run --from nanobot-ai nanobot ...orpipx run --spec nanobot-ai nanobot ..., or use the Python executable from the environment where pip installed the package.

## 🚀 Quick Start

1. Initialize

Skip this step if the one-command setup already started the wizard and Quick Start finished there.

nanobot onboard

Usenanobot onboard --wizardif you prefer an interactive setup.

2. Configure(~/.nanobot/config.json)

Skip this step if you already configured provider and model settings in the wizard.

nanobot onboardcreates~/.nanobot/config.jsonand~/.nanobot/workspace/. Configure thesetwo partsin the config file. Add or merge the following blocks into the existing file instead of replacing the whole file.

The example below uses a generic OpenAI-compatiblecustomprovider so the compact path does not recommend one hosted service. Provider examples are recipes, not rankings or endorsements. For copyable provider-specific setup, seeProvider Cookbook.

Set your API key:

{
 
"providers"
: {
 
"custom"
: {
 
"apiKey"
: 
"
your-api-key
"
,
 
"apiBase"
: 
"
https://api.example.com/v1
"

 }
 }
}

Set a model preset and make it active:

{
 
"modelPresets"
: {
 
"primary"
: {
 
"label"
: 
"
Primary
"
,
 
"provider"
: 
"
custom
"
,
 
"model"
: 
"
model-id-from-your-provider
"
,
 
"maxTokens"
: 
8192
,
 
"contextWindowTokens"
: 
200000
,
 
"temperature"
: 
0.1

 }
 },
 
"agents"
: {
 
"defaults"
: {
 
"modelPreset"
: 
"
primary
"

 }
 }
}

Directagents.defaults.providerandagents.defaults.modelstill work for existing configs, but named presets are the recommended path because they also power/modelswitching andfallbackModels.

For another provider, the same config shape still applies:

Replace

Where

Provider config key

providers.<provider>

API key

providers.<provider>.apiKey

Preset provider name

modelPresets.primary.provider

Model ID

modelPresets.primary.model

Endpoint URL, only when needed

providers.<provider>.apiBase

3. Open the WebUI

The stable-compatible path is:

nanobot gateway

Leave the terminal open and visithttp://127.0.0.1:8765. Current source versions also providenanobot webui, which prepares the local WebSocket channel if needed, starts the gateway, and opens the browser automatically. The first-run WebUI binds to127.0.0.1by default, so it is not exposed to your LAN. Prefer not to keep a terminal open? Usenanobot gateway --background, then manage it withnanobot gateway status,logs,restart, andstop.

For manual or terminal-only setup, test one CLI message:

nanobot status
nanobot agent -m 
"
Hello!
"

Innanobot status, it is normal for most providers to saynot set. The active preset's provider should be configured, andConfigplusWorkspaceshould show check marks.

If that works, start an interactive chat:

nanobot agent

Need help withPATH, API keys, provider/model matching, or JSON errors? See the fullerInstall and Quick StartandTroubleshooting.

* Want a pasteable provider setup? SeeProvider Cookbook
* Want to understand provider/model matching? SeeProviders and Models
* Want web search, MCP, security settings, or more config options? SeeConfiguration
* Want to run locally? SeeOllama,vLLM or another local OpenAI-compatible server, and the fullprovider reference.
* Want to run nanobot in chat apps like Telegram, Discord, WeChat or Feishu? SeeChat Apps
* Want Docker or Linux service deployment? SeeDeployment

## 🌐 WebUI

The WebUI shipsinside the published wheel— no extra build step. It is the browser workbench for chat sessions, workspace controls, Apps, Skills, Automations, and settings. For the full user guide, seedocs/webui.md.

Open it

nanobot webui

On current source versions, the command enables the local WebSocket channel after confirmation, starts the gateway, and openshttp://127.0.0.1:8765. If your installed stable release does not includenanobot webui, runnanobot gatewayand open that address manually. To open it from another device on your LAN, seeWebUI docs -> LAN access.

The WebUI is served by the WebSocket channel on port8765by default. The gateway's18790port is for the health endpoint, not the browser UI.

Tip

Working on the WebUI itself? Check outwebui/README.mdfor the source-tree, Vite dev server, build, and test workflow.

## 🏗️ Architecture

🐈 nanobot stays lightweight by centering everything around a small agent loop: messages come in from chat apps, the LLM decides when tools are needed, and memory or skills are pulled in only as context instead of becoming a heavy orchestration layer. That keeps the core path readable and easy to extend, while still letting you add channels, tools, memory, and deployment options without turning the system into a monolith.

## ✨ Features

📈 24/7 Real-Time Market Analysis

🚀 Full-Stack Software Engineer

📅 Smart Daily Routine Manager

📚 Personal Knowledge Assistant

Discovery • Insights • Trends

Develop • Deploy • Scale

Schedule • Automate • Organize

Learn • Memory • Reasoning

## 📚 Docs

Browse therepo docsfor the latest features and GitHub development version, or visitnanobot.wikifor the stable release documentation.

* Use task-oriented guides:Guides
* Start with no technical background:Start Without Technical Background
* Start from zero with developer basics:Install and Quick Start
* Understand the runtime model:Concepts
* Read the source-level map:Architecture
* Choose a provider/model:Providers and Models
* Copy provider setup recipes:Provider Cookbook
* Debug setup and runtime failures:Troubleshooting
* Talk to your nanobot with familiar chat apps:Chat App AI Agent·Chat Apps
* Schedule or trigger agent work:Automations
* Configure providers, web search, MCP, and runtime behavior:Configuration
* Integrate nanobot with local tools and automations:OpenAI-Compatible API·Python SDK
* Run nanobot with Docker or as a Linux service:Deployment

## 🤝 Contribute & Roadmap

PRs welcome! The codebase is intentionally small and readable. 🤗

### Contribution Flow

SeeCONTRIBUTING.mdfor setup, review, and contribution guidelines.

Roadmap— Pick an item andopen a PR!

* Multi-modal— See and hear (images, voice, video)
* Long-term memory— Never forget important context
* Better reasoning— Multi-step planning and reflection
* More integrations— Calendar and more
* Self-improvement— Learn from feedback and mistakes

## Contact

Nanobot was started byXubin Renas a personal open-source project and is now maintained collaboratively with contributors from the open-source community. Feel free to contactxubinrencs@gmail.comfor questions, ideas, or collaboration.

### Contributors

Thanks for visiting ✨ nanobot!

## About

Lightweight, open-source AI agent for your tools, chats, and workflows.

nanobot.wiki

### Topics

 ai

 openai

 codex

 ai-agents

 claude

 nanobot

 ai-agent

 llm

 chatgpt

 anthropic

 claude-code

 codex-cli

 openclaw

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

46k

 stars
 

### Watchers

205

 watching
 

### Forks

8.1k

 forks
 

 Report repository

 

## Releases18

v0.2.2

 Latest

 

Jun 23, 2026

 

+ 17 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python77.9%
* TypeScript21.5%
* Shell0.2%
* CSS0.2%
* PowerShell0.1%
* HTML0.1%