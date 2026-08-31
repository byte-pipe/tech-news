---
title: Agent memory as a file format
url: https://calpaterson.com/memoryfields.html
date: 2026-08-31
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-01T09:51:37.649684
---

# Agent memory as a file format

# Agent memory as a file format

## Motivation  
- Benchmarks start agents with an empty context, but real agents should begin with relevant memories.  
- Existing memory systems are inadequate, leading to wasted context and poor scalability.

## Issues with current memory approaches  
- **Platform‑locked systems**: Tie agents to a specific harness, focusing on conversation history rather than useful world knowledge.  
- **Over‑engineered stacks**: Require components such as pgvector, Neo4j, and auxiliary LLMs, making deployment hard and confusing the model.  
- **High‑modernist graph models**: Strip context into isolated facts or logical propositions, producing lists of “distilled facts” that lack meaning for the agent.  
- Common flaw: treat memory as a multi‑stage pipeline instead of raw data.

## Memoryfield: a portable memory file format  
```
my‑memories.memoryfield.zip
├── carbon‑fibre‑woks.md
├── finnish‑bureaucracy‑tips.md
├── … many more md files …
├── wec‑2026‑season‑notes.md
└── nomic‑embed‑text‑v1.5.sqlite3
```  
- Consists of Markdown pages (optional YAML front‑matter) and an optional SQLite vector index for semantic search.  
- Agents interact directly with files, eliminating complex APIs.

## Design decision 1 – Prose instead of chunks or “facts”  
- Memories are written by the agent in natural Markdown prose; no need for chunking, summarising, or extra enrichment.  
- Each page is limited to ~8 KB (≈2 000 tokens), roughly the length of a medium magazine article; larger details are split into additional pages.  
- Example front‑matter:  
  ```yaml
  title: Carbon Fibre Woks
  created: '2026-03-01T09:00:00Z'
  updated: '2026-08-22T14:30:00Z'
  uuid: 6aa615f0-486f-48a7-a210-ba4f5ff18c8b
  summary: Thermal properties of carbon fibre cookware
  ```

## Design decision 2 – Semantic jump, not graph walking  
- Prior “Karpathy wikis” rely on hyperlinked Markdown files; agents must make a series of tool calls to traverse links, which is slow and error‑prone.  
- Semantic search using the SQLite vector index allows a direct jump to relevant pages:  
  1. Search vector index (one tool call).  
  2. Retrieve matching pages in parallel (second tool call).  
- This reduces latency, avoids irrelevant noise, and eliminates the need for SEO‑style link titles.

## Design decision 3 – More model, less mechanism  
- High‑mechanism systems force agents through extensive, often mismatched APIs, consuming context space and limiting flexibility.  
- Memoryfields are low‑mechanism: a simple file format that agents can manipulate with any tools they prefer (e.g., Perl regex, inline CSV queries via SQLite).  
- Agents retain full freedom to design custom access patterns without loading large OpenAPI specifications.

## Overall benefits  
- **Simplicity**: One zip file containing readable Markdown and an optional vector index.  
- **Speed**: At most two tool calls to locate and load relevant memories.  
- **Scalability**: Works with any model size; no external services required.  
- **Transparency**: Humans can inspect and edit memories directly.  
- **Flexibility**: Agents can apply any programming or query technique they find useful.