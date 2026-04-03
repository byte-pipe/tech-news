---
title: How Dropbox Built a Scalable Context Engine for Enterprise Knowledge Search - InfoQ
url: https://www.infoq.com/news/2026/02/dropbox-context-engine/
date: 2026-03-02
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-02T08:26:54.615767
---

# How Dropbox Built a Scalable Context Engine for Enterprise Knowledge Search - InfoQ

# How Dropbox Built a Scalable Context Engine for Enterprise Knowledge Search

## Overview
- Dropbox created the context engine behind **Dropbox Dash** to enable enterprise AI knowledge retrieval at scale.  
- The design emphasizes pre‑processed, permission‑aware context rather than on‑the‑fly tool usage, reducing latency, token pressure, and improving relevance.

## Architecture and Retrieval Strategy
- Content from dozens of SaaS applications is **normalized, enriched, and indexed** before queries are issued.  
- Queries combine **lexical search** with **dense vector** matching, allowing results without a cascade of runtime API calls.  
- This offline indexing incurs higher storage and complexity costs but provides predictable query performance and enables offline ranking experiments.

## Knowledge Graph Integration
- A **knowledge graph** models relationships among business entities (people, documents, meetings, etc.).  
- Instead of querying a graph database at runtime, **“knowledge bundles”** are generated and fed into the indexing pipeline.  
- Treating graph data as enrichment avoids latency spikes and query‑pattern changes observed in earlier graph‑database experiments.

## Tool Consolidation and the Model Context Protocol (MCP)
- Directly exposing many tools to language models caused **context‑window consumption** and degraded performance.  
- Dropbox consolidated retrieval behind a few **high‑level tools** that fetch context outside the prompt and delegate complex requests to specialized agents.  
- MCP designers also highlighted the need for careful management of context windows when multiple tools are used.

## Evaluation at Scale
- Since retrieval results are consumed by LLMs, traditional click‑based relevance signals are insufficient.  
- Dropbox used **LLMs as judges** to score retrieval quality, enabling prompt and ranking refinements that align better with human expectations.  
- The evaluation workflow is orchestrated with **DSPy**, a prompt‑optimization framework handling over 30 prompts across workflows and facilitating rapid model switching.

## Comparison with Other Enterprise Assistants
- The approach mirrors patterns in other assistants, e.g., **Microsoft 365 Copilot**, which also relies on a pre‑computed semantic index derived from the Microsoft Graph.  
- The common trend is treating **context as a first‑class system**, pre‑computing and continuously evaluating it rather than assembling it during inference.

## Implications for Enterprise AI
- Pre‑computing, constraining, and continuously evaluating context is becoming a foundational architecture for scalable internal search and agent capabilities in large organizations.  
- This strategy helps manage token limits, improve latency, and maintain high relevance in enterprise‑grade AI assistants.