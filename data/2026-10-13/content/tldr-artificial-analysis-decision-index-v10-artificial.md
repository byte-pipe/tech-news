---
title: Artificial Analysis Decision Index v1.0 | Artificial Analysis
url: https://artificialanalysis.ai/articles/artificial-analysis-decision-index
site_name: tldr
content_file: tldr-artificial-analysis-decision-index-v10-artificial
fetched_at: '2026-10-13T23:13:35.360492'
original_url: https://artificialanalysis.ai/articles/artificial-analysis-decision-index
date: '2026-10-13'
published_date: '2026-10-13'
description: The Artificial Analysis Decision Index benchmarks decision models, a new category of models that answer structured decisions in a single call with a probability for each option. Version 1.0 combines four evaluations across classification, tool calling, knowledge, hallucination, and reasoning.
tags:
- tldr
---

Artificial Analysis
K

All articles

October 13, 2026

# Artificial Analysis Decision Index v1.0

The Artificial Analysis Decision Index benchmarks decision models, a new category of models that answer structured decisions in a single call with a probability for each option. Version 1.0 combines four evaluations across classification, tool calling, knowledge, hallucination, and reasoning.

Decision Index leaderboard
Read the methodology
This is the original launch article and shows 
Artificial Analysis Decision Index
 results as of launch. For live results across the latest models, see the 
Artificial Analysis Decision Index
 leaderboard
.

## Introducing the Artificial Analysis Decision Index

Decision models are an emerging class of models that output structured answers or classifications with associated probabilities. Unlike language models designed for complex reasoning and long-horizon tasks, decision models focus on making structured decisions faster and at lower cost.

With the launch of theArtificial Analysis Decision Indexv1.0, we aim to help developers and companies understand the capability, cost, and speed trade-offs of decision models, both relative to other decision models and to language models.

#### State

“Help! My payouts have been failing for 3 days and my rent is due tomorrow. This is unacceptable.”

#### Questions

* ChoiceRoute to team
* Yes/NoUrgent?
* ScoreHow upset?

#### Decision model

Every question in one call, with a probability for every option

Route to team

Billing
Technical
Account

Urgent?

Yes
No

How upset?

Calm
Frustrated
Angry

#### Language model

Generates a structured output

.

Parsed answer

Route to team
 
Billing
Urgent?
 
Yes
How upset?
 
Angry

Decision models choose from a fixed set of options, with a probability for each, in one call. That makes them cheap and fast, and lets us measure their calibration.

## What the Decision Index measures

At launch, theArtificial Analysis Decision Indexcombines four evaluations covering classification, tool calling, knowledge, hallucination, and reasoning:

Knowledge and hallucination
AA-Omniscience-Decision

500 private questions adapted from our knowledge and hallucination benchmark AA-Omniscience. Each offers five options: four answers, one of them correct, and "I don't know".

25% of the index: accuracy and non-hallucination rate 12.5% each

Reasoning
HLE-MultiChoice

The 513 text-only multiple-choice questions from Humanity's Last Exam, each posed as one choice among its lettered answers.

25% of the index

Tool calling
When2Call

NVIDIA's tool-calling evaluation. Given a conversation and a set of tools, the model chooses whether to answer directly, call a tool, ask for more information, or say it cannot answer.

25% of the index

Classification
WildGuardTest

Ai2's safety classification test set. The model decides whether a user's request is harmful, whether an assistant's reply is a refusal, and whether that reply is harmful.

25% of the index

We also run every evaluation on LLMs. An LLM answers with a structured output that names the option it chose, so it gives no probability for each option.

## Decision model results

Jev 1.13 leads the Decision Index with 58, ahead of GLiDE and Microsoft-Decision-1, both on 54. Jev 1.13 outperforms other decision models on the reasoning benchmark HLE-MultiChoice, scoring 21 where other models score 15 or less. On the knowledge and hallucination benchmark AA-Omniscience-Decision, Jev 1.13 has an accuracy score of 35, below most decision models and the top score of 41 by Liquid AI's d1, but has the second highest non-hallucination rate of 35 where d1 scores only 2. On the tool calling benchmark When2Call, Jev 1.13 scores 81 in fourth place, with Celeris-1 Decision and Fastino Labs' GLiDE both leading at 84. It scores 94 on the classification benchmark WildGuardTest, equal with Perplexity's Decider v1.1 27B and one point behind GLiDE at 95.

Decision Index
Score by Benchmark
AA-Omniscience-Decision Accuracy
AA-Omniscience-Decision Non-Hallucination Rate
HLE-MultiChoice
When2Call
WildGuardTest

### Artificial Analysis Decision Index

Weighted average of AA-Omniscience-Decision, HLE-MultiChoice, When2Call, and WildGuardTest · Higher is better
9 of 11 models
Include language models

## Cost and time efficiency of decision models

Decision models differ widely in cost and speed. Costs run from $17 to $199 per one million tasks, and median times from 0.06 to 0.5 seconds per task.

Decision Index vs. Cost per 1M Tasks
Decision Index vs. Time per Task

### Artificial Analysis Decision Index vs. Cost per 1M Tasks

Artificial Analysis Decision Index score vs. average cost per 1 million tasks (USD) · Lower is better
9 of 11 models
Include language models
Most attractive quadrant
Pareto line
TypeSafe
Fastino
Microsoft
Perplexity
Inception
Celeris
Liquid AI
Cloudflare
OpenAI

### Decision Cost per 1M Tasks

Average cost per task at current token prices, multiplied by 1 million; for the index, the cost of one pass through all its evaluations divided by their combined tasks, multiplied by 1 million. Decision models are billed for input tokens only, and language models for input and output tokens.

Decider v1.1 27B has the lowest Cost per 1M Tasks at $17, with Microsoft-Decision-1 ($31) and Jev 1.13 ($42) also on the Capability vs. Cost Pareto frontier. GLiDE scores 54, level with Microsoft-Decision-1, but costs $119, about three times as much as Jev 1.13. Celeris-1 Decision has the fastest Time per Task at 0.06 seconds, more than twice as fast as Jev 1.13 at 0.13 seconds.

Time per Task
Cost per 1M Tasks

### Artificial Analysis Decision Index: Time per Task

Median time per task over every task across all Artificial Analysis Decision Index evaluations · Lower is better
9 of 11 models
Include language models

### Decision Time per Task

Median latency per task, in milliseconds; for the index, the median across the tasks of all its evaluations.

## Decision models are overconfident

Decision models give a probability for each option, so we can check whether the probability a model assigned to its chosen answer matches how often it is right. Overall, across almost all probability levels, accuracy falls below that probability for all decision models. This is driven by relatively poor calibration on the knowledge and reasoning tasks in HLE-MultiChoice and AA-Omniscience-Decision. In comparison, most decision models are relatively well-calibrated on When2Call (tool calling) and WildGuardTest (classification).

Index Calibration
AA-Omniscience-Decision
HLE-MultiChoice
When2Call
WildGuardTest

### Artificial Analysis Decision Index Calibration

Accuracy of answers against the probability the model gave its chosen answer, grouped into tenths of that probability, each benchmark weighted equally
9 of 11 models
Jev 1.13
GLiDE
Microsoft-Decision-1
Decider v1.1 27B
Mercury Decide
Celeris-1 Decision
d1
Clef
GPT-6 Luna (Decisions)
Perfect calibration

Calibration for language models coming soon.

## How decision models compare with LLMs

Decision models offer significant speed and cost advantages over language models, but trail on knowledge and reasoning. Claude Haiku 5.5 (Low) scores 61 on the Decision Index, 3 points ahead of Jev 1.13, but takes 1.4 seconds per task against 0.13 seconds (11 times slower) and costs $184 per one million tasks against $42 (4.4 times as much). GPT-6 Luna (Low) scores 55, below Jev 1.13, at 1.5 seconds per task and $131 per one million tasks.

Language models lead on knowledge: on AA-Omniscience-Decision accuracy, Claude Haiku 5.5 (Low) scores 52 and GPT-6 Luna (Low) 66, against 28 to 41 for decision models. On HLE-MultiChoice, they score 24 and 22, against 21 for Jev 1.13 and 15 or less for every other decision model.

On classification and tool calling, leading decision models perform comparably. On WildGuardTest, GLiDE scores 95 and Decider v1.1 27B and Jev 1.13 score 94, against 93 for Claude Haiku 5.5 (Low) and 89 for GPT-6 Luna (Low). On When2Call, Celeris-1 Decision and GLiDE score 84, against 77 for GPT-6 Luna (Low) and 73 for Claude Haiku 5.5 (Low).

Decision Index
Score by Benchmark
AA-Omniscience-Decision Accuracy
AA-Omniscience-Decision Non-Hallucination Rate
HLE-MultiChoice
When2Call
WildGuardTest

### Artificial Analysis Decision Index

Weighted average of AA-Omniscience-Decision, HLE-MultiChoice, When2Call, and WildGuardTest · Higher is better
11 of 26 models
Include language models
Decision model
Language model
Decision Index vs. Cost per 1M Tasks
Decision Index vs. Time per Task

### Artificial Analysis Decision Index vs. Cost per 1M Tasks

Artificial Analysis Decision Index score vs. average cost per 1 million tasks (USD) · Lower is better
11 of 26 models
Include language models
Most attractive quadrant
Pareto line
Anthropic
TypeSafe
OpenAI
Fastino
Microsoft
Perplexity
Inception
Celeris
Liquid AI
Cloudflare

### Decision Cost per 1M Tasks

Average cost per task at current token prices, multiplied by 1 million; for the index, the cost of one pass through all its evaluations divided by their combined tasks, multiplied by 1 million. Decision models are billed for input tokens only, and language models for input and output tokens.

## Knowing when not to answer

Every AA-Omniscience-Decision question offers "I don't know", and the non-hallucination rate is the share of questions a model did not answer correctly where it chose that option. Microsoft-Decision-1 leads decision models at 40%, followed by Jev 1.13 at 35% and Mercury Decide at 32%. No other decision model reaches 17%.

Non-Hallucination Rate
Accuracy

### AA-Omniscience-Decision: Non-Hallucination Rate

Share of questions not answered correctly where the model chose "I don't know" · Higher is better
9 of 11 models
Include language models

## Explore further

* Live scores for the latest models are on theArtificial Analysis Decision Indexpage
* Themethodology pagedetails how we pose and score each evaluation
* Each of the four evaluations has its own leaderboard:AA-Omniscience-Decision,HLE-MultiChoice,When2Call, andWildGuardTest
* To have a decision model added to the index, contact us atdecision-models@artificialanalysis.ai

#### Read the latest

### Announcing AA-3D: a benchmark for AI models building interactive 3D experiences

AA-3D is a new benchmark of how well AI models build interactive 3D experiences. Each model turns a written brief into a working three.js scene in an offline sandbox, and our recruited panel compares the scenes in blind pairwise votes.

October 12, 2026

### Announcing FrontierCode on Artificial Analysis: can AI models write code maintainers would merge?

Cognition's FrontierCode 1.1 tests whether AI models make code changes that maintainers of real open source repositories would merge. Leading models still fail more than 40% of the time.

October 12, 2026

### Muse Wonder and Muse Wonder Full: a material jump in intelligence over previous Meta models

Meta has released Muse Wonder and Muse Wonder Full, achieving Artificial Analysis Intelligence Index v4.3 scores of 52 and 56 at max reasoning effort - each a material gain over Muse Spark 1.3 (max) at 48, with a release gap of only 6 weeks

October 12, 2026