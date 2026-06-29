---
title: Qwen 3.6 27B is the sweet spot for local development - Quesma Blog
url: https://quesma.com/blog/qwen-36-is-awesome/
site_name: hackernews_api
content_file: hackernews_api-qwen-36-27b-is-the-sweet-spot-for-local-developmen
fetched_at: '2026-06-29T19:36:09.977429'
original_url: https://quesma.com/blog/qwen-36-is-awesome/
author: Piotr Migdał
date: '2026-06-29'
published_date: '2026-06-29T10:34:14.302Z'
description: Qwen 3.6 27B is finally a smart model we can use for coding on Macbook or Nvidia RTX - with llama.cpp and OpenCode.
tags:
- hackernews
- trending
---

Back to Blog
 
 
 

# Qwen 3.6 27B is the sweet spot for local development

 
 
 
 Piotr Migdał 
 
 
 29 June 2026 
 
 

 
 
 
 
 

 
 
 
 
 
 
 

Download PNG

 
 
 
 
 
 
 
 
 
 
 

I’ve been disappointed by local models in the past. But then I checked Qwen 3.6, and I was in awe.
For me it’s the first local model that actually makes sense as a general intelligence.

It comes in two variants, a mixture-of-experts modelQwen 3.6 35B A3B, and a denseQwen 3.6 27B- slower, but more powerful. The one I recommend!

Let me share my impressions, and show that you can run it too.

 
 
 
 
 

It’s hot, literally. When my knees started to melt, I grabbed a phone-attachedthermal cameraand took a photo.

 
 

Qwen 3.6, rightfully,got a lot of coverage on Hacker News. The most common statement about Qwen 3.6 27B is that it punches above its weight - seeWill it Mythos?. And I think it is a well-deserved sentiment.
It will make your computer hot, but it’s worth it!

## Testing the waters

Simon Willison uses “penguins on a bicycle” as a smoke test (see forQwen 3.6 35B A3Band thenQwen 3.6 27B). I usually go with constrained writing.

 
 
 
 
 

A year ago these kinds of things were state of the art, needing a unique, and insanely expensive GPT-4.5, seevibe
translating Quantum Flytrap.

 
 

I also asked it to write an 8 line poem about Zouk dance and quantum physics, seethe transcript.
The thought process made sense, both in terms of deliberation on quantum terms, and rhymes.

Then I asked in OpenCode to create a hexagonal minesweeper usingpnpm. It worked:

It worked on the first go, from a single prompt, with a proper Node package.
The mixture-of-experts Qwen 3.6 35B A3B was faster… but ignored my instruction to create a package, and did it in a singleindex.html.

## Real work

Sure, creative writing about quantum mechanics, or yet another clone of a minesweeper, is rarely a day job.
But Qwen 3.6 27B is decent at regular tasks as well.

 
 
 
 
 

Prompt by a friend,Maciej Cielecki, atAI Tinkerers Warsaw.

 
 

It worked for a few minutes and created this:

By standards of current frontier models, it’s unremarkable.
But it is already a practical job. It worked, was reactive, defaults were nice - all from a single, short prompt.

## Running Qwen 3.6 locally with llama.cpp

Running local models is easier than ever. A few CLI lines and you’re off.

I recommendllama.cpp- a direct, open source tool that allows running models on various devices. You don’t need Ollama, and frankly -I would recommend against using that on ethical grounds.

First, we go to Hugging Face, to get proper quantization, i.e. a model with reduced size - popular ones are byunslothorbartowski, among others.
Default models usually come withBF16precision. A common 8-bit quantization saves half the space at almost no cost to quality. Going further down the road, models are smaller (and potentially - faster), but at the cost of quality, seethis comparison for 27Band another one for35B A3B.

We grabunsloth/Qwen3.6-27B-MTP-GGUF:Q8_0, an 8-bit quantization with support for multi-token prediction (MTP).

llama-server
 -hf
 unsloth/Qwen3.6-27B-MTP-GGUF:Q8_0
 \

 --spec-type
 draft-mtp
 -ngl
 999
 -fa
 on
 -c
 65536
 --jinja
 --port
 8080

What it does:

* -hf unsloth/Qwen3.6-27B-MTP-GGUF:Q8_0grabs from Hugging Face, on the next runs will reuse that
* -m ~/models/Qwen3.6-27B-Q8_0.ggufuse instead if you already have it
* draft-mtpwe use a fast model to predict subsequent tokens, speeds up things
* -ngl 999for putting all layers to GPU
* -fa onflash attention is on
* -c 65536context size set to 64k tokens (this we can tweak, as Qwen 3.6 27B native context is 256k)
* --jinjafor tool calling support
* --port 8080better to pin port, as it will be used by other configs

If you openhttp://127.0.0.1:8080, you can directly chat with it.

Precisely the same server can be used for vibe coding. Choice of agent depends both on one’s goal and subjective taste - for an all-around OpenCode, minimalistic Pi, and self-improving Hermes.

For OpenCode, it is as simple as adding to~/.config/opencode/opencode.jsonc:

{

 "$schema"
: 
"https://opencode.ai/config.json"
,

 "provider"
: {

 "llama"
: {

 "name"
: 
"llama.cpp (local)"
,

 "npm"
: 
"@ai-sdk/openai-compatible"
,

 "options"
: {

 "baseURL"
: 
"http://127.0.0.1:8080/v1"
,

 "apiKey"
: 
"local"

 },

 "models"
: {

 "qwen3.6-27b"
: { 
"name"
: 
"Qwen3.6-27B Q8 +MTP"
 }

 }

 }

 },

 "model"
: 
"llama/qwen3.6-27b"

}

If you just want to chat and are a big fan of Terminal, instead ofllama-serverusellama-cli:

 llama-cli
 -hf
 unsloth/Qwen3.6-27B-MTP-GGUF:Q8_0
 \

 -ngl
 999
 -fa
 on
 -c
 65536
 --jinja

## Measuring performance

Is it fast enough?

I ran a few tests (source is here) on my Macbook Max M5 128 GB, running it with and without multi-token prediction, and comparing both with the 35B A3B model, and also a quantized DeepSeek V4 Flash versionDwarfStar4.

 
 
 
tokens / s
 
RAM
 
 
 
 Qwen3.6-35B-A3B 
· 8-bit
 
 
 
 
 MLX 
 
 
 
 
85 tok/s
 
85
 
 
 
 
 
37 GB RAM
 
37 GB
 
 
 
 
 
 llama.cpp 
 
 
 
 
93 tok/s
 
93
 
 
 
 
 
44 GB RAM
 
44 GB
 
 
 
 
 
 llama.cpp + MTP 
 
 
 
 
105 tok/s
 
105
 
 
 
 
 
45 GB RAM
 
45 GB
 
 
 
 
 
 
 
 Qwen3.6-27B 
· 8-bit
 
 
 
 
 MLX 
 
 
 
 
17 tok/s
 
17
 
 
 
 
 
28 GB RAM
 
28 GB
 
 
 
 
 
 llama.cpp 
 
 
 
 
18 tok/s
 
18
 
 
 
 
 
41 GB RAM
 
41 GB
 
 
 
 
 
 llama.cpp + MTP 
 
 
 
 
32 tok/s
 
32
 
 
 
 
 
42 GB RAM
 
42 GB
 
 
 
 
 
 
 
 DeepSeek-V4-Flash 
· Q2–Q4
 
 
 
 
 llama.cpp 
 
 
 
 
33 tok/s
 
33
 
 
 
 
 
103 GB RAM
 
103 GB
 
 
 
 
 
 
 

30 tokens per second is not bad,well within typical frontier model API range.
Whilemlx-lmis precisely targeted at Apple Silicon devices, and AI agents heavily recommend it, llama.cpp turned out to be faster.
It was using 95% of GPU, which means it is efficiently using available resources.

Macbook Max M5 is a beast (at least for a laptop), but on other devices it should also work decently.
For consumer Nvidia RTX cards, on one hand models need to be quantized, on the other, it is even faster.

I set this up today on my 5090 at Q6_K quantization and Q4_0 KV, got 50 tokens/s consistently at 123k context, using ~28/32gb vram through LM Studio. -gfosco on the Hacker News

While 35B A3B is 3x faster, I prefer 27B. I’d rather generate a third as much code, but of higher quality.

## How do they relate to previous state of the art models?

Manual inspection is great, but benchmarks help with grounding intuitions. Here is the score fromArtificial Analysis, comparing it with frontier models:

 
 
 
Gemma 4 31B
 
 
 29 
 
 
 
≈ late 2024
 
o1 / Claude 3.5 Sonnet
 
 
 
Qwen3.6-35B-A3B
 
 
 32 
 
 
 
≈ early 2025
 
o3 / Claude 4 Sonnet
 
 
 
Qwen3.6-27B
 
 
 37 
 
 
 
≈ mid 2025
 
GPT-5 / Claude Sonnet 4.5
 
 
 
DeepSeek-V4-Flash
 
 
 40 
 
 
 
≈ late 2025
 
GPT-5.2 / Claude Opus 4.5
 
 
 
 

A few more benchmarks are inthese notes, but the spirit is similar.
Added hereGemma 4 31B, as a lot of people use this as the default for local coding. But both benchmarks and general sentiment online favour Qwen 3.6 27B by a large margin.

Here there is a caveat - 8-bit quantization likely does not affect results much, but DwarfStar4 uses much more aggressive ones for DeepSeek V4 Flash, 2-4 bit. For sure it is worse than the full model.
My personal impression is that within these quantizations Qwen 3.6 27B is as good as (or maybe slightly better than) DwarfStar4. Though, I won’t be surprised if for longer context projects DS4 has an edge.

## What’s next

I think we are entering a fascinating era, when it becomes feasible to run one’s own models.

The change will be propelled further by the state of proprietary frontier models. Claude Fable 5 was taken down. Other frontier models run at a massive subsidy, where paying $100 a month gives us thousands worth in tokens. Let’s use the discount while it lasts!

A locally set model can be fine-tuned to our needs, and cannot be taken away. Businesses can use them for proprietary and sensitive data. We can use them personally for offline projects, or when we don’t feel comfortable sharing our deepest secrets, or medical data, with the US or China.

With the release offrontier-level open-weight GLM 5.2, there is a new era.
While Qwen 3.6 was the stepping stone, even frontierGLM 5.2 can be run locally. It won’t run on your Macbook or a single RTX 5090. But still, it is manageable with a company budget.

Moreover, I strongly believe that we will have models smarter than current state of the art, while runnable on local devices, maybe even smartphones. Current models combine both raw intelligence and factual knowledge in the same weights.
Future models will likely separate that, offloading a lot of knowledge to tool calling.

 
 
 
 
 
 
 

Stay tuned for future posts and releases

 
 
 
 
 

Subscribe

 
 
 
 
 
 
 
OR
 
 

Subscribe via RSS

 
 
 
 
 
 

## RelatedArticles

Continue exploring similar topics

 
 
 
 
 
 
 
 
 

### Antigravity feels heavy and Claude Skills are light

 
 

Comparing Google Antigravity and Claude Code for AI-assisted workflows, and why custom Claude Skills might be the better approach.

 
 
 
 
 
Piotr Migdał
 
16 Dec 2025
 
 
 
 

Read more

 
 
 
 
 
 
 
 
 

HN

 
 
 
 
 
 
 
 
 
 

### CompileBench: Can AI Compile 22-year-old Code?

 
 

We tested 19 LLMs on their ability to handle real-world software engineering tasks like compiling old code and cross-compiling. See how Anthropic, OpenAI, and Google models stack up in our new benchmark – CompileBench.

 
 
 
 
 
Piotr Grabowski
 
17 Sep 2025
 
 
 
 

Read more

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

### Sandboxing AI-Generated Code: Why We Moved from WebR to AWS Lambda

 
 

Why we moved our AI chart generator from in-browser WebR (WASM) to AWS Lambda. A case study on the real-world trade-offs of running AI-generated R and ggplot2 code.

 
 
 
 
 
Piotr Migdał & Przemysław Hejman
 
7 Aug 2025
 
 
 
 

Read more

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

### Antigravity feels heavy and Claude Skills are light

 
 

Comparing Google Antigravity and Claude Code for AI-assisted workflows, and why custom Claude Skills might be the better approach.

 
 
 
 
 
Piotr Migdał
 
16 Dec 2025
 
 
 
 

Read more

 
 
 
 
 
 
 
 
 

HN

 
 
 
 
 
 
 
 
 
 

### CompileBench: Can AI Compile 22-year-old Code?

 
 

We tested 19 LLMs on their ability to handle real-world software engineering tasks like compiling old code and cross-compiling. See how Anthropic, OpenAI, and Google models stack up in our new benchmark – CompileBench.

 
 
 
 
 
Piotr Grabowski
 
17 Sep 2025
 
 
 
 

Read more

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

### Sandboxing AI-Generated Code: Why We Moved from WebR to AWS Lambda

 
 

Why we moved our AI chart generator from in-browser WebR (WASM) to AWS Lambda. A case study on the real-world trade-offs of running AI-generated R and ggplot2 code.

 
 
 
 
 
Piotr Migdał & Przemysław Hejman
 
7 Aug 2025
 
 
 
 

Read more

 
 
 
 
 
 
 
More Articles