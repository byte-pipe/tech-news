---
title: 'Claude Opus 4.8: “a modest but tangible improvement”'
url: https://simonwillison.net/2026/May/28/claude-opus-4-8/
site_name: tldr
content_file: tldr-claude-opus-48-a-modest-but-tangible-improvement
fetched_at: '2026-05-30T11:32:38.831431'
original_url: https://simonwillison.net/2026/May/28/claude-opus-4-8/
author: Simon Willison
date: '2026-05-30'
description: 'Claude Opus 4.8: “a modest but tangible improvement” (3 minute read)'
tags:
- tldr
---

# Simon Willison’s Weblog

Subscribe

Sponsored by:
 The AI App and Agent Factory — Microsoft Foundry is the enterprise Al platform where intelligence and trust ship with every agent. 
Try Foundry

## Claude Opus 4.8: “a modest but tangible improvement”

28th May 2026

Anthropic shippedClaude Opus 4.8today. My favourite thing about it is this note in the release announcement:

Users will find Opus 4.8 to be a modest but tangible improvement on its predecessor. There’s still more to be done: we’re working on developing and releasing models that provide many of the same capabilities as Opus at a lower cost.

It’s so refreshing to see an AI lab honestly describe a release as a minor incremental improvement over the previous model!

Honesty seems to be a theme. Here’s my other favorite note from that announcement:

One of the most prominent improvements in Opus 4.8 is itshonesty. We train all our models to be honest---for instance, to avoid making claims that they can’t support. But a general problem with AI models is that they sometimes jump to conclusions, confidently claiming to have made progress in their work despite the evidence being thin. Early testers report that Opus 4.8 is more likely to flag uncertainties about its work and less likely to make unsupported claims. This is borne out inour evaluations, which show that Opus 4.8 is around four times less likely than its predecessor to allow flaws in code it has written to pass unremarked.

That linked system card includes the following:

Claude Opus 4.8 had the lowest incorrect-rate of the six models on every benchmark—the most direct measure of factual hallucination. It achieved this mainly by abstaining on questions about which it was uncertain rather than by answering more questions correctly.

#### Model characteristics

Not much has changed since 4.7.

It’s priced the same as Opus 4.5/4.6/4.7—$5/million input and $25 per million output. “Fast mode” is twice that price, which is a significant reduction from their previous models—fast mode on 4.6/4.7 remains at $30/$150. Note thatfast modeis only available to organizations that are part of the research preview, “Contact your account manager to request access”.

Both the reliable knowledge cutoff and the training data cutoff are January 2026, the same as for 4.7.

The context window is still 1,000,000 tokens, and the max output is 128,000 tokens.

TheWhat’s new in Claude Opus 4.8document has some of the more interesting details. These caught my eye:

Mid-conversation system messages. Claude Opus 4.8 acceptsrole: "system"messages immediately after a user turn in themessagesarray (subject toplacement rules). This lets you append updated instructions later in a long-running conversation without restating the full system prompt, which preservesprompt cachehits on the earlier turns and reduces input cost on agentic loops.

See alsothis updateto the Anthropic Python SDK. Being able to steer the system prompt mid-conversation sounds really powerful. I was worried this would be incompatible with the abstraction provided by my ownLLM library, which expects a single system prompt per conversation... but it turns out my recentredesignshould handle thatjust fine.

Lower prompt cache minimum. The minimum cacheable prompt length on Claude Opus 4.8 is 1,024 tokens, lower than on Claude Opus 4.7.

I checked and 4.7’s minimumwas 4,096.

#### And some pelicans

Here arepelicans riding bicyclesfor all five thinking levels,low,medium,high,xhigh, andmax:

low

medium

high

xhigh

max

This time I ran them using theLLM CLI, exported the logs to Markdown and then had Claude Opus 4.8build mean HTML tool that could render that Markdown with thesvgfenced code blocks displayed as SVGs on the page.

(I later had GPT-5.5 xhigh in Codexupdate that codeto remove any XSS holes. I’m sure Claude could have done that if I’d asked, but GPT-5.5 is my code security blanket at the moment.)

The max one was clearly the best, but it did take 25 input, 17,167 output tokens for a total cost of43 cents!

Posted 
28th May 2026
 at 11:59 pm · Follow me on 
Mastodon
, 
Bluesky
, 
Twitter
 or 
subscribe to my newsletter

## More recent articles

* I think Anthropic and OpenAI have found product-market fit- 27th May 2026
* Notes on Pope Leo XIV's encyclical on AI- 25th May 2026

 

This isClaude Opus 4.8: “a modest but tangible improvement”by Simon Willison, posted on28th May 2026.

 ai
 
2,042

 generative-ai
 
1,805

 llms
 
1,772

 anthropic
 
287

 claude
 
276

 pelican-riding-a-bicycle
 
116

 llm-release
 
201

Previous:I think Anthropic and OpenAI have found product-market fit

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