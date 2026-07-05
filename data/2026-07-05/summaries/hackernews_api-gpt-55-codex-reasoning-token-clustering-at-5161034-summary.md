---
title: GPT-5.5 Codex reasoning-token clustering at 516/1034/1552 may be leading to degraded performance on complex tasks · Issue #30364 · openai/codex · GitH...
url: https://github.com/openai/codex/issues/30364
date: 2026-07-04
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-07-05T11:38:03.464700
---

# GPT-5.5 Codex reasoning-token clustering at 516/1034/1552 may be leading to degraded performance on complex tasks · Issue #30364 · openai/codex · GitH...

### Codex Reasoning-Token Clustering at 516/1034/1552: An Aggregate Pattern with Implications for Complex Tasks

#### Background
A report by an individual referred to as "vguptaa45" discovered a discrepancy in performance of the Codex model. Notably, responses were landing on exactly 516 reasoning tokens, which was accompanied by additional fixed-boundary spikes around 1034 and 1552.

This issue is connected to a higher error rate for complex tasks compared to others, suggesting that Codex might experience degraded performance on these tasks due to the detected anomaly.

#### Investigation
The researcher identified an aggregate pattern indicative of model-specific behavior. While analyzing larger data sets across multiple time windows, they found evidence supporting this notion and linked it back to previous issues with Codex reproduction (related issue #30364).

Key findings include:

* **GPT-5.5**: A specific Collexmodel implicated in the anomaly.
* **Timestamps**:
	+ February 1, 2026 - Feb 27, 2026 UTC time window analyzed.
	+ Earlier issues (#29353) also found within this time frame.

#### Implications
This discovery has implications for Codex task performance expectations. A pattern indicating fixed-boundary spikes around specific reasoning token counts (516, 1034, and 1552) could contribute to reduced overall complexity of responses and higher errors on complex tasks.

Further investigation is needed to understand the mechanism behind this anomaly and its potential effects on model performance across various scenarios.