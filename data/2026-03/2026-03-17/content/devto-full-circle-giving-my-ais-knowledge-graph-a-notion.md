---
title: 'Full Circle: Giving My AI''s Knowledge Graph a Notion Interface using MCP - DEV Community'
url: https://dev.to/juandastic/full-circle-giving-my-ais-knowledge-graph-a-notion-interface-using-mcp-2dmp
site_name: devto
content_file: devto-full-circle-giving-my-ais-knowledge-graph-a-notion
fetched_at: '2026-03-17T19:27:46.743614'
original_url: https://dev.to/juandastic/full-circle-giving-my-ais-knowledge-graph-a-notion-interface-using-mcp-2dmp
author: Juan David Gómez
date: '2026-03-17'
description: This is a submission for the Notion MCP Challenge When I started building AI tools for my wife, it... Tagged with devchallenge, notionchallenge, mcp, ai.
tags: '#devchallenge, #notionchallenge, #mcp, #ai'
---

Notion MCP Challenge Submission 🧠

This is a submission for theNotion MCP Challenge

When I started building AI tools for my wife, it was because she had outgrown Notion.

She uses LLMs as a life coach, therapist, and sounding board. To give the AI context, she maintained a massive 35,000-token "Master Prompt" in a Notion page detailing her life, medical history, and goals. She had to manually copy-paste this wall of text into every new chat.

To automate this, I builtSynapse, a system that replaces that manual prompt with a Temporal Knowledge Graph (Neo4j + Graphiti). As she chats, the AI quietly extracts entities and relationships in the background, building a continuous memory.

It worked perfectly. But then I hit a UX wall.

I built a visualizer of the actual knowledge graph so she could explore her AI's memory. I thought it was beautiful. To me, it was fascinating to watch the graph grow and see new connections form over time. But to her, it was just overwhelming. The sheer amount of nodes and floating edges was too much to process, so she ended up completely ignoring that section of the app.

It turns out that while theconceptof a graph is great for understanding relationships, navigating a massive raw graph view is for machines, not humans. She missed Notion. She missed structured tables, clear properties, and the simple ability to just click and type to fix a mistake.

So, I brought the project full circle. I used the new Notion MCP to turn Notion back into the ultimate Human-Machine interface for her AI's brain.

## What I Built

I built abidirectional, human-in-the-loop syncbetween a Neo4j Knowledge Graph and Notion.

This isn't just a one-way "AI appending text to a page" script. It is a dynamic two-way pipeline:

1. The Export (AI Designs the UI):Instead of using hardcoded Notion templates, Synapse compiles the user's graph and asks Gemini todesigna custom database schema. If the user talks a lot about their health, the AI creates a "Medications" database with "Active/Suspended" select tags. If they talk about code, it creates a "Projects" database with tech stacks. No two exports look the same.
2. The Import (Human-in-the-Loop):AI memory systems hallucinate. To fix this, every AI-generated Notion database gets aNeeds Reviewcheckbox and aCorrection Notescolumn. If the AI misunderstood something, my wife just checks the box, types the correction in Notion, and hits sync. The system updates the Knowledge Graph (invalidating the old facts) and automatically patches the Notion row.

## Video Demo

## Show us the code

The entire architecture is open source:

* Backend (Synapse Cortex):https://github.com/juandastic/synapse-cortex
* Frontend (Synapse Chat):https://github.com/juandastic/synapse-chat-ai

## juandastic/synapse-cortex

# Synapse Cortex

Cognitive backend for the Synapse AI Chat application. A stateless REST API that processes conversational data into a dynamic knowledge graph, enabling personalized long-term memory and intelligent context retrieval for AI assistants.

## 📋 Table of Contents

* Overview
* Core Features
* Technical Architecture
* Backend Components
* API Endpoints
* Data Flow
* Technology Stack
* Observability in Axiom
* Notion Export
* Notion Correction Import
* Setup & Deployment
* Demo User Seeding

## Overview

Synapse Cortex is aknowledge graph-powered backenddesigned to give AI chat applications long-term memory capabilities. Instead of treating each conversation in isolation, Synapse Cortex:

1. Ingestsconversational data from chat sessions
2. Extractsentities, relationships, and facts using LLMs
3. Storesthem in a temporal knowledge graph (Neo4j)
4. Retrievesrelevant context for future conversations
5. Visualizesthe knowledge graph for user exploration and debugging

The system is built onGraphiti, a temporal knowledge graph framework that handles entity resolution, relationship extraction, and temporal invalidation of…

View on GitHub

However, to see the actual backend code that implements the Notion integration, you can check theExport feature commitand theCorrection commit.

TheUI workhere was minimal since Notion will be the actual UI, but I decided to have a simple interface to set the Notion config (for simplicity, I did not implement a full OAuth flow) and trigger the export and sync corrections

## How I Used Notion MCP

Integrating AI with rigid APIs is usually a nightmare of mapping schemas, formatting JSON, and handling edge cases. MCP fundamentally changes this. I no longer write rigid ETL pipelines; I just give tools to reasoning engines.

### 1. SDK for Structure, MCP for Intelligence

I split my architecture into two phases.

First, I use the standard Notion SDK to create the empty databases. This is a rigid, structural operation.

Second, I use the@notionhq/notion-mcp-servercombined withLangGraph(a ReAct agent) to actually populate the data and process corrections.

When a row is flagged for correction, I don't write complex if/else logic to figure out how to update Notion. I just pass the user's correction and the updated graph data to the LangGraph agent equipped with the Notion MCP tools.The agent autonomously decideswhether to useAPI-patch-page(to update the specific properties) orAPI-delete-block(if the fact is completely invalidated and the row should be archived).

### 2. The Engineering Deep Dive: Node.js in a Python World

My backend is written in Python (FastAPI). The official Notion MCP server is written in Node.js.

Because Synapse is a multi-tenant system (each user has their own independent Notion OAuth token), I couldn't just leave a single global MCP server running. I needed a way to securely isolate connections and ensure low latency between my Python agent and the MCP tools.

I decided to run the official Node.js MCP server as asubprocess (stdio)directly inside my FastAPI backend.

This created some fun lifecycle management challenges:

1. Docker adjustments:I had to modify my PythonDockerfileto install Node.js so the environment could executenpx @notionhq/notion-mcp-server.
2. Context Management:I built an asynchronous context manager (_NotionAgentContext) in Python. When an export or correction job starts, it spins up the Node subprocess, passes the specific user'sNOTION_TOKENsecurely via environment variables, initializes the LangGraph agent, processes the batches of data, and gracefully shuts down the subprocess when the job is done.

class

_NotionAgentContext
:


async

def

__aenter__
(
self
):


# 1. Start the Node.js MCP subprocess via stdio


self
.
_stdio_cm

=

stdio_client
(
server_params
)


read
,

write

=

await

self
.
_stdio_cm
.
__aenter__
()


# 2. Initialize session and load Notion tools


self
.
_session_cm

=

ClientSession
(
read
,

write
)


session

=

await

self
.
_session_cm
.
__aenter__
()


await

session
.
initialize
()


tools

=

await

load_mcp_tools
(
session
)


# 3. Return a LangGraph autonomous agent equipped with Notion MCP


return

create_react_agent
(
llm
,

tools
)


async

def

__aexit__
(
self
,

exc_type
,

exc_val
,

exc_tb
):


# Gracefully shut down the subprocess to prevent zombie Node processes


await

self
.
_session_cm
.
__aexit__
(
exc_type
,

exc_val
,

exc_tb
)


await

self
.
_stdio_cm
.
__aexit__
(
exc_type
,

exc_val
,

exc_tb
)

Enter fullscreen mode

Exit fullscreen mode

By running it viastdioinstead of SSE, the communication between the LangGraph reasoning loop and the Notion MCP server is lightning fast, localized, and securely scoped to the current user's job.

Notion MCP allowed me to stop writing fragile API wrappers and focus on what actually matters: building a system that lets a human seamlessly collaborate with their AI's memory.

## Conclusion

This project has been incredibly rewarding. My wife absolutely loves the result; she finally has her AI's brain in a format she can actually read, organize, and correct without feeling overwhelmed.

I also have to acknowledge that this Notion MCP Challenge was perfectly timed. I already knew my graph visualizer wasn't working for her, but this contest provided the exact motivation and the right technology (MCP) to bring this bidirectional integration to life. It’s a great feeling when a new tool perfectly aligns with a real-world problem you are trying to solve.

If you are curious about the rest of the Synapse architecture—like why I chose Knowledge Graphs over standard Vector RAG, or how I handled the backend scaling challenges of processing massive context windows—you can check out my previous articles on my DEV profile.

Synapse is live inhttps://synapse-chat.juandago.dev/if you want to check it out

Building software is fun, but seeing it come alive and solve actual problems for the people you care about is magical.

I'd love to hear your thoughts on this approach or how you are using MCP in your own projects. Let's continue the conversation onXor connect onLinkedIn.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
