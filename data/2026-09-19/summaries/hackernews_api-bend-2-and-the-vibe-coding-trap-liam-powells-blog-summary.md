---
title: "Bend 2 and the Vibe-Coding Trap | Liam Powell's Blog"
url: https://blog.liampwll.com/posts/bend_vibe_coding/
date: 2026-09-18
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-19T06:01:09.508156
---

# Bend 2 and the Vibe-Coding Trap | Liam Powell's Blog

# Bend 2 and the Vibe‑Coding Trap

## Main argument
- The author critiques Bend 2 as an example of “vibe‑coding”, where developers rely on LLMs to build large systems without first understanding existing research.
- Bend 2 claims to let humans write “laws” while an AI generates implementations and proofs, but the required specifications and proofs are excessively verbose (58 lines of laws, 442 lines of proof).

## Problems identified
- **Vibe‑coding pitfall**: creates substantial solutions before recognizing better, established approaches.
- The author of Bend 2 appears unaware of the formal verification field, which already provides mature tools and methodologies.
- By not consulting existing work, Bend 2 ends up reinventing a language and compiler that are far more cumbersome than necessary.

## Demonstration with SPARK
- The author reproduces Bend’s demo in SPARK, an open‑source language for formal verification, using an LLM only to translate the example.
- The SPARK version includes all necessary specifications and proofs, yet GNATprove verifies the program with only 12 checks—no massive proof script.
- This shows that the same guarantees can be achieved with far less effort when leveraging established verification tools.

## Broader implications
- Vibe‑coding enables rapid prototyping of broken or outdated designs because the LLM does not suggest existing solutions or point out that the problem has already been solved.
- Relying solely on LLM‑generated code can hide the need for research, leading to duplicated work and missed opportunities to use state‑of‑the‑art techniques.

## Takeaway
- Before embarking on a large LLM‑driven project, developers should survey the relevant field to avoid reinventing the wheel and to benefit from existing, more efficient solutions.