---
title: 'GitHub - secureagentics/Adrian: Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts. · GitHub'
url: https://github.com/secureagentics/Adrian
site_name: tldr
content_file: tldr-github-secureagenticsadrian-open-source-runtime-ai
fetched_at: '2026-07-27T19:33:03.896098'
original_url: https://github.com/secureagentics/Adrian
date: '2026-07-27'
description: Open-source runtime AI agent security tool - monitors and controls AI agents, catching malicious tool use, prompt injection, and policy drift in real time, before the agent acts. - secureagentics/Adrian
tags:
- tldr
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 secureagentics

 

/

Adrian

Public

* NotificationsYou must be signed in to change notification settings
* Fork83
* Star437

 
 
 
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

53 Commits
53 Commits
.claude-plugin
.claude-plugin
 
 
.github
.github
 
 
assets
assets
 
 
backend
backend
 
 
data
data
 
 
deploy
deploy
 
 
docs
docs
 
 
examples
examples
 
 
frontend
frontend
 
 
integrations/
claude-code
integrations/
claude-code
 
 
models
models
 
 
proto
proto
 
 
scripts
scripts
 
 
sdk
sdk
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
CLA.md
CLA.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTORS.md
CONTRIBUTORS.md
 
 
GET_STARTED_AI_GUIDE.md
GET_STARTED_AI_GUIDE.md
 
 
LICENSE
LICENSE
 
 
LICENSE_HEADER.txt
LICENSE_HEADER.txt
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
compose.yaml
compose.yaml
 
 
View all files

## Repository files navigation

### Agent attacks slip past static analysis and network monitoring.

Adrian catches them at runtime, by watching what the agent actually does (its actions and its reasoning) and stepping in before it acts. Open source, free forever.

+35% detection accuracy · 4x more nuanced attacks caughtvs behaviour-only monitoring (OpenAI & DeepMind research)

⭐ If you think agents need a runtime security layer, star the repo. It is how new people find Adrian, and how we know to keep building it in the open.

Adrian is an open-source,AARM-alignedruntime security monitoring and control engine for AI agents. It analyses both agent activity logs (tool calls, actions, outputs) and reasoning traces to detect malicious, misaligned, or out-of-remit behaviour, and optionally intervene in-flight. SDKs are available for Python (LangChain) and TypeScript (sdk/typescript/README.md), plus a nativeClaude Code pluginthat secures every tool call from your terminal.

🆕 Claude Code plugin - now live.Drop Adrian into Claude Code and every tool call is classified in real time, with risky actions blocked or held for your approval right in the terminal. No code changes: install with/plugin marketplace add secureagentics/Adrianthen/adrian-init. Full guide:integrations/claude-code/README.md.

Documentation•Dashboard•Discord•LinkedIn

▶️See it in action:Adrian catches an agent going out-of-remit in real time and steps in before the action lands.

Adrian_Demo.mp4

New to Adrian? Check out theLaunch Video.

## Why Adrian is different

Most agent monitoring stops at activity logs: APIs, MCP, DB interactions, tool calls, etc. Adrian enhances this by also analysing the agent's reasoning: understandingwhyit took an action, under what context, and what it is planning on doing next. Combining behaviour and reasoning analysis like this is exactly what theOpenAI and DeepMind researchfound catches far more, and Adrian is the first tool to put it into a deployable security control, free forever.

What it catches:

* Prompt injection and jailbreaks, direct and indirect
* Tool poisoning and unsafe or off-policy tool calls
* Data exfiltration and secret / credential leakage
* Privilege escalation and out-of-remit actions

Classifiers trained on prompt-injection datasets only catch what they have seen before. Adrian works differently: it holds a working understanding of what your agent is meant to do and judges each new action against that, correlated across the whole session. So when your e-commerce agent starts resetting user passwords, something no training set would flag, Adrian catches it.

## Quickstart

Want the stupidly simple, 60-second hands-off install?Feed your coding agent (Claude, Codex, Cursor, etc.) this file:GET_STARTED_AI_GUIDE.md. It will walk you through the installation process (video guide here). Always review instructions manually.

The next fastest way to try Adrian is the managed dashboard atapp.adrian.secureagentics.ai. Sign-up takes a minute and there is nothing to install beyond the SDK. To run Adrian on your own infrastructure instead, jump toSelf-hostingbelow.

1. Sign up atapp.adrian.secureagentics.aiand generate an API key.
2. Configure Adrian for your agent and your preferences (remit of your agent, audit vs block mode, alerting channels, accepted behaviours vs known-risks).
3. Install the SDK:pip install adrian-sdk
4. Install LangChain and the provider for your agent's model (the SDK auto-instruments LangChain / LangGraph; pick whichever provider matches your model):pip install langchain langchain-openai#or langchain-anthropic, etc.#or, in a uv project: uv add langchain langchain-openailangchainpullslanggraphin, so this covers bothcreate_agentandcreate_react_agent. Last verified 2026-06-24 withlangchain==1.3.9,langgraph==1.2.5,langchain-core==1.4.7,langchain-openai==1.3.2. Supported:langchain/langgraph/langchain-openai>=1.0,<2.0,langchain-core>=1.2.19,<2.0.
5. Wrap your LangChain agent. Two lines of Adrian (init+shutdown) bracket your normal LangChain / LangGraph code:importasyncioimportadrianfromlangchain_openaiimportChatOpenAIasyncdefmain():adrian.init(api_key="adr_live_...")llm=ChatOpenAI(model="gpt-4o")response=awaitllm.ainvoke("Find the most underpriced recent IPOs and build an investment strategy",
 )print(response.content)adrian.shutdown()asyncio.run(main())Full runnable version (with env-var checks) atexamples/python/quickstart.py. More complex examples using agents are inexamples/python/.
6. Run your agent. Events appear in the dashboard within seconds, classified by severity.

Full guide:Quickstart.

## Self-hosting

Adrian supports entirely offline, data sovereign deployments using just a handful of docker commands. This repository ships everything needed to run the entire Adrian stack on a single host: the Go backend (WebSocket + dashboard API + AI engine), the Next.js dashboard, the Python SDK, and a Llama.cpp container that serves a local Gemma model. No managed cloud, no telemetry leaving the box.

Hardware support:Tested on NVIDIA GPUs with Gemma 4 (E2B / E4B) which is the model the bootstrap picker downloads by default. CPU-only is technically possible but will be slow on real workloads with those sized models.

### Prerequisites

* A host with Docker + Docker Compose v2.
* AnNVIDIA GPUwith recent CUDA driver and theNVIDIA Container Toolkitinstalled (for the bundled Llama.cpp classifier). ~10 GB free disk for the model.

### Bring-up

1. Clone:git clone https://github.com/secureagentics/Adrian
cd Adrian
2. Run bootstrap.Createsdata/adrian.db, applies migrations, generates a random admin password, and writes.env. With no--ggufflag, the bootstrap interactively offers to download the recommended on-device classifier (Gemma 4 E4B, ~5 GB, or E2B ~3 GB) into./models/.#Default: interactive picker downloads Gemma 4 E4B / E2Bdocker compose --profile setup run --rm setup bootstrap#Already have a GGUF under ./models/? Pass it by namedocker compose --profile setup run --rm setup bootstrap \
 --gguf my-model.gguf
3. Start the stack.docker compose --profile llm up -d
4. Open the dashboard.Browse tohttp://localhost:3000. Sign in withadmin@localhostplus the password the bootstrap printed; you'll be prompted to set a new one. Create an SDK API key and configure Adrian to monitor your specific agent fromSettings → Agents → New key.
5. Wrap your agent.The SDK lives in-tree undersdk/. Install it into a fresh.venvvia the bundled Make target (usesuv):make sdk-installsource.venv/bin/activateInstall LangChain and the provider for your agent's model into the same venv:uv pip install"langchain>=1.0,<2.0""langchain-openai>=1.0,<2.0"#swap langchain-openai for your model's providerlangchainpullslanggraphin, so this covers bothcreate_agentandcreate_react_agent. Last verified 2026-06-24 withlangchain==1.3.9,langgraph==1.2.5,langchain-core==1.4.7,langchain-openai==1.3.2.Use the sameadrian.initsnippet as in theQuickstartabove. The SDK defaults tows://localhost:8080/ws, so a self-hosted setup needs nothing more than the API key - drop thews_url=line.

Toreset the admin password,change the modeland much more check out the dedicatedDocs site.

## Architecture

flowchart TD
 Agent[Agent runtime] --> SDK[Adrian SDK]
 SDK --> Backend[Adrian backend]
 Backend --> Classifier[Classifier model]
 Classifier --> Verdict{Verdict}
 Verdict --> Control[Control plane]
 Verdict -.->|"Alert /<br>Human Review /<br>Block"| Agent

 
Loading

## Integrations

Supported
On roadmap

Frameworks

  
 
  
 

  
 
  
 

Alerting

  
 

  
 
  
 

Full list:Integrations.New:theClaude Code pluginis live. ⭐ the repo orjoin Discord.

## Contributing

⭐ Star the repo if Adrian is useful. Then seeCONTRIBUTING.mdfor the full guide. In short: sign theCLA, branch offmain, follow the PR template, and use British English / no em-dashes in prose.

SeeCONTRIBUTORS.mdfor the list of people who have shaped Adrian, and how to add yourself.

## Licence

Adrian is released under theApache 2.0 licence. New source files should carry the SPDX header fromLICENSE_HEADER.txt.

## Community

* Discordfor chat with the team and other Adrian users
* LinkedInfor product updates

## Featured on

* Product Hunt
* There's An AI For That