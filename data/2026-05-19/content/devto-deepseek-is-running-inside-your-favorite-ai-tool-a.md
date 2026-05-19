---
title: DeepSeek Is Running Inside Your Favorite AI Tool – And Nobody Told You - DEV Community
url: https://dev.to/harsh2644/deepseek-is-running-inside-your-favorite-ai-tool-and-nobody-told-you-5g47
site_name: devto
content_file: devto-deepseek-is-running-inside-your-favorite-ai-tool-a
fetched_at: '2026-05-19T19:37:04.585716'
original_url: https://dev.to/harsh2644/deepseek-is-running-inside-your-favorite-ai-tool-and-nobody-told-you-5g47
author: Harsh
date: '2026-05-18'
description: I was debugging a slow response in HuggingChat last Tuesday. Standard stuff Open DevTools, check the... Tagged with ai, opensource, transparency, discuss.
tags: '#discuss, #ai, #opensource, #transparency'
---

DevTools exposing hidden model providers

I was debugging a slow response in HuggingChat last Tuesday.

Standard stuff Open DevTools, check the Network tab, filter by Fetch/XHR, look at the API responses.

And then I saw this right there in the chat UI:

agentic with Kimi-K2.6 via 🤗 together

Enter fullscreen mode

Exit fullscreen mode

HuggingChat showing exactly which model it's using - Kimi-K2.6 via Together AI No hiding This is what transparency looks like.

I stared at the screen for a second Kimi-K2.6 That's a model from Moonshot AI a Chinese AI company Not something HuggingChat built from scratch Just a third-party API call, right there in plain sight.

But here's the thing HuggingChat was being honest They show you the model name They show you the inference provider Right in the UI.

Then I checked some of the other tools I use every day.

That's when things got uncomfortable.

## What the API Traffic Actually Shows

DeepSeek, Kimi, Qwen Chinese open-source models are everywhere right now In my case, HuggingChat revealed it was using Kimi-K2.6 Other tools hide DeepSeek or similar models in their API calls while their marketing pages talk about something very different.

I found multiple tools with proprietary claims that were actually calling DeepSeek, Qwen, and Kimi APIs The pattern was consistent: marketing said one thing, network traffic said another.

One tool's website says"frontier intelligence built from scratch"The API response sayskimi-k2p5-rl-0317.

Another claims"self-developed AI, fully in-house"Network traffic showsdeepseek-coder-v2.

A third markets itself as"next-generation proprietary model"DevTools revealsqwen-2.5-72b.

They had us in the first half.

## Why This Actually Matters

Before you say "who cares what model is under the hood, if it works it works" let me push back.

It matters for your decision-makingYou're choosing between tools partly based on the claim that one has a better, proprietary model If they're both calling the same third-party API, that's not a differentiator. You're paying a premium for a wrapper.

It matters for your dataIf a tool says your data never leaves our servers but the API traffic shows calls toapi.together.aiorapi.moonshot.cnthose are different servers In different countries. Possibly under different data protection laws This matters for enterprise use especially.

It matters for trust.A tool that misrepresents what model it's using makes you wonder what else in the product description is marketing fiction Pricing Data handling Capabilities All of it.

It matters for debuggingWhen something gives weird or unexpected output, knowing the actual model helps enormously Why is this responding strangely to Chinese language inputs? is a lot easier to debug if you know it's routing to a Chinese model behind the scenes.

## HuggingChat Is Actually the Good Example Here

I want to be clear about something: the screenshot that started all this HuggingChat showingKimi-K2.6 via togetheris HuggingChat doing the right thing.

They show you the model They show you the inference provider They put it right in the chat UI No DevTools required No API snooping.

That's not hard to implement It's a design choice.

Showing the model says: we trust you to know what you're using

Not showing the model says: we'd rather you didn't think about this

HuggingChat should be the baseline The uncomfortable reality is that most tools don't meet it.

## How to Check Your Own Tools (5 Minutes)

You don't need anything special. Just a browser and 5 minutes

Step 1:Open your AI tool of choice in Chrome or Edge

Step 2:PressF12to open DevTools → go to theNetworktab

Step 3:Filter byFetch/XHR

Step 4:Ask something simple — "Explain Python in one line"

Step 5:Click the API request that fires. Look at theResponsetab

Look for:

* Amodelfield in the JSON response
* Third-party domains in the request URL:together.ai,openai.com,anthropic.com,moonshot.cn,deepseek.com
* Model IDs in the payload — they look likekimi-k2p5-rl-0317ordeepseek-coder-v2orqwen-2.5-72b-instruct

That's it. Five minutes. You'll know exactly what you're actually talking to.

## The Broader Pattern

AI tools are in an awkward middle phase right now The underlying models are mostly commodities everyone is calling the same APIs from OpenAI Anthropic Together AI Moonshot Mistral DeepSeek The real differentiation is supposed to be in the product layer: the UX the context handling the integrations the workflow.

But some companies are still trying to compete on the model itself And when they can't build one, some just... say they did Put "proprietary" in the marketing Hope no one opens DevTools.

Most people don't check. You're busy. The tool works. Move on.

But it works and it's honest with you about what it is are two different things And the second one matters more than the industry currently acknowledges.

The tools that are transparent about their models tend to be transparent about other things too pricing, limitations, data handling Honesty compounds. So does opacity.

## One Question Before You Go

Open DevTools right now on the AI tool you use most.

Check the Network tab Find the model name in the API response.

Is it what you expected?

I'll share exactly what I found in my daily tools in the comments —including the ones that surprised me.

Your turn. 👇

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (23 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse