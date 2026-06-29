---
title: "HackerRank's Open-Source ATS Gave My Resume a Different Score Every Time."
url: https://danunparsed.com/p/hackerrank-open-source-ats
date: 2026-06-29
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-29T19:25:26.352759
---

# HackerRank's Open-Source ATS Gave My Resume a Different Score Every Time.

# Summary of “HackerRank’s Open‑Source ATS Gave My Resume a Different Score Every Time”

## Overview
- The author tested HackerRank’s open‑source applicant‑tracking system (ATS) on their own résumé.
- Scores varied widely across runs (e.g., 90, 74, 88, 83 out of 100) despite using the same résumé and command.
- The variability is attributed to non‑deterministic behavior of the underlying language model (LLM).

## How the Tool Works
- PDF résumé is parsed to text.
- An LLM is called six times to extract sections: basics, work history, education, skills, projects, awards.
- The tool also pulls the candidate’s GitHub profile and top repositories as extra context.
- All extracted data are fed to a final LLM call that produces a score out of 100, plus up to 20 bonus points.
- Scoring breakdown (default):
  - 35 points for open‑source contributions
  - 30 points for personal projects
  - 25 points for work experience
  - 10 points for technical skills
  - Up to 20 bonus points for startup experience, portfolio site, technical blog, etc.
- Default model: gemma3:4b with temperature 0.1 (low temperature intended to increase determinism).

## Observed Score Distribution
- Running the ATS 100 times produced scores ranging from 66 to 99.
- With a cutoff of 85, the author would fail about 65 % of the time despite an unchanged résumé.
- Switching to Gemini narrowed the range (48–64) but still caused failures (≈28 % below a cutoff of 60).

## Category‑Level Consistency
- **Technical skills:** Highly consistent (≈8/10 in 98 % of runs). Checklist‑style evaluation leaves little room for LLM variance.
- **Projects:** Large variation; the LLM’s judgment on “architectural complexity” or “real‑world deployment” changes randomly.
- **Work experience:** Always scored 25/25, regardless of the depth or seniority of the experience, due to an overly vague prompt with no rubric or anchors.

## Core Issues Identified
- **Non‑determinism:** Even with temperature 0, scores fluctuate, indicating a fundamental design flaw rather than a tuning problem.
- **Prompt design:** Sparse prompts for experience lead to uniform but meaningless scores; detailed rubrics for projects still yield noisy results.
- **Weighting bias:** Heavy emphasis on open‑source and projects (65 % of total) can undervalue seasoned engineers whose work isn’t on GitHub.
- **Reliability for hiring:** The tool cannot reliably differentiate candidate quality; it essentially filters by luck.

## Recommendations for Practitioners
- Treat AI‑screening tools with caution; they may discard qualified candidates due to randomness.
- Prefer using LLMs for structured data extraction and simple skill checks, not for nuanced experience evaluation.
- If employing such tools, supplement them with human review to mitigate false negatives.

## Corrections & Additional Notes
- A reader pointed out that the `resume_evaluation_criteria.jinja` template mentions “Software Intern” without documentation; the scoring is position‑agnostic.
- The repository’s open‑source status dates back to October 2025, though it only recently went viral on LinkedIn and Reddit.
- Non‑determinism at temperature 0 was previously reported in a GitHub issue opened in October 2025.