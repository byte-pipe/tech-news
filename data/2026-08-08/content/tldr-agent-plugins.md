---
title: Agent Plugins
url: https://agent-plugins.org/
site_name: tldr
content_file: tldr-agent-plugins
fetched_at: '2026-08-08T11:25:50.419884'
original_url: https://agent-plugins.org/
date: '2026-08-08'
description: A portable package format for reusable components that extend AI agents.
tags:
- tldr
---

# Agent Plugins

A portable package format for reusable components that extend AI agents.

Agent Plugins is an open, vendor-neutral standard for packaging reusable components into portable plugins. Its version 1.0.0 specification defines a shared format forAgent SkillsandMCP serversthat compatible clients can discover and load consistently.

## Why Agent Plugins?

AI agent clients have developed their own plugin formats, even when plugins contain the same underlying components. Authors must rearrange or duplicate those components for each client, so a plugin packaged for one client may need adaptation before another can use it.

Agent Plugins defines a small interoperability floor for the parts that can be portable across clients. Shared components can use one predictable structure, while distribution, installation, permissions, user experience, and client-specific capabilities remain under each client's control.

## The portable package

An Agent Plugin is a directory with a required manifest and optional components in fixed locations:

my-plugin/

├── plugin.json

├── skills/

│ └── summarize/

│ ├── SKILL.md

│ ├── scripts/

│ └── references/

├── mcp.json

└── com.example.client/

 └── hooks/

* plugin.jsonidentifies the plugin and the Agent Plugins version it targets.
* skills/contains Agent Skills in the format defined by the Agent Skills specification.
* mcp.jsondescribes stdio, Streamable HTTP, or legacy HTTP+SSE MCP servers.
* Reverse-domain extension namespaces let individual clients add behavior without changing the portable core.

## Open development

Agent Plugins is openly licensed and developed in public. Its initial Technical Steering Committee includes Core Maintainers from Amazon, Cursor, Microsoft, OpenAI, and Vercel.

Proposals and technical decisions are public, and participation is open to the broader ecosystem. Ideas for new features and material changes begin inGitHub Discussions, where proposals can establish a concrete portability need and implementer support.

Explore the specification, schemas, governance, and contribution process in theAgent Plugins specification repository.

## Choose your path

### Build a plugin

Create a portable package with skills and MCP servers.

### Implement a client

Load, validate, and run Agent Plugins safely.

### Read the specification

Consult the complete normative specification.

### Browse the schemas

Use the canonical plugin and MCP JSON Schemas.

Compatible Clients

Explore clients that support the portable Agent Plugins format and the components each client can load.