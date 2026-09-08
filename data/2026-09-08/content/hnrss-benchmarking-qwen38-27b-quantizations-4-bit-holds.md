---
title: 'Benchmarking Qwen3.8 27B quantizations: 4-bit holds up, 1-bit collapses - Quesma Blog'
url: https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/
site_name: hnrss
content_file: hnrss-benchmarking-qwen38-27b-quantizations-4-bit-holds
fetched_at: '2026-09-08T21:35:06.291295'
original_url: https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/
author: Piotr Migdał
date: '2026-09-08'
published_date: '2026-08-26T00:00:00.000Z'
description: I test Unsloth GGUFs of Qwen3.8 27B (Q4_K_M, UD-Q2_K_XL, UD-IQ1_S) with llama.cpp on GPQA Diamond, IFBench, Terminal-Bench 2.1. Q4_K_M matches BF16 abd fits an RTX 4090.
tags:
- hackernews
- hnrss
---

How much GPU RAM do you actually need to run Qwen3.8 27B without sacrificing quality?

The fullBF16model weighs 55 GB, putting it beyond most consumer hardware.
Yet the 17 GBQ4_K_Mmatches the full model on a popular agentic coding benchmark, Terminal-Bench 2.1. It fits on a 24 GB card such as RTX 4090, still leaving room for about 64k tokens of context.

Compression eventually hits a cliff. At 1 bit, the model performs around random chance on GPQA Diamond, and longer reasoning makes it worse.

## Background

Qwen3.8 27B GGUF quantizations available fromUnsloth on Hugging
Face. So much to choose from! I will check 8-bitQ8_0(29 GB), 4-bitQ4_K_M(17 GB), 2-bitUD-Q2_K_XL(10.7 GB), and the smallest one possible, 1-bitUD-IQ1_S(6.2 GB).

Previously, I investigated the Qwen3.6 27B model, which wasgood at generating SVG pelicans even at 12GB, andmaintained most of its knowledge up to 16GB.
At the same time, in Reddit threads, many complain that all quantizations, even the 8-bit ones, give worse results - with people askingwhy your local LLM feels dumber than it is. Are these complaints grounded?

Measuring token prediction differences (KL-divergence, top-1 predictions) is easy, but it does not tell us whether the model gets worse at solving tasks. Some noise might be irrelevant for solving tasks, as (say) a quantized model generates an answer of precisely the same quality, paraphrased a bit. In other cases, a single different token might be a logical error, or even abruptly end the output.

Download as PNG

70%
80%
90%
100%
6
10
20
30
50 GB
model size on disk
same top-1 token as BF16
UD-IQ1_S
UD-IQ1_M
UD-Q2_K_XL
Q4_K_M
Q8_0
BF16

So, I focus on directly measuring results on popular benchmarks -GPQA Diamond, instruction-followingIFBench, programmingTerminal-Bench 2.1.
First, to replicate official results of the full modelBF16, and then to see how quantization affects results.

I burned around $3,000 onModalGPUs when I ran models withllama.cppusing a build from 16 August 2026 asearlier builds do not work for this model. I could have run it on my own laptop, in principle, but (unlike pelican-generation), these are time-consuming benchmarks.

Note that I useF16KV-cache regardless of model quantization, weighing around 2.3 GB per 32k tokens.

I usedUnsloth quantizations: v2 for the 2-, 4-, and 8-bit models, andv3for the 1-bit models.Unsloth replaced the v2 files on 19 August 2026, so the exact files used for most tests are no longer available.

In short, if you go with a 4-bit quantizationQ4_K_M(17GB), you won’t notice a difference on these benchmarks.
At the same time, the effort setting matters a lot (note that the default isxhigh) - and it is a tricky choice, asit can overthink.

## One-shot tests

The easiest ones are one-shot tests: in this case, graduate-level science GPQA Diamond and instruction-following IFBench.
I run each at three reasoning efforts:low,medium, and the defaultxhigh.

### GPQA Diamond

Download as PNG

70%
75%
80%
85%
90%
95%
100%
10
20
30
50 GB
model size on disk
GPQA Diamond score
xhigh (default)
reported by Qwen
low
medium
UD-Q2_K_XL
Q4_K_M
Q8_0
BF16

First and foremost, I was happy I replicated the official results. Running benchmarks is hard; there are many hidden settings or assumptions that can change the results drastically. Here, on the first go, results were as reported by Qwen.

Second, besides noise (bars areWilson 95% confidence intervals, very conservative for run-to-run noise), there is little difference down to 4-bit; only the 2-bit scores a bit lower.

At the same time, thinking level changed the score dractically. The best results, forxhigh, needed around 8k reasoning tokens.

### IFBench

Download as PNG

60%
80%
10
20
30
50 GB
model size on disk
IFBench followed (strict)
xhigh (default)
reported by Qwen
medium
low
UD-Q2_K_XL
Q4_K_M
Q8_0
BF16

Here, to my great surprise, there is no change between models, down to a decent 2-bit one, weighing less than 11 GB.
Yet, context is even lower, around 4k tokens.

## Agentic coding and Terminal-Bench 2.1

How does it work for programming? Terminal-Bench 2.1 is a standard agentic benchmark, with 89 tasks.
Here I use 3h timeout,xhigheffort. I reserve 98k context.

Download as PNG

reported by Qwen
55%
60%
65%
70%
75%
80%
10
20
30
40
50 GB
model size on disk (log scale)
Terminal-Bench 2.1 passed
UD-Q2_K_XL
Q4_K_M
BF16

Not only does my measurement ofBF16replicate the stated result, but, to my surprise,Q4_K_Mdoes as well.
I accidentally skipped runningQ8_0; yet, in this case, I can safely interpolate between 4-bit and the full model’s values. Running it would be both costly and unnecessary (and would exceed an informal blog post’s budget).
Only at 2-bitUD-Q2_K_XLthings break a bit. A noticeable fall, but stillthe level of Opus 4.7 or Gemini 3.1 Pro. Again, far from frontier, but also - far from useless.

Results are one thing, but what about the process? Do smaller models need more turns, tokens or time to get the result?

Download as PNG

same as BF16
0.8x
1.0x
1.2x
1.4x
1.6x
1.8x
output tokens vs BF16, same solved tasks
UD-Q2_K_XL
Terminal-Bench 2.1
turns
GPQA Diamond
IFBench
Q4_K_M
Terminal-Bench 2.1
turns
GPQA Diamond
IFBench
Q8_0
GPQA Diamond
IFBench

On the same solved tasks,UD-Q2_K_XLtakes as many turns as BF16 but writes about a quarter more tokens.
The number of turns stay roughly the same.

## The 1-bit cliff

Quality drops off a cliff at 1-bit.As with knowledge, quantization damage is nonlinear: first there is no measurable change, then a small decline, and finally a collapse.

While 2-bit quantizations work to some extent, even the best 1-bit model is useless for these benchmarks:

Download as PNG

0%
20%
40%
60%
80%
100%
low
medium
xhigh
reasoning effort (xhigh is the model default)
GPQA Diamond score
Q4_K_M
reported by Qwen
UD-Q2_K_XL
UD-IQ1_M
random guess
UD-IQ1_S

As you may see, the scores are around the random guessing level, with the smallest model being below that threshold.
And longer reasoning makes it worse: atxhigh, scores drop belowlow, as the model more often reasons until the token budget runs out and returns an empty answer.
Sure, Unsloth boasts that:

We also made some smaller UD-1bit quants with UD-IQ1_S being 6.2GB (without MTP) which retain around 72% top-1% accuracy yet being 89% smaller.

But in this case, these remaining 28% matter a lot. And this matches another user’s experience, videQwen3.8 27b 1bit brain damage quant on r/LocalLLaMA.

## Costs

Running these benchmarks isn’t cheap.
Running benchmarks via API is costly, as I know from myprevious benchmarks. Running on rented GPU is much costlier.

Download as PNG

BF16
$804
task containers
$759
Q4_K_M
$502
UD-Q2_K_XL
$243
UD-IQ1_S
$167
UD-IQ1_M
$143
Q4_K_M
$120
UD-Q2_K_XL
$80
BF16
$80
Q8_0
$73
Terminal-Bench 2.1 $2,308
GPQA + IFBench $663

I used Modal, as it is easy to run it from the CLI, including from agents. Other setups may have different pricing. Obviously, this calculation changes if you have your own devices.

It takes some testing to find the optimal way to run models. Usually, instead of using Multi-Token Prediction (MTP), which works well for a single stream, I use a few parallel streams. The key constraint is whether the GPU has enough memory for both the model and the required KV caches.

I used NVIDIA L40S (the same Ada Lovelace chip as the RTX 4090 but twice as much memory: 48 GB), H100 (80 GB) and H200 (141 GB). I would like to share costs to give you a ballpark estimate if you want to run benchmarks yourself.

Download as PNG

$3
$5
$10
20
30
50
80 tok/s
speed per stream
price per 1M output tokens
UD-Q2_K_XL
Q4_K_M
Q8_0
BF16
L40S
H100
H200
8 parallel streams
1 stream, MTP draft
OpenRouter

For comparison,DeepSeek V4 Flash 0731, a 284B model, costs around $0.1/Mtok for output from the cheapest providers on OpenRouter. I am not sure how much of this difference comes from the efficiency of running models at scale, pricing strategy, or popularity.

## Conclusion

If you run experiments locally, usually pick the best model that fits in your GPU memory together with the required context.
For most tasks Unsloth’sQ4_K_Mshould be good enough, without any noticeable difference; for some simpler tasksUD-Q2_K_XLshould be more than fine.
Since people report that KV-caches are more susceptible to quantization, I may test it as well.

But in general, I believe that quantization should be embraced, rather than feared.

And what is your experience? Join the discussion onr/LocalLLaMA,Hacker News, orLinkedIn.

Previous

### Gemini 3.7 Flash, Grok 4.6, GLM-5.3 and DeepSeek V4 Pro joined the frontier

August 2026 on Baba Is Bench: Gemini 3.7 Flash, Grok 4.6 and DeepSeek V4 Pro 0813 each beat their predecessor while costing 3-20x less. For open-weight GLM-5.3 and Qwen3.8 progress is gradual.

Next

### OpenAI Codex pricing: the $270 PR a $200/month sub covers daily

A buyer’s guide to OpenAI Codex for individuals, teams, and enterprises. Includes comparisons with Claude Code.

Related

### Do Qwen3.6 27B quantizations break the pelican?

We tested Qwen3.6 27B quantizations by Unsloth on Hugging Face, with pelicans on bikes, gears, Terminal-Bench 2.1, and AIME-120.