---
title: 'GitHub - AstrBotDevs/AstrBot: Agentic IM Chatbot infrastructure that integrates lots of IM platforms, LLMs, plugins and AI feature, and can be your openclaw alternative. ✨ · GitHub'
url: https://github.com/AstrBotDevs/AstrBot
site_name: github
content_file: github-github-astrbotdevsastrbot-agentic-im-chatbot-infra
fetched_at: '2026-03-11T11:16:10.604816'
original_url: https://github.com/AstrBotDevs/AstrBot
author: AstrBotDevs
description: Agentic IM Chatbot infrastructure that integrates lots of IM platforms, LLMs, plugins and AI feature, and can be your openclaw alternative. ✨ - AstrBotDevs/AstrBot
---

AstrBotDevs



/

AstrBot

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.5k
* Star20.7k




 
master
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

4,191 Commits
4,191 Commits
.github
.github
 
 
astrbot
astrbot
 
 
changelogs
changelogs
 
 
dashboard
dashboard
 
 
docs
docs
 
 
k8s
k8s
 
 
openspec
openspec
 
 
samples
samples
 
 
scripts
scripts
 
 
tests
tests
 
 
typings/
faiss
typings/
faiss
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.python-version
.python-version
 
 
AGENTS.md
AGENTS.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
EULA.md
EULA.md
 
 
FIRST_NOTICE.en-US.md
FIRST_NOTICE.en-US.md
 
 
FIRST_NOTICE.md
FIRST_NOTICE.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
README_fr.md
README_fr.md
 
 
README_ja.md
README_ja.md
 
 
README_ru.md
README_ru.md
 
 
README_zh-TW.md
README_zh-TW.md
 
 
README_zh.md
README_zh.md
 
 
compose-with-shipyard.yml
compose-with-shipyard.yml
 
 
compose.yml
compose.yml
 
 
main.py
main.py
 
 
openapi.json
openapi.json
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
runtime_bootstrap.py
runtime_bootstrap.py
 
 
View all files

## Repository files navigation

简体中文｜繁體中文｜日本語｜Français｜Русский

Documentation｜Blog｜Roadmap｜Issue TrackerEmail Support

AstrBot is an open-source all-in-one Agent chatbot platform that integrates with mainstream instant messaging apps. It provides reliable and scalable conversational AI infrastructure for individuals, developers, and teams. Whether you're building a personal AI companion, intelligent customer service, automation assistant, or enterprise knowledge base, AstrBot enables you to quickly build production-ready AI applications within your IM platform workflows.

## Key Features

1. 💯 Free & Open Source.
2. ✨ AI LLM Conversations, Multimodal, Agent, MCP, Skills, Knowledge Base, Persona Settings, Auto Context Compression.
3. 🤖 Supports integration with Dify, Alibaba Cloud Bailian, Coze, and other agent platforms.
4. 🌐 Multi-Platform: QQ, WeChat Work, Feishu, DingTalk, WeChat Official Accounts, Telegram, Slack, andmore.
5. 📦 Plugin Extensions with 1000+ plugins available for one-click installation.
6. 🛡️Agent Sandboxfor isolated, safe execution of code, shell calls, and session-level resource reuse.
7. 💻 WebUI Support.
8. 🌈 Web ChatUI Support with built-in agent sandbox and web search.
9. 🌐 Internationalization (i18n) Support.

💙 Role-playing & Emotional Companionship

✨ Proactive Agent

🚀 General Agentic Capabilities

🧩 1000+ Community Plugins

## Quick Start

### One-Click Deployment

For users who want to quickly experience AstrBot, are familiar with command-line usage, and can install auvenvironment on their own, we recommend theuvone-click deployment method ⚡️:

uv tool install astrbot
astrbot init
#
 Only execute this command for the first time to initialize the environment

astrbot

Requiresuvto be installed.

Note

For macOS user: due to macOS security checks, the first run of theastrbotcommand may take longer (about 10-20s).

Updateastrbot:

uv tool upgrade astrbot

### Docker Deployment

For users familiar with containers and looking for a more stable, production-ready deployment method, we recommend deploying AstrBot with Docker / Docker Compose.

Please refer to the official documentation:Deploy AstrBot with Docker.

### Deploy on RainYun

For users who want one-click deployment and do not want to manage servers themselves, we recommend RainYun's one-click cloud deployment service ☁️:

### Desktop Application Deployment

For users who want to use AstrBot on desktop and mainly use ChatUI, we recommend AstrBot App.

VisitAstrBot-desktopto download and install; this method is designed for desktop usage and is not recommended for server scenarios.

### Launcher Deployment

For desktop users who also want fast deployment and isolated multi-instance usage, we recommend AstrBot Launcher.

VisitAstrBot Launcherto download and install.

### Deploy on Replit

Replit deployment is maintained by the community and is suitable for online demos and lightweight trials.

### AUR

AUR deployment targets Arch Linux users who prefer installing AstrBot through the system package workflow.

Run the command below to installastrbot-git, then start AstrBot in your local environment.

yay -S astrbot-git

More deployment methods

If you need panel-based management or deeper customization, seeBT-Panel Deploymentfor BT Panel app-store setup,1Panel Deploymentfor 1Panel app-market deployment,CasaOS Deploymentfor NAS/home-server visual deployment, andManual Deploymentfor fully custom source-based installation withuv.

## Supported Messaging Platforms

Connect AstrBot to your favorite chat platform.

Platform

Maintainer

QQ

Official

OneBot v11 protocol implementation

Official

Telegram

Official

Wecom & Wecom AI Bot

Official

WeChat Official Accounts

Official

Feishu (Lark)

Official

DingTalk

Official

Slack

Official

Discord

Official

LINE

Official

Satori

Official

Misskey

Official

WhatsApp (Coming Soon)

Official

Matrix

Community

KOOK

Community

VoceChat

Community

## Supported Model Services

Service

Type

OpenAI and Compatible Services

LLM Services

Anthropic

LLM Services

Google Gemini

LLM Services

Moonshot AI

LLM Services

Zhipu AI

LLM Services

DeepSeek

LLM Services

Ollama (Self-hosted)

LLM Services

LM Studio (Self-hosted)

LLM Services

AIHubMix

LLM Services (API Gateway, supports all models)

CompShare

LLM Services

302.AI

LLM Services

TokenPony

LLM Services

SiliconFlow

LLM Services

PPIO Cloud

LLM Services

ModelScope

LLM Services

OneAPI

LLM Services

Dify

LLMOps Platforms

Alibaba Cloud Bailian Applications

LLMOps Platforms

Coze

LLMOps Platforms

OpenAI Whisper

Speech-to-Text Services

SenseVoice

Speech-to-Text Services

OpenAI TTS

Text-to-Speech Services

Gemini TTS

Text-to-Speech Services

GPT-Sovits-Inference

Text-to-Speech Services

GPT-Sovits

Text-to-Speech Services

FishAudio

Text-to-Speech Services

Edge TTS

Text-to-Speech Services

Alibaba Cloud Bailian TTS

Text-to-Speech Services

Azure TTS

Text-to-Speech Services

Minimax TTS

Text-to-Speech Services

Volcano Engine TTS

Text-to-Speech Services

## ❤️ Sponsors

## ❤️ Contributing

Issues and Pull Requests are always welcome! Feel free to submit your changes to this project :)

### How to Contribute

You can contribute by reviewing issues or helping with pull request reviews. Any issues or PRs are welcome to encourage community participation. Of course, these are just suggestions—you can contribute in any way you like. For adding new features, please discuss through an Issue first.

### Development Environment

AstrBot usesrufffor code formatting and linting.

git clone https://github.com/AstrBotDevs/AstrBot
pip install pre-commit
pre-commit install

## 🌍 Community

### QQ Groups

* Group 9: 1076659624 (New)
* Group 10: 1078079676 (New)
* Group 1: 322154837
* Group 3: 630166526
* Group 5: 822130018
* Group 6: 753075035
* Group 7: 743746109
* Group 8: 1030353265
* Developer Group: 975206796

### Discord Server

## ❤️ Special Thanks

Special thanks to all Contributors and plugin developers for their contributions to AstrBot ❤️

Additionally, the birth of this project would not have been possible without the help of the following open-source projects:

* NapNeko/NapCatQQ- The amazing cat framework

## ⭐ Star History

Tip

If this project has helped you in your life or work, or if you're interested in its future development, please give the project a Star. It's the driving force behind maintaining this open-source project <3

Companionship and capability should never be at odds. What we aim to create is a robot that can understand emotions, provide genuine companionship, and reliably accomplish tasks.

私は、高性能ですから!

## About

Agentic IM Chatbot infrastructure that integrates lots of IM platforms, LLMs, plugins and AI feature, and can be your openclaw alternative. ✨

astrbot.app

### Topics

 python

 agent

 docker

 ai

 telegram

 discord

 mcp

 chatbot

 gemini

 openai

 llama

 qq

 gpt

 qqbot

 llm

 chatgpt

### Resources

 Readme



### License

 AGPL-3.0 license


### Code of conduct

 Code of conduct


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

20.7k

 stars


### Watchers

64

 watching


### Forks

1.5k

 forks


 Report repository



## Releases201

v4.19.5

 Latest



Mar 10, 2026



+ 200 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.






* opencollective.com/astrbot
* https://afdian.com/a/astrbot_team

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python69.0%
* Vue25.6%
* TypeScript3.4%
* JavaScript1.3%
* Shell0.3%
* SCSS0.2%
* Other0.2%
