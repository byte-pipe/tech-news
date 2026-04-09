---
title: Continuing to bring you our latest models, with an improved Gemini 2.5 Flash and Flash-Lite release - Google Developers Blog
url: https://developers.googleblog.com/en/continuing-to-bring-you-our-latest-models-with-an-improved-gemini-2-5-flash-and-flash-lite-release/
site_name: hackernews_api
fetched_at: '2025-09-26T11:06:31.669797'
original_url: https://developers.googleblog.com/en/continuing-to-bring-you-our-latest-models-with-an-improved-gemini-2-5-flash-and-flash-lite-release/
author: meetpateltech
date: '2025-09-25'
description: Google is releasing updated Gemini 2.5 Flash and Flash-Lite preview models with improved quality, speed, and efficiency.
tags:
- hackernews
- trending
---

English


 Español (Latam)


 Bahasa Indonesia


 日本語


 한국어


 Português (Brasil)


 简体中文


# Continuing to bring you our latest models, with an improved Gemini 2.5 Flash and Flash-Lite release

SEPT. 25, 2025

Shrestha Basu Mallick

Product

Google DeepMind

Sid Lall

Product

Google DeepMind

Zach Gleicher

Product

Google DeepMind

Kate Olszewska

Product

Google DeepMind

Share

* Facebook
* Twitter
* LinkedIn
* Mail



Today, we are releasing updated versions of Gemini 2.5 Flash and 2.5 Flash-Lite, available onGoogle AI StudioandVertex AI, aimed at continuing to deliver better quality while also improving the efficiency.

 Improvements in quality and speed for Gemini 2.5 Flash and 2.5 Flash Lite preview models compared to the current stable models


 50% reduction in output tokens (hence costs) for Gemini 2.5 Flash-Lite and 24% reduction for Gemini 2.5 Flash


## Updated Gemini 2.5 Flash-Lite

The latest version of Gemini 2.5 Flash-Lite was trained and built based on three key themes:

* Better instruction following: The model is significantly better at following complex instructions and system prompts.
* Reduced verbosity:It now produces more concise answers, a key factor in reducing token costs and latency for high-throughput applications (see charts above).
* Stronger multimodal & translation capabilities:This update features more accurate audio transcription, better image understanding, and improved translation quality.

You can start testing this version today using the following model string:gemini-2.5-flash-lite-preview-09-2025.

## Updated Gemini 2.5 Flash

This latest 2.5 Flash model comes with improvements in two key areas we heard consistent feedback on:

* Better agentic tool use:We've improved how the model uses tools, leading to better performance in more complex, agentic and multi-step applications. This model shows noticeable improvements on key agentic benchmarks, including a 5% gain on SWE-Bench Verified, compared to our last release (48.9% → 54%).
* More efficient:With thinking on, the model is now significantly more cost-efficient—achieving higher quality outputs while using fewer tokens, reducing latency and cost (see charts above).

We’re already seeing positive feedback from early testers. As Yichao ‘Peak’ Ji, Co-Founder & Chief Scientist atManus, an autonomous AI agent, noted:“The new Gemini 2.5 Flash model offers a remarkable blend of speed and intelligence. Our evaluation on internal benchmarks revealed a 15% leap in performance for long-horizon agentic tasks. Its outstanding cost-efficiency enables Manus to scale to unprecedented levels—advancing our mission to Extend Human Reach.”

You can start testing this preview version today by using the following model string:gemini-2.5-flash-preview-09-2025.

## Start building with Gemini

Over the last year, we’ve learned that shipping preview versions of our models allows you to test our latest improvements and innovations, provide feedback, and build production-ready experiences with the best of Gemini. Today’s releases are not intended to graduate to a new,stable versionbut will help us shape our future stable releases, and allow us to continue iterating and bring you the best of Gemini.

To make it even easier to access our latest models while also reducing the need to keep track of long model string names, we are also introducing a-latestaliasfor each model family. This alias always points to our most recent model versions, allowing you to experiment with new features without needing to update your code for each release. You can access the new previews using:

* gemini-flash-latest
* gemini-flash-lite-latest

To ensure you have time to test new models, we will always provide a 2-week notice (via email) before we make updates or deprecate a specific version behind-latest. These are just model aliases so the rate limits, cost, and features available may fluctuate between releases.

For applications that require more stability, continue to usegemini-2.5-flashandgemini-2.5-flash-lite.

We continue to push the frontier of what is possible with Gemini and this release is just another step in that direction. We will have more to share soon, but in the meantime, happy building!
