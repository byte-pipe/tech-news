---
title: "Richard Sutton on X: \"A new and possibly controversial perspective: In this video, I explain the sense in which generative AI trained by supervised le..."
url: https://twitter.com/RichardSSutton/status/2061216087744946656
date: 2026-06-10
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-11T06:02:06.482795
---

# Richard Sutton on X: "A new and possibly controversial perspective: In this video, I explain the sense in which generative AI trained by supervised le...

# Richard Sutton – AI Creativity and Discovery (Speech Summary)

## Introduction
- Sutton presents a “controversial perspective” on generative AI trained by supervised learning.
- He explains why such AI cannot make truly novel scientific or mathematical discoveries.

## Main Argument: Novelty vs. Goodness
- Generative AI (LLMs, image/video models, world‑model learners) can produce outputs that are **novel** or **good**, but not both simultaneously.
- For factual tasks (answers, summaries) novelty is undesirable; we prefer “good” outputs that faithfully reflect source material.
- For fiction/entertainment novelty is acceptable, yet we cannot reliably measure how much the AI deviates from its training data because the internet is vast.

## Limitation of Supervised Generative AI
- Supervised learning creates models that **mimic** training examples.
- The stochastic nature of generation can yield novelty, but there is no built‑in **evaluation** of that novelty at runtime.
- Without evaluation and selective retention, the system cannot achieve **true creativity** or **discovery**.

## Contrast with Creative AI Systems
- Systems that combine variation, evaluation, and selective retention can produce outputs that are both novel and good:
  - AlphaGo (move 37), AlphaZero (original chess style)
  - GT‑Sophy (simulated race‑car control)
  - AlphaFold, AlphaProof, Claude‑Code (advances in science, math, programming)
  - RL‑Lyft (ride‑hailing optimization)
- These systems incorporate mechanisms beyond pure supervised learning, often using **reinforcement learning**, planning, or combinatorial search.

## The Concept of “Discovery”
- Defined as a three‑step process:
  1. **Variation** – generate many possibilities.
  2. **Evaluation** – assess the quality or usefulness of each.
  3. **Selective Retention** – keep the best-performing candidates.
- Mirrors natural selection, the scientific method, instrumental learning, operant conditioning, and reinforcement learning.
- Not present in standard back‑propagation or gradient‑descent training of generative models.

## Role of Evaluation
- Human judgment can provide evaluation (e.g., selecting the best AI‑generated image).
- Autonomous AI systems need built‑in evaluation mechanisms to achieve discovery without human intervention.

## Conclusion
- Generative AI based solely on supervised learning is a powerful mimic but fundamentally limited for scientific and mathematical discovery.
- To attain true creativity, AI must incorporate the “Discovery” loop (variation, evaluation, selective retention), typically via reinforcement learning or similar approaches.