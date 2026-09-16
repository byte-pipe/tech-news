---
title: Ant Group releases finance-focused Ling-3.0-flash-Fin | Artificial Analysis
url: https://artificialanalysis.ai/articles/ant-group-releases-finance-focused-ling-3-0-flash-fin
site_name: tldr
content_file: tldr-ant-group-releases-finance-focused-ling-30-flash-f
fetched_at: '2026-09-16T15:21:48.342273'
original_url: https://artificialanalysis.ai/articles/ant-group-releases-finance-focused-ling-3-0-flash-fin
date: '2026-09-16'
published_date: '2026-09-16'
description: Independent analysis of AI models and hosting providers. Understand the AI landscape and choose the best model and API provider for your use-case.
tags:
- tldr
---

Artificial Analysis
K
All articles

September 16, 2026

# Ling-3.0-flash-Fin, Ant Group’s new finance-focused open weights model, scores 23 on the Artificial Analysis Intelligence Index and 24 on the Finance & Accounting Index, and is on the Intelligence vs. Active Parameter Pareto Frontier

See model page

Ant Group has released Ling-3.0-flash-Fin, a finance-focused model built on Ling-3.0-flash. Ant Group announced that it developed the model with financial institutions and industry experts to support financial research, including checking sources, building valuation spreadsheets and writing reports. This text-only model comes after their release of their image and video input-capable model Ling-3.0-flash-VL, which scored 25 on the Intelligence Index.

## Key results:

➤Ling-3.0-flash-Fin matches MiniMax-M2.7’s Intelligence Index score with roughly half the active parameters.Both score 23, while Flash-Fin activates 5.1B parameters per token compared with MiniMax-M2.7’s 10B.

➤Ling-3.0-flash-Fin matches Ling-3.0-flash-VL at 24 on the Artificial Analysis Finance & Accounting Index.Fin has higher business knowledge accuracy than VL (17% vs. 11%), but also higher business knowledge hallucination (33% vs. 19%)

➤Ling-3.0-flash-Fin scores slightly below Ling-3.0-flash-VL on professional knowledge work.It scores 1171 Elo on GDPval-AA v2 and 967 on AA-Briefcase, compared with 1225 and 986 respectively for Ling-3.0-flash-VL. Both benchmarks test agents on professional tasks such as producing documents and spreadsheets.

➤Difficult agentic tasks remain a challenge for Ling-3.0-flash-Fin.It scores 7% on AutomationBench-AA, which tests workflows across business apps while respecting guardrails, compared with 16% for the flash-VL model. Both models score 0% on Terminal-Bench v4.0, which tests difficult terminal-use tasks.

➤Ling-3.0-flash-Fin uses more output tokens than the flash-VL model and MiniMax-M2.7.It averages ~67k output tokens per Intelligence Index task, about 34% more than VL (~50k) and 3.2x MiniMax-M2.7 (~21k).

## Additional model details:

➤Type:Open weights reasoning model.

➤Size:124B total parameters, 5.1B active per token (MoE).

➤Context window:256K tokens.

➤Modalities:Text input and output.

➤API availability:Available through @OpenRouter, including a rate-limited free endpoint.

➤License:MIT.

Ling-3.0-flash-Fin sits on the Intelligence Index vs. active parameters Pareto frontier, scoring 23 with 5.1B active parameters per token vs. a score of 25 or Ling-3.0-flash-VL which uses 5.5B active per token.Both have 124B total parameters, while Qwen3.8 27B (xhigh) scores 34 with 27B total parameters, placing both Ling models below the total-parameter frontier.

Ling-3.0-flash-Fin scores 24 on the Artificial Analysis Finance & Accounting Index, which combines business knowledge, reasoning, agentic work, long-context analysis and non-hallucination.This is the same score as Ling-3.0-flash-VL both. Fin has higher business knowledge accuracy (17% vs. 11%), but also worse business knowledge hallucination (non-hallucination rate of 67% vs. 81%).

Ling-3.0-flash-Fin scores 1171 Elo on GDPval-AA v2, which tests agents on professional knowledge work.This is ~50 points behind Ling-3.0-flash-VL which scored 1225, and is above MiniMax-M2.7, which scored 1087.

Ling-3.0-flash-Fin scores 967 Elo on AA-Briefcase, slightly below Ling-3.0-flash-VL (986).AA-Briefcase tests agents on complex business workflows, using large collections of source files to produce spreadsheets, presentations and memos. Against VL, Fin passes fewer rubric checks (23.5% vs. 24.9%) and scores lower on Analytical Quality Elo (866 vs. 907), while its Presentation Elo is slightly higher (1095 vs. 1076), which is surprising as it does not posses the image input capabilities of the VL model.

Ling-3.0-flash-Fin averages ~67k output tokens per Intelligence Index task, ~34% more than Ling-3.0-flash-VL, which produced ~50k per task.

Full results for Ling-3.0-flash-Fin across the 10 evaluations in the Artificial Analysis Intelligence Index v4.3.

#### Read the latest

### Benchmarking GPT-6 Astra

GPT-6 Astra ties leadership with Claude Fable 5.1 in both of our flagship Indices, at lower cost. Astra equals Fable 5.1 in the Intelligence Index at ~40% of the cost, and in the Coding Agent Index at ~60% of the cost.

September 9, 2026

### Announcing the Artificial Analysis Intelligence Index v4.3

We are upgrading Terminal-Bench to 4.0 and adding AutomationBench-AA, an agentic workflow automation benchmark with a private test set. This is a continuation of our rollout of Intelligence Index v5.

September 7, 2026

### OpenBMB releases MiniCPM5-2B

OpenBMB releases MiniCPM5-2B

September 7, 2026