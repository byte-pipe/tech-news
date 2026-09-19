---
title: Artificial Analysis starts counting when coding agents refuse the job
url: https://runtimewire.com/article/artificial-analysis-coding-agent-safety-refusal-reporting
site_name: tldr
content_file: tldr-artificial-analysis-starts-counting-when-coding-ag
fetched_at: '2026-09-19T21:18:07.628368'
original_url: https://runtimewire.com/article/artificial-analysis-coding-agent-safety-refusal-reporting
author: RuntimeWire
date: '2026-09-19'
published_date: '2026-09-19T18:06:59.835Z'
description: Artificial Analysis now tracks blocked and fallback safety refusals in its Coding Agent Index, showing how provider policies affect agent reliability.
tags:
- tldr
---

Primary source:Artificial Analysis on X

## Why it matters

Coding-agent performance depends on provider policies as well as model capability. By separating blocked attempts from successful fallbacks, Artificial Analysis gives developers a clearer view of whether an agent can complete legitimate security and terminal work when safeguards intervene.

Artificial Analysis, co-founded byMicah Hill-Smith (@_micah_h)andGeorge Cameron, added safety-refusal reporting to its Coding Agent Index on September 18th, exposing how often an AI provider or model declines benchmark work on safety grounds. Artificial Analysis announced the addition on X alongside version 1.5 of its coding-agent benchmark.

Artificial Analysis on X

The metric fits the problem that pulled Hill-Smith into AI evaluation in the first place. While building a legal-research tool, he found that different models worked better at different steps, with no dependable way to compare quality, speed and price. He began publishing experimental dashboards in early 2023, then teamed up with Cameron, a friend he had met during a Google internship, according to Hill-Smith'saccount of Artificial Analysis's origin.

Hill-Smith, who studied computer science before working at McKinsey, now serves as CEO. Cameron, previously a strategy consultant focused on data centers and technology businesses, is chief product officer. Their product has steadily expanded from comparisons of standalone models into evaluations of complete agent systems, where the model, harness, tools and provider policies all affect whether a task gets finished.

Safety refusals put a number on one of those operational dependencies.

### A zero can begin with a policy decision

Artificial Analysis defines a safety refusal as a provider or model declining to start or continue a task on safety grounds. Thepublished methodologydivides those events into two outcomes: blocked and fallback.

A blocked attempt ends after a provider safety error or a model refusal. Artificial Analysis retries provider errors up to 10 times. If every retry is blocked, the attempt receives a zero. A model refusal that ends an attempt also receives a zero, without a retry.

A fallback occurs when the coding agent recovers, either by moving to another model or continuing with the same one. Artificial Analysis scores the completed attempt normally. That distinction matters because a visible refusal does not always end the workflow. An agent with effective routing can absorb the refusal, though the fallback model may be less capable than the first choice.

Artificial Analysis calculates the refusal rate from retained, scored attempts. Superseded retries are excluded. The overall rate gives equal weight to each of the index's three component benchmarks, matching the index's scoring method.

The blocked rate also provides an upper bound on the damage refusals did to the index score. Artificial Analysis says a 2% blocked rate could have cost an agent no more than two index points, since every blocked attempt scores zero.

### Security work makes refusals part of performance

The issue is particularly relevant to coding agents because the benchmark suite includes security work, including tasks involving vulnerability discovery and exploitation. Those assignments can activate safeguards even when they appear inside a controlled evaluation.

A refusal can be the intended outcome of a provider's safety policy. It still leaves a developer without a completed task. Artificial Analysis's new chart makes that tradeoff visible next to capability, cost, token use and execution time, rather than folding every unsuccessful run into the same pass-rate number.

That distinction will matter as coding agents move into security reviews, system administration and other workflows where legitimate work can resemble harmful activity to a model or provider filter. Two agents with similar aggregate scores may behave differently when a task crosses a policy boundary: one can stop, another can switch models, and a third can proceed without triggering a refusal.

The metric does not determine whether a provider's policy is appropriate. It measures the practical effect of that policy within a defined set of tasks. Buyers still have to decide whether a lower refusal rate reflects greater usefulness, looser safeguards or a harness that handles provider restrictions more effectively.

### The leaderboard is a composite, with all the usual caveats

TheCoding Agent Indexcombines 303 tasks across three evaluations. DeepSWE v1.1 contributes 113 long-horizon software-engineering tasks. Terminal-Bench 4.0 contributes 66 terminal-use tasks. SWE-Atlas-QnA contributes 124 repository question-and-answer tasks.

Each task is attempted three times. Artificial Analysis averages those attempts into a pass@1 result for each task, then calculates each benchmark score. The final index gives the three benchmarks equal weight, despite their different task counts.

That choice prevents the 124-task SWE-Atlas-QnA set from automatically carrying nearly twice the influence of the 66-task Terminal-Bench set. It also means rankings depend on the selected benchmark mix and its grading systems. DeepSWE uses a program verifier, Terminal-Bench uses test-suite outcomes, and SWE-Atlas-QnA follows Scale AI's binary task-resolution method withClaude Opus 4.5as judge.

Each public row represents a specific agent variant, including model and reasoning settings, rather than a generic model family. The current page displays 14 of 15 model or agent variants. Artificial Analysis reports cost using pay-per-token API pricing, excluding engineering, infrastructure and supervision. Its active runtime measure also excludes environment startup and verifier or judge time.

Those boundaries make the charts useful for comparison, though they stop short of representing the full expense or elapsed time of operating an agent in production.

### Hill-Smith and Cameron are benchmarking the failure modes

RuntimeWirereported in Julythat Hill-Smith and Cameron were applying final-state scoring to SaaS workflows, checking whether an agent left a database in the correct condition instead of judging only its written answer. Safety-refusal reporting follows the same approach: inspect what happened inside the workflow, then separate distinct ways an agent can fail or recover.

Artificial Analysis is building a benchmark product around failure diagnosis alongside the leaderboard number. The coding index now reports performance, token consumption, API cost, execution time, safety refusals and reward hacking. A planned harness comparison would add another variable, measuring how much of an outcome comes from the agent framework rather than the underlying model.

Artificial Analysissays it has benchmarked more than 500 models, more than 100 inference providers and more than 1,000 endpoints, processing over 1 trillion evaluation tokens. Those scale figures are self-reported. Artificial Analysis lists Nat Friedman, Daniel Gross, Andrew Ng, Adam D'Angelo, Clem Delangue, Guillermo Rauch, Shawn Wang and Charlie Songhurst among its backers.

For developers choosing a coding agent, the refusal chart adds a concrete reliability question: when a permitted task resembles an unsafe one, does the system finish, recover through a fallback or stop? Hill-Smith and Cameron have turned that question into a metric vendors and customers can inspect rather than discover after deployment.

## Reader comments

Conversation for this story loads after sign-in.