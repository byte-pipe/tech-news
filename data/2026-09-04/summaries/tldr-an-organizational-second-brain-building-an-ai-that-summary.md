---
title: An Organizational Second Brain: Building an AI That Learns From Experts - Engineering at Meta
url: https://engineering.fb.com/2026/09/02/ml-applications/organizational-second-brain-ai-learns-from-experts/
date: 2026-09-04
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-04T07:27:12.759277
---

# An Organizational Second Brain: Building an AI That Learns From Experts - Engineering at Meta

# An Organizational Second Brain: Building an AI That Learns From Experts

## Overview
- Developed an AI agent that serves as a “secondary expert” for a specific domain, making deep specialist knowledge easily accessible across the organization.  
- Novelty lies in two integrated layers:  
  1. **Structured, auditable knowledge architecture** that separates what the agent knows from how it reasons.  
  2. **Self‑improvement loop** that compiles expert feedback into verified, regression‑tested updates without retraining the underlying model.  
- The combination turns one‑off expert corrections into permanent, compounding institutional memory and can generalize to any domain governed by retrievable text.  
- Saves Meta subject‑matter experts substantial time, allowing them to focus on high‑impact, novel work.

## Problem Statement
- Specialist knowledge often remains tacit, residing in experts’ heads rather than durable documentation.  
- In compliance and other high‑stakes domains, routine questions consume expert time, lead to inconsistent assessments, and create organizational risk.  
- Organizations need systems that capture expert reasoning, make it shareable, and preserve it for future use.

## Architecture at a Glance
- Built on off‑the‑shelf LLMs, augmented with four inter‑dependent layers:  
  1. **Knowledge system** – a file‑based, structured repository of curated statements, constraints, and routing rules.  
  2. **Reasoning layer** – explicit procedures that mirror how domain experts think, enabling tractable failure attribution.  
  3. **Evaluation framework** – gates every change to ensure regression safety.  
  4. **Improvement loop** – feeds expert feedback back into both knowledge and reasoning without model retraining.  
- Removing any layer degrades the overall performance.

## Building the Organizational “Second Brain”
- Large organizations generate thousands of documents; the real knowledge is the implicit reasoning behind them.  
- An offline process extracts and distills this reasoning into structured knowledge files, making it machine‑readable and auditable.  
- Knowledge files are organized into a strict taxonomy (200+ files) with YAML front‑matter declaring dependencies (`depends_on`) and consumers (`referenced_by`).  
- Types of files:  
  - **Position files** – authoritative stances, constraints, and routing implications.  
  - **Taxonomy & vocabulary files** – single source of truth glossaries.  
  - **Routing indexes** – deterministic mapping of input characteristics to relevant positions/procedures.  
  - **Gateway files** – threshold tests that prevent the agent from applying specialized knowledge in inappropriate contexts.

## Organizing Knowledge by Density and Usage Frequency
- **High‑density, frequently referenced knowledge** → stored in the wiki (positions, decision frameworks, boundary examples).  
  - Consulted on nearly every inference step, versioned, and validated.  
- **Sparse, situationally relevant knowledge** → accessed via retrieval‑augmented generation (RAG) using semantic or lexical search.  
  - Includes detailed reference material, product specs, historical decisions, niche external sources.  
- This split ensures the core reasoning stays grounded in refined, current organizational knowledge while still allowing on‑demand access to supporting evidence.

## Benefits and Impact
- Provides a durable, auditable repository of expert reasoning that can be updated incrementally.  
- Enables deterministic, traceable retrieval, reducing inconsistency and risk in high‑stakes domains.  
- Allows experts to spend less time on routine queries and more on novel, ambiguous problems where their judgment is most valuable.  
- The pattern is designed to be domain‑agnostic, applicable to finance, security, engineering, and other enterprise areas requiring deep specialist knowledge.