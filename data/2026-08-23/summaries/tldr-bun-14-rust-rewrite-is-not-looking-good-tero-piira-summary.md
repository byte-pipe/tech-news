---
title: Bun 1.4 Rust rewrite is not looking good • Tero Piirainen
url: https://tipiirai.com/writing/bun-rust-rewrite-worries
date: 2026-08-23
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-23T06:01:16.411503
---

# Bun 1.4 Rust rewrite is not looking good • Tero Piirainen

# Bun 1.4 Rust rewrite is not looking good

## Personal background
- I have been a supporter of Bun since its 2022 launch, switching my development from Node to Bun.
- Used Bun for theNue framework and the new project Hertta.

## Missed release promises
- “In the next version of Bun” used to signal a concrete, near‑term release; after the Rust rewrite it became a vague placeholder.
- Timeline of announced dates (June 24 → July 7 → July 14 → … → August 17) repeatedly slipped, with no stable release for over three months—the longest gap in Bun’s history.

## Community reaction
- Users express frustration with repeated “tomorrow” promises:
  - “I’m editing blog post… if I say a date you won’t believe me but let’s say tomorrow.”
  - “I am switching to Go now… you are just stringing your users along again and again.”
- The tone shows loss of trust and growing impatience.

## GitHub activity and AI involvement
- The 1.4 rewrite is heavily AI‑driven:
  - 15.8 k commits from `robobun`
  - 1.6 k commits from `autofix-ci[bot]`
  - 790 commits from Jarred
- Most PRs now originate from prompting Claude, rather than human contributors.
- Over 5 k open pull requests, far exceeding typical limits (GitHub suggests < 1 000 per branch).

## Concerns about code quality
- Andrew Kelley (Zig creator) criticized the codebase for “hacks on top of hacks” and excessive assertion abuse.
- The rewrite introduced many `unsafe` blocks, undermining the memory‑safety rationale for moving to Rust.
- The project feels more like an Anthropic showcase than a stable product.

## Zig vs. Rust debate
- Bun’s early identity relied on Zig’s performance, fast compile times, and low‑friction memory control.
- The switch to Rust appears motivated by a desire to demonstrate Claude’s capabilities, using Zig’s memory issues as a pretext.
- The author suggests that AI‑assisted work could have improved Zig code instead of a full language migration.

## Outlook
- No v1.4 release has materialized despite repeated “tomorrow” claims.
- The author is considering moving to Go due to the ongoing delays and uncertainty.