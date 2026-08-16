---
title: Models Are Getting Dumber on Purpose - Walter van der Giessen
url: https://w4g1.dev/blog/models-are-getting-dumber-on-purpose
date: 2026-08-17
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-17T08:45:29.586623
---

# Models Are Getting Dumber on Purpose - Walter van der Giessen

# Models Are Getting Dumber on Purpose

## Overview
- Reasoning benchmarks improve dramatically while per‑token compute and active parameter counts drop.
- Math and code scores suggest models are becoming smarter per parameter, but factual recall degrades sharply.
- The shift is intentional: labs trade stored world knowledge for reasoning ability.

## Why Parameters Are Being Repurposed
- Factual knowledge occupies roughly two bits per parameter; storing every detail requires massive models.
- Reasoning procedures compress well: breaking problems, tracking state, self‑checking, and backtracking can be distilled into smaller models.
- Training on synthetic, procedure‑focused data (e.g., Phi‑4) yields strong math performance but poor trivia, indicating a design choice rather than a limitation.

## Facts Rot, Procedures Don’t
- Front‑line training runs are costly and take months; facts baked into weights become outdated quickly (API changes, price shifts, personnel moves).
- Procedural knowledge (algebra, problem‑decomposition) remains stable over time.
- A model heavy on procedures ages less, making the training cutoff less critical.

## The Harness Carries the Knowledge
- When the model lacks facts, external systems supply them: retrieval from knowledge bases, tool calls, web search, local document stores.
- Agents can query these sources at runtime, grounding answers in up‑to‑date information rather than stale weights.
- This separates reasoning (model) from factual grounding (harness).

## Toward a Frontier Model on a Consumer GPU
- Active‑parameter counts for reasoning are now within consumer‑GPU limits (e.g., DeepSeek V4‑Flash with ~13 B active parameters).
- The large expert layers that store facts (~271 B parameters) can be omitted, shrinking the model to 20–40 B parameters at 4‑bit quantization, fitting a 24 GB GPU.
- Such a model would admit “I don’t know” for pure factual queries and rely on the harness to look up answers.

## Hallucination Reduction
- Facts stored in weights are untraceable; wrong answers cannot be corrected without costly retraining.
- When facts are retrieved from external sources, wrong answers are linked to a document that can be edited, providing a clear fix path.
- Retrieval does not eliminate all errors (misreading or mis‑combining sources is possible), but it makes claims checkable and regressions manageable.
- In the long term, the model’s knowledge cutoff could become irrelevant, as up‑to‑date information is supplied at runtime.