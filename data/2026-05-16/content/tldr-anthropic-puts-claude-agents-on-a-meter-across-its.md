---
title: Anthropic puts Claude agents on a meter across its subscriptions | InfoWorld
url: https://www.infoworld.com/article/4171274/anthropic-puts-claude-agents-on-a-meter-across-its-subscriptions.html
site_name: tldr
content_file: tldr-anthropic-puts-claude-agents-on-a-meter-across-its
fetched_at: '2026-05-16T11:25:10.926849'
original_url: https://www.infoworld.com/article/4171274/anthropic-puts-claude-agents-on-a-meter-across-its-subscriptions.html
date: '2026-05-16'
description: Anthropic’s move reflects a broader industry shift toward metered pricing for AI agents, forcing developers and enterprises to rethink the economics of large-scale automation workloads, analysts say.
tags:
- tldr
---

by									
Anirban Ghoshal

Senior Writer

# Anthropic puts Claude agents on a meter across its subscriptions

news

May 14, 2026
6 mins
 

## Anthropic’s move reflects a broader industry shift toward metered pricing for AI agents, forcing developers and enterprises to rethink the economics of large-scale automation workloads, analysts say.

 

							Credit: 															T. Schneider / Shutterstock													

The era of “all-you-can-eat” AI coding and agent subscriptions may well be ending. Beginning June 15, Anthropic will separate programmatic Claude usage from standard chat subscription limits, introducing a dedicated monthly credit system, billed at API-style rates, for tools including its Agent SDK, GitHub Actions, and third-party frameworks such as OpenClaw, the company wrote in ablog post.

The monthly credit for programmatic usage will depend on a user’s existing Claude subscription tier and generally mirror its monthly price, with Pro users receiving $20 in credits, Max 5x users $100, and Max 20x users $200.

In April, Anthropic had announced via apost on Xthat Claudesubscriptions would “no longer cover usage on third-party tools like OpenClaw”,citing compute capacity restraints, and effectively forcing developers using external agent frameworks either to purchase additional usage bundles or switch to direct API access.

Before that change, programmatic workloads and interactive Claude usage drew from the same subscription pool, allowing developers to use higher-tier Claude plans not only for chat and coding assistance, but also for autonomous agents, scripts,CIpipelines, and other automated workflows.

That arrangement had made Claude subscriptions particularly attractive to developers running long-lived agent tasks, as usage through tools such asOpenClawor the Agent SDK was effectively covered under the broader subscription limits rather than being billed separately at API rates.

## Could complicate enterprise budgeting

Unsurprisingly, the new policy, set to kick in next month, has triggered concerns among developers, many of whom argue that the move undermines one of Claude’s biggest advantages for agentic workflows: the ability to run large-scale automations under comparatively predictable subscription pricing.

“The monthly limit you are providing won’t even last a day of serious work. You are just reducing/removing the usage of some of the most used features like Claude Agent SDK and claude -p [in Claude Code] and calling it a perk,” senior data scientistYadesh Salvi, wrote in apost on X.

Advait Patel, a senior site reliability engineer at Broadcom, echoed Salvi’s concerns: “For developers who built side projects and personal automations on top of a flat Pro or Max plan, this is a real shift.”

“A dedicated credit pool gives you a small free runway for experimentation, but the moment your agents become useful enough to run often, you are on metered billing whether you like it or not,” Patel added.

He said that developers may need to stop viewing AI subscriptions as a low-cost route to running production-grade agentic workloads, as vendors increasingly shift toward consumption-based pricing models in response to the rising cost of automation-heavy AI usage.

“Heavy agentic users were consuming far more compute than a $20 or $100 subscription could support. Running these models is genuinely expensive, and unlimited flat rate plans for programmatic use were never going to last,” Patel said.

He feels that the new policy will introduce new operational and budgeting challenges for developers and teams who were relying on Claude subscriptions to run unattended workflows such as CI pipelines, scheduled automations, and long-running coding agents.

“Because usage is now tied more directly to token consumption than subscription tiers, enterprises may find it harder to forecast costs for workloads involving retries, large context windows, or multi-step agent loops,” Patel said.

“Also, credits are per user and do not pool, so you cannot share a budget across a team. That makes shared automations awkward,” he added. “Similarly, a runaway agent or a bad prompt can burn through credit fast and then either stop your pipeline or quietly start garnering extra usage.”

## Treat agents like cloud infrastructure

In fact, the senior engineer feels that developers and enterprises soon have to start treating programmatic AI usage less like a bundled software subscription and more like a metered cloud service with its own operational and financial controls: “Treat your Claude usage the same way you treat AWS or GCP. Know your token cost per workflow, set hard budget alerts.”

Paul Chada, co-founder of agentic AI startup Doozer AI, also advised developers to start focusing more aggressively on efficiency and cost discipline when designing AI agents and automation workflows, given the new policy.

“Stop optimizing for the subsidy and start optimizing for the token. Treat prompt caching, context discipline, and model selection as first-class engineering. The developers who thrive in the metered era are the ones who’d have built efficient agents anyway; the subsidy was just hiding who that was,” Chada said.

For analysts such as Greyhound Research Chief AnalystSanchit Vir Gogia, the new policy from Anthropic around programmatic use is less of an isolated pricing adjustment and more of a broader industry transition toward metered economics for agentic AI workloads.

OpenAI, he noted, has long relied on usage-based API pricing while reserving subscription offerings such as ChatGPT Plus primarily for interactive use cases. GitHub, meanwhile, is transitioning Copilot toward a token- and credit-based system that he said closely resembles Anthropic’s latest changes.

“Over the next 12 to 24 months, enterprises should expect more vendors to create separate consumption pools for agents, premium models, tool use, background tasks, and third party integrations. Some will call them credits. Some will call them requests. Some will call them messages. Some will call them compute units. Some will hide the meter inside bundles. The vocabulary will vary because marketing departments need hobbies. The direction will not,” Gogia said.

Artificial Intelligence
Development Tools
Software Development
 

 

														by 															

																Anirban Ghoshal															

Senior Writer

1. Follow Anirban Ghoshal on X
2. Follow Anirban Ghoshal on LinkedIn

Anirban is an award-winning journalist with a passion for enterprise software, cloud computing, databases, data analytics, AI infrastructure, and generative AI. He writes for CIO, InfoWorld, Computerworld, and Network World. He won the 2024 Silver Azbee Award for Best News Article in the Technology category. He has a post-graduate diploma in journalism from the Indian Institute of Journalism and New Media.

## More from this author

* news### AWS debuts Graviton-powered Redshift RG instances to cut analytics costsMay 13, 20264 mins
* news### Google pitches Agentic Data Cloud to help enterprises turn data into context for AI agentsApr 23, 20266 mins
* news### Amazon’s $5B Anthropic bet is really about compute, not just cashApr 21, 20265 mins
* news### Oracle delivers semantic search without LLMsApr 17, 20264 mins
* news### Salesforce launches Headless 360 to support agent‑first enterprise workflowsApr 16, 20266 mins
* news### MuleSoft Agent Fabric adds new ways to keep AI agents in lineApr 15, 20266 mins
* news### GitHub adds Stacked PRs to speed complex code reviewsApr 14, 20267 mins
* news### Google Cloud introduces QueryData to help AI agents create reliable database queriesApr 13, 20264 mins
 

## Show me more

Popular
Articles
Videos

opinion
 
 

### Capacity markets could reshape cloud computing

 
By David Linthicum
May 15, 2026
7 mins

Cloud-Native
IaaS
Technology Industry

news
 
 

### Anthropic puts Claude agents on a meter across its subscriptions

 
By Anirban Ghoshal
May 14, 2026
6 mins

Artificial Intelligence
Development Tools
Software Development

opinion
 
 

### Evidence-driven workflows: Rethinking enterprise process design

 
By Nitesh Varma
May 14, 2026
12 mins

Development Approaches
Enterprise Architecture
Software Development

video
 
 

### Profile Python Functions With ZERO Extra Code

 
May 12, 2026
4 mins

Python

video
 
 

### Two powerful tools for viewing Python app performance stats

 
May 5, 2026
5 mins

Python

video
 
 

### How to back up SQLite databases the right way (not by copying them!)

 
Apr 28, 2026
5 mins

Python