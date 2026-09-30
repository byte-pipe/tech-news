---
title: The Internet has a second audience | Cloudflare Blog
url: https://blog.cloudflare.com/agentic-web
site_name: tldr
content_file: tldr-the-internet-has-a-second-audience-cloudflare-blog
fetched_at: '2026-09-30T22:51:00.495777'
original_url: https://blog.cloudflare.com/agentic-web
date: '2026-09-30'
published_date: '2026-09-30T12:58:00.000Z'
description: More than half the traffic reaching sites on Cloudflare is now automated, and AI agents are the fastest-growing part of it. We're giving site owners the tools to see who's visiting, decide who gets in, and charge for access.
tags:
- tldr
---

For most of its history, the Internet had one audience that paid the bills: people. We read the articles, saw the ads, and bought the subscriptions. Bots were always there, but they were mostly large, automated operations that didn't view ads, pay for anything, or read in any meaningful sense.

That's changing fast. At the end of 2024, Cloudflare handled an average of 63 million HTTP requestsa second. Today, it's almost doubled to 115 million, with peaks above 150 million. Over the past year, daily requests from AI agents on our network grew by more than 1,700%. This year, for the first time, more than half of Internet traffic wasn't human.

The human web didn't shrink to make room. A second audience arrived alongside it: agents, software acting on behalf of people. They sit somewhere between humans and traditional bots. They don't respond to ads, but there's usually a person behind them with a job to get done. For businesses that learn to serve them and capture value from them, agents are additive. For those that don't, they're extractive.

What our customers need hasn't changed: to be discovered, to tell great stories, to build great experiences, and to sell. What's changed is that more than half your visitors are now software. Our job is to help you serve both audiences.

## More traffic, less revenue

For thirty years, the web ran on one arrangement: you let search engines crawl your site, they sent you visitors, and you turned those visitors into a business. Being found and getting paid were the same thing.

AI has caused this delicate balance to break down. Now, answer engines read the page and give the reader a summary. This costs websites bandwidth without leading a human to a website where the ads or payments happen. The machines kept coming, and the audience that paid for the web stopped reaching those sites. Some of the most heavily crawled categories, like Retail, Computer Software, IT & Services, and Financial Services, have seen human traffic decline as much as 40% in less than one year.

The result is that revenue per request is falling while costs are rising. Every automated request still costs bandwidth, compute, and origin capacity, and a growing share of those requests carry no referral, no ad impression, and no subscription. Our first instinct was to block all automated traffic. Last year we recommended blocking AI training crawlers on new domains so site owners could at least say no to their content being used to build models. In Spring 2025, 22% of the crawler requests we saw were for AI training (according to the crawlers’ stated purpose). By June 2026, it was 52%. The problem is a blanket “no” is not a sufficiently nuanced approach for the Internet economy being built right now.

The opportunity is there to cater to agents. Get it right, and you are at the forefront of a new business model. Get it wrong, however, and the results will be the same as they were for generations of websites that were on the wrong side of search engine algorithm changes.

## Some of that traffic is a customer

An agent booking a table, comparing insurance quotes, or buying a dataset for a researcher is a customer. It just isn't a human one.

The fastest-growing part of automated traffic is no longer crawlers. It's agents: software fetching pages on a person's behalf, often because the human asked a chatbot something. That agent traffic follows human routines, with a weekly rhythm and a dip over the summer holidays. Turn an agent away, and you may be turning away the person who sent it.

Agents also behave differently from training crawlers. A training crawler collects your pages to build a model. An agent comes back each time someone asks about that content, so this traffic grows with how many questions people ask, not how much you publish.

You can't do business with an audience you can't see, can't tell apart, can't set terms for, and can't charge. Until recently, for most of the web's non-human traffic, none of those four things were possible.

### See who’s really visiting

"AI bot" no longer means anything useful. What matters is what a bot does. Cloudflare’sAI Crawl Control,Business Insights,andBotBaseshow site owners who is crawling, what they take, what comes back, and which of your URLs they want most.

A bot's name is only worth something if you can trust it. WithWeb Bot Auth, operators, including OpenAI, Google, and AWS, cryptographically sign their agents' requests, so a site can tell a real agent from an impersonator without guessing from IP addresses or user-agent strings. We see more than 500 billion verified bot requests each week.

### Set your terms

In July, we replaced the single "block AI bots" switch with separateSearch, Agent, and Training controls, available on every plan, including Free. The data showed why that distinction was needed. Fewer than 1% of sites on Cloudflare block search crawlers, while 17% block training. Site owners were never trying to hide. But with the rise of agentic traffic and the new ways agents use information, they suddenly had no transparency into, or choice over, how their content was being used. Being found no longer ensures they get paid, and they want to be found without being exploited.

That’s particularly difficult in the case of mixed-use crawlers. When one bot does both search and training, refusing one means refusing the other. On September 15, we shippedDisallow AI Training. It keeps you indexed for search while using crawler-specific mechanisms to instruct the operator not to use your data for training. Apple, Google, and Microsoft have committed to honor it.Cloudflare Radaralso publicly tracks crawler behavior.

New domains now see recommended configurations based on how the site makes money rather than what piece of software is visiting. For ad-supported sites, you can easily disallow training and block agents on pages that carry ads, because an ad only pays when a person sees it. You can change any of these settings at any time.

### Get paid

In August 2026, we describedthe Agentic Internet we're buildingas readable, discoverable, callable, and payable. The last word, payable, is the one that determines whether the open web can fund itself. The web needs a way to say ‘yes, if you pay’instead of a binary ‘yes’or ‘no’.

The licensing market shows both how much demand there is and where the gaps are. More than 50 publisher-AI deals have been signed since 2023. Nearly all of them are bespoke and bilateral, between large publishers and large AI companies. They prove content has value. But they don't reach most of the web, and they don't reach most buyers.

Not every asset should be sold the same way. High-value content and datasets need a trusted network, where buyers are identified and report how the work was used. Services like APIs and MCP tools don’t work like that: every request is the use.

So we're building for both.

Pay Per Usereaches the sites that direct licensing can't. Most publishers will never get a bespoke deal with each AI company, and no AI company can negotiate with millions of sites. Pay Per Use is the bridge. It doesn't charge for the crawl. It pays when content is actually used. Every buyer is a verified crawler, which is what makes this a trusted network, and each one defines what counts as use and what it will pay.

Publishers see the offer, choose whether to opt in, and are able to opt out whenever it stops working for them. The buyer reports each use, Cloudflare checks those reports, then bills the buyer and pays the publisher. The reporting matters as much as the payment. Publishers see what was used, when and what they earned, and, where the buyer reports it, information about which questions surfaced their work. Licensing deals rarely show any of that. It creates a feedback loop: publishers learn what people are actually asking for, and from that can decide what to cover, what to update, and what to make readily available to agents.

There won't be one definition of use. A search engine citing a source, a research agent quoting a passage, and a shopping agent completing a purchase create different kinds of value, and each will want its own business model. Buyers can participate via multiple business models using the same rails, with no new integration for publishers. Take a trade journal for marine engineers, with a few thousand subscribers and little prospect of an AI licensing deal. It gets paid by every participating AI company that draws on its work.

Monetization Gatewaycaptures value that has never had a way to change hands. Accounts, API keys, and subscriptions work for customers you already know, not for an agent that wants one lookup from a service it has never used before. Our closed beta allows eligible U.S. Cloudflare customers to put a price on anything that passes through us, using the Rules language they already know. When a rule matches, we return an HTTP 402 Payment Required using the open x402 protocol, and the agent pays the seller directly.

That does more than recover lost revenue. Agents are customers in their own right: they pay for the data, APIs, and tools they use, whether the request is the whole purchase or one step in a larger task.

Monetization Gateway prices per request, per query, or per token, at fixed or capped prices. A sports statistics site built on ads can charge a fraction of a cent each time an agent asks "who leads the league in assists?" When we announced Monetization Gateway, thousands of sellers joined the waitlist, and their most common request was "charge agents, not humans." We're also our own first customer. Cloudflare's AI Gateway uses Monetization Gateway to let agents pay for inference, so we find the rough edges before our customers do.

For buyers, both products beat a block page: reliable access, and a way to reach millions of sites instead of one licensing deal or API key at a time. Every paid request leaves a receipt showing what was bought and that it was paid for.

Both Pay Per Use and Monetization Gateway are bets, built with customers on shared primitives: identity, metering, pricing, settlement, and analytics. They work together, so a publisher can disallow training, allow search, earn from AI answers, and charge agents per article from one dashboard. Pricing and discovery aren't solved yet, which is why both launch as betas, shaped by real customers and real transactions.

### Make every request cheaper

Payment is the answer to falling revenue. Rising cost is a different problem, and much of it is simply waste. Most crawlers still download pages built for humans, again and again, to extract a few paragraphs of text. Too often, bots crawl sites that haven’t changed since the last attempt. That burns bandwidth for the site and compute for the crawler, and it happens before any answer is written. We’re working with our customers and the crawlers on tools that will help. Today, you can see the bandwidth consumption used per operator in our dashboard.

In July, we announced ajoint research project with OpenAI, a first-of-its-kind pilot to explore how insights from Cloudflare’s global network can help AI search engines discover and index relevant content on the open web more efficiently and effectively. We’re planning to share our initial results in the next few weeks.

For our customers, we’re shipping tools and one-click experiences to make their sites optimized for this new kind of traffic.Markdown for Agentslets agents read a page without the additional styling meant for human eyes, andWebMCPlets a site expose actions directly instead of making agents guess which button to press.

## Why build on Cloudflare

More than 20% of the web sits behind Cloudflare’s network, and so do nearly 80% of leading AI companies. We see both sides of this market. We build the rails for visibility, identity, controls, and settlement, and let the market work out what things are worth.

The old deal is gone, and the new one is still being written. Together we can shape what happens next.

In one version, a few companies control how agents find things, prove who they are and pay, and everyone else routes through them. In the other, those pieces are open standards anyone can implement, and a site of any size can set its terms and get paid. We prefer the latter.

That's why these rails run on open standards like x402 and Web Bot Auth, so anyone can build on them. Domain owners choose their own identity providers, their own payment processors, their own agent partners. Cloudflare is one option, not the whole stack.

For decades, the web was paid for by the people who visited it. Now the software visiting on their behalf can pay its share too.

## Related tags

Agents
AI
AI Bots
AI Search
Birthday Week

Follow on Social Media

* Cloudflare

## Subscribe to receive notifications of new posts

Email address

We’ll never share your email address.

Subscribe

Thanks for subscribing! Check your inbox to confirm.