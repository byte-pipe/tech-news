---
title: On the Navier–Stokes Millennium Prize Problem | OpenAI
url: https://openai.com/index/navier-stokes-solution/
date: 2026-09-09
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-09T08:37:47.015159
---

# On the Navier–Stokes Millennium Prize Problem | OpenAI

# On the Navier–Stokes Millennium Prize Problem – Summary

## The problem
- Navier–Stokes equations describe fluid motion using Newton’s second law, treating the fluid as a continuous medium.  
- The open question (one of the Clay Millennium Problems) asks whether a smooth, three‑dimensional incompressible fluid with constant density can develop a singularity—unbounded velocity in finite time—despite viscosity.  
- Jean Leray (1934) proved existence of weak solutions, but smoothness for all time remained unresolved.

## The result
- OpenAI’s internal AI system produced an analytical proof and a Lean formalization showing that an initially smooth fluid at rest, subjected to a smooth external force, can develop a finite‑time singularity while its total energy stays finite.  
- The construction is a vortex that spirals inward and stretches axially, shrinking in radius while accelerating, satisfying the precise balance of acceleration, pressure, momentum transfer, and viscosity.  
- This resolves statements “C” and “D” of the official Millennium Prize formulation, confirming that smooth solutions need not exist for all time.

## How the proof was found
- Training of a new internal model began on 28 August 2026; performance on mathematical benchmarks quickly surpassed previous versions.  
- A coordinated multi‑agent system, powered by the model, was deployed on 1 September. Agents had internet‑read and code‑execution tools, communicated in groups, and were kept under strict monitoring safeguards.  
- Approximately 10 000 agents worked on the Navier–Stokes problem, after an earlier Euler‑regularity disproof was obtained by a separate 100‑agent team.  
- Agents explored multiple problem variants (A–D) and were cross‑pollinated using Codex to merge insights.  
- The Navier–Stokes resolution emerged on 5 September, about 88 hours after launch; Lean verification added another 17 hours.  
- Overall communication: 4.9 million messages and ~300 billion output tokens across all problems; Navier–Stokes alone required 2.7 million messages and ~130 billion tokens.

## Concurrent work
- A rumor about a solution from Levent Alpöge (Anthropic) and Tristan Buckmaster (NYU) prompted OpenAI to reach out after completing their own proof.  
- The external team had resolved the forced Euler problem, not Navier–Stokes; OpenAI offered a joint announcement but the results remained distinct.