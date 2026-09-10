---
title: Introducing Neki — PlanetScale
url: https://planetscale.com/blog/introducing-neki
date: 2026-09-11
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-11T08:30:38.259910
---

# Introducing Neki — PlanetScale

# Introducing Neki – Summary

## What is Neki?
- Sharded PostgreSQL service built by PlanetScale, keeping a real Postgres instance on each shard.  
- Applications connect via a Neki router using the standard Postgres wire protocol, so existing drivers, ORMs, and connection strings work unchanged.  
- Each shard is a full Postgres cluster (1 primary, ≥2 replicas) spread across three availability zones.  
- Shard key and table distribution are defined in a JSON “data topology”.  
- Supports online workflows for schema changes, version upgrades, failovers, imports, and resharding.  
- Includes PlanetScale features such as Insights, schema recommendations, branching, and MCP.  
- Can start as an unsharded single‑primary cluster and later reshard when needed.

## Why Neki?
- Addresses common pain points of rapidly growing Postgres databases: large tables, long backups, connection limits, maintenance windows, transaction wraparound, etc.  
- Scaling by moving to larger instances eventually hits hardware limits and does not solve linear growth issues.  
- Existing alternatives force trade‑offs: application‑level sharding adds routing code; “Postgres‑compatible” distributed databases hide the shard key, limit extensions, and add latency/complexity.  
- Neki’s guiding principle: stay true to Postgres without workarounds or compromises.

## How does Neki work?
- **Neki routers**: Accept client connections, parse queries, plan distribution across shards, execute, and merge results. They scale vertically and horizontally.  
- **Sharding and shard groups**: Real Postgres shards organized into groups; each group can have its own instance size, replica count, storage, parameters, and extensions.  
- **Connection pooling**: Sidecar processes run alongside each Postgres instance, allowing the router to size pools precisely for each node.  
- **Control plane**: Monitors node health, handles planned switchovers, unplanned failovers, and coordinates online workflows (resharding, schema changes, upgrades).  
- **Data topology**: JSON configuration mapping logical tables to physical shards, defining shard indexes (column and hash) and shard groups; routers cache this topology for planning.

## What you get beyond sharding
- All typical maintenance tasks (schema changes, version upgrades, failovers, imports, resharding) run as built‑in online workflows without downtime.  
- Same PlanetScale value‑added features: Insights, schema recommendations, branching, MCP, etc.  
- Even in an unsharded mode you benefit from improved connection pooling, zero‑downtime DDL, seamless upgrades, and health monitoring.

## What is a platform preview?
- Early access program; Neki is not yet recommended for production workloads.  
- The product is still evolving and may introduce breaking changes.  
- Users are encouraged to provide feedback via support tickets or Discord.

## Try Neki today
- Sign in to PlanetScale, opt into the platform preview, and create a Neki cluster.  
- Consult the Neki documentation for architecture details, sharding guidance, and operational instructions.  
- For large existing Postgres clusters, request a private demo to evaluate fit, review schema/query patterns, and receive sharding recommendations.