---
title: Agents are coming for data (just slowly) | InfoWorld
url: https://www.infoworld.com/article/4203157/agents-are-coming-for-data-just-slowly.html
site_name: tldr
content_file: tldr-agents-are-coming-for-data-just-slowly-infoworld
fetched_at: '2026-08-14T06:00:34.709517'
original_url: https://www.infoworld.com/article/4203157/agents-are-coming-for-data-just-slowly.html
date: '2026-08-14'
description: LLMs became reliably good at writing SQL only six or nine months ago. Soon agents will handle boring data tasks, but automated insights will take longer.
tags:
- tldr
---

by									Jordan Tigani							

# Agents are coming for data (just slowly)

opinion

Aug 6, 2026
7 mins

Agents have turned up just about everywhere in software this past year, with one conspicuous exception: data. That’s a little odd, because querying data is exactly the kind of structured, checkable task that agents excel at. The likeliest culprit is timing.Large language modelshave only been reliably good at writingSQLfor the last six to nine months, and the field hasn’t caught up to what that unlocks. It’s worth separating two flavors of the idea: agents thatdoanalytics, and agents that help you run the data plumbing. Both turn out to be more useful than they first look.

Data engineering is hard mostly because you’re at the mercy of systems you don’t control. Schemas change without warning. Sources go offline. The API you pull from ships a new version. A column that only ever holds integers starts returning decimals. A field you assumed was unique sprouts duplicates, and the next join detonates into a Cartesian explosion. Records go missing, or come back wrong for an hour and then quietly fix themselves. If nothing ever changed, data engineering would be easy. But as they say, the only constant is change.

## The boring work is where agents thrive

Unglamorous maintenance is something agents are genuinely good at. Every data model is a stack of assumptions: this is unique, that’s always populated, these two tables join cleanly. An agent can read those assumptions out of your code and turn them into tests that check whether they still hold. A lot of the fixes are mechanical anyway: a table got renamed, a type got widened, a column moved. An agent can often patch those on its own, and when it can’t, it can still do the legwork, tracing what changed and handing a human a diagnosis and a proposed fix instead of just a 3am stack trace.

Context is the other half of the story, and the context landscape is honestly a mess. Vendors are working hard to convince you that only their semantic modeling language can save you, while it is not entirely clear whether these are necessary or even sufficient. Whether you keep your business logic in a semantic layer likeMetricFloworMalloy, or just in plainMarkdown, the goal is the same: get that logic into a form an LLM can use. Context is almost always created by hand, and like all hand-written documentation, it starts drifting the moment it gets written down.

This highlights an opportunity, namely that agents are good at precisely the parts of context that are mechanical and bad at precisely the parts that aren’t. An agent can infer which tables join to which, what values a column tends to hold, what your sales regions are, and which tables people actually query. What it can’t infer is the stuff that was never really a data question: therightway to calculate revenue, what counts as a “customer,” when the fiscal year starts. Those aren’t facts hiding in the warehouse waiting to be found. They’re decisions, often business ones, that a person has to make. What an agent can do is flag the moment one of them quietly stops being true.

## Automated agent insights remain a fantasy

The flashier pitch, where agents surface insights you never asked for, is the one I’d bet on last. It sounds wonderful to have hands-free analytics. An agent will keep watch over your data, notice what matters, and drop a dashboard tailored to whatever is happening today. But the bar is high for relevance and false positives can make human users lose confidence.

Deterministic alerting systems have the same problem. People end up turning off alarms because they are too hard to tune. But if humans writing pre-canned triggers have a hard time getting it right, it is going to be hard for agents to do better (at least not before we get some form of super-intelligence). While I’d expect proactive insights to be part of the future, they are still a research prototype at this point.

Here are three concrete things a data team should do to get their stack ready for agents:

1. Lay the groundwork first. Agent use cases that are compelling sit on top of groundwork most teams haven’t laid yet. You don’t need an agent to curate your context until you’ve decided how your context is going to work in the first place.
2. Then go after context. Write a handful of evals, automate them, and then wait to see what breaks. Evals are the load-bearing part. They’re what makes it safe to let an agent near your pipeline at all, because they tell you the instant it gets something wrong.
3. Run on infrastructure that fits how agents behave. An agent goes from zero to a flood of queries in an instant, so you want something that scales up and back down quickly. Agents also fan out, chasing several threads at once, so you need both the headroom and the tenant isolation to absorb a burst. One agent’s curiosity shouldn’t take down everyone else’s ability to run queries.

## Latency is a bigger deal than it looks

Latency matters more than you’d expect when you’re using agents. While you might be waiting seconds or minutes for Claude Code to do its thing, it is often running a bunch of tasks. Part of the time that the agent spends is waiting for the LLM, but an increasing amount of time is using other tools, like querying a database. Over time, you can expect LLMs to get a lot faster; you can use smaller models, smarter models, local models, or fancier GPUs. As that happens the tools that an agent uses become the bottleneck.

Picture two engines: one answers in 10 milliseconds, the other in 100. A person won’t notice the difference because both feel near instantaneous, and a person will spend far longer thinking up the next question than either engine spends answering it. What feels instantaneous to an agent is very different, and it doesn’t need to stop and think. When its next query depends on the last result, that 10x gap compounds straight into 10x more work per minute.

One of the ways to make an agent go faster is to take more of their work and run it in parallel. But this also increases load on the systems. You’d want to make sure you have enough parallel capacity and isolation to be able to scale to all of the parallel agent queries at once. Engines tuned for human patience and engines tuned for agent throughput are not the same engines.

The agentic wave is coming whether or not any given team is ready, and the best time to start preparing yourself and your stack is now, before the queries start pouring in. This isn’t just future proofing. The teams that move early are the ones who work out the patterns everyone else ends up copying. A little curiosity now buys a real head start later.

—

New Tech Forumprovides a venue for technology leaders—including vendors and other outside contributors—to explore and discuss emerging enterprise technology in unprecedented depth and breadth. The selection is subjective, based on our pick of the technologies we believe to be important and of greatest interest to InfoWorld readers. InfoWorld does not accept marketing collateral for publication and reserves the right to edit all contributed content. Send allinquiries todoug_dineley@foundryco.com.

Artificial Intelligence
Generative AI
Data Management
 

 

														by 															
Jordan Tigani

Contributor

1. Follow Jordan Tigani on LinkedIn

Jordan Tigani is co-founder and CEO ofMotherDuck, an early-stage startup that has raised $100M from A16z, Felicis, and Redpoint. He helped create Google BigQuery, wrote two books on it, and led first the engineering team and then the product team through its first $1B or so in revenue. More recently, as SingleStore’s Chief Product Officer, Jordan helped them build a cloud-native SaaS business. Jordan has also worked at Microsoft Research and at a handful of star-crossed startups. He has an undergraduate degree from Harvard and a Master’s from the University of Washington. When not working, Jordan can often be found rowing or walking around Seattle.

## Show me more

Popular
Articles
Videos

news
 
 

### Visual Studio Code 1.133 brings flexibility to Claude sessions

 
By Paul Krill
Aug 13, 2026
2 mins

Development Tools
Integrated Development Environments
Visual Studio Code

opinion
 
 

### MCP didn't remove sessions. It handed them to the model

 
By Karthik Karunanithi
Aug 13, 2026
9 mins

Artificial Intelligence
Cloud Computing
Development Tools

feature
 
 

### Relief from the bookkeeping of change management

 
By Joseph Michela
Aug 13, 2026
7 mins

Cloud Computing
Cloud Management
Devops

video
 
 

### AI trends that need more attention

 
Aug 4, 2026
5 mins

Python

video
 
 

### Who's leaving GitHub and why

 
Jul 29, 2026
7 mins

Python

video
 
 

### Typst, the programming language for documents

 
Jul 23, 2026
7 mins

Python