---
title: 🧠 How AI Creates New Fintech Products and Markets
url: https://www.fintechbrainfood.com/p/ai-customer-problems
site_name: tldr
content_file: tldr-how-ai-creates-new-fintech-products-and-markets
fetched_at: '2026-08-31T17:51:33.577387'
original_url: https://www.fintechbrainfood.com/p/ai-customer-problems
author: Simon Taylor
date: '2026-08-31'
published_date: '2026-08-27T13:00:00.000Z'
description: How AI-created customer problems lead to new fintech products, from token spend and model routing to agent identity, payments and distribution.
tags:
- tldr
---

* Home
* Posts
* 🧠 AI Created New Customer Problems

# 🧠 AI Created New Customer Problems

Solving them is where the next generation of finance products are forming. Token spend, agent identity, and model routing barely existed before AI.

Simon Taylor

Aug 27, 2026

Your browser does not support the audio element.

Ramp recently raised $750m at a$44bn valuation. It probably didn’t need the money, but the round was buying something bigger than impressive growth*. The round bought a coherent story about becoming AI-native.

And the story is credible because it is rebuilding itself around customer jobs that AI created. For example,Router finds the lowest-cost, high-quality modelfor each request and, according to Ramp, saves customers 40%.Stripe is assembling a version of the same stack: payments at the bottom,Metronome measuring and billing for usage, thenOpenRouter routing traffic across more than 400 models. It reportedly paidmore than $7bnfor the top layer.

Every investor, especially the growth investor, is looking for companies that benefit from AI’s rapid take-off and become more durable because of it. They are looking for the beneficiary, and trying not to own the victim.

I spoke to three founders this week. All three were close to raising very large rounds on the basis of being AI-native. All three asked me some version of the same thing:

How should we position ourselves as AI native? What should our product be?

They were asking a positioning question. I think the answer is a product question.

This Rant is my answer.

Fintech Nerdconis BACK. And it might just be the most stacked lineup of speakers ever. Co-founder of Chime, CEO of Figure, CEO of Mercury, CPO of Navan, CEO of Valon. With some incredible names coming…

The kind of speakers no other show gets. One rule: no platitudes.

San Diego Convention Center, November 18–20.

Get your ticket here!

You’ll be in great company: speakers from Chime, Mercury, Figure, Valon and Forward have already joined the guild, and tickets are on track to sell out again.Grab yours here.

A quick map:

1. Where you sit: adopter, beneficiary, or native
2. There’s a ladder of jobs to be done that AI created* Old jobs, done better
* New jobs next to your core
* New jobs nobody’s cracked
3. Why your agent needs a distribution strategy
4. What to build now

### Where you sit: adopter, beneficiary, or native

Clayton Christensen’s most useful idea for this essay is that customers don’t buy your product. They hire it to do ajob.

Jobs to be Done in finance include, file my expenses, reconcile my invoices and help me manage fraud. Those jobs predate AI. Modern models can do parts of them faster, cheaper and with fewer humans in the loop, but the customer woke up wanting the same thing.

AI created a second kind of job too. Watch my token spend. Route every inference request to the best model. Let my agent buy something without giving it my whole identity and bank account.

Nobody had those jobs before AI gave them the problem.

### AI-native describes the product. AI-created describes the demand.

I think about how to become AI native in a 2x2.

* Jobs:Old customer jobs always existed (e.g. manage fraud), and AI-created jobs arrived with the technology (e.g. manage my token spend).
* Companies:A company or product that existed pre-AI, or a company that only existsbecauseof that AI

When you put them together it looks like this?

Old customer job

AI-created customer job

Existing company / product

Nubank / NuFormer

Ramp and Stripe

Impossible without modern AI

Harvey, Hebbia and Rogo

OpenRouter and fal

* Top-left is deep adoption. Nubank uses NuFormer to make better credit decisions, but underwriting is an ancient banking job.
* The bottom-left is whereHarvey, Hebbia and Rogosit: products that could not have existed before modern models, doing legal and financial-research jobs that absolutely did.
* The right-hand side is where the tailwind lives. Ramp and Stripe already had businesses when AI handed their customers new things to buy. OpenRouter and fal only make sense because inference became an industry.

This also means a company can occupy more than one square. Ramp’s spend product is top-left. Its token dashboard and Router are top-right. Stripe’s payments business is top-left; Metronome and OpenRouter drag it across the table. Things rarely fit neatly into a 2x2.

So allow me to throw another concept at you.

I find three labels useful for describing thepostureof the company:

1. Adopters use AI to serve the demand they already had.Maybe they added a co-pilot. There is real value here. They can become faster, cheaper and leaner, but the sales pipeline is structurally the same. This is most SaaS companies that bolted on an agent.
2. Beneficiaries serve those old jobs better and capture new demand AI created next door.Ramp or Stripe is the cleanest example. Spend management remains the core job; token cost management and model routing are new revenue pockets sitting beside it.
3. Natives exist because of the new demand.OpenRouter routes requests across more than 400 models. fal runs generative-media inference at enormous scale. Neither has a business in a world without inference to sell.

The map tells you where the demand comes from.

The jobs tell you where they opportunities might be. Progression to being AI native comes on a ladder: familiar at the bottom, gloriously unsolved at the top. So take a climb with me.

### Pre-requisite: Run yourself with AI

AI-powered operating models change the shape, governance and operating system of a company. Teams build harnesses around employees that plug into internal data, share skills and change who can do what. Product managers and designers ship code. Engineers move further into product. Teams build their own internal tools. (For more, see theAI Operating Model report.)

This is table stakes. It speeds you up. It doesn’t, on its own, change what you sell.

### Rung 1: Old jobs, done better with AI

Some AI-native products serve very old jobs. That doesn’t make them less native.

Compliance screening, document and email reconciliation, legal research and financial reporting were all messy paperwork problems before AI arrived. Beacon, Sardine*, Gradient Labs, Harvey, Hebbia and Rogo use modern models to pull together hundreds of documents and data sources, then produce an answer or manage the workflow. The product would have been impossible a few years ago. The job is ancient.

* I advise Sardine.

### Rung 2: New jobs next to your core

If what you do is manage spend, accounts, or help people make payments, the old customer jobs still exist, but there are some new ones near them too. There are a few flavors of this.

* Job: Help me manage my AI usage.Ramp’s token dashboardis an AI-created job living inside a product that already existed. You might object that a cost dashboard is hardly new.VantageandDatadoghave priced cloud and compute spend for years. The difference is the bill. Nobody had token costs to categorize, forecast or split between COGS and OpEx until AI handed them one. On Ramp, AI token spend grew20.7xbetween June 2025 and June 2026.Metronome, now part of Stripe, sits on the other side of the same job by measuring and billing for that usage.
* Job: Help my agent connect to your product and do work.Companies are shipping a Command Line Interface (CLI) like Mercury, Visa, and Ramp, and the OG Stripe shipped theirs 7 years ago (but noticed a massive spike in usage since Claude Code launched). CLIs are user interfaces that use the command line (terminal) instead of an app or web page. Agents find these much easier to navigate, and they cost far fewer tokens to use. For example, run the Ramp CLI in --agent mode and a transaction comes back as JSON in about 105 tokens. Run the same transaction in --human mode, and it costs 280 tokens of pretty formatting. That is a product surface designed for a customer who isn’t human.
* Job: Help my store be discovered by AI agents.Roughly a third of Gen Z now reach for AI over Google to research what to buy. If your store and SKUs aren’t there, you could be missing out. Companies like Shopify and WooCommerce, and the PSPs that help merchants already in e-commerce, are now optimizing here too.

There’s a whole category of demand AI created right next to what you already do, and your opportunity is to build the surface that serves it, without pivoting your whole business immediately.

But imagine a future where agents make up 80 to 90% of internet traffic, commerce, the economy. How would you reposition your company and its narrative if that’s even some way true? What is the core unit of value you create, and how does it apply to that customer?

For that thought experiment, we have to get away from thinking about AI as a feature you add on top of what you do already.

### Rung 3: New jobs that exist because of AI

There are some problems that didn’t exist before the massive spike in AI, and that don’t come from simplytrying to use AI.

* How can I trust this agent with my data, or the decisions it makes?We’re heading into a world where 3rd-party-developed agents may interact with your business. You need some way to ensure they’re safe, reliable, manage privacy, and that some legal entity is accountable somewhere. The easy model is the agent sits inside some existing SaaS provider you have an enterprise agreement with. But increasingly the agent is the product. It could come from a lab like Anthropic, a startup, or an internal department. I’m seeing companies build or buy harnesses or control planes (likePrimitive) to wrap those agents. Another approach isAIUC, which aims to underwrite and certify agents.
* How do I trust this agent to transact?If an agent appears on your store trying to buy something, how do you understand its reputation, or who its creator was? Did the user authenticate that agent to go buy something? Right now there are emerging standards like Google’s A2A, Visa’s Trusted Agent Protocol, and FIDO is building an identity standard. But we’re stillso early. This is where companies like Natural Payments, Skyfire and A-comm are planting flags, managing the parts of the agentic-commerce workflow where agents actually move money.
* How can I source lower-cost inference and compute?Brex sayscompanies now add their first open-compute vendor within five months of their first OpenAI or Anthropic API charge.Five months.One minute you are paying a model lab for an API; the next you are comparingTogether AI,FireworksandBaseten, deciding where a workload should run, and asking finance how to hedge the cost. AI created a software supply chain and then started building a capital stack beneath it.Nvidia and Wall Streetare trying to mobilize $500bn around that layer.

Source: Brex Benchmark; Brex card + bill pay data, Jan 2021–Jun 2026.

These jobs are larger than features. They cut across products, data, identity and money. Once they cut across products, the question becomes who the customer trusts to sit above them.

### Your agent needs a distribution strategy

I don’t want your agent. I want my agent inside your thing.

Most business customers will eventually run some kind of control plane or harness: one place to orchestrate the agents they own across the tools they use. The CFO’s finance agent, the engineer’s coding agent and the ops team’s procurement agent will be budgeted, permissioned and observed from a layer above the individual products.

Consumers will have versions too. Whether it is Grokbot or Instinct, a new consumer app from OpenAI or Google, or maybe Apple finally makes Siri not shit, something will look out for the user across products.

Garry Tan put the threat to incumbent software perfectly:

Source: Garry Tan on X.

Systems of record already own the data, permissions and distribution a harness needs. Their problem is that a new orchestration layer can sit above them and turn every product underneath into a callable supplier.

That creates three strategic choices:

* Own the orchestration. Become the place where the customer sees, permissions and manages every agent.
* Own a trusted control point.Identity, reputation, routing, procurement and settlement can all hold value even when somebody else owns the harness.
* Become the easiest product for every important harness to call.The CLI, API and agent surface are distribution. (This is the right answer for more of you than you think)

Salesforce and bank cores will not casually surrender the sticky wedges they already own. This is not pure aggregation theory. A system of record can become a harness; a specialist can own a control point; a product can distribute through all of them.

That tension is the point. The prize may be the control plane. It may also be the indispensable thing every control plane needs.

### What to build now, and what nobody has cracked

So, back to the three founders I spoke to.

The answer was always the job. Positioning follows the product.

Find the job AI created next to the value you already deliver, and build the surface for it.

Then decide how it travels. You can own the harness, own a trusted control point inside it, or become beautifully callable from all of them.

That is what re-inventing yourself means. You start by running yourself with AI. You use it to do the old job better. Then you climb towards the jobs that did not exist before models gave customers the problem.

Ramp didn’t reach $44bn by being best at expense management. It got there because investors believe AI can keep creating new demand beside the core, and Ramp has the velocity to catch it.

Pick the job. Pick the surface. Give it distribution.

Start now.

ST.

* (Ramp’s growth is absurd by finance-company standards: TPV (total processed volume) grew 170% YoY through March, its fastest pace in three years, after the business had already become 20x larger.)

If you enjoy this kind of content, I can guarantee you’ll love being in a room of 1,500 other folks who love to go deeper into where finance meets AI. That’s a huge theme for us at this year’sNerdcon in San Diego on the 18th to 20th November.I’m bringing my audience, the operators, the people who read this newsletter. And it’s the perfect place to find your next hire, client, or just get inspired. Let’s make events awesome again.

### That's all, folks.👋

Remember, if you're enjoying this content, please do tell all your fintech friends to check it out and hit the subscribe button :)

Want more? I also run theTokenized podcastandnewsletter.

(1) All content and views expressed here are the authors' personal opinions and do not reflect the views of any of their employers or employees.

(2) All companies or assets mentioned by the author in which the author has a personal and/or financial interest are denoted with a *. None of the above constitutes investment advice, and you should seek independent advice before making any investment decisions.

(3) Any companies mentioned are top of mind and used for illustrative purposes only.

(4) A team of researchers has not rigorously fact-checked this. Please don't take it as gospel.

(5) Citations may be missing, and I've done my best to cite, but I will always aim to update and correct the live version where possible. If I cited you and got the referencing wrong, please reach out

### Keep Reading

View more
caret-right

# Fintech Brainfood

Food for thought about Finance, AI and the future of money.

Subscribe

###### Home

Posts