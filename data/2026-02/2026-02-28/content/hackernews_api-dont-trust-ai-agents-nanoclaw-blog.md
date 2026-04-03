---
title: Don't trust AI agents | NanoClaw Blog
url: https://nanoclaw.dev/blog/nanoclaw-security-model
site_name: hackernews_api
content_file: hackernews_api-dont-trust-ai-agents-nanoclaw-blog
fetched_at: '2026-02-28T19:08:30.629815'
original_url: https://nanoclaw.dev/blog/nanoclaw-security-model
author: gronky_
date: '2026-02-28'
description: AI agents need a security model that assumes things will go wrong. The right response isn't better permission checks, it's architecture that makes trust unnecessary.
tags:
- hackernews
- trending
---

When you’re building with AI agents, they should be treated as untrusted and potentially malicious. Whether you’re worried about prompt injection, a model trying to escape its sandbox, or something nobody’s thought of yet, regardless of what your threat model is, you shouldn’t be trusting the agent. The right approach isn’t better permission checks or smarter allowlists. It’s architecture that assumes agents will misbehave and contains the damage when they do.

That’s the principle I builtNanoClawon.

## Don’t trust the process

OpenClaw runs directly on the host machine by default. It has an opt-in Docker sandbox mode, but it’s turned off out of the box, and most users never turn it on. Without it, security relies entirely on application-level checks: allowlists, confirmation prompts, a set of “safe” commands. These checks come from a place of implicit trust that the agent isn’t going to try to do something wrong. Once you adopt the mindset that an agent is potentially malicious, it’s obvious that application-level blocks aren’t enough. They don’t provide hermetic security. A determined or compromised agent can find ways around them.

In NanoClaw, container isolation is a core part of the architecture. Each agent runs in its own container, on Docker or an Apple Container on macOS. Containers are ephemeral, created fresh per invocation and destroyed afterward. The agent runs as an unprivileged user and can only see directories that have been explicitly mounted in. A container boundary is enforced by the OS.

## Don’t trust other agents

Even when OpenClaw’s sandbox is enabled, all agents share the same container. You might have one agent as a personal assistant and another for work, in different WhatsApp groups or Telegram channels. They’re all in the same environment, which means information can leak between agents that are supposed to be accessing different data.

Agents shouldn’t trust each other any more than you trust them. In NanoClaw, each agent gets its own container, filesystem, and Claude session history. Your personal assistant can’t see your work agent’s data because they run in completely separate sandboxes.

SHARED CONTAINER

Personal

Assistant

Work

Agent

Family Group

Agent

Shared filesystem

All credentials accessible

All session histories visible

All mounted data shared

All agents see everything

PER-AGENT CONTAINERS

Personal Assistant

/data/personal

own session

ro

×

Work Agent

/data/work

own session

rw

×

Family Group Agent

/data/family

own session

ro

Agents isolated from each other

The container boundary is the hard security layer — the agent can’t escape it regardless of configuration. On top of that, a mount allowlist at~/.config/nanoclaw/mount-allowlist.jsonacts as an additional layer of defense-in-depth: it exists to prevent theuserfrom accidentally mounting something that shouldn’t be exposed, not to prevent the agent from breaking out. Sensitive paths (.ssh,.gnupg,.aws,.env,private_key,credentials) are blocked by default. The allowlist lives outside the project directory, so a compromised agent can’t modify its own permissions. The host application code is mounted read-only, so nothing an agent does can persist after the container is destroyed.

People in your groups shouldn’t be trusted either. Non-main groups are untrusted by default. Other groups, and the people in them, can’t message other chats, schedule tasks for other groups, or view other groups’ data. Anyone in a group could send a prompt injection, and the security model accounts for that.

## Don’t trust what you can’t read

OpenClaw has nearly half a million lines of code, 53 config files, and over 70 dependencies. This breaks the basic premise of open source security. Chromium has 35+ million lines, but you trust Google’s review processes. Most open source projects work the other way: they stay small enough that many eyes can actually review them. Nobody has reviewed OpenClaw’s 400,000 lines. It was written in weeks with no proper review process. Complexity is where vulnerabilities hide, andMicrosoft’s analysisconfirmed this: OpenClaw’s risks could emerge through normal API calls, because no one person could see the full picture.

NanoClaw is one process and a handful of files. We rely heavily on Anthropic’s Agent SDK, the wrapper around Claude Code, for session management, memory compaction, and a lot more, instead of reinventing the wheel. A competent developer can review the entire codebase in an afternoon. This isa deliberate constraint, not a limitation. Ourcontribution guidelinesaccept bug fixes, security fixes, and simplifications only.

New functionality comes through skills: instructions with a full working reference implementation that a coding agent merges into your codebase. You review exactly what code will be added before it lands. And you only add the integrations you actually need. Every installation ends up as a few thousand lines of code tailored to the owner’s exact requirements.

This is the real difference. With a monolithic codebase of 400,000 lines, even if you only enable two integrations, the rest of the code is still there. It’s still loaded, still part of your attack surface, still reachable by prompt injections and rogue agents. You can’t disentangle what’s active from what’s dormant. You can’t audit it because you can’t even define the boundary of what “your code” is. With skills, the boundary is obvious: it’s a few thousand lines, it’s all code you chose to add, and you can read every line of it. The core is actually getting smaller over time: WhatsApp support, for example, is being pulled out and packaged as a skill.

## Design for distrust

If a hallucination or a misbehaving agent can cause a security issue, then the security model is broken. Security has to be enforced outside the agentic surface, not depend on the agent behaving correctly. Containers, mount restrictions, and filesystem isolation all exist so that even when an agent does something unexpected, the blast radius is contained.

None of this eliminates risk. An AI agent with access to your data is inherently a high-risk arrangement. But the right response is to make that trust as narrow and as verifiable as possible. Don’t trust the agent. Build walls around it.

You can read NanoClaw’ssource codeandfull security model; they’re short enough to read in an afternoon.