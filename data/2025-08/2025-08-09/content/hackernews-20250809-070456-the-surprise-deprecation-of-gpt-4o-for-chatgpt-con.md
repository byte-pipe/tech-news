---
title: The surprise deprecation of GPT-4o for ChatGPT consumers
url: https://simonwillison.net/2025/Aug/8/surprise-deprecation-of-gpt-4o/
site_name: hackernews
fetched_at: '2025-08-09T07:04:56.286681'
original_url: https://simonwillison.net/2025/Aug/8/surprise-deprecation-of-gpt-4o/
author: Simon Willison
date: '2025-08-09'
---

# Simon Willison’s Weblog

Subscribe

## The surprise deprecation of GPT-4o for ChatGPT consumers

8th August 2025

I’ve been dipping into ther/ChatGPTsubreddit recently to see how people are reacting tothe GPT-5 launch, and so far the vibes there are not good.This AMA threadwith the OpenAI team is a great illustration of the single biggest complaint: a lot of people areveryunhappy to lose access to the much older GPT-4o, previously ChatGPT’s default model for most users.

A big surprise for me yesterday was that OpenAI simultaneously retired access to their older models as they rolled out GPT-5, at least in their consumer apps. Here’s a snippet fromtheir August 7th 2025 release notes:

When GPT-5 launches, several older models will be retired, including GPT-4o, GPT-4.1, GPT-4.5, GPT-4.1-mini, o4-mini, o4-mini-high, o3, o3-pro.

If you open a conversation that used one of these models, ChatGPT will automatically switch it to the closest GPT-5 equivalent. Chats with 4o, 4.1, 4.5, 4.1-mini, o4-mini, or o4-mini-high will open in GPT-5, chats with o3 will open in GPT-5-Thinking, and chats with o3-Pro will open in GPT-5-Pro (available only on Pro and Team).

There’s no deprecation period at all: when your consumer ChatGPT account gets GPT-5, those older models cease to be available.

Update 12pm Pacific Time: Sam Altman on Redditsix minutes ago:

ok, we hear you all on 4o; thanks for the time to give us the feedback (and the passion!). we are going to bring it back for plus users, and will watch usage to determine how long to support it.

See alsoSam’s tweetabout updates to the GPT-5 rollout.

Rest of my original post continues below:

(This only affects ChatGPT consumers—the API still provides the old models, theirdeprecation policies are published here.)

One of the expressed goals for GPT-5 was to escape the terrible UX of the model picker. Asking users to pick between GPT-4o and o3 and o4-mini was a notoriously bad UX, and resulted in many users sticking with that default 4o model—now a year old—and hence not being exposed to the advances in model capabilities over the last twelve months.

GPT-5’s solution is to automatically pick the underlying model based on the prompt. On paper this sounds great—users don’t have to think about models any more, and should get upgraded to the best available model depending on the complexity of their question.

I’m already getting the sense that this isnota welcome approach for power users. It makes responses much less predictable as the model selection can have a dramatic impact on what comes back.

Paid tier users can select “GPT-5 Thinking” directly. Ethan Mollick isalready recommending deliberately selecting the Thinking modeif you have the ability to do so, or trying prompt additions like “think harder” to increase the chance of being routed to it.

But back to GPT-4o. Why do many people on Reddit care so much about losing access to that crusty old model? I thinkthis commentcaptures something important here:

I know GPT-5 is designed to be stronger for complex reasoning, coding, and professional tasks, butnot all of us need a pro coding model. Some of us rely on 4o for creative collaboration, emotional nuance, roleplay, and other long-form, high-context interactions. Those areas feel different enough in GPT-5 that it impacts my ability to work and create the way I’m used to.

What a fascinating insight into the wildly different styles of LLM-usage that exist in the world today! With700M weekly active usersthe variety of usage styles out there is incomprehensibly large.

Personally I mainly use ChatGPT for research, coding assistance, drawing pelicans and foolish experiments.Emotional nuanceis not a characteristic I would know how to test!

Professor Casey Fiesleron TikTokhighlighted OpenAI’s post from last weekWhat we’re optimizing ChatGPT for, which includes the following:

ChatGPT is trained to respond with grounded honesty. There have been instances where our 4o model fell short in recognizing signs of delusion or emotional dependency. […]

When you ask something like “Should I break up with my boyfriend?” ChatGPT shouldn’t give you an answer. It should help you think it through—asking questions, weighing pros and cons. New behavior for high-stakes personal decisions is rolling out soon.

Casey points out that this is an ethically complicated issue. On the one hand ChatGPT should be much more careful about how it responds to these kinds of questions. But if you’re already leaning on the model for life advice like this, having that capability taken away from you without warning could represent a sudden and unpleasant loss!

It’s too early to tell how this will shake out. Maybe OpenAI will extend a deprecation period for GPT-4o in their consumer apps?

Update: That’s exactly what they’ve done, seeupdate above.

GPT-4o remains available via the API, and there are no announced plans to deprecate it there. It’s possible we may see a small but determined rush of ChatGPT users to alternative third party chat platforms that use that API under the hood.

Posted
8th August 2025
 at 5:52 pm · Follow me on
Mastodon
,
Bluesky
,
Twitter
 or
subscribe to my newsletter

## More recent articles

* GPT-5: Key characteristics, pricing and model card- 7th August 2025
* OpenAI's new open weight (Apache 2) models are really good- 5th August 2025



This isThe surprise deprecation of GPT-4o for ChatGPT consumersby Simon Willison, posted on8th August 2025.

Part of seriesGPT-5

1. GPT-5: Key characteristics, pricing and model card- Aug. 7, 2025, 5:36 p.m.
2. The surprise deprecation of GPT-4o for ChatGPT consumers- Aug. 8, 2025, 5:52 p.m.

 ai

1494

 openai

329

 generative-ai

1309

 chatgpt

172

 llms

1287

 ai-ethics

207

 ai-personality

22

 gpt-5

4

Previous:GPT-5: Key characteristics, pricing and model card

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
