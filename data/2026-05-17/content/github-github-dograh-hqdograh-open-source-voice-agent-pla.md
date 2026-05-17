---
title: 'GitHub - dograh-hq/dograh: Open Source Voice Agent Platform · GitHub'
url: https://github.com/dograh-hq/dograh
site_name: github
content_file: github-github-dograh-hqdograh-open-source-voice-agent-pla
fetched_at: '2026-05-17T19:29:29.930041'
original_url: https://github.com/dograh-hq/dograh
author: dograh-hq
description: Open Source Voice Agent Platform. Contribute to dograh-hq/dograh development by creating an account on GitHub.
---

dograh-hq

 

/

dograh

Public

* NotificationsYou must be signed in to change notification settings
* Fork348
* Star1.5k

 
 
 
 
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

468 Commits
468 Commits
.github
.github
 
 
api
api
 
 
config/
coturn
config/
coturn
 
 
deploy/
templates
deploy/
templates
 
 
docs
docs
 
 
evals
evals
 
 
examples
examples
 
 
nginx
nginx
 
 
pipecat @ 13e98d0
pipecat @ 13e98d0
 
 
scripts
scripts
 
 
sdk
sdk
 
 
ui
ui
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.nvmrc
.nvmrc
 
 
.python-version
.python-version
 
 
.release-please-manifest.json
.release-please-manifest.json
 
 
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
 
 
SECURITY.md
SECURITY.md
 
 
docker-compose-local.yaml
docker-compose-local.yaml
 
 
docker-compose.yaml
docker-compose.yaml
 
 
release-please-config.json
release-please-config.json
 
 
remote_up.sh
remote_up.sh
 
 
View all files

## Repository files navigation

# Dograh AI

The open-source, self-hostable alternative to Vapi & Retell— build production voice agents with a drag-and-drop workflow builder. From zero to a working bot in under 2 minutes.

  
 

  
 

📖 Docs·📜 BSD 2-Clause

* 100% open source, self-hostable — no vendor lock-in, unlike Vapi or Retell
* Full control & transparency— every line of code is open, with flexible LLM / TTS / STT integration
* Maintained by YC alumni and exit founders, committed to keeping voice AI open

## 🎥 Featured

Featured by 
Better Stack
 — a hands-on look at Dograh

📺 Prefer a 2-minute product walkthrough? Click here.

## ⚖️ Dograh vs Vapi vs Retell

An honest comparison on the axes that matter most to teams evaluating voice AI platforms.

Dograh

Vapi

Retell

License

BSD 2-Clause (open source)

Proprietary

Proprietary

Self-hostable

✅ Yes — one Docker command

❌ SaaS only

❌ SaaS only

Pricing

Free (self-host) · usage-based (cloud)

Per-minute SaaS

Per-minute SaaS

Bring your own LLM / STT / TTS

✅ Any provider, or use Dograh's stack

Configurable within their integrations

Configurable within their integrations

Source-level customization

✅ Every line is yours to modify

❌ Closed source

❌ Closed source

Data residency

Your infra, your rules

Their cloud

Their cloud

Vendor lock-in

None

Full

Full

## 🚀 Get Started

##### Download and setup Dograh on your Local Machine

NoteWe collect anonymous usage data to improve the product. You can opt out by setting theENABLE_TELEMETRYtofalsein the below command.

NoteIf you wish to run the platform on a remote server instead, checkout ourDocumentation

curl -o docker-compose.yaml https://raw.githubusercontent.com/dograh-hq/dograh/main/docker-compose.yaml 
&&
 REGISTRY=ghcr.io/dograh-hq ENABLE_TELEMETRY=true docker compose up --pull always

NoteFirst startup may take 2-3 minutes to download all images. Once running, openhttp://localhost:3010to create your first AI voice assistant!
For common issues and solutions, see 🔧Troubleshooting.

### 🎙️ Your First Voice Bot

1. Openhttp://localhost:3010in your browser.
2. PickInboundorOutbound, name your bot (e.g.Lead Qualification), and describe the use case in 5–10 words (e.g.Screen insurance form submissions for purchase intent).
3. ClickWeb Call— you're talking to your bot.

🔑No API keys needed.Dograh ships with auto-generated keys and its own LLM / TTS / STT stack. Connect your own keys for LLM, TTS, STT, or Telephony (e.g. Twilio, Vonage, Telnyx) anytime.

## Features

### Voice Capabilities

* Telephony: Built-in telephony integration like Twilio, Vonage, Vobiz, Cloudonix (easily add others), with support for transferring calls to human agents
* Languages: English support (expandable to other languages)
* Custom Models: Bring your own TTS/STT models
* Real-time Processing: Low-latency voice interactions

### Developer Experience

* Zero Config Start: Auto-generated API keys for instant testing
* Python-Based: Built on Python for easy customization
* Docker-First: Containerized for consistent deployments
* Modular Architecture: Swap components as needed

### Testing & Quality

* Test Mode: Try your agent end-to-end before publishing, with no production calls or data affected
* In-Dashboard Web Calls: Talk to your bot directly while building — no telephony setup required
* QA Node: A built-in workflow node that analyzes prompt quality across your other nodes

## Deployment Options

### Local Development

ReferLocal Setup

### Self-Hosted Deployment

For detailed deployment instructions including remote server setup with HTTPS, see ourDocker Deployment Guide.

### Cloud Version

Visithttps://www.dograh.comfor our managed cloud offering.

## 📚Documentation

You can go tohttps://docs.dograh.comfor our documentation.

## 🤝Community & Support

👋Coming from the Better Stack video?Drop your use case in ourpinned GitHub Discussion— we read every reply and the founders personally onboard early adopters.

* Slack— the cornerstone of Dograh AI contributions. Connect with maintainers, discuss features before coding, get help with setup, and stay current on contribution sprints.
* GitHub Discussions— share use cases, ask questions, swap workflow recipes.
* GitHub Issues— report bugs or request features.

👉 Join us →Dograh Community Slack

## 🙌 Contributing

We love contributions! Dograh AI is 100% open source and we intend to keep it that way.

### Getting Started

* Fork the repository
* Create your feature branch (git checkout -b feature/AmazingFeature)
* Commit your changes (git commit -m 'Add some AmazingFeature')
* Push to the branch (git push origin feature/AmazingFeature)
* Open a Pull Request

## ⭐ Star History

## 📄 License

Dograh AI is licensed under theBSD 2-Clause License- the same license as projects that were used in building Dograh AI, ensuring compatibility and freedom to use, modify, and distribute.

## 🏢 About

Built with ❤️ byDograh(Zansat Technologies Private Limited)
Founded by YC alumni and exit founders committed to keeping voice AI open and accessible to everyone.

⭐ Star us on GitHub|☁️ Try Cloud Version|💬 Join Slack

## About

Open Source Voice Agent Platform

app.dograh.com

### Topics

 python

 open-source

 text-to-speech

 ai

 nextjs

 webrtc

 voice

 self-hosted

 telephony

 voip

 speech-to-text

 voice-assistant

 ai-agents

 conversational-ai

 outbound-calls

 fastapi

 voice-ai

 llm

 pipecat

 voice-agents

### Resources

 Readme

 

### License

 BSD-2-Clause license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.5k

 stars
 

### Watchers

21

 watching
 

### Forks

348

 forks
 

 Report repository

 

## Releases38

dograh: v1.30.1

 Latest

 

May 17, 2026

 

+ 37 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python55.6%
* TypeScript40.7%
* Shell2.3%
* JavaScript0.6%
* PowerShell0.6%
* Dockerfile0.1%
* Other0.1%