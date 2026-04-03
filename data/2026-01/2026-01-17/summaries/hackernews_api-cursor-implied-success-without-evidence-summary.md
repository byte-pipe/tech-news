---
title: Cursor Implied Success Without Evidence
url: https://embedding-shapes.github.io/cursor-implied-success-without-evidence/
date: 2026-01-16
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-01-17T11:12:34.483087
screenshot: hackernews_api-cursor-implied-success-without-evidence.png
---

# Cursor Implied Success Without Evidence

# Cursor's Browser Experiment Implied Success Without Evidence

On January 14th 2026, Cursor published a blog post discussing their experiments with running "coding agents autonomously for weeks" and exploring the limitations of agentic coding. They proposed an approach where multiple autonomous agents could work together to achieve significant progress on projects that typically take human teams months to complete.

## Main Points

* Cursor ran an ambitious project to build a web browser from scratch for near a week, generating over 1 million lines of code across 1,000 files.
* Despite the impressive feat, Cursor explicitly states they never "solved most of our coordination problems and let us scale to very large projects without any single agent," suggesting their approach may not have achieved true success.

## Discrepancies Between Claimed Success and Actual Outcome

* Cursor claimed that new agents could understand and make meaningful progress in the codebase, but this was never explicitly stated or tested.
* The browser, despite seeming simple, is plagued by errors and warnings from various contributors who failed to compile it during recent attempts.
* AGitHub Action on `mainshow` project fails multiple times since most recent commit, with dozens of compiler errors and 100 warnings reported.

## Critical Observations

* Cursor never ran "cargo build" or more explicitly stated compilation commands, suggesting their code may not be engineered well enough for production use.
* The compilation errors made clear that none of the effort was suitable as high-quality code (known as "AI slop").
* This is evident from open issues on the `fastrender` GitHub repository regarding the project's code quality and functionality.
