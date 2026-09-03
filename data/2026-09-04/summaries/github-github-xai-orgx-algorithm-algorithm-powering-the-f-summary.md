---
title: GitHub - xai-org/x-algorithm: Algorithm powering the For You feed on X · GitHub
url: https://github.com/xai-org/x-algorithm
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-09-04T07:26:52.161847
---

# GitHub - xai-org/x-algorithm: Algorithm powering the For You feed on X · GitHub

# X For You Feed Algorithm

## Notable Updates
- **August 14 2026**
  - Clarified that weights modify predicted probabilities of actions (like, share, report) rather than raw counts; a report’s weight does not directly cancel out likes.
  - Added Brazil 2026 Election Filter to remove posts from accounts reported to Brazil’s Electoral Court unless the viewer follows them.
- **August 13 2026**
  - Introduced key configuration parameters, including weights for blending predicted action values.
  - Added code for visibility‑filtering and the label systems that drive it (botmaker, scarecrow, agatha, bdsm, user‑cred‑v2, media‑model‑proxy, clip, abuse‑enforcement‑service).
  - Replaced the Phoenix demo model with training code and synthetic data generation for proof‑of‑concept runs.
  - Integrated SimClusters as an additional out‑of‑network source.
  - Released an “Under the Hood” transparency tool showing aggregate label statistics for accounts and posts.

## Overview
- The For You feed is built per request from two sources:
  - **In‑Network** – recent posts from accounts the viewer follows (handled by `thunder`).
  - **Out‑of‑Network** – posts discovered via ML retrieval (`phoenix`) and similarity clusters (`simclusters`).
- Both sources are ranked together by a transformer model.
- `phoenix` reads the viewer’s recent engagement history and predicts probabilities for each possible action; these probabilities are combined into a single score using the configured weights.
- Two pipelines operate:
  - **Post Pipeline** – finds, ranks, and filters posts.
  - **Blending Pipeline** – adds non‑ranked items such as ads, “Who to Follow” recommendations, and prompts.
- Visibility filtering, implemented in `visibility-filtering`, decides whether a post can be shown at all, based on user blocks/mutes and labels attached by other systems.

## System Architecture – Request Path
1. **Query Hydration**
   - Collects the viewer’s recent action sequence, following list, blocks, mutes, muted keywords, already‑seen posts, followed topics, etc.
2. **Candidate Sources** (queried in parallel)
   - **In‑Network:** `thunder` provides recent posts from followed accounts.
   - **Out‑of‑Network:** `phoenix` retrieval model and `simclusters` similarity clusters supply posts from non‑followed accounts.
3. **Candidate Hydration**
   - Retrieves post text, media, author details, account labels, quoted posts, language, engagement counts, subscription status, and other metadata.
4. **Pre‑Scoring Filters**
   - Removes duplicates, posts older than 48 hours, the viewer’s own posts, content from blocked/muted accounts, muted keywords, already‑served items, subscriber‑only posts the viewer cannot access, etc.

*The repository also contains additional sections on labeling path, scoring & ranking, filtering, experiments, what is not included, the transparency tool, key design decisions, and licensing, which together document the full end‑to‑end operation of X’s For You feed.*