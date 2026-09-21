---
title: Bun Rewrites 535K Lines of Zig into Rust in Four Months, Eliminates Numerous Memory Leaks - InfoQ
url: https://www.infoq.com/news/2026/09/bun-AI-rewrite-zig-rust-4-months
date: 2026-09-22
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-22T08:47:06.714407
---

# Bun Rewrites 535K Lines of Zig into Rust in Four Months, Eliminates Numerous Memory Leaks - InfoQ

# Bun Rewrites 535K Lines of Zig into Rust in Four Months, Eliminates Numerous Memory Leaks

## Overview
- Bun, the JavaScript/TypeScript runtime, bundler, and package manager, was rewritten from Zig to Rust.
- The rewrite aimed to remove memory‑safety bugs (use‑after‑free, double‑free, missed frees) by leveraging Rust’s borrow checker.
- The project, driven by Bun creator Jarred Sumner, was completed in four months instead of the originally estimated one year.

## Motivation
- A large share of existing bugs were memory‑related and would be compile‑time errors in safe Rust.
- Traditional rewrites are risky because they freeze bug fixes and feature work for the duration of the rewrite.
- Bun’s test suite is written in TypeScript, allowing the runtime language to change without breaking tests.

## AI‑Assisted Porting Process
- Sumner experimented with Anthropic’s Claude Fable 5 model to rewrite the codebase.
- An automated pipeline transpiled Zig to Rust, using a pre‑release Claude model orchestrated across ~50 dynamic workflows.
- Key artifacts:
  - `PORTING.md` – mapping of Zig patterns/types to Rust equivalents.  
  - `LIFETIMES.tsv` – lifetimes for every struct field.
- Workflow:
  1. **Implementer agent** translates Zig files to Rust using the mapping files.  
  2. Two **adversarial reviewer agents** examine only file diffs to find bugs or behavioral differences.  
  3. A **fixer agent** addresses issues reported by reviewers.
- Parallelization:
  - 4 workspace shards, each with 16 agents (64 Claude instances total).  
  - Peak output: ~1,300 lines of code per minute, up to 695 commits per hour.
- Token cost: ~165 k USD for 5.9 B input tokens, 690 M output tokens, and 72 B cached reads.

## Testing, Validation, and Security
- Over 1 million test assertions were run; the Rust build passed the full suite after extensive debugging.
- 19 subtle semantic regressions were discovered, caused by syntactic similarities between Zig and Rust.
- Security review:
  - 11 rounds of Claude Code Security reviews fixed multiple security issues.  
  - Continuous fuzzing of all parsers produced 15 pull requests.

## Outcomes
- Bun v1.4.0 (released August 2026) fixed 128 long‑standing bugs from v1.3.14.
- Memory leaks were dramatically reduced: 2,000 consecutive `Bun.build()` calls stabilized at 609 MB (vs. >6.7 GB in Zig).  
- HTTP throughput improved by 2 %–5 %.
- The rewrite demonstrated that large‑scale LLM‑generated codebases can be produced quickly while maintaining functional correctness.

## Community Reactions
- Zig creator Andrew Kelley criticized the rewrite, arguing that bug elimination relies on dedicated engineering effort rather than language choice alone.
- User “vitaminCPP” noted that the project serves as a canary for the maintainability of massive LLM‑generated codebases over time.

## Acquisition
- Bun was acquired by Anthropic in December 2025, providing the resources and models used for the rewrite.

## Author
- Article written by Bruno Couriol.