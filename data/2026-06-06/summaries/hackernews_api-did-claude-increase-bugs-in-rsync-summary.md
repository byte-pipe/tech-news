---
title: Did Claude Increase Bugs in rsync?
url: https://alexispurslane.github.io/rsync-analysis/
date: 2026-06-05
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-06T11:51:15.684447
---

# Did Claude Increase Bugs in rsync?

# Did Claude Increase Bugs in rsync?

## Disclaimer: How AI Assistance Was Used
- All metrics, methodology, and data sources were chosen by the author with input from his wife (M.S. in Statistics).  
- The wife advised against simple bugs‑per‑lines comparisons and linear regression due to small post‑Claude sample size; instead she suggested comparing post‑Claude releases to the historical distribution.  
- The author spent several days manually drafting the report and later rewrote it in his own voice.  
- Scripts that fetched data, built a DuckDB database, performed statistical analysis, and generated HTML were written by GLM 5.1 (Claude).  
- Numbers, statistics, cards, and graphs are inserted automatically from the Python analysis script, eliminating hallucination risk.  
- The full reproducible pipeline is available in a public GitHub repository; readers can verify the data and calculations.

## Background: The rsync Outrage
- Late May 2026, a Mastodon post linked regressions observed after an rsync upgrade to the presence of Claude‑generated commits, sparking viral attention.  
- The post led to a GitHub issue titled “Please Do Not Vibe Fuck Up This Software,” which contained only a screenshot of the Mastodon critique, no technical details.  
- The issue attracted hundreds of comments, some devolving into harassment and threats toward the maintainer.  
- The controversy spread to Hacker News, Lobsters, and other platforms, with many users asserting that Claude‑assisted development introduced bugs into a previously stable tool.  
- Some community members called for empirical evidence, prompting the author to create a data‑driven analysis of bug regressions across releases.

## Executive Summary
- Analyzed 36 rsync releases (v2.4.6 – v3.4.3) with available bug data.  
- Two releases contain Claude commits:  
  - v3.4.2 – 9 Claude commits, severity‑weighted bugs per 10 commits (sev/10c) = 0.00 (below interquartile range).  
  - v3.4.3 – 28 Claude commits, sev/10c = 3.29 (above interquartile range).  
- Neither Claude release is a statistical outlier.  
- Exact permutation test: p‑value = 46 % (randomly picking any two releases would be as bad or worse 46 % of the time).  
- Fisher’s exact test: p‑value = 74 % (Claude releases are not more likely than others to exceed the historical median; odds ratio ≈ 1.06).  
- Historical mean sev/10c = 2.95; Claude mean = 1.65 (historical mean is 1.8× the Claude mean).  
- Release v3.4.1 (59 bugs / 9 commits, no Claude) is an outlier but considered part of the baseline distribution.

## The Metric
- Primary metric: severity‑weighted bugs per 10 commits (sev/10c).  
- Each bug is normalized by its severity rating, then summed and divided by the number of commits (scaled to ten).  
- This single metric enables comparison across releases with differing commit counts.