---
title: Introducing GPT-5.4 | OpenAI
url: https://openai.com/index/introducing-gpt-5-4/
date: 2026-03-06
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-07T06:01:53.707867
---

# Introducing GPT-5.4 | OpenAI

# Introducing GPT‑5.4

## Overview
- Released on March 5 2026 for ChatGPT (as **GPT‑5.4 Thinking**), the API, and Codex.
- Two variants: **GPT‑5.4 Thinking** (standard) and **GPT‑5.4 Pro** (maximum performance on complex tasks).
- Combines advances in reasoning, coding, and agentic workflows into a single frontier model.
- Supports up to 1 M tokens of context, enabling long‑horizon planning and verification.
- First general‑purpose model with native, state‑of‑the‑art computer‑use capabilities.

## Professional Knowledge Work
- Improves spreadsheet, presentation, and document creation/editing.
- On the GDPval benchmark (44 occupations), achieves 83.0 % win/tie rate vs. 70.9 % for GPT‑5.2.
- Spreadsheet modeling benchmark: mean score 87.3 % (vs. 68.4 % for GPT‑5.2).
- Presentation evaluation: human raters prefer GPT‑5.4 outputs 68.0 % of the time.
- Reduces factual errors: individual claims 33 % less likely false; full responses 18 % less likely to contain any error compared to GPT‑5.2.
- New ChatGPT for Excel add‑in and updated spreadsheet/presentation skills in Codex and the API.

## Computer Use & Vision
- Native ability to operate computers: write code for libraries like Playwright, issue mouse/keyboard commands from screenshots.
- Steerable via developer messages; safety behavior can be customized with confirmation policies.
- Benchmarks:
  - OSWorld‑Verified (desktop navigation): 75.0 % success (human benchmark 72.4 %).
  - WebArena‑Verified (browser use): 67.3 % success (vs. 65.4 % for GPT‑5.2).
  - Online‑Mind2Web (screenshot‑only browser): 92.8 % success (vs. 70.9 % for ChatGPT Atlas).
  - MMMU‑Pro (visual reasoning without tools): 81.2 % success (vs. 79.5 % for GPT‑5.2).
- Introduces “tool yield” metric to better reflect latency benefits of parallel tool calls.

## Efficiency & Token Usage
- Most token‑efficient reasoning model to date; solves problems with significantly fewer tokens than GPT‑5.2.
- Faster response times and lower cost for developers and enterprise users.

## Availability & Integration
- Accessible in ChatGPT (Thinking and Pro modes), the API, and Codex.
- Enterprise customers encouraged to use the new ChatGPT for Excel add‑in.
- Updated skill libraries for spreadsheets and presentations are available for API and Codex users.

## Reliability & Hallucination Reduction
- Targeted improvements to lower hallucinations and factual errors.
- Claims are 33 % less likely to be false; full responses 18 % less likely to contain any error versus GPT‑5.2.

## Notable Endorsements
- Brendan Foody, CEO of Mercor: “GPT‑5.4 is the best model we’ve ever tried… top of the leaderboard on our APEX‑Agents benchmark, delivering long‑horizon deliverables faster and at lower cost.”
- Niko Grupen, Head of Applied Research at Harvey: “GPT‑5.4 sets a new bar for document‑heavy legal work… scores 91 % on BigLaw Bench, excelling in complex transactional analysis and accuracy.”
