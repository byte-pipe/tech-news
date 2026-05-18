---
title: 'GitHub - humanlayer/12-factor-agents: What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? · GitHub'
url: https://github.com/humanlayer/12-factor-agents
site_name: github
content_file: github-github-humanlayer12-factor-agents-what-are-the-pri
fetched_at: '2026-05-18T12:11:37.567781'
original_url: https://github.com/humanlayer/12-factor-agents
author: humanlayer
description: What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers? - humanlayer/12-factor-agents
---

humanlayer

 

/

12-factor-agents

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.5k
* Star20.2k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

273 Commits
273 Commits
content
content
 
 
drafts
drafts
 
 
hack/
contributors_markdown
hack/
contributors_markdown
 
 
img
img
 
 
packages
packages
 
 
workshops
workshops
 
 
.gitignore
.gitignore
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# 12-Factor Agents - Principles for building reliable LLM applications

In the spirit of12 Factor Apps.The source for this project is public athttps://github.com/humanlayer/12-factor-agents, and I welcome your feedback and contributions. Let's figure this out together!

Tip

Missed the AI Engineer World's Fair?Catch the talk here

Looking for Context Engineering?Jump straight to factor 3

Want to contribute tonpx/uvx create-12-factor-agent- check outthe discussion thread

Hi, I'm Dex. I've beenhackingonAI agentsfora while.

I've tried every agent framework out there, from the plug-and-play crew/langchains to the "minimalist" smolagents of the world to the "production grade" langraph, griptape, etc.

I've talked to a lot of really strong founders, in and out of YC, who are all building really impressive things with AI. Most of them are rolling the stack themselves. I don't see a lot of frameworks in production customer-facing agents.

I've been surprised to findthat most of the products out there billing themselves as "AI Agents" are not all that agentic. A lot of them are mostly deterministic code, with LLM steps sprinkled in at just the right points to make the experience truly magical.

Agents, at least the good ones, don't follow the"here's your prompt, here's a bag of tools, loop until you hit the goal"pattern. Rather, they are comprised of mostly just software.

So, I set out to answer:

### What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers?

Welcome to 12-factor agents. As every Chicago mayor since Daley has consistently plastered all over the city's major airports, we're glad you're here.

Special thanks to@iantbutler01,@tnm,@hellovai,@stantonk,@balanceiskey,@AdjectiveAllison,@pfbyjy,@a-churchill, and the SF MLOps community for early feedback on this guide.

## The Short Version: The 12 Factors

Even if LLMscontinue to get exponentially more powerful, there will be core engineering techniques that make LLM-powered software more reliable, more scalable, and easier to maintain.

* How We Got Here: A Brief History of Software
* Factor 1: Natural Language to Tool Calls
* Factor 2: Own your prompts
* Factor 3: Own your context window
* Factor 4: Tools are just structured outputs
* Factor 5: Unify execution state and business state
* Factor 6: Launch/Pause/Resume with simple APIs
* Factor 7: Contact humans with tool calls
* Factor 8: Own your control flow
* Factor 9: Compact Errors into Context Window
* Factor 10: Small, Focused Agents
* Factor 11: Trigger from anywhere, meet users where they are
* Factor 12: Make your agent a stateless reducer

### Visual Nav

## How we got here

For a deeper dive on my agent journey and what led us here, check outA Brief History of Software- a quick summary here:

### The promise of agents

We're gonna talk a lot about Directed Graphs (DGs) and their Acyclic friends, DAGs. I'll start by pointing out that...well...software is a directed graph. There's a reason we used to represent programs as flow charts.

### From code to DAGs

Around 20 years ago, we started to see DAG orchestrators become popular. We're talking classics likeAirflow,Prefect, some predecessors, and some newer ones like (dagster,inggest,windmill). These followed the same graph pattern, with the added benefit of observability, modularity, retries, administration, etc.

### The promise of agents

I'm not the firstperson to say this, but my biggest takeaway when I started learning about agents, was that you get to throw the DAG away. Instead of software engineers coding each step and edge case, you can give the agent a goal and a set of transitions:

And let the LLM make decisions in real time to figure out the path

The promise here is that you write less software, you just give the LLM the "edges" of the graph and let it figure out the nodes. You can recover from errors, you can write less code, and you may find that LLMs find novel solutions to problems.

### Agents as loops

As we'll see later, it turns out this doesn't quite work.

Let's dive one step deeper - with agents you've got this loop consisting of 3 steps:

1. LLM determines the next step in the workflow, outputting structured json ("tool calling")
2. Deterministic code executes the tool call
3. The result is appended to the context window
4. Repeat until the next step is determined to be "done"

initial_event
 
=
 {
"message"
: 
"..."
}

context
 
=
 [
initial_event
]

while
 
True
:
 
next_step
 
=
 
await
 
llm
.
determine_next_step
(
context
)
 
context
.
append
(
next_step
)

 
if
 (
next_step
.
intent
 
==
=
 
"done"
):
 
return
 
next_step
.
final_answer

 
result
 
=
 
await
 
execute_step
(
next_step
)
 
context
.
append
(
result
)

Our initial context is just the starting event (maybe a user message, maybe a cron fired, maybe a webhook, etc), and we ask the llm to choose the next step (tool) or to determine that we're done.

Here's a multi-step example:

027-agent-loop-animation.mp4

GIF Version

## Why 12-factor agents?

At the end of the day, this approach just doesn't work as well as we want it to.

In building HumanLayer, I've talked to at least 100 SaaS builders (mostly technical founders) looking to make their existing product more agentic. The journey usually goes something like:

1. Decide you want to build an agent
2. Product design, UX mapping, what problems to solve
3. Want to move fast, so grab $FRAMEWORK andget to building
4. Get to 70-80% quality bar
5. Realize that 80% isn't good enough for most customer-facing features
6. Realize that getting past 80% requires reverse-engineering the framework, prompts, flow, etc.
7. Start over from scratch

Random Disclaimers

DISCLAIMER: I'm not sure the exact right place to say this, but here seems as good as any:this in BY NO MEANS meant to be a dig on either the many frameworks out there, or the pretty dang smart people who work on them. They enable incredible things and have accelerated the AI ecosystem.

I hope that one outcome of this post is that agent framework builders can learn from the journeys of myself and others, and make frameworks even better.

Especially for builders who want to move fast but need deep control.

DISCLAIMER 2: I'm not going to talk about MCP. I'm sure you can see where it fits in.

DISCLAIMER 3: I'm using mostly typescript, forreasonsbut all this stuff works in python or any other language you prefer.

Anyways back to the thing...

### Design Patterns for great LLM applications

After digging through hundreds of AI libriaries and working with dozens of founders, my instinct is this:

1. There are some core things that make agents great
2. Going all in on a framework and building what is essentially a greenfield rewrite may be counter-productive
3. There are some core principles that make agents great, and you will get most/all of them if you pull in a framework
4. BUT, the fastest way I've seen for builders to get high-quality AI software in the hands of customers is to take small, modular concepts from agent building, and incorporate them into their existing product
5. These modular concepts from agents can be defined and applied by most skilled software engineers, even if they don't have an AI background

#### The fastest way I've seen for builders to get good AI software in the hands of customers is to take small, modular concepts from agent building, and incorporate them into their existing product

## The 12 Factors (again)

* How We Got Here: A Brief History of Software
* Factor 1: Natural Language to Tool Calls
* Factor 2: Own your prompts
* Factor 3: Own your context window
* Factor 4: Tools are just structured outputs
* Factor 5: Unify execution state and business state
* Factor 6: Launch/Pause/Resume with simple APIs
* Factor 7: Contact humans with tool calls
* Factor 8: Own your control flow
* Factor 9: Compact Errors into Context Window
* Factor 10: Small, Focused Agents
* Factor 11: Trigger from anywhere, meet users where they are
* Factor 12: Make your agent a stateless reducer

## Honorable Mentions / other advice

* Factor 13: Pre-fetch all the context you might need

## Related Resources

* Contribute to this guidehere
* I talked about a lot of this on an episode of the Tool Use podcastin March 2025
* I write about some of this stuff atThe Outer Loop
* I dowebinars about Maximizing LLM Performancewith@hellovai
* We build OSS agents with this methodology undergot-agents/agents
* We ignored all our own advice and built aframework for running distributed agents in kubernetes
* Other links from this guide:12 Factor AppsBuilding Effective Agents (Anthropic)Prompts are FunctionsLibrary patterns: Why frameworks are evilThe Wrong AbstractionMailcrew AgentMailcrew Demo VideoChainlit DemoTypeScript for LLMsSchema Aligned ParsingFunction Calling vs Structured Outputs vs JSON ModeBAML on GitHubOpenAI JSON vs Function CallingOuter Loop AgentsAirflowPrefectDagsterInngestWindmillThe AI Agent Index (MIT)NotebookLM on Finding Model Capability Boundaries
* 12 Factor Apps
* Building Effective Agents (Anthropic)
* Prompts are Functions
* Library patterns: Why frameworks are evil
* The Wrong Abstraction
* Mailcrew Agent
* Mailcrew Demo Video
* Chainlit Demo
* TypeScript for LLMs
* Schema Aligned Parsing
* Function Calling vs Structured Outputs vs JSON Mode
* BAML on GitHub
* OpenAI JSON vs Function Calling
* Outer Loop Agents
* Airflow
* Prefect
* Dagster
* Inngest
* Windmill
* The AI Agent Index (MIT)
* NotebookLM on Finding Model Capability Boundaries

## Contributors

Thanks to everyone who has contributed to 12-factor agents!

 
 
 
 
 
 

 
 
 
 
 
 

## License

All content and images are licensed under aCC BY-SA 4.0 License

Code is licensed under theApache 2.0 License

## About

What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of production customers?

### Topics

 framework

 ai

 memory

 orchestration

 agents

 12-factor

 rag

 prompt-engineering

 llms

 context-window

 12-factor-agents

### Resources

 Readme

 

### License

 View license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

20.2k

 stars
 

### Watchers

191

 watching
 

### Forks

1.5k

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript80.2%
* Jupyter Notebook11.2%
* Python7.5%
* Other1.1%