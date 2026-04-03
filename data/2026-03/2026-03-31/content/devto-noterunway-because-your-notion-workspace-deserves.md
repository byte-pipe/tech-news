---
title: 'NoteRunway: Because Your Notion Workspace Deserves an Elite Crew - DEV Community'
url: https://dev.to/georgekobaidze/noterunway-because-your-notion-workspace-deserves-an-elite-crew-53bk
site_name: devto
content_file: devto-noterunway-because-your-notion-workspace-deserves
fetched_at: '2026-03-31T11:22:23.129351'
original_url: https://dev.to/georgekobaidze/noterunway-because-your-notion-workspace-deserves-an-elite-crew-53bk
author: Giorgi Kobaidze
date: '2026-03-29'
description: This is a submission for the Notion MCP Challenge Table of Contents What I... Tagged with devchallenge, notionchallenge, mcp, ai.
tags: '#devchallenge, #notionchallenge, #mcp, #ai'
---

Notion MCP Challenge Submission 🧠

This is a submission for theNotion MCP Challenge

## Table of Contents

* What I BuiltExplanatory VideoIntroductionThe BackstoryThe 7 Tools
* Explanatory Video
* Introduction
* The Backstory
* The 7 Tools
* Show us the code
* How I Used Notion MCPThe ArchitectureWhy MCP and Not Just the API?Destructive Tool Safety
* The Architecture
* Why MCP and Not Just the API?
* Destructive Tool Safety
* The Tech Behind ItMulti-Provider AI (BYOK)The Archive System
* Multi-Provider AI (BYOK)
* The Archive System
* Wrapping Up

## What I Built

### Explanatory Video

### Introduction

NoteRunway: an AI-powered workspace management tool that helps Notion power users clean up, audit, and command their workspace through a single interface.

Think of it as a flight control tower for your Notion workspace. It scans for problems you didn't know you had, visualizes connections you couldn't see, and lets you talk to your workspace in plain English.

🔗Live Demo → noterunway.pilotronica.com

### The Backstory

I'm a Notion addict. Not the"I use it for grocery lists"kind, rather the"I have 400+ pages, nested databases inside databases, and a set of half-written ideas from 2 AM"kind.

It all started in 2020, when I decided it was time to bring more order into my life. My notes were scattered everywhere, there was some structure, but not nearly enough. I needed something more powerful... something more organized.

Then I discovered Notion and instantly knew it was exactly what I'd been looking for all along and didn't know existed.

You know how it goes, at first, you're fully motivated. Everything's clean, structured, flawless. You're convinced this time you'll manage your notes perfectly.

But sooner or later, every power user ends up in the same place: orphaned pages from long-forgotten projects, duplicate notes written three times because the first two vanished into the void, and dead links leading to pages you archived months ago.

And somewhere in that chaos, there's probably a note with an API key you definitely didn't mean to paste and leave it forever. Have you ever pasted an API key or secret thinking "I'm gonna move it somewhere more secure later"? And that "later" doesn't really come, does it?

I needed a tool that could see the bigger picture, something that could scan everything, something that'd surface what's broken, and help me fix it without blindly deleting content or forcing me to manually comb through bajillion pages.

When the Notion MCP Challenge dropped, it clicked right away. I could build that tool, and give something back to the Notion community while I'm at it.

### The 7 Tools

NoteRunway packs 7 workspace management tools, split between pure scanners and AI-powered analyzers.

Think of it as a crew of seven tools at your disposal, everything you need to keep your Notion workspace in top shape. Each one has a specific role: some scan your workspace to surface hidden issues, others go deeper to analyze patterns and give you smarter insights.

Together, they cut through the clutter, highlight what actually needs attention, and help you clean things up without the risk of losing something important. No guesswork, no endless manual checks, just a clear view of your workspace and the tools to keep it running smoothly.

#### 📊 Workspace Health Dashboard

Your workspace at a glance. Total pages, top-level pages, recently edited, empty pages, and link density (how well-connected your workspace actually is).

It's the "oh wow, I havehow manyempty pages?" moment.

#### 🔍 Duplicate Detection

This is where the AI earns its keep. NoteRunway fetches up to 100 pages with their content snippets, sends them to the LLM with a specialized system prompt, and gets backsemantic duplicate groupswith similarity scores.

Not just "same title" duplicates, it catches pages with different names but overlapping content. The AI picks a recommended "keep" version (⭐), and you choose which ones to archive.

#### 🗑️ Garbage Collector

Rule-based detection across three categories:

* Orphaned— parent page was deleted, child is floating in limbo
* Empty— zero content blocks (you created it and... forgot)
* Stale— untouched for 90+ days (configurable)

Dry-run mode is on by default. You review everything before anything moves.

#### 🔗 Dead Link Detector

Finds @mentions pointing to pages that no longer exist. Every broken mention is tracked back to its source page, so you know exactly where to fix it.

#### 🔐 Sensitive Data Finder

Two-phase security scanner:

Phase 1 (Regex):Scans all pages against 13 patterns: API keys (OpenAI, Anthropic, Stripe, AWS, GitHub), PEM keys, JWTs, database URLs, passwords, credit cards. Findings are alwayspartially redacted, never exposing full values.

Phase 2 (AI Deep Scan):Optionally sends page text to the LLM to catch natural-language secrets that regex misses. Things like"the password is hunter2"or"login: admin/secret123".

#### 🕸️ Dependency Graph

An interactive force-directed graph of your entire workspace. Pages are nodes (colored by depth), connections are edges (solid for parent-child, dashed for @mentions). Orphaned pages glow red.

You can hover, click, collapse branches, and zoom around. It's surprisingly therapeutic to see your workspace as a living network.

#### 💬 Semantic Ask (Agentic Chat)

A natural language interface to your workspace, powered by an agentic AI loop.

Type something like"Find all pages about authentication and summarize them"or"Archive everything in the old-project folder."The AI breaks it into tool calls (search, read, analyze), feeds results back into its context, and proposes structured actions for your approval.

It supports 5 action types:archive,create,rename,append, andupdate, all with a human-in-the-loop confirmation step. No action executes without your explicit "yes."

Just a heads-up: be cautious with destructive actions. Avoid updating or archiving critical data.

This project is still in beta, and I don't want you to risk losing important information. As you know, AI isn't deterministic, and unexpected outcomes can happen.

## Show us the code

Here's the repository:

## georgekobaidze/noterunway

# NoteRunway

### AI-Powered Notion Workspace Management

Clean, organize, and command your Notion workspace with AI. Powered by the Notion MCP.

🔗Live Demo → noterunway.pilotronica.com

## Table of Contents

* Overview
* Features
* Tech Stack
* Architecture
* Project Structure
* Getting Started
* AI Provider Support
* MCP Integration
* Archive System
* Security
* Scripts
* Author
* Acknowledgements
* License

## Overview

NoteRunwayis a browser-based tool that helps Notion power users clean up, audit, and manage their workspace using a combination of deterministic scans and AI-powered intelligence via theNotion MCP.

It connects to your Notion workspace through OAuth, runs server-side analysis via Next.js API routes, and provides a cyberpunk-themed UI for reviewing findings and approving actions.

### Core Principles

Principle

Description

Zero Lock-in

Your data stays in Notion. NoteRunway never stores workspace content.

Human-in-the-Loop

No destructive action runs without explicit user approval.

Privacy First

AI keys stored only in your browser (BYOK). Sent per-request to NoteRunway APIs and never persisted server-side.

…

View on GitHub

## How I Used Notion MCP

This is the core of the whole project. NoteRunway uses theNotion MCP Serveras the execution layer for all workspace interactions in the Semantic Ask feature.

### The Architecture

Browser → Next.js API (SSE) → Vercel AI SDK → MCP Client → notion-mcp-server (stdio) → Notion API

Enter fullscreen mode

Exit fullscreen mode

Here's the flow:

1. User sends a messagein the Ask interface
2. Vercel AI SDKprocesses it withstreamText()and the selected LLM
3. When the AI decides it needs workspace data, itcalls tools:search_pages,get_page,get_page_content,run_analysis
4. These tools route throughMCPClient, which communicates with the Notion MCP server overstdio(JSON-RPC 2.0)
5. The MCP server translates tool calls intoNotion API requestsand returns structured results
6. Results feed back into the AI's context for the next reasoning step (up to 10 steps)
7. When the AI wants to make changes, it callspropose_actions, which streams proposed actions to the UI forhuman approval
8. Only after the user confirms does the action execute via MCP

### Why MCP and Not Just the API?

I useboth. Here's the split:

* NotionClient (direct SDK)for bulk reads, workspace scans, pagination-heavy operations. It's faster for fetching 400 pages than routing through MCP.
* MCPClient (MCP server)for all writes like creating, archiving, renaming, updating pages. MCP provides a sandboxed execution layer with tool-level safety.

This hybrid approach gives me thespeedof direct API access with thesafetyof MCP's tool calling protocol.

### Destructive Tool Safety

Any tool that modifies workspace data (patch, post-page, delete, move) requires anapproved: trueflag. The AI can propose actions, butnothing destructive runs without the user clicking "Execute."

## The Tech Behind It

Layer

Technology

Why

Framework

Next.js 16 (App Router)

Full-stack React with API routes

AI SDK

Vercel AI SDK 6

Unified streaming + tool calling across 4 providers

MCP

@notionhq/notion-mcp-server

Notion workspace access via Model Context Protocol

Visualization

React Flow 11

Force-directed graph for the dependency viewer

Validation

Zod 4

Runtime schema validation for all API inputs/outputs

Styling

Tailwind CSS 4 + shadcn/ui

Cyberpunk aesthetic with accessible components

### Multi-Provider AI (BYOK)

NoteRunway supports4 AI providerswith13 models: OpenAI (GPT-5.4, GPT-5 Mini), Anthropic (Claude Opus 4.6, Haiku 4.5), xAI (Grok 4, Grok 3), and Google (Gemini 2.5 Pro/Flash).

Your API key stays in yourbrowser's localStorage. It's sent per-request in an HTTP header, used once to create a provider instance, and discarded. NoteRunway's server never stores, logs, or persists your key.

### The Archive System

Every destructive action creates an audit trail:

NoteRunway Archive/
├── Duplicates/
│ └── [Audit Stub] Original Title
├── Garbage Collection/
│ └── [Audit Stub] Stale Page Name
└── Semantic Ask/
 └── [Audit Stub] Archived via Chat

Enter fullscreen mode

Exit fullscreen mode

Each audit stub contains a callout with the archive date, reason, and a faithful copy of the original content. The original page is soft-archived to Notion's trash (recoverable for 30 days).

Nothing is ever truly deleted without a paper trail.

## Wrapping Up

NoteRunway started as a personal itch, a messy workspace and a dev challenge deadline. It turned into something I'm going to use every week.

Building with the Notion MCP was a revelation. The ability to give an AI structured access to a workspace, with tool-level control over what it can read and write, opens up workflows that feel like magic. Ask a question, get an answer sourced from your actual pages. Propose a cleanup, review it, execute it. All in one flow.

If you're a Notion power user drowning in pages, give it a spin:noterunway.pilotronica.com

And if you find an API key you forgot about in a meeting note... you're welcome. 😄

Built with ☕ and too many late nights byGiorgi Kobaidze

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (27 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse