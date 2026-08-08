---
title: Introducing Agent Plugins - Vercel
url: https://vercel.com/blog/introducing-agent-plugins
site_name: tldr
content_file: tldr-introducing-agent-plugins-vercel
fetched_at: '2026-08-09T00:34:53.647635'
original_url: https://vercel.com/blog/introducing-agent-plugins
date: '2026-08-09'
description: Agent Plugins 1.0.0 is an open, vendor-neutral specification for packaging Agent Skills and MCP servers into distributable plugins that compatible AI agent clients can discover and load.
tags:
- tldr
---

A common format for packaging Agent Skills and MCP servers into distributable plugins

Today, Agent Plugins 1.0.0 is publicly available.Agent Pluginsis an open, vendor-neutral standard for plugins that extend AI agents.

Agent Skillsprovide reusable instructions and resources for AI agents.MCP serversconnect agents to tools and services. Both can be reused across clients, but clients often package and discover them differently.

Agent Plugins gives compatible clients a common format: a directory with aplugin.jsonmanifest and fixed locations for its components. The format is intentionally small and easy to implement, and it leaves installation, distribution, policy, user experience, and client-specific capabilities to each client.

## Copy link to headingOne package for the portable parts

Extension authors often adapt the same component to several client formats. Even though the underlying Skill or MCP server is identical, clients often expect different top-level metadata, discovery paths, or MCP configuration.

Agent Plugins gives those shared components one predictable, structured home:

my-plugin/
├── plugin.json
├── skills/
│ └── summarize/
│ ├── SKILL.md
│ ├── scripts/
│ └── references/
├── mcp.json
└── com.example.client/

A minimal JSON manifest (plugin.json) identifies the specification version and names the plugin:

plugin.json
1
{
2
 
"$schema"
:
 
"https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
,
3
 
"name"
:
 
"my-plugin"
4
}

Those two fields are the minimum requirement for the manifest, and the rest of the contract is represented in the file structure of the directory itself. A reusable component should not need to be repackaged for every client, so the format specifies only what a client needs to discover and load what is inside.

Every compatible client checks forplugin.jsonat the plugin root. Clients that support Skills discover them underskills/. Clients that support MCP servers read their configuration frommcp.json. A client can support either component type or both. After the client validates the manifest, components are validated independently, so one invalid component does not disable unrelated ones.

For plugin authors, that means fewer client-specific conventions for the same component. For client implementers, the specification defines a small, deterministic contract for discovery, validation, and loading.

## Copy link to headingSmall on purpose

Agent Plugins defines the portable contract for a plugin and leaves the behavior of the client up to each client.

Version 1 focuses that contract on two component types: Agent Skills and MCP servers. Both already have specifications and meaningful adoption of their own, and Agent Plugins does not attempt to redefine them. Agent Plugins provides a shared definition of how clients find the components together in a distributable plugin.

Other components, such as commands, hooks, and agents, remain with clients. The Technical Steering Committee may consider additional component types in future versions as semantics converge and a demonstrated portability need emerges.

Keeping the boundary small makes the format easier to implement and gives the ecosystem room to converge before adding more portable surface area.

## Copy link to headingClients retain flexibility

Clients need freedom to innovate while a shared format evolves, so Agent Plugins includes a namespaced extension mechanism for client-specific data and files.

Extensions remain outside the portable contract. Each client defines its own namespace, and other clients ignore it. This prevents client-specific behavior from leaking into the common format or blocking adoption of the shared components. A client-specific capability can remain client-specific until there is reason and consensus to standardize it.

## Copy link to headingAn open, multi-vendor project

Vercel initiated the proposal, which representatives from Amazon Web Services (AWS), Anysphere, GitHub, Microsoft, OpenAI, and Vercel refined collaboratively into Agent Plugins 1.0.0.

The initial Technical Steering Committee includes Core Maintainers from AWS, Cursor, Microsoft, OpenAI, and Vercel.

The project is openly licensed, and its maintainers, contribution process, and technical decisions are public. No single company's product roadmap sets the format's direction.

## Copy link to headingBuild with Agent Plugins 1.0.0

The specification, its JSON Schemas, and guides for plugin authors and client implementers are available atagent-plugins.org. Governance and the contribution process live in theAgent Plugins specification repositoryon GitHub.

If you author agent extensions, you can use the specification to package Skills and MCP servers behind one portable manifest. If you build an agent client, the specification's conformance checklist defines the minimum requirements for discovering and loading Agent Plugins.

At launch, Agent Plugins are supported across:

* ChatGPT and Codex
* Cursor
* GitHub Copilot
* Kiro
* VS Code

Plugin authors can package components once, and their plugin will automatically carry between supporting clients.

Agent Plugins is a contract between the authors who build extensions for agents and the clients that load them. That contract is now defined and open for both sides to shape.

## Contributors

Eric Dodds,Andrew Qu