---
title: The Pulse: Anthropic builds its own source control system - The Pragmatic Engineer
url: https://blog.pragmaticengineer.com/the-pulse-anthropic-builds-its-own-source-control-system
date: 2026-10-22
site: tldr
model: llama3.2:1b
summarized_at: 2026-10-22T16:08:09.783721
---

# The Pulse: Anthropic builds its own source control system - The Pragmatic Engineer

**Anthropic Builds Autonomous Source Control System - The Pragmatic Engineer**

The article discusses how Anthropic, a technology company, has removed its reliance on Git and built its own custom source control system. This decision was made after the company noticed that coding was no longer a bottleneck to its operations and research was being made at a faster speed while being scaled.

**Main Points:**

* Anthropic's bottleneck now is its developer infrastructure, including source control, builds, and continuous integration (CI).
* The company averaged over 30,000 code changes merged daily in September 2022, and 50,000 code changes daily by May 2026.
* Prior to the implementation of its custom source control system, Anthropic merged around 2,500 code changes daily.

**Key Findings:**

* The increased frequency of code changes leads to a snowball effect, with more PRs and reviews.
* The growth of code changes by 12x in a four-month period is a notable increase.
* Another tech company, Google, has been preparing for a similar scenario by planning for 100x more code in production.

**Industry Comparison:**

* Anthropic's use of a monorepo and 25 million daily Git checkouts sets it apart from other tech companies.
* The extensive use of parallel Claude agents enables a large number of pull requests to be created daily, triggering a massive number of checks for the CI system.

**Impact on Development Workflow:**

* The development team at Anthropic sees a significant shift in their workflow, as automation allows for faster iteration and research.
* The company's ability to build new services from the ground up at a speed and scale that it hasn't seen before has enabled significant growth in its growth rate.