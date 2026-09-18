---
title: SemIf — local decisions in your browser
url: https://openjev.com/
site_name: hackernews_api
content_file: hackernews_api-semif-local-decisions-in-your-browser
fetched_at: '2026-09-18T14:48:04.254008'
original_url: https://openjev.com/
author: ilreb
date: '2026-09-18'
description: Run typed option logits and autoregressive JSON locally with open models and WebGPU.
tags:
- hackernews
- trending
---

A live, local experiment

# Decision modelin your browser.

A local model can either read probabilities for your allowed options without decoding them, or write the same kind of distribution token by token. Pick a size, run both on your own GPU, and measure the difference.

browser only
no backend
your timings
1.56 GB model

celebrationThere is no waitlist!Just try it out ↓

MiniCPM5 2B is selected by default. On a phone or smaller device, switch to Qwen3 0.6B in the model box if needed.

00 / setup

## Load the model once

Model
 

Qwen3 0.6B · recommended for phones and small devices

MiniCPM5 2B · recommended on desktop

Qwen3.5 4B · high-memory desktop

download
 load MiniCPM5 2B

Larger model. Loading may be slower or may not fit on some low-end devices.

Measured model quality
native checkpoints · owned + public benchmarks

Model
Download
Authored
Perturbed
TypeSafe

Qwen3 0.6B
639 MB
44.0%
52.8%
40.7%

MiniCPM5 2B
1.56 GB
68.6%
69.3%
63.7%

Qwen3.5 4B
3.01 GB
81.3%
76.6%
84.5%

Published Jev
hosted
—
—
88.3%

Owned columns are balanced accuracy. TypeSafe is equal-case agreement on the same 102-row public subset; Jev is the published value. Browser quantization may change model accuracy.

{{ icon }}{{ text }}

download / cache
—
starts only when you click load

model load
—
download and prepare

warmup
—
compile passes for both methods

Weights come from Hugging Face and remain in your browser cache. Inputs never leave this page. First load can take several minutes depending on the selected model, network and GPU.

01 / decision

## Give it a real choice

play_arrow
 run both methods

Try an example

Account support

Email triage

State
A customer says a password reset succeeded, but every login attempt still returns “account locked”. Two unlock emails were requested and neither arrived.

Question

Allowed options

A

B

C

remove
 remove

3 / 20

add
 add

Both paths receive the same decision. One reads option probabilities directly; the other asks the model to write its option probabilities as JSON text.

your decision
state + question + options

→

same local model
MiniCPM5 · 2B

↗
↘

read logits
A…T probabilities

write tokens
{
options
 + 
probabilities
}

02A / direct readout

## Choice probabilities

no decoding

Read the model’s choice logits and normalize only across the options you supplied.

waiting for a run

total
—

input
—

output
1 readout

02B / generation

## JSON probabilities

token by token

Ask the model to estimate the same displayed-option distribution and write it as JSON. Watch every token arrive.

waiting for a run

first token
—

total
—

input
—

output
—

measured wall-time ratio
run it on your GPU

The methods run sequentially on the same loaded model so they do not contend for one GPU. Direct runs first, then generation.

What these numbers do—and do not—mean

Conditional probabilities.Direct scores are a softmax over only the displayed option tokens. They are not calibrated confidence and do not include every answer the model might prefer.

Local model tiers.The phone model trades accuracy for size. MiniCPM is the desktop default. The 4B option needs substantially more memory. None is claimed to match Jev.

Real local timing.Setup, warmup, prompt preparation, direct execution, first generated token and generation completion are timed withperformance.now(). No canned results appear.

Quantized weights.The demo uses pinned GGUF builds through wllama. Quantization can change both quality and speed.