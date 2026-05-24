---
title: Contexts graphs, AI memory, and enterprise knowledge: Are decision traces enough? | InfoWorld
url: https://www.infoworld.com/article/4156909/context-graphs-and-decision-traces-to-the-rescue.html
date: 2026-05-24
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-24T18:01:10.204466
---

# Contexts graphs, AI memory, and enterprise knowledge: Are decision traces enough? | InfoWorld

# Contexts graphs, AI memory, and enterprise knowledge: Are decision traces enough?

## Overview
- A December 2025 Foundation Capital paper introduced “context graphs,” a type of knowledge graph designed to store AI “decision traces.”
- The author sees decision traces as valuable but not a complete solution; they must be part of a broader AI architecture.

## Decision traces versus full reasoning
- Decision traces correspond to **episodic memory** – they record how specific decisions were made.
- Effective AI also needs:
  - **Semantic memory** – factual data, schemas, and organizational truths.
  - **Procedural memory** – skills, processes, and operating principles.
- Omitting any layer can cause AI to hallucinate or produce answers that do not match the organization’s reality.

## Why graphs matter in enterprise AI
- Traditional systems (ERP, CRM, data warehouses) remain the canonical sources for transactions and raw data.
- Context graphs add:
  - Evidence of what mattered in a decision.
  - Relationships between entities, policies, exceptions, and approvals.
  - An operational memory that complements, rather than replaces, existing systems.
- Graph structures capture relational queries (who approved, what policy applied, how systems are linked) that vector‑based text search cannot.

## Integration with existing graph ecosystems
- Context graphs act as a “graph of graphs,” sitting on top of domain‑specific graphs (e.g., accounting, fraud detection) and directing agents to the appropriate source.
- They serve as a central “hive mind” for AI agents, enabling unified query routing across heterogeneous data stores.

## Role of GraphRAG
- Retrieval‑augmented generation applied to graphs (GraphRAG) improves the ability of AI to retrieve structured knowledge from context graphs.
- Open challenges include:
  - Representing and managing procedural knowledge and skills.
  - Automating skill creation and evaluation while ensuring performance gains.

## Practical advice for enterprise AI teams
- Experiment with context graphs and decision traces, but avoid locking in a single architecture.
- Stay agile: the AI landscape evolves rapidly, and new critical ideas may emerge soon.
- Treat context graphs as an augmenting layer that enriches existing enterprise data sources and supports explainable, autonomous decision‑making.

## Author note
- Dominik Tomicevic, CEO of Memgraph, contributed this opinion piece. His background includes founding a high‑performance graph database company and recognition as a leading technology CEO.