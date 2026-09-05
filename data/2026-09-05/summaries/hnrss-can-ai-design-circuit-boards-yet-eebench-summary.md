---
title: Can AI design circuit boards yet? — EEBench
url: https://eebench.org/blog/can-ai-design-circuit-boards-yet/
date: 2026-09-04
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-05T10:36:28.917642
---

# Can AI design circuit boards yet? — EEBench

# Summary of “Can AI design circuit boards yet? — EEBench”

## Background
- OpenAI showcased GPT‑6 Astra designing a KiCad circuit board, sparking interest in AI‑assisted electronics design.
- The core question is how to evaluate the quality of AI‑generated hardware, not just its ability to draw schematics.

## The models know a surprising amount about electronics
- Current language models have absorbed textbooks, datasheets, application notes, and code, giving them substantial domain knowledge.
- Directly manipulating a graphical CAD tool is inefficient for agents because most context is visual (coordinates, menus).
- EEBench uses **atopile**, a declarative code format for circuits, allowing agents to edit components, connections, and constraints programmatically, run simulations, and inspect failures without leaving the project.

## Real‑world messiness captured in the benchmark
- Example task: a residential energy meter must keep a processor alive for 20 ms after a 5 V loss, staying above a 3 V brown‑out threshold.
- Simple solutions (e.g., adding a capacitor) overlook tolerances, voltage‑dependent capacitance, cost, space, and recharge speed.
- EEBench simulates power‑loss events, measures voltage over time, evaluates effective capacitance, recovery behavior, and checks component limits (package, dielectric, voltage rating, cost).
- Harder tasks involve synthesizing analog filters, solving component ratios, and verifying performance across worst‑case tolerance corners using SPICE simulations.

## Grading methodology
- The benchmark is fully deterministic: it builds the submitted design, creates a circuit graph and bill of materials, then runs a suite of SPICE simulations and design checks.
- Each requirement yields a measurement with a defined limit; technical scores are combined with cost‑efficiency relative to a reference BOM.
- Cost contributes to the score only after the circuit meets functional requirements.
- This mirrors a coding test where an agent must pass compiler tests, but here the tests are voltage and component‑behavior measurements.

## Leaderboard results (EEBench V1)
- Claude Opus 5 leads with 61.6 % across 13 tasks.
- Grok 4.6 follows at 57.1 %; Claude Fable 5.1 at 56.4 %; Claude Fable 5 at 54.3 %; Claude Opus 4.8 Max at 51.4 %.
- xAI highlighted Grok 4.6’s 60.0 % score in its model card, emphasizing “engineering acceleration.”
- Anthropic models consistently perform well; Grok’s improvement is attributed to domain‑specific engineering data and RL training.
- OpenAI models lag: GPT‑5.5 at 42.3 %, GPT‑5.6 Sol at 39.4 %; no GPT‑6 Astra result yet.

## Training environment
- The simulation harness doubles as a reinforcement‑learning (RL) reward signal for post‑training.
- Failed runs provide detailed feedback (e.g., which voltage missed limits, which corner failed, cost inefficiencies), enabling richer training signals than a simple plausibility check.
- EEBench serves as a public view of this work; collaborations with frontier labs aim to further improve model capabilities in electronics.

## Outlook
- EEBench V1 focuses on analog and digital design verification but does not yet assess layout, manufacturing, or product bring‑up.
- Future versions plan to incorporate those stages, moving closer to a complete end‑to‑end hardware design benchmark.