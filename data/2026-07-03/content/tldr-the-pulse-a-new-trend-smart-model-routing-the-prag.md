---
title: 'The Pulse: a new trend, smart model routing - The Pragmatic Engineer'
url: https://blog.pragmaticengineer.com/the-pulse-a-new-trend-smart-model-routing/
site_name: tldr
content_file: tldr-the-pulse-a-new-trend-smart-model-routing-the-prag
fetched_at: '2026-07-03T19:33:10.841540'
original_url: https://blog.pragmaticengineer.com/the-pulse-a-new-trend-smart-model-routing/
date: '2026-07-03'
published_date: '2026-07-02T18:46:24.000Z'
description: Are there any ‘intelligent’ router solutions out there which select the right model for the right task? I looked into it, and there are a few options.
tags:
- tldr
---

Hi, this is Gergely with a bonus, free issue of the Pragmatic Engineer Newsletter. In every issue, I cover Big Tech and startups through the lens of senior engineers and engineering leaders. Today, we cover one out of four topics from a previousThe Pulse issue. Full subscribers received the article below three weeks ago. If you’ve been forwarded this email, you cansubscribe here.

Two weeks ago, I covered atrend of companies trying to reduce spending on AI within their engineering departments. While talking to my sources about this, one head of engineering at a larger company told me that they wished there was an ‘intelligent’ router that picks the right model for the right task.

The reason for such a wish is clear; prices for tokens vary greatly per model, and there can easily be a 10-20x difference between a cheap, average model, and a state-of-the-art one.

I did some digging into whether any solutions like this currently exist because the benefits look obvious, and what I found is listed below.Usual disclaimer: I have no affiliation with these vendors, and have not been paid to mention any of them!

Vendors:

* Factory Router: automatically selecting the right model per session, claiming 20-25% cost savings.More details.
* Not Diamond: auto-selection of coding models, claiming around 30% cost savings. Used by OpenRouter, under the hood.More details.
* Vercel AI gateway. Hundreds of AI models, smart routing and billing in one place.More details.
* Prismby Augment Code. Choosing the “best” model automatically for coding tasks.More details.
* Model Routerby Morph. An API to suggest model selection for a prompt, based on a list of models.More details
* Weave router: a token router that works inside Codex, Claude Code and Cursor. “Hard” requests stay on frontier models, while “easy” ones go to open source ones.More details

AI gateways with routing built in.API gateways are popular ways to use LLMs in workplaces.

* OpenRouter: comes with “auto router” functionality where, after analyzing the prompt, the best one is selected. Uses Not Diamond under the hood.More details
* Kilo Gateway: route requests the model considered the best price-per-value. Supports using your own model keys, and using the service only as a router.More details
* Requestly.ai: automatically route requests to the right model based on cost, latency, and availability, and tons of configuration.More details
* LiteLLM: define routing rules that automatically select the best model, based on input content with the “auto routing” functionality. The setup is more manual, but you get more control than with many other AI gateways.More details
* Envoy AI Gateway: an open source gateway that offerssomerouting configuration, though it feels that the routing engine focuses more on availability, not cost optimization and smart model routing.More details

Cursor and GitHub Copilot also have an “Auto” model selection that does automatic model selection. For Cursor, it’s afixed-price modelwhere any savings made are for Cursor: they are not passed on to customers, but the model is cheaper than most others. For Copilot, theAuto moderesults in intelligent model selection – but I’ve not heard much positive feedback about this mode from the few devs I asked about it. For Pro plans, Copilot supports pretty old models: GPT-5.5 and Opus 4.8 are not available. These are, however, available on the Pro+ and above plans.

Demand seems to be extremely high for intelligent routing. I askedMatan Grinberg, cofounder and CEO at Factory AI, who told me:

“Demand has been off the charts, especially from the enterprise [from large companies.] I’ve met with practically every bank CEO since we launched this offering, because they want a layer to control spend, while still generating high-quality code.
Pretty much everyone in tech is starting to see that open models are often sufficient. 
We’re seeing open model usage strictly increasing the last six months. My guess is that hosted open models are sufficient in performance for around 60% of coding-related work, in terms of token spend.”

It feels to me that “intelligent routing” will become table stakes, and so we can expect pretty much all AI vendors to build some version of it, and many new vendors to offer this kind of functionality.

If you know of any additional vendors not listed, you can add a commenton the original The Pulse article, and see more options there.Read the full issueThe Pulse that this excerpt was from, or check outall The Pulse issues.

Subscribe to my weekly newsletterto get articles like this in your inbox. It's a pretty good read - and the#1 software engineering newsletteron Substack.