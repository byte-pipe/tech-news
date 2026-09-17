---
title: Android Developers Blog: Android Bench 2.0: Pushing the frontier with challenging long-horizon tasks
url: https://android-developers.googleblog.com/2026/09/android-bench-2-long-horizon-tasks.html
date: 2026-09-18
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-18T05:28:21.937967
---

# Android Developers Blog: Android Bench 2.0: Pushing the frontier with challenging long-horizon tasks

# Android Bench 2.0: Pushing the frontier with challenging long‑horizon tasks

## Overview
- Android Bench was created to measure how large language models (LLMs) help developers with real Android work.  
- The benchmark has been updated to align with the Harbor framework and now includes **long‑horizon tasks (LHTs)** that can take days or weeks.  
- Agentic evaluation is added, testing agents provided by model vendors alongside the models themselves.

## From incremental fixes to long‑horizon tasks
- The original benchmark focused on small, incremental changes such as bug fixes or minor feature additions.  
- Android Bench 2.0 raises the bar with tasks like dependency upgrades, new feature development, building apps from scratch, and porting cross‑platform apps to Android.

## Complex tasks require nuanced evaluation
- Binary pass/fail scoring is insufficient for multi‑day engineering work.  
- A continuous scoring system now measures:
  - Functional completeness  
  - Visual fidelity  
  - Regression avoidance  
  - Penalties for deviating from instructions or structural constraints  
- Leaderboard cards display pass rate, completion rate, and average cost per model and per task.  
- Highest LHT pass rate is ~28 % (versus ~91 % for the original tasks).

## Insights from long‑horizon tasks
- Models are better at **writing new code** than refactoring existing code.  
- Strong performance on deterministic transformations (e.g., Java→Kotlin, Retrofit→Ktor, adding ViewModel layers) across large codebases.  
- Weaknesses appear when tasks need runtime validation, involve breaking framework changes, or rely on unreleased libraries.  
- Porting cross‑platform apps remains difficult; no model reaches 100 % pass, top models achieve ~80 % completion.

## Introducing agent evaluations
- Agents from the same provider as the model are now evaluated on LHTs (e.g., GPT 5.6 Sol on Codex, Gemini 3.8 Flash on Google Antigravity).  
- Early results show that harness design (prompt caching, compact tool windows) can reduce token usage and improve outcomes.  
- Future work will test mixed model‑agent combinations to identify optimal pairings.

## New models added
- Added to the leaderboard: Gemini 3.8 Flash, Gemini 3.7 Flash, OpenAI’s GPT‑6, Anthropic’s Fable 5.1, Kimi K3, Qwen 3.8 Max.  
- OpenAI’s GPT‑6 Astra leads with a 28 % pass rate on LHTs.

## Looking ahead
- Android Bench 2.0 provides a robust platform for measuring AI assistance in Android development through LHTs, multimodal evaluation, agents, and continuous scoring.  
- The goal is to guide AI research toward more capable, dependable coding partners and give developers clearer transparency on AI options.  
- Feedback is welcomed via GitHub, X, and LinkedIn; the updated leaderboard and methodology are publicly available.