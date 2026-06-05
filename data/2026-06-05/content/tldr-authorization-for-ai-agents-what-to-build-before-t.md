---
title: 'Authorization for AI Agents: What to Build Before the EU AI Act Deadline | Cerbos'
url: https://cerbos.dev/blog/authorization-for-ai-agents-what-to-build-before-eu-ai-act-deadline
site_name: tldr
content_file: tldr-authorization-for-ai-agents-what-to-build-before-t
fetched_at: '2026-06-05T12:04:01.152314'
original_url: https://cerbos.dev/blog/authorization-for-ai-agents-what-to-build-before-eu-ai-act-deadline
date: '2026-06-05'
description: What runtime policy at the orchestration layer means, why the agent-to-tool layer is the missing category in agentic AI governance, and which EU AI Act articles actually apply to infrastructure vendors. Practical steps for CTOs and security leads on inventorying agents, sponsoring identities, and externalizing authorization.
tags:
- tldr
---

Guide

# Authorization for AI agents: What to build before the EU AI Act deadline

A
Alex Olivier
June 01, 2026
7
 min read

There's a line from Jonathan Care at KuppingerCole that's been bouncing around in my head since I heard it.

Frameworks govern what models say. Almost nothing governs what agents do.

That's the gap. The teams I've been talking to keep landing on it from different angles, which is usually a sign a category is forming. Some show up because their CTO wants agents in production and security won't sign off. Some show up because the EU AI Act is making someone in legal nervous. Same gap underneath.

Here's how I'd carve it up.

## Three gaps, only one of them named

There are three layers, each with an emerging acronym attached. The acronyms matter less than the shape underneath.

The first is identity. Every agent needs its own identity, per instance, not per class. Short-lived credentials scoped to a single tool call. Lifecycle tied to a named human sponsor. Most enterprises today are issuing one long-lived API key per "the agent" and treating every spawned instance as the same actor. That stops working the moment one agent spawns another. (We've written about this undernon-human identityand thesponsor-tied lifecyclepattern.)

The second is audit. Once an agent delegates to a sub-agent, every existing audit trail breaks. Who consented. What was the original purpose. Did the consent survive the hop. Today's logs answer none of that. They tell you a service account did a thing. They don't tell you which human authorized it, through which chain, for what purpose, on what data. The chain of custody is the bit that's missing, and it's abigger dealthan people are giving it credit for.

The third is the one with no mature category yet. Care calls it orchestration. The agent-to-agent and agent-to-tool layer. Tool gating outside the agent. Inter-agent trust enforcement. Fail-closed runtime when the policy plane is unreachable. Today this layer is just whatever the agent framework chose to expose. Often the agent itself decides what tools it can call, which is the security model of asking a child whether they're allowed dessert.

The first two are problems the IAM industry knows how to think about, even if the implementations aren't there yet. The third is the one nobody has been naming as its own category. I think naming it is the moment it becomes real, and the runtime layer for agent traffic is where most of the architectural work is about to happen.

## What "runtime policy at the orchestration layer" actually means

This is the layer I work in, so I'll be specific.

Every agent-to-tool call is a decision. Should this agent, acting on behalf of this human, in this context, be allowed to invoke this tool with these arguments. The agent shouldn't be the thing making that decision. A separate policy engine should, sitting outside the agent's reasoning loop, evaluating the call before it goes through.

That's a runtime policy engine for agent-to-tool calls. It's the sameexternalized authorizationpattern I've been writing about for years, just with the agent slotted in as a new principal type and the tool slotted in as a new resource type. Decoupled. Externalised. Fail-closed if the engine is unreachable. SamePEP/PDP shape, agent-shaped surface.

The reason this matters for governance is that without it, every other control sits inside the agent. Prompt-level guardrails. Framework-level allowlists. System prompts saying "do not call the refund tool." All of that lives in the same probabilistic system you're trying to constrain. Controls on the inmate, written by the inmate.

Take the policy out of the agent and you get something a security team can reason about. Same engine across all your agents. Same audit log. Same change management. Same rollback story. The agent loses the privilege of deciding what it can do, which is exactly what you want.

## The August deadline, and why it's the smaller story

The reason this is suddenly urgent is theEU AI Act.Article 9covers risk management.Article 10covers data governance.Article 12covers automatic record-keeping over the system's lifetime.Article 13covers transparency to deployers. Together they form the operational core of what a high-risk AI system has to demonstrate.

These obligations sit on the AI system provider, not on Cerbos and not on any other infrastructure vendor in the agent stack. I want to be careful about that, because the "AI compliance" marketing pile is already getting deep. We do not satisfy Article 9 for you. We do not make you AI-Act-compliant. Anyone telling you that is selling you a story.

What Cerbos does help with is the part that's almost impossible to demonstrate without working runtime controls in our layer. A risk management process that doesn't enforce decisions at the agent-to-tool boundary is a document. Data governance that doesn't filter what an agent can read isn't governance. Automatic logging that misses the authorization decisions taken at runtime, and the policy that produced them, isn't a chain of custody.Transparencyto deployers that omits the same isn't transparency.

Originally August 2026 was the activation date for the high-risk obligations under Annex III. The Commission's Digital Omnibus proposal in November 2025 pushed for a deferral to December 2027, and Council and Parliament reached provisional agreement on that in early May. So the date may slip. The architecture obligation doesn't.

The runtime layer where those obligations have to be enforced still doesn't exist in most stacks. The deadline gives it urgency. The category being named gives it shape.

## Why this is converging now

Vendors, analysts, and end users are landing on the same architectural shape from different starting points.

Identity, scoped per agent, with a sponsor-tied lifecycle. Audit chains that survive delegation. A runtime policy plane that gates tool calls outside the agent. Care's eight-question vendor checklist sits on top of these three areas. Martin Kuppinger's tectonic-shifts framework lands on the same. The CoSAI agentic IAM reference covers the same ground.AuthZEN, which I co-chair at the OpenID Foundation, is wiring up the protocol layer for the policy-decision part.

When that many independent threads land on the same architecture, the category has been named. The implementations now have to catch up.

## What security leads should do this quarter

A few practical things to do now, in roughly the order I'd do them.

Inventory.Most organisations are in denial about how many agents they already have. Three teams already do, while leadership says we don't. Find them. Treat shadow AI like shadow IT, but moving faster.

Sponsor every agent.Each agent should have a named human owner whose lifecycle status the agent's existence depends on. If Sally leaves, Sally's agents stop. That's a governance change as much as a technical one.

Move policy out of the agent.Pick a runtime policy engine that can evaluate agent-to-tool calls externally. Thereasons to externalize authorizationfor your normal application traffic apply to agent traffic too, with the principal type swapped.

Wire the audit chain.Every agent action should carry the human sponsor, the original purpose, and the policy decision that authorized it, all the way down to the leaf tool call. Without that you can't answer the Article 86 explainability question even if the deadline moves.

Test fail-closed behaviour.If your policy engine is unreachable, what happens. If the answer is "the agent does it anyway," you have a runtime that fails open. That's the worst class of bug in this layer.

## Where this goes next

The next twelve months are going to be loud. Every infrastructure vendor will start claiming a runtime story. Some will be re-skinning existing PAM or API gateway products. A few will be genuinely new. The signal to watch is whether the policy is decoupled from the agent. If the policy still lives inside the agent, you're looking at something else.

I'd rather we got that architecture right than that anyone, including us, got to claim AI Act compliance on a slide. The deadline is a forcing function. The actual work is the runtime.

Try Cerbosto see what a runtime policy engine for agent-to-tool calls looks like in practice, orbook a callif you want to walk through what runtime controls you can realistically put in place before the deadline.

Go deeper:

* Policy-based guardrails for AI agentsto explore how your organization can secure agentic workflows, RAG pipelines, and MCP servers with runtime authorizationl and full decision logging.
* Zero Trust for AI: Securing MCP servers(eBook) for a practical walkthrough of putting policy between agents and tools.
* Fine-grained authorization for non-human identities(Webinar) for how the same patterns extend across service accounts and agents.

## FAQ

Tagged in

Guide
Free policy workshop

### Get your first Cerbos policy written by our team.

Book a session to talk through your requirements and walk away with a working policy.

Book a session

## Recommended content

### Mapping business requirements to authorization policy

### eBook: Zero Trust for AI, securing MCP servers

### Experiment, learn, and prototype with Cerbos Playground

### eBook: How to adopt externalized authorization

### Framework for evaluating authorization providers and solutions

### Staying compliant – What you need to know

## Subscribe to our newsletter

Join thousands of developers | Features and updates |1x per month| No spam, just goodies.