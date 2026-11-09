---
title: "GitHub - garrytan/gbrain: Garry's Opinionated OpenClaw/Hermes Agent Brain · GitHub"
url: https://github.com/garrytan/gbrain
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-10T04:42:04.130429
---

# GitHub - garrytan/gbrain: Garry's Opinionated OpenClaw/Hermes Agent Brain · GitHub

# GBrain – Garry’s Opinionated OpenClaw/Hermes Agent Brain

## Overview
- MIT‑licensed, self‑hostable knowledge‑base for AI agents; optional paid hosted service at gbrain.io.  
- Stores explicit facts with provenance, supports corrections, withdrawals, and makes memory available across multiple agents.  
- Built by Garry Tan (President & CEO of Y Combinator) to power his own OpenClaw and Hermes deployments (≈155 k pages, 24 k people, 5 k companies, 66 autonomous cron jobs).

## Core Features
- **Memory Model**  
  - Keyless keyword retrieval, optional semantic search, synthesis, and background enrichment.  
  - Memory skills live alongside knowledge in the agent’s content root.  

- **Retrieval Options**  
  - Keyword/semantic retrieval for raw chunks.  
  - Synthesis layer that returns a fully‑cited answer with gap analysis.  
  - Typed knowledge graph for fast relationship queries (e.g., “who works at X?”) with benchmark‑level performance.  

- **Sharing & Security**  
  - Authorized catalog for agents; only approved editors can publish.  
  - Remote clients constrained by source and operation grants plus visibility filters.  
  - Separate trust boundaries for local files and shared database credentials.  

- **Scalability & Performance**  
  - 24/7 daemon ingests meetings, emails, tweets, voice calls, and ideas; enriches and consolidates memory overnight.  
  - Relationship retrieval runs in milliseconds on dense clusters; improves BrainBench R@5 from 0.6626 to 0.7241.  

## Setup Options
1. **Add GBrain to an existing agent** – keep the agent’s identity; start with guides for Grok Bot, Muse, or Codex/Claude Code.  
2. **Run locally and expose via MCP** – one command publishes the brain over Tailscale; agents can “use my brain over mcp”.  
3. **Connect to an existing hosted brain** – choose native OAuth or private‑machine connection; manage permissions via MCP admin.  

## Typical Interaction
- User asks: “What do I need to know before my meeting with Alice tomorrow?”  
- GBrain returns a concise answer (e.g., “Alice runs engineering at Acme…”) together with citations, eliminating the need to open multiple pages manually.

## Documentation & Resources
- Quick‑start guides: `AGENTS.md`, `BOOTSTRAP_FOR_AGENTS.md`, `INSTALL_FOR_AGENTS.md`.  
- Design details in `DESIGN.md`; contribution guidelines in `CONTRIBUTING.md`.  
- Model lists in `llms.txt` (summary) and `llms-full.txt` (full map).  

## Licensing & Availability
- Free to self‑host under the MIT license.  
- Optional hosted version (gbrain.io) provides a managed brain, integrated with ChatGPT, Claude, and Cursor, with email support.  

## Vision
- Provide a strategic “moat” of persistent, searchable context that never gets lost.  
- Enable agents to answer directly from personal knowledge rather than returning raw document lists.  
- Run entirely on the user’s hardware, database, and keys, keeping data under full control.