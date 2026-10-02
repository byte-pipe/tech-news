---
title: Supabase is acquiring Turso
url: https://supabase.com/blog/supabase-is-acquiring-turso
site_name: hackernews_api
content_file: hackernews_api-supabase-is-acquiring-turso
fetched_at: '2026-10-02T22:50:47.619517'
original_url: https://supabase.com/blog/supabase-is-acquiring-turso
author: cvburgess
date: '2026-10-02'
description: Supabase is acquiring Turso to build the database infrastructure for agentic AI
tags:
- hackernews
- trending
---

Blog
 / 
company

# Supabase is acquiring Turso

2 Oct 2026

·

3 minute read

Paul Copplestone
CEO and Co-Founder

AI is enabling builders to create an immense amount of software. Today, agents are spinning up millions of databases to power the prototypes, explorations, dashboards, and apps they're building. This new pattern, at this massive scale, requires an evolution in database infrastructure. Turso is joining Supabase to build this evolution.

For existing users, nothing changes. Supabase will continue building around Postgres, while Turso will continue its work on SQLite. And together, we’re creating something new that will bring the Supabase experience to every agent.

## Databases for agents#

Supabase is already launching over one million databases per week. As agents build more software, we believe database demand will outpace the world’s current capacity to support them. So we need infrastructure that can scale to meet this growth and is suited to how we build with agents.

Agents should be able to create a database as easily as creating a file, with just as little concern about cost. For smaller workloads, that shouldn’t require provisioning a dedicated machine every time. Databases should be cheap to create, available on demand, and have a clear path to production when needed.

SQLite is well suited to these small, on-demand workloads. Postgres is what you want as your application scales. We want builders to have the same developer experience from prototyping to production.

## Turso#

Turso has built an architecture for exactly this pattern. They rebuilt SQLite in Rust and created a cloud platform where a single server can manage millions of databases, loading them when needed and suspending them when they’re not.

This architecture makes it possible to provision a database for each agent on demand, whether on Turso Cloud or in customers’ own clouds, as Superhuman, Sauna.ai, CTO.new, and Mastra do.

We share a vision for how infrastructure needs to evolve to support agentic AI. Turso will continue operating, with a clear path into the broader Supabase ecosystem as workloads grow.

## Open source#

Turso and Supabase have a lot in common: a commitment to open source, a focus on developer experience, and an appetite to tackle hard infrastructure problems.

We’re excited to welcome Glauber Costa and Pekka Enberg to Supabase with the rest of the Turso team. Glauber will lead this agentic infrastructure effort.

Our mission is to store the world’s data, and agents are going to create a lot more of it. This gets us closer to that goal.

Copy as Markdown
Ask ChatGPT
Ask Claude

Previous post

#### Build anything: Supabase from code, and an MCP server for your app

2 October 2026

Next post

#### Supabase is now available in Gemini Enterprise

9 September 2026

ai
open-source
database

On this page

Databases for agents
Turso
Open source
Copy as Markdown
Ask ChatGPT
Ask Claude

## Build in a weekend,scale to millions

Start your project
Request a demo