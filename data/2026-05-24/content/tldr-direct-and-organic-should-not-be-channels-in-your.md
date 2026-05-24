---
title: Direct and organic should not be channels in your attribution reporting
url: https://www.021newsletter.com/p/direct-and-organic-should-not-be
site_name: tldr
content_file: tldr-direct-and-organic-should-not-be-channels-in-your
fetched_at: '2026-05-24T18:00:36.105916'
original_url: https://www.021newsletter.com/p/direct-and-organic-should-not-be
author: Barbara Galiza
date: '2026-05-24'
description: I cover why that's my take, and how to reattribute that traffic
tags:
- tldr
---

# Direct and organic should not be channels in your attribution reporting

### I cover why that's my take, and how to reattribute that traffic

Barbara Galiza
May 19, 2026
9
Share

A short note before the article: this Thursday (May 21st), we’re hosting a webinar onsignal engineering for data professionals. If you’d like to learn more about designing ad platform conversion events, then don’t forget toregister here. (It is free!)

We now return you to your regularly scheduled programming.

Most attribution reports show a clean breakdown of where traffic came from. The problem is that a significant chunk of that breakdown is either wrong or unactionable.

This article covers why direct and organic are often channels you can’t act on and what you can do to recover the signal. My goal here is to share concrete methods to reattribute traffic sitting in ambiguous buckets, and a simple benchmark to know if your data is clean enough to make decisions from.

Subscribe to 021 Newsletter to receive ~1 article a month on the intersection of marketing and data:

Subscribe

## First: what attribution is actually for

It is not to have a report. Arguably, it’s not even about “understanding the customer journey”. It is to know what marketing initiatives to put more budget and what to cut. If your report cannot answer those questions, your attribution is a dashboard, not a decision tool.

## Direct and organic look like answers. But are they?

You cannot increase spend in direct. You cannot build a campaign around it. When direct, organic and referral make up a large share of your attributed traffic, it usually means your tracking has gaps and those gaps got bucketed somewhere.

The report looks complete but it’s not.

### Direct can be a tracking error

Direct is not always someone typing your URL into a browser. It can be a tracking failure. Common reasons:

* UTMs stripped by redirects or link shorteners
* In-app browsers (Meta, TikTok) breaking referrer data
* iOS privacy changes limiting cookie-based tracking
First thing: fix your UTMs

UTM hygiene is the foundation everything else builds on. If your UTMs are broken or inconsistently applied, direct will stay inflated regardless of what else you fix.

### But what if someone did enter your URL and visit your directly?

I’m assuming, in this case, the user did not get a vision that your company exists and went on to visit your site.

What has most likely happened is that they saw your company elsewhere—anything from a marketing initiative to word-of-mouth—and then went on to visit your site.

The touchpoint that your marketing, product and finance teams care about is the one that is not visible.

### Let’s look at organic search. Or is it really?

Organic search is definitely an initiative, but brand search lives inside your organic numbers, and it can changes the interpretation significantly.

I’ve worked with marketing measurement for nearly 10 years. I do not exaggerate when I say most companies’s organic search conversions are usually 70%+ people searching for their brand name. The exception are companies that have programmatic SEO as their bread and butter.

Similarly to direct: if someone searched your name and clicked through, they already knew you. That is not discovery, that is recall. Crediting it to organic search flatters your SEO and hides the channel that actually created the awareness.

Search Console is the right first tool here. If 60% of your organic clicks come from branded queries, your SEO number is overstated by at least that much. Most teams never check.

Subscribe to receive articles on marketing measurement, analytics, attribution:

Subscribe

### What about organic social?

I actually think that’s mostly fine. (But I’m more than happy to be challenged here—so do let me know if you disagree.) There’s some overlap with paid social, but the vanity URL suggestion below helps with the edge case.

## The big question: How to find where your traffic actually came from?

These methods work in combination. Each one closes a different gap. They are ordered roughly by ease of implementation: start with survey data, work toward incrementality.

There are different strategies for reattributing direct traffic 

### Layer survey data on top of click-based attribution

Surveys (post-purchase / HDHYAU) are the easiest way to start.And the easiest way to start with surveys can be a free-text field. No structured options, just an open question. Free text surfaces the channels worth turning into structured options later. Once you see patterns, move to structured answer choices that map to your spend categories.

For structured survey data to work well:

* The survey fires right after signup, not buried in onboarding
* Answer options map to your actual spend categories
* Responses are joined with click-based data, not treated as a separate report

If “other” makes up more than 10-15% of responses, you are losing signal. Review open-text responses regularly to catch emerging channels early.

Reattributing direct traffic can make hard-to-measure channels more visible in your reporting

For a full guide on how to set up and calculate ROAS from survey data,this article covers it in detail.

When this applies: most valuable when direct and unknown together exceed 20% of attributed conversions.

### Use landing pages and vanity URLs as attribution signals

If a user arrives from direct but lands on a page built for a paid social campaign, that visit is probably not organic. The landing page itself is a signal. You can write attribution rules that reclassify traffic based on URL patterns, even when UTMs are missing.

The same logic applies to vanity URLs:

Vanity URLs enable you to identify traffic when there are no UTMs or click IDs

A sponsorship on a show with no click tracking is invisible in your model. A vanity URL makes it visible.

When this applies: most valuable when you run channels where UTMs are unreliable or frequently stripped, like video, podcasts, or affiliates.

### Strip out the noise before interpreting anything

Not all touchpoints deserve credit. Brand search is the clearest example. If someone clicks your paid brand search ad after already knowing you, that touchpoint is not doing discovery work. Including it inflates the performance of channels that did not earn it.

Touchpoints worth considering for exclusion:

* Brand search
* Donor or vendor flows that contaminate your signup data
* Direct revisits from existing users

You are not removing data. You are removing noise.

When this applies: most valuable when brand search is a significant spend line and you suspect it is inflating paid performance.

### Stitch cross-device journeys with identity linking

A user sees your ad on Instagram, opens it in the in-app browser, then converts two days later on desktop. Meta gets no credit. Direct gets all of it.

Emails can help you stitch journeys together

Email-based identity linking closes this gap. If you capture an email earlier in the journey (lead form, newsletter signup, demo request), you can use it to connect pre-signup activity to the eventual account:

1. Create a lead table in your data warehouse with email, timestamp, and source
2. When a conversion has no tracked origin, check the lead table first
3. If a match exists before the conversion timestamp, attribute to that source
4. If not, fall back to your existing logic

When this applies: most valuable when a meaningful share of conversions come from Meta or other in-app browser traffic.

Subscribe

### Run incrementality tests for what tracking cannot reach

Some channels will always be hard to attribute through clicks. Podcast sponsorships. YouTube awareness. Out-of-home. Pausing a channel because it looks weak in click-based reporting is one of the most common and most expensive mistakes in paid media.

Geo holdouts and controlled experiments tell you whether a channel is driving conversions that would not have happened otherwise.If your model attributes 5% to a channel and a geo test shows 15% lift, that gap is worth acting on.

It does not replace your attribution model. It calibrates it.

When this applies: most valuable when you are considering cutting a channel that looks weak in click-based reporting but you suspect is doing more than it appears.

## A simple test for whether your data is clean enough

My rule of thumb for clients: direct and referral combined above 10% of attributed conversions means you have recovery work to do.Getting there usually requires layering several of the methods above, not fixing one thing.

It will never be perfect. Attribution is directional, not precise. You are not looking for truth. You are looking for signal that is good enough to make better budget decisions than you are making today.

Traffic you cannot explain is budget you cannot justify.

## From report to decision tool

A clean attribution model does not tell you everything. It tells you enough. Enough to know which channels are actually finding new users, which ones are taking credit for traffic that was already yours, and where adding budget is likely to compound rather than just add.

In the end, that is the only version of attribution worth maintaining.

If you’ve enjoyed this article, then don’t forget to subscribe to 021 Newsletter for free:

Subscribe
9
Share