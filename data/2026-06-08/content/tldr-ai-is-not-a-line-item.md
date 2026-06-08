---
title: AI is not a line item
url: https://frontierai.substack.com/p/ai-is-not-a-line-item
site_name: tldr
content_file: tldr-ai-is-not-a-line-item
fetched_at: '2026-06-08T11:00:09.322010'
original_url: https://frontierai.substack.com/p/ai-is-not-a-line-item
author: Vikram Sreekanti
date: '2026-06-08'
description: One number for all your AI spend is a recipe for disaster
tags:
- tldr
---

# AI is not a line item

### One number for all your AI spend is a recipe for disaster

Vikram Sreekanti
 and 
Joseph E. Gonzalez
Jun 04, 2026
8
Share

As soon as we started hearing stories of companies maintaining internal leaderboards for token counts, a backlash to AI spend felt inevitable. Just a few months later, it’s arrived.

Headlines over the last few weeks have been filled with discussion of companies like Uber dramaticallyrunning over their AI token budgets for the year, unexpectedClaude overages, andwhether you can measure the impact from coding agents. And of course, there’sthe backlash to the backlash. We’ve heard stories ourselves about CTOs and VPs of Engineering freezing budgets and instituting extreme scrutiny on all new AI spend.

Token leaderboards are no more intelligent than ranking engineers based on lines of code generated. Even if you assume that everyone was behaving with the best of intentions, using more tokens doesn’t mean you got more done. You’re measuring the wrong thing and allocating your budget the wrong way.

Source: Gemini.

What happens next is somewhat predictable. Enterprises will pull back on token spend, institute per-employee limits, and have teams submit budget requests for token allocations. Budget freezes will be widespread practice by the end of the year. From our perspective, this is completely the wrong way to approach AI spend. You shouldn’t be turning up spend to brag about how big the number is, and you shouldn’t be limiting AI use out of a fear of overagesbecause you were previously tokenmaxxing. In fact, thinking about your AI spend as one number is the wrong way to look at it.

Different agents – and different experiments with new tools – are going to have different impact on your business. It makes no more sense to have one number for all of your AI spend than it does to have one number for all of your salary spend. Instead, you should think about each AI tool as impacting the team or the functionality buying it. When put in that frame, the rational rules for AI spend start to look pretty different. We have a few rules that we’ve started to solidify both from our own experiences and from talking to hundreds of engineering organizations.

## Limits with limits

Enterprises need budgets, and we’re not advocating for unrestrained use or $500M Claude bills being the new norm. But you need to set limits on how you set limits. Going from no constraints on usage and massive bills to extreme scrutiny and justification for every expense both creates organizational whiplash (how often do I have to change my habits) and also discourages experimentation. Different uses of AI – proven value adds like coding agents vs. experimental new tools – should explicitly be treated differently. If you don’t have a budget for experimenting with new tools, you’re going to fall behind.

Discouraging experimentation is probably the biggest and most avoidable own-goal. While the pace of change is very high, there’s still tons of undiscovered or poorly understood application areas, and aggressively setting limits on budgets means that your team isn’t going to learn about what’s possible. We’ve already heard engineering teams share that they’re not being allowed to spend on any new AI tools even while they believe our solution would solve a real problem for them – and would cost 1-2 orders of magnitude less than what they’re spending on salaries solving the problem (or on OpenAI or Anthropic for that matter).

This also requires reframing your thinking on software vs. headcount budget. Traditionally, software budgets and salary budgets have been treated differently, but we’ve seen cases where teams have open headcount for which they can’t find high-quality talent, while they’re blocked from spending more money on software. Agents won’t replace humans 1-for-1, but they will defray the tedious work that allows people to focus on what they’re best at.

When you limit experimentation, you’re embracing a static worldview. You’re limiting your team’s ability to adapt to the latest technology, and relying only on headcount is the hardest way to solve capacity problems. You certainly don’t want to be blowing out your budgets, but giving your competitors an advantage by sitting on your hands and pretending the technology around you isn’t changing doesn’t work either.

## Build vs. buy: The calculus (isn’t all that) different

There’s plenty of ink being spilled on whetheryou should build all your software moving forward. We’ve talked about thebuild vs. buy calculus before, so we won’t repeat the arguments in full detail, but the build vs. buy decision plays into the budget discussion. Building a product in-house is more likely to lead to budget overruns than buying something off the shelf. Humans are generally terrible at sunk costs, so once you invest into building a prototype, it’s natural to double down on that effort – but that’s where your budget overrun is most likely to get worse.

It’s a tired trope at this point that coding agents make it mind-numbingly easy to build a good-enough demo. It takes minutes and costs pennies. But the iteration and time that’s required to take that demo and turn it into a useful product is not quite so simple – or cheap. You’re both going to spend valuable time on that productionization process and you’re going to spend tons of tokens fixing all the bugs and edge cases that you didn’t anticipate in the demo that you built in just a few minutes. More importantly, when a coding agent writes most of the code, no one’s going to know what happened when it breaks. That means Claude is going to burn tons of tokens figuring out the issue.

This is where the budget argument and ROI calculus get particularly difficult. Is this engineering expense or operational cost? How much of this is expected, and how much will stability increase with time? How do you account for the time humans are spending on this problem as opposed to others? Properly estimating complexity and allocating budget for a piece of software that’s not your key expertise is inevitably going to be noisy and inaccurate – and that inaccuracy will spill over to affect the rest of your “AI budget.” The token cost will look tiny in the build phase – but when you get to productionization, maintenance, and new features, the token and salary math get very hard to justify.

## Prioritization is more important than ever

We’re noticing that engineering teams are increasingly distracted – we sharedan anecdotea couple weeks ago about an engineering team that was jumping between possible solutions. To some extent, this is understandable because engineering teams really can do anything right now. But running tons of experiments that end up resulting in very little (especially when there are off-the-shelf solutions available) is an expensive distraction. Once again, this runs up token costs – and the budget experiments that have dubious value shouldn’t be conflated with real systems that can help your team.

This is perhaps a more subtle challenge at first glance. Each potential experiment that you run that isn’t well thought out can go from a $5 starting point to a $1,000 sinkhole very quickly. We’ve had this happen ourselves. While we’re not advocating for shutting down all agent use for the purposes of keeping a lid on budgets, knowing what you’re trying to accomplish – and how that ties into your token use – is critical. Giving your team room to experiment is valuable, but that’s not the same as something that’s directly adding value to the business. Mixing the two up leads to bad decision making about “AI.”

## AI is not a line item

The question underlying this whole conversation is what the budget for AI tools should be, which is (literally) a million-dollar question. We’ve seen a pretty wide range of approaches – no limits at all (quickly becoming a thing of the past), everything goes to engineering, or an AI budget per-organization. But in all cases, AI is being treated as a line item on the budget – the wrong approach.

This isn’t a question about whether AI is here to stay, but about how we think about the value AI is adding. The value AI is adding to shipping product features that directly affect your top line is very different from the value it’s adding when you’re experimenting with recreating a third-party tool – or from the value it adds in writing cold email copy. Treating that all as “AI spend” is misguided. Different agents are going to add different amounts of value and in different ways.

That also doesn’t mean that you should treat every AI agent as one that’s going to have immediately measurable ROI – you should absolutely have budget allocated to experiment with things thatmightadd value (or might not). How large that number is and how strictly it’s metered probably varies from business to business. Either way, putting all AI spend in one bucket and tokenmaxxing that number up or hurriedly rushing it down is a recipe for disaster.

8
Share