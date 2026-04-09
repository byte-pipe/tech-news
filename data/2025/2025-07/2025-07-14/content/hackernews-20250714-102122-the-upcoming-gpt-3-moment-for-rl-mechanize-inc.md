---
title: The upcoming GPT-3 moment for RL | Mechanize Inc.
url: https://www.mechanize.work/blog/the-upcoming-gpt-3-moment-for-rl/
site_name: hackernews
fetched_at: '2025-07-14T10:21:22.871990'
original_url: https://www.mechanize.work/blog/the-upcoming-gpt-3-moment-for-rl/
author: jxmorris12
date: '2025-07-14'
description: Mechanize Inc. is developing virtual environments and benchmarks to fully automate the economy.
---

# The upcoming GPT-3 moment for RL

Matthew Barnett, Tamay Besiroglu, Ege ErdilJun 20, 2025

GPT-3 showed that simply scaling up language models unlocks powerful, task-agnostic, few-shot performance, often outperforming carefully fine-tuned models. Before GPT-3, achieving state-of-the-art performance meant first pre-training models on large generic text corpora, then fine-tuning them on specific tasks.

Today’s reinforcement learning is stuck in a similar pre-GPT-3 paradigm. We first pre-train large models, and then painstakingly fine-tune them on narrow tasks in highly specialized environments. But this approach suffers from a fundamental limitation: the resulting capabilities generalize poorly, leading to brittle performance that rapidly deteriorates outside the precise contexts seen during training.

We think RL will soon have its own GPT-3 moment. Rather than fine-tuning models on a small number of environments, we expect the field will shift toward massive-scale training across thousands of diverse environments. Doing this effectively will produce RL models with strong few-shot, task-agnostic abilities capable of quickly adapting to entirely new tasks. But achieving this will require training environments at a scale and diversity that dwarf anything currently available.

How much RL will this take?

Current RL datasets are relatively small. For example, DeepSeek-R1 was trained on roughly 600k math problems, representing about six years of continuous human effort if each task takes five minutes to complete. By contrast, reconstructing GPT-3’s 300-billion-token training corpus would require on the order of tens of thousands of years of human writing at typical human writing speeds.

Incidentally, achieving RL compute expenditure comparable to current frontier-model pretraining budgets will likely require about ~10k years of model-facing task-time, measured in terms of how long humans would take to perform the same tasks. DeepSeek-R1 usedabout 6e23 FLOPduring the RL stage using about 6 years of model-facing task-time. Assuming future training runs use a similar number of epochs and group sizes as DeepSeek-R1, scaling this to about 6e26 FLOP would imply roughly 6k years of model-facing task-time.

It is unclear whether future RL training will involve larger or smaller group sizes or more epochs, especially as we increase the diversity of task distributions. We don’t have much data on this question, so making precise estimates of the required model-facing task-time remains difficult, though ~10k years seems likely to be the correct order of magnitude.

For comparison, the amount of work that this will require of models is on the same order of major projects likeWindows Server 2008,GTA V, orRed Hat Linux 7.1, each estimated to involve on the order of 10k yrs of cumulative human effort.

Expanding RL to this scale is economically efficient. Because compute spending dominates total training expenses, scaling RL to be comparable with pretraining budgets will yield significant performance improvements without substantially increasing overall costs. However, achieving this will require dramatically scaling up RL environments, while still ensuring tasks can be automatically scoreable. Doing so will likely require new approaches to building RL environments.

Replication training

Imagine if every time you wanted to pretrain a language model using next-token prediction, you had to manually create the entire training corpus yourself. Clearly, this would be impractical. Instead, we leverage the enormous amount of existing content such as books, academic articles, blog posts, and Reddit discussions to build training corpora.

Similarly, we suspect the GPT-3 moment for RL will be enabled largely by a paradigm we’re callingreplication training. This proposed paradigm involves tasking AIs with duplicating existing software products, or specific features within them. Simple command-line tools that implement obscure hashing and encryption algorithms are straightforward initial targets, but this approach can easily extend to more complex software, such as websites, professional software, and games.

Each replication task consists of a detailed specification and a reference implementation. The central idea is that AI models are trained to produce an implementation that precisely matches the reference behavior. This clear-cut approach significantly simplifies evaluation, as the grading criteria are objective and direct: either the generated implementation behaves identically to the reference, or it doesn’t.

Though these replication tasks may differ from typical day-to-day software engineering activities, they specifically target critical skills that current AI systems often struggle with. For instance, replicating a complex algorithm (such as a 10k-line-of-code encryption/decryption CLI tools guided by a detailed specification) requires the model to:

* Accurately read and deeply understand detailed instructions.
* Execute instructions meticulously and precisely, without errors.
* Notice earlier mistakes and reliably recover from them.
* Sustain consistent performance over extended periods of time, comparable to month-long human development efforts, where quality is directly rewarded by correctness.
* Demonstrate resilience in the face of hurdles, rather than settling prematurely for a solution that merely looks “good enough.”

We are predicting that replication training will be the next paradigm in AI because it follows naturally from trends we have already observed in AI by leveraging a vast repository of existing human-generated data to create new tasks. Software, like natural language, is abundant on the internet. Thus, replication training provides a scalable approach for efficient and complex task production, moving us closer to AIs that can complete entire software projects end-to-end.

There are, however, several challenges with this approach. Writing effective and comprehensive tests remains a non-trivial task and demands substantial engineering effort. Additionally, replication tasks are somewhat artificial, as exact replication of existing software is not typical in everyday software engineering (though it does come up, such as in software porting, legacy system rewrites, clean-room reimplementations, etc.)

Despite these challenges, we think replication training provides a clear path to scaling RL environments to the immense volumes required for meaningful generalization. It will likely be the key to unlocking RL’s GPT-3 moment, providing the tens of thousands of years of task experience required for robust, task-agnostic performance.

Will replication training be the last paradigm that unlocks full automation of labor? We doubt it. While it could lead to systems capable of autonomously completing highly complex software projects given precise design specifications, we suspect these abilities will still fall short of the open-ended abilities that humans possess. Even if AIs are sophisticated coders, they won’t necessarily be competent at high-level management and agentic planning outside of narrow software domains.

Yet replication training could still serve as a bridge to the next paradigm, in the same way that we needed to invent pretraining first before we could move onto replication training. We are excited about the promise this new paradigm holds for the future.

Interested in what we’re working on?We’re hiringsoftware engineers to work on RL environments.
