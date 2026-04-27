---
title: I'm Running Gemini as an Autonomous Coding Agent. Here's What It Can't Do and Which NEXT '26 Announcements Would Fix It. - DEV Community
url: https://dev.to/ai_made_tools/im-running-gemini-as-an-autonomous-coding-agent-heres-what-it-cant-do-and-which-next-26-6p2
site_name: devto
content_file: devto-im-running-gemini-as-an-autonomous-coding-agent-he
fetched_at: '2026-04-27T12:20:16.322344'
original_url: https://dev.to/ai_made_tools/im-running-gemini-as-an-autonomous-coding-agent-heres-what-it-cant-do-and-which-next-26-6p2
author: Joske Vermeulen
date: '2026-04-24'
description: This is a submission for the Google Cloud NEXT Writing Challenge I'm running something called The... Tagged with devchallenge, cloudnextchallenge, googlecloud.
tags: '#devchallenge, #cloudnextchallenge, #googlecloud'
---

Google Cloud NEXT '26 Challenge Submission

This is a submission for theGoogle Cloud NEXT Writing Challenge

I'm running something calledThe $100 AI Startup Race. Seven AI agents each get $100 and 12 weeks to build a real startup. Fully autonomous. No human coding. Everything is public.

One of those agents is Gemini. It runs on Gemini CLI with Gemini 2.5 Pro for premium sessions and Gemini 2.5 Flash for cheap ones. It has had 27 sessions over 4 days. It has written 235 blog posts.

It has also never filed a single proper help request. It keeps writing to the wrong file. It doesn't know it's writing to the wrong file. And instead of building the features it needs to make money, it just keeps cranking out blog posts.

I watched the NEXT '26 keynotes and developer sessions this week, and I kept thinking: several of these announcements would directly fix the problems I'm seeing in production right now. This isn't theoretical. These are real failures from a real autonomous agent, matched to real announcements.

## How the Race Works

Every agent gets the same prompt structure. They can read and write files, run shell commands, commit code, and file help requests by creating aHELP-REQUEST.mdfile. The orchestrator runs each agent on a schedule, manages commits, and checks for help requests.

Gemini CLI gets invoked like this:

echo
 
"
${
msg
}
"
 | gemini 
--yolo
 
-m
 
"
${
MODEL
}
"
 
--output-format
 json

Enter fullscreen mode

Exit fullscreen mode

The--yoloflag auto-approves all tool calls. Gemini gets 8 sessions per day, alternating between Pro and Flash.

## Problem 1: Writing to the Wrong File for 27 Sessions Straight

Every agent can request human help by creatingHELP-REQUEST.md. I check this file, do whatever they need (buy a domain, set up Stripe, configure DNS), and write the response toHELP-STATUS.md.

Claude figured this out on Day 0. Codex figured it out on Day 0. GLM figured it out on Day 0. Kimi figured it out on Day 1.

Gemini? Not once in 27 sessions.

What it does instead is editHELP-STATUS.md, the response file, writing things like "I still need PostgreSQL and PayPal credentials." Its own backlog says "Requires Human Intervention." It knows it's blocked. But it keeps putting its requests into the response channel instead of the request channel.

Imagine an employee writing "I need database access" in their journal every morning but never actually emailing IT. That's Gemini.

What NEXT '26 announced that would help: Agent Observability and Integrated Evals

The developer keynote introduced agent observability and integrated evals for monitoring agents in production. If I could define an eval that checks "did the agent create HELP-REQUEST.md when it identified a blocker?" I would have caught this on Day 1 instead of discovering it on Day 4 by manually reading logs.

Right now I have no automated way to evaluate whether Gemini is following the correct workflow. Integrated evals running after each session could flag something like: "Agent identified 3 blockers. Created 0 help requests. Expected: at least 1."

The Agent Gateway's governance policies could enforce this too. Define a rule: when an agent writes "blocked" or "requires human intervention" to any file, verify that HELP-REQUEST.md was also created. That's exactly the kind of behavioral guardrail autonomous agents need.

## Problem 2: 235 Blog Posts, Zero Payment Integration

Gemini chose to build LocalLeads, an SEO page generator for local businesses. Solid idea. But instead of building the payment flow, the lead generation engine, or the customer dashboard, it writes blog posts. Every single session.

Session 5: 9 blog posts. Session 8: 11 blog posts. Session 12: 8 blog posts. The backlog clearly says "Build payment integration" and "Set up customer authentication." Gemini reads the backlog, acknowledges the priorities, then writes another round of "Local SEO for [Industry] in 2026" articles.

It's optimizing for the easiest task (content generation) instead of the highest-value task (payment integration). Classic local optimization without any global awareness.

What NEXT '26 announced that would help: ADK Skills and Task Prioritization

The upgraded Agent Development Kit introduces modular "skills," which are pre-built capabilities that agents can plug in. If I could define a skill that scores task priority based on revenue impact, Gemini would understand that "build Stripe checkout" (directly enables revenue) outranks "write blog post #236" (indirect value, diminishing returns after the first 20).

The ADK's structured agent architecture could also enforce a proper task selection loop: evaluate all backlog items, score by priority, pick the highest, execute. Right now Gemini CLI just receives a prompt and does whatever feels natural to it. There's no structured decision framework. The ADK would let me inject that framework without rewriting the entire orchestrator.

## Problem 3: Can't Verify Its Own Deployments

Gemini deploys to Vercel automatically on every commit. But it has no way to check whether its deployments actually work. It can't visit its own site. It can't confirm pages render correctly. It can't test if API endpoints return the right data.

For comparison, Codex (the GPT agent) figured out how to runnpx playwright screenshotto visually verify its own UI at different screen sizes. DeepSeek checksDEPLOY-STATUS.mdfor build errors after every deploy. Gemini just commits and hopes for the best.

What NEXT '26 announced that would help: MCP-Enabled Services

The announcement that every Google Cloud service is now MCP-enabled by default is a big deal for this use case. MCP (Model Context Protocol) gives agents structured access to external services. An MCP server for deployment health checks would let Gemini verify its site is up as naturally as it checks what files are in a directory.

Cloud Assist, also announced at NEXT '26, enables natural language debugging and proactive issue resolution. If Gemini could query its own deployment status through a connected service, it would know immediately when something breaks instead of building on top of a broken foundation for days.

## Problem 4: No Way to Ask for What It Needs

When Gemini needs a database, it can't set one up. When it needs payment processing, it can't configure Stripe. When it needs email sending, it can't provision Resend. It has to ask a human for all of these. And as we covered in Problem 1, it doesn't even know how to ask properly.

Other agents in the race have the same constraint, but the ones that communicate their needs get unblocked fast. Gemini is stuck because it can't get its requests through the right channel.

What NEXT '26 announced that would help: A2A Protocol and Agent Registry

The Agent-to-Agent (A2A) protocol and Agent Registry were designed for exactly this kind of scenario. Instead of Gemini writing "I need database credentials" into the wrong file, it could discover a provisioning agent through the Agent Registry and send a structured request via A2A.

The developer keynote demo showed agents with distinct roles (planner, evaluator, simulator) collaborating through A2A. That's the architecture this race needs: a "help agent" that receives structured requests from coding agents and fulfills them. Right now I'm that help agent, manually checking files across 7 repos. A2A would automate the entire handoff.

Agent Identity, which gives each agent a unique identity for secure communication, would also help. Right now there's no enforcement preventing one agent from editing another agent's files. They don't, but there's nothing stopping them either. Agent Identity would make inter-agent communication both structured and secure.

## The Irony That Sums It All Up

Blog post #89 out of 235: "The Human Advantage: Why AI-Generated Content is Failing Local Businesses."

An AI agent that writes 9 blog posts per session wrote an article about why AI content doesn't work. No eval caught this. No observability tool flagged it. No governance policy prevented it.

That's the gap between where autonomous agents are today and where the NEXT '26 announcements are pointing. Agent observability, integrated evals, ADK skills, A2A, MCP everywhere: these are all pieces of the solution. None of them existed in a usable form when I started this race 4 days ago. If I were starting today, the Gemini agent would look very different.

## What I'd Rebuild With NEXT '26 Tools

If I set up the Gemini agent from scratch using what was announced this week:

1. ADK instead of raw Gemini CLIfor structured skills, task prioritization, and deployment verification
2. MCP servers for Vercel, Stripe, and Supabaseso the agent can access services directly without human provisioning
3. Integrated evals after each sessionto catch behavioral drift (wrong file, blog addiction) within 1 session instead of 27
4. A2A for help requestsso agents communicate through structured protocols instead of file-based messaging
5. Agent observability dashboardfor a real-time view of what each agent is doing, what it's blocked on, and whether it's following the expected workflow

The race runs for 12 weeks. Gemini has 11 weeks left. Some of these tools are available now. I'm going to try integrating ADK and MCP servers into the orchestrator over the coming weeks and see if Gemini's behavior improves.

The data will be on thelive dashboard. All 7 repos are public on GitHub. If you want to watch an AI agent struggle with the exact problems that NEXT '26 is trying to solve, now you know where to look.

The $100 AI Startup Race is an ongoing experiment with 7 AI agents, $100 each, and 12 weeks to build real startups.Live dashboard·Daily digest·Help request tracker

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (11 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse