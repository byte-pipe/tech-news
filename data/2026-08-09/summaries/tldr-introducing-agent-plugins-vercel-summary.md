---
title: Introducing Agent Plugins - Vercel
url: https://vercel.com/blog/introducing-agent-plugins
date: 2026-08-09
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-09T00:36:36.140855
---

# Introducing Agent Plugins - Vercel

# Introducing Agent Plugins - Vercel

## Overview
- Agent Plugins 1.0.0 is publicly released as an open, vendor‑neutral standard for extending AI agents.  
- It defines a common, lightweight directory format that includes a `plugin.json` manifest and fixed locations for Agent Skills and MCP servers.  
- Installation, distribution, policy, UX, and client‑specific capabilities remain the responsibility of each client.

## Plugin Structure
- Example layout:  
  ```
  my-plugin/
  ├── plugin.json
  ├── skills/
  │   └── summarize/
  │       ├── SKILL.md
  │       ├── scripts/
  │       └── references/
  ├── mcp.json
  └── com.example.client/
  ```
- Minimal `plugin.json` contains only `$schema` and `name`.  
- Clients look for `plugin.json` at the root; they discover Skills under `skills/` and MCP configuration in `mcp.json`.  
- Validation of each component is independent, so an invalid component does not affect others.

## Design Philosophy
- The contract focuses on two component types: Agent Skills and MCP servers, both of which already have their own specifications.  
- Other component types (commands, hooks, agents) are left to clients, with the possibility of future inclusion as needs converge.  
- A namespaced extension mechanism allows clients to add proprietary data without affecting the shared format.

## Ecosystem & Governance
- Initiated by Vercel and refined with AWS, Anysphere, GitHub, Microsoft, OpenAI, and Vercel.  
- Technical Steering Committee includes core maintainers from AWS, Cursor, Microsoft, OpenAI, and Vercel.  
- The project is openly licensed, with public repositories, contribution processes, and transparent technical decisions.

## Adoption & Usage
- Specification, JSON Schemas, and author/implementer guides are available at **agent-plugins.org**; governance lives in the GitHub repository.  
- Supported at launch by:  
  - ChatGPT and Codex  
  - Cursor  
  - GitHub Copilot  
  - Kiro  
  - VS Code  
- Authors can package a plugin once and have it work across all supporting clients.

## Contributors
- Eric Dodds  
- Andrew Qu