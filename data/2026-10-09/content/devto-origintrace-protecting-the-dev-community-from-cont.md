---
title: 'OriginTrace: Protecting the DEV Community from Content Theft using Sanity Context MCP'
url: https://dev.to/dj29/origintrace-protecting-the-dev-community-from-content-theft-using-sanity-context-mcp-j5c
site_name: devto
content_file: devto-origintrace-protecting-the-dev-community-from-cont
fetched_at: '2026-10-09T17:19:21.267522'
original_url: https://dev.to/dj29/origintrace-protecting-the-dev-community-from-content-theft-using-sanity-context-mcp-j5c
author: Dhruv Jani
date: '2026-10-04'
description: 'This is a submission for the Sanity Challenge, Path One: Ship an Agent That Queries Real Content ... Tagged with devchallenge, sanitychallenge, sanity, ai.'
tags: '#devchallenge, #sanitychallenge, #sanity, #ai'
---

Sanity Challenge Path One Submission

This is a submission for theSanity Challenge, Path One: Ship an Agent That Queries Real Content

## What I Built

A few weeks ago, I was checking my DEV.to dashboard and noticed something weird in theTraffic Sourcespanel. Views were coming from websites I'd never heard of — random blogs, content farms, sites I'd never visited, let alone posted on.

So I clicked through. And there it was: my article, word for word, on someone else's website. Some had credited me. Most hadn't.

That moment of"wait, is this... stolen?"is something every content creator eventually hits. But figuring out whether a repost is actually plagiarism or a legitimate cross-post with credit is surprisingly hard. You have to manually compare the text, check if they mentioned your name, see if they linked back. And if they didn't? Good luck drafting a DMCA notice from scratch.

OriginTrace automates the entire thing.

It's an AI-powered content provenance agent with three core capabilities:

1. 🔍 The Scanner— Paste any DEV.to article URL. OriginTrace extracts distinctive phrases, searches the entire web via Google (Serper API), scrapes up to 15 candidate pages, and runs a multi-signal overlap analysis (word overlap, 5-gram shingling, LCS ratio) to determine if they copied your content.
2. ⚖️ The Verdict Engine— For every copy found, OriginTrace doesn't just say "it's a match." It checks structured attribution evidence:Does the copy mention the original author's name? Does it link back to the original post? Does it use attribution phrases like "via" or "originally published on"?Based on these boolean signals, it renders a verdict:credited_syndication(legal, no action needed) orunattributed_repost(DMCA time).
3. 💬 The Sanity AI Agent— This is the heart of the Path One submission. A conversational AI agent powered entirely by theSanity Knowledge Base and Context MCP. It lets youtalkto your provenance data. Ask it:"Which copycat had the highest overlap but still credited me?"or"Draft a DMCA takedown for the worst offender."The agent dynamically queries the structured content in Sanity and gives you actionable, source-backed answers.

Every article, every provenance check, every attribution signal, and every DMCA template is persisted as structured JSON documents in Sanity's Content Lake — creating an immutable, queryable ledger of who copied what, when, and whether they gave credit.

## Demo

🔗Live App:origintrace.onrender.com

📺Video Walkthrough:

To test the Sanity AI Agent:(Note: For the best experience, please scan a DEV.to post on the homepage first so the Sanity Knowledge Base has your structured data to query!)Visitorigintrace.onrender.com/chatand try asking:

* "Which article has the highest overlap percentage?"
* "Did the top copycat credit the original author?"
* "Draft a DMCA takedown notice for the worst offender."

The AI Agent querying Sanity via Context MCP, with transparent "Agent Thoughts" blocks showing its reasoning process.

A structured response: the agent analyzed boolean attribution fields from Sanity, rendered a verdict table, and concluded that no DMCA was needed because the copy properly credited the author.

The scanner homepage — paste a DEV.to URL and the programmatic pipeline crawls the web for copies.

Real-time animated radar scanner during an active web crawl.

Scan results with overlap percentages, attribution verdicts, and DMCA generation — all backed by Sanity.

## Code

## JaniDhruv/OriginTrace

### OriginTrace uses Sanity Knowledge Base reconciliation as the provenance engine. Your published articles are the canonical source; a checked URL becomes a KB source; Context's reconciliation surfaces the conflict with citations through MCP.

# OriginTrace

AI-Powered Content Plagiarism Detective & DMCA AgentBuilt forPath One: Ship an Agent That Queries Real Content— Sanity Challenge 2026

Live Demo·GitHub·How It Works·The AI Agent

## 🧠 TL;DR

Paste a DEV.to article URL → OriginTrace's programmatic pipeline crawls the web for stolen copies → structured evidence is persisted to theSanity Content Lake→ then chat with theAI Agent(powered by NVIDIA NIM +Sanity Context MCP) to analyze the data, determine attribution verdicts, generate DMCA takedown notices, and eventrigger new scans directly from the chat.

Why this only works with structured content:The agent doesn't keyword-search for answers — it queries boolean attribution flags (hasAuthorName,hasOriginalLink), exactoverlapPercentintegers, andverdictenums from Sanity. A keyword search would never be able to answer"Which copycat had the highest overlap but still credited the…

View on GitHub

## How I Used Sanity

### The Core Thesis: This Agent Only Works Because the Content Is Structured

OriginTrace's AI Agent doesn't do keyword search. It queriestyped fieldsin Sanity — booleans, integers, enums, and string arrays — to answer questions that would be impossible with unstructured text.

Here's a concrete example. When a user asks:

"Which copycat had the highest overlap but still credited the original author?"

The agent connects toSanity Context MCPand queries the Content Lake. It needs to:

1. FilterprovenanceCheckdocuments whereverdict != "no_match"
2. Sort byoverlapPercent(a number field) descending
3. Checkattribution.hasAuthorName(a boolean) andattribution.hasOriginalLink(a boolean)
4. Readattribution.signals(a string array) for the exact credit items found

No keyword search in the world can answer that. The answer requires comparing anumberagainstbooleansacross multiple documents. That's why structured content matters.

### Sanity Schema Design

Four document types power everything:

article— The canonical source of truth. When a user scans a DEV.to URL, the pipeline fetches the article, extracts its content, and persists it in Sanity with a reference to itsauthor. This establishes the provenance claim.

provenanceCheck— The evidence record. Every candidate copy found on the web gets its own check document containing:

* overlapPercent(number) — similarity score from the multi-signal NLP engine
* verdict(enum) —credited_syndication,unattributed_repost, orno_match
* attribution(object) — structured booleans:hasAuthorName,hasOriginalLink,hasAttributionPhrase,isProperlyAttributed, plussignals[]andmissing[]arrays
* dmcaTemplate(text) — a pre-generated legal takedown notice
* reconciledEntries(array) — matched passages between original and copy

author— Referenced by articles, containsnameandhandlefor attribution matching.

user— Account-level document withemail,authId, andavatarUrlfor future per-user gating.

### Sanity Context MCP Integration

The AI Agent connects to Sanity Context MCP via theAI SDK(@ai-sdk/mcpwith HTTP transport). At runtime, the agent:

1. Callsinitial_contextto get a Knowledge Base outline
2. Usesgroq_queryto dynamically write and execute GROQ queries against the Content Lake
3. Interprets the structured JSON results (booleans, numbers, arrays) to formulate human-readable answers
4. Cites the source documents in its responses

// 1. Connect to Sanity Context MCP

const
 
mcpClient
 
=
 
await
 
createMCPClient
({

 
transport
:
 
{

 
type
:
 
'
http
'
,

 
url
:
 
SANITY_CONTEXT_ENDPOINT
,

 
headers
:
 
{
 
Authorization
:
 
`Bearer 
${
mcpToken
}
`
 
},

 
},

});

// 2. Fetch MCP tools & combine with our custom scan_article action tool

const
 
mcpTools
 
=
 
await
 
mcpClient
.
tools
();

const
 
tools
 
=
 
{
 
...
mcpTools
,
 
scan_article
:
 
scanArticleTool
 
};

// 3. Stream response using NVIDIA NIM with injected Sanity tools

const
 
result
 
=
 
streamText
({

 
model
:
 
nim
.
chatModel
(
'
nvidia/nemotron-3.5-lightning-30b-a3b
'
),

 
tools
,

 
messages
,

 
system
:
 
agentSystemPrompt
,

});

Enter fullscreen mode

Exit fullscreen mode

### Pre-Fetched Structured Context (Not Just MCP)

Before the agent even starts reasoning, the backend runs a dedicatedfetchSanityContext()function that executes GROQ queries directly against Sanity to build a structured snapshot of all indexed articles and their provenance checks — including per-article breakdowns of actionable vs. credited counts, attribution booleans, overlap percentages, and aggregate platform stats. This pre-fetched context is injected into the agent's system prompt so it can answer summary questions ("How many articles have been scanned?") instantly, without burning an MCP round-trip.

### What The Agent Actually Does With Retrieved Content

Sanity Field

Type

Agent Behavior

overlapPercent

number

Ranks copycats: 
"the highest overlap is 98%"

verdict

string
 (enum)

Filters results: 
"3 unattributed reposts found"

attribution.hasAuthorName

boolean

Evaluates credit: 
"the copy does mention your name"

attribution.hasOriginalLink

boolean

Evaluates backlinks: 
"no link to the original post"

attribution.signals

string[]

Explains what credit exists: 
"uses 'via' and links to the original"

attribution.missing

string[]

Explains gaps: 
"missing author name and original URL"

dmcaTemplate

text

Retrieves and customizes the pre-generated DMCA notice

## Sanity Project Details

Sanity Project ID:iossngh3Dataset:production

The schema is defined in TypeScript atsanity/schemas/— the core document isprovenanceCheck.tswith its nestedattributionobject containing the boolean evidence fields.

## Agent Session

This project was built iteratively across multiple agent-assisted IDE sessions over the course of the challenge period. TheREADMEcontains a full technical breakdown of the agent architecture, schema design decisions, and the complete pipeline flow — including ASCII architecture diagrams showing how every component connects.

## Technical Highlights

### ⚡ Lightning Fast Agent Reasoning with NVIDIA NIM

Action Agents that use tools (like Sanity Context MCP) require multiple "thinking" loops before they finally respond to the user. If the underlying LLM is slow, the chat experience feels broken.

To solve this, the OriginTrace Agent is powered byNVIDIA NIM, specifically running theNemotron 3.5 Lightningmodel. This provides the massive context window needed to ingest complex Sanity JSON payloads, while delivering the ultra-low latency required for real-time tool calling.

### 🧠 Custom Multi-Signal Overlap Engine

We didn't just want to rely on basic keyword matching. OriginTrace implements a robust NLP engine in TypeScript that resists common plagiarism obfuscation (like deleting a sentence or swapping synonyms). It calculates an overalloverlapPercentusing a weighted trio of algorithms:

1. Word Overlap (20%): Jaccard similarity of shared vocabulary.
2. 5-Gram Shingling (50%): Detects structurally identical paragraphs by matching overlapping 5-word chunks.
3. Longest Common Subsequence / LCS (30%): Handles reordering and injected words by finding the longest contiguous identical string.

## Future Enhancements (Beyond the Hackathon)

OriginTrace is currently a fully functional prototype built in hackathon scope. The AI Agent and Sanity Ledger are currently inBeta, operating as a global, public ledger (similar to a blockchain explorer) where anyone can query all scanned DEV.to URLs.

Here is the future roadmap:

* 🔐 User Authentication: Add NextAuth/JWT so each author has a private dashboard and personal AI Agent session that only queriestheirspecific provenance data.
* 🌐 Multi-Platform Support: Extend the scanner to index Hashnode, Medium, and personal blogs.
* 📬 Automated Monitoring: Cron-based scheduled scans to proactively alert authors when new stolen copies appear.
* 🤖 Paraphrase Detection: Upgrade the NLP engine with LLM embeddings to catch "rewritten" content that evades traditional word-overlap algorithms.

### Tech Stack

Component

Technology

Frontend

Next.js 16 (App Router)

AI Agent LLM

NVIDIA NIM (Nemotron 3.5 Lightning)

Agent Framework

AI SDK (
ai
 + 
@ai-sdk/mcp
 + 
@ai-sdk/react
)

MCP Bridge

Sanity Context MCP (HTTP transport)

Knowledge Base

Sanity Content Lake (GROQ queries)

Web Search

Serper.dev (Google Search API)

NLP Engine

Custom TypeScript (word overlap, 5-gram shingling, LCS)

Content Extraction

Mozilla Readability + Cheerio + JSDOM

Deployment

Render

Thanks for reading! If you've ever seen your own content on a site you didn't post to, OriginTrace was built for you. 🛡️

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (27 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse