---
title: 'Announcing Cline Kanban: a CLI-agnostic app for multi-agent orchestration. - Cline Blog'
url: https://cline.bot/blog/announcing-kanban
site_name: tldr
content_file: tldr-announcing-cline-kanban-a-cli-agnostic-app-for-mul
fetched_at: '2026-03-28T11:10:52.597601'
original_url: https://cline.bot/blog/announcing-kanban
date: '2026-03-28'
description: 'Here’s the elephant in the room about coding in 2026: the bottleneck isn’t the AI; it’s you. Not your skill. Not your prompts. Your attention. Your cognitive bandwidth. If you’ve spent any real time with coding agents, you know the feeling. You start the morning with a clean plan. Spin up a few agents. One is refactoring the auth module. Another is writing tests. A third is scaffolding a new API endpoint. You’re flying. Then around 10:30 AM, you look up and realize you have 20 terminal window'
tags:
- tldr
---

Written by
Sidd Sant
Published on
March 26, 2026

# Announcing Cline Kanban: a CLI-agnostic app for multi-agent orchestration.

Here’s the elephant in the room about coding in 2026: the bottleneck isn’t the AI; it’s you.

Not your skill. Not your prompts. Your attention. Your cognitive bandwidth.

If you’ve spent any real time with coding agents, you know the feeling. You start the morning with a clean plan. Spin up a few agents. One is refactoring the auth module. Another is writing tests. A third is scaffolding a new API endpoint. You’re flying.

Then around 10:30 AM, you look up and realize you have 20 terminal windows open. One agent is blocked waiting for a decision you forgot to make. Another finished 40 minutes ago and you never noticed. A third went sideways three commits back. You’re no longer flying. You’re drowning.

The problem isn't the tools - those tools are incredible. The real problem is that nothing was designed to help youorchestratethem.

## The real cost of context switching

Every time you alt-tab to check on an agent, you pay a tax. And I don’t mean the two seconds it takes to switch windows. I mean the invisible, expensive cost of re-loading context in your head.Where am I? What was this agent doing? Where did I leave off? What does it need from me?

That mental reload takes 30 seconds, sometimes a minute. Multiply it by 15 or 20 agents across a couple of projects. In addition: it’sexhausting. Unfortunately our human mind’s programmed to be more focused and context syncing, not as clean as opening up a new terminal window for agents.

We adopted AI agents to move faster, but now the overhead of babysitting them is slowing us down (and hurting my brain!!)

## What if your agents lived on a kanban board?

That’s the question that started everything for us. Not “how do we build a better agent?”. There are brilliant teams working on that already. The question was simpler and, honestly, more urgent: how do we help a human stay sane while running a dozen of them?

So we built a kanban view for coding agents.

Think of it like a project board, but every card is a live agent task. At one glance you see which agents are running, which are done, which are blocked. No more cycling through terminals trying to reconstruct what’s happening. No more “wait, did that one finish?” moments. You open the board, and you know.

And here’s the thing that surprised even us: the psychological effect is massive. Parallelization stops being scary when you can actually see it. Kick off 20 tasks with confidence, because you’re not holding them all in your head anymore. The board is holding them for you.

## Dependencies change everything

Here’s where it gets interesting. Real work isn’t a flat list of tasks, but a sequence of multiple things to be done: the API endpoint can’t be tested until the schema migration is done; the frontend component depends on the hook that another agent is still writing.

While orchestrating the task cards, we made dependency linking from day 1. You connect tasks to each other, and then the board respects those relationships. When a parent task completes, its dependent tasks can automatically kick off. When something is blocked, you see it immediately — not 45 minutes later when you finally check that terminal.

This turns the agent workflow from a bag of disconnected terminals into something that actually resembles a pipeline. Users think about tasks and dependencies, and the board handles the sequencing.

## Your agents, your choice

Cline started by being model agnostic: use whatever LLM you want, we just want you to ship great code. That philosophy hasn’t changed and it’s now grown.

Cline Kanban is agent agnostic. Use the Cline agent harness if you love it. But also Claude Code, Codex, etc… We’re not here to lock you into our agent, but here to be the calm, organized layer on top ofwhateveragents you choose to run.

Because the real value isn’t in the agent. It’s in helping the human stay in control of them.

## Focus is the whole game

While terminals have always been the interfaces that developers love, we all know how chaotic it feels to have dozens of agents, all running in the terminal with no idea what’s happening. We all know you deserve a better experience.

What about a version of coding that feels calm with directed momentum. You define the work. You set the dependencies. You hit the start. And then you pay attention only to what needs your attention, not everything, all the time.

We’re not trying to replace your terminal. We’re trying to give you your attention back. If 20 open terminals sounds familiar, come take a look!

Trynpm i -g clineto get started!

## Related Posts

### A practical guide to hill climbing

February 26, 2026

### Post-mortem: Unauthorized Cline CLI npm publish on February 17, 2026

February 24, 2026

### Introducing Cline CLI 2.0: from sidebar to the terminal

February 13, 2026