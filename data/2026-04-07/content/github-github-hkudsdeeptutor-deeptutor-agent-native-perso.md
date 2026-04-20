---
title: 'GitHub - HKUDS/DeepTutor: "DeepTutor: Agent-Native Personalized Learning Assistant" · GitHub'
url: https://github.com/HKUDS/DeepTutor
site_name: github
content_file: github-github-hkudsdeeptutor-deeptutor-agent-native-perso
fetched_at: '2026-04-07T11:23:25.417123'
original_url: https://github.com/HKUDS/DeepTutor
author: HKUDS
description: '"DeepTutor: Agent-Native Personalized Learning Assistant" - HKUDS/DeepTutor'
---

HKUDS



/

DeepTutor

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.6k
* Star11.6k




 
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

450 Commits
450 Commits
.github
.github
 
 
assets
assets
 
 
deeptutor
deeptutor
 
 
deeptutor_cli
deeptutor_cli
 
 
docs
docs
 
 
requirements
requirements
 
 
scripts
scripts
 
 
tests
tests
 
 
web
web
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.env.example_CN
.env.example_CN
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.secrets.baseline
.secrets.baseline
 
 
AGENTS.md
AGENTS.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Communication.md
Communication.md
 
 
DeepTutor.code-workspace
DeepTutor.code-workspace
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SKILL.md
SKILL.md
 
 
docker-compose.dev.yml
docker-compose.dev.yml
 
 
docker-compose.ghcr.yml
docker-compose.ghcr.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
View all files

## Repository files navigation

# DeepTutor: Agent-Native Personalized Tutoring

Features·Get Started·Explore·TutorBot·CLI·Community

🇨🇳 中文·🇯🇵 日本語·🇪🇸 Español·🇫🇷 Français·🇸🇦 العربية·🇷🇺 Русский·🇮🇳 हिन्दी·🇵🇹 Português

### 📰 News

[2026.4.4]Long time no see! ✨ DeepTutor v1.0.0 is finally here — an agent-native evolution featuring a ground-up architecture rewrite, TutorBot, and flexible mode switching under the Apache-2.0 license. A new chapter begins, and our story continues!

[2026.2.6]🚀 We've reached 10k stars in just 39 days! A huge thank you to our incredible community for the support!

[2026.1.1]Happy New Year! Join ourDiscord,WeChat, orDiscussions— let's shape the future of DeepTutor together!

[2025.12.29]DeepTutor is officially released!

### 📦 Releases

[2026.4.7]v1.0.0-beta.2— Runtime cache invalidation for hot settings reload, MinerU nested output support, mimic WebSocket fix, Python 3.11+ minimum, and CI improvements.

[2026.4.4]v1.0.0-beta.1— Agent-native architecture rewrite (DeepTutor 2.0) with two-layer plugin model (Tools + Capabilities), CLI & SDK entry points, TutorBot multi-channel bot agent, Co-Writer, Guided Learning, and persistent memory.

Past releases

[2026.1.23]v0.6.0— Session persistence, incremental document upload, flexible RAG pipeline import, and full Chinese localization.

[2026.1.18]v0.5.2— Docling support for RAG-Anything, logging system optimization, and bug fixes.

[2026.1.15]v0.5.0— Unified service configuration, RAG pipeline selection per knowledge base, question generation overhaul, and sidebar customization.

[2026.1.9]v0.4.0— Multi-provider LLM & embedding support, new home page, RAG module decoupling, and environment variable refactor.

[2026.1.5]v0.3.0— Unified PromptManager architecture, GitHub Actions CI/CD, and pre-built Docker images on GHCR.

[2026.1.2]v0.2.0— Docker deployment, Next.js 16 & React 19 upgrade, WebSocket security hardening, and critical vulnerability fixes.

## ✨ Key Features

* Unified Chat Workspace— Five modes, one thread. Chat, Deep Solve, Quiz Generation, Deep Research, and Math Animator share the same context — start a conversation, escalate to multi-agent problem solving, generate quizzes, then deep-dive into research, all without losing a single message.
* Personal TutorBots— Not chatbots — autonomous tutors. Each TutorBot lives in its own workspace with its own memory, personality, and skill set. They set reminders, learn new abilities, and evolve as you grow. Powered bynanobot.
* AI Co-Writer— A Markdown editor where AI is a first-class collaborator. Select text, rewrite, expand, or summarize — drawing from your knowledge base and the web. Every piece feeds back into your learning ecosystem.
* Guided Learning— Turn your materials into structured, visual learning journeys. DeepTutor designs multi-step plans, generates interactive pages for each knowledge point, and lets you discuss alongside each step.
* Knowledge Hub— Upload PDFs, Markdown, and text files to build RAG-ready knowledge bases. Organize insights across sessions in color-coded notebooks. Your documents don't just sit there — they actively power every conversation.
* Persistent Memory— DeepTutor builds a living profile of you: what you've studied, how you learn, and where you're heading. Shared across all features and TutorBots, it gets sharper with every interaction.
* Agent-Native CLI— Every capability, knowledge base, session, and TutorBot is one command away. Rich terminal output for humans, structured JSON for AI agents and pipelines. Hand DeepTutor aSKILL.mdand your agents can operate it autonomously.

## 🚀 Get Started

### Option A — Setup Tour (Recommended)

Asingle interactive scriptthat walks you through everything: dependency installation, environment configuration, live connection testing, and launch. No manual.envediting needed.

git clone https://github.com/HKUDS/DeepTutor.git

cd
 DeepTutor

#
 Create a Python environment

conda create -n deeptutor python=3.11
&&
 conda activate deeptutor

#
 Or: python -m venv .venv && source .venv/bin/activate

#
 Launch the guided tour

python scripts/start_tour.py

The tour asks how you'd like to use DeepTutor:

* Web mode(recommended) — Picks a dependency profile, installs everything (pip + npm), then spins up a temporary server and opens theSettingspage in your browser. A four-step guided tour walks you through LLM, Embedding, and Search provider setup with live connection testing. Once complete, DeepTutor restarts automatically with your configuration.
* CLI mode— A fully interactive terminal flow: choose a dependency profile, install dependencies, configure providers, verify connections, and apply — all without leaving the shell.

Either way, you end up with a running DeepTutor athttp://localhost:3782.

### Option B — Manual Local Install

If you prefer full control, install and configure everything yourself.

1. Install dependencies

git clone https://github.com/HKUDS/DeepTutor.git

cd
 DeepTutor

conda create -n deeptutor python=3.11
&&
 conda activate deeptutor
pip install -e
"
.[server]
"

#
 Frontend

cd
 web
&&
 npm install
&&

cd
 ..

2. Configure environment

cp .env.example .env

Edit.envand fill in at least the required fields:

#
 LLM (Required)

LLM_BINDING
=
openai

LLM_MODEL
=
gpt-4o-mini

LLM_API_KEY
=
sk-xxx

LLM_HOST
=
https://api.openai.com/v1

#
 Embedding (Required for Knowledge Base)

EMBEDDING_BINDING
=
openai

EMBEDDING_MODEL
=
text-embedding-3-large

EMBEDDING_API_KEY
=
sk-xxx

EMBEDDING_HOST
=
https://api.openai.com/v1

EMBEDDING_DIMENSION
=
3072

3. Start services

#
 Backend (FastAPI)

python -m deeptutor.api.run_server

#
 Frontend (Next.js) — in a separate terminal

cd
 web
&&
 npm run dev -- -p 3782

Service

Default Port

Backend

8001

Frontend

3782

Openhttp://localhost:3782and you're ready to go.

### Option C — Docker Deployment

Docker wraps the backend and frontend into a single container — no local Python or Node.js required. Two options depending on your preference:

1. Configure environment variables(required for both options)

git clone https://github.com/HKUDS/DeepTutor.git

cd
 DeepTutor
cp .env.example .env

Edit.envand fill in at least the required fields (same asOption Babove).

2a. Pull official image (recommended)

Official images are published toGitHub Container Registryon every release, built forlinux/amd64andlinux/arm64.

docker compose -f docker-compose.ghcr.yml up -d

To pin a specific version, edit the image tag indocker-compose.ghcr.yml:

image
:
ghcr.io/hkuds/deeptutor:1.0.0
#
 or :latest

2b. Build from source

docker compose up -d

This builds the image locally fromDockerfileand starts the container.

3. Verify & manage

Openhttp://localhost:3782once the container is healthy.

docker compose logs -f
#
 tail logs

docker compose down
#
 stop and remove container

Cloud / remote server deployment

When deploying to a remote server, the browser needs to know the public URL of the backend API. Add one more variable to your.env:

#
 Set to the public URL where the backend is reachable

NEXT_PUBLIC_API_BASE_EXTERNAL
=
https://your-server.com:8001

The frontend startup script applies this value at runtime — no rebuild needed.

Development mode (hot-reload)

Layer the dev override to mount source code and enable hot-reload for both services:

docker compose -f docker-compose.yml -f docker-compose.dev.yml up

Changes todeeptutor/,deeptutor_cli/,scripts/, andweb/are reflected immediately.

Custom ports

Override the default ports in.env:

BACKEND_PORT
=
9001

FRONTEND_PORT
=
4000

Then restart:

docker compose up -d
#
 or docker compose -f docker-compose.ghcr.yml up -d

Data persistence

User data and knowledge bases are persisted via Docker volumes mapped to local directories:

Container path

Host path

Content

/app/data/user

./data/user

Settings, memory, workspace, sessions, logs

/app/data/knowledge_bases

./data/knowledge_bases

Uploaded documents & vector indices

These directories survivedocker compose downand are reused on the nextdocker compose up.

Environment variables reference

Variable

Required

Description

LLM_BINDING

Yes

LLM provider (
openai
,
anthropic
, etc.)

LLM_MODEL

Yes

Model name (e.g.
gpt-4o
)

LLM_API_KEY

Yes

Your LLM API key

LLM_HOST

Yes

API endpoint URL

EMBEDDING_BINDING

Yes

Embedding provider

EMBEDDING_MODEL

Yes

Embedding model name

EMBEDDING_API_KEY

Yes

Embedding API key

EMBEDDING_HOST

Yes

Embedding endpoint

EMBEDDING_DIMENSION

Yes

Vector dimension

SEARCH_PROVIDER

No

Search provider (
tavily
,
jina
,
serper
,
perplexity
, etc.)

SEARCH_API_KEY

No

Search API key

BACKEND_PORT

No

Backend port (default
8001
)

FRONTEND_PORT

No

Frontend port (default
3782
)

NEXT_PUBLIC_API_BASE_EXTERNAL

No

Public backend URL for cloud deployment

DISABLE_SSL_VERIFY

No

Disable SSL verification (default
false
)

### Option D — CLI Only

If you just want the CLI without the web frontend:

pip install -e
"
.[cli]
"

deeptutor chat
#
 Interactive REPL

deeptutor run chat
"
Explain Fourier transform
"

#
 One-shot capability

deeptutor run deep_solve
"
Solve x^2 = 4
"

#
 Multi-agent problem solving

deeptutor kb create my-kb --doc textbook.pdf
#
 Build a knowledge base

SeeDeepTutor CLIfor the full feature guide and command reference.

## 📖 Explore DeepTutor

### 💬 Chat — Unified Intelligent Workspace

Five distinct modes coexist in a single workspace, bound by aunified context management system. Conversation history, knowledge bases, and references persist across modes — switch between them freely within the same topic, whenever the moment calls for it.

Mode

What It Does

Chat

Fluid, tool-augmented conversation. Choose from RAG retrieval, web search, code execution, deep reasoning, brainstorming, and paper search — mix and match as needed.

Deep Solve

Multi-agent problem solving: plan, investigate, solve, and verify — with precise source citations at every step.

Quiz Generation

Generate assessments grounded in your knowledge base, with built-in validation.

Deep Research

Decompose a topic into subtopics, dispatch parallel research agents across RAG, web, and academic papers, and produce a fully cited report.

Math Animator

Turn mathematical concepts into visual animations and storyboards powered by Manim.

Tools aredecoupled from workflows— in every mode, you decide which tools to enable, how many to use, or whether to use any at all. The workflow orchestrates the reasoning; the tools are yours to compose.

Start with a quick chat question, escalate to Deep Solve when it gets hard, generate quiz questions to test yourself, then launch a Deep Research to go deeper — all in one continuous thread.

### ✍️ Co-Writer — AI Inside Your Editor

Co-Writer brings the intelligence of Chat directly into a writing surface. It is a full-featured Markdown editor where AI is a first-class collaborator — not a sidebar, not an afterthought.

Select any text and chooseRewrite,Expand, orShorten— optionally drawing context from your knowledge base or the web. The editing flow is non-destructive with full undo/redo, and every piece you write can be saved straight to your notebooks, feeding back into your learning ecosystem.

### 🎓 Guided Learning — Visual, Step-by-Step Mastery

Guided Learning turns your personal materials into structured, multi-step learning journeys. Provide a topic, optionally link notebook records, and DeepTutor will:

1. Design a learning plan— Identify 3–5 progressive knowledge points from your materials.
2. Generate interactive pages— Each point becomes a rich visual HTML page with explanations, diagrams, and examples.
3. Enable contextual Q&A— Chat alongside each step for deeper exploration.
4. Summarize your progress— Upon completion, receive a learning summary of everything you've covered.

Sessions are persistent — pause, resume, or revisit any step at any time.

### 📚 Knowledge Management — Your Learning Infrastructure

Knowledge is where you build and manage the document collections that power everything else in DeepTutor.

* Knowledge Bases— Upload PDF, TXT, or Markdown files to create searchable, RAG-ready collections. Add documents incrementally as your library grows.
* Notebooks— Organize learning records across sessions. Save insights from Chat, Guided Learning, Co-Writer, or Deep Research into categorized, color-coded notebooks.

Your knowledge base is not passive storage — it actively participates in every conversation, every research session, and every learning path you create.

### 🧠 Memory — DeepTutor Learns As You Learn

DeepTutor maintains a persistent, evolving understanding of you through two complementary dimensions:

* Summary— A running digest of your learning progress: what you've studied, which topics you've explored, and how your understanding has developed.
* Profile— Your learner identity: preferences, knowledge level, goals, and communication style — automatically refined through every interaction.

Memory is shared across all features and all your TutorBots. The more you use DeepTutor, the more personalized and effective it becomes.

### 🦞 TutorBot — Persistent, Autonomous AI Tutors

TutorBot is not a chatbot — it is apersistent, multi-instance agentbuilt onnanobot. Each TutorBot runs its own agent loop with independent workspace, memory, and personality. Create a Socratic math tutor, a patient writing coach, and a rigorous research advisor — all running simultaneously, each evolving with you.

* Soul Templates— Define your tutor's personality, tone, and teaching philosophy through editable Soul files. Choose from built-in archetypes (Socratic, encouraging, rigorous) or craft your own — the soul shapes every response.
* Independent Workspace— Each bot has its own directory with separate memory, sessions, skills, and configuration — fully isolated yet able to access DeepTutor's shared knowledge layer.
* Proactive Heartbeat— Bots don't just respond — they initiate. The built-in Heartbeat system enables recurring study check-ins, review reminders, and scheduled tasks. Your tutor shows up even when you don't.
* Full Tool Access— Every bot reaches into DeepTutor's complete toolkit: RAG retrieval, code execution, web search, academic paper search, deep reasoning, and brainstorming.
* Skill Learning— Teach your bot new abilities by adding skill files to its workspace. As your needs evolve, so does your tutor's capability.
* Multi-Channel Presence— Connect bots to Telegram, Discord, Slack, Feishu, WeChat Work, DingTalk, Email, and more. Your tutor meets you wherever you are.
* Team & Sub-Agents— Spawn background sub-agents or orchestrate multi-agent teams within a single bot for complex, long-running tasks.

deeptutor bot create math-tutor --persona
"
Socratic math teacher who uses probing questions
"

deeptutor bot create writing-coach --persona
"
Patient, detail-oriented writing mentor
"

deeptutor bot list
#
 See all your active tutors

### ⌨️ DeepTutor CLI — Agent-Native Interface

DeepTutor is fully CLI-native. Every capability, knowledge base, session, memory, and TutorBot is one command away — no browser required. The CLI serves both humans (with rich terminal rendering) and AI agents (with structured JSON output).

Hand theSKILL.mdat the project root to any tool-using agent (nanobot, or any LLM with tool access), and it can configure and operate DeepTutor autonomously.

One-shot execution— Run any capability directly from the terminal:

deeptutor run chat
"
Explain the Fourier transform
"
 -t rag --kb textbook
deeptutor run deep_solve
"
Prove that √2 is irrational
"
 -t reason
deeptutor run deep_question
"
Linear algebra
"
 --config num_questions=5
deeptutor run deep_research
"
Attention mechanisms in transformers
"

Interactive REPL— A persistent chat session with live mode switching:

deeptutor chat --capability deep_solve --kb my-kb

#
 Inside the REPL: /cap, /tool, /kb, /history, /notebook, /config to switch on the fly

Knowledge base lifecycle— Build, query, and manage RAG-ready collections entirely from the terminal:

deeptutor kb create my-kb --doc textbook.pdf
#
 Create from document

deeptutor kb add my-kb --docs-dir ./papers/
#
 Add a folder of papers

deeptutor kb search my-kb
"
gradient descent
"

#
 Search directly

deeptutor kb set-default my-kb
#
 Set as default for all commands

Dual output mode— Rich rendering for humans, structured JSON for pipelines:

deeptutor run chat
"
Summarize chapter 3
"
 -f rich
#
 Colored, formatted output

deeptutor run chat
"
Summarize chapter 3
"
 -f json
#
 Line-delimited JSON events

Session continuity— Resume any conversation right where you left off:

deeptutor session list
#
 List all sessions

deeptutor session open
<
id
>

#
 Resume in REPL

Full CLI command reference

Top-level

Command

Description

deeptutor run <capability> <message>

Run any capability in a single turn (
chat
,
deep_solve
,
deep_question
,
deep_research
,
math_animator
)

deeptutor chat

Interactive REPL with optional
--capability
,
--tool
,
--kb
,
--language

deeptutor serve

Start the DeepTutor API server

deeptutor bot

Command

Description

deeptutor bot list

List all TutorBot instances

deeptutor bot create <id>

Create and start a new bot (
--name
,
--persona
,
--model
)

deeptutor bot start <id>

Start a bot

deeptutor bot stop <id>

Stop a bot

deeptutor kb

Command

Description

deeptutor kb list

List all knowledge bases

deeptutor kb info <name>

Show knowledge base details

deeptutor kb create <name>

Create from documents (
--doc
,
--docs-dir
)

deeptutor kb add <name>

Add documents incrementally

deeptutor kb search <name> <query>

Search a knowledge base

deeptutor kb set-default <name>

Set as default KB

deeptutor kb delete <name>

Delete a knowledge base (
--force
)

deeptutor memory

Command

Description

deeptutor memory show [file]

View memory (
summary
,
profile
, or
all
)

deeptutor memory clear [file]

Clear memory (
--force
)

deeptutor session

Command

Description

deeptutor session list

List sessions (
--limit
)

deeptutor session show <id>

View session messages

deeptutor session open <id>

Resume session in REPL

deeptutor session rename <id>

Rename a session (
--title
)

deeptutor session delete <id>

Delete a session

deeptutor notebook

Command

Description

deeptutor notebook list

List notebooks

deeptutor notebook create <name>

Create a notebook (
--description
)

deeptutor notebook show <id>

View notebook records

deeptutor notebook add-md <id> <path>

Import markdown as record

deeptutor notebook replace-md <id> <rec> <path>

Replace a markdown record

deeptutor notebook remove-record <id> <rec>

Remove a record

deeptutor config/plugin/provider

Command

Description

deeptutor config show

Print current configuration summary

deeptutor plugin list

List registered tools and capabilities

deeptutor plugin info <name>

Show tool or capability details

deeptutor provider login <provider>

OAuth login (
openai-codex
,
github-copilot
)

## 🗺️ Roadmap

Status

Milestone

🔜

Authentication & Login
 — Optional login page for public deployments with multi-user support

🔜

Themes & Appearance
 — Diverse theme options and customizable UI appearance

🔜

LightRAG Integration
 — Integrate
LightRAG
 as an advanced knowledge base engine

🔜

Documentation Site
 — Comprehensive docs page with guides, API reference, and tutorials

If you find DeepTutor useful,give us a star— it helps us keep going!

## 🌐 Community & Ecosystem

DeepTutor stands on the shoulders of outstanding open-source projects:

Project

Role in DeepTutor

nanobot

Ultra-lightweight agent engine powering TutorBot

LlamaIndex

RAG pipeline and document indexing backbone

ManimCat

AI-driven math animation generation for Math Animator

From the HKUDS ecosystem:

⚡ LightRAG

🤖 AutoAgent

🔬 AI-Researcher

🧬 nanobot

Simple & Fast RAG

Zero-Code Agent Framework

Automated Research

Ultra-Lightweight AI Agent

## 🤝 Contributing

We hope DeepTutor becomes a gift for the community. 🎁

SeeCONTRIBUTING.mdfor guidelines on setting up your development environment, code standards, and pull request workflow.

## ⭐ Star History

Data Intelligence Lab @ HKU

⭐ Star us·🐛 Report a bug·💬 Discussions

Licensed under theApache License 2.0.

## About

"DeepTutor: Agent-Native Personalized Learning Assistant"

### Topics

 interactive-learning

 multi-agent-systems

 ai-agents

 cli-tool

 rag

 large-language-models

 ai-tutor

 deepresearch

 clawdbot

### Resources

 Readme



### License

 Apache-2.0 license


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

11.6k

 stars


### Watchers

89

 watching


### Forks

1.6k

 forks


 Report repository



## Releases10

v1.0.0-beta.2

 Latest



Apr 7, 2026



+ 9 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python79.0%
* TypeScript19.9%
* JavaScript0.4%
* Dockerfile0.3%
* CSS0.2%
* Shell0.1%
* HTML0.1%
