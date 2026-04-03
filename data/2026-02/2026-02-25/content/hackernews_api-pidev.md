---
title: pi.dev
url: https://pi.dev
site_name: hackernews_api
content_file: hackernews_api-pidev
fetched_at: '2026-02-25T11:53:12.030402'
original_url: https://pi.dev
author: kristianpaul
date: '2026-02-24'
description: A terminal-based coding agent
tags:
- hackernews
- trending
---

There are many coding agents, but this one is mine.

 GitHub


 npm


 Discord


$
 npm install -g @mariozechner/pi-coding-agent

Copy

About

## Why pi?

Pi is a minimal terminal coding harness. Adapt pi to your workflows, not the other way around. Extend it with TypeScriptextensions,skills,prompt templates, andthemes. Bundle them aspi packagesand share via npm or git.

Pi ships with powerful defaults but skips features like sub-agents and plan mode. Ask pi to build what you want, or install a package that does it your way.

Four modes: interactive, print/JSON,RPC, and SDK. Seeclawdbotfor a real-world integration.

Read the docs

Providers & Models

## 15+ providers, hundreds of models

Anthropic, OpenAI, Google, Azure, Bedrock, Mistral, Groq, Cerebras, xAI, Hugging Face, Kimi For Coding, MiniMax, OpenRouter, Ollama, and more. Authenticate via API keys or OAuth.

Switch models mid-session with/modelorCtrl+L. Cycle through your favorites withCtrl+P.

Add custom providers and models viamodels.jsonorextensions.

Sessions

## Tree-structured, shareable history

Sessions are stored as trees. Use/treeto navigate to any previous point and continue from there. All branches live in a single file. Filter by message type, label entries as bookmarks.

Export to HTML with/export, or upload to a GitHub gist with/shareand get a shareable URL that renders it.

Context

## Context engineering

Pi'sminimal system promptand extensibility let you do actual context engineering. Control what goes into the context window and how it's managed.

AGENTS.md:Project instructions loaded at startup from~/.pi/agent/, parent directories, and the current directory.

SYSTEM.md:Replace or append to the default system prompt per-project.

Compaction:Auto-summarizes older messages when approaching the context limit. Fully customizable viaextensions: implement topic-based compaction, code-aware summaries, or use different summarization models.

Skills:Capability packages with instructions and tools, loaded on-demand. Progressive disclosure without busting the prompt cache. Seeskills.

Prompt templates:Reusable prompts as Markdown files. Type/nameto expand. Seeprompt templates.

Dynamic context:Extensionscan inject messages before each turn, filter the message history, implement RAG, or build long-term memory.

Queuing

## Steer or follow up

Submit messages while the agent works.Entersends a steering message (delivered after current tool, interrupts remaining tools).Alt+Entersends a follow-up (waits until the agent finishes).

Extensions

## Primitives, not features

Features that other agents bake in, you can build yourself. Extensions are TypeScript modules with access to tools, commands, keyboard shortcuts, events, and the full TUI.

Sub-agents,plan mode,permission gates,path protection,SSH execution,sandboxing, MCP integration, custom editors, status bars, overlays.Yes, Doom runs.

Don't want to build it? Ask pi to build it for you. Or install apackagethat does it your way. See the50+ examples.

Packages

## Install and share

Bundle extensions, skills, prompts, and themes as packages. Install from npm or git:

$
 pi install npm:@foo/pi-tools
$
 pi install git:github.com/badlogic/pi-doom

Pin versions with@1.2.3or@tag. Update all withpi update, list withpi list, configure withpi config.

Test without installing usingpi -e git:github.com/user/repo.

Find packages onnpmorDiscord. Share yours with thepi-packagekeyword.

Browse packages

Integration

## Four modes

Interactive:The full TUI experience.

Print/JSON:pi -p "query"for scripts,--mode jsonfor event streams.

RPC:JSON protocol over stdin/stdout for non-Node integrations. Seedocs/rpc.md.

SDK:Embed pi in your apps. Seeclawdbotfor a real-world example.

Philosophy

## What we didn't build

Pi is aggressively extensible so it doesn't have to dictate your workflow. Features that other tools bake in can be built withextensions,skills, or installed from third-partypi packages. This keeps the core minimal while letting you shape pi to fit how you work.

No MCP.Build CLI tools with READMEs (seeSkills), or build an extension that adds MCP support.Why?

No sub-agents.There's many ways to do this. Spawn pi instances via tmux, or build your own withextensions, or install a package that does it your way.

No permission popups.Run in a container, or build your own confirmation flow withextensionsinline with your environment and security requirements.

No plan mode.Write plans to files, or build it withextensions, or install a package.

No built-in to-dos.Use a TODO.md file, or build your own withextensions.

No background bash.Use tmux. Full observability, direct interaction.

Read theblog postfor the full rationale.

Community

## Get involved

Issues:GitHubfor bugs and features.

Discord:Community serverfor discussion and sharing.

Docs:READMEanddocs/for everything else.

MIT License •Mario Zechner&contributors

 pi.dev domain graciously donated by


 exe.dev


❤️
