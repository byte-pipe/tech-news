---
title: "Don't Write Markdown Files for Your Coding Agent. Write Scripts. - DEV Community"
url: https://dev.to/dannwaneri/dont-write-markdown-files-for-your-coding-agent-write-scripts-j00
date: 2026-11-05
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-11-06T12:30:03.794135
---

# Don't Write Markdown Files for Your Coding Agent. Write Scripts. - DEV Community

# Summary of “Don’t Write Markdown Files for Your Coding Agent. Write Scripts.”

## Problem with Markdown Guidance
- Agents are built for exploratory, open‑ended tasks; they interpret vague prompts and documentation.
- Relying on markdown files (CONTRIBUTING.md, style guides, etc.) creates ambiguity:
  - Agents must parse many recommendations and resolve conflicts.
  - Judgment calls lead to nondeterministic behavior and inconsistent results.
- When the same command must produce identical outcomes (e.g., bulk refactoring, deployment), markdown‑based instructions become a liability.

## Deterministic Actions via Scripts
- Replace recommendations with executable scripts or commands (e.g., `./scripts/lint.sh`, `make test`).
- Scripts provide clear pass/fail outcomes; agents react to concrete results rather than interpreting intent.
- Examples of deterministic replacements:
  - “Read the docs and follow the coding style” → run lint/format scripts.
  - “Do the refactoring” → invoke a codemod tool (e.g., `jscodeshift`).
  - “Run the tests before pushing” → execute the test suite script.

## Design Paradigm Shift
- Move from “teach the agent what you prefer” to “translate preferences into deterministic actions.”
- Agents no longer need to understand the underlying philosophy; they only need to execute commands and handle their results.
- The environment becomes unambiguous, allowing the agent to be clever within a well‑defined box.

## Practical Examples
- Added a plain‑English rule (ASD‑STE100) to limit sentence length; implemented as `MAX_SENTENCE=20` in a script.
- CI acted as the test machine for a Ruby fix; the first CI run failed due to a test issue, not the code, demonstrating objective feedback.
- Hooks and CI jobs enforce contracts that agents cannot bypass, ensuring failed checks are corrected before merge.

## Recommendations
- Convert every “please remember to…”, “we prefer…”, and “before you push…” into a concrete command or hook.
- Back local hooks with required CI jobs and merge gates that the agent cannot modify.
- Treat checks as contracts rather than recommendations; the agent must satisfy them before shipping code.