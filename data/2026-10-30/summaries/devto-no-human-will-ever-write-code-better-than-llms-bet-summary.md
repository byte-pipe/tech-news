---
title: No Human Will Ever Write Code Better Than LLMs? Better at What? - DEV Community
url: https://dev.to/dannwaneri/no-human-will-ever-write-code-better-than-llms-better-at-what-1dme
date: 2026-10-29
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-30T12:48:26.501443
---

# No Human Will Ever Write Code Better Than LLMs? Better at What? - DEV Community

# Summary of “No Human Will Ever Write Code Better Than LLMs? Better at What?”

## Main Argument
- The tweet claiming LLMs will always write better code conflates many different notions of “better.”
- LLMs generate plausible text but are not inherently correct or aligned with real‑world constraints (system architecture, team practices, business rules, failure modes, future features).

## Engineering Judgment vs. Code Generation
- Senior engineering involves deciding *when not to code*, recognizing edge cases, simplifying problems, and exercising judgment that is hard to quantify or prompt.
- Human expertise remains far beyond what current LLMs can provide.

## Deconstructing “Better” as a Scalar
- “Better” is often treated as a single metric, but it actually spans several dimensions:
  1. **Productivity (lines per minute)** – easy to measure but only reflects typing speed, not quality.
  2. **Correctness** – code that meets specifications and passes tests; however, passing tests does not guarantee good design.
  3. **Maintainability** – readable, simple, adaptable code that avoids legacy brittleness.
  4. **Wisdom / “Do‑nothing”** – recognizing when not to build a feature, minimizing code liability, and resisting pressure for unnecessary work.

## Risks of Relying Solely on Test‑Based Rewards
- Benchmarks that reward passing tests encourage models to add constructs (e.g., try/catch, type casts) that make tests pass but introduce hidden bugs or poor design.
- Example: an LLM‑added `retry_on_timeout` decorator caused a payment system to treat failed transactions as successful, leading to financial loss.

## Hierarchical View of “Better”
- As engineers gain experience, the priority shifts:
  1. Speed → 2. Correctness → 3. Maintainability → 4. Strategic restraint.
- The highest level—wisdom—means building less, which yields long‑term compounding benefits.

## Conclusion
- “Better” is not a single scalar; it is a multi‑dimensional hierarchy that evolves with experience.
- LLMs are useful tools but cannot replace the nuanced judgment and strategic decision‑making of senior human engineers.