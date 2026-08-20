---
title: 7 lessons for IT leaders on using observability to monitor AI applications | Elastic Blog
url: https://www.elastic.co/blog/monitor-ai-applications-llm-observability
site_name: tldr
content_file: tldr-7-lessons-for-it-leaders-on-using-observability-to
fetched_at: '2026-08-20T19:30:48.322904'
original_url: https://www.elastic.co/blog/monitor-ai-applications-llm-observability
date: '2026-08-20'
description: Discover the seven lessons we learned as we evolve our LLM observability practice to monitor and improve our AI applications.
tags:
- tldr
---

# 7 lessons for IT leaders on using observability to monitor AI applications

What it takes to prove AI value with LLM observability

By
Brad Quarry
August 19, 2026
* Share on TwitterShare on Twitter
* Share on LinkedInShare on LinkedIn
* Share on FacebookShare on Facebook
* Share by EmailShare by Email
* Print this pagePrint

Over six months, the Elastic IT team ran internal AI applications that returned $2.5 million in operational time to the business.1A conversational support assistant moved us from zero digital resolution, where anything complex became a ticket, to 30% of support interactions closing without one.

We can put those numbers in front of a finance team because we measured them from day one at the level of individual usage events. For each use case, we assigned a conservative time-saving goal and validated it with the teams doing the work. For example, a support case summary saves about five minutes. And, using a simple formula (events*minutes saved*a standard burden), the ROI of the application is now a real-time KPI rather than simply assuming that it might be valuable because the application uses generative AI. The hours came back to support engineers who had been searching for answers and went toward work on the roadmap.

Most organizations are not in that position yet. In ourLandscape of Observability surveyof 500 IT decision-makers, 85% said they planned to enable observability for their large language model (LLM) applications. Only 8% had done it. Teams see the value, they just don’t seem to be prioritizing it.

I suppose you can call that deferral “measurement debt.” Every AI capability shipped without instrumentation borrows against a future in which someone must prove it was worth shipping. Like technical debt, it compounds quietly and will come due with rising pressure from leadership to justify observability spend.

The lessons below are what we learned from our own implementation as well as useful tips we have gleaned from others.

## Lesson 1: MVP should include LLM observability

Teams under pressure to show AI progress should not treat telemetry as a phase-two concern. By the time leadership asks for a return figure, the usage history that would have answered that question needs to already have been captured. If it hasn’t been captured, there may not be a way to reconstruct it. Data can age out. Sampling can discard what was never flagged as important.

According to the Elastic Landscape of Observability report, while 93% of organizations report financial and business impact to leadership in some form, only 19% do so regularly as part of an established process.3The rest report occasionally or only when asked, which means the figure gets assembled as a one-off under deadline from whatever is available.

Pilots get funded on a projected return and need to be launched with a definition of success, so there is a threshold to measure against. Decide what success looks like before the first user arrives, and instrument for it in the same sprint. ROI should be a query, not an anecdote.

## Lesson 2: Don’t monitor a probabilistic system with deterministic metrics

Uptime and latency were sufficient metrics when point A to point B produced the same result every time. However, a generative application can be fully available, comfortably fast, and totally wrong. Teams that catch quality problems track a second set of signals alongside the traditional ones, such astoken consumptionbecause it is the cost meter;retrieval qualitybecause a grounded answer depends on what was retrieved; anduse-case classificationbecause knowing what people actually ask is the fastest way to quickly course correct.

These signals matter most after launch. Launch instrumentation tells you if your app is running okay. But as real users interact with the application, they surface a different and equally important question:Is this version better than the last? Nothing in that instrumentation can provide an answer.4Swap a model, rewrite a prompt, or change the retrieval strategy, and you need a system that tells you whether you made things better or only made them different. That is a comparison, and a comparison needs a record of what came before. And, a test suite only answers part of it, which are the cases you thought to capture. The questions users actually ask drift constantly, and the curated set needs to constantly evolve from live telemetry. The baseline has to exist before you know you need it.

## Lesson 3: Stick with established telemetry vocabulary

When a team creates an AI application by hand, someone has to name every field it emits like the token counts, the model, the tool calls, and the retrieval steps. Every dashboard, alert, and cost report that follows is keyed to those invented names, and the debt comes due at the moment of change. If an agent framework is swapped, a second model provider is added. Or if a new company is acquired, the reporting layer has to be rebuilt.

OpenTelemetry's semantic conventions for generative AI exist to prevent this. They define standard names for the operations that matter, including model calls, agent invocations, tool executions, and retrievals. Adoption is moving in one direction: OpenTelemetry in production nearly doubled year over year, and 60% of organizations now use a vendor distribution, which is up from 44% according to the Landscape of Observability report.

No generative AI span, metric, or attribute in that specification is marked stable yet, and attributes have already been renamed between versions.5However, using a moving standard still beats using a private one. A rename is a migration; a private vocabulary is a rebuild.

## Lesson 4: Let the instrumentation report what it already knows

At some point someone will put your AI cost report next to the provider invoice and ask why they disagree. The answer is usually that the application worked out its own numbers instead of recording the ones the provider already sent back.

Three versions of this are common:

* Token counts estimated with a tokenizer library when the provider's response carries the exact figure it will bill
* Cost computed from prices hardcoded in application code, which go stale with every model release
* Duplicate instrumentation emitting two records of the same call, quietly doubling every downstream count

Estimation also fails in ways a dashboard cannot show. Tokenizers differ by provider, so the same prompt counts differently against different models. Reasoning models are billed for intermediate work the caller never receives, so a count taken from the visible response omits part of what is charged and omits most on the calls that cost the most.6

In an audit of a reference environment our field team built this year, we found and removed all three, including token estimates that disagreed with the provider's actual figures and duplicated spans that inflated call counts. The correction was not more code; it was less. Let the instrumentation report what it already knows, then compute derived values like cost at query time against a price table so that a price change is a data update rather than a deployment.

## Lesson 5: Letting the telemetry bill become the next surprise

Observability spend is a top priority for leadership in 2026:97% of organizations have already hit unexpected costs or overages, and 67% say it happens regularly. AI workloads make that worse because a request that once produced a handful of spans can now produce dozens.

Two decisions cause most of the damage, and both are made below the level where anyone reviews them.

1. Tagging metrics with values that grow with usage:A conversation identifier is the classic case. Every new conversation then adds to what the monitoring platform has to store and index, so the observability bill starts tracking adoption instead of infrastructure. The application succeeds and the monitoring gets more expensive.
2. The remedy teams reach for once the bill arrives:This keeps a flat percentage of everything. A uniform sample discards failures and successes in the same proportion, and the failures are the entire reason the telemetry exists.

Neither problem needs exotic tooling. Schema and sampling policy are architectural decisions with a budget attached, not defaults inherited from a configuration file.

## Lesson 6: The problem is probably the data, not the model

In our experience, most quality failures in an AI application are not model failures. They are data and retrieval failures that surface as model failures.

An application grounded in your own content answers from documents it pulled at query time. When the answer is wrong, the only visible artifact is the model's output, so that is what gets investigated. Teams rewrite the prompt, then escalate to a larger and more expensive model, and the answer improves slightly or not at all because the model was working from what it was given. We have seen this in our own testing. In the same reference environment, an answer failed a quality review because the documents retrieved to support it covered three of the six policy areas the question asked about. No model swap recovers a document that was never retrieved.

None of that is visible unless the application records it. What was retrieved, how it ranked, and how much of the answer it actually supported are properties of the request rather than the model, and they exist only at the moment of the call. Capture them and quality debugging changes character. You can tell a model problem from a ranking problem from a content problem, and only the first is solved by changing models.

The old rule still holds — garbage in; garbage out — now delivered as a fluent and confident hallucination. We spent a year building a knowledge-centric support process with engineers writing knowledge articles as part of case closures. That foundation made theSupport Assistanttruly valuable. Better data raised the ceiling. Measuring the retrieval is what lets us watch the ceiling move.

## Lesson 7: Understanding cost visibility does not equal quality assurance

A complete cost picture answers what the AI spent. It says nothing about whether the AI was right. These are different disciplines, and the second is the one most organizations defer indefinitely. Machine learning engineer Hamel Husain, who consults with AI product teams on evaluation, argues that unsuccessful AI products almost always share one root cause: "a failure to create robust evaluation systems."6Systematic evaluation of groundedness, faithfulness, and tool use is not a quarterly exercise. It belongs wired into the same trace data that carries performance and spend, so a quality score points back at the run that produced it.

Cost visibility on its own can also mislead because the number most dashboards show has the wrong denominator. Price per call is a unit cost. What the business actually buys is a resolved request. A weaker model lowers the first figure and can raise the second because work that fails on the first attempt comes back as a retry, a follow-up question, or a longer chain of tool calls, and each of those bills again. The savings show up immediately and in the obvious place. The offsetting spend shows up later in a different line and often in a different team's budget. So, the two savings don’t seem connected.

The remedy is a change of denominator. Reportcost per completed task— total spend divided by the tasks that actually succeeded — and the cheaper model that needs three attempts stops looking cheap. Keep the quality verdict on the same trace as the cost, so a finance review and a quality review are reading the same record. There is a compact version of that pairing for anyone who wants a single number: task success rate multiplied by accuracy, then divided by cost per completed task. For the Support Assistant, success meant answering a question without a ticket being opened.

## The stakes continue to rise

An assistant that answers badly wastes a moment. An agent that reasons badly acts on it across multiple steps with tool calls at a cost that accrues per task rather than per question. The usage history that was never captured becomes an action history that cannot be explained. The baseline that was never recorded becomes judgment drift that cannot be seen.

The operational question shifts from what the model said to what the agent did and why. Everything in this piece has been preparation for that question, and the preparation is a single decision made before the next AI initiative ships; its value will be measurable from the first event.

An organization that cannot measure what an assistant returned has no basis for handing an agent the authority to act.

Dive deeper into how leading organizations are tackling the most pressing challenges in AI model lifecycle management in our on-demand webinar,The new competitive advantage: Using observability to monitor AI applications.

Sources

1. Elastic internal measurement, six-month period. Methodology: observed usage events × validated time savings × standard employee burden rate.2. Phillip Carter, "Improving LLMs in Production With Observability," 2023.3. John Hodge, "The state of the OpenTelemetry GenAI semantic conventions," 2026.4. Braintrust, "How to track LLM costs,” 2026.5. OpenTelemetry, “OpenTelemetry semantic conventions for generative AI systems,” 2026.6. Hamel Husain, "Your AI Product Needs Evals,” 2024.7. Mostafa Ibrahim, "What Is Agent Observability? Traces, Loop Rate, Tool Errors, and Cost per Successful Task," 2026.

The release and timing of any features or functionality described in this post remain at Elastic's sole discretion. Any features or functionality not currently available may not be delivered on time or at all.

In this blog post, we may have used or referred to third party generative AI tools, which are owned and operated by their respective owners. Elastic does not have any control over the third party tools and we have no responsibility or liability for their content, operation or use, nor for any loss or damage that may arise from your use of such tools. Please exercise caution when using AI tools with personal, sensitive or confidential information. Any data you submit may be used for AI training or other purposes. There is no guarantee that information you provide will be kept secure or confidential. You should familiarize yourself with the privacy practices and terms of use of any generative AI tools prior to use.

Elastic, Elasticsearch, and associated marks are trademarks, logos or registered trademarks of elasticsearch B.V. in the United States and other countries. All other company and product names are trademarks, logos or registered trademarks of their respective owners.

## Share

* Share on TwitterShare on Twitter
* Share on LinkedInShare on LinkedIn
* Share on FacebookShare on Facebook
* Share by EmailShare by Email
* Print this pagePrint

### Sign up for Elastic Cloud free trial

Spin up a fully loaded deployment on the cloud provider you choose. As the company behindElasticsearch, we bring our features and support to your Elastic clusters in the cloud.

Start free trial