---
title: 🧠 AI Checkout is Becoming a Reality | Fintech Brainfood
url: https://www.fintechbrainfood.com/p/ai-checkout
site_name: tldr
content_file: tldr-ai-checkout-is-becoming-a-reality-fintech-brainfoo
fetched_at: '2026-05-06T12:27:33.001595'
original_url: https://www.fintechbrainfood.com/p/ai-checkout
author: Simon Taylor
date: '2026-05-06'
description: AI is reshaping checkout experiences. Walmart ran the largest A/B test in the industry, and the results show conversion is better when the merchant owns checkout
tags:
- tldr
---

* Home
* Posts
* 🧠 AI at the Checkout > AI Checkout

# 🧠 AI at the Checkout > AI Checkout

This is the first moment agentic commerce has anything close to a Schelling point. Plus; Mercury got its OCC conditional approval.

Simon Taylor

May 3, 2026

Your browser does not support the audio element.

Welcome to Fintech Brainfood, the weekly deep dive into Fintech news, events, and analysis. You can subscribe by hitting the button below, and you can get in touch by hitting reply to the email (or subscribing then replying)

Subscribe

### Weekly Rant📣

### 🧠AI at the Checkout > AI Checkout

The merchants are trying to tell you something.

After two years of agent demos, chatbot checkouts, press releases, and “AI shopping” theatre, the market has found its first real answer.

The AI chatbot does not own the checkout.

The merchant does.

On April 24, 2026, Amazon, Meta, Microsoft, Salesforce, and Stripe joined theUniversal Commerce Protocol (UCP) Tech Council

They sit alongside Google, Shopify, Etsy, Target, and Wayfair.

That is every hyperscaler. Every major commerce platform. Every payments network of relevance in the transatlantic sphere. The card schemes (Visa, Mastercard, Amex), the PSPs (Stripe, Adyen, Checkout), the marketplaces (Etsy, Wayfair, Target, Walmart, Best Buy, Home Depot, Macy's, Flipkart, Zalando) — all on the same protocol.

This is the first time the agentic commerce category has agreed onanything.

It’s now clear.

The chatbot does not own the checkout. The merchant does.

The best metaphor is the shipping container.

Before containers, global trade existed, but every handoff was bespoke. Ports, ships, warehouses, and merchants all had their own weird little workflows. Commerce moved, but it dragged.

The container standardized the interface.

It did not own the goods. It did not replace the merchant. It made the whole system interoperable.

UCP is the container for agentic commerce.

### What is UCP, and why does it matter?

The Universal Commerce Protocol (UCP) is an open standard designed foragentic commerce. It acts as a "common language," allowing AI agents (like Gemini or ChatGPT) to interact directly with merchant backends without the user ever visiting a website.

* Discovery:Agents query a merchant’s/.well-known/ucpmanifest to dynamically discover capabilities like loyalty programs, pre-orders, and product catalogs.
* Negotiation:AI and the merchant backend negotiate real-time pricing, tax, and complex discount stacking via standardized APIs.
* Transaction:Secure, API-driven checkout sessions finalize the sale, often utilizing theAgent Payments Protocol (AP2)for verified, one-tap payments (e.g., Google Pay, Shop Pay).
* Fulfillment & Settlement:UCP orchestrates logistics (shipping vs. pickup) and provides post-purchase status updates directly to the agent.

UCP is not a payment protocol. Commerce is everything before and after the transaction. When Imapped the agentic payments landscape in Januarythe protocols broke down into layers.

You’ll note Google has several layers in sync:

* Agent communication layer— how do agents talk to each other? (A2A)
* Mandate layer— does the agent have authority to pay? (AP2)
* Transaction layer— what's being bought, and how does the checkout work? (UCP)

The payment itself still goes through the traditional rails likecards, ACH, stablecoins etc. That’s one of the things that makes agentic commerce so confusing. Not every protocol is trying to do the same thing.

And even in the transaction coordination layer, there’s complexity. MPP and x402 are designed for agents buying online resources (API access, etc.), ACP and UCP are about commerce, how do consumers find, select, and pay for goods and services online.

The core difference between UCP and ACP is who they face.

* UCP: The Merchant owns the checkout.UCP wasco-developed by Google and Shopify, Merchants own the cart. Merchants own the checkout. Merchants remain the merchant of record.The agent is the discovery surface, not the storefront.
* ACP, OpenAI's competing standard, started from the opposite end of the funnel. It began with checkout — Instant Checkout inside ChatGPT— and worked outward toward discovery and fulfilment.

UCP started with the full commerce flow and worked inward to the details. Today the two specs are converging. The difference is the path each took to get there, and which one had the architecture coalitions could trust early

UCP's other clever move was being deliberately layered.

Like TCP/IP, it separates concerns.

* Core checkout primitives sit at the bottom.
* Capabilities (Catalog, Orders, Checkout) sit above.
* Extensions (loyalty, fulfillment, subscriptions) compose on top.

Merchants implement only what they need, and can make it work with any payment method or loyalty integration. As long as they own thenamespace(the .com or equivalent that they’re impacting), they can do what they like with the workflow and protocol.

(That's why every PSP, every commerce platform, and every hyperscaler eventually converged on it. The architecture lets them all extend the protocol without permission.)

The combination of

1. A coherent stack from communication to consent to commerce
2. Being merchant-initiated and owned

Has made UCP an early winner, and a center of gravity for the agentic commerce conversation. There may yet be merit in the “checkout in the LLM” model that ACP was designed for, but it doesn’t yet have traction.

If you’re building a standard, job 1 is to get support for it. And UCP now has that.

The bigger question is if everyone supports it, will it make any difference?

### Is agentic commerce working yet?

The data is mixed.

All the predictions say agentic commerce is the next big thing.

* McKinseysays agentic commerce is a $3-5 trillion category by 2030.
* Morgan Stanleysays $190-385 billion in US e-commerce by 2030 — roughly 10-20% of online retail.

But I can't find evidence that customers are adopting this en masse. Maybe they are. Maybe it's just early. But it’s not hitting the mainstream.

The mainstream is not here yet.

In October 2025, Maximilian Kaiser (University of Hamburg) and Christian Schulze (Frankfurt School of Finance) publishedthe first peer-reviewed studyof LLM e-commerce traffic. They took 12 months of first-party data from 973 e-commerce sites and 50,000 ChatGPT-referred transactions compared against 164 million traditional-channel transactions.

The findings:

* ChatGPT referrals underperformed every traditional channel except paid social
* Affiliate links converted 86% better than ChatGPT
* Organic search converted ~13% better than ChatGPT
* ChatGPT accounted for 0.2% of total traffic across the dataset
* The authors concluded parity with organic search inside a year is "unlikely."

But the early adopters are showing promising signs.

* Attribution:Adobe saysAI-driven traffic to retail is up 693% YoY for the 2025 holiday season — and for the first time, AI referrals are converting 31% better than other channels (vs. 9% worse just three months earlier)."
* Attribution:Shopify saysAI-attributed orders grew 15xsince the start of 2025 — that's the freshest number from their Q4 2026 earnings call."
* AI gives higher conversion:Panxo saysChatGPT converts at 11.4%, beating direct, paid search, organic, email, display, and social.

Two things are true at the same time. AI-referred traffic is growing fast off a tiny base, and the mainstream isn’t here yet.

And that’s OK.

Most people use AI as a better google, that’s showing up in attribution and marketing data, but the conversion jury is still out.

The early adopter merchants are trialling agentic commerce

Except in one specific place. Where merchants own the AI, the data isn't mixed at all.

### Merchant-owned won because it converts

When I wroteThe Checkout is Deadalmost a year ago, ChatGPT had just integrated checkout into its interface. Perplexity and others followed. The obvious question was,how is this going to fly?

Merchants risked losing the customer, losing the data that helped convert them, and losing the signals that flagged fraud. The LLM-as-a-channel approach meant ceding much of the customer relationship and potentially paying some unknown take rate (ChatGPT wanted to charge 2% initially).

Every one of those concerns was real. None of them mattered. Because the only thing that needed to be true for the model to work was that conversion was good.

Narrator:The conversion was not good.

Walmart tested 200,000 SKUs through ChatGPT Instant Checkout.Daniel Danker, Walmart's EVP of AI Acceleration, Product and Design,told WIREDthe conversion wasone thirdof click-out rates. He called the experience "unsatisfying."Two weeks later, OpenAI announced the closure of Instant Checkout — the agent-owned-checkout implementation. ACP itself moved on, evolving toward the merchant-owned model the spec now supports.

Walmart then ran the experiment the other way. They embedded their own assistant — Sparky inside their app (and later as a ChatGPT app),but kept cart, login, and checkout onWalmart.com.

Agentic Commerce in chatbots do not convert as well as owned websites

The results from Walmart'sQ4 FY26 earnings call:

* Half of Walmart's app users have engaged with Sparky
* Sparky users have anaverage order value 35% higherthan non-Sparky users
* Sparky inside ChatGPT converts atroughly 70%ofWalmart.comdirect rates — more than double ChatGPT Instant Checkout's run rate (but not quite as good as the owned channel)

This is the experiment the entire industry needed someone with Walmart's scale and leverage to run.

The control group is the website itself, and the website is still winning, but I don’t think that lasts. Those 1,000s of tiny micro optimizations will come to Sparky.

Walmart didn't use UCP — their experiments predate it. But they ran UCP's hypothesis as a controlled test on the largest retail surface in the world and disclosed the results on an earnings call.

And it's not just Walmart. Tatcha (Unilever-owned luxury skincare) attributes11.4% of total site revenueto its on-site AI assistant, with conversion 3x site average and AOV up 38%. Microsoft Copilot Checkout reports 53% more purchases within 30 minutes when shopping intent is present. The pattern is consistent across every dataset where the merchant owns the AI:

AI by the merchant can work. AI by the aggregator doesn't yet.

There are still some questions the industry will need to work through like:

* Is fraud worse or better with agentic commerce?I can’t find any data on this, and it could go either way. Apple Pay is proud of reducing overall fraud in e-commerce vs other payment methods; agentic commerce could go that way. But fraudsters are always the earliest adopters and will exploit any weak spot.
* Are returns worse or better with agentic commerce?We just don't know — agentic transaction volumes are still too small for return-rate signals to be statistically meaningful. But if your agent yolo bought a bunch of stuff for you, are you gonna hit that chargeback button or are you liable?Target thinks you’re liable. The schemes are still building their frameworks.
* How will attribution work?ACP and UCP webhooks tell merchants what sold and which agent sold it. They tell merchants nothing about discovery, consideration, or whether the sale was incremental versus cannibalized. Retail media networks are about to get very confused.

A lot of this will get solved at the payment network layer, as card networks build their liability frameworks and security models around trusted agents and update how payments work accordingly.

### We're early. We're experimenting. And the cost of trying has never been lower.

When Apple Pay launched, it was optional. Today, it'saround 14% of US online payments, and on mobile, it's table stakes.

AI adoption is near-universal, but AI value capture is still concentrated in a small minority. Like everything in AI, the 1% are getting incredible gains. Most people are using it as a better Google search.

The danger here is complacency.

When the early-adopter crowd is rushing into somethingandgetting value from it, that's your signal to pay attention. These are businesses reacting to actual customer demand.

What the early adopters are doing today will be universal in 10 years.

And it has never been cheaper to experiment or build.

With agentic coding, tooling, and workflows, experiments that used to take months and large teams can be cranked out much faster and at lower cost(assuming your production back end is capable of running experiments and A/B tests).

If merchants get this right, the cost of trying a new checkout flow, a new merchant agent, a new AEO experiment, has gone from six engineers and a quarter to one engineer and an afternoon. That changes the calculation.

The merchants who get this will run twenty UCP experiments in 2026. The merchants who don't will run one in 2027, when the data is already in, and the option is already expensive

(See theEnterprise AI Playbookfrom a couple of weeks ago for pointers on how).

The longer-term question becomes: how do you optimize conversion with AI assistance?

Merchant AI starts with answering questions, building trust, and suggesting upsells. Over time, merchants, AI labs, and everyone else will optimize the conversion, and as that happens, I fully expect AI conversion to outpace existing e-com checkout conversion.

If you buy that hypothesis, then you need to be:

* Discoverable to agents
* Able to build agent-friendly checkouts
* Ready to communicate (merchant-side AI)
* Ready to optimize that experience over time

The merchants who win will run AI on both sides. A consumer agent for discovery. A merchant agent for conversion. UCP is what lets them talk to each other.

### Don't treat AI as just another marketing channel.

Do get UCP-ready. The cost is real but bounded. Being on the wrong side of the next 18 months could be the difference between a great holiday season and being the next category to get SaaSpoacalypse’d.

Nobody knows exactly when this hits.

But the probability of it being an "if" is low.

When your downside is limited.

When your upside is unlimited.

When the cost of trying something new has never been cheaper

The gap between you and experimentation should be zero.

ST.

### 4 Fintech Companies💸

1.Maisa AI- AI Knowledge Workers for Regulated Companies

Maisa has pre-built AI agents for tasks in use cases like trade finance, loan processing, KYC, customer onboarding, and power of attorney. It also allows institutions to build their own “workers” with a BPO like interface. By combining small and large models. They claim to increase automation to 93% increasing capacity for work by 6x.

🧠The company claims to be “regulatory ready.”Which is abigclaim, but they back that up by ensuring every step, of every agent is audited, regularly tested, and overseen by humans. They focus on onboarding, and testing workers in controlled scenarios, and continuing to monitor once deployed. (FWIW, this is the best practice we wrote in theAgentic Oversight Frameworkback in my Sardine days).

2.Ultraviolet Credit- Credit scores for onchain activity.

Ultraviolet provides onchain underwriting by looking at a customers wallet history, and creating a “UV score” based on it. It then calculates an interest rate based on your personal risk profile plus a published benchmark (they don’t say which). Lenders can then buy tranches of capital (junior and senior), from ultraviolets onchain pool. Collections are handled “by a legal framework in every jurisdiction where its available).

🧠This could be huge for the growing global south population of stablecoin-linked neobank users.Kast, Dolar and apps like it have risen to popularity as a global account for everyone else. We haven't really seen undercollateralized lending onchain. But now we have consumer distribution, we could. The open question is collections — how do you enforce repayment on someone whose income arrives as ETH to a self-custodied address? Really fascinated to see this pressure tested over a cycle.

3.Spektr- AI Agents for Compliance

Spektr has pre-built AI agents and an agent builder dashboard for compliance tasks like document checks, beneficial owner discovery, source of funds verification, and ongoing monitoring. Agents return structured risk rationales with policy references that teams can use directly. They also monitor, audit, and suggest improvements for agent performance over time.

🧠Europe focussed with clients like Santander Leasing, Pleo and Mercuryo.There are so many of these now, I wonder if someone will roll them up. The value is almost immediate, and Europe (despite its data privacy obsession) doesn’t seem as terrified about MODEL RISK OMG, before it does anything with agents.

4.Rebind- The Global Euro Account

Rebind is a Euro denominated wallet offering between 5% on EUR and 8% on USD on savings. With 200k users, and 36bn Euro deposited to date users can deposit from any bank account or existing onchain wallet and begin earning.

🧠We had global dollar accounts with stablecoins, why not global Euro?Interesting they’re leading with savings as the core value prop. The website specifically compares rates offered by banks and Revolut vs Rebind. Is this wedge enough to attract users? Interesting too that savings are “deposited in open money markets that maintain higher balances than deposited.” AKA, a DeFi vault. It’s a nice repackaging. But if customers start losing money then what? We’ve seen how markets like Aave can freeze after a hack.

### Things to know👀

1.Mercury receives conditional approval to form Mercury Bank NA from OCC

Mercury announced this week that it had received conditional approval from the Office of the Comptroller of the Currency (OCC) to establish Mercury Bank, N.A., a national bank. It now enters an organization phase to work to obtain final authorization from the OCC, as well as pending approvals from the FDIC and the Federal Reserve.

🧠Mercury now becomes a genuine apples to apples bank competitor.Brex is now at Capital One so gets many of the “being a bank” benefits, Ramp could well hit IPO long before it even considersifit becomes a bank.

🧠Mercury now gets access to Zelle a feature customers wanted.Didn’t expect that to be a big customer demand, but tells you the moat banks had on certain capabilities.

🧠Mercurylaunched a CLI.Command Line Ineterface (CLI) is the new mobile app. CLIs give powerful, localized features to AI agents like having a per-agent-wallet, a policy engine, and initator approver workflow. Instead of a human doing this via a dashboard. They can ask their agents to build all of this for them.

🧠Mercury is and its peers are raising the baseline of customer expectations.Just as mobile apps by Neobanks made mobile a default. Neobanks are now making agent-native a default.

🧠Can you name another company who got OCC conditional approval and launched a CLI in the same week?

2. Other news roundup

* Meta and Stripe are doing stablecoin payouts via Link and Tempo. Meta, the company that once scared the bejesus out of regulators with its digital currency ambitions, is now doing stablecoin payouts to creators using Stripe’s Link wallet. Link is now also a wallet for agents, creating a major mainstream way to give agents payment credentials to buy things.
* Ramp launched procurement agents. That can build an RFP, distribute it, score responses, negotiate on pricing, run security reviews, and then begin contract management with providers.I, for one, hope the agents are kinder than the SAP Ariba portals and procurement teams of old!
* SoFi added 1.1m members up to 14.7m total.They highlighted the launch of SoFi USD and being a “rule of 70” growth company.For all the talk of Nubank and Revolut entering, SoFi is arguably the one to catch.SoFi USD is also the only major bank-backed stablecoin available today that can settle against FedWire. Can they turn that into a durable advantage?
* FIDO alliance to build standards for trusted AI agents. FIDO are the people who built passkeys, the secure alternative to passwords popping up everywhere on the internet.Don’t sleep on this news.This standard could slowly make every agent compatible with simple human-in-the-loop auth.
* Visa pops 9% after strong earnings.Driven by value-added services (VAS), which is now 30% of all revenue. Stablecoins hit a $7bn run rate, and Visa Direct was up 23% YoY.Stablecoin settlement was $4bn annualized last quarter; it’s growingfast.
* My favorite nugget from Sessions though, wasStripe showing a chart of them launching their CLI 7 years ago, and the incredible increase in usage since Q1, since coding agents came along. Say it with me. CLI in the new UI.

### Good Reads📚

1.Designing for Agents

❝

If you spend time in the same corner of X as I do, scrolling past the "How I built a second brain with Obsidian" and "Anthropic just KILLED [insert industry] FOREVER" posts, you've probably also seen the take that UI is dead. And unless a product can be used by agents via an MCP, API, CLI, or something in between, it won't survive. The trend is real at Ramp.

Designing for Agents

Salesforce is killing the dashboard and going agent first. The UI isn’t dying but the 80/20 has flipped. We used to go User → Interface → Database, now its User → User's Agent (e.g. Claude) → Database. But where we’re going is even more interesting: User → User's Agent → Software's Agent → Database.

🧠The art is in the design of how MCPs and skills interact with other agents and software.The author, Teddy Riker gives the example of how Notion’s MCP never needs to be told how to format things, but Slack does, meaning, agents produce ugly outputs in Slack.

🧠Everyone says “build for agents” nobody tells you how.It’s this kind of detail and framework that helps you build better products. Figure out where the generic agent doesn’t understand your data or your workflow, and remove the hidden bits of pain.

🧠I’m tempted to write a whole rant about the ideas I had from reading this post. But I’ve already got CEOs emailing me saying “Why didn’t you do a whole write up about us!”After my recentRamp piece. Well. Honestly, you’re not shipping things nearly as interesting. And also, if you’re at a bank right now trying to figure out AI. There’s 1000x more ROI in reading the Ramp twitter articles than there is inanyconsulting firm. Trust me on that.

### Tweets of the week🕊

### That's all, folks.👋

Remember, if you're enjoying this content, please do tell all your fintech friends to check it out and hit the subscribe button :)

Want more? I also run theTokenized podcastandnewsletter.

(1) All content and views expressed here are the authors' personal opinions and do not reflect the views of any of their employers or employees.

(2) All companies or assets mentioned by the author in which the author has a personal and/or financial interest are denoted with a*.None of the above constitutes investment advice, and you should seek independent advice before making any investment decisions.

(3) Any companies mentioned are top of mind and used for illustrative purposes only.

(4) A team of researchers has not rigorously fact-checked this. Please don't take it as gospel—strong opinions weakly held

(5) Citations may be missing, and I’ve done my best to cite, but I will always aim to update and correct the live version where possible. If I cited you and got the referencing wrong, please reach out

### Keep Reading

View more
caret-right

# Fintech Brainfood

Food for thought about Finance, AI and the future of money.

Subscribe

###### Home

Posts