---
title: "AI's Architect Problem: Why We're Building on Borrowed Land :: Notes from the Rabbit Hole"
url: https://magnus919.com/2026/05/ais-architect-problem-why-were-building-on-borrowed-land/
date: 2026-05-09
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-09T07:55:04.455591
---

# AI's Architect Problem: Why We're Building on Borrowed Land :: Notes from the Rabbit Hole

# AI’s Architect Problem: Why We’re Building on Borrowed Land

## Overview
- The talk by Kanupriya Yakhmi at an AgileRTP meetup highlighted how companies often lock‑in to a single AI provider without planning for change.
- Her background (AI/ML PhD, product manager, former Waymo systems architect, Executive MBA) gives credibility to the failure patterns she described.

## The Three Essential Questions
- **Can the business logic run on a different model without a rewrite?**  
  - If core behavior depends on a specific model’s quirks, migration becomes a full rebuild, threatening small‑margin businesses.
- **Can the training data, embeddings, and evaluation sets migrate?**  
  - Swapping providers often breaks RAG pipelines and evaluation harnesses, creating expensive technical debt.
- **Can the deployment move across providers without changing the architecture?**  
  - Without this flexibility the product is essentially a managed service controlled by the provider’s roadmap.

## Portability Spectrum
- **Stage 1 – Direct SDK calls:** Fast to build but extremely costly to unwind; analogous to deep coupling in iOS apps.
- **Stage 2 – Internal interface wrapper:** Same models underneath, but swapping becomes a configuration change; rarely implemented.
- **Stage 3 – Portable builder:** Open‑weight alternatives evaluated, data pipelines owned, only evaluation harness needs adjustment when moving.
- **Stage 4 – Full infrastructure portability:** Hardware‑agnostic serving, provider diversity, independent movement of model, data, and compute; treated as a competitive advantage.

## Hidden Cost of Speed
- Vendor lock‑in can be a deliberate trade‑off for rapid market entry; many startups start on cloud AI and later migrate in‑house when costs rise.
- The trap is treating a proof‑of‑concept decision as permanent, leading to unknown switching costs and a reduced serviceable obtainable market (SOM).
- Engineering morale suffers when teams inherit undocumented dependency decisions and must fix breakages caused by upstream model changes.

## Agile for External Dependencies
- “Agile 2.0” proposes surfacing external vendor risks in standard ceremonies:  
  - Stand‑ups ask “what changed upstream that might break us?”  
  - Sprint planning accounts for model deprecation timelines.  
  - Retrospectives evaluate vendor‑induced technical debt.
- Different teams should run tailored Agile processes reflecting their specific external dependencies rather than a monolithic approach.

## Why AI Can’t Replace People
- Current AI systems are pattern matchers; they cannot model future failures or understand undocumented assumptions (e.g., hidden rate limits, response formats).
- Human‑in‑the‑loop governance is essential, not as a checkbox but as a mechanism to catch contextual reliability issues.
- Hiring domain specialists to test AI products and paying external users to find flaws helps surface failures that AI alone cannot anticipate.