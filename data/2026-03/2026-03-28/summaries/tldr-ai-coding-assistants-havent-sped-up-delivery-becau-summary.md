---
title: AI Coding Assistants Haven’t Sped up Delivery Because Coding Was Never the Bottleneck - InfoQ
url: https://www.infoq.com/news/2026/03/agoda-ai-code-bottleneck/
date: 2026-03-28
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-28T01:02:02.670007
---

# AI Coding Assistants Haven’t Sped up Delivery Because Coding Was Never the Bottleneck - InfoQ

# AI Coding Assistants Haven’t Sped up Delivery Because Coding Was Never the Bottleneck

## Main Observation
- Agoda’s analysis shows AI coding tools boost individual developer output but only modestly increase project‑level delivery speed.
- The real bottleneck has moved upstream to specification and verification, which still require human judgment.

## Supporting Data
- Faros AI telemetry (10 000+ developers, 1 255 teams) reports:
  - Teams with high AI adoption complete 21 % more tasks and merge 98 % more pull requests.
  - Pull‑request review time rises by 91 %, indicating pressure shifting from coding to review.

## Implications for Team Structure
- Traditional small, focused teams were built on the assumption that coding was the primary value‑creating activity and communication was overhead.
- With specification and architectural alignment becoming the highest‑value work, communication itself is now the core activity.
- Smaller teams win because they achieve shared understanding faster; five engineers can align on intent and corner cases more effectively than fifteen.

## Taxonomy of Engineer‑AI Interaction
- **White‑box**: Human reads and reviews every line of AI‑generated code – does not scale.
- **Black‑box (vibe coding)**: Ship AI output with minimal verification – fast but brittle for production.
- **Grey‑box (preferred)**: Engineer focuses on two accountable points:
  1. Writing precise specifications that guide the AI.
  2. Verifying results against evidence rather than line‑by‑line inspection.
- Accountability remains with the human who guides the AI and approves the merge.

## Shift in Engineering Deliverables
- High‑fidelity specifications with testable acceptance criteria, explicit corner cases, and captured architectural decisions become the primary deliverable.
- Generated code is treated as a downstream, regenerable artifact, echoing the Spec‑Driven Development approach where specifications are the executable source of truth.

## Conclusion
- Human authority is moving upward in the abstraction stack: from writing code to defining and governing intent.
- Effective adoption of AI coding assistants requires re‑architecting workflows, team structures, and review practices to focus on specification quality and evidence‑based verification.
