---
title: "Don't classify. Hallucinate!"
url: https://softwaredoug.com/blog/2026/08/10/hypothetical-classifications
date: 2026-08-10
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-15T04:05:26.515760
---

# Don't classify. Hallucinate!

# Summary of “Don’t classify. Hallucinate!”

## Overview
- Traditional LLM classification forces the model to output only legal taxonomy values, often using large models and extensive schema transmission.
- A cheaper alternative leverages “hallucination”: prompting a small LLM to generate plausible but fictitious classifications, then mapping them to the real taxonomy via vector similarity.

## Method
1. **Prompt a small LLM** to invent a classification for a query (e.g., “brown coffee table”).  
   - Example prompt includes several real‑world classification formats for guidance.  
2. **Obtain the generated string** (may be non‑existent in the actual taxonomy).  
3. **Pre‑compute embeddings** (e.g., MiniLM) for all genuine classifications in the target taxonomy.  
4. **Embed the hallucinated classification** and compute dot‑product similarity with the real embeddings.  
5. **Select the nearest real classification** as the final output.

## Advantages
- **Cost‑effective**: Uses inexpensive, “dumb” models instead of large LLMs.  
- **Scalable**: No need to transmit the full list of legal values with each request.  
- **Fast**: In‑memory embedding lookup provides quick nearest‑neighbor matching.  

## Example Workflow
- Query: “brown coffee table”  
- Hallucinated output: “Furniture / Living Room / Tables / Coffee”  
- Vector similarity maps it to the real taxonomy entry:  
  “Furniture / Living Room Furniture / Coffee Tables & End Tables / Coffee Tables”

## Resources
- Notebook demonstrating the embedding approach.  
- Utility code for building the in‑memory embedding index.  

## Upcoming Event
- **Vectors Week** – series on vector retrieval, hybrid search, and building vector databases (hosted by Doug Turnbull).