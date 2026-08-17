---
title: How it works | Foreman - eve Software Factory
url: https://ask-foreman.dev/docs/how-it-works
site_name: tldr
content_file: tldr-how-it-works-foreman-eve-software-factory
fetched_at: '2026-08-17T11:22:22.395007'
original_url: https://ask-foreman.dev/docs/how-it-works
date: '2026-08-17'
description: The runtime map of Foreman, covering what runs where, how the filesystem defines the agent, and the three boundaries that shape the design.
tags:
- tldr
---

Menu

# How it works

Copy page
Copy page

The runtime map of Foreman, covering what runs where, how the filesystem defines the agent, and the three boundaries that shape the design.

Copy for LLM
Markdown
View Markdown
Ask AI about this page

Foreman is one eve agent with five subagents, three inbound channels, and two durable stores. Everything it can do is declared as a file underagent/, and eve discovers the surface from the filesystem at build time.

## What runs where

Component
Lives in
Responsibility
Orchestrator
agent/agent.ts
, 
agent/instructions.ts
Routes work between stations, assembles the pull request, speaks to people
Stations
agent/subagents/{classifier,analyst,implementer,reviewer}/
The four-stage pipeline every work item passes through
Researcher
agent/subagents/researcher/
Optional web research, run before the Analyst when an item turns on an external fact
Inbound surfaces
agent/channels/
Turn GitHub webhooks, Linear Agent Sessions, and local dev requests into sessions
GitHub tools
agent/extensions/github.ts
31 allowlisted 
github__*
 tools, 12 of them gated
Linear tools
agent/connections/linear.ts
Linear's hosted MCP server, writes denied on unattended runs
Root tools
agent/tools/
The five memory tools, one artifact reader, and one that disables a framework built-in
Shared logic
agent/lib/
Trust predicates, approval policies, git safety, model assignments, and the Blob layer holding every reserved prefix
Skills
agent/skills/
Load-on-demand instruction packages for the orchestrator

## The agent directory

In eve, identity comes from the filesystem rather than anamefield. The fileagent/tools/read_factory_brain.tsis the toolread_factory_brain, and the directoryagent/subagents/classifier/lowers into the toolclassifier. Renaming something means moving the file.

agent
agent.ts
instructions.ts
sandbox.ts
channels
connections
extensions
lib
skills
subagents
analyst
classifier
implementer
researcher
reviewer
tools

## Three boundaries

Most of Foreman's behavior falls out of three structural decisions. They hold because of how the agent is wired, not because a prompt asks nicely.

### Stations inherit nothing

Every declared subagent runs in a fresh child session with none of the root's instructions, skills, connections, tools, or sandbox. That has two consequences worth internalizing.

The orchestrator must pack everything a station needs into the delegation message: the work item verbatim, plus every prior stage's output. Stations never see the conversation history, and they cannot read thefactory brain, so any repository fact that matters has to be woven into the message.

Long documents are the one exception, and they travel by reference rather than inline. The station that produced one saves it as ahandoff artifactand returns the id, the orchestrator relays that id, and the receiving station opens the document itself.

The upside is that each station's blast radius is readable at a glance. Whatever sits inagent/subagents/<id>/is the complete list of what that station can do.

### Trust is stamped at dispatch

Every channel decides who the caller is from the signed webhook, before the model reads anything, and writes that decision into session auth. Nothing downstream re-derives trust from model-readable content, because model-readable content is exactly what an attacker controls.

agent/lib/trust.tsis the single authority that reads those stamps. New capabilities gate on its predicates rather than inventing their own caller check. Thetrust modelcovers the caller classes and policies.

### Each station works in its own sandbox

Every eve agent gets a sandbox whether or not it asks for one, so all five subagents run in one. What separates them is what is inside it.

The Analyst, Implementer, and Reviewer each declare their ownsandbox.ts, so each gets a separate Vercel Sandbox holding its own clone ofFACTORY_REPO. The three declarations are functionally identical, and none is more isolated than the others. The Reviewer's copy just carries the most weight, because it fetches the pushed branch into a clean checkout and therefore reviews what was actually pushed rather than the Implementer's working tree.

The Classifier and Researcher never set one up, so they get the default: a working environment with an empty/workspaceand no repository in it.

The three repository sandboxes share their bootstrap throughagent/lib/github/repo-sandbox.ts. The clone andFACTORY_SETUP_COMMANDrun once per template build, and each session pays only a fetch. Git always targets the literalhttps://github.com/<FACTORY_REPO>.gitURL rather thanorigin, because remote config inside a sandbox is model-writable.

## What persists and what does not

Three things survive a run, and all three live in Vercel Blob under reserved prefixes.

State
Durable
Notes
Factory brain
Yes
One document per target repository, read by every run
User preferences
Yes
One document per person
Handoff artifacts
Yes
Written once, never overwritten or deleted, but only the run that minted an id knows it
Root thread checkout
No
Rebuilt per session by the GitHub channel
Analyst, Implementer, and Reviewer clones
No
Rebuilt per template build, refreshed per session
Conversation history
No
Each webhook dispatch is a fresh session

The last row explains a design choice that looks odd otherwise. Because each dispatch starts clean, the red-CI fix loop counts its own earlier comments on the pull request thread to enforce its 2-attempt cap. The thread is the only durable record those runs share.

Handoff artifacts are durable in storage without being durable in practice. Nothing lists or expires them, but an id only ever reaches the next station through a delegation message, so a later run has no way to find one. That makes them a handoff mechanism rather thanmemory.

## Next steps

### The pipeline

How a work item moves through the four stations to a draft pull request.

### Stations reference

Model, tools, sandbox, and output contract for each of the five subagents.

### Trust model

Caller classes, approval policies, and the reasoning behind each gate.

### Glossary

Definitions for principal, parks, task mode, and the rest of the vocabulary.

Previous
Getting started
Next
The pipeline