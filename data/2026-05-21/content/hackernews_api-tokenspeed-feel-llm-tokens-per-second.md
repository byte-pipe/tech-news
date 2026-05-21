---
title: tokenspeed — feel LLM tokens-per-second
url: https://mikeveerman.github.io/tokenspeed/
site_name: hackernews_api
content_file: hackernews_api-tokenspeed-feel-llm-tokens-per-second
fetched_at: '2026-05-21T12:05:47.287741'
original_url: https://mikeveerman.github.io/tokenspeed/
author: hexagr
date: '2026-05-18'
description: How fast is N tokens per second really?
tags:
- hackernews
- trending
---

Every local-LLM benchmark reports throughput:"47 tok/s on an M3,""180 tok/s on a 4090,""500 tok/s on Groq."Unless you've actually watched tokens stream at those rates, the numbers are
 hard to internalize. This is the rendering.

### Four modes

* code— syntax-highlighted pseudo-code, the most common thing you watch stream out of an LLM.
* text— lorem ipsum prose, for the chat/answer case.
* think— dim-italic reasoning sentences alternating with code, mimicking a reasoning model thinking out loud.
* agent— alternating tool calls and code generation with processing pauses, simulating an AI coding agent.

### What to try

Start at the default30and read along. Then hit1(5 tok/s — Raspberry-Pi-class local model),5(60 tok/s — typical hosted Claude or GPT),7(200 tok/s — Groq territory),9(800 tok/s — Cerebras-class, where the bottleneck is your eyeballs).

Now switch betweencandtat the same rate.
 The difference is striking — and intentional.

### What counts as a token

This approximates BPE-style tokenization, not any vendor-specific encoder
 (tiktoken, Claude's tokenizer, etc. — those disagree in the
 details anyway).

Short words are often one token; longer identifiers split into chunks
 (processUserInput→process+User+Input);
 punctuation and operators usually count too.

Code is more token-dense than prose, so the same tok/s can feel very
 different depending on what's streaming. The benchmark number is honest;
 the perceptual effect varies a lot by content type — which is the gap this
 tool exists to expose.

English prose averages ~1.3 tokens per word, so 30 tok/s ≈ 23 words/s.