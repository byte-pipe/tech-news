---
title: My 2.5 year old laptop can write Space Invaders in JavaScript now, using GLM-4.5 Air and MLX
url: https://simonwillison.net/2025/Jul/29/space-invaders/
site_name: hackernews_api
fetched_at: '2025-07-29T23:07:35.348462'
original_url: https://simonwillison.net/2025/Jul/29/space-invaders/
author: Simon Willison
date: '2025-07-29'
description: My 2.5 year old laptop can write Space Invaders in JavaScript now (GLM-4.5 Air)
tags:
- hackernews
- trending
---

# Simon Willison’s Weblog

Subscribe

## My 2.5 year old laptop can write Space Invaders in JavaScript now, using GLM-4.5 Air and MLX

29th July 2025

I wrote about the newGLM-4.5model family yesterday—new open weight (MIT licensed) models fromZ.aiin China which their benchmarks claim score highly in coding even against models such as Claude Sonnet 4.

The models are pretty big—the smaller GLM-4.5 Air model is still 106 billion total parameters, whichis 205.78GBon Hugging Face.

Ivan Fioravantibuiltthis44GB 3bit quantized version for MLX, specifically sized so people with 64GB machines could have a chance of running it. I tried it out... and it worksextremely well.

I fed it the following prompt:

Write an HTML and JavaScript page implementing space invaders

And it churned away for a while and producedthe following:

Clearly this isn’t a particularly novel example, but I still think it’s noteworthy that a model running on my 2.5 year old laptop (a 64GB MacBook Pro M2) is able to produce code like this—especially code that worked first time with no further edits needed.

#### How I ran the model

I had to run it using the currentmainbranch of themlx-lmlibrary (to ensure I hadthis commitaddingglm4_moesupport). I ran that usinguvlike this:

uv run \
 --with
'
https://github.com/ml-explore/mlx-lm/archive/489e63376b963ac02b3b7223f778dbecc164716b.zip
'
 \
 python

Then in that Python interpreter I used the standard recipe for running MLX models:

from

mlx_lm

import

load
,
generate

model
,
tokenizer

=

load
(
"mlx-community/GLM-4.5-Air-3bit"
)

That downloaded 44GB of model weights to my~/.cache/huggingface/hub/models--mlx-community--GLM-4.5-Air-3bitfolder.

Then:

prompt

=

"Write an HTML and JavaScript page implementing space invaders"

messages

=
 [{
"role"
:
"user"
,
"content"
:
prompt
}]

prompt

=

tokenizer
.
apply_chat_template
(

messages
,

add_generation_prompt
=
True

)

response

=

generate
(

model
,
tokenizer
,

prompt
=
prompt
,

verbose
=
True
,

max_tokens
=
8192

)

The response started like this:

<think>The user wants me to create a Space Invaders game using HTML, CSS, and JavaScript. I need to create a complete, functional game with the following features:

1. Player spaceship that can move left/right and shoot
2. Enemy invaders that move in formation and shoot back
3. Score tracking
4. Lives/health system
5. Game over conditions [...]

Followed by the HTML and this debugging output:

Prompt: 14 tokens, 14.095 tokens-per-sec
Generation: 4193 tokens, 25.564 tokens-per-sec
Peak memory: 47.687 GB

You can seethe full transcript here, or viewthe source on GitHub, ortry it out in your browser.

#### A pelican for good measure

I ranmy pelican benchmarkagainst the full sized modelsyesterday, but I couldn’t resist trying it against this smaller 3bit model. Here’s what I got for"Generate an SVG of a pelican riding a bicycle":

Here’s thetranscript for that.

In both cases the model used around 48GB of RAM at peak, leaving me with just 16GB for everything else—I had to quit quite a few apps in order to get the model to run but the speed was pretty good once it got going.

#### Local coding models are really good now

It’s interesting how almost every model released in 2025 has specifically targeting coding. That focus has clearly been paying off: these coding models are gettingreally goodnow.

Two years ago when Ifirst tried LLaMAI neverdreamedthat the same laptop I was using then would one day be able to run models with capabilities as strong as what I’m seeing from GLM 4.5 Air—and Mistral 3.2 Small, and Gemma 3, and Qwen 3, and a host of other high quality models that have emerged over the past six months.

Posted
29th July 2025
 at 1:02 pm · Follow me on
Mastodon
,
Bluesky
,
Twitter
 or
subscribe to my newsletter

## More recent articles

* Using GitHub Spark to reverse engineer GitHub Spark- 24th July 2025
* Vibe scraping and vibe coding a schedule app for Open Sauce 2025 entirely on my phone- 17th July 2025



This isMy 2.5 year old laptop can write Space Invaders in JavaScript now, using GLM-4.5 Air and MLXby Simon Willison, posted on29th July 2025.

Part of seriesLLMs on personal devices

1. I can now run a GPT-4 class model on my laptop- Dec. 9, 2024, 3:08 p.m.
2. DeepSeek-R1 and exploring DeepSeek-R1-Distill-Llama-8B- Jan. 20, 2025, 3:20 p.m.
3. Using pip to install a Large Language Model that's under 100MB- Feb. 7, 2025, 6:34 a.m.
4. My 2.5 year old laptop can write Space Invaders in JavaScript now, using GLM-4.5 Air and MLX- July 29, 2025, 1:02 p.m.

 python

1169

 ai

1465

 generative-ai

1281

 local-llms

129

 llms

1260

 ai-assisted-programming

219

 uv

62

 mlx

35

 pelican-riding-a-bicycle

45

Previous:Using GitHub Spark to reverse engineer GitHub Spark

### Monthly briefing

Sponsor me for$10/monthand get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

 Sponsor & subscribe






* Colophon
* ©
* 2002
* 2003
* 2004
* 2005
* 2006
* 2007
* 2008
* 2009
* 2010
* 2011
* 2012
* 2013
* 2014
* 2015
* 2016
* 2017
* 2018
* 2019
* 2020
* 2021
* 2022
* 2023
* 2024
* 2025
