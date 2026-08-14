---
title: Introducing Toast 1
url: https://www.mixedbread.com/blog/toast-1
site_name: hnrss
content_file: hnrss-introducing-toast-1
fetched_at: '2026-08-15T04:03:00.954722'
original_url: https://www.mixedbread.com/blog/toast-1
author: Mixedbread Team
date: '2026-08-14'
description: Meet Toast 1, Mixedbread's search agent for knowledge-intensive tasks, matching or outperforming Claude Opus 5 and GPT-5.6 Sol while being up to 10× cheaper and 12× faster.
tags:
- hackernews
- hnrss
---

All posts

# Introducing Toast 1

Research
Product
MB
Mixedbread Team
·
August 13, 2026
·
6 min read
Copy to clipboard

Toast 1, our first specialised search agent, is available today. It provides frontier search quality, matching or outperforming Claude Opus 5 and GPT-5.6 Sol while being up to 10× cheaper and 12× faster. It performs best with Mixedbread Search, but it can work with any search backend.

Today, frontier models are now able to perform real knowledge work. They can reason, analyse, and find information in complex document collections. But they are also the most expensive models in the stack. As intelligence is increasingly metered, the need for specialised agents able to match their capabilities at a fraction of the cost is greater than ever.

Toast 1 can run as a standalone specialized retrieval agent, or as one of many subagents your frontier model already knows how to rely on. It fully takes over the search loop: given an initial query, it decomposes it into subqueries, gathers evidence, inspects sources, and curates the relevant context before returning it. This lets your agent spend its context and compute on the task that requires a generalist, frontier-level model: reasoning, acting, and producing the final answers.

Waterfall trace of a Toast 1 agentic search: 16 tool calls across 3 rounds answering an employment-rate comparison query in just over 5 seconds. Expand the trace, then select a step to see the sub-query, grep pattern, or plan the agent produced at that point.
“
How did the employment rate change in retail compares to the healthcare sector?
”
16
 tool calls · 
3
 rounds ·
 
5.33s
 ·
 
view trace

## Pareto Optimal SearchLink to section

This specialisation of agentic labor results in considerably cheaper search, but also in better end-to-end results on many realistic tasks. We found that Toast 1 establishes a new Pareto frontier across agentic workloads across cost per task and speed per task.

### Financial Analysis: OfficeQA Pro V2Link to section

OfficeQA Pro V2,released by Databricks, evaluates answer correctness across 90 questions in realistic, complex enterprise financial situations.

GPT‑5.6 Sol with Toast 1 made available as a sub-agent within Codex reaches 70% answer correctness at approximately $1.15 per task: that is the highest score among the systems evaluated by Databricks in the OfficeQA v2 release, establishing new state-of-the-art performance in both quality and efficiency.

Scatter plot of answer correctness versus cost per rollout on OfficeQA Pro V2, log-scale cost. GPT-5.6 Sol running in Codex with Toast 1 as a sub-agent reaches 70 percent correctness at about $1.20 per task, above the previous Pareto frontier from the Databricks evaluation, where Claude Fable 5 on Databricks Genie reaches 60 percent at about $4.

Cost–quality Pareto on OfficeQA Pro V2

20
%
30
%
40
%
50
%
60
%
70
%
$0.1
$0.2
$0.5
$1
$2
$5
$10
$20
$50
Answer correctness
Cost per rollout (log scale)
GPT-5.6 Luna
GPT-5.6 Terra
Claude Fable 5
GPT-5.6 Sol
Kimi K3
GLM 5.2
Sonnet 5
GPT-5.6 Luna
(Codex)
GPT-5.6 Terra
(Codex)
GPT-5.6 Sol
(Codex)
Sonnet 5
(Claude Code)
Claude Fable 5
(Claude Code)
GPT-5.6 Sol Low
(Codex + Toast 1)
GPT-5.6 Sol High
(Codex + Toast 1)
Databricks Genie
Model provider harness
Pareto frontier (Databricks)
Codex + Toast 1
Answer correctness vs. cost per rollout on OfficeQA Pro V2. Genie and harness numbers as reported by Databricks; Codex + Toast 1 runs are ours. Shaded region sits under the previous Pareto frontier.

By comparison, the previous best performer, Claude Fable 5 on Databricks Genie, reaches 60% correctness at approximately $4 per task, while GPT-5.6 Sol within Codex without Toast 1 only reaches 33% correctness.

This improvement stems from reformulating the economics of evidence gathering. Toast 1's specialization allows it to produce high-quality, token-efficient evidence packages, leaving ample resources for the reasoning process to reach the final answer.

### Legal Agentic Benchmark - Firm KnowledgeLink to section

Harvey LAB's Law Firm Knowledge benchmarkseeks to evaluate how well an agent can search and use institutional legal knowledge at large, realistic scales.

Legal work, by nature, is context-heavy. You cannot outargue someone with access to better, more relevant precedents and details. But it is also noisy: many situations are similar but vary by simple details, making it tricky to collect high quality evidence packages without numerous false positives.

On a randomly selected subset of 33 tasks,1we found that GPT-5.6 Sol's answer quality remained constant across search methods.

Bar chart of total tokens used on the Harvey LAB firm-knowledge benchmark. A vanilla agent uses 80.6 million tokens at 21.7 turns per task. Adding Mixedbread Search cuts that by 42 percent to 47 million tokens at 14.6 turns per task. Adding Toast 1 as a subagent cuts it by another 51 percent to 23 million tokens at 11.2 turns per task. All three configurations reach the identical task score of 55, so the end result is the same performance with 3.5 times fewer tokens.

3.5× fewer tokens with the same performance.

Harvey LAB firm-knowledge benchmark (33 tasks) — all settings are equal except the retrieval stack

tokens / benchmark
80.6
M
score 55
Vanilla agent
21.7
 turns / task
47.0
M
score 55
+ Mixedbread Search
14.6
 turns / task
23.0
M
score 55
+ Toast 1 subagent
11.2
 turns / task
−42% tokens
−51% tokens
Tokens are totals across the 33-task benchmark; turns are agent loop iterations per task. All three configurations reach the identical task score of 55.

However, increasing search quality drastically increased token efficiency: replacing the vanilla agent's filesystem search with Mixedbread Search cut token usage from 80.6M to 47M at an identical task score. Subsequently adding Toast 1 as its dedicated search subagent reduced it further to 23M, and allowed it to finish in half the turns required by vanilla agent.

The introduction of a Mixedbread Search-powered Toast 1 preserved answer quality, while consuming 3.5× fewer tokens, leading to a cost reduction of over 60%. Toast 1 frees up the context window of frontier models to let them spend their tokens on reaching the right answer.

## Demo: Dig Deep Into Dwarkesh's PodcastLink to section

Benchmarks and numbers can only tell one part of the story. To truly understand how Toast 1 works, there is no better way than watching it search in action. At Mixedbread, we really enjoyDwarkesh's podcast, and thought being able to search deep into its transcripts would be fun.

You can try it yourselfhere.

## Frontier Class RetrievalLink to section

Although it is a capable subagent for complex tasks, Toast 1 is also a capable standalone model, trained specifically for deep search. It represents the next step of our co-design approach behind our embedding models and Silo: the model, agent harness, and retrieval primitives are designed to work together.2

Retrieval quality versus cost and latency per query on BrowseComp Plus, OfficeQA Pro, and LongSeal. Toast 1 matches or approaches the best frontier-model sweeps on each benchmark while costing a fraction per query and answering in about 8 to 10 seconds, far faster than the frontier sweeps.
BrowseComp Plus
OfficeQA Pro
LongSeal

BrowseComp Plusquality versuscost

0.30
0.45
0.60
0.75
0.90
$0.01
$0.03
$0.1
$0.3
$1
NDCG@10
Cost per query (log scale)
DeepSeek
Kimi K3
Qwen
GLM
Haiku 4.5
Sonnet 5
Opus 5
GPT-5.6 Luna
GPT-5.6 Terra
GPT-5.6 Sol
Toast 1
(
RRF ×3
)
Cost
Latency
Cost per query at list prices with prompt caching; latency is p50 per query. Lines show each model's Pareto-efficient reasoning sweep.

On a variety of deep search benchmarks, it reaches frontier model performance, standing in the same league as GPT-5.6 Sol and comfortably outperforming models such as Kimi K3 or GLM-5.2.

It remains lightweight in doing so. A standard Toast 1 run costs approximately0.016−0.016 -0.016−0.023 per query and has an eight-second median latency. Our highest-quality fusion configuration costs approximately0.05−0.05 -0.05−0.07 per query and has an eleven-second median latency. In practice, among the systems in our evaluation that reached similar performance, Toast 1 was 7–11× cheaper and considerably faster: Frontier-model retrieval agents took between 20 seconds and four minutes on the same evaluation.

## Availability and PricingLink to section

Toast 1 is available immediately through the Mixedbread API at thediscounted launch pricing:

* $0.30 per million input tokens
* $0.036 per million cached input tokens (cache writes are free)
* $0.72 per million output tokens

Mixedbread search invoked by Toast 1 ispriced at a special rate.

### With Your Existing Retrieval StackLink to section

Toast 1 was co-designed with Mixedbread Search's primitives and will be at its strongest performance with it. But we put special care in ensuring that it remains backend agnostic: it can run over your existing retrieval indexes, and does not require migrating your existing backend. We conducted thorough testing to ensure that Toast 1 remains competitive with the performance of frontier models in similar conditions at a fraction of the cost and latency, no matter the provided index.

You can use Toast 1 with ourChat Completions APIand add it as a retrieval tool to your existing agentic workflows in just a few minutes. Here is agolden harness you can use directly.

### With Coding AgentsLink to section

Let your coding agents handle the integration withnpx skills add mixedbread-ai/skills. Or use Toast 1 directly as a subagent with ourOpenCode integration.

### With Your Mixedbread StoresLink to section

Python
TypeScript
Copy to clipboard
from
 mixedbread 
import
 Mixedbread

client 
=
 Mixedbread()

results 
=
 client.stores.search(

 store_identifiers
=
[
"legal-documents"
],

 query
=
"does the MSA allow assignment on a change of control?"
,

 search_options
=
{

 "agentic"
: 
True
, 
# enable Toast 1

 },

)

Get an API keywith $5 in included credits to try it out.

## FootnotesLink to section

1. We evaluated a randomly selected subset of 33 tasks to make repeated comparative runs tractable. Every configuration used the same tasks and evaluation setup; only the retrieval stack changed.↩
2. Toast 1 is part of a growing body of work on specialised search agents, alongsideSID-1and Chroma'sContext-1. While each takes a different approach, they share the goal of bringing frontier-level retrieval to production at lower cost and latency.↩

mxbai-rerank-v3.1-listwise
How PlanetScale Powers the Mix...