---
title: The last six months in LLMs in five minutes
url: https://simonwillison.net/2026/May/19/5-minute-llms/
site_name: hackernews_api
content_file: hackernews_api-the-last-six-months-in-llms-in-five-minutes
fetched_at: '2026-05-19T12:04:02.937279'
original_url: https://simonwillison.net/2026/May/19/5-minute-llms/
author: Simon Willison
date: '2026-05-19'
description: The last six months in LLMs in five minutes
tags:
- hackernews
- trending
---

# Simon Willison’s Weblog

Subscribe

Sponsored by:
 Datadog — Ship reliable AI faster with LLM Observability. 
Read the best practices guide

## The last six months in LLMs in five minutes

19th May 2026

I put together these annotated slides from my five minute lightning talk at PyCon US 2026, using thelatest iterationof myannotated presentation tool.

#

I presented this lightning talk at PyCon US 2026, attempting to summarize the last six months of developments in LLMs in five minutes.

#

Six months is a pretty convenient time period to cover, because it captures what I’ve been calling theNovember 2025 inflection point. November was a critical month in LLMs, especially for coding.

#

For one thing, the supposedly “best” model (depending mostly on vibes) changed hands five times between the three big providers.

#

As always, I’m using myGenerate an SVG of a pelican riding a bicycletest to help illustrate the differences between the models.

Why this test? Because pelicans are hard to draw, bicycles are hard to draw, pelicanscan’t ride bicycles... and there’s zero chance any AI lab would train a model for such a ridiculous task.

#

At the start of November the widely acknowledged “best” model was Claude Sonnet 4.5, released on29th September. It drew me this pelican.

In November it was overtaken byGPT-5.1, thenGemini 3, thenGPT-5.1 Codex Max, and then Anthropic took the crown back again withClaude Opus 4.5.

I think Gemini 3 drew the best pelican out of this lot, but pelicans aren’t everything. Most practitioners will agree that Opus 4.5 held the crown for the next couple of months.

#

It took a little while for this to become clear, but the real news from November was that the coding agents gotgood.

OpenAI and Anthropic had spent most of 2025 runningReinforcement Learning from Verifiable Rewardsto increase the quality of code written by their models, especially when paired up with their Codex and Claude Code agent harnesses.

In November the results of this work became apparent. Coding agents went from often-work to mostly-work, crossing a quality barrier where you could use them as a daily-driver to get real work done, without needing to spend most of your time fixing their stupid mistakes.

#

Also in November, this happened—the first commit to an obscure (back then) repo called “Warelay” by some guy called Pete.

#

Over the holiday period, from December to January, a whole lot of us took advantage of the break to have a poke at these new models and coding agents and see what they could do.

They could do a lot! Some of us got a little bit over-excited. I had my own short-lived bout of a form of LLM psychosis as I started spinning up wildly ambitious projects to see how far I could push them.

#

One of my projects was a vibe-coded implementation of JavaScript in Python—a loose port ofMicroQuickJS—which I calledmicro-javascript. You can try it out in your browser inthis playground.

#

That playground demo shows JavaScript code run using my micro-javascript library, in Python, running inside Pyodide, running in WebAssembly, running in JavaScript, running in a browser!

It’s pretty cool! But did anyone out thereneeda buggy, slow, insecure half-baked implementation of JavaScript in Python?

They did not. I have quite a few other projects from that holiday period that I have since quietly retired!

#

On to February. Remember that Warelay project that had its first commit at the end of November?

#

In December and January it had gone throughquite a few name changes... and by February it was taking the world by storm under its final name,OpenClaw.

The amount of attention it got is pretty astonishing for a project that was less than three months old.

#

OpenClaw is a “personal AI assistant”, and we actually got a generic term for these, based on NanoClaw and ZeroClaw and suchlike... they’re calledClaws.

#

Mac Minis started to sell out around Silicon Valley, because people were buying them to run their Claws.

Drew Breunigjoked to me that this is because they’re the new digital pets, and a Mac Mini is the perfect aquarium for your Claw.

#

My favourite metaphor for Claws is Alfred Molina’s Doc Ock in the 2004 movie Spider-Man 2. His claws were powered by AI, and were perfectly safe provided nothing damaged his inhibitor chip... after which they turned evil and took over.

#

Also in February: Gemini 3.1 Pro came out, and drew me areally good pelican riding a bicycle. Look at this! It’s even got a fish in its basket.

#

And then Google’s Jeff Deantweeted this videoof an animated pelican riding a bicycle, plus a frog on a penny-farthing and a giraffe driving a tiny car and an ostrich on roller skates and a turtle kickflipping a skateboard and a dachshund driving a stretch limousine.

So maybe the AI labs have been paying attention after all!

#

A lot of stuff happened just in the past month.

#

Google released theGemma 4series of models, which are the most capable open weight models I’ve seen from a US company.

#

Also last month, Chinese AI lab GLM came out withGLM-5.1—an open weight 1.5TB monster! This is a very effective model... if you can afford the hardware to run it.

#

GLM-5.1 drew me this very competent pelican on a bicycle.

#

... though when ittried to animate itthe bicycle bounced off into the top and the bicycle got warped.

#

Charleson Blueskysuggested I try it with a North Virginia Opossum on an E-scooter

#

And it did this! I’ve tried this on other models and they don’t even come close. “Cruising the commonwealth since dusk” is perfect. It’sanimated too.

#

The other neat Chinese open weight models in April came from Qwen.Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7. That’s a 20.9GB open weights model that runs on my laptop!

(I think this mainly demonstrates that the pelican on the bicycle has firmly exceeded its limits as a useful benchmark.)

#

Here’s that Claude Sonnet 4.5 pelican from September for comparison.

#

So those were the two main themes of the past six months. The coding agents got really good... and the laptop-available models, while a lot weaker than the frontier, have started wildly outperforming expectations.

Posted 
19th May 2026
 at 1:09 am · Follow me on 
Mastodon
, 
Bluesky
, 
Twitter
 or 
subscribe to my newsletter

## More recent articles

* Notes on the xAI/Anthropic data center deal- 7th May 2026
* Live blog: Code w/ Claude 2026- 6th May 2026

 

This isThe last six months in LLMs in five minutesby Simon Willison, posted on19th May 2026.

 lightning-talks
 
7

 pycon
 
28

 speaking
 
120

 ai
 
2025

 generative-ai
 
1792

 local-llms
 
157

 llms
 
1758

 annotated-talks
 
31

 pelican-riding-a-bicycle
 
114

 coding-agents
 
203

Previous:Notes on the xAI/Anthropic data center deal

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