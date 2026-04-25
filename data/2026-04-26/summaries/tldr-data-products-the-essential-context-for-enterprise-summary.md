---
title: Data Products: The Essential Context for Enterprise AI
url: https://moderndata101.substack.com/p/data-products-the-essential-context
date: 2026-04-26
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-26T06:01:16.652386
---

# Data Products: The Essential Context for Enterprise AI

# Data Products: The Essential Context for Enterprise AI

## The Moment
- In 2024‑2025 “AI agents for your data” were heavily marketed, promising natural‑language queries without analysts or dashboards.  
- Most agents failed in production; MIT’s 2025 report cited brittle workflows, missing contextual learning, and misalignment with operations.  
- The industry initially blamed model limitations, but model improvements did not solve the problem.  
- OpenAI’s internal data agent (Jan 2026) succeeded by layering six sources of context for every query: schema metadata & lineage, historical query patterns, curated expert descriptions, code‑derived definitions, institutional knowledge from Slack/docs, and persistent memory of past corrections.  
- a16z (Mar 2026) and other analysts reinforced that the core issue is a lack of context, calling for a dedicated architectural layer rather than an after‑thought.

## The Industry’s Realisation
- Traditional enterprise data strategy focused on centralising data in warehouses/lakehouses, assuming self‑service via SQL and dashboards.  
- Human analysts bring tacit context (canonical tables, business definitions, fiscal calendars, source trust) that AI agents lack, leading to confident but wrong answers.  
- The failure of AI‑for‑data agents highlighted that context, not model capability, is the bottleneck.  
- The consensus in early 2026 is that context must become a durable, versioned, discoverable layer—managed infrastructure rather than ad‑hoc prompts or tribal knowledge.

## Shape of the Answer: Data Products
- A Data Product is a managed unit of data treated as a product, with:
  - an owner  
  - a contract defining guarantees and limits  
  - a named consumer  
  - a lifecycle (versioning, deprecation, sunset)  
  - discoverability in a catalog  
  - a stable addressable interface  
  - attached semantics, lineage, and quality signals  
- Historically promoted for human usability (data mesh, Zhamak Dehghani, 2019); now positioned as the primary consumption unit for AI agents.  
- In AI terms, a Data Product packages all necessary context as a first‑class asset, eliminating the need for agents to reconstruct schema, semantics, ownership, freshness, lineage, and quality on the fly.

## Six Layers of Context Aligned with Data Products
1. **Schema metadata and lineage** – included in the product’s specification.  
2. **Historical query patterns** – captured automatically through usage telemetry of the governed interface.  
3. **Curated expert descriptions** – authored by the product owner as part of its contract.  
4. **Code‑derived definitions** – the transformation logic that creates the product, already versioned.  
5. **Institutional knowledge** – encoded in the product’s semantic layer, replacing tribal knowledge.  
6. **Memory of past corrections** – maintained via governance and revision history of the product.  

By treating these layers as integral to Data Products, enterprises can provide AI agents with the rich, accurate context needed for reliable answers, turning the “context problem” into a solvable architectural component.