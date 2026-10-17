---
title: How the Claude Code team does code review / claude.dev Blog
url: https://claude.dev/blog/solving-code-review-at-anthropic/
date: 2026-10-17
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-17T13:53:25.875151
---

# How the Claude Code team does code review / claude.dev Blog

# How the Claude Code team does code review

## Overview
- Claude Code generates ~90 % of its own code, producing a high volume of changes.  
- The team shifted from manual line‑by‑line reviews to a layered, mostly automated process.  
- From June to September 2026 the number of merged PRs more than doubled while revert rates dropped >40 %.  

## Rethinking the purpose of code review
- Traditional review served two goals: catch bugs before shipping and spread shared knowledge.  
- The focus of this article is on the first goal—preventing defects.  
- “Did a human read the code?” is replaced by “Which check, automated or human, is best suited to catch a potential issue?”  
- Review now runs continuously, similar to spell‑check, with most routine mistakes fixed by Claude before a human is involved.  

## Human time and attention as a scarce resource
- Goal: limit each PR to at most one human (often the author) without increasing reverts or incidents.  
- Human effort is measured by:  
  - Median and 95th‑percentile human approvals per PR  
  - Number of human comments  
  - Waiting time for a person’s response  
- Revert and incident rates act as guardrails; any rise indicates the automation is merely shifting work, not reducing it.  

## Life of a change (review pipeline)
1. **Before the PR** – Claude runs tests, builds, linters and a secondary agent reviews the diff in a fresh context.  
2. **On every PR** – Required CI (lint, type checks, cross‑platform tests, build) blocks merges on failures.  
3. **Claude code review** – Parallel agents hunt for bugs, vote on findings, and rank survivors by severity.  
4. **Security review** – Separate pass; open findings block the merge.  
5. **Risk‑based approval** – A classifier assigns the change to a tier: no human, one human, or two humans; some paths always require a person.  
6. **Merging** – Change enters a merge queue; checks run again on the latest main branch.  
7. **After merge** – Feature is behind a flag, rolled out internally first, then gradually to users. Monitoring, quick flag removal, and automated rollback handle any breakage.  

## Layer‑by‑layer checks
- Six automated layers plus a fast rollback:  
  1. Verification before PR  
  2. Required CI  
  3. AI (Claude) review  
  4. Security review  
  5. Human approval (risk‑based)  
  6. Merge queue & feature flags  
- Each layer catches a subset of problems; the rollback layer catches any that slip through.  

## Verification before a PR exists
- Most review happens prior to PR creation: Claude is given a concrete artifact (test run, build output, screenshot) and asked to show the result.  
- Sub‑agents then review the diff with fresh context.  
- Internal “skills” run automatically: bug hunting, diff simplification, end‑to‑end behavior checks, UI design compliance.  
- Repeated flagging of the same issue leads to fixing the source (skill, lint rule, or instructional file).  

## Instructional files that guide Claude
- **CLAUDE.md** – Describes project stack, conventions, goals, and non‑goals; loaded by every review.  
- **REVIEW.md** – Authored by code owners; lists failure signatures, nit‑picking limits, paths to skip, and required evidence format.  

## Outcomes and metrics
- By moving most checks to machines and only involving humans for high‑risk or contextual questions, the team achieved:  
  - >2× increase in merged PRs (June‑September 2026)  
  - >40 % reduction in revert share  
  - Stable or reduced incident rates, confirming genuine time savings.  

## Takeaway
- Automated, continuous review combined with risk‑based human approval allows Claude Code to scale code production while preserving developer attention for the problems only humans can solve.