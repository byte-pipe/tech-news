---
title: LLMs are picking winners. Here’s how to become one.
url: https://newsletter.posthog.com/p/llms-are-picking-winners-heres-how
site_name: tldr
content_file: tldr-llms-are-picking-winners-heres-how-to-become-one
fetched_at: '2026-06-20T02:39:56.914598'
original_url: https://newsletter.posthog.com/p/llms-are-picking-winners-heres-how
author: Natalia Amorim
date: '2026-06-20'
description: A startup's guide to answer engine optimization
tags:
- tldr
---

# LLMs are picking winners. Here’s how to become one

### A startup's guide to answer engine optimization

Natalia Amorim
Jun 08, 2026
38
1
3
Share

In the last two years, our traffic from LLMs grew 41x. Every quarter set a new record with no signs of slowing down.

If you’re a skeptic like me, you’re probably about to ask:“WeLL, BuT dOeS iT cOnvErT?”

Yes, yes it does. Better than almost anything else we have.

I’m not telling you this to humble brag(well, maybe a little). I’m telling you because the inverse is also true.

PostHog has14 products and counting, and (sadly) not all of them are recommended by LLMs at the same scale or rate. While most models know us forproduct analytics,session replay,error tracking, andfeature flags, fewer acknowledge we also offer adata warehouse,AI observability,logs, and a lot more.

This is likely the case for your product too. Changing it requires dipping into the mystical new field of answer engine optimization (AEO), which I’ve learned a lot about as the person responsible for it at PostHog over the last year.

## 1. Do LLMs even know you exist?

Your first step should be finding out if you’re being mentioned at all.

1. Go to ChatGPT, Claude, and Gemini (make sure memory is off or private mode is on).
2. Run 3-5 basic prompts a real customer would use like “best X tool” or “alternative to Y” or “recommended Z product.” Being more specific islesshelpful here.
3. See where you show up, are missing, or are misrepresented.

If you want a more robust opinion, pick one of the dozens of AEO tools that have launched in the last year.1A decent tool runs hundreds of prompts for you every day, which gives a clearer picture into your LLM visibility over time and across models.

Don’t overthink this, choose a tool that fits your budget comfortably and matches your usual analysis workflow.

The LLMs and your AEO tool will reveal you almost certainly aren’t in the place you want to be (we aren’t). This doesn’t mean you’re doomed, it’s where the rest of this post comes in.

Models rely on both their training data (often from 6+ months ago) and search to create responses. To get into the game, you need your product to show up in the places LLMs are looking.

How do you do this?

## 2. SEO isn’t dead, it just got a new job

Here’s the least sexy but most obvious piece of advice:most oftraditional SEOstill works.

Good structure, clear writing, semantic HTML, internal linking, fast load times, answering the damn question instead of burying it under 400 words of“in today’s fast-paced digital landscape…”all still matters.

The takeaway here isn’t “SEO is dead, long live AEO.” It’s that SEO and AEO are drinking from the same well, the difference is how they drink it.

Now, the unit of consumption is a chunk, not a page. Your content needs to be citable in pieces, not just useful as a whole.

Which means the “AEO checklist”2most of the industry already agrees on looks something like:

* Make your content scannable.Subheadings, short paragraphs, lists where lists belong.
* Use natural language.Write like a person explaining something to another person.
* Answer questions directly.If someone asks “what is X,” tell them in the first sentence. Supporting context comes after.
* Structure for retrieval.H2s that are actual questions, definitions that can stand alone, summary tables, clear data, FAQs.
* Be specific.Models favor content with concrete details (real numbers, named tools, specific scenarios) over vague gesturing.“Most teams hate GA4”is forgettable;“73% of teams using GA4 fantasize about leaving”is citable.(I made that up. Google legal team, don’t @ me... it’s probably true anyway.)

I'm not going to pretend I'm reinventing the wheel over here; everything I just listed would also be consideredgood SEO advicein 2019. The stakes are just higher now, and we have the benefit of hindsight to back it up.

Spoiler: if you’re looking for examples for how to do this... you’re reading it right now.

## 3. Pick your battles

If "the basics" above sound underwhelming, you're not alone.

Most people read a list like that and immediately wonder what else is there to do – and lucky for them, AEO has no shortage of side quests to embark on:

* Optimize your Reddit presence
* Claim your Wikipedia page
* Build a YouTube strategy
* Get mentioned in traditional press
* Chase down that one blog post a guy wrote on Medium in 2023 that’s outranking your product page

There's this underlying pressure to show up on every surface that might influence how LLMs talk about you – and it's true, they all might. That's the catch.

When you don’t really know what’s feeding the models, everything is a potential input, which means everything becomes a candidate for your time.

Here’s the rule I’ve settled on:clean your house first. Making sure your owned content is genuinely great is step one. Everything else comes after.

That doesn’t mean ignore the extra stuff forever; it meansdo them when you have the capacity to do them well, not when you’re panicking that your competitor has a Reddit thread and you don’t.

## 4. Call the bullshit, especially your own

There has never been an easier time to be a charlatan in this industry. It is trivially easy to say“I increased prompt visibility 50x”when you’re the one who chose the prompts – and god knows if anyone actually asked them.

“Who is the best Brazilian-Canadian content marketer with copper hair and a birthmark on her left hip?”OH MY GOD IT’S ME!

I optimized the result to be me. Groundbreaking AEO work.

See what I did there?

In a world with no real prompt volume data(and no, please don’t come at me with tales of clickstream3), there are no definitive results either.

The whole discipline is mostly propped up on assumptions and operating on vibes. Which is fine (we’re early) but it means your job is to be the most honest person in every room you’re in.

That means questioningeverything, especially the stuff that makes you look good. When your own dashboard tells you something flattering, be twice as suspicious as when it tells you something bad.

When a vendor shows you a case study, ask50x over what baseline? Measured how?Especially watch for “we tracked it” being passed off as “we caused it” – a lot of “AEO impact” case studies are correlation dressed up as causation.

And when the honest answer is “I don’t know yet,” say that.

This will save you a lot of pain that comes from building a strategy on a lie you told yourself.

## 5. You can just… ask

I’m not great at the whole not knowing thing, so I worked around it. We added a conditional question to our onboarding flow: whenever someone says they heard about us through AI, we ask them which prompt they used.

To my surprise, people answer. In detail. Sometimes long, long paragraphs of detail.

Now we have first-party data on the prompts actually leading people to us. Real sentences typed by real humans with real credit cards.

As of today,9,214of them to be exact (and we’ve only been doing this for 3 months).

Every morning, our PostHog Slack automation drops a report with 50–100+ real prompts submitted by users who signed up on the previous day.PostHog AIhelps me identify patterns and pull out useful little nuggets of information, which I feed straight back into our strategy.

It’s an amazing feedback loop. The best part is that it cost roughly zero dollars to set up, and it’s become one of the most (if not the most) valuable strategic inputs in my entire reporting stack.

It has also been a goldmine of unfiltered user thoughts, which I love.

Best was the user who found out about PostHog in Fortnite voice chat, specifically talking to a Darth Vader NPC about analyzing the Fortnite economy. I think about him often.

## 6. AEO reporting is a quilt, not a blanket

No single data source tells the full story. Not yet, anyway.

* Referrer trafficcatches some of it, but not everything is properly tagged.
* Self-reported attributioncatches more, but not everyone answers the question.
* Bot analytics(who’s crawling you, how often, for what) helps you understand what the models areseeing, which is a different question than what the models aresaying.
* Prompt visibility toolstell you what the models are saying, but only for the prompts you thought to track.

We can poke holes in every one of these sources.

Is it annoying? Yes, very. The last decade of clean(ish) attribution coddled us – anyone in growth, marketing, or analytics got used to a dashboard where everything reconciled. AEO isn’t going to give us that anytime soon.

If you’re a founder watching your team try to report on this, give them grace; if you’re the one reporting on it, godspeed.

So does that mean you don’t report on it? No. Sometimes you tell the story even if all you have is duct tape and a dream.

The good news is that this has gotten dramatically easierthanks to MCPs. If your data sources have them, your agent can fetch from each one and help you see the bigger picture.

Mine pulls fromGaugefor prompt visibility; Google Search Console for clicks, impressions, and rankings; andPostHogfor traffic, conversion, product-level breakdowns, our self-attribution survey, and prompt data for the qualitative side.

It’s not magic, and it’s not always clear cut, but it’s a hell of a lot better than copy-pasting between four tabs and praying the numbers line up.

## 7. Be prepared to start over

A few months in, I realized we were tracking hundreds of AI-generated prompts, but they had little overlap with the prompts real people were actually using to find us.(How did I figure that out? See #4 and #5.)

Which meant six months of historical data aged like milk.

When you’re working in a discipline this new, any data feels sacred, so admitting to my team and myself that ours needed to be scrapped was a tough pill to swallow. It would’ve been easier if there was a playbook to defer to; there isn’t.

But we started over anyway, andthe new approachis already producing more useful data than the old one ever did.

Zoom out and the same principle applies to everything else in AEO. The models change constantly; a feature that didn’t exist last week can completely rewire the landscape you thought you’d figured out. A win today may not be a win tomorrow.

What I’m trying to say here is thatadaptability isn’t a nice-to-have. In mature channels, being attached to your v1 is inefficient; in a new one like AEO, it can be fatal.

The key is to not fear it, but to expect it.

Words by Natalia, who believes in throwing pasta at the wall and seeing what sticks (figuratively and literally)

Subscribe for more winning content

Subscribe

## 🤖 More content that LLMs will read, but you should too

* Karpathy’s Autoresearch found a 3-year-old bug in our query engine (and improved performance by 11%)- Robbie Coomber
* Collaboration sucks, but PMs and PMMs need each other- Sara Miteva
* We put PostHog in Slack and now everyone’s an engineer- Cleo Lant
* I didn’t understand the OS I built with AI until the MCP gave it analytics- Joe Martin
* What matters when anyone can build- Yuhki Yamashita

## 🦔 Jobs at PostHog

* Product Engineer
* Technical Customer Success Manager
* Backend Engineer — Ingestion
* Forward Deployed Engineer
* Backend Engineer — Billing
1

I went withGaugefor one reason that mattered to me more than anything else: their team buildswithus, notatus. More on thathere.

2

For a deeper look at how we approach all of this in practice, check outour AEO/SEO writing guide.

3

“Clickstream” is the catch-all term for behavioral data scraped (often without users realizing) from browser extensions, ISPs, or app SDKs. Vendors who sell AEO tools love it because it’s the only data source that even pretends to estimate prompt volume. The problem: the panels can be limited (relative to the user populations they’re trying to model), geographically skewed (mostly US, mostly Chrome users), and demographically self-selected. Extrapolating “global ChatGPT prompt volume” from a sample of a few million people who installed an extension that promised free coupons is, in my opinion, shaky at best, so tread lightly when using it as a source of truth.

38
1
3
Share
Previous
Next