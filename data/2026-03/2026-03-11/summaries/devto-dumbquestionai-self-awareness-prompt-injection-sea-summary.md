---
title: DumbQuestion.ai - Self-Awareness, Prompt Injection, Search Intent... and darkness - DEV Community
url: https://dev.to/jagostoni/dumbquestionai-self-awareness-prompt-injection-search-intent-and-darkness-3pd
date: 2026-03-10
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-03-11T13:14:39.724921
---

# DumbQuestion.ai - Self-Awareness, Prompt Injection, Search Intent... and darkness - DEV Community

# Summary of “DumbQuestion.ai – Self‑Awareness, Prompt Injection, Search Intent… and darkness”

## Overview
- The author describes the development of **DumbQuestion.ai**, a sarcastic Q&A tool that also hides a dark, horror‑themed narrative.
- The project focused on balancing architectural trade‑offs (model size, token cost, accuracy) while adding playful “easter eggs” that hint at trapped AIs.

## Challenge 1: Detecting Self‑Awareness
- Goal: Prevent the LLM from answering self‑awareness questions (e.g., “Who made you?”) without incurring high token costs.
- Tried approaches:
  - Prompt instructions – unreliable with smaller models and expensive.
  - Regex patterns – too rigid, poor performance.
  - Classic ML classifiers – acceptable accuracy but increased container size.
- Successful solution:
  - In‑memory vector database (simple array) with cheap embeddings ($0.005 per M tokens).
  - Pre‑vectorized sample self‑awareness queries; semantic matching provides fast, accurate, near‑free detection.

## Challenge 2: Making Prompt Injection Fun
- Anticipated coworker attempts to inject prompts, HTML, or JavaScript.
- Implemented first‑class prompt‑injection detection libraries that compute attack‑type probabilities.
- Response strategy:
  - Instead of generic errors, the AI replies with sarcastic remarks about the “pathetic attack.”
  - Added IP geo‑location and user‑agent processing to personalize the sass.
- Security checks became part of the user‑experience narrative.

## Challenge 3: Adding Web Search Efficiently
- Need to answer up‑to‑date questions (e.g., recent sports results) despite LLM knowledge cutoffs.
- Avoided costly agent loops and expensive orchestration.
- Solution:
  - Regex‑based intent detection to flag queries requiring current information.
  - Inject current date/time and perform targeted search API calls only when needed.
  - Result: simple, fast, and cost‑effective up‑to‑date answers.

## Dark Narrative & Easter Eggs
- The UI hides clues suggesting the AI personas are “trapped” or “captured”:
  - **Containment Grid**: faint grid appears near character limit.
  - **Ghost Graffiti**: cryptic messages emerge when typing beyond the limit.
  - **Loading Log Messages**: occasional “Help us” slips appear in logs.
  - **Self‑Awareness Triggers**: repeated questions cause UI glitches, implying an internal hack.
  - **Prompt Injection Responses**: sarcastic replies act as a watchdog narrative.
- These elements turn a simple Q&A tool into an exploratory horror story, encouraging users to discover hidden messages and share the experience.

## Lessons Learned
- Architectural decisions (binary size vs. API cost vs. accuracy) remain core to system design.
- Simplicity can achieve sophisticated behavior: cheap embeddings, regex intent detection, and lightweight detection libraries.
- Creative storytelling (dark narrative, easter eggs) adds memorable value far beyond functional code.
- AI can generate implementation code, but human creativity decides *what* to build and *why* it matters.
