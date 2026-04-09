---
title: Claude Code on the web \ Anthropic
url: https://www.anthropic.com/news/claude-code-on-the-web
site_name: hackernews
fetched_at: '2025-10-21T11:08:29.116004'
original_url: https://www.anthropic.com/news/claude-code-on-the-web
author: adocomplete
date: '2025-10-21'
description: Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.
---

Product

# Claude Code on the web

Oct 20, 2025
●
2 min
 read

Today, we're introducing Claude Code on the web, a new way to delegate coding tasks directly from your browser.

Now in beta as a research preview, you can assign multiple coding tasks to Claude that run on Anthropic-managed cloud infrastructure, perfect for tackling bug backlogs, routine fixes, or parallel development work.

## Run coding tasks in parallel

Claude Code on the web lets you kick off coding sessions without opening your terminal. Connect your GitHub repositories, describe what you need, and Claude handles the implementation.

Each session runs in its own isolated environment with real-time progress tracking, and you can actively steer Claude to adjust course as it’s working through tasks.

With Claude Code running in the cloud, you can nowrun multiple tasks in parallelacross different repositories from a single interface andship fasterwith automatic PR creation and clear change summaries.

## Flexible for every workflow

The web interface complements your existing Claude Code workflow. Running tasks in the cloud is especially effective for:

* Answering questions about how projects work and how repositories are mapped
* Bugfixes and routine, well-defined tasks
* Backend changes, where Claude Code can use test-driven development to verify changes

You can also use Claude Code on mobile. As part of this research preview, we’re making Claude Code available on our iOS app so developers can explore coding with Claude on the go. It’s an early preview, and we hope to quickly refine the mobile experience based on your feedback.

## Security-first cloud execution

Every Claude Code task runs in an isolated sandbox environment with network and filesystem restrictions. Git interactions are handled through a secure proxy service that ensures Claude can only access authorized repositories—helping keep your code and credentials protected throughout the entire workflow.

You can also add custom network configuration to choose what domains Claude Code can connect to from its sandbox. For example, you can allow Claude to download npm packages over the internet so that it can run tests and validate changes.

Read ourengineering bloganddocumentationfor a deep dive on Claude Code’s sandboxing approach.

## Getting started

Claude Code on the web is available now in research preview for Pro and Max users. Visitclaude.com/codeto connect your first repository and start delegating tasks.

Cloud-based sessions share rate limits with all other Claude Code usage.Explore our documentationto learn more.

News

### Claude for Life Sciences

Oct 20, 2025

News

### Claude and your productivity platforms

Oct 16, 2025

News

### Introducing Agent Skills

Oct 16, 2025
