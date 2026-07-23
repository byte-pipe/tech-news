---
title: AI Makes Software Quality A Board Conversation. Are You Ready For It?
url: https://vinvashishta.substack.com/p/ai-makes-software-quality-a-board
site_name: tldr
content_file: tldr-ai-makes-software-quality-a-board-conversation-are
fetched_at: '2026-07-24T05:40:02.849742'
original_url: https://vinvashishta.substack.com/p/ai-makes-software-quality-a-board
author: Vin Vashishta
date: '2026-07-24'
description: You understand why the technology creates value. The people who control the budget need you to connect that to something they care about and understand. Can you do it?
tags:
- tldr
---

# AI Makes Software Quality A Board Conversation. Are You Ready For It?

Vin Vashishta
Jul 19, 2026
8
Share

You understand why the technology creates value. The people who control the budget need you to connect that to something they care about and understand; either an opportunity or a risk that’s big enough to get their attention. This is the translation that creates influence in the C-suite, but few technical leaders have been taught how.

In this article, I’m partnering withTricentisto explain how to translate an emerging need into the language and framing that opens up wallets and gets C-level buy-in.

## Understanding The Need

The most important sentence inTricentis’ 2026 Quality Transformation Reportis its last one:Software quality is becoming a boardroom concern, akin to cybersecurity before it.

But does your C-suite and board understand that? It should be obvious. AI tooling makes development a continuous process. AI tools create new quality risks and scale existing risks. Businesses need a new approach to quality that enables them to adapt and reap the benefits of AI coding tools without falling victim to their risks.

More changes are checked in more often. More code is AI-generated, and purely human validation processes threaten to offset the productivity gains. The solution is continuous automated testing, issue detection, and escalation.

The obstacle to what should be an obvious conclusion is that the people who would have to carry quality up to the board can’t yet describe it in language that the board can act on. There’s a number in the data that proves it.

## The 23 Point Gap That Should Worry The Board

93% of C-level respondents are confident their testing strategy covers the most critical risks to the business. Only 70% of practitioners agree. That 23-point spread is a population of executives who are confident in a strategy, while the people closest to it are not. They’re signing off on something their own experts are uneasy about.

42% of C-level leaders believe their developers and executives are fully aligned on what good software looks like. Among QA and DevOps leaders, just 22% agree. Most of the confident executives have a gap they can’t see. They are reassured by an alignment that doesn’t exist.

It’s easy to get visibility and approval for AI tools. They are front of mind, and enterprise vendors have done an excellent job of connecting the dots between adoption and value creation. But AI development tools fundamentally change the development lifecycle. Those upstream changes require new tools to support a new kind of quality assurance lifecycle.

Those are a lot harder to get the budget for, and the root cause is the same as the one that causes the 23-point gap.

## The Real Job Is Connecting The Dots

Technical leaders understand how the technology creates value. That fluency is what makes us all bad at explaining it. We can see the whole causal chain from better test selection to fewer escaped defects and lower change-failure rate. So we assume the value is self-evident, but outside of the tech bubble, it isn’t.

Everyone who controls a budget needs you to connect that chain to something they already care about, and “the regression suite is more resilient” is not on the list. The big reveal is that not all technology sells itself. Either we translate it, or it dies in committee.

There’s a structure to the translation, because there’s a structure to the room. In any real funding conversation, there are two kinds of deciders, usually at the same table.

The opportunity decider leads with upside: growth, speed, or market position. That’s the CEO, CRO, and often the head of product.

The risk decider leads with downside: loss, exposure, compliance, or the thing that ends up on the incident bridge or in front of a regulator. That’s your CFO, your CISO, your audit and board-risk people.

A capability gets funded only when you can speak to both. Lead with opportunity to a risk decider, and you sound reckless. Lead with risk to an opportunity decider, and you sound like a barrier. Every translation is 3 parts:

1. Here’s what the technology does.
2. Here’s the business consequence or impact.
3. Here’s how you explain that consequence to each decider.

Let’s run Tricentis’ platform through it, because it’s a good example of a quality platform investment built to survive this conversation, and because seeing the moves on a real product is how you learn to make them on your own.

### Start With The Artifact

Every discipline that climbs into the boardroom arrives carrying a recognizable object. Cybersecurity didn’t get elevated on a message of more security tools or explanations of what the tools do. It got elevated around a control plane or a single pane of glass, the audit trail, and continuous monitoring. These are the things a CISO could put on a slide and say ‘This is how we know’. Quality needs the same kind of objects, and that’s the center of Tricentis’ design.

What it does.The platform is organized around anAI Workspacethat Tricentis calls a control plane and system of record for agentic quality engineering. It coordinates the AI agents doing the actual quality work, holds shared context across roughly 200 enterprise systems plus web and custom apps, connects to the tools teams already run (Jira, GitHub,Tosca,qTest), and embeds governance, approvals, and an auditable decision trail directly into how releases happen, with humans kept in the loop for the judgment calls.

The business consequence.It is, for the first time, a system of record for release decisions. You can prove after the fact why something shipped, and stop something before it does. Quality stops being a checkpoint bolted on at the end and becomes a governed, continuous layer.

How you say it.

To the opportunity decider: “This is how we release at AI speed without growing the QA team in lockstep. This platform enables us to scale output and productivity, not headcount.”

To the risk decider: “This is our auditable control plane for autonomous releases. When the board or a regulator asks how we govern AI-generated code, this is the documented, provable answer.”

### Knowing What To Ship

What it does.Agentic Quality Intelligence continuously reads change and risk signals across the lifecycle, decides what actually warrants testing, judges release readiness, and escalates to a human only when judgment is genuinely required. It’s the engine that blocks untested changes and runs only the tests the change demands. It gives us risk-based selection instead of brute force.

The business consequence.You stop testing everything and start testing what matters, which is the rare lever that makes you faster and safer in the same motion. It’s the operational form of what Tricentis’ own CEO, Kevin Thompson, argues in the report: You don’t need to test everything. You need to understand the changes, their impact, and where the risk truly sits.

How you say it.

To the opportunity decider: “We shorten release cycles because we only run the tests a given change actually warrants. That removes the blanket regression tax on every deploy.”

To the risk decider: “We always know our release-readiness posture, and we can show the risk basis behind every go/no-go decision.”

### Keeping Coverage Ahead Of AI-Written Code

What it does.Two agents work the production line.Agentic Test Creationlives inside qTest and turns plain-language requirements into reusable test cases, so generating coverage no longer depends on scarce specialist expertise.Agentic Test Automationruns and maintains those tests through Tosca’s automation engines across SAP, web, and custom applications, intelligently reusing modules instead of rebuilding them.

The business consequence.This is the answer to the report’s central challenge that code volume is scaling faster than teams can validate it. Coverage now scales with AI-generated code without a matching rise in cost or headcount. The bottleneck that’s been capping AI’s productivity dividend is removed.

How you say it.

To the opportunity decider: “Our ability to validate finally scales with our ability to generate. We unlock the productivity AI development promised, but quality risks were throttling.”

To the risk decider: “AI-written code stops outrunning our ability to verify it. The gap between generated and trusted closes instead of scaling.”

### Surviving Production

What it does.Agentic Performance Testingputs autonomous agents across the analysis, design, and execution of performance and load testing, from individual APIs to full end-to-end systems, surfacing performance risk early. Tricentis reports that the agents accelerate time-to-insight by up to 90% to 95% over manual expert work.

The business consequence.You find the outage-class defect in the pipeline rather than in production. Discovery happens before it becomes a customer-trust event, which the report ties directly to lost revenue and lost partners.

How you say it.

To the opportunity decider: “We can commit to performance under scale to our biggest customers and actually prove it before we promise it.”

To the risk decider: “We catch the thing that takes the system down before customers do, and we catch it in the pipeline, not on a 2 a.m. incident call with the brand on the line.”

## Why This Stops Being Overhead And Becomes Governance

String those four capabilities together through the control plane, and something changes about the category that the spend lives in, and the category is everything to a check writer.

Pitch this stack as more tooling (a testing platform, test automation coverage, and QA management), and it lands as a cost. There, it competes with every other tool, gets benchmarked on price per seat. Overhead is what a board looks to cut.

Pitch the same stack as the governance layer for AI-scale release decisions and the system of record that lets the company move at machine speed without going blind on its risk exposure. It lands beside the security stack, the audit function, and the controls a board is obligated to fund. Governance is what a board is accountable for.

This is the journey cybersecurity has already made. A decade ago, it was an IT line item you funded grudgingly until breaches got quantified, regulators arrived, customer trust got a price, and security walked up the stairs into the boardroom with its own committee and its own budget logic. Once the framing changed, that all changed with it.

The financial data is now doing the same thing to quality. 1 in 5 companies is losing up to $5 million a year to poor software quality. 45% are losing between $500,000 and a million. 40% of large enterprises sit in the $1–5 million band. Those are the shareable metrics we can use to start the conversation with C-level leaders and the board.

The moment poor quality has a dollar figure and a customer-trust line item, it stops being an engineering metric and becomes a category of enterprise risk. That’s important because enterprise risk has a higher-level owner than engineering metrics.

And to name the thing technical leaders avoid at all costs: none of this is spin. You are not inflating the value of the platform. You are translating its real value into the frame that the executive actually uses to allocate capital. Persuasion is helping someone see what’s true through a lens they can act on. Manipulation is getting them to act against their interests. The risk is genuinely board-level; saying so out loud is just accurate.

8
Share
Previous
Next