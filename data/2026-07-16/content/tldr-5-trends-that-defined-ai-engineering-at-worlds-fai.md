---
title: 5 Trends That Defined AI Engineering at World’s Fair 2026
url: https://www.latent.space/p/aiewf26trends
site_name: tldr
content_file: tldr-5-trends-that-defined-ai-engineering-at-worlds-fai
fetched_at: '2026-07-16T11:35:00.213527'
original_url: https://www.latent.space/p/aiewf26trends
author: Richard MacManus
date: '2026-07-16'
description: 'At this year''s AIE World’s Fair, AI engineering entered a new phase: building systems around agents, rather than just building with agents.'
tags:
- tldr
---

# 5 Trends That Defined AI Engineering at World’s Fair 2026

### At this year's AIE World’s Fair, AI engineering entered a new phase: building systems around agents, rather than just building with agents.

Richard MacManus
Jul 14, 2026
73
2
Share

swyx’s note: thanks toRichardfor covering AIE while I was working on the conference itself! Make sure you haveopted intotheAINewsfeed to get our weekday updates. AIE next returns toNYC, Oct 12-14, with a heavy focus on AI in Finance this year.

AI engineering has come a long way in three years. When swyxcoined the term “AI engineer”in June 2023, he was giving a name to a new kind of developer emerging from the big bang of large language models. It seems like ancient history now, but remember when we called the intersection of AI and software development “prompt engineering”? That wasjust months beforeswyx’s reframing.

The latestAI Engineer World’s Fairshowed just how much the field has matured. Whether or not “AI engineer” has become a formal job title everywhere is almost beside the point. The engineering practices that have developed around AI over the past three years — building coding agents, designing harnesses, managing context, evaluating model outputs, and orchestrating increasingly autonomous systems — arebecoming part of mainstream software development.

Rather than focusing on individual announcements at AIEWF, this post will pick out five larger trends that show where AI engineering stands in 2026.

## 1:The focus shifts from agents to the systems around them

One of the clearest ways to see how AI engineering has evolved is to compare two essays by former OpenAI researcher, and now co-founder of Thinking Machines Lab, Lilian Weng. Her influential 2023 article,LLM Powered Autonomous Agents, described the anatomy of an LLM agent in terms of planning, memory and tool use. AutoGPT, BabyAGI and GPT-Engineer were among her examples — proof-of-concept systems that suggested autonomous agents might soon become practical.

Her new 2026 essay,Harness Engineering for Self-Improvement, takes a very different perspective. Rather than focusing on the agent itself, Weng argues that the system surrounding the model has become just as important: the harness that manages workflows, context, permissions, evaluation, persistent state and continuous improvement. In other words, AI engineering has moved beyond prompting models toward engineering reliable systems around them.

Coding agent loop; Image by Lilian Weng

This shift was very much top of mind at AIEWF. I don’t think AutoGPT — the buzzy autonomous agent projecteveryone was talking about in 2023— was even mentioned this year. Instead, the conversation revolved around Claude Code, Codex, Gemini CLI, Cursor, Warp and all the infrastructure needed to make coding agents dependable in production.

I remember being turned off by the AutoGPT buzz at the 2023 event, mainly because all the discussions seemed to focus on removing humans from the equation. But over the past few years we’ve learned thatcomplete agent autonomy is not only unreliable, it isn’t even desirable — especially at scale. So it was a relief that at AIEWF, agents were largely positioned as augmenting the AI engineer, rather than replacing them.

During the OpenAI keynote on day 2 at AIEWF, Romain Huet emphasized this point. Using tools like OpenAI’s Codex, Huet argued, engineers can more easily collaborate with agents. As he put it, “software ate the world, and then AI ate software, but now what we’re here to say is that the AI engineers are eating the world.”

Despite the growing power of AI engineers, there’s also a sense that even the frontier companies don’t fully understand how their models are evolving — and so how much control can engineers truly have over them?In a separate keynote, Anthropic’sThariq Shihipar talked about how their latest model, Claude Fable, is like an organic system —“models are grown, not designed.”There’s a “capability overhead,” he said, where “Claude gets smarter in a spiky way.”

AINews: Weekday Roundups

## [AINews] The Field Guide to Fable

Jul 7

While we congratulate (friend of the show!) General Intuition on their new model and (friend of the show!) Shunyu Yao on their new model, and the world awaits the release of GPT-5.6 Sol Ultra, people are racing to find the limits of Fable 5 before the

Read full story

All the more reason to build systems for agentic development, so that we can evaluate and monitor the outputs.

## 2: Loop engineering is the new control layer

By the end ofthe first morning of keynotes at AIEWF, it was clear that “loops” was the buzzworddu jourof the event. Overuse of the term aside, it did highlight a key point of tension around AI engineering: how much control should agents have, and where should humans remainin the loop?

OpenClaw creator Peter Steinberger advocating for better loops.

One approach a lot of leading engineers are now taking is putting themselves in an “outer loop” — to oversee the largely autonomous work being done by agents in an inner loop.

Roland Gavrilescuis co-founder and CEO of Introspection, a new company building infrastructure for deploying self-improving systems. Inan interview with Latent Space, he explained how the concept of “autoresearch” provides the necessary feedback structure for agent loops:

“You can think of the system as having aninner loopand anouter loop. The inner loop is the primary system interacting with users and performing the work.Autoresearch is more concerned with the outer loop: another system that studies and maintains the primary system.“

#### Autoresearch: The feedback loop behind self-improving agents

Richard MacManus
·
Jul 1
Read full story

The outer loop can include feedback signals, evals and human input. So it might still be largely autonomous, but the point is it is a method of oversight for the primary agent loop. Former Google engineering leaderAddy Osmanihad a nice line relating to this, saying that “agents can run much more of the inner execution loop, but that outer loop is still engineering.”

The term “loop engineering” came up multiple times during AIEWF, suggesting that it’s the human AI engineer’s responsibility to build these loop systems. Even the “ClawFather” Peter Steinberger, creator of OpenClaw, makes a point of putting himself in the outer loop. In the OpenAI keynote, he explained that“the agent runs the inner execution loop; I set the direction and I make decisions in the outer loop.”

The Loop Debate at AIEWF.

On the final day,an on-stage debate was heldto determine whether fully autonomous agents were capable of managing loops in reality.Dex Horthyfrom HumanLayer claimed that “the hype is outrunning the discipline.” He wasn’t against loops, per se, noting that Kubernetes is built on control loops — “but they’re deterministic loops.” Geoffrey Huntley, creator of the Ralph Loop, admitted that loops were “frontier thinking,” but he had a wonderful analogy for the audience to ponder:

“[We’re] kind of like locomotive engineers now. That’s our job: to keep the locomotive on the rails.”

## 3: AI engineering enters the enterprise

This way of working with AI tools is starting to make its way into enterprises, typically via a new role called a “forward deployed engineer” (FDE) — where engineers work directly with organizations to implement AI capabilities.

#### Forward Deployed Engineers and the future of software engineering

Richard MacManus
·
Jul 1
Read full story

Natalie Meurer, who leads FDE at Sierra,told Latent Spacethat implementing AI into organizations typically requires a lot of orchestration.“Every enterprise we work with wants to know how it can maintain everything its agentic ecosystem is capable of doing,”she said. “It needs to manage all the integrations and all the teams that contribute to the agent.”

Cursor’s Pauline Brunet talking about FDEs in an AIEWF session.

In her session at AIEWF, Cursor’sPauline Brunetspoke about what their FDEs look to achieve in each engagement:

“When [we] walk away at the end of the engagements — and we, in our case, have deployed cloud agents, long-running agents, automations, [and] we’ve built applications on top of our Cursor SDK — that when we walk away, it is a strict ROI for them.That means they’re not gonna turn things off when we leave.”

Another term used regularly at the conference was “software factory.” At Cursor, “a software factory means long-running agents helping people throughout that entire process,” said Brunet. This is basically what her team of FDEs is responsible for implementing, sitting alongside their customers’ engineers.

Where human engineers fit into a software factory is a key issue for enterprises. Warp CEOZach Lloyd explainedthat organizations need to choose which parts of the lifecycle to automate, and where humans should be brought into the loop.

Warp’s Zach Lloyd on building the thing that builds the product.

“You choose your repositories, the parts of the software lifecycle you want to automate, andthe points where humans should be brought into the loop,” Lloyd told us, regarding his company’s new software factory platform, Oz. “Different organizations and codebases will have different preferences. Do you fully automate code review? Do you have humans review certain high-risk changes?”

#### Warp CEO Zach Lloyd on why software factories are the next phase of coding

Richard MacManus
·
Jul 1
Read full story

Another concern for enterprises is managing their unique organizational data in AI systems.Prukalpa Sankarfrom Atlan spoke at the conference about “context engineering,” explaining ina tweetthat it’s important to consider“​​how context flows from your business systems into a shared company brain, then out to agents, copilots, and apps through MCP, APIs, and retrieval.”

Finally, lest we think enterprises are all-in on agents,Cursor’sBrunet pointed outthat enterprise adoption of AI “is still concentrated among early adopters.” So finding “the right champions inside an organization” is a challenge for FDEs at this stage.

#### How Cursor deploys AI inside the enterprise

Richard MacManus
·
Jul 1
Read full story

## 4: Coding agents replace IDEs as the developer interface

Perhaps the biggest practical change since the first AI Engineer Summit is how developers interact with AI on a daily basis.

In 2023, AI-assisted programming largely meant GitHub Copilot completing the next few lines of code. Most developers were still writing almost everything themselves, using AI as an intelligent autocomplete.But now we have tools such as Claude Code, Codex, Gemini CLI, Cursor and Warp.These “coding agents” can typically understand a broader objective, explore a codebase, modify multiple files, run tests, debug failures and iterate on their own work before presenting it back to the developer.

In Barr Yaron’s AI engineering survey, coding agents was a key trend.

The trend of coding agents now extends to web development too — with the recent release of Vercel’s eve, which the company calls an “agent framework,” comparable to its popular open source React framework, Next.js.

Vercel’s Chief of Software, Andrew Qu,told Latent Space at AIEWFthatagents are effectively a new type of software. “They [agents] are not as predictable as web applications,” he explained. “The infrastructure can look similar, but the interaction, interface and outputs are much more dynamic.”

#### Vercel's Andrew Qu on why agents are a new kind of software

Richard MacManus
·
Jul 3
Read full story

Qu added that the job of building a framework for agent development is far from over. “A year ago, we did not know sandboxes would become so important, or how much demand there would be for secure code execution and long-running jobs,” he said. “As we learn more from production, there will be much more to build.”

A for agents? Andrew Qu flashes the Vercel triangle logo.

This brings us back to the software factory trend, when developers are managing multiple agents.Charlie Holtz, CEO of Conductor, reminded the AIEWF audience that regardless of the coding harness, human engineers should always remain in control.

“I don’t want the future to be built around factories,” Holtz said.“I want to feel like a human, I want to be in the flow, I want to be in front of an orchestra, waving my baton.”

There was a sense during the conference that AI engineers aren’t yet aligned on which term is more appropriate: software factories or orchestras? Even Geoffrey Huntley, a loopmaxxing advocate, cautions about getting ahead of ourselves when it comes to automation:

“My biggest concern is that this time next year at the conference, we’re going to see a whole bunch of folks saying, our factories failed, our loops failed.These are things that we are still yet to figure out.”

## 5: Every agent platform is building around skills

One of the talking points of the conference was “skills,” a concept Anthropic popularized when it introduced “agent skills” to Claudelast October. To borrowAddy Osmani’s definition, skills “encode the workflows, quality gates, and best practices that senior engineers use when building software.”

At AIEWF, Vercel’s Andrew Qu said that skills were“useful as portable, on-demand knowledge.”Introspection co-founder Roland Gavrilescu declared that AI engineering has shifted “from agent tools to agent skills.”

PicoCreator - AI builder @ 🇫🇷
@picocreator
By queue vote : the most oversubscribed workshop is the dark arts of skills md 
@aiDotEngineer
 🤯 
11:19 PM · Jun 29, 2026
 · 
432 Views
1 Repost
 · 
6 Likes

In a session on the main stage,Philipp Schmidfrom Google DeepMind showed how using skills (and other declarative Markdown files) allows developers to use “agents without code.”His main point was that skills reduce the need for orchestration code, which up till recently was typically done using Python. His conclusion:

“Agents are just files. We write markdown files to extend capabilities. Agents can learn from those, can create their own files.”

Paul Bakaus, who used to work for Google but now runs a company called Renaissance Geek, has created an entire project around agent skills.Impeccableis an open source design skills system that gives coding agents a vocabulary for improving interfaces. He even advocates for “skill engineering” as a discipline in its own right.

Paul Bakaus: “You can’t one-shot design.”

Inan interview with Latent Space,Bakaus argued that most skills — and indeed most models — are not very creative.“They converge in one direction, and if everybody uses the same skill to do frontend design work or something like that, everything ends up looking the same,” he said.

#### Skill engineering and the case against one-shot AI design

Richard MacManus
·
Jul 2
Read full story

Apparently there’s also such a thing as “skills hell,” which Matt Pocock said is comparable to previous developer frustrations — like frameworks hell. In a virtual presentation, Pocock provided a detailed checklist for writing skills, which you can see in the video below. In a nutshell,he advises writing fewer and smaller skills, and putting more thought into structure.

In a closing keynote, Y Combinator president Garry Tan implored the audience to use skills and other “AI native” approaches at their own startups or employers. Talking about business functions like sales, support and finance, Tan said that “the AI native companies that I see inside YC encode all of that as skills, written procedures that their agents execute, andthey hire engineers whose job it is to maintain those skills, to do the work the skills can’t do yet.”

But again, there’s a danger in relying too much on what agents autonomously do. As AIEWF attendee Tyler Brownnoted on X, “autonomy without structure creates as much slop as leverage.” One of his learnings from the conference was to“re-visit and re-implement your skills”:

“Each time there’s a new model release, it’s as if you have a kid that grows from middle school to high school. You have to change the curriculum for them to get the benefits of the new model.”

## Agent engineering at scale

It’s been three full years since The Rise of the AI Engineer and the first AI Engineer Summit. Looking back, it really is striking how much the conversation has evolved. Three years ago, the focus was on proving that LLMs could act as autonomous agents at all (and the answer at that time was usuallyno). AutoGPT, prompt engineering, and early orchestration frameworks like Langchain dominated the discussion back then.

Now that agents not only work, but have proven they can scale,this year’s AI Engineer World’s Fair was able to concentrate on the bigger problems: building reliable systems, orchestrating teams of agents, managing context, evaluating outputs and integrating AI into production software.

Agents are everywhere now…even on the back of San Francisco buses.

The term “AI engineer” may have started life as a new job title, but at AIEWF 2026 it felt more like a description ofwhere software engineering itself is heading. Whether developers call themselves AI engineers, software engineers or Forward Deployed Engineers, they’re increasingly working with the same set of ideas: coding agents, harness engineering, designing loops, and orchestration.

73
2
Share
Previous