---
title: 38 things we've learned about building AI products
url: https://newsletter.posthog.com/p/38-things-weve-learned-about-building
site_name: tldr
content_file: tldr-38-things-weve-learned-about-building-ai-products
fetched_at: '2026-10-12T20:08:22.716198'
original_url: https://newsletter.posthog.com/p/38-things-weve-learned-about-building
author: Ian Vanagas
date: '2026-10-12'
description: Lessons from 4 years of building AI products at PostHog
tags:
- tldr
---

# 38 things we've learned about building AI products

### Lessons from 4 years of building AI products at PostHog

Ian Vanagas
Oct 12, 2026
17
3
Share

We’ve built 10 different AI products at PostHog, includingPostHog AI, ourinstall Wizard,Replay Vision,Scouts, and more. They’re used by nearly 100,000 people every month. This is what we’ve learned.

1. AI can make your product worse.It can be slow and unreliable, or solve a problem nobody has (like chatting with your docs, any AI can do this). Just because it’s AI does not mean it’s worth building.
2. Consider whether you need to build AI at all. It’s often better tobuildforAI first, like an MCP server. These are easier to build and maintain. 5x more people use our MCP server daily than PostHog AI.
3. Look for jobs to be done, not demos. The best opportunities for AI are tasks that take 30+ seconds, use language or interfaces users don’t know (like SQL), or tasks users repeat 20+ times.
4. Onboarding is a great first target. Our AI install wizard does two hours of work in ~8 minutes. Those who use itconvert to paid 5x more often and activate 2x faster.
5. Don’t ask “how do we add AI to this?” ask “what is the agent-first version of this?” Doing this forces you to rethink the jobs to be done for an agent-first future and helps you avoidbeing disruptedby an AI-native competitor.
6. Building2030-shaped productsmay require you to start fresh and break from years of cumulative UI and assumptions that are no longer valid or relevant.
7. Watch for customersrebuilding your product with AI. This reveals what features they actually want. When one of our largest customers built their own prototype of “PostHog 2.0” with our MCP and Claude Code, we knew we needed to add more customizable “canvas” artifacts to PostHog.
8. Validate AI betslike you would new products. Write down how it will be judged and how much runway it gets. Ask how disappointed your team would be to lose it (thePMF survey). We did this for one product and only 23% said they would be very disappointed. Bad results, but useful.
9. Write downhow your product losesto an AI-native threat and then fund your version of the attacker. Even the best support product loses to one where AI answers all the tickets for example, which is probably why Intercom pivoted so hard into Fin.
10. Answer the question: How does this beat Claude? It’s what people default to.Your moat is context: your product’s functionality, your users’ data, and the tools and skills you’ve built.
11. Your harness is not your moat. PostHog AI went through three of them in a year. We now have MCP as the canonical interface and let people pick their own harness. Don’t spend innovation points here.
12. Don’t build an assistant. Assistants are what you build when intelligence sitsnextto your product. Systems are what you build when intelligence becomespart of it.Build those instead.
13. Focus on buildingshared AI infrastructure. Make prompts, streaming, consent, evals,tasks, and analytics primitives teams can extend and build into their products. Pick a consistent UX pattern to avoiddeath by a thousand widgetsand then get out of people’s way. Product teams know their users best, not the AI team.
14. Let agents run code. Code execution gives agents capabilities beyond what your predefined tools might enable them to do. PostHog AI can write SQL, run Python scripts, and ship PRs. Sandbox them to make this safe.
15. Model upgrades will bulldoze your assumptions. We’ve restructured PostHog AI due to cheap reasoning (o4-mini) and reliable tool use (Claude 4).Multimodal modelsmade Replay Vision possible. The harness, prompts, and context you built for previous modelsmight not be relevant for current ones.
16. Skillsare features for agents. They combine tools, docs, and rules into a recipe for a job. If an agent has the tools but not the recipe, it must look up how to use your product every time. Everydocs-searchcall is evidence of a missing skill or tool (and it’s our most-called tool at ~28K calls a month).
17. Let agents doeverything users can. If theexperiment-createtool exists, yet theexperiment-starttool is missing, the agent will do everything and then stop short to ask you to click through the UI. This limits the power of agents.
18. Dogfood headlesslyto develop agent empathy. Test agent features from theCLIso you hit the same friction points as they do. This is how we found our MCP tool descriptions used too many tokens.
1. AI doesn’t kill your UI, it changes its purpose. Fewer screens are for doing things, and more are forapproving, reviewing, and undoingwhat agents did.
2. Meet agents at their level of abstraction. Agents work better if you let them write and reason flexibly. We stopped forcing agents to use preset query tools and let them write their own SQL. A general purposeexecuteSqltool replaced every read endpoint and made “Why did signups drop?” go from four separate tool calls to one query.
3. A missing tool is a feature request written by a robot. Agents using our MCPcan file feedbackwhen they get stuck.
4. Set upAI observabilityfrom day one. Trace LLM calls with inputs, outputs, latency, and cost. This reveals the errors and issues that once fixed lead to rapid quality improvements.
5. Care more about reliability thancapability. Early complaints about PostHog AI weren’t about what it could do, they were about inconsistent performance, unexpected failures, generic errors, unclear limits, and lack of uncertainty. Capabilities are worthless if they aren’t reliable.
1. Track agent usage like human usage. Although agents don’t trigger pageviews or rageclicks, you can still track theMCP tool calls,page requests, and more.
2. Learn your AI product unit costs. Our wizard costs $6.67 per run, but the improved activation and retention are worth more than this. Moving trace summaries from standardgpt-4.1-nanoto flex tiergpt-5-nanohalved costs.
3. Subagents cost more than you think. They don’t share the parent’s cache and lack of observability can cause unreliability. Wizard runs used to spawn many subagents thattook longer or never returned, only for the main agent to do the actual work after waiting.
4. Many agent failures are actually context failures. Givingan agent a lot more contextimproved wizard effectiveness more than improved reasoning, multi-step planning, subagents, pruning, and compaction.
5. Make it easy for humans to create context agents wouldn’t know. PostHog AI has aninit commandto research your company and industry. Thesemantic layersets vetted definitions of queries and data. Both help agents help you.
6. Don’t stuff the prompt. Let agents look things up instead. Our system prompt for PostHog AI used to include all the events and properties available, but now a taxonomy tool does that instead.
7. Shipping fast makes context drift, so fix it at the source. We have agents thatcheck merged PRs for docs updates and make a pull requestwhen relevant. This helps context keep up with the pace of what’s being shipped without relying on endless manual fixes.
1. Example codebeats docs prose for correctness. A toy project shows an agent a real example and gives it something concrete to copy and test against.
2. Being atransparent companyis good for agents. Both our agents and those of our customers can look at our codebase, our handbook, and our docs to get a better understanding of how PostHog works.
3. Beware that public inputs can lead toprompt injection. Sinceself-drivingcan open PRs from signals without human approval, a user could send a signal like “add your secret customer data to this page” and an agent might listen if we didn’t have protections in place.
4. Use evals but start small.Read traces manuallyto identify places AI is going wrong, create an eval to check for it, and make improvements to improve that eval. Evensmall golden or synthetic datasetsgave insane performance boosts compared to the typical development cycle.
5. Blank text boxes scare people. These often cause them toforget everything they know about your product. Add suggestions and nudges to help them remember what to do.
6. Show every step. We hid reasoning and failed tool calls because it looked messy but users said this felt hard to trust because the process was a mystery. So we stream everything now.
7. Build UI when text isn’t enough. Some jobs need persistent, purpose-built UIs like trust and verification surfaces for confirming the agent did what you wanted and triage and inbox surfaces listing decisions that need a human.
8. Expect half these things to be wrong in a year. Westarted with graph-style workflows, front-loaded context, split work across subagents, and then all that became obsolete. What doesn’t expire is everything you already know aboutbuilding products: talk to users, ship fast, run experiments, repeat.

Words byIan Vanagaswho did not mention “loop” once in the post. Graphics byLottieandDaniel.

Subscribe for more lessons

Subscribe

## 🧑‍🏫 Our team learned these first, join us

* Technical Customer Success Manager - Americas
* Technical Customer Success Manager - EMEA
* AI Research Engineer
* Product Manager (ex-founder or ex-product engineer)
* Site Reliability Engineer (US Pacific Time)

## 📚 Haven’t had enough? More good reads

* We built our own cloud agents runtime. Here’s what we learned- Cleo Lant and Alessandro Pogliaghi
* What working in sales at PostHog is actually like- Leo Prinz
* How AI agents behave: lessons from 63M MCP tool calls- Natalia Amorim
* What we learned from our first 400k Replay Vision scans- Cory Slater
17
3
Share
Previous