---
title: AI Applications and Vertical Integration
url: https://www.tanayj.com/p/ai-applications-and-vertical-integration
site_name: tldr
content_file: tldr-ai-applications-and-vertical-integration
fetched_at: '2026-04-01T11:24:24.337348'
original_url: https://www.tanayj.com/p/ai-applications-and-vertical-integration
author: Tanay Jaipuria
date: '2026-04-01'
description: The two kinds of "full-stack" AI application companies
tags:
- tldr
---

# AI Applications and Vertical Integration

### The two kinds of "full-stack" AI application companies

Tanay Jaipuria
Mar 30, 2026
11
1
Share

I’m Tanay Jaipuria, a partner atWingand this is a weekly newsletter about the business of the technology industry. To receive Tanay’s Newsletter in your inbox, subscribe here for free:

Subscribe

Hi friends,

I’ve been thinking about a pattern that we’re increasingly starting to see across AI application companies. Over time, I think most of them become “full-stack”.

At a high level, you can think about an AI product that achieves outcomes as having three layers:

1. At the bottom, the model
2. In the middle, the application or agent which includes the data/context, etc
3. At the top, the human or service layer needed to review/prompt/do the last mile to actually get to an outcome

This is obviously a simplified way to describe the world. Models sit on top of chips, etc and there’s a lot of infrastructure, data systems, orchestration, evals in building agents. But I still think the simplification is useful.

Traditional application layer companies would sit just in the middle layer. But these companies are increasingly beginning to (or starting off) vertically integrate in one of two directions. Some move down into the model layer. Others start or move up into the human or service layer. Both end up looking “full-stack1,” just in very different ways.

## 1. Full stack down

The first version of full-stack is when the application company integrates down into the model layer.

This is the pattern we are seeing in coding, customer service and a few other categories where the company has enough usage, enough proprietary traces, and enough economic incentive to start pulling intelligence in-house.

Cursor is a very recent example. Last week it introduced Composer 2, positioning it as a frontier-level coding model with meaningfully improved benchmark performance and lower pricing than many alternatives. In its technical report, Cursor says Composer 2 uses Kimi K2.5 as a base model, then extends it with continued pretraining plus reinforcement learning on long-horizon coding tasks.

Intercom made a similar move this week with Fin Apex. Intercom CEO Eoghan McCabe described it as “the age of vertical models” and Intercom says Apex now powers essentially all of its English-language chat and email customer conversations.

Cursor, Intercom, Cognition, Harvey, Sierra, and are increasingly trying to shape, tune, route, and in some cases train the intelligence itself around a specific domain.

Why does this happen?

The biggest reason is that for AI companies, this is the most important flywheel they have to drive increased performance. They have the traces of the agents. They see the prompt, the outputs, the edits/acceptances/rejections. Over time, that becomes extremely valuable proprietary training data. Better product creates more usage. More usage creates more traces. More traces make the model better. Then the better model improves the product again.

Other reasons include:

* Cost and Speed: Once you have enough scale, the COGS can add up, and smaller, fine-tuned models can end up giving you enough performance for your use case at much lower cost and at much faster speed.
* Differentiation: If everyone in a category is calling the same handful of models, it becomes harder to build real product distance from the intelligence layer alone.

## 2. Full stack up

The second version of full-stack goes the other way. Instead of integrating into the model, the company integrates upward into the human or service layer. It sells true outcomes instead of software.

This is the more classical full-stack startup idea that Chris Dixon wrote about in 2015. You do not just sell software into a workflow. You own the end-to-end process and provide an outcome or service to the end customer.

Historically, that often meant ugly services economics and challenges with scaling. But AI changes the shape of that equation and opens up the possibility to take this route in many end markets that weren’t attractive.

This idea of “sell outcomes, not software”, “services-as-software” and AI-native services has been growing in popularity over the last few years, but as models increasingly get better at agentic tasks over longer horizons, we’re now starting to see the first wave of these companies truly break out.

There are a number of examples of these AI-native Services business across various services categories such as legal, insurance, accounting, customer support, recruiting, and IT modernization with the extreme version of these the “roll-up and layer on AI approaches”. On the de-novo AI-native services businesses side, we see companies such as:

* Crosby AI combines software, AI, and attorneys to own more of the delivered result and outcome in what co-founder and CEO Ryan calls a “Neofirm”.
* WithCoverage and Harper building AI-native insurance brokerages
* Mechanical Orchard is an AI-native software modernization services firm

AI is great but it isn’t 100% there, and a company that owns the end result can both plug the gaps in all the missing places is both incentivized to contuosly improve and allows the customer to not have to think about the last mile.

This path is especially interesting because it may eventually absorb even more of the stack. What starts as application plus service can, over time likely post-train specialized models too. As AI does more of the work, some of these companies may end up owning two layers at first, then increasingly all three.

## 3. Closing thoughts

I think AI application companies will not tend to stay just AI application companies. Over time, they will vertically integrate. Many will use their traces to own the intelligence as well to increase differentiation, performance and reduce costs, particularly given that the model companies themselves are encroaching on some of their applications. The others will either start out delivering full outcomes or over time as they can do an increasing amount of the work, decide they can capture more value by selling the full service rather than an agent that does 90% of it.

For more related to this topic, here are some good pieces:

* Ryan Daniels (Crosby AI) on theRise of the Neofirm
* Cursor’sComposer 2 Technical Report
* Eoghan McCabe (Intercom) on theAge of Verticalized Models
* Chris Dixon’s original piece onFull-stack Startups
1

I realise that per the three layered stack, neither approach is “full-stack” :)

11
1
Share
Previous