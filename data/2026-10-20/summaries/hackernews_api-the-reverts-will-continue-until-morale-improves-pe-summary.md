---
title: The reverts will continue until morale improves | Peter Eisentraut
url: http://peter.eisentraut.org/blog/2026/10/09/the-reverts-will-continue-until-morale-improves
date: 2026-10-20
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-20T12:22:19.670649
---

# The reverts will continue until morale improves | Peter Eisentraut

# The reverts will continue until morale improves | Peter Eisentraut

## Overview
- During the PostgreSQL 19 beta an unusually high number of features (8‑10 significant ones) were reverted, many late in the cycle.
- The author, a developer/committer of some of those features, shares his perspective on why this happened and what may change.

## Reasons for the reverts
- **Code quality** – Some features were not implemented well enough; the team will learn and improve.
- **Over‑ambitious schedule** – A strong development roll led to tackling several hard features that could not be finished in time.
- **Architectural defects & edge cases** – Many reverted features had deep design problems and numerous minor issues that LLM‑assisted code review exposed quickly; fixing dozens of small defects consumes a lot of time.
- **Not “vibe coding”** – The affected code was written before that style became common, so it is not the primary cause.
- **Vulnpocalypse impact** – Senior developers were occupied with security fixes from April to August, reducing the usual beta‑time review and testing; this caused many problems to surface late.
- **System complexity** – Features interact with many other components (domains, composites, partitions, views, security‑definer functions, etc.), making exhaustive manual testing impossible; LLM‑assisted fuzzing finds issues rapidly, highlighting the need for more robust internal interfaces.
- **Experimental feature handling** – The community has discussed committing features with an “experimental” status to mature them before full inclusion; this approach is not yet established and contributed to misunderstandings.

## Outlook and next steps
- The author thanks the community for support and expects many reverted features to return soon.
- PostgreSQL 19 will still be a strong release, featuring REPACK CONCURRENTLY, logical replication of sequences, and planner hinting via pg_plan_advice, among others.
- Predicting future feature counts is difficult; while PostgreSQL 20 was once thought to contain only bug fixes, several 80 %‑complete features are now queued for it.
- Ongoing work aims to improve development processes, incorporate experimental status handling, and strengthen code quality to reduce future large‑scale reverts.