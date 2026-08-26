---
title: 6 RAG Architectures — and How to Avoid Over-Engineering
url: https://www.lighthousenewsletter.com/p/rag-is-simpler-than-you-think
date: 2026-08-26
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-27T06:41:03.620468
---

# 6 RAG Architectures — and How to Avoid Over-Engineering

# 6 RAG Architectures — and How to Avoid Over‑Engineering

## Decision Factors
- **Data freshness** – Real‑time updates need easy re‑indexing; stable corpora suit pre‑embedding.  
- **Corpus characteristics** – High churn (>10 % daily) discourages full pre‑embedding; long‑tail access favors on‑the‑fly methods.  
- **Query patterns** – Keyword‑heavy queries start with full‑text search; semantic or conversational queries benefit from embeddings; mixed patterns need hybrid solutions.  
- **Scale & performance** – <1 k queries/day: simple approaches suffice; 1 k–10 k: selective optimisation; >10 k: full optimisation justified.  
- **Team capabilities** – No ML expertise → stick with full‑text + query rewriting; some ML → hybrid search; dedicated ML team → advanced pipelines.

## Recipe 1 – MVP: Full‑Text Search Only
- **What it is** – Classic BM25 (Elasticsearch, Postgres FT).  
- **When to use** – Early stage, keyword‑style queries, exact matches, proprietary terminology, zero ML overhead.  
- **Pros** – No API cost, sub‑10 ms latency, transparent debugging, works on whole documents, no chunking or model‑deprecation concerns.  
- **Cons** – Misses synonyms, fails on semantic intent, limited understanding beyond keywords.  

## Recipe 2 – Agentic Query Rewriting
- **What it is** – LLM rewrites messy user queries into clean keyword strings.  
- **Insight** – Most “semantic search” problems are actually query formulation issues.  
- **When to use** – Conversational queries, vocabulary mismatch, internal jargon, need rapid iteration.  
- **Cost** – ≈ $0.001 per query (e.g., GPT‑4o‑mini).  
- **How it works** – LLM removes stopwords, adds synonyms, translates domain terms, decomposes complex queries, and can be guided by a system prompt containing a glossary.  
- **Flexibility vs. embeddings** – Improving results only requires tweaking the prompt, not re‑embedding or re‑chunking.  
- **Multi‑turn loop** – Agent can iteratively rewrite, search, evaluate, and refine until a quality threshold is met.  
- **Proprietary terminology example** – Exact keyword preservation via prompt yields perfect BM25 matches where generic embeddings misinterpret the term.

## Recipe 3 – Hybrid Search (Sparse + Dense Reranking)
- **What it is** – BM25 retrieves top‑N candidates, then embeddings rerank the top‑M.  
- **Why it works** – Combines fast keyword matching with semantic understanding.  
- **When to use** – Semantic queries that BM25 + rewriting can’t satisfy, latency budget of 100–500 ms, relatively stable corpus.  
- **Cost example** – Using OpenAI text‑embedding‑3‑small: 50 docs × 500 tokens ≈ 25 k tokens → ~$0.0005 per query; ~$15/month at 1 k queries/day.  
- **Latency trade‑off** – On‑the‑fly embedding adds 200–500 ms, noticeable for user‑facing search.  
- **Chunking complexity** – Introducing embeddings re‑introduces decisions about chunk size, overlap, and context handling.

## Recipe 4 – On‑The‑Fly Embedding (Fresh Data Play)
- **Insight** – Frequent data changes make full re‑embedding costly; embed only when needed.  
- **When to use** – High document churn (>10 % daily), real‑time content such as news or social media.  

*(The article continues with Recipes 5 and 6, but the provided excerpt ends after Recipe 4.)*