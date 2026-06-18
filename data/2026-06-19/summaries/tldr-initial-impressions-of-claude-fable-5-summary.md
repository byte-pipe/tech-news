---
title: Initial impressions of Claude Fable 5
url: https://simonwillison.net/2026/Jun/9/claude-fable-5/
date: 2026-06-19
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-06-19T01:19:26.171043
---

# Initial impressions of Claude Fable 5

# Initial impressions of Claude Fable 5

## Overview
- Spent ~5.5 hours testing Claude Fable 5; feels like a “beast” – slow, expensive, but capable.
- Main challenge is finding tasks it cannot perform, as with many frontier models.

## Key characteristics
- Claims to match Claude Mythos 5 performance while adding stricter safety guardrails.
- Guardrails trigger often; API provides signals and can fall back to another model automatically.
- Claude Mythos 5 offers the same capabilities without safety classifiers.
- Context window: 1 million tokens; max output: 128 000 tokens; knowledge cut‑off: January 2026.
- Pricing: $10 per million input tokens, $50 per million output tokens (twice the cost of Claude Opus 4.x series); no extra charge for longer context.
- Upgrade guide is notably shorter than that for Opus 4.8.

## Knowledge comparison (Simon Willison projects)
- **Opus 4.8** gave a cautious, partial list with approximate dates.
- **Fable 5** produced a longer, more detailed list, including recent projects such as:
  - files‑to‑prompt (Apr 2024)
  - datasette‑extract (2024)
  - LLM CLI/tool (2023‑2024)
  - symbex (Jun 2023)
  - ttokandstrip‑tags (May 2023)
  - and many earlier tools back to 2003‑2005.
- Demonstrates that Fable 5 stores more factual knowledge, likely due to larger parameter count.

## Model size implications
- Greater stored knowledge suggests a larger model, possibly the biggest released by any vendor to date.
- More knowledge can aid coding tasks that rely on awareness of modern libraries and patterns.

## Using Fable in Claude.ai
- Available across Claude.ai surfaces: chat interface, Claude Code (web & CLI), and Claude Cowork.
- Accessible on subscription plans until 22 June 2026; thereafter billed separately.
- Claude.ai provides a full container environment for code execution, including package installation and GitHub cloning.

## Practical experiment: upgrading micropython‑wasm
- Prompted Fable 5 to replace MicroPython with full CPython in a WebAssembly sandbox.
- Fable identified Brett Cannon’s cpython‑wasi‑builds but could not download them directly.
- After uploading the zip files, Fable assembled a working proof‑of‑concept within minutes.
- Highlighted technical details such as zip‑based stdlib handling and the need for proper _PYTHONHOME configuration.

## Pricing and availability summary
- $10 / M input tokens, $50 / M output tokens.
- No additional cost for the 1 M token context window.
- Model appears on higher‑tier subscription plans with extra billing after the trial period.

## Conclusions
- Claude Fable 5 is slower and more costly than Opus 4.x but offers substantially richer built‑in knowledge.
- Strict safety guardrails are a double‑edged sword: they increase reliability for safe use but may interrupt certain workflows.
- The model’s large context and extensive knowledge make it a strong candidate for complex coding and data‑exploration tasks, especially when paired with Claude.ai’s container execution environment.