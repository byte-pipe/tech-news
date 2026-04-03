---
title: 'Build in Public: Day Zero - DEV Community'
url: https://dev.to/olgabraginskaya/build-in-public-day-zero-end
site_name: devto
fetched_at: '2025-11-06T19:33:43.698544'
original_url: https://dev.to/olgabraginskaya/build-in-public-day-zero-end
author: Olga Braginskaya
date: '2025-11-01'
description: A few weeks ago we built an agent called WYKRA for the Real-Time AI Agents challenge powered by... Tagged with ai, buildinpublic, development, saas.
tags: '#ai, #buildinpublic, #development, #saas'
---

A few weeks ago we built an agent called WYKRA for the Real-Time AI Agentschallenge powered by Bright Data and n8n. It was a small experiment that could accept a natural-language query like “I run a small bakery in Barcelona, find influencers who talk about bread here” and return relevant Instagram profiles with context.

When the challenge ended, I assumed the idea would just stay a hackathon thing: fun, useful and then forgotten like most weekend projects, but it didn’t go away. It kept sitting in the back of my mind, annoying me in that “ugh, maybe this is actually worth building” way. So I started digging, reading Reddit threads, founders’ comments, marketing groups and small-business discussions, and the same pattern kept showing up: finding relevant voices and communities online is still weirdly painful.

Right now the market looks like this:

* outdated influencer spreadsheets
* overpriced “databases” with questionable accuracy
* agencies that charge startup-unfriendly money
* or doing it manually: hashtags, profile hopping, too many tabs, mild existential crisis included

That’s… not great. And the fact that people still DIY this process in 2025 says a lot.

Instead of letting this idea quietly die or locking it behind a login like Yet Another AI Tool, we decided to build it in public, to make something genuinely useful, contribute to the open-source community and spend the next three months developing it out in the open.

### What problem this is actually about

The first version focused on Instagram, but WYKRA was never really about a single platform or even the narrow concept of “influencers.” The problem is broader: the internet is full of people, places and communities that shape taste, trust and attention, and it is incredibly inefficient to find and evaluate them manually.

Sometimes those voices are creators. Sometimes they are chefs, small business owners, reviewers, niche experts or even local shops on Google Maps. Whatever the format, the problem is the same: you need to know where attention lives in your niche, who influences it and whether they are worth your time.

This matters for marketers, indie founders, small business owners, creators and anyone trying to reach the right audience without spending hours scrolling through platform search. In simpler terms: help me find who to talk to if I want to grow without drowning in tabs and spreadsheets.

### Early lessons from the first attempt

Even in its scrappy challenge version WYKRA showed something real. It turned out to be surprisingly straightforward to pull public profile data throughBright Dataand feed it into a model that produces a meaningful summary. Once you give the model good input, the analysis is fine. That part was not the problem.

The difficult part appeared one step earlier: actually finding the right accounts.

“Show me people in Barcelona talking about bread” sounds simple, until you try to automate it. Instagram hashtag discovery doesn’t behave like it does inside the app. Bright Data doesn’t currently support direct Instagram hashtag search there. We tried routing discovery through Bright Data Google Search API; sometimes it works beautifully, and sometimes it returns nothing useful. That inconsistency is the real challenge right now.

There is also the question of performance. Scraping and analyzing a meaningful number of accounts can take between five and fifteen minutes. Technically it is fine for deeper research, but will a user wait that long? Should we cache results and gradually build our own collection of verified accounts? At which point “real-time” becomes “realistic time with sensible engineering decisions” is still open.

We also hit another very real constraint: AI is not cheap. Both Claude and Gemini have strict rate limits when used directly and inference cost adds up quickly once you move beyond toy examples. We will likely need to experiment with options like Anthropic’s prompt caching and explore whether any providers offer grant programs or free-credit tiers for open-source AI projects. I know a lot of people use OpenRouter for multi-model access and softer rate limits, so we may explore that route too. If you’ve already gone down that path and have thoughts or warnings, I’d honestly love to hear them, no need to reinvent pain someone else already survived. Part of this journey is simply figuring out the most reasonable way to run this without burning a hole in the budget.

And finally, there is the business side. Running an agent like this online at scale will never be free, so we will need a clear pricing model once the hosted version goes live. The current idea is simple usage-based tiers, so individual creators, small teams and curious experimenters can use it without pain, while heavier workloads help cover compute costs. Self-hosting will remain free; the hosted version exists so the project can sustain itself instead of collapsing under invoices.

These are not issues we want to hide. They are simply part of reality and we plan to address them publicly rather than quietly patching things. On top of that, n8n worked well for a hackathon, but it is not the right foundation for an open-source tool. The cost model creates friction and a custom backend will make it possible to run the agent locally or fork it freely.

So the next phase is not only about polishing a prototype. It is about understanding discovery, caching, performance and product boundaries step by step, in public, without pretending that we already have all the answers.

## Where we are heading (not a strict roadmap, just direction)

The next step is to turn WYKRA from a hackathon setup into something practical. We will replace n8n with a real backend, make the agent easy to run locally and document decisions as we go rather than after the fact. The goal is to support more than just Instagram by trying different platforms, search approaches and data signals, depending on what proves reliable.

We will move in small, testable steps: stabilize the core, add sources beyond Instagram, keep what works and drop what does not.

We also found an actual marketer who does influencer research for a living, and we plan to annoy them with questions so we build something grounded in reality, not in developer imagination.

We’ll share weekly updates on Dev.to and keep the process open. Community channels are still TBD - likely Discord or Slack, but GitHub issues may be enough at the beginning. The point is to stay accessible, not over-engineer the “community infrastructure” before there is one.

For context “we” here is just two people: me, Olga - a senior data engineer and data blogger - and my brother Alex, a full-stack engineer.(And if you enjoy following technical builds, my personal blog is here:Oh That Data Girl)

### How to follow and join the journey

The repo is here:https://github.com/wykra-io/wykra-apiIt’s empty right now on purpose, we’re starting clean and building it piece by piece.

If you’re curious, feel free to star it or check back in a week to see what changed. I’ll also share updates here and on Twitter:https://x.com/ohthatdatagirl

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
