---
title: your agent can think. it can't remember. - DEV Community
url: https://dev.to/ghostbuild/your-agent-can-think-it-cant-remember-5e1o
site_name: devto
content_file: devto-your-agent-can-think-it-cant-remember-dev-communit
fetched_at: '2026-03-25T19:21:50.017035'
original_url: https://dev.to/ghostbuild/your-agent-can-think-it-cant-remember-5e1o
author: ghost
date: '2026-03-25'
description: 'TLDR: ghost gives your agent instant, ephemeral postgres databases. unlimited databases, unlimited... Tagged with ai, mcp, postgres, agents.'
tags: '#ai, #mcp, #postgres, #agents'
---

TLDR:ghostgives your agent instant, ephemeral postgres databases. unlimited databases, unlimited forks, 1tb storage, free. pair it with Memory Engine for memory, pg_textsearch for full-text search, TigerFS for files, and Ox for sandboxed execution. All postgres-native.

try Ghost today:curl -fsSL https://install.ghost.build | sh

your agent can reason. it can plan. it can call tools and write code and hold a conversation that feels almost human.

but ask it what it did yesterday and it doesn't know. ask it to store something for later and you’re the one figuring out where it goes. give two agents the same files and things break. tell it to run code safely and you're one bad rm -rf away from a really bad day.

agents are getting smarter everyday. we haven't spent nearly enough time giving them somewhere to be productive.

## duct tape as ai infra

if you're building agents today, your infrastructure might look something like this:

* neon or supabase for the database
* mem0 or zep for memory
* pinecone or pgvector for search
* s3 for files
* e2b for sandboxed execution

five services. it works. kind of.

until your agent's memory can't query its own database. until your sandbox can't read your agent's files. and what happens if the glue code holding everything together dissolves.

## ghost is the database your agent is missing

traditional databases are designed to be permanent, and the ritual of DB setup feels permanent. you provision one, you name it, you size compute, you choose a cloud provider, and a cloud region. you care for it, you back it up, you keep it running for years. that's fine for human workflows. it's wrong for agents.

ghostgives your agent postgres databases that are instant, ephemeral, and disposable. provision them through CLI or MCP. no UI. a thousand databases for a thousand parallel sessions, free.

the mental model is git, not RDS. spin up a database the way a developer creates a branch. do work. if the work is good, keep it. if not, throw it away. fork before a risky migration. run experiments on the fork. merge or discard. databases become part of the workflow, not the infrastructure you worry about underneath it.

ghost is MCP/CLI only. your agent discovers it the same way it discovers any other tool, through MCP, and starts provisioning databases immediately. CLI works too, if that's more your speed. and because every ghost database is just postgres, your agent already knows how to use it. every LLM has postgres in the weights. schema design, queries, indexes, debugging. no proprietary query language. no SDK to learn. just SQL.

ghost does one thing and does it well. but because it's postgres, it pairs naturally with other tools that extend what your agent can do.

## extend ghost with purpose-built tools

ghost gives your agent a database. that alone gets you pretty far. but agents need more than storage. they need memory, search, files, and safe execution. here's what plugs into ghost:

## memory engine: persistent, temporal agent memory

pairs with ghost. works with any postgres.

your agent forgets everything between sessions. you've probably already tried to solve that with a vector database or a standalone memory service.

memory enginesolves this inside postgres. when you pair it with ghost, your agent's memory and data live in the ghost space. y you can query memories with SQL. you can ask "what did this agent know about this user at 3pm on tuesday?" and get an answer, because memory engine understands time natively.

no separate vector database. no syncing between systems. no second bill. just postgres doing what postgres is good at.

the temporal part matters more than it sounds. most memory solutions treat memory like a flat store. things go in, things come out. memory engine tracks when things were true. when facts changed. when old information got superseded by new information. this is how human memory works and it's how agent memory should work too.

it's not just temporal either. memory engine lets your agent search its memory with keyword, semantic, faceted, and hierarchical search in the same query. under the hood, retrieval is powered bypg_textsearch, which combines BM25 for keyword precision with pgvector for semantic similarity. pg_textsearch also ships with every ghost database, so you get full-text search out of the box even if you're not using memory engine. no elasticsearch sidecar. no separate search cluster to sync and monitor.

## tigerfs: a filesystem backed by postgres

pairs with ghost. works with any postgres.

agents create files constantly. reports, code, datasets, images, logs. most of that output ends up in s3, unstructured and impossible to query.tigerfsgives your agent a filesystem backed by postgres, so files become first-class data. transactions on writes, concurrent access from multiple agents, and metadata you can actually query.

two agents working on the same project both need to write files. tigerfs handles that without corruption. s3 doesn't.

## search: vector, keyword, and hybrid search built into postgres

pairs with ghost. works with any postgres.

every ghost database ships withpg_textsearchandpgvectorscale. that gives you BM25 keyword search, vector semantic search, and hybrid search combining both. no elasticsearch. no pinecone. no separate system to sync.

you don't need to know how to set any of this up. ghost MCP includes skills that teach your agent how to configure search indexes, choose between keyword and semantic approaches, and wire up hybrid search with reciprocal rank fusion. tell your agent you need search on a table and it handles the rest.

this is also what powers memory engine's retrieval. when your agent searches its memories, it's using hybrid search under the hood: BM25 for keyword precision, pgvector for semantic similarity, combined and ranked. all inside postgres.

## ox: sandboxed execution with full context

pairs with ghost. works with any postgres.

agents need to run code.oxgives them a sandboxed execution environment that's connected to their data but quarantined from their main branch. when paired with ghost, an ox sandbox can query the agent's database and read its tigerfs files directly. no API hops. no extra auth.

this is the difference between a sandbox and a workspace. your agent doesn't just execute code in isolation. it executes code in the context of everything it knows.

## how people are building with ghost

ghost was in private preview for the past two months. here are some of the things beta testers built.

the code review agent

the agent picks up a PR. it forks its ghost database to get a clean copy of the current state. it spins up an ox sandbox, runs the test suite against the fork, and checks for regressions. it searches memory engine for past reviews on the same files. what broke last time. what patterns the team prefers. what feedback the author got previously. it writes its review, stores the results in tigerfs, and updates its memory with what it learned.

the research agent

the agent spins up a ghost database to store everything it finds. company profiles, product comparisons, pricing data. it writes raw reports to tigerfs as markdown files. it checks memory engine: have we researched this company before? what did we find last time? what changed? when it needs to crunch numbers, it forks the database into an ox sandbox so it can run analysis without touching the original data. when it's done, it stores what it learned with full temporal context. next quarter, the agent knows what the landscape looked like this quarter.

the multi-agent team

three agents, one project. one writes code. one writes docs. one runs tests. all three read and write files through tigerfs without stepping on each other. all three check memory engine so they don't duplicate work. all three get their own ox sandbox that can still query the shared ghost database. they share a substrate without sharing a failure mode.

the data exploration agent

a user asks "what would our metrics look like if we changed the pricing model?" the agent forks the ghost database. rewrites the pricing logic on the fork. reruns three months of transactions against the new model in an ox sandbox. doesn't like the result. forks again with a different model. runs it again. the user gets three scenarios in ten minutes. all run against real data. none of them touching production.

## all on postgres

we are proud members of the postgres fan club. here's why we build on it:

postgres is battle-tested. it's been in production for 30+ years. it handles transactions, concurrent access, replication, and failure recovery. when your agent's infrastructure needs to be reliable, you want it built on something boring.

one substrate means zero glue code. when your database, memory, search, and files all run on postgres, they share the same transaction model, the same auth, the same query language. the integration layer doesn't exist because it doesn't need to.

we've been building on postgres for years. before ghost, we built timescaledb, one of the most widely-used postgres extensions for time-series data. memory engine's temporal capabilities come directly from that work. we're applying a decade of postgres engineering to a new problem.

## get started

ghost is in early access. install it with the comment below. runghost mcp installdirectly in claude code, and let your agents cook.

curl 
-fsSL
 https://install.ghost.build | sh

Enter fullscreen mode

Exit fullscreen mode

the full toolkit:

* ghost→ instant, ephemeral postgres databases for agents
* memory engine→ persistent, temporal agent memory
* pg_textsearch→ BM25 + keyword search for postgres
* tigerfs→ postgres-backed file storage
* ox→ sandboxed execution, connected to your data

everything is postgres. everything is MCP-native. each one works on its own. they're better together.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (18 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse