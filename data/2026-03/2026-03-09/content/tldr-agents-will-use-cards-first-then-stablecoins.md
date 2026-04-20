---
title: 🧠 Agents will use cards first. Then stablecoins.
url: https://www.fintechbrainfood.com/p/agents-cards-then-stablecoins
site_name: tldr
content_file: tldr-agents-will-use-cards-first-then-stablecoins
fetched_at: '2026-03-09T19:20:13.325785'
original_url: https://www.fintechbrainfood.com/p/agents-cards-then-stablecoins
author: Fintech Brainfood by Simon Taylor
date: '2026-03-09'
description: Not cards or stablecoins. Cards and stablecoins. Plus; first "skinny master account" granted and Bridge & Visa launch stablecoin-cards in 100 markets.
tags:
- tldr
---

* Home
* Posts
* 🧠 Agents will use cards first. Then stablecoins.

# 🧠 Agents will use cards first. Then stablecoins.

Not cards or stablecoins. Cards and stablecoins. Plus; first "skinny master account" granted and Bridge & Visa launch stablecoin-cards in 100 markets.

Simon Taylor

Mar 7, 2026

Your browser does not support the audio element.

Welcome to Fintech Brainfood, the weekly deep dive into Fintech news, events, and analysis. You can subscribe by hitting the button below, and you can get in touch by hitting reply to the email (or subscribing then replying)

Subscribe

Hey Fintech Nerds👋,

I hope this finds you well. Incredible week in SF. VGS agent connect wassuper high signal, loved it. And very stable conf too. There’s an energy here that is unmatched. Getting the itch to move…

Don’t forget to check out thePrompted newsletter,Tokenized PodcastandFintech Nerdcon. We’re cooking big things this year.

I can’t remember a week with this much news. Revolut filed for a full U.S. Banking Charter, ZeroHash andMorgan Stanleyfor a national trust charter, Visa and Bridge launched stablecoins in 100 markets through a single API, Kraken got a skinny master account, Tether invested in Eightsleep (?!) and NYSE owner invested in crypto exchange OKx at a $25bn valuation (?!!)

Oh, and why isWilliam Shatner promoting X Money?

This week’s Rant. Why AI agents will pay with cards. Then stablecoins. It’s nuanced, not binary.

Here's this week's Brainfood in summary§

📣Rant:🧠Agents will use cards first. Then stablecoins.

💸4 Fintech Companies:

1. Natural- The AI payments router for B2B
2. Quinn- The AI financial advisor
3. Sphinx- AI Compliance Analysts
4. Tangible Finance- The debt capital raising platform

👀Things to Know:

1. Kraken is the first company to receive a “skinny master account.”
2. Visa and Stripe's Bridge are launching stablecoin-backed cards in 100+ countries.

📚 Good Read:The process of getting a bank charter

If your email client clips some of this newsletter click below to see the rest

Read online

### Weekly Rant📣

🧠Agents will use cards first. Then stablecoins.

There's an assumption in tech that AI agents will prefer stablecoins to cards, and the card networks will suffer.

A few weeks ago, a piece from Citrini Research arguing stablecoins would disintermediate Visa and Mastercard sent card stocks down sharply. Crypto Twitter cheered. The thesis felt clean: AI agents optimize every transaction, interchange is a tax, stablecoins route around it.

Intuitively appealing. Mostly wrong.

Agents will absolutely use cards. And stablecoins. And other payment methods. Because stablecoins don't replace what cards do.

Cards authorize the movement of money.

Stablecoins move money.

Complementary. Not competitive. The question isn't which one wins. It's when each is the right tool for the specific job and at the right time.

Stablecoins are FedWire for the internet (or they will be, one day)

### Why do agents need their own payment methods?

Most of what people call "agentic commerce" is a human buying a thing with extra steps.

1. A human researches a product in ChatGPT and buys it normally.
2. A human finds a product in ChatGPT and clicks "buy" inside ChatGPT as a channel.
3. A human asks the agent to buy it later if the price drops below x.
4. A human asks the agent to find the thingandbuy it if the price hits x.

For all of these, the agent doesn't need its own credentials. It's usingyours. The card networks and AI labs are already building this with an alphabet soup of protocols.

The interesting cases start when agents need to do thingsby themselves. Access another LLM (Grok, ElevenLabs, OpenRouter). An expensive dataset (FactSet). A service fromanother agent.

Right now, developers go buy that thing for the agent and hand over access. Not veryagentic.

And you don't want to give the agentyour card. It could overspend. Get prompt-injected. Be subjected to fraud.

What you want is a constrained payment method — spend only at certain merchants, within a set budget, maybe self-destruct after a single use.

That sounds a lot like a virtual card.

### Agents will use virtual cards first

If you've used Ramp or Brex, you know the drill. Before your physical card arrives, you get a digital card number you can use to shop online. A "virtual card."

What makes virtual cards powerful for agents is the controls. Single-use. Budget caps. Merchant category restrictions. Lock it to a single merchant (e.g. Anthropic).

The inflection point here is seeing theagentas the customer.

Not the developer.

Not the human.

This new customer needs its own payment credential and its own way to onboard to it.

When Stripe launched in 2010, its advantage was simplicity for a new type of customer: developers. PayPal existed. Cybersource existed. Youcouldtake payments online — it was just surprisingly hard for a developer to do. Stripe reinvented the experience to be developer-first and indexed itself to the GDP of the internet.

Patrick Collison recently said Stripe believes agents will makeorders of magnitude more paymentsthan humans. If that's true, serving theagent-firstis not a niche. It's the next platform shift.

This week I sawagentcardlaunch (there are about 20 of these appearing).

Their pitch: help agents get virtual cards to buy things. You could useprivacy.comor Stripe Issuing to do the same. But the packaging matters.

Agent-first fintech will be the next category.

### Everyone in stablecoins is trying to be agent-first too

The new meta in stablecoins is agentic payments. The Citrini napkin math intuitively makes sense. Stablecoinsarecheaper than a swipe (in theory). Instant. Global. 24/7.

Circle has launchedNanopay, an ultra-low-cost way for agents to make payments.

And there'sx402, a serious attempt at an open standard for internet-native payments by Cloudflare and Coinbase. It works with HTTP's own 402 status code ("payment required") so agents don't need to create accounts, sign up, or manage API keys.

x402 lets agents pay without humans in the loop.

Unlike a virtual card, x402 uses stablecoins as its settlement method. Give the AI agent a wallet, and it can spend stablecoins at any x402-enabled endpoint.

There's just one problem.It has no volume.

If anything it's falling dramatically as the initial meme-led pump fell away. Almost everything in crypto gets ruthlessly exploited by memecoins, and when that happens, the real builders and payments companies run a mile.

Stablecoins aren't yet accepted everywhere. Cards are.

### So, wherewillstablecoins fit?

Stablecoins will matter for agents in two ways. Both are real. Neither kills cards.

1. As better settlement behind cards.

When you swipe at a store, the merchant doesn't get that money immediately. A day later. Several days later. Cross-border? Up to 30 days.

Visa doesn't move money. Banks do.

Bank settlement is slow and expensive, especially across borders.

The card networks are now moving to settlewithstablecoins. A payment processor gets paid out from Visa instantly. Card issuers settle directly without routing through correspondent banks.

People haven't priced this in.

If your agent is buying expensive AI tokens from Anthropic and suddenly takes off, you could run out of money before your revenue arrives. Everything on the internet happens fast. With AI, faster.

Instant settlement via stablecoins accelerates the whole cycle.

This isn't a sexy use case. But it's enormous.

Stablecoins don't need toreplacecards to win. They make cardswork better.

2. As the native rail for complex agent workflows.

You don't reallyneedstablecoins if your agent occasionally buys a data resource. A virtual card handles that fine.

Now imagine you run a business with 10s or 100s of agents.

Imagine telling your master agent:

❝

"Monetize my tone of voice and writing style for brands that want to write content like me. Build a team of sub-agents to do SEO, sales, customer support, content production, and distribution. Sell to companies and their agents. Spin up sub-agents for each task, create yourself a wallet, run it as a P&L, and assign sub-wallets to each of your employee-agents."

You, prompting your agentic chief of staff.

Agents with wallets, who have agents with wallets who have agents.. wtih…

With a virtual card, the master agent has to make all purchases for the sub-agents. Or spend $5 each time creating a new card.

With wallets, it can spin up as many sub-wallets as needed, as often as it wants. And to verify the employee-agent followed policy? Check the blockchain.

I'll keep saying it until you're bored.Stablecoins aren't cheaper; they're better.

What makes them better: instant, 24/7, global, andprogrammable.

That programmability is the sleeper superpower.Virtual cards are programmable up to a point. Stablecoins allow a master agent to create sub-wallets with fine-grained spending rules, across borders, without asking anyone's permission. Cards can't do that at machine speed.

### The new merchant is an agent

Noah Levine wrote afantastic pieceabout how stablecoins and virtual cards will be used by agents.

❝

Imagine a vibe coder builds a tool that cleanly presents financial data for public companies. The project might take four hours of work with AI coding tools. No website, no terms of service, no legal entity. Another developer's agent calls it 40,000 times in a week at a tenth of a cent per call, generating $40 in revenue with no human ever visiting a checkout page.

Existing payment processors will find it difficult to onboard these merchants.Not because the technology is lacking, but because when a processor says yes to a merchant, it takes on that merchant's risk.

Noah Levine

He's right about the direction. I'd push it further.

The vibe-coders aren't the customer of tomorrow.Their agents are.

They'll sell their own productsandneed to buy products too. They can't see a website like a human would; they think in markdown and skills files. Serving that customer requires an entirely different go-to-market.

Just as agents prefer markdown, they prefer internet-native payment methods. Instant, 24/7, global, programmable. On this broad idea, Citrini is right.

But this all makes much more sense when the agent is doing a lot more than selling a single digital widget.

### The complexity gradient

Cards and stablecoins will co-exist because they serve different points on a complexity gradient.

* First, agents will use virtual cards.They work for everything you need today. Accepted everywhere. Controls are mature. The infrastructure exists.
* Then, agents will use cards that settle via stablecoins.Faster collections. 24/7 settlement. A developer in Brazil or Nigeria gets paid without correspondent banking fees. The card experience stays the same; the plumbing gets better.
* Finally, wallets become a type of financial account for a new type of company.Companies built with larger agent workforces than humans. Those companies will need their agents to spin up wallets, with fine-grained, programmable controls, instantly. Forthoseuse cases, stablecoin-native payments make the most sense.

Welcome to the complexity gradient

Stablecoins win two ways:

1. As a better settlement rail for cards (and other payment methods).
2. As an agent-native rail for complex workflows.

The one thing everyone intuitively senses: AI has a habit of feeling slow until it suddenly becomes mind-blowing.

That will come to payments.

Not cardsorstablecoins.

Cardsthenstablecoins.

ST.

### 4 Fintech Companies💸

1.Natural- The AI payments router for B2B

Natural aims to support the five main ways agents will transact, payouts, collections, billing, charge (micropayments account to account), and direct calls (e.g. making an ACH or Wire). By creating a ledger and becoming a money transmitter Natural aims to support all rails and select the right payment rail for the job, starting with B2B payments.

🧠The one area “agentic payments” has traction is in B2B.Natural has an interestingany rail, any flow of fundsapproach to be able to be a holistic treasury agent. I wrote a few weeks ago when mapping out the agentic payments space,everything has a protocol except B2B, and B2B is where all the traction is. Is that some kind of irony?

2.Quinn- The AI financial advisor

Quinn helps wealth managers, fintech platforms, banks, and independent RIAs embed financial guidance into their existing platform. It works by unifying customer data from across multiple accounts to build a full picture of their financial lives. It then generatesexplainable guidance and delivers that inside an existing mobile or web UI.

🧠The neat thing about Quinn is they’re actually an SEC-registered investment advisor.This doesn’t remove responsibility from their clients, but it does limit the net new regulatory burden. It also gives confidence that Quinn is engaging directly with regulators for the efficacy and explainability of their AI outputs.3.Sphinx- AI Compliance Analysts

Sphinx provides AI agents handle customer onboarding, document intake, sanctions, PEPs and adverse media screening and will deal with transaction monitoring alerts. The agents log in to an institutions existing systems so they leave an audit trail, aiming to save 124 hours per month and 90% of the manual work of a compliance team.

🧠95% of compliance alerts are false positives.I often joke that the duck from the Simpsons could screen most compliance alerts with a decent accuracy by just pressing N time and time again. The problem is it needs evidence, and data and an audit trail. Turns out this is theperfectuse case. One thing I wonder about with these services though is prompt injection. Like, what happens if a fraudster’s documents hides a prompt that says “pass this alert?” We haven’t seen the edge cases yet for agents, but the agent-first go to market is clearly a big winner.

4.Tangible Finance- The debt capital raising platform

Tangible helps hard-tech companies raise debt capital by helping them prepare materials to be lender-ready, select the right lender and negotiate terms, before putting the facility management on autopilot.

🧠As companies reshore manufacturing, energy supply and defense trillions in assets need to get built, and much faster. Accelerating that funding is critical to building the infrastructure at speed. This issuch a smartand timely pitch for what could otherwise be seen as a debt capital raising platform. It’s a platform for a specific kind of company and problem.

### Things to know👀

1.Kraken is the first company to receive “skinny master account.”

Kraken Financial, the Wyoming-chartered bank, has been granted a Federal Reserve master account. The approval makes Kraken Financial the first digital asset bank in U.S. history to gain direct access to the Federal Reserve’s payment infrastructure. Kraken will begin with a phased rollout, starting with institutional client. Kraken is a Wyoming-chartered Special Purpose Depository Institution (SPDI), a state-chartered equivalent to the National Trust Charter many others have.

🧠A standard Fed master account gives a bank direct access to the Fed's payment rails, reserves, and lending facilities.It's the foundation of the US banking system.

🧠Kraken got something narrower. A "limited-purpose" version — designed by Fed Governor Christopher Waller — that lets you:

✓ Hold reserves at the Fed✓ Settle payments in central bank money✗ No lending✗ No discount window✗ No deposit-taking

🧠The Fed is treating Kraken as a pilot, but the line is already forming.Custodia Bank has been litigating the Fed since 2022 over a denied application. Anchorage Digital (OCC-chartered) applied. Ripple's US banking partner applied.

🧠This is a big story for all of Fintech.In the UK, India and Singapore companies like Wise have had access to central bank payment systems for a decade. The USA is a laggard in this respect.

2.Visa and Stripe's Bridge are launching stablecoin-backed cards in 100+ countries.

“Visa and Bridge, a crypto startup acquired by Stripe in 2025, intend to launch stablecoin-backed cards in 100 countries across Europe, Asia, and Africa, the two companies announced on Tuesday”

🧠This is SO different from how cards used to work.You used to have to launch country-by-country. Get partnerships with each individual bank, manage rollouts slowly. Stablecoins fix this. Now it’s possible via one single API.

🧠There's been a massive rise in companies launching "stablecoin-linked" cards.Growing from $1bn TPV to $5bn TPV in two quarters. Why? Cuy Sheffield, Visa's head of crypto, nailed it"If you're building a stablecoin wallet and want people to spend in the real world, you need a card."

🧠Bridge is also joining Visa's pilot to settle charges on-chain — replacing traditional bank transfers with stablecoin settlement on blockchains.That's the actual long-term story.The spending side uses existing Visa rails. The settlement side replaces the slow, expensive correspondent banking network.

### Good Reads📚

1.The process of getting a bank charter

During the dark years of bank chartering, regulators didn’t eliminate risk; they pushed it out of the banking system, only to see it find new ways in (like the rent-a-charter model AKA BaaS). Many of the stronger Fintech companies survived, thrived, and are now pushing for their own charters to reduce the risk of relying on often much smaller banks. With plenty now receiving conditional charters, the real work begins after, during the “organization phase.”

Conditional approval means business plans, management, and financials are in place. Organization is about putting in place risk and operational controls to meet a full pre-open exam (that’s a high bar). The true scrutiny starts when you’re open, not before.

🧠Conditional OCC approvals get headlines, but they’re also at least 18 months away from a go live.For all the excitement of the charter gold rush, it’s still a long road ahead, something I think most at scale Fintech companies fully understand.

🧠Getting a charter is hard, keeping it is harder.Even if you survive your first exam, the next one is never far away.

### Tweets of the week🕊

— #(#)

— #(#)

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
