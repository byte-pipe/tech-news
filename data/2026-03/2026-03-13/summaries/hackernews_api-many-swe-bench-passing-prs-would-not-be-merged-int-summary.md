---
title: Many SWE-bench-Passing PRs Would Not Be Merged into Main - METR
url: https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
date: 2026-03-12
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-13T03:13:29.042179
---

# Many SWE-bench-Passing PRs Would Not Be Merged into Main - METR

# Many SWE‑bench‑Passing PRs Would Not Be Merged into Main – METR

## Overview
- Approximately 50 % of AI‑generated pull requests (PRs) that pass the SWE‑bench Verified automated grader would be rejected by real maintainers, even after adjusting for reviewer noise.
- The agents were not allowed to iterate on feedback, so the gap does not imply a fundamental capability limit.
- Naïve reliance on benchmark scores can overstate the practical usefulness of code‑generation agents without additional elicitation or human feedback.

## Introduction
- Benchmark scores (e.g., 60 % SWE‑bench Verified) are often interpreted as real‑world success rates, but benchmarks use clean, automated grading unlike real maintainer review.
- To quantify this gap, four active maintainers from three SWE‑bench Verified repositories evaluated 296 AI‑generated PRs, indicating whether they would merge or request changes and why (functionality failure, breaking other code, or quality issues).
- Maintainer decisions on 47 human‑written “golden” PRs were also recorded to create a noise‑adjusted baseline.
- Main finding: maintainer merge rates are on average 24 percentage points lower than automated‑grader pass rates; improvement over time is ~9.6 pp/yr slower for maintainer decisions.
- Clarifications:
  1. Not claiming agents lack the capability to pass maintainer review; better prompting may close many gaps.
  2. Humans iterate with feedback, whereas models have a single submission attempt.
  3. Benchmarks still provide signal but should be treated as one piece of evidence, not decisive proof of real‑world capability.

## Relation to Prior Work
- Extends a previous blog post by:
  - Using actual maintainers instead of self‑review.
  - Focusing on SWE‑bench Verified scores for interpretability.
  - Expanding coverage to 95 tasks and five language models (vs. 18 tasks, one model).
  - Normalizing results with a golden baseline to account for reviewer noise.
  - Blinding reviewers to the source (human vs. AI).
- Prior analysis involved larger PRs (average 500 LOC changed) compared to the current sample (average 17 LOC).

## Data and Methods

### Maintainers & Repositories
- Four maintainers from three repos: two from scikit‑learn, one from Sphinx, one from pytest.
- Represents 25 % of SWE‑bench Verified repos and 19 % of issues.
- Maintainers recruited via cold email, compensated hourly with quality bonuses.
- Sample shown to be representative of overall pass rates.

### Agent Runs
- Patches sourced from Epoch’s benchmarking hub (2025) for:
  - Claude 3.5 Sonnet (old), Claude 3.7 Sonnet, Claude 4 Opus, Claude 4.5 Sonnet, GPT‑5, and human “golden” patches.
- Primarily Anthropic models, historically state‑of‑the‑art on SWE‑bench Verified.
- Minor manual cleanup (removing debugging files) before uploading to private repo snapshots.

### Review Procedure
- Only PRs that passed the automated grader were submitted for maintainer review; failures were imputed as maintainer rejections.
- Assumption of negligible false negatives is supported by:
  1. Human‑verified test suite screening.
  2. Small manual check showing 3.7 % false‑negative rate.
- Golden patches reviewed partially (half, randomly) to reduce workload.
- Reviews conducted on GitHub in “waves” with non‑overlapping issues; reviewers blinded to PR origin.
- Two deviations from real workflow:
  - No CI/linting due to historical repo state; reviewers informed that patches already passed automated tests.
  - Maintainers asked to evaluate as they would real PRs, except for missing CI feedback.

## Key Findings
- Maintainer merge rate ≈ 24 pp lower than automated‑grader pass rate on average.
- Year‑over‑year improvement in maintainer acceptance is slower than benchmark score gains.
- Roughly half of benchmark‑passing PRs would not be merged without additional iteration or feedback.

## Implications
- Benchmark scores alone can mislead stakeholders about the immediate deployability of AI‑generated code.
- Incorporating human feedback loops, better prompting, or post‑generation refinement may bridge the gap.
- Forecasts of AI progress should treat benchmark performance as indicative, not definitive, of real‑world impact.
