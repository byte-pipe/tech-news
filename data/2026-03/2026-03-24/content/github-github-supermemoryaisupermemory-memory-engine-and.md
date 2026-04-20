---
title: 'GitHub - supermemoryai/supermemory: Memory engine and app that is extremely fast, scalable. The Memory API for the AI era. · GitHub'
url: https://github.com/supermemoryai/supermemory
site_name: github
content_file: github-github-supermemoryaisupermemory-memory-engine-and
fetched_at: '2026-03-24T11:20:47.613622'
original_url: https://github.com/supermemoryai/supermemory
author: supermemoryai
description: Memory engine and app that is extremely fast, scalable. The Memory API for the AI era. - supermemoryai/supermemory
---

supermemoryai



/

supermemory

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.8k
* Star18.2k




 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

1,472 Commits
1,472 Commits
.github/
workflows
.github/
workflows
 
 
apps
apps
 
 
packages
packages
 
 
skills/
supermemory
skills/
supermemory
 
 
.gitignore
.gitignore
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
biome.json
biome.json
 
 
bun.lock
bun.lock
 
 
package.json
package.json
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

State-of-the-art memory and context engine for AI.

Docs·Quickstart·Dashboard·Discord

Supermemory is the memory and context layer for AI.#1 onLongMemEval,LoCoMo, andConvoMem— the three major benchmarks for AI memory.

We are a research lab building the engine, plugins and tools around it.

Your AI forgets everything between conversations. Supermemory fixes that.

It automatically learns from conversations, extracts facts, builds user profiles, handles knowledge updates and contradictions, forgets expired information, and delivers the right context at the right time. Full RAG, connectors, file processing — the entire context stack, one system.

🧠
Memory

Extracts facts from conversations. Handles temporal changes, contradictions, and automatic forgetting.

👤
User Profiles

Auto-maintained user context — stable facts + recent activity. One call, ~50ms.

🔍
Hybrid Search

RAG + Memory in a single query. Knowledge base docs and personalized context together.

🔌
Connectors

Google Drive · Gmail · Notion · OneDrive · GitHub — auto-sync with real-time webhooks.

📄
Multi-modal Extractors

PDFs, images (OCR), videos (transcription), code (AST-aware chunking). Upload and it works.

All of this is in our single memory structure and ontology.

## Use Supermemory

### 🧑‍💻 I use AI tools

Build your own personal supermemory by using our app. Buildspersistent memory graph across every conversation.

Your AI remembers your preferences, projects, past discussions — and gets smarter over time.

→ Jump to User setup

### 🔧 I'm building AI products

Add memory, RAG, user profiles, and connectors to your agents and apps witha single API.

No vector DB config. No embedding pipelines. No chunking strategies.

→ Jump to developer quickstart

## Give your AI memory

The Supermemory App, browser extension, plugins and MCP server gives any compatible AI assistant persistent memory. One install, and your AI remembers you.

### The app

You can use supermemory without any code, by using our consumer-facing app for free.

Start athttps://app.supermemory.ai

It also comes with an agent embedded inside, which we call Nova.

### Supermemory Plugins

Supermemory comes built with Plugins for Claude Code, OpenCode and OpenClaw.

These plugins are implementations of the supermemory API, and they are open source!

You can find them here:

* Openclaw plugin:https://github.com/supermemoryai/openclaw-supermemory
* Claude code plugin:https://github.com/supermemoryai/claude-supermemory
* OpenCode plugin:https://github.com/supermemoryai/opencode-supermemory

### MCP - Quick install

npx -y install-mcp@latest https://mcp.supermemory.ai/mcp --client claude --oauth=yes

Replaceclaudewith your client:cursor,windsurf,vscode, etc.

Read more about our MCP here -https://supermemory.ai/docs/supermemory-mcp/mcp

### What your AI gets

Tool

What it does

memory

Save or forget information. Your AI calls this automatically when you share something worth remembering.

recall

Search memories by query. Returns relevant memories + your user profile summary.

context

Injects your full profile (preferences, recent activity) into the conversation at start. In Cursor and Claude Code, just type
/context
.

### How it works

Once installed, Supermemory runs in the background:

1. You talk to your AI normally.Share preferences, mention projects, discuss problems.
2. Supermemory extracts and stores the important stuff.Facts, preferences, project context — not noise.
3. Next conversation, your AI already knows you.It recalls what you're working on, how you like things, what you discussed before.

Memory is scoped withprojects(container tags) so you can separate work and personal context, or organize by client, repo, or anything else.

### Supported clients

Claude Desktop·Cursor·Windsurf·VS Code·Claude Code·OpenCode·OpenClaw

The MCP server is open source —view the source.

### Manual configuration

Add this to your MCP client config:

{

"mcpServers"
: {

"supermemory"
: {

"url"
:
"
https://mcp.supermemory.ai/mcp
"

 }
 }
}

Or use an API key instead of OAuth:

{

"mcpServers"
: {

"supermemory"
: {

"url"
:
"
https://mcp.supermemory.ai/mcp
"
,

"headers"
: {

"Authorization"
:
"
Bearer sm_your_api_key_here
"

 }
 }
 }
}

## Build with Supermemory (API)

If you're building AI agents or apps, Supermemory gives you the entire context stack through one API — memory, RAG, user profiles, connectors, and file processing.

### Install

npm install supermemory
#
 or: pip install supermemory

### Quickstart

import

Supermemory

from

"supermemory"
;

const

client

=

new

Supermemory
(
)
;

// Store a conversation

await

client
.
add
(
{


content
:
"User loves TypeScript and prefers functional patterns"
,


containerTag
:
"user_123"
,

}
)
;

// Get user profile + relevant memories in one call

const

{
 profile
,
 searchResults
}

=

await

client
.
profile
(
{


containerTag
:
"user_123"
,


q
:
"What programming style does the user prefer?"
,

}
)
;

// profile.static → ["Loves TypeScript", "Prefers functional patterns"]

// profile.dynamic → ["Working on API integration"]

// searchResults → Relevant memories ranked by similarity

from

supermemory

import

Supermemory

client

=

Supermemory
()

client
.
add
(

content
=
"User loves TypeScript and prefers functional patterns"
,

container_tag
=
"user_123"

)

result

=

client
.
profile
(
container_tag
=
"user_123"
,
q
=
"programming style"
)

print
(
result
.
profile
.
static
)
# Long-term facts

print
(
result
.
profile
.
dynamic
)
# Recent context

Supermemory automatically extracts memories, builds user profiles, and returns relevant context. No embedding pipelines, no vector DB config, no chunking strategies.

### Framework integrations

Drop-in wrappers for every major AI framework:

// Vercel AI SDK

import

{

withSupermemory

}

from

"@supermemory/tools/ai-sdk"
;

const

model

=

withSupermemory
(
openai
(
"gpt-4o"
)
,

"user_123"
)
;

// Mastra

import

{

withSupermemory

}

from

"@supermemory/tools/mastra"
;

const

agent

=

new

Agent
(
withSupermemory
(
config
,

"user-123"
,

{

mode
:
"full"

}
)
)
;

Vercel AI SDK·LangChain·LangGraph·OpenAI Agents SDK·Mastra·Agno·Claude Memory Tool·n8n

### Search modes

// Hybrid (default) — RAG + Memory in one query

const

results

=

await

client
.
search
.
memories
(
{


q
:
"how do I deploy?"
,


containerTag
:
"user_123"
,


searchMode
:
"hybrid"
,

}
)
;

// Returns deployment docs (RAG) + user's deploy preferences (Memory)

// Memories only

const

results

=

await

client
.
search
.
memories
(
{


q
:
"user preferences"
,


containerTag
:
"user_123"
,


searchMode
:
"memories"
,

}
)
;

### User profiles

Traditional memory relies on search — you need to know what to ask for. Supermemory automatically maintains a profile for every user:

const

{
 profile
}

=

await

client
.
profile
(
{

containerTag
:
"user_123"

}
)
;

// profile.static → ["Senior engineer at Acme", "Prefers dark mode", "Uses Vim"]

// profile.dynamic → ["Working on auth migration", "Debugging rate limits"]

One call. ~50ms. Inject into your system prompt and your agent instantly knows who it's talking to.

### Connectors

Auto-sync external data into your knowledge base:

Google Drive·Gmail·Notion·OneDrive·GitHub·Web Crawler

Real-time webhooks. Documents automatically processed, chunked, and searchable.

### API at a glance

Method

Purpose

client.add()

Store content — text, conversations, URLs, HTML

client.profile()

User profile + optional search in one call

client.search.memories()

Hybrid search across memories and documents

client.search.documents()

Document search with metadata filters

client.documents.uploadFile()

Upload PDFs, images, videos, code

client.documents.list()

List and filter documents

client.settings.update()

Configure memory extraction and chunking

Full API reference →supermemory.ai/docs

## Benchmarks

Supermemory is state of the art across all major AI memory benchmarks:

Benchmark

What it measures

Result

LongMemEval

Long-term memory across sessions with knowledge updates

81.6% — #1

LoCoMo

Fact recall across extended conversations (single-hop, multi-hop, temporal, adversarial)

#1

ConvoMem

Personalization and preference learning

#1

We also builtMemoryBench— an open-source framework for standardized, reproducible benchmarks of memory providers. Compare Supermemory, Mem0, Zep, and others head-to-head:

bun run src/index.ts run -p supermemory -b longmemeval -j gpt-4o -r my-run

### Benchmarking your own memory solution

We provide an Agent skill for companies to benchmark their own context and memory solutions against supermemory.

npx skills add supermemoryai/memorybench

Simply run this and do/benchmark-context- Supermemory will automatically do the work for you!

## How memory works under the hood

Your app / AI tool
 ↓
 Supermemory
 │
 ├── Memory Engine Extracts facts, tracks updates, resolves contradictions,
 │ auto-forgets expired info
 ├── User Profiles Static facts + dynamic context built from engine, always fresh
 ├── Hybrid Search RAG + Memory in one query
 ├── Connectors Real-time sync from Google Drive, Gmail, Notion, GitHub...
 └── File Processing PDFs, images, videos, code → searchable chunks

Memory is not RAG.RAG retrieves document chunks — stateless, same results for everyone. Memory extracts and tracksfacts about usersover time. It understands that "I just moved to SF" supersedes "I live in NYC." Supermemory runs both together by default, so you get knowledge base retrievalandpersonalized context in every query. Read more about this here -https://supermemory.ai/docs/concepts/memory-vs-rag

Automatic forgetting.Supermemory knows when memories become irrelevant. Temporary facts ("I have an exam tomorrow") expire after the date passes. Contradictions are resolved automatically. Noise never becomes permanent memory.

## Links

* 📖Documentation
* 🚀Quickstart
* 🧪MemoryBench
* 🔌Integrations
* 💬Discord
* 𝕏Twitter

Give your AI a memory. It's about time..

## About

Memory engine and app that is extremely fast, scalable. The Memory API for the AI era.

supermemory.ai/docs

### Topics

 postgres

 typescript

 memory

 remix

 tailwindcss

 vite

 cloudflare-workers

 cloudflare-kv

 cloudflare-pages

 drizzle-orm

 ai-memory

 agent-memory

### Resources

 Readme



### License

 MIT license


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

18.2k

 stars


### Watchers

81

 watching


### Forks

1.8k

 forks


 Report repository



### Uh oh!

There was an error while loading.Please reload this page.





## Contributors75

+ 61 contributors

## Languages

* TypeScript63.2%
* MDX29.9%
* Python6.2%
* Other0.7%
