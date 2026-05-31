---
title: I Made My AI Models Argue, Then Let Hermes Be the Judge - DEV Community
url: https://dev.to/arqamwd/i-made-my-ai-models-argue-then-let-hermes-be-the-judge-5e6c
date: 2026-05-30
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-06-01T04:19:33.350722
---

# I Made My AI Models Argue, Then Let Hermes Be the Judge - DEV Community

# Hermes Agent Challenge Submission – Build With Hermes Agent

## Overview
- The author created **Council**, a system that turns any judgment‑call question into a mini‑jury of three AI models.  
- Each juror (two OpenRouter models and one local Ollama model) gives its reasoning; if they disagree, a second deliberation round lets them see each other’s arguments and possibly change their vote.  
- Hermes then synthesizes a single verdict, a confidence score (high for agreement, lower for 2‑1 splits), and a “why they disagreed” panel.  
- All verdicts and weight adjustments are stored in Hermes’ memory, enabling the system to re‑weight jurors for future questions without external state.

## What Was Built
- **Problem addressed:** Single‑model overconfidence that can lead to costly mistakes (e.g., a wrong database migration).  
- **Solution:** A jury of three models that debate before a final decision, eliminating hidden overconfidence.  
- **Key features:**  
  - Parallel fan‑out to three Hermes sub‑agents.  
  - Optional second deliberation round for dissenting jurors.  
  - Confidence dial that rises when dissent is resolved.  
  - Human‑in‑the‑loop trust adjustments that persist client‑side.  
  - Zero monetary cost when using the offline mock mode.

## Demo & Repository
- **Repo:** https://github.com/ArqamWaheed/council  
- **Live demo:** https://council-jet-kappa.vercel.app/  
- Quick local run (offline mock, no API key):  
  ```bash
  git clone https://github.com/ArqamWaheed/council
  cd council
  ./setup_hermes.sh
  python server.py
  ```

## Architecture (Visual Summary)
1. **Core loop:** One question → three independent Hermes sub‑agents → fourth Hermes “foreman” synthesizes verdict.  
2. **Model‑agnosticism:** Jurors can be swapped by changing `--provider`/`--model` flags; no code changes required.  
3. **UX:** Confidence displayed prominently; dissent panel collapsed by default, expandable when confidence is low.  
4. **Deliberation:** After round 1, dissenting jurors receive a second Hermes run with peers’ arguments; a “⇄ changed” badge marks those that switched.  
5. **Learning loop:** Hermes proposes trust‑weight updates; user approval persists these rules for future calls.

## Code Highlights
- `hermes_run.py`: Wrapper that invokes Hermes (`hermes -z`) for any juror or judge call.  
- `run_council.py`: Orchestrates parallel juror calls, the deliberation loop, and deterministic judging.  
- `skills/council/SKILL.md`: Stores juror‑weighting logic that Hermes can edit.  
- `server.py`: API endpoints for question handling, reflection, and learning.  
- `index.html`: Front‑end UI showing verdict, confidence, and dissent details.

## How Hermes Was Used
- Leveraged Hermes’ **model‑agnostic core** to run heterogeneous models (two hosted via OpenRouter, one local via Ollama) through the same `hermes -z` interface.  
- Each juror runs as an isolated Hermes process, ensuring independent reasoning.  
- The second‑round deliberation is a genuine Hermes inference step, not just UI logic; mock jurors provide deterministic behavior for offline demos.  
- The system respects Hermes’ 64 KB context floor, requiring custom provider configuration for the local model.

## Takeaways
- **Model‑agnosticism** is a powerful property for building multi‑model ensembles without code duplication.  
- A **deliberative jury** can convert hidden disagreement into transparent confidence metrics, improving decision safety.  
- Storing verdicts and trust adjustments in Hermes’ memory enables a pure‑function judging step that evolves over time.