---
title: Magic
url: https://magic.dev/blog/pretraining
site_name: tldr
content_file: tldr-magic
fetched_at: '2026-09-10T07:20:53.263997'
original_url: https://magic.dev/blog/pretraining
date: '2026-09-10'
description: Research update on compute-efficient pretraining and scaling to trillion-parameter models.
tags:
- tldr
---

# >10x More Efficient Pretraining

Research update on compute-efficient pretraining and scaling to trillion-parameter models.

Magic Team
, on 
September 8, 2026

Frontier pretraining is said to be a big-lab-only game. We don’t have 100k chips yet, so there’s only one way: algorithmic efficiency. After compounding for … a while …, our pretraining recipe is now >10x more compute-efficient than that of leading open-weight base models.

We match DeepSeek V4 Pro Base using ~50x fewer FLOPs – that’s around half of GPT3’s pretraining compute, or ~$0.5M on GB200. We continued scaling 10x (~$4M) and meaningfully outperformed all publicly available open base models on perplexity evals. By the scaling laws in Figure 1, training a model this capable would cost >$100M under DeepSeek V4 Pro’s recipe (and this is ignoring how much data exists). Of course, we won’t stop scaling there.

We believe pretraining, agentic RL, and long-context are sufficient to build superhuman coding agents and automate AI R&D. We started withlong-context. Today’s blog post is about pretraining.

bits per byte (lower is better)
Private Code Repos
i
Lower bits per byte is better. Training compute is in FLOPs on a logarithmic axis.
 The curve fits our current recipe; the dashed segment is a projection beyond the largest run.
0.185
0.204
0.223
0.242
0.261
10
21
10
22
10
23
10
24
10
25
DeepSeek V4 Flash: 0.206 bpb
DeepSeek V4 Pro: 0.202 bpb
Kimi K2: 0.205 bpb
Nemotron 3 Ultra: 0.203 bpb
V5 e21: 0.246 bpb
V5 e22: 0.222 bpb
V5 e23: 0.202 bpb
V5 e24: 0.194 bpb
29x
DSv4 Flash
48x
DSv4 Pro
31x
Kimi K2
47x
Nemotron 3 Ultra
Heldout Research Papers
i
Lower bits per byte is better. Training compute is in FLOPs on a logarithmic axis.
 The curve fits our current recipe; the dashed segment is a projection beyond the largest run.
0.36
0.41
0.46
0.52
0.57
10
21
10
22
10
23
10
24
10
25
DeepSeek V4 Flash: 0.415 bpb
DeepSeek V4 Pro: 0.404 bpb
Kimi K2: 0.421 bpb
Nemotron 3 Ultra: 0.406 bpb
V5 e21: 0.527 bpb
V5 e22: 0.463 bpb
V5 e23: 0.407 bpb
V5 e24: 0.383 bpb
24x
DSv4 Flash
45x
DSv4 Pro
41x
Kimi K2
35x
Nemotron 3 Ultra
Reasoning on heldout math problems
i
Lower bits per byte is better. Training compute is in FLOPs on a logarithmic axis.
 The curve fits our current recipe; the dashed segment is a projection beyond the largest run.
0.53
0.64
0.76
0.87
0.98
10
21
10
22
10
23
10
24
10
25
DeepSeek V4 Flash: 0.710 bpb
DeepSeek V4 Pro: 0.678 bpb
Kimi K2: 0.695 bpb
Nemotron 3 Ultra: 0.619 bpb
V5 e21: 0.890 bpb
V5 e22: 0.770 bpb
V5 e23: 0.647 bpb
V5 e24: 0.587 bpb
72x
DSv4 Flash
127x
DSv4 Pro
58x
Kimi K2
15x
Nemotron 3 Ultra
6·N·D training FLOPs
Figure 
1
: 
Pretraining scaling laws against training compute, comparing to leading available open-weight base models
.
 

1

We measured bits-per-byte loss (a metric that normalizes out differences in tokenizers) on heldout data and fit ascaling lawto project how much compute is needed to reach a given level of capability. Better training compute efficiency means stronger models at all budgets.

We evaluated the latest available open-weight base models2from DeepSeek, Moonshot (Kimi), and NVIDIA. Base models for Claude, Gemini, GPT-n, and many others aren’t openly available, butKimi K3andMeta’s Muse Sparkindicate a 2.5x and 3.3x gain over Kimi K2, respectively. We evaluated logprobs for open models in both vLLM and SGLang on both GB200 and GB300 and foundissueswith somebackendsin the process. For further confirmation, we partnered withFireworksto verify baseline logprobs in their in-house inference engine. Since models can learn their training parser’s characteristics, we built our eval sets using a different parser/OCR than the one our pretraining pipeline uses.

## Evaluating generalization

To measure generalization, we evaluated loss on heldout data (Figure 1). Our code evals consist of our own codebase and private codebases we acquired from other startups. For reasoning evals, we generated CoT and step-by-step walkthroughs to heldout, private math problems using Kimi K3 and filtered for correct answers. For text and research, we used recent, low-citation research papers. We removed vendored OSS code and any document with a matching 96-character window of normalized text or Jaccard similarity above a sensitive threshold compared to our training data.3

## Evaluating knowledge

In addition to generalization, we are interested in testing our model’s knowledge in key domains to identify gaps in our dataset. For example, we can decompose our heldout research text eval set by subject.

bits per byte (lower is better)
Heldout Computer Science Papers
i
Lower bits per byte is better. Training compute is in FLOPs on a logarithmic axis.
 The curve fits our current recipe; the dashed segment is a projection beyond the largest run.
0.37
0.43
0.48
0.54
0.59
10
21
10
22
10
23
10
24
10
25
DeepSeek V4 Flash: 0.450 bpb
DeepSeek V4 Pro: 0.437 bpb
Kimi K2: 0.458 bpb
Nemotron 3 Ultra: 0.434 bpb
V5 e21: 0.548 bpb
V5 e22: 0.481 bpb
V5 e23: 0.425 bpb
V5 e24: 0.400 bpb
62x
DSv4 Flash
120x
DSv4 Pro
108x
Kimi K2
69x
Nemotron 3 Ultra
Heldout Engineering Papers
i
Lower bits per byte is better. Training compute is in FLOPs on a logarithmic axis.
 The curve fits our current recipe; the dashed segment is a projection beyond the largest run.
0.359
0.409
0.458
0.507
0.556
10
21
10
22
10
23
10
24
10
25
DeepSeek V4 Flash: 0.413 bpb
DeepSeek V4 Pro: 0.403 bpb
Kimi K2: 0.421 bpb
Nemotron 3 Ultra: 0.405 bpb
V5 e21: 0.517 bpb
V5 e22: 0.456 bpb
V5 e23: 0.405 bpb
V5 e24: 0.383 bpb
26x
DSv4 Flash
48x
DSv4 Pro
49x
Kimi K2
38x
Nemotron 3 Ultra
Heldout Math Papers
i
Lower bits per byte is better. Training compute is in FLOPs on a logarithmic axis.
 The curve fits our current recipe; the dashed segment is a projection beyond the largest run.
0.32
0.37
0.43
0.48
0.54
10
21
10
22
10
23
10
24
10
25
DeepSeek V4 Flash: 0.365 bpb
DeepSeek V4 Pro: 0.354 bpb
Kimi K2: 0.367 bpb
Nemotron 3 Ultra: 0.360 bpb
V5 e21: 0.492 bpb
V5 e22: 0.426 bpb
V5 e23: 0.367 bpb
V5 e24: 0.342 bpb
12x
DSv4 Flash
21x
DSv4 Pro
16x
Kimi K2
22x
Nemotron 3 Ultra
Heldout Physics Papers
i
Lower bits per byte is better. Training compute is in FLOPs on a logarithmic axis.
 The curve fits our current recipe; the dashed segment is a projection beyond the largest run.
0.38
0.43
0.49
0.54
0.60
10
21
10
22
10
23
10
24
10
25
DeepSeek V4 Flash: 0.433 bpb
DeepSeek V4 Pro: 0.422 bpb
Kimi K2: 0.440 bpb
Nemotron 3 Ultra: 0.425 bpb
V5 e21: 0.552 bpb
V5 e22: 0.487 bpb
V5 e23: 0.431 bpb
V5 e24: 0.406 bpb
16x
DSv4 Flash
29x
DSv4 Pro
29x
Kimi K2
24x
Nemotron 3 Ultra
6·N·D training FLOPs
Figure 
2
: 
Effective-compute per research area
.
 

By collecting granular buckets of content (e.g. documentation of a particular software tool or key papers in alignment research) we can get even more precise signals. Unlike for our generalization eval, we don’t want to fully remove much of this information (e.g. key papers in a field) from the pretraining corpus, but we still need to avoid rewarding sequence memorization4. To do this, we reworded/summarized these documents using a third-party frontier LLM. To avoid overfitting to granular evals, we created and evaluated them once per model generation; the ones below were made last week.

Magic’s goal is to build the best model for coding and autonomous AI R&D. To intentionally balance data mixing trade-offs, we also evaluate domains we deprioritize (e.g. facts about notable people, local news, or sports/events).

Our recipe vs.
Best open model per eval
effective-compute multiplier vs.
 
best open model per eval
Eval multipliers are ranked within each panel on a logarithmic axis. Values above 1 favor our current recipe; values below 1 favor the baseline.
0.01x
0.1x
1x
10x
100x
SWE & AI R&D
SWE
AI R&D
0.01x
0.1x
1x
10x
100x
Local news, world knowledge & law
Local news
World knowledge
Law
Figure 
3
: 
Effective-compute multiplier across domains
.
 

We fit scaling laws on eval sets across 167 domains and show compute efficiency gains per dataset.

## No shortcuts

In late 2024, we trained asmall dense modelwith an architecture designed for very long context windows. Our initial pretraining scale-ups kept blowing up in a wide variety of ways. We learned quickly that we had to build a stable foundation first. Smooth convergence, low-precision training quality equivalent to FP32, fast and stable infra, correct hyperparameter scaling rules. And most importantly: hunt the bugs.

Once we had that in place, we needed to find enough compute efficiency improvements to close the gap to the frontier with less compute. We had a few big bets to start with, but our progress ended up being the multiplicative result of tens of changes across model architecture, optimizer, training objective, and data curation.

NanoGPT speedrunsprovide a fast feedback cycle to evaluate new ideas, but we found that many things that improve tiny models don’t improve big models. Similarly, we found that some features present in most LLMs can bedeletedwithout harming large scale performance.

To evaluate each model, optimizer, or data change, we train 3 models spanning 2 orders of magnitude of compute. We consider a change worth keeping if its power law fit suggests it will help at scale. Every few weeks, we scaled up to 1/10th of our hero scale and every few months we ran a full-scale hero run (V3, V4, V5 in Figure 4).

Compute efficiency relative to V2, with competitor reference lines.
1x
10x
100x
1000x
V2
Late '24
V3
Early '26
V4
July '26
V5
Sep '26
Compute efficiency
vs. our V2
Nemotron 3 · 24x
Kimi K2 · 10x
DSv4 Pro · 5.6x
x1.9
x11
x24
505x vs V2
Figure 
4
: 
Acceleration of our pretraining research progress
.
 

To sanity check how pretraining loss translates to post-RL performance, we ran a short math RL run with a 16k CoT budget (Figure 5). All of our RL starts directly from the base model without SFT or distillation.

Math pass rate over RL training compute, with competitor reference lines.
0%
25%
50%
75%
100%
0.01%
0.1%
1%
10%
100%
RL compute (as % of the model's
own pretraining FLOPs)
Pass rate
GPT-6 Astra
 ·
 
100%
Claude 5.1
 ·
 
98%
Muse Spark 1.3
 ·
 
88%
Gemini 3.8
 ·
 
83%
Kimi K3
 ·
 
75%
Grok 4.6
 ·
 
71%
DSv4 Pro
 ·
 
65%
Inkling
 ·
 
50%
Qwen 3.8
 ·
 
45%
GLM-5.3
 ·
 
45%
Nemotron 3
 ·
 
27%
V5 (e24) · 72%
V5 (e23) · 31%
Figure 
5
: 
Pass@1 on heldout competition math problems during low-compute RL
.
 

5FLOPs are 6·N·D, as in Figure 1.

## What’s next

Our pretraining and long-context work is now quite mature. We’ll now scale long-horizon RL, training agents to keep learning after deployment through long-context. We’re also putting significant work towards alignment training techniques that present robust theoretical properties. And last but not least, we look forward to releasing the thing!

Concrete problems we’re tackling include:

* Exploration and credit assignment in long-horizon RL (and systems work to scale up).
* Alignment training against narrowlyelicited latent knowledge.6
* Further improvements to pretraining.

We are likely the smallest team in the world training trillion parameter models. The impact a single person with strong judgement can have has never been higher. If you want to help build aligned superintelligence,consider joining.

## Footnotes

1. We report 6·N·D in place of exact training flops, where N is the activated parameter count and D is the pretraining token count each report states. Sequence-dimension (e.g. attention, etc.) cost makes up a minority of the FLOPs for these (and our) models but depends on the exact sequence length distribution used. These aren’t reported for all public models, so we opted for the 6·N·D approximation to avoid guessing. The “6” appears because (add+mul) * (fwd+bwd*2). We derived active parameter counts by downloading the checkpoints’ safetensors headers from HuggingFace, reading each tensor’s shape, and adding up the sizes of all active parameters except token embeddings and MTP heads. 6·N·D for each model:ModelND6·N·DCurrent_e24 (ours)--1.63e24Current_e23 (ours)--1.58e23Current_e22 (ours)--1.12e22V4 (ours)--1.91e24V3 (ours)--3.85e24V2 (ours)--7.20e23DeepSeek V4 Pro48,852,265,05433T9.67e24DeepSeek V4 Flash13,270,025,81032T2.55e24Kimi K231,687,072,76815.5T2.95e24Nemotron 3 Ultra54,985,076,73620T6.60e24Sources: Kimi K2: 31.6B params, 15.5T tokens (tech report, Section 2.5). DeepSeek V4 Flash: 13.2B params, 32T tokens (tech report, Section 4.2.2) and DeepSeek V4 Pro: 48.8B params, 33T tokens (Section 4.2.2). Nemotron 3 Ultra: 55B params, 20T tokens (tech report, abstract).↩
2. “Base models” are pretrained models that have not yet undergone reinforcement learning, SFT, or other post-training. They are highly sensitive to prompting, making sampling-based evals unreliable. Instead, we measured bits-per-byte loss on heldout data, which does not suffer from prompt sensitivity and smooths measurement of otherwiseemergent abilities. As a side note, we were surprised that Nemotron 3 outperforms DeepSeek V4 Pro across the board but found this to be consistent across domains and inference engines. This might indicate that Nemotron’s weak performance on benchmarks after RL is due to weaker post-training, but the pretrain was ahead of Chinese open-weight competitors.↩
3. We can of course only decontaminate evals for our own models, not open-weight models. This means some of the data in our heldout internet-based evals may naturally be in their training data, but any contamination on their side would favor open models, not ours.↩
4. There are some outliers where we suspect source memorization to distort results. For example, we find that Nemotron has memorized specific numbers and phrases from source documents in the medicine/health world knowledge category and predicts these shockingly well even after LLM rewriting of the documents. We still included these outliers in our plot. All knowledge evals were created after our current-generation pretraining run started training and the vast majority of categories are new (i.e. they had no direct feedback loop into the run), but knowledge evals intentionally target semantic content that we expect appears frequently (and intentionally so) in anyone’s training data.↩
5. We evaluated pass rate on a private heldout competition math eval (400 problems) that’s harder than AIME. Baseline models presumably use orders of magnitude more RL compute. The e24 model’s AIME26 pass@1 first crossed 90% (and 100% pass@16) at ~0.2% of its pretraining compute budget, using just over 6k CoT tokens on average, and displays continued log-linear climbing. We report performance on a heldout dataset instead as we found AIME to be contaminated in some third-party models.↩
6. We plan to release an updatedAGI Readiness Policycovering deployment gates, safety requirements during RL training, and how we approach alignment research.↩