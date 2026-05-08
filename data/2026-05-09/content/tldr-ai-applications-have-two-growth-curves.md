---
title: AI applications have two growth curves
url: https://frontierai.substack.com/p/ai-applications-have-two-growth-curves
site_name: tldr
content_file: tldr-ai-applications-have-two-growth-curves
fetched_at: '2026-05-09T07:54:13.974726'
original_url: https://frontierai.substack.com/p/ai-applications-have-two-growth-curves
author: Vikram Sreekanti
date: '2026-05-09'
description: Different markets, different physics
tags:
- tldr
---

# AI applications have two growth curves

### Different markets, different physics

Vikram Sreekanti
May 07, 2026
5
Share

Every board deck in AI right now uses the same benchmarks. Companies like Cursor and Sierra have ridiculous growth curves. The message is implicit: this is what AI growth looks like in 2026, and if your company isn’t on this trajectory, something is wrong. Founders have to explain the gap. Investors are calibrating expectations against it. Buyers are wondering whether every vendor they talk to needs to have raised $100MM.

Source: Gemini.

This is a category error, and it’s distorting how everyone in AI reads the market. Cursor and Sierra are growing fast for very different reasons — and crucially, neither of those reasons applies to the hardest and most valuable problems AI is being pointed at. The infrastructure markets that look slow by comparison are not behind. They are operating on fundamentally different physics, and in many cases, the slowness is the thing that will make the eventual companies valuable.

## The market map, revisited

We mapped this out earlier this year inData is your only moat. The 2x2 we introduced in that post separates AI markets along two axes: how hard the problem is to solve technically, and how hard the product is to adopt organizationally. Three of the four quadrants are seeing fast growth right now, and each for a different reason. Easy-to-adopt, easy-to-solve (easy-easy) markets — consumer chat, basic search replacement — are growing because there’s almost no friction in either direction. The model providers are dominating these and that’s mostly fine. Easy-to-adopt, hard-to-solve markets, the Cursor quadrant, are growing because individual users can adopt without organizational approval and the data flywheel that follows is incredibly powerful. The core AI capabilities are racing ahead, and it’s hard to catch up if you’re not already in the game.

The hard-to-adopt-easy-to-solve quadrant is the more interesting case for this discussion, because the growth there has been remarkable too. Sierra, Decagon, and other enterprise support agents are scaling rapidly despite needing committee buy-in to land each customer – an individual support rep can’t buy Sierra. The reason is that the underlying problem — execute a defined playbook for a known workflow — is tractable enough that vendors can demonstrate value quickly once they’re in the door. The large fundraises these companies have done signal credibility to a Fortune 500 buyer who needs to know you’ll still be around in three years.

That leaves the fourth quadrant: hard-to-adopt-hard-to-solve. SRE, security operations, complex infrastructure agents. This is the only quadrant that doesn’t have a Cursor or a Sierra growing into it at breakneck pace, and it’s where the misreading is doing the most damage. Founders in this quadrant get benchmarked against companies in the other three quadrants and asked why they’re not on the same curve. The honest answer is that they were never going to be — and more importantly, that the slowness is fundamental to the problems being solved here.

## What slowness buys you

When a market doesn’t let you move at breakneck speed — because the buyer is a committee, because the integration is genuinely complex, because the customer needs weeks to evaluate — you are forced to spend that time figuring out what the right product actually is. In a fast market, you don’t get that time. The competitive pressure is too high, the customers are too willing to start immediately, and the only correct move is to ship the obvious solution as quickly as possible and iterate from there.

Certainly for hard problems, the obvious solution is rarely the best one. Take AI SRE, which is where we spend our time. Almost every startup in the space (and there are many!) is building an AI-powered root cause analysis agent that is triggered by incident management alerts and requires customer-maintained runbooks. It’s the obvious solution: humans use runbooks, so the agent should too. Except alert thresholds are noisy, no engineering team actually maintains their runbooks well, and the agent inherits all the gaps. By trying to chase the Cursor growth curve, the players in this space haven’t asked the more interesting question: how do you use agents to detect early warning signs of an incident, validate them, and figure out the root cause from that structure — before any threshold alert ever fires?

To be transparent, we didn’t see this initially either. When we started, we set out to build the same banal runbook-driven RCA agent everyone else was building. The reason we ended up somewhere different is that the market gave us time. If customers had been willing to write us $250K checks on day one for a generic RCA agent, we would have shipped that and spent the next two years executing on the wrong product. The slowness of the market is what pushed us to keep asking whether the obvious solution was the right one. It turned out it wasn’t.

This is the first-order benefit of a slow market: it forces you to solve the actual problem, not the one that’s easiest to monetize.

Understanding this dynamic also helps you tailor your approach to the market you’re in. When you try to grow too fast for the type of market you’re in, the pressure forces you to take POCs you shouldn’t take, ship to customers you can’t actually serve well, and chase logos you don’t have the product depth to make successful. The cost isn’t just churn. It’s reputational damage that extends to the entire category. We’ve heard plenty of stories about AI agents in our market and adjacent ones that were rushed into enterprise environments, failed in visible ways, and left buyers with the strong sense that this whole category of product doesn’t work yet. That impression is sticky. It poisons the well not just for the vendor that failed but for everyone behind them trying to sell into the same buyers.

## Education as a moat

The other key benefit is the one we underestimated coming into this experience: the education process itself becomes a moat. Most customers in hard-hard markets don’t fully know what an agent in their space is supposed to do. They have intuitions and pain points — but the category isn’t well-defined in their heads yet. That sounds like a problem, and in a fast market it would be. In a slow market, it’s an opportunity.

Look at finance agents for closing books, a market which perhaps is a few steps ahead of AI SRE on the same curve. Walk into any controller’s office and you’ll find a long list of vendors all positioned around roughly the same pitch: We automate your close. Some are reconciling against templates, some are categorizing transactions, some are flagging variance. The buyer’s job is to figure out which of these is actually solving their problem and which is selling them a glorified macro.

A vendor with a real point of view – we’re not experts, butDigitsseems interesting – can stand out from the noise. The idea behind digits isn’t to put a pretty UI on top of your existing, messy general ledger data: They’re rebuilding the concept of a general ledger from scratch in order to support quicker, more efficient books that are constantly kept up to date. You might not agree with the approach, but it expresses a clear point of view that’s cohesive – not just AI slapped on top of whatever you had before. A differentiated point of view earns trust that competitors with vague positioning can’t easily replicate.

You don’t get to do this in a fast market. By the time Cursor was teaching anyone what coding agents could do, every developer on Twitter had already figured it out themselves. The market did the education for them. In hard-to-adopt markets, you do the education yourself, and the customers who learn from you tend to remember who taught them.

## How to read these markets

Taken together — time to find the right solution, protection from category-poisoning failures, and education-as-differentiation — and you start to see why the slow curve isn’t just a consolation prize. It’s the trajectory that builds companies competitors can’t easily copy in a quarter when the funding cycle turns. The fast curve produces companies that grow incredibly quickly and then have to fight off model providers, incumbents, and a long tail of well-funded copycats with similar products. The slow curve produces companies that, by the time they’re visible, have a product nobody else can replicate without going through the same multi-year process.

This has implications for how you interpret business in these markets. The signals worth tracking are whether a company has a non-obvious technical thesis, whether their POC win rate is improving over time, whether their existing customers are deepening usage rather than just renewing. These are the signals that actually predict which companies in hard-hard markets will still be standing in five years.

The companies winning the fast AI markets right now deserve their growth. We’re not arguing otherwise. What we are arguing is that the curve they’re on is not the only curve, and treating it as the benchmark for all of AI is going to lead to a lot of misallocated capital, misread pipelines, and eventually, a lot of surprise when the slow-market companies turn out to be the ones with the deepest moats.

The next phase of AI isn’t going to look like Cursor’s growth chart. For the most valuable problems, it isn’t supposed to.

5
Share