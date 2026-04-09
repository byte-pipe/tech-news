---
title: LLMs Can Get "Brain Rot"!
url: https://llm-brain-rot.github.io/
site_name: hackernews_api
fetched_at: '2025-10-22T11:16:57.995957'
original_url: https://llm-brain-rot.github.io/
author: tamnd
date: '2025-10-21'
description: 'New finding: LLMs Can Get Brain Rot if being fed trivial, engaging Twitter/X content.'
tags:
- hackernews
- trending
---

We propose and test theLLM Brain Rot Hypothesis: continual exposure tojunk web textinduces lasting cognitive decline in large language models (LLMs). To causally isolate data quality, we run controlled experiments on real Twitter/X corpora, constructing junk and reversely controlled datasets via two orthogonal operationalizations:M1(engagement degree) andM2(semantic quality), with matched token scale and training operations across conditions.

Contrary to the control group,continual pre-training of 4 LLMs on the junk dataset causes non-trivial declines (Hedges'g>0.3)on reasoning, long-context understanding, safety, and inflating "dark traits" (e.g., psychopathy, narcissism). The gradual mixtures of junk and control datasets also yield dose-response cognition decay: for example, under M1, ARC-Challenge with Chain Of Thoughts drops74.9 → 57.2and RULER-CWE84.4 → 52.3as junk ratio rises from0%to100%.

Error forensics reveal several key insights:Thought-skipping as the primary lesion:models increasingly truncate or skip reasoning chains, explaining most of the error growth.Partial but incomplete healing:scaling instruction tuning and clean data pre-training improve the declined cognition yet cannot restore baseline capability, suggesting persistent representational drift rather than format mismatch.Popularity as a better indicator:the popularity, a non-semantic metric, of a tweet is a better indicator of the Brain Rot effect than the length in M1.

Together, the results provide significant, multi-perspective evidence thatdata quality is a causal driver of LLM capability decay, reframing curation for continual pretraining as atraining-time safetyproblem and motivating routine "cognitive health checks" for deployed LLMs.
