---
title: Anthropic's Opus 5 is about token efficiency, not a capability leap - Ars Technica
url: https://arstechnica.com/ai/2026/07/anthropics-opus-5-is-about-token-efficiency-not-a-capability-leap/
site_name: newsfeed
content_file: newsfeed-anthropics-opus-5-is-about-token-efficiency-not-a
fetched_at: '2026-07-25T19:28:47.560407'
original_url: https://arstechnica.com/ai/2026/07/anthropics-opus-5-is-about-token-efficiency-not-a-capability-leap/
date: '2026-07-24'
published_date: '2026-07-24T21:05:51+00:00'
description: Models are improving quickly, but the cheaper options are often good enough.
tags:
- ars-technica
- ai
- agentic development
- anthropic
---

Text
 settings

Today, Anthropicrolled out Opus 5, the newest update for the model that has recently become a popular choice for coding and other software development tasks, among other things.

While this is a noteworthy bump for Opus, it doesn’t seem to be an Opus 4.5-level breakthrough in agentic coding performance.

A chart (made by Anthropic) with various benchmarks like Frontier-Bench and DeepSWE shows Opus 5 performing at about the same level or slightly ahead of the much-ballyhooed capabilities of Anthropic’s Fable model for coding tasks. It ostensibly beats Opus 4.8 and OpenAI’s competing GPT-5.6-Sol in just about every kind of task.

The various benchmarks show an iterative increase in performance, but not a radical leap, while the main pitch is that it’s a model that offers something just shy of Fable at approximately half the cost.

It’s also worth mentioning that Anthropic specifically avoided giving Opus 5 cutting-edge training on cybersecurity tasks, so it lags way behind Fable and Mythos in that regard. Anthropic claims it is relatively good at finding cybersecurity vulnerabilities, but because of decisions made in training the model, it is “substantially behind Mythos 5 on theexploitationof those vulnerabilities.”

As such, Opus 5 doesn’t have all of the same controversial protections that Fable had, such as the policy of keeping data for review for 30 days in case of an incident.

But this is really a cost story. From one model update to the next subsequent one, we’ve mostly been seeing modest performance improvements—though they look far more dramatic when you look at a whole year of updates. The discourse among software developers and engineering managers right now is mostly around dealing with cost, and there’s real movement in open-weight models, local models, and other alternatives to cutting-edge frontier models.

Opus 5 sits at $5 per million input tokens, or $25 per million output tokens—on par with its predecessor, but cheaper than Fable. That said, the recently announced Chinese open-weight model Kimi K3 comes in at just $15 per million output tokens at similar performance, so competition is fierce.

Lately, companies like Cursor and Meta have beenbuilding“model routers,” systems that automatically select models of varying size and capability from an array of options based on the nature of the prompt. The idea is that you save a lot of tokens (and therefore compute and/or money) by not using something like Fable for every task.

Companies like Anthropic are going to have to keep bringing token costs down, or at least (as is the case here) offering more performance for no additional cost, to continue to see the growth they’ve seen. Otherwise, they will start seeing reduced usage as people turn to smaller or open models once those models get good enough to handle the less challenging development tasks.

 Samuel Axon
 

Senior Editor

 Samuel Axon
 

Senior Editor

 Samuel Axon is the editorial lead for tech and gaming coverage at Ars Technica. He covers physical and generative AI, large language models, software development, gaming, entertainment, and mixed reality. He has been writing about gaming and technology for nearly two decades at Engadget, PC World, Mashable, Vice, Polygon, Wired, and others. He previously ran a marketing and PR agency in the gaming industry, led editorial for the TV network CBS, and worked on social media marketing strategy for Samsung Mobile at the creative agency SPCSHP. He also is an independent software and game developer for iOS, Windows, and other platforms, and he is a graduate of DePaul University, where he studied interactive media and software development.
 

1. 1.OpenAI says its AI agent broke out of testing sandbox to hack Hugging Face
2. 2.AI Kill Switch Act would let Trump admin order shutdown of rogue AI systems
3. 3.Canadian legislator reads out apparent LLM response in floor speech
4. 4.European Union grants US request to restrict satellite images of Iran War region
5. 5.Rocket Report: Lightning strikes in China; Starship launch on deck

Customize