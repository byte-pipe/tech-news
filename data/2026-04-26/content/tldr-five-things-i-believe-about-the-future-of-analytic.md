---
title: Five things I believe about the future of analytics
url: https://roundup.getdbt.com/p/five-things-i-believe-about-the-future
site_name: tldr
content_file: tldr-five-things-i-believe-about-the-future-of-analytic
fetched_at: '2026-04-26T06:00:35.601288'
original_url: https://roundup.getdbt.com/p/five-things-i-believe-about-the-future
author: Tristan Handy
date: '2026-04-26'
description: '...and 4 conclusions I draw as a result.'
tags:
- tldr
---

# Five things I believe about the future of analytics

### ...and 4 conclusions I draw as a result.

Tristan Handy
Apr 19, 2026
53
2
Share

Here’s what I’m thinking about right now. Over the past few weeks, a handful of beliefs have crystallized for me about where the analytics world is heading. Not data pipelines, not infrastructure, specifically analytics.

I wanted to get them out of my head, so this post is a bit of a brain dump. I connect them all at the end with some conclusions.

Enough preamble. Let’s go.

## Thing 1: Analysts are going technical

Vibe coding and coding agents are pulling analysts onto the command line and into IDEs. That’s always been software engineers’ territory. Analytics engineers splintered off into it over the past decade. Now data analysts are joining the party. Our finance team is using Claude Code to build Excel models. Our data analysts are drafting initial analyses there and spending less time in our BI tool every day.

Why is this happening? Two things at once: you no longer have to actually write code to benefit from these tools, and the return on the time invested is enormous.

But data consumers aren’t following—at least, yet. They’re staying in tools that are native to them. For us that’s our BI tools, Notion, and Claude Desktop & Cowork.

The bifurcation is real. Before, it was: data engineers and analytics engineers in technical tooling, analysts and business users in the BI tool. Now everyone except consumers moving into technical tooling. This is an important shift.

## Thing 2: Data usage will explode

Think about jobs-to-be-done in three layers: platform, pipelines, analysis. The biggest AI-related disruption is coming at the analysis layer. In fact, it’s not even fair to call it the ‘data analysis’ layer; I have been thinking of it more as the ‘data usage’ layer.

There are real benefits to agents in the pipeline world—the cost of building new pipelines goes down, refactoring gets better, observability improves. All very good, and things that we’re actively working on / shipping.

But these changes pale in comparison to the disruption that will happen at the usage layer.

Over the past decade, there’s been amassiveinvestment in data infrastructure. And it worked. Data infrastructure (platform and pipelines), previously the bottleneck, got dramatically better.

But we revealed a new bottleneck. We didn’t actually makedata analysismuch better. Analysis is mostly just…thinking a lot, and we hadn’t solved thinking yet.

Lots of ink has been spilled about this under the heading of “ROI of data”—the frustration that all this investment in infrastructure hadn’t unlocked as much value as we all might have wanted. But of course, all of the layers of the stack have to work together to unlock business value.

But if analysis requires thinking, well, that bottleneck just vanished.

## Thing 3: Analytic agents are happening now, and moving fast

People are, right now, building agents to do analytic work. And it’s working. We’ve unlocked this at dbt Labs over the past six weeks and the pace of improvement is remarkable.

We’re not alone. Meta recentlypublished a detailed lookat their internal analytics agent, which went from a weekend prototype to a company-wide tool used by thousands in roughly six months. OpenAI hasbuilt their owntoo, covering the full analytics workflow: discovering data, writing SQL, publishing notebooks. Our friends at Ramp builtRamp Research.

These are no longer experiments. They’re in production today, and they are being widely adopted because they work.

## Thing 4: Agents consume dramatically more than humans

But the data agents that we see in production today are still largely responding to direct requests from humans. That is going to change; agents are going to be put in charge of optimizing processes, and will be given access to data tools to help them.

Imagine I build aRalph Wiggum agentwhose entire job is to scan our dbt usage data looking for product opportunities. It’s going to run alotof queries, far more than I ever could. It can generate hypotheses faster than I could, write queries faster than I can, follow chains of reasoning faster than I can, and work around the clock. It can also run arbitrarily many copies of itself, whereas there is only one of me.

The queries that this agent executes are interesting because not only is the agent writing the query, but the agent is generating the entire thought process, from hypothesis to test to conclusion. No human in the loop. The only time a human sees the output is when an agent finally says “hm, this is interesting enough to tell someone about.”

I’m going to call these queries agent-initiated, because the agent actually initiates them, it is not simply responding to a direct human request.

The best data point for this that I have today is the absolutely exploding volume of dbt MCP server calls. Usage of the dbt MCP server, a critical piece of infra for data agents, has been growing 50% month-over-month every month sinceits launch early last year. But even without this data point the conclusion seems obviously true to me.

So: when will agent-initiated queries to the data lake surpass human-initiated queries? I believe some companies have already crossed that threshold. I’m fairly convinced that within 12 months, it will becommon. And the line won’t stop there—I think it’s entirely possible we see 100x more agent-initiated than human-initiated queries within 36 months. That might even be conservative.

The implications for this are massive.

## Thing 5: Harnesses are a leverage point

A recent paper out of Stanford,*Meta-Harness: End-to-End Optimization of Model Harnesses*, makes a point I think is under-appreciated: the performance of an LLM system depends not only on the model weights, but enormously on theharness—the code that determines what information is stored, retrieved, and presented to the model. And the impact is not small:

Changing the harness around a fixed large language model (LLM) can produce a 6× performance gap on the same benchmark.

Meta-Harness is a system that automates the search over harness designs. IMO the most important finding for the data ecosystem: vertical-specific harnesses (harnesses tuned to a particular domain) significantly outperform generic ones in that domain.

So: a harness designed for data work, with deep knowledge of your warehouse schema, your dbt project, your business definitions, will likely outperform a generic coding assistant by a wide margin. And we can tune these harnesses automatically.

## My conclusions

1. Agents will be the primary consumers of analytic data within 12 months.Design your infrastructure for that now.
2. Data analysts won’t disappear—their impact is going up significantly.But the job is changing. The analysts who thrive will be the ones who start building and operating agentic analytic systems rather than continuing to ship dashboards. With coding agents, this doesn’t require a whole new set oftechnical skills, but it does require a reconceptualization of the role. This is similar tothis takeof SWEs that I strongly agree with.
3. Analytic data will (sometimes!) still need to be formatted for human consumption—but thecreationof those assets is changing.Because all the creators have moved out of the BI tool into technical tooling, the creation of human-facing assets will follow. They will be built from within Claude Code, Cursor, or similar tools that get purpose-built for analytics.
4. The workflow of a data analyst is going to start to look a lot more like the workflow of a front-end software engineer.Because the systems they’re building are exactly that—the UI layer on top of a massive data-driven reasoning engine. There’s a lot more to say here; I’ll return to it in a future issue.

3.5 years into the current AI wave and things are truly getting fun. Hope you’re enjoying yourself too :)

- Tristan

53
2
Share