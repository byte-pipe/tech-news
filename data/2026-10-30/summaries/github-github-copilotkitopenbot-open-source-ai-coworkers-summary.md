---
title: GitHub - CopilotKit/OpenBot: Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided bef...
url: https://github.com/CopilotKit/OpenBot
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-10-30T12:47:48.466720
---

# GitHub - CopilotKit/OpenBot: Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided bef...

# OpenBot Overview

## What it is
- An agent platform that runs inside your own infrastructure using Docker Compose and PostgreSQL.  
- Each coworker (agent) receives its own browser, file space, and a limited set of tools; every action is decided before execution and recorded afterwards.  
- Built on the AG‑UI open protocol, allowing any AG‑UI‑compatible agent (LangGraph, Mastra, CrewAI, Pydantic AI, Google ADK, or custom code) to be added as a coworker.

## Key Features
- Self‑hosted only; no hosted SaaS version to sign up for.  
- Provided as a template repository that you clone, replace example agents in `examples/` with your own, and run.  
- Comes with starter agents such as General Assistant, Knowledge, Risk Analyst, and a catalog of fintech‑specific bots (expense claim reviewer, meeting‑note processor, release‑note drafter, ticket triager, handbook responder, interview writer, on‑call handoff, renewal preparer, customer‑feedback summarizer).  
- A governance gateway mediates and logs every interaction with the computer, files, or external services.  
- Can be run locally on a laptop or deployed within a company’s infrastructure.

## Architecture
- Agents are located in `agent-*` directories.  
- Core services include the UI app, API server, worker, supervisor, and supporting scripts.  
- Docker Compose starts all components; data resides in a private PostgreSQL instance.  
- Model selection is up to the operator; no model is shipped by default. Credentials are encrypted at rest and never logged.  
- Uses CopilotKit Intelligence (free developer plan available) for model serving; compatible with OpenAI, Anthropic, Google, etc.

## Requirements
- Docker (for PostgreSQL and bundled bots).  
- Bun 1.4 or newer (for the app, API server, and tests).  
- A CopilotKit Intelligence project and license (free plan usable).  
- An LLM API key (e.g., OpenAI).

## Quick Start
1. Create an environment file: `cp .env.example .env` then run `bun install`.  
2. Log in to CopilotKit and select a project:  
   `npx --yes copilotkit@latest login`  
   `npx --yes copilotkit@latest project select`  
   Run `bun scripts/setup-learning.ts` to provision the runtime key, create or reuse the `openbotLearning` container, and write settings to `.env`.  
3. Fill remaining required variables such as `OPENAI_API_KEY`.  

## Development Status
- Early beta, under active development; expect rough edges and bugs.  
- Issues and pull requests are welcomed.

## Commercial Offer
- CopilotKit can assist in standing up OpenBot inside your infrastructure, customizing it to match your product, and handing it back for ongoing iteration.