---
title: A phone maker now has the world’s top open-weight AI model
url: https://thenextweb.com/news/xiaomi-mimo-v2-6-open-weight-model-anthropic-distillation
site_name: tldr
content_file: tldr-a-phone-maker-now-has-the-worlds-top-open-weight-a
fetched_at: '2026-09-24T15:44:20.010253'
original_url: https://thenextweb.com/news/xiaomi-mimo-v2-6-open-weight-model-anthropic-distillation
author: Ana Maria Constantin
date: '2026-09-24'
published_date: '2026-09-22T18:25:00+00:00'
description: Xiaomi's MiMo-V2.6-Pro tops Artificial Analysis' open-weight index at $0.13 a task. It was trained in under six days for $2.62m.
tags:
- tldr
---

Credit: Xiaomi

Frontier intelligence, all the modalities, built in public.

Xiaomi opened itsMiMo-V2.6 announcementwith that line on Tuesday. The phone and electric car maker released two open-weight models, Pro and Flash, under an MIT licence. The weights are on Hugging Face.

The benchmark firmArtificial Analysisscores MiMo-V2.6-Pro at 46 on its Intelligence Index. That is first of the 114 models in its class. It is the highest score any open-weight model has reached, and the firm also rates it the cheapest model it tracks, at $0.13 per task.

## What the model is

Pro is a sparse mixture-of-experts model. It has 1.02 trillion parameters in total, of which 42 billion are active for any given token, which is what keeps it cheap to run at that size.

It takes text, images, audio and video, and holds a million tokens of context. That is enough for a long repository, a full tool trace, or several sessions of an agent’s working memory.

Xiaomi charges $0.435 per million input tokens and $0.87 per million output. Anthropic cutClaude Opus 5.5to $4 and $20 on the same day.

Pro passes Moonshot’sKimi K3, Xiaomi says. It also passes Alibaba’sQwen3.8 Max. Those two have traded the open-weight lead for most of this year.

Both models are live now. They run in Xiaomi’s AI Studio, in its MiMo Code and MiMo Desktop apps, through its own API platform, and on OpenRouter. Anyone who would rather host the weights themselves can pull them from Hugging Face.

There is a third variant, Pro-UltraSpeed, which Xiaomi says generates up to 20 times faster than Pro at the same quality. It costs ten times as much per token, at $4.35 in and $8.70 out.

## Six days and $2.62m

The gains came from one large reinforcement learning run. Xiaomi streamed it live as it happened.

Pro and Flash each completed 30 training steps over roughly 750,000 trajectories, in under six days. Pro cost about $2.62m to train that way. Flash cost about $0.85m.

On DeepSWE, a held-out software engineering benchmark, Xiaomi reports Pro climbing from 58.4 to 72.57 across the run. Flash went from 48.8 to 65.68.

Most labs run separate training jobs per domain. Xiaomi mixed coding, general agents, visual work and cybersecurity into one, so that gains in each would reinforce the others.

It also details its defences against reward hacking. Early agents, it found, solved assigned bugs by fetching the fix from a later version of the package rather than writing it. Xiaomi stripped build caches and future Git history from the training environments and ran a dedicated agent to hunt for remaining loopholes.

## Flash is the one most companies will use

Pro will get the headlines. Flash is the one that ends up in production.

It costs $0.14 and $0.28 per million tokens, roughly a third of Pro. It keeps the same million-token context and the same multimodal input.

On most of Xiaomi’s own agent benchmarks it trails Pro by four points or fewer. DeepSWE is 67.9 against 71.9, AutomationBench 52.3 against 53.1, JobBench 61.2 against 62.0.

On one cybersecurity test, CyberGym, Flash beats Pro, 95.1 to 94.0. Pro is well ahead on the other three cyber benchmarks, so that is a quirk rather than a pattern.

## It is not a clean sweep

Xiaomi’s own tables show where it loses. Claude Opus 5 beats Pro on DeepSWE and on ProgramBench. On Terminal Bench 4.0 the gap is wide: 49.0 against 34.9, with GPT-6 Astra at 59.6.

The index says the same. Artificial Analysis has Opus 5.5 at 58 against MiMo’s 46. Xiaomi leads the open-weight field, not the field.

Pro performs on par with Opus 5 and GPT-5.6 Sol across most agent benchmarks, Xiaomi says. That claim is the company’s own, from its own testing. The 46 is not.

## The unusual part is what else it published

An open-weight release normally means the weights and a paper. Xiaomi published considerably more.

Alongside the two models came the full technical report, the end-to-end reinforcement learning framework, more than 7,000 RL task environments with automatic graders, a set of composable mini-harnesses, and a smaller model distilled from MiMo’s training runs.

The tasks cover software development, cybersecurity, office work and web design. Roughly a thousand more cover music composition.

Xiaomi has also published the reward design, the hyperparameters, the data mixtures and the costs. The stated point is reproducibility, and researchers are invited to check the result.

That may matter more than the ranking. Leaderboard positions last weeks. A published RL framework that smaller labs can run on smaller models changes what a well-funded research team can attempt.

## Why the price is the real story

Rankings turn over fast. DeepSeek held thecheapest-to-run titlein August, and Kimi K3 held the open crown in July.

The operating cost gap moves more slowly. A company running millions of agent calls is choosing between $0.87 per million output tokens and $20 for Opus 5.5. For a coding assistant or a document pipeline burning hundreds of thousands of tokens a job, that decides more procurement than a benchmark does.

Xiaomi is also one of seven Chinese labs Anthropic named ina threat reporton 10 September, accusing them of routing requests through Claude to harvest its output. Xiaomi has not responded to that allegation.

What it has done is hand anyone who wants to test its claims the weights, the code, the environments and the bill.

## Get the TNW newsletter

Get the most important tech news in your inbox each week.