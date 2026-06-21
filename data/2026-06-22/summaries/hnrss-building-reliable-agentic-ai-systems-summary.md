---
title: Building Reliable Agentic AI Systems
url: https://martinfowler.com/articles/reliable-llm-bayer.html
date: 2026-06-21
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-22T00:53:43.726514
---

# Building Reliable Agentic AI Systems

# Building Reliable Agentic AI Systems – Summary

## Overview
- Presents PRINCE, a cloud‑hosted platform built by Bayer AG with Thoughtworks to improve preclinical drug‑development data access.  
- Combines Agentic Retrieval‑Augmented Generation (RAG) and Text‑to‑SQL to integrate decades of safety study reports.  
- Evolves from keyword search to an intelligent research assistant that answers complex queries and drafts regulatory documents.  
- Emphasizes **context engineering** (shaping and routing information between specialized agents) and **harness engineering** (orchestration, recovery, observability) to ensure control and reliability.  
- Prioritizes trust through transparency, explainability, and human‑in‑the‑loop review.

## The Challenge: Navigating the Preclinical Data Maze
- Preclinical data are split between structured study metadata and large volumes of unstructured PDF reports.  
- Key pain points:
  - **Data silos** across many systems hinder holistic view of a compound or study.  
  - **Limited search**: Boolean keyword tools cannot handle nuanced terminology, yielding irrelevant or incomplete results.  
  - **Manual analysis** is time‑consuming, pulling researchers away from scientific work.

## The Solution: PRINCE – An Evolutionary Platform
- **Phase 1 – Search**: Unified gateway that consolidates structured metadata from thousands of study reports, offering advanced filtering.  
- **Phase 2 – Ask**: Adds AI‑powered RAG to enable natural‑language queries over unstructured PDFs, extracting “gold‑standard” information directly from the documents.  
- **Phase 3 – Assist** (implied): Agentic workflow that orchestrates specialized agents (Researcher, Reflection, Writer) to validate data, synthesize answers, and format regulatory drafts.

## System Architecture – Engineering a Reliable Agentic RAG System
- **Specialized agents**:
  - *Clarify User Intent*: interprets natural‑language questions.  
  - *Think & Plan*: reflects on the query, selects tools, and creates a processing plan.  
  - *Researcher Agent*: performs retrieval (vector search, Text‑to‑SQL) and extracts relevant passages.  
  - *Reflection Agent*: validates completeness, checks for hallucinations, and ensures sufficiency of evidence.  
  - *Writer Agent*: synthesizes validated content into a coherent answer or document, applying required formatting.  
- **Context engineering**: controls what context each agent receives and how it is passed along the pipeline.  
- **Harness engineering**: provides orchestration, state persistence, retries, fallbacks, validation loops, observability, and human review layers.

## Building Trust in a Production LLM System
- **Transparency & Explainability**: each answer is accompanied by source citations and a confidence score; UI surfaces retrieval traces for user inspection.  
- **Evaluation**: continuous benchmarking against curated QA sets and domain‑expert review.  
- **Monitoring**: real‑time metrics on latency, error rates, hallucination detection, and usage patterns; alerts trigger automated remediation.

## Engineering for Resilience – Error Handling and Recovery
- Retry policies with exponential back‑off for transient model or service failures.  
- Fallback to deterministic keyword search when RAG confidence falls below a threshold.  
- Automated logging of prompt/response pairs for post‑mortem analysis.  
- Human‑in‑the‑loop escalation for ambiguous or high‑risk queries.

## Enhancing Data Quality – Named Entity Recognition and Annotation
- Custom NER models trained on pharmaceutical terminology to tag compounds, assays, and safety endpoints.  
- Annotation pipeline enriches PDF text with structured tags, improving retrieval relevance and downstream validation.

## The Journey Continues – Iterative Development
- Agile cycles incorporate user feedback, expand domain coverage, and refine agent prompts.  
- Ongoing research explores multi‑turn conversations, adaptive prompting, and tighter integration with regulatory submission systems.

## Conclusion
- PRINCE demonstrates that a carefully engineered agentic RAG system can transform preclinical data access, delivering faster, more accurate insights while maintaining governance and compliance.  
- The case study highlights the importance of context and harness engineering to achieve reliability, trust, and production readiness in agentic AI applications.