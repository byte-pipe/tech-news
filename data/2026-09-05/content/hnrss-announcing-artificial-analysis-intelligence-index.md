---
title: Announcing Artificial Analysis Intelligence Index v4.2 | Artificial Analysis
url: https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2
site_name: hnrss
content_file: hnrss-announcing-artificial-analysis-intelligence-index
fetched_at: '2026-09-05T13:42:05.657009'
original_url: https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v4-2
date: '2026-09-05'
published_date: '2026-09-04'
description: Independent analysis of AI models and hosting providers. Understand the AI landscape and choose the best model and API provider for your use-case.
tags:
- hackernews
- hnrss
---

Artificial Analysis
K
All articles

September 4, 2026

# Announcing Artificial Analysis Intelligence Index v4.2

We are accelerating elements of our upcoming v5 release with interim updates to keep pace with the frontier. Index v4.2 has more complex and realistic tasks, and more private test sets to prevent gaming

Intelligence Index v4.2 changelog:

+ AA-Briefcase, our agentic knowledge work evaluation with a private test set

+ Surge’s GDP.pdf, long context document reasoning across 4,592 PDF pages

- GPQA Diamond,an exceptional scientific reasoning evaluation that has now been saturated

… plus greater weighting on held-out test sets to prevent gaming, and grading infrastructure upgrades to increase robustness

This update brings the Index closer to real-world use cases with more challenging, complex and realistic tasks and private test sets to prevent gaming. We have been planning and building elements of Index v5 for months - it’s been 8 months since we launched Index v4 in January.

We have deliberately held back updates to keep the Index stable through recent major model launches. However, with the frontier moving so quickly in the past weeks, we feel it is important to deliver an immediate interim update to ensure our Index remains as relevant and useful as ever to users.

Beyond this interim update, our team is hard at work on v5 of the Index. We are planning more incremental releases in the near future. Stay tuned!

Intelligence Index v4.2 changes in detail:

➤ Adding AA-Briefcase:Our in-house evaluation with a private held-out test set, AA-Briefcase tests models on realistic agentic knowledge work tasks in complex projects built by industry experts. Models are evaluated on multi-week knowledge work projects, each with many linked tasks and thousands of input source files. AA-Briefcase combines rubric and pairwise grading to evaluate verifiable task success, analytical quality, and presentation quality, giving a holistic view of overall agentic capability in knowledge work.

➤ Adding GDP.pdf:Created by Surge AI, GDP.pdf evaluates single-turn professional document reasoning across 100 PDFs and ten domains. Models must synthesize evidence distributed across 4,592 pages, including text, tables, charts, footnotes, and exclusions. Responses are graded against 1,275 expert-authored atomic criteria; the headline All-pass Rate credits a task only when every criterion is satisfied.

➤ Weighting to measure real-world use and prevent gaming:40% of our Index weighting is now private, held-out test sets - double the figure from v4.1. Held-out data includes AA-Briefcase, AA-Omniscience, and solutions for CritPt. This reduces the ability for labs to game evaluations. The held-out percentage will increase further in Index v5.

➤ Improving our grading infrastructure:In AA-LCR v1.1, we have added a grading system prompt and corrected errors and ambiguities in answer keys, improving scoring accuracy. For GDPval-AA v2 and AA-Briefcase, we have improved our sampling and re-anchored the Elo scale, making ratings more stable as new models are added. For SciCode we have improved robustness of grading sandboxes to ensure slow but correct code does not count as a failure.

Key results:

➤ Anthropic and OpenAI lead the Index:Anthropic’s Claude Fable 5.1 leads the Index, followed by OpenAI’s GPT-6 Astra, which shows a 4pt gain over GPT-5.6 Sol. Meta is the third-ranked lab on the leaderboard, followed by SpaceXAI, Moonshot/Kimi, Z.AI, and Google.

➤ Cost per Task Pareto frontier shared by four labs:Anthropic, OpenAI, Meta and Z.AI occupy the updated Cost per Task frontier.

➤ GPT-6 Astra dominates the output token frontier:GPT-6 Astra is more token efficient than almost every other model near the intelligence frontier, with Claude Fable 5.1, Grok 4.5 and Gemini 3.5 Flash-Lite at either end of the curve (excludes models below 25 on the Index)

GPT-6 Astra is more token efficient than almost every other model near the intelligence frontier, with Claude Fable 5.1, Grok 4.5 and Gemini 3.5 Flash-Lite at either end of the curve (excludes models below 25 on the Index)

Anthropic’s Claude Fable 5.1 and Opus 5 lead AA-Briefcase, followed by GPT-6 Astra and Muse Spark 1.3. GPT-6 Astra shows a substantial gain above GPT-5.6 Sol of ~85 Elo points

AA-Briefcase is our frontier in-house evaluation with a private held-out test set. The evaluation tests models on realistic agentic knowledge work tasks in complex projects built by industry experts. Models are evaluated on multi-week knowledge work projects, each with many linked tasks and thousands of input source files. AA-Briefcase combines rubric and pairwise grading to evaluate verifiable task success, analytical quality, and presentation quality, giving a holistic view of overall agentic capability in knowledge work.

OpenAI leads GDP.pdf with GPT-6 Astra at 33.2% and GPT-5.6 Sol at 28.2%, followed by Claude Fable 5.1 at 26.2%

Created by Surge AI, GDP.pdf evaluates single-turn professional document reasoning across 100 PDFs and ten domains. Models must synthesize evidence distributed across 4,592 pages, including text, tables, charts, footnotes, and exclusions. Responses are graded against 1,275 expert-authored atomic criteria; the headline All-pass Rate credits a task only when every criterion is satisfied

Full per-model breakdowns below:

Read more about Artificial Analysis Intelligence Index v4.2 athttps://artificialanalysis.ai/methodology/intelligence-benchmarking

#### Read the latest

### Benchmarking GPT-6 Astra

GPT-6 Astra makes significant gains in the Artificial Analysis Coding Agent Index, scoring equal to Fable 5 at lower cost. In the Intelligence Index, it uses fewer tokens than GPT-5.6 Sol for similar performance, but this is outweighed by higher prices

September 3, 2026

### Muse Spark 1.3: Meta reaches the frontier

Independent analysis and benchmarks of Meta's Muse Spark 1.3

September 2, 2026

### Google has released Gemini 3.8 Flash, its fourth Flash model in under four months

Gemini 3.8 Flash scores 59 on the Artificial Analysis Intelligence Index and reaches the Intelligence vs. Cost per Task Pareto frontier

September 2, 2026