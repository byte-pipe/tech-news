---
title: Context Language Models | DAIR.AI Academy | DAIR.AI Academy
url: https://academy.dair.ai/papers/context-language-models-2609.37725
site_name: tldr
content_file: tldr-context-language-models-dairai-academy-dairai-acad
fetched_at: '2026-10-04T07:00:47.660887'
original_url: https://academy.dair.ai/papers/context-language-models-2609.37725
date: '2026-10-04'
description: Rulin Shao, Hamish Ivison, Nathan Lambert, Mike Lewis, Wen-tau Yih, Luke Zettlemoyer, Pang Wei Koh and colleagues at the University of Washington and Meta Super
tags:
- tldr
---

← All papers
  / 
 
Oct 1, 2026
Agents

# Context Language Models

Rulin Shao, Shannon Zejiang Shen, Junjie Oscar Yin, Yuetai Li, Minheng Wang, Hamish Ivison, et al.

Chat with Paper
First page
The curator’s take

Rulin Shao, Hamish Ivison, Nathan Lambert, Mike Lewis, Wen-tau Yih, Luke Zettlemoyer, Pang Wei Koh and colleagues at the University of Washington and Meta Superintelligence Labs (with MIT) introduce Context Language Models (CLMs), which manage their own context by treating it as a file they can edit with Bash, replacing harness-defined compaction, offloading and retrieval rules.

## Ask this paper

Question about this paper
Ask in Paper Chat
Key points
01

Context as a file. The live context is mirrored to storage the model can write; any edit is synced back for the next turn. Multiple agent contexts can coexist as files, which extends the design to swarms and subagents.

02

Zero-shot results. Applied to existing models, CLMs reach 11.4% higher accuracy with 21.5% fewer FLOPs on BrowseComp-Plus, 5% higher scores with 59% fewer FLOPs on 12-hour EdgeBench, and 65% more improvement at equal compute on a 24-hour six-repository agent-swarm task.

03

Learning strategies. Natural-language instructions evolved by a skill-optimization loop raise held-out accuracy on ContextBench by up to 35.9 points; online RL with a success-gated efficiency advantage improves Qwen3.5-9B on BrowseComp-Plus by 47.6% while using 12% fewer FLOPs.

04

Serving cost. Edits in the middle of the context break prefix caching, so the paper measures prefix-reuse FLOPs and adds Suffix Cache Reuse, which cuts server-side compute by 35% against standard SGLang at matched performance.

05

Stated risk. A model-editable context is a new channel through which injected or self-written instructions can persist across turns.

Abstract

We introduce Context Language Models (CLMs), language models that natively manage their own context. We implement this by treating the context as a file and allowing the model to make unrestricted updates to this file. This allows the model to learn what is most important to maintain in context, and naturally extends to multi-agent systems where multiple agent contexts coexist as files. Building CLMs zero-shot with existing models outperforms SOTA context management strategies across a variety of tasks: 11.4% higher accuracy with 21.5% fewer FLOPs on BrowseComp-Plus, 5% higher scores with 59% fewer FLOPs on 12-hour EdgeBench, and 65% greater improvement with the same compute on a 24-hour multi-repository agent-swarm task. Moreover, by shifting context management from external harness control to intrinsic model behavior, CLMs naturally enable both in-context and parametric learning of context-management strategies. We show that CLMs can be steered with natural-language instructions evolved through a standard skill-optimization loop, improving held-out accuracy by up to 35.9 points on a context-management task while reducing compute. We also introduce an online reinforcement learning method for CLMs, improving Qwen3.5-9B performance on BrowseComp-Plus by 47.6% while using 12% fewer FLOPs. Finally, we co-design Suffix Cache Reuse for CLM serving, further reducing server-side compute by 35% relative to standard SGLang at matched performance.

Every Monday

##### Get next week’s papers.

Subscribe on Substack