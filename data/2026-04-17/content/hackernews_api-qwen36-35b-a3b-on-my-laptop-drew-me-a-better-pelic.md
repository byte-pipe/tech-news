---
title: Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7
url: https://simonwillison.net/2026/Apr/16/qwen-beats-opus/
site_name: hackernews_api
content_file: hackernews_api-qwen36-35b-a3b-on-my-laptop-drew-me-a-better-pelic
fetched_at: '2026-04-17T11:51:17.780693'
original_url: https://simonwillison.net/2026/Apr/16/qwen-beats-opus/
author: Simon Willison
date: '2026-04-16'
description: Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7
tags:
- hackernews
- trending
---

# Simon Willison’s Weblog

Subscribe

Sponsored by:
 Honeycomb — AI agents behave unpredictably. Get the context you need to debug what actually happened. 
Read the blog

## Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7

16th April 2026

For anyone who has been (inadvisably) taking mypelican riding a bicycle benchmarkseriously as a robust way to test models, here are pelicans from this morning’s two big model releases—Qwen3.6-35B-A3B from AlibabaandClaude Opus 4.7 from Anthropic.

Here’s the Qwen 3.6 pelican, generated usingthis 20.9GB Qwen3.6-35B-A3B-UD-Q4_K_S.ggufquantized model by Unsloth, running on my MacBook Pro M5 viaLM Studio(and thellm-lmstudioplugin)—transcript here:

And here’s one I got from Anthropic’sbrand new Claude Opus 4.7(transcript):

I’m giving this one to Qwen 3.6. Opus managed to mess up the bicycle frame!

I tried Opus a second time passingthinking_level: max. It didn’t do much better (transcript):

#### I don’t think Qwen are cheating

A lot of people areconvinced that the labs train for my stupid benchmark. I don’t think they do, but honestly this result did give me a little glint of suspicion. So I’m burning one of my secret backup tests—here’s what I got from Qwen3.6-35B-A3B and Opus 4.7 for “Generate an SVG of a flamingo riding a unicycle”:

Qwen3.6-35B-A3B
(
transcript
)

Opus 4.7
(
transcript
)

I’m giving this one to Qwen too, partly for the excellent<!-- Sunglasses on flamingo! -->SVG comment.

#### What can we learn from this?

The pelican benchmark has always been meant as a joke—it’s mainly a statement on how obtuse and absurd the task of comparing these models is.

The weird thing about that joke is that, for the most part, there has been a direct correlation between the quality of the pelicans produced and the general usefulness of the models. Thosefirst pelicans from October 2024were junk. Themore recent entrieshave generally been much, much better—to the point that Gemini 3.1 Pro producesillustrations you could actually use somewhere, provided you had a pressing need to illustrate a pelican riding a bicycle.

Today, even that loose connection to utility has been broken. I have enormous respect for Qwen, but I very much doubt that a 21GB quantized version of their latest model is more powerful or useful than Anthropic’s latest proprietary release.

If the thing you need is an SVG illustration of a pelican riding a bicycle though, right now Qwen3.6-35B-A3B running on a laptop is a better bet than Opus 4.7!

Posted 
16th April 2026
 at 5:16 pm · Follow me on 
Mastodon
, 
Bluesky
, 
Twitter
 or 
subscribe to my newsletter

## More recent articles

* Meta's new model is Muse Spark, and meta.ai chat has some interesting tools- 8th April 2026
* Anthropic's Project Glasswing - restricting Claude Mythos to security researchers - sounds necessary to me- 7th April 2026

 

This isQwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7by Simon Willison, posted on16th April 2026.

 ai
 
1963

 generative-ai
 
1742

 local-llms
 
154

 llms
 
1709

 anthropic
 
270

 claude
 
267

 qwen
 
54

 pelican-riding-a-bicycle
 
105

 llm-release
 
191

 lm-studio
 
19

Previous:Meta's new model is Muse Spark, and meta.ai chat has some interesting tools

### Monthly briefing

Sponsor me for$10/monthand get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

 Sponsor & subscribe
 

 

 

* Disclosures
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
* 2026