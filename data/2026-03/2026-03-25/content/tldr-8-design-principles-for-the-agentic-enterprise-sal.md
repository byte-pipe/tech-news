---
title: 8 Design Principles for the Agentic Enterprise - Salesforce
url: https://www.salesforce.com/news/stories/agentic-enterprise-design-principles/
site_name: tldr
content_file: tldr-8-design-principles-for-the-agentic-enterprise-sal
fetched_at: '2026-03-25T19:21:52.598270'
original_url: https://www.salesforce.com/news/stories/agentic-enterprise-design-principles/
author: Shibani Ahuja
date: '2026-03-25'
published_date: '2026-03-23T13:00:00+00:00'
description: Key Takeaways AI failures aren’t about the model. They’re about the architecture. Trust and governance must be built in from the start, not
tags:
- tldr
---

0%

## Key Takeaways

* AI failures aren’t about the model. They’re about the architecture.
* Trust and governance must be built in from the start, not added later.
* Design for modularity and open standards to avoid vendor lock-in.

WhenAI deployments fail, it might be tempting to blame the models. Or a mischosen use case. Or unwilling humans.

Dig deeper, though, and the real problem becomes apparent: Simply plastering anagenton top of an existing but inadequate architecture won’t work. Not because models are outdated or lacking but because classic architectures aren’t designed for agent workloads.

A successful agentic deployment relies on four architectural layers: the system of engagement, where people and agents work; the system of agency, which is the agents themselves; the system of work, or a company’s business applications; and the system of data, meaning unified enterprise data.

The success of anAgentic Enterprisedepends on how these layers work together. Drawing on years of strategy, innovation, and generative and agentic AI experience, leaders across the Salesforce Product and Architecture teams have distilled their expertise into eight design pillars — a framework for what good implementation looks like and what red flags to watch for.

Open Image Modal

# Image Modal

## 1. Design for modularity.

Picture a Lego kit. The same set of blocks can build an airplane or a dollhouse or a fire truck.

Anagentic AIarchitecture needs similar modular workability. Companies can’t afford to rebuild entire architecture elements from scratch for every new function assigned to an agent. It takes too long and costs too much. It also defeats the very reason for using AI in the first place: If every agent is unique, every agent is ungovernable.

What good looks like:Work off a menu of modular “premade” items. Need a customer offboarding agent six months after developing a customer onboarding agent? No problem. Simply reuse the same data connectors and integrations you’ve already built.

Where things go wrong:If even slight variations on an existing agent require a complete reboot or if every new API call or agent needs a monthlong rejiggering of the existing architecture, something isn’t working.

## 2. Harmonize data with metadata-driven understanding.

A human will know “Acme Corp” in the CRM is the same as “Acme Corporation” in the ERP and “ACME-NA” in the data warehouse.

Agents need more than unified data — they need the metadata to understand what it all means.

What good looks like:Consistently label files with a fixed nomenclature. Agents have access to data and metadata, business glossaries, and ontologies. Equipped with these tools, agents can better connect the dots (and learn over time).

Where things go wrong:An agent fulfills its assigned task (say, increasing sales by offering deep discounts) but still fails (because the company now loses money on every sale). If data isn’t properly interconnected, an agent doesn’t have the context to know that its decisions should also be financially sound.

Agents need guardrails. So bake governance and trust principles into the very DNA of the Agentic Enterprise architecture.

## 3. Enable unified observability.

When an agent does something wrong, everyone needs to know why. Having a clear view of how agents are executing actions (and where) helps fine-tune a system that works exactly as it should and that can easily be fixed when it doesn’t.

Unified observability means real-time visibility into actions (what the agent did), reasoning (why it chose that path), context (what data and definitions it used), governance (how it complies with policies and permissions), and business outcomes (what changed; whether it worked and by how much). Such observability also needs to span IT and business so the impact of one is more clearly visible on the other.

What good looks like:You know which actions are most used, where mistakes are happening, and how those actions are driving business outcomes. This full-scale observability gives you the ability to tune and optimize your agentic workforce.

Where things go wrong:If you don’t have observability, you can’t trace the problem when mistakes happen (and they will).

## 4. Build with trust.

Agents can write to financial systems, send emails on behalf of executives, and approve contracts. They need guardrails. So bake governance and trust principles into the very DNA of the agentic enterprise architecture.

What good looks like:Governance should exist across the entire architecture. It includes distinct and verifiable identities for agents; task-based permissions that expire after specified periods of time, not unfettered access to agents for all time; and steps in the workflows that ensure checks and balances against established policy and risk protocols.

Where things go wrong:If you can’t trust it, you won’t use it.

## 5. Design for strategic human intervention and oversight.

Picture a pass-through at airport security. Physically patting down every passenger or riffling through every carry-on is overkill and delays traffic. On the flip side, it’s unsafe to let every passenger and bag go through unchecked. Instead, all passengers and bags go through X-ray screening and only the suspicious-looking ones get pulled aside for more thorough examination. AI agents need similar strategic human oversight.

Design for the right level of human-in-the-loop engagement at each decision point.

What good looks like:Agents handle routine, low-risk tasks by default and alert humans when the end user asks for something that’s outside its domain or just asks to speak to a human. Agent-human handoffs are smooth and delivered with context, so the human doesn’t have to start the case over.

Where things go wrong:Human intervention is required for every agent decision — or  agents are making completely unsupervised decisions all the time.

## 6. Enable event-driven processing.

The speed of business needs real-time decision-making. Agents need to be always on, alert for triggers that need a response and through any channel — texts, emails, calls, or APIs.

What good looks like:The architecture responds to real-time triggers and multimodal inputs. The agent can take a call from a human asking about a refund or a system sending a systems outage ping.

Where things go wrong:If the architecture doesn’t enable real-time connectivity across any channel, calls go unanswered, messages go unread. Agents working with different sets of information lead to inaccurate conclusions and frustrated customers.

## 7. Ensure infrastructure can scale growing AI workloads.

The challenge with AI workloads is that their computing needs aren’t just intensive; they’re unpredictable. Loads can spike dramatically in seconds, and data retrieval and token usage vary wildly. An Agentic Enterprise architecture needs to be resilient.

What good looks like:AI-ready infrastructure includes compute that scales based on workload needs. Distributed loads reduce the possibility of a single point for catastrophic failure. The architecture needs storage that handles unpredictable patterns of data access and bandwidth to accommodate increased API traffic.

Where things go wrong:Without the necessary compute power, spikes in agent reasoning and workflows cause brittle systems to break, risking system outages.

## 8. Prioritize open ecosystems and standards.

A robust architecture for an Agentic Enterprise needs interoperability. Not only can no one vendor deliver everything for agentic AI, but you also can’t afford to be locked into today’s must-haves when you don’t know what’s coming tomorrow.

It’s why you need to design for an “any data, any LLM, any app” environment, banking on open ecosystems and universal standards so as to not be locked into any one set of protocols.

What good looks like:An open architecture has standard interfaces for models so when a better one comes along, it can easily swap in. It has open protocols (Model Context Protocol, APIs, standard data formats) for integration of the various modules. Portable workflow definitions ensure orchestration doesn’t work for only one platform configuration. Finally, data access patterns need to work across sources so agents aren’t confined to specific databases.

Where things go wrong:You’re ready to scale AI deployments or try a new LLM tailored to your enterprise needs but are locked into vendors whose plans might not accommodate your vision. Switching to a new one will mean you have to rewire over 40 agents.

## Onward and Upward

These principles are your control surfaces. They’re how you scale AI agents without breaking trust. They’re how you turn intelligence into action in a way you can defend to regulators, customers, and your board.

Without them, you don’t have an Agentic Enterprise. You have disconnected experiments and wishful thinking.

With them, you can finally talk about moving forward in a realistic way: phased, bounded, and focused on closing the gap where most companies are stuck.

Read the full report:The Invisible Advantage: Why Your Architecture, Not the Model, Will Define Your Agentic Enterprise

#### Go deeper:

* Dive into the process ofbuilding the world’s first Agentic Enterprise
* Learn more aboutmeasuring value with Agentic Work Units
* Step inside what it’s like towork in an Agentic Enterprise

## Explore related content by topic

* Agentic Enterprise
* Agents
* AI
* Enterprise AI

Shibani Ahuja

SVP, Enterprise IT Strategy

					More by Shibani



	8 min read



	1 min read



	6 min read



	4 min read

Get the latest Salesforce News

Subscribe

Close
