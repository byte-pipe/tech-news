---
title: claude code is not making your product better
url: https://ethanding.substack.com/p/claude-code-is-not-making-your-product
site_name: tldr
content_file: tldr-claude-code-is-not-making-your-product-better
fetched_at: '2026-04-26T06:00:32.717788'
original_url: https://ethanding.substack.com/p/claude-code-is-not-making-your-product
author: Ethan Ding
date: '2026-04-26'
description: why the most respected engineers are pushing back on the coding agent hype cycle, and what the claude code argument actually reveals
tags:
- tldr
---

# claude code is not making your product better

### why the most respected engineers are pushing back on the coding agent hype cycle, and what the claude code argument actually reveals

Ethan Ding
Apr 21, 2026
111
11
13
Share

something interesting is happening. the loudest voices in the room are telling you that ai coding agents changed everything. the engineers who actually built the things you use every day are telling you something more complicated.

## the k-shaped productivity curve

before we get to the twitter discourse, there’s actual data. the labor economists got here first. the productivity gains from coding agents are not evenly distributed. they’re split along a k-shape: senior engineers are getting meaningfully more productive. junior engineers are, at best, treading water. at worst, they’re getting worse.

engineering output by seniority · ai adoption eralog size of commits · q1 2015 – q1 2025

seniors (blue) have seen measurable output growth since the llm inflection in 2023. junior output (red) has gone essentially flat or declined. the k-shape is real. the question is what it means.

the popular narrative maps cleanly onto the top half of that k. venture-backed twitter has been producing its own version of this chart for two years running. the quotes are now predictable:

“our team cleared six years of backlog in a quarter. every PR is ai-generated. we’ve never shipped faster.” — any yc batch founder, any month 2025

“i used cursor to build our entire backend in three days. two engineers doing the work of twenty. — the tweet that gets 40k likes every time someone posts a version of it

“anthropic’s claude code is completely claude-coded. ai writing ai. the recursion is real.— dario amodei / anthropic, repeatedly

and to be fair: there’s something real in the top half of the k. agentic coding does reduce the time to produce a pull request for certain categories of work. no one serious is disputing that. the question is whether lines of code produced per hour is the right thing to be measuring at all.

if engineers are more productive, the rate at which product improves per engineer should be going up

## the best product builders are a canary

a couple weeks ago, three things happened within days of each other. dax (buildingopencode.ai) sent something to his team. karri saarinen (ceo of linear) responded. david cramer (who built sentry from scratch to $10m/month) posted his github graphs. none of them are critics of ai. all of them are seeing the same pattern.

dax’s original message to his team (top left),karri saarinen’s “drunken whiteboard” reply (center),david cramer’s productivity conviction tweet(top right), and cramer’s follow-up thread breaking down exactly why agentic engineering creates bloat.

David Cramer
@zeeg
im fully convinced that LLMs are not an actual net productivity boost (today)

they remove the barrier to get started, but they create increasingly complex software which does not appear to be maintainable

so far, in my situations, they appear to slow down long term velocity
11:03 PM · Mar 16, 2026
 · 
671K Views
463 Replies
 · 
225 Reposts
 · 
3.51K Likes

cramer’s follow-up is worth reading in full. he points specifically to “the poor performance of LLMs on incremental development in complexity,” “the inability for LLMs to truly simplify and create idiomatic interfaces,” and “the pure slop test generation techniques they often follow.” his summary: “its mostly bloat.”

these are not luddites. dax is literally building a coding agent. karri built linear, a product that’s specifically designed around the philosophy that less is more in software tooling. cramer has been shipping open-source software for twenty years and can read a commit graph better than anyone.

and all of them are saying that they are having a hard time finding their product improvement velocity accelerate with coding agents

dax
@thdxr
us: we are struggling to figure out the best way to use coding agents, we don't have clarity yet

everyone else: our team is moving at speeds unheard of, all our PRs are ai generated, we've cleared 6 years of backlog

man we must really suck huh
3:53 AM · Mar 11, 2026
 · 
184K Views
166 Replies
 · 
104 Reposts
 · 
3.09K Likes

## why isn’t claude code in fast take off mode?

think about claude code itself: claude code is completely claude-coded. the loop is closed. the machine is writing the machine…

this means that the RATE AT WHICH THE PRODUCT IS IMPROVING should be accelerating.

and if that’s true, it implies something specific. engineering productivity is a compounding function. if using claude code gives you even a 1.5x improvement in the rate at which you can improve your product, then the team using it from day one should be racing away from everyone else. the gap should be widening every quarter. it should look like this:

source: y = e^(c*x)

but that’s not the reality. the reality is that codex launched months after claude code and is already functionally competitive. cursor’s deal flow is strong. cognition and factory are still closing serious enterprise contracts. this is what the actual picture looks like:

source: i made up the vibes

the falsification:if using claude code gives you a genuine product velocity advantage, and anthropic had it exclusively for 7 months, the gap between claude code and every competitor should be unbridgeable. codex would be irrelevant. instead, people are still actively debating which one is better. the compound advantage isn’t showing up. something else is bottlenecking product quality, and it was never the code

there are a few counterarguments worth taking seriously. maybe the gains are there but they’re being eaten by complexity debt. maybe anthropic’s engineering team is so large that the marginal gain per engineer is diluted. but if anything, those counterarguments prove the original point: even with the world’s best coding agent, the bottleneck isn’t code production. it’s something harder.

## lines of code is a cost, not a product

here’s the mental model that most people writing about this space are missing. and i say this as someone who wroterecently about how the token economics of this whole ecosystem don’t add up— the problem isn’t just financial, it’s conceptual. we’ve misunderstood what software engineering is actually optimizing for.

the best engineering cultures treat lines of code as something you spend, not something you produce. you spend them on the features that matter. you refuse to spend them on the features that don’t. the codebase is a liability on your balance sheet, not an asset.

tinychat (comma.ai‘s software subsidiary) famously had an alarm that triggered when the codebase exceeded a certain size. they celebrated deleted code. the reasoning is straightforward once you understand what software actually is: every line is a surface for bugs. every function is a dependency for the next function. every feature creates neighbors.

product surface area expands fractally. add a slack integration, and you need a teams integration, and then an email fallback. add notifications, and you need to rebuild them for mobile, sms, and enterprise mdm policies. add mfa support, and you need to be compatible with duo, okta, and saml. complexity doesn’t scale linearly. it compounds.

linear is in the top-right quadrant with the smallest bubble on the chart. 178 people, 6 years old, $100m arr. jira has 56× more cumulative engineering effort and scores 6 points lower on consumer quality. the bubble size is the point: quality and codebase mass are not the same thing.

facebook at 100,000 engineers is never gated by how fast they can produce UI code. a competent engineer can mock up the facebook feed in a day. the actual constraint is reducing the number of lines of code it takes to deliver that experience to billions of people under any load, at any latency, while maintaining uptime. the reward function is compression, not production. for workloads like that, coding agents cannot evaluate the long-term tradeoffs. they don’t have a theory of the system.

## the real bottleneck: pushing the frontier of good product ideas

there’s a final layer to this argument that nobody’s quite articulated yet. product quality improvements, at the frontier, are not bounded by how fast you can write code. they’re bounded by how fast you can come up with ideas good enough to push the frontier.

jira is designed reasonably well. the difference between jira and linear isn’t that linear drew better boxes. it’s that someone had a specific creative vision about what project management software should feel like, and then executed on it with restraint over years. that kind of product quality doesn’t emerge from token throughput. it emerges from taste. from the decision to build less.

product visionaries who can push the frontier of “what good software feels like” are rarer than anyone wants to admit. the ideas that sit at the edge of the curve don’t come from sprinting through a backlog. they come from the kind of slow, uncomfortable thinking that dax is warning his team about when he says we’re losing our ability to delay gratification.

this is also why the “cleared 6 years of backlog” claim is less impressive than it sounds. a backlog full of CRUD features and internal tooling is exactly the kind of work coding agents accelerate. it’s also exactly the kind of work that isn’t pushing the frontier. your product isn’t better because you shipped faster. your product is better if something you shipped made users care more.

↑ai coding agents do helpget 0-to-1 products to the quality frontier faster. they reduce time to first working version. the speed is real for early-stage work.

↑but at a cost:they make your circle bigger. the codebase grows faster than the quality does. the technical debt compounds. you’re buying speed with money you’ll pay later.

## camrys for everyone, ferraris for no one

so what are the actual conclusions of all this? do i think claude code isn’t worth paying for? well, it depends on where you are on the stack.

* if you’re at the frontier, your bottleneck isn’t coding agents — it’s tastemakers.the state of being “the best through subtractive taste,” held by companies like linear and sentry, lives inside specific people. nan yu at linear. kelly johnson at skunk works, where a hand-picked team built the sr-71 — still, sixty years later, the fastest air-breathing manned aircraft ever built. the blackbird wasn’t fast because johnson’s team produced more blueprints. it was fast because johnson had a theory of what to leave out. the taste to delete, compress, refuse — that isn’t on any frontier model’s roadmap. if anything, it’s more valuable now that the floor beneath it is rising.
* if you’re already at the frontier, it’s not clear that doubling R&D salaries on tokens produces any economic value at all.take ramp. their engineers have reportedly been doubling their salaries on token spend over the past year. has ramp the product gotten any better? how would you even know? when you’re already #1, your win rate is basically fixed — going from #1 to #1-by-a-larger-margin is pretty hard to measure. i’d need to see win-rate or P&L data from ramp to change my mind, but as a happy ramp customer, i genuinely can’t feel a difference between today and last year.
* claude code helps anyone and their mom build a camry competitor. it doesn’t help the artisans at ferrari make faster ferraris.but if you’re going from zero to a camry, it’ll be extraordinarily helpful.this is going to drive down the cost of camrys. software that isn’t produced by the best of the best is about to get dramatically cheaper.at the expense of a lot of chaos and debt piling up in the rafters of the factory. eventually someone has to clean the rafters.
* this is going to drive down the cost of camrys. software that isn’t produced by the best of the best is about to get dramatically cheaper.
* at the expense of a lot of chaos and debt piling up in the rafters of the factory. eventually someone has to clean the rafters.

thank you Mark Hay, Nan Yu, & Nikunj Kothari

read more at

mandates
all content here is generated by ai
By Ethan Ding
111
11
13
Share