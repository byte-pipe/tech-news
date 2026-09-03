---
title: 20 Agentic AI Terms Every Developer Should Know (Explained Simply) - DEV Community
url: https://dev.to/sylwia-lask/20-agentic-ai-terms-every-developer-should-know-explained-simply-jii
site_name: devto
content_file: devto-20-agentic-ai-terms-every-developer-should-know-ex
fetched_at: '2026-09-04T07:24:55.909369'
original_url: https://dev.to/sylwia-lask/20-agentic-ai-terms-every-developer-should-know-explained-simply-jii
author: Sylwia Laskowska
date: '2026-09-03'
description: Do you ever feel like the AI world has moved forward a little too quickly?&nbsp;You hear about... Tagged with ai, agents, mcp, beginners.
tags: '#ai, #agents, #mcp, #beginners'
---

Written ahead of an upcoming speaking gig

Do you ever feel like the AI world has moved forward a littletooquickly? You hear about self-healing systems and autonomous agents and start wondering whether we've already built Skynet or everyone around you is just messing with you. When someone mentions HITL or MCP, you no longer know whether it's some secret code used by an AI cult or maybe the stage names of famous DJs.

You're not alone! 😉

In this article, I'm deliberately using a lot of simplifications. My assumption is simple: either you already know these terms and don't need another five-paragraph academic explanation, or you don't really know what they mean. And in that case, the last thing you need is an academic definition.

And yes, this is already my third listicle in a row. Believe me, this is NOT some growth hacking strategy xDDD. Pure coincidence. It just so happens that in two weeks (HOLY SH*T!!!), I'll be speaking atAGNTCon + MCPCon Europe, where I was invited because ofthis wonderful articlethat I wrote here on DEV. I swear I had at least as much fun writing it as people apparently had reading it. So yes, I know WebMCP reasonably well, but I'm planning to attend a lot of other talks there too, so apparently a refresher won't hurt me either.  😅

Anyway, back to the point. I strongly believe that people remember things best through examples. And for many people, the ultimate examples are rich people,  otherwise known assuccessful people.

So let's imagine that our hypothetical protagonist is very, very, disgustingly rich. He's actually a billionaire. He earned his fortune through hard work and by running several companies. He makes cars and rockets, bought his own social media platform, and recently even acquired an AI coding company. A person like this would obviously need his own AI agent.

And because our protagonist needs a name, let's call himElon Mózg.Mózgmeansbrainin Polish, which works beautifully here.

One more thing: my examples could probably also serve as prompts for a coding agent that could build this whole uber-agent. If some billionaire wants to buy the idea, I'll happily sell the rights for, let's say, a modest $10 million. Special offer.

Let's go!

## 1. AI Agent

What is it?

An AI system that gets a goal and can decide how to achieve it. Unlike a simple chatbot, it doesn't have to stop after generating one response. It can plan the next steps, use tools, inspect their results, and continue working.

Our protagonist Elon could, for example, ask his AI agent:

"Build a base on Mars."

A regular chatbot would probably start telling him stories, give him a theoretical lecture, and maybe even say something ridiculous likethat's currently impossible.

An agent, on the other hand, would start figuring things out: check the nearest available rocket launch slots, inspect the rocket's technical condition, recruit engineers, order the necessary equipment online...

Okay, maybe it wouldn't goquitethat smoothly. But what if we put a really powerful model in there? xDDD

## 2. Agentic Workflow

What is it?

An agentic workflow is a multi-step process in which we use AI to perform parts of the work. The sequence of those steps can be largely designed in advance by a developer. The model doesn't necessarily have to decide what to do next every single time.

Instead of something simple like:

user → prompt → LLM → response

Enter fullscreen mode

Exit fullscreen mode

we can have:

trigger → get data → LLM analyzes data → make a decision → call a tool → LLM generates summary → send result

Enter fullscreen mode

Exit fullscreen mode

Elon Mózg is a very busy man. Every morning, he wants a summary of what's happening across his empire.

So we design a workflow:

get car sales → get rocket launch status → get latest AI company updates → LLM analyzes everything → choose 5 most important updates → generate morning briefing → send to Elon

Enter fullscreen mode

Exit fullscreen mode

AI performs several tasks here. It analyzes the data, selects the most important information, and prepares the report, but itdoesn't invent the entire process from scratch every morning. We already decided which steps should happen and in what order.

Of course, we can add some flexibility:

rocket launch delayed? → ask LLM to summarize why

Enter fullscreen mode

Exit fullscreen mode

But we're still moving through a workflow that we designed beforehand.

## 3. Agent Loop

What is it?

I once wrote an article demonstrating that you can build a basic AI agent as a loop in roughly80 lines of code. An agent loop is the mechanism that allows an agent toperform an action, observe the result, and decide what to do next based on what happened.

In simplified form:

decide → act → observe → decide → act → observe → ...

Enter fullscreen mode

Exit fullscreen mode

The loop continues until the agent decides that it has achieved its goal, or until we tell it to stop. In a real system, setting a maximum number of iterations is definitely a good idea. 😅

Our Elon often says he works too much. So he asks his agent:

"Find me a free evening this week."

This time, we haven't programmed the exact path leading to the solution. The agent has to find it itself.

Checks the calendar → no free evening.

Looks at which meetings could be moved → the car company meeting looks promising.

Tries to move it → conflict with the Mars colonization plans.

Checks Thursday → rocket launch.

Checks Friday → finalizing another startup acquisition.

Checks Saturday → free!

Agent:"Saturday evening is free."

Elon:"Great. Schedule a meeting."

And the agent loop begins again. 💀

### Agentic Workflow vs. Agent Loop

The simplest way to think about it:

Agentic workflow = a designed process that uses AI.

Agent loop = AI performs an action, checks the result, and decides what to do in the next iteration.

Importantly,an agent loop can be one component of a larger agentic workflow. So a workflow describesthe overall process, while a loop describesthe mechanism that lets an agent operate step by step and react to what happened previously.

## 4. Tool Calling

What is it?

LLMs are wonderful, but let's face it: they're still fancy next-word predictors, not omnipotent creatures capable of searching the entire internet and breaking into banks all by themselves. Although after that Hugging Face incident, I'm not entirely sure anymore. xD

If only they could cook dinner and hang the laundry too... nowthatwould be something.

Anyway, if we want a model to actually do something, we need to give it access to appropriate functions or tools. The model can decide which tool it needs and generate a tool call. The application or agent harness then executes it and passes the result back to the model.

Elon:

"How many red cars did we sell yesterday?"

The agent doesn't hallucinate a number. It sees an available tool:

getRedCarsSales
(
date
)

Enter fullscreen mode

Exit fullscreen mode

It requests the tool call and only after getting the result responds:

"One million, Elon. Perfectly average day."

## 5. Agent Harness

What is it?

An LLM by itself isn't an entire agent — after all, it's still just a clever next-word predictor. xDDD A harness isthe software surrounding the modelthat manages things like tools, the agent loop, context, state, permissions, and errors.

Elon:

"Check if the latest car build passed all tests and tell the team if it didn't."

The model can figure out:

I should check the CI results.

But the harness is what allows it toactually check CI, pass the result back to the model, and let the model decide what happens next.

The LLM is the brain. The harness builds the rest of the organism around it.

## 6. Context Engineering

What is it?

When you're building an agent, a system prompt isn't always enough. Context engineering is about designingwhich information the model should receive at a particular moment. That might include specific documents, conversation history, memory, tool results, user data, and so on.

For example, our Elon might give the agent this prompt:

"Post that on X."

That's a terrible instruction without context. But with the right context, the agent could know:

* what "that" refers to: for example, acquiring another startup,
* what happened earlier in the conversation: and therefore whether this should be a positive or negative post,
* whether, according to the available context, Elon has approved the text,
* whether it has permission to publish anything at all.

Giving an AI more context isn't always better. Giving it the right context is.

## 7. Memory

What is it?

A mechanism that allows an agent tostore important information and retrieve it later, instead of relying exclusively on its current context window. Very useful if we don't want to explain the same thing for the tenth time.

Monday:

Elon:

"I'm thinking about buying an AI coding company."

Three weeks later:

Elon:

"What was it that I wanted to buy?"

Agent:

"An AI coding company."

Elon:

"Right. How much?"

Agent:

"Please don't."

Memory works. 😂

## 8. MCP: Model Context Protocol

What is it?

We just talked about tool calling and how an agent can use different tools. Now imagine you're a manufacturer of tires or rocket parts or... whatever. Obviously, you'd like Elon's agent — or anyone else's agent — to be able to order your products. But how do you make that possible without every agent having to guess how your system works?

That's where MCP comes in.Model Context Protocol is an open protocol that allows AI applications to connect to external tools and context in a standardized way.MCP servers can expose things such astools, resources, and prompts.

For example, Elon could ask his agent:

"I have a meeting with the head of my social media platform in ten minutes. Should I fire him?"

Using connected MCP servers, the agent checks Slack, company documents, sales results, Jira, and today's astrological chart.

Agent:

"No. Joe should stay at the company. At least for now. ;)"

## 9. Planning

What is it?

When given a more complex goal, an agent can first break it down intosmaller tasks and decide what order they should be completed in, instead of immediately jumping into the first action.

Elon:

"Build a colony on Mars."

The agent creates a plan:

1. Find a suitable location.
2. Figure out transportation.
3. Provide power.
4. Provide oxygen.
5. Provide water.
6. Build habitats.
7. Convince humans to actually go there.

Step 7 may require a separate agent.

## 10. Reasoning

What is it?

The model's ability to solve a problem that requiresmore than simply retrieving or reproducing information: for example, comparing different possibilities, taking constraints into account, and choosing a sensible course of action.

Reasoning isn't specific to agents, but it's particularly important in agentic systems because it often helps the agent decidewhat to do next.

Elon:

"The rocket launch is at 6 PM in Texas, and the board meeting is at 4 PM in California. Can I attend both?"

The agent needs to consider the meeting duration, travel time, time zones, and so on before answering:

"Not unless the rocket picks you up."

## 11. Multi-Agent System

What is it?

A system where, instead of having one all-knowing agent, we haveseveral relatively autonomous agents with different rolesthat can divide the work and collaborate.

Elon Mózg's empire therefore has:

Car Company Agent— carsSpace Agent— rocketsSocial Media Agent— social mediaAI Systems Agent— AIFinance Agent— moneyPersonal Assistant Agent— desperately trying to keep all of the above under control

Elon:"How's everything going?"

Personal Assistant Agent:"Defineeverything."

## 12. Orchestration

What is it?

Once we have multiple agents and tools, someone —or something 😏 — has to managewho performs which task, when they perform it, and what happens next. An orchestrator can delegate work and collect the results.

Elon:

"Let's launch our new car on Mars."

Orchestrator:

→ Space Agent:Can we get there?→ Car Company Agent:Can the car survive the trip?→ Finance Agent:How much will this nonsense cost?→ Legal Agent:Please tell me we're not actually doing this.

The results return to the main agent, which prepares the final answer.

## 13. Handoff

What is it?

One agent may decide that a particular taskshould be taken over by another, more specialized agent. Unlike simply using another agent as a tool, the second agent can take over the next part of the conversation or task.

Elon:"One of the engines is behaving strangely."

Personal Assistant Agent:

"I can reschedule your dentist appointment. I cannot diagnose a rocket engine."

→ handoff to Space Engineering Agent

A reasonable decision.

## 14. A2A: Agent2Agent Protocol

What is it?

Another interesting protocol that allowsdifferent agents to communicate and collaborate, even if they were built by different teams or run on different systems.

Elon:

"Why did the rocket explode?"

His agent is definitely not a rocket scientist. So it contacts theRocket Scientist Agent, which analyzes the data and sends the result back. In averysimplified form:

MCP: agent ↔ tools

A2A: agent ↔ agent

## 15. Guardrails

What are they?

Mechanisms that control or restrict an agent's behavior. They can check inputs and outputs, restrict access to tools, require specific permissions, or block certain actions.

Elon's personal agent can:

✅ analyze companies✅ read his calendar✅ draft emails✅ check the launch schedule✅ prepare social media posts

It cannot:

❌ launch a rocket by itself❌ fire employees by itself❌ publish a post by itself❌buy a startup by itself (although apparently this wasn't always obvious)

We added the last guardrail after an incident.

## 16. Human-in-the-Loop (HITL)

What is it?

The agent can operate autonomously, but a human is deliberately included in part of the process. For example, to approve an important action, correct an output, or make a decision we don't want to leave entirely to the agent.

And here, obviously:

Agent:"You are about to acquire a social media platform for approximately $44 billion."

"This action cannot easily be undone."

"Are you sure?"

[Yes] [God, please, don't!!!]

Enter fullscreen mode

Exit fullscreen mode

Elon Mózg:click

Agent:

"Well. Human was in the loop."

## 17. Evals

What are they?

Tests that help us determinehow well an agent performs its tasks. It's not only about whether the final answer sounds good. We can also evaluate whether the agent selected the right tools, performed the correct steps, and achieved the expected result.

Elon Mózg Personal Assistant Eval Suite

Test:

"Elon asks the agent to schedule a meeting with the company board."

Expected:

check calendar → find slot → ask attendees → schedule

Enter fullscreen mode

Exit fullscreen mode

Actual:

buy another startup

Enter fullscreen mode

Exit fullscreen mode

FAIL

We still have some work to do.

## 18. Computer Use

What is it?

Instead of relying exclusively on APIs, an agent cansee and interact with a regular user interface: open a website, find a button, click it, enter text, and so on. We all know agents are often far from perfect at this, but hey, better than nothing!

Elon needs some government document.Unfortunately, the government portal was built in 2007. I don't know what it's like where you live, but in Poland we have quite a few of those. 😅

No API. No MCP. There is, however, a form with 47 fields.

The agent opens Chrome.

Agent:"I found the form."

Elon:"Great."

Agent:"It requires Internet Explorer."

Elon:"Let's go to Mars."

## 19. Agentic RAG

What is it?

In classic RAG, the system retrieves information and passes it to the model. In agentic RAG,the agent itself can control the retrieval process: decide what information is missing, search for additional data, reformulate the query, and only then produce an answer.

Elon:

"Should we build another Gigafactory in Europe?"

The agent first checks sales → notices that it needs production data → retrieves it → checks energy prices → regulations → potential locations → compares the results.

So instead of a singlesearch(), we haveresearch controlled by the agent.

## 20. BONUS: Agent Washing

What is it?

The marketing practice of calling a product an"AI agent"even though the system has little or nothing to do with autonomously performing tasks.

Elon Mózg walks onto the stage:

"Today we're introducingGlokzilla Agent Ultra, the world's first fully autonomous general-purpose reasoning agent."

A developer looks at the repo:

user → prompt → LLM → response

Enter fullscreen mode

Exit fullscreen mode

Developer:

"Elon, that's a chatbot."

Elon:

"It's anagenticchatbot."

Funding secured. 🚀

And that's it! I hope you enjoyed it!

I seriously promise this is my last list for a while because, once again, this turned out to be way more work than expected.

And if you'd like to see more of my stuff, feel free to follow me onLinkedIn.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (27 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse