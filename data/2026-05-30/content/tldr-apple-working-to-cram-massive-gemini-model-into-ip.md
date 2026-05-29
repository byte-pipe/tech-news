---
title: Apple working to cram massive Gemini model into iPhone to power new Siri - Ars Technica
url: https://arstechnica.com/ai/2026/05/apple-reportedly-trying-to-distill-googles-multi-trillion-parameter-gemini-ai-to-run-on-iphone/
site_name: tldr
content_file: tldr-apple-working-to-cram-massive-gemini-model-into-ip
fetched_at: '2026-05-30T06:00:34.666202'
original_url: https://arstechnica.com/ai/2026/05/apple-reportedly-trying-to-distill-googles-multi-trillion-parameter-gemini-ai-to-run-on-iphone/
date: '2026-05-30'
published_date: '2026-05-28T18:30:48+00:00'
description: As Apple tries to shrink Gemini for the iPhone, a cloud component is probably inevitable.
tags:
- tldr
---

Text
 settings

It’s impossible to totally avoid generative AI when interacting with technology anymore, but Apple has a bit less of it. That’s not entirely by choice, though. The iPhone maker has delayed the AI-enhanced Siri multiple times since first promising it in 2024, buta deal with Googlewill merge the iconic assistant with Gemini later this year. As we approach theWorldwide Developers Conference, Apple has been working to bring big AI smarts to the modest processing environment of a smartphone. Apple fans may not like the outcome, though.

Apple has long crowed about the privacy value ofrunning AI locally, but a new report suggests that despite Apple’s best efforts, the iPhone’s Gemini makeover will lean heavily on Google and Nvidia in the cloud. The Informationreportsthat Apple’s Gemini-infused Siri will run both on-device and in the cloud, an apparent reversal of its privacy-focused preference for local AI.

With every new chip announcement, we hear about how the silicon has been optimized for AI—even Apple does this with its focus on Neural Engine upgrades. You may think from the grandiose language that smartphones are equipped to handle beefy AI models, butthat’s not necessarily the case. In fact, the GPUs in most phones can process more AI tokens than the AI-focused NPUs. Components like Apple’s Neural Engine are designed for contextual, efficient AI processing. Even if phones had faster AI processing, they lack the RAM to keep enormous models in memory.

Even the largest AI models are still middling assistants, and that makes local AI very challenging. The AI models that run on phones are physically smaller, featuring at most a few billion parameters. Compare that to Google’s latest Gemini models, which have trillions of parameters, The Information reports. On-device AI models are also “quantized” to run at lower precision, making them faster but affecting the accuracy of token generation. This all adds up to AIs that feel less smart than their cloud brethren, and even big cloud-based models can be pretty dumb sometimes.

## The amazing, shrinking Gemini

Google has versions of Gemini optimized for mobile devices, which it callsGemini Nano. However, these are designed for powering contextual features like Magic Cue and audio summarization. Siri, on the other hand, is supposed to be a conversational assistant—you talk to it and it does things. That’s a different experience that requires a different kind of model. On Android, Google doesn’t even bother trying to do that locally. Talking to Gemini always goes straight to the cloud.

After inking the Google deal, Apple apparently got to work distilling Google’s giant cloud-based Gemini models. Distillation is a process in which a small, less resource-intensive model learns to mimic a large, expensive one. With enough time, this can reliably transfer useful capabilities while pruning less important weights from the model. That may enable Siri to handle some tasks with private local compute, but a cloud component looks inevitable.

Processing users’ AI data in the cloud could be a problem for Apple. At WWDC, the company will probably promote its years of experience designing chips and how well that positions it for AI. However, The Information claims that Apple has struggled to even get Google’s massive undistilled Gemini models running on its custom Private Cloud Compute infrastructure, which is built on on M-series Mac chips.

When the smarter Siri rolls out, it will probably route more complex tasks to Google’s cloud infrastructure instead of Apple’s, but it won’t be running on Google TPUs. Apple has reportedly signed a deal with Nvidia to use its Confidential Computing platform for this purpose. Confidential Computing keeps data encrypted on Nvidia GPUs while it’s being processed in the cloud, which could help Apple claim it’s stillsensitive to user privacy concerns. It might even retain its own Private Cloud Compute branding for the system.

The iPhone probably won’t tell you which version of Gemini is handling individual Siri requests. Device makers designing hybrid systems that rely on local and cloud-based AI like to talk about making the experience feel “seamless.” There might be clues, though.

We’re all familiar with the sluggishness of big AI models, which can churn for a long time while they generate tokens. Nvidia’s fully encrypted Confidential Compute does slow processing compared to other AI options. Users may find it more noticeable when Siri has to talk to a remote server, but local AI will only get you so far when the best models can only run on multi-million-dollar servers.

 Ryan Whitwam
 

Senior Technology Reporter

 Ryan Whitwam
 

Senior Technology Reporter

 Ryan Whitwam is a senior technology reporter at Ars Technica, covering the ways Google, AI, and mobile technology continue to change the world. Over his 20-year career, he's written for Android Police, ExtremeTech, Wirecutter, NY Times, and more. He has reviewed more phones than most people will ever own. You can 
follow him on Bluesky
, where you will see photos of his dozens of mechanical keyboards.
 

1. 1.The most spectacular rocket explosion since N1 just happened in Florida
2. 2.Fed up with vibe coders, dev sneaks data-nuking prompt injection into their code
3. 3.Here's why the failure of Blue Origin's New Glenn rocket is so catastrophic
4. 4.Websites have a new way to spy on visitors: Analyzing their SSD activity
5. 5.Rocket Report: A dark day for Blue Origin; Pentagon eyes new launch site

Customize