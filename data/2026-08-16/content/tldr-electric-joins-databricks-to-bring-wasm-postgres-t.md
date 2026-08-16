---
title: Electric joins Databricks to bring WASM Postgres to AI agent sandboxes | Databricks Blog
url: https://www.databricks.com/blog/electric-joins-databricks-bring-wasm-postgres-ai-agent-sandboxes
site_name: tldr
content_file: tldr-electric-joins-databricks-to-bring-wasm-postgres-t
fetched_at: '2026-08-16T19:20:08.731844'
original_url: https://www.databricks.com/blog/electric-joins-databricks-bring-wasm-postgres-ai-agent-sandboxes
date: '2026-08-16'
published_date: Tue, 08/11/2026 - 07:00
description: Electric is joining Databricks to extend Databricks’ Postgres capabilities from the lakehouse to the edge, allowing for an abundance of lightweight open-source databases that can all be synced back to Lakebase Postgres for centralization and control on cheap, durable object storage.
tags:
- tldr
---

Skip to main content
Summary
* Electric is joining Databricks to bring WASM Postgres to AI agent sandboxes.
* Electric has pioneered data primitives purpose-built for agents, including PGlite and a real-time sync engine to keep data synchronized between distributed agents and a centralized Lakebase.
* Extending Databricks’ Postgres capabilities from the lakehouse to the edge allows for an abundance of lightweight open-source databases that can all be synced back to Lakebase Postgres for centralization and control on cheap, durable object storage.

Today, we’re excited to welcome Electric to Databricks. The world is building a new era of agentic applications which require distributed state and real-time data synchronization between teams of agents working in sandboxes. Electric is leading the way in pioneering data primitives purpose-built for agents: PGlite gives every agent its own lightweight Postgres right where it runs, providing ultra-low latency access to local context, and Electric’s real-time sync engine synchronizes distributed state back to a central Lakebase, enabling teams of agents to collaborate without losing track of shared context. That vision now continues at Databricks as we bring WASM Postgres to AI agent sandboxes, extending Databricks’ Postgres capabilities from the lakehouse to the edge.

Agents don’t behave like traditional applicationsDevelopers are moving from building traditional apps to building agentic applications, and the assumptions underlying traditional infrastructure are shifting with them. A traditional application has a known shape: its queries are written in advance, its data access patterns are predictable, and it runs in a place its architects chose. One managed Postgres database serves it well.

The agents in agentic applications add a second surface. Alongside the durable, governed state every application needs, an agent generates a fast-moving context set. Agents differ in three ways that matter for a database:

* They decide what data they need at runtime, deciding their next move and updating their context several times a second. That inner loop wants data in the same process; the results it produces belong in a durable store.
* They run wherever the work is, often in sandboxed environments, where databases are only reachable via a network connection to the cloud.
* They work in groups, requiring fast local context and a shared, current view of what others have done to avoid duplicating work, acting on stale state, or arriving at conflicting conclusions.

Introducing ElectricThe Electric team built data primitives for the era of agentic applications.

They created PGlite to push Postgres to the edge, creating a WASM Postgres database small enough to run inside the application or agent itself - in an agent sandbox, browser tab, or user’s device - rather than on a separate server. PGlite has grown from 1M to 13M weekly downloads in just twelve months, enabling developers to build a new class of distributed Postgres applications and agents.

But local execution is just part of the challenge. Agents also need a shared, up-to-date view of changing information. Electric’s real-time sync engine continuously synchronizes data between distributed agents and centralized Lakebase infrastructure, enabling agents to securely share information with the definitive record in the cloud while keeping fast local context. The real-time sync architecture powers collaborative apps like Google Docs, Figma and Notion, and it turns out to be exactly what a fleet of agents needs to stay current while working in parallel.

Shared Postgres DNABoth Electric and Lakebase are built on Postgres, the open-source database technology that has become the default foundation for AI agents. In fact, PGlite was built on the foundational WASM Postgres work of Stas Kelvich, who co-founded Neon. Electric took that proof of concept and turned it into the embeddable Postgres that millions of projects run every week. Bringing these teams together reunites two halves of the same idea and strengthens Databricks’ leadership at the center of innovation for modern databases as demand for agents accelerates.

Databricks + ElectricLakebase delivers Postgres at production scale. PGlite brings WASM Postgres into the agent's own sandbox. Sync keeps the two consistent. By combining the power of Lakebase Postgres with the local execution of PGlite, agents get the lightweight databases they need to move fast and the infrastructure required to deploy at any scale.

For developers, this means:

* Building collaborative, agentic applications on a single Postgres standard.
* Running Postgres directly inside the agent sandbox, giving each agent a lightweight database it needs to move fast.
* Keeping teams of agents in sync to instantly share context and act on fresh data, while centralizing control in Lakebase Postgres on cheap, durable object storage.

We’re thrilled to have the Electric team join Databricks, and can’t wait to see what our customers build.

Check out theNeon blog, andhear directly from Electric’s foundersabout why they’re excited to join forces.

### Get the latest posts in your inbox

Subscribe to our blog and get the latest posts delivered to your inbox.

## Sign up

View all blogs