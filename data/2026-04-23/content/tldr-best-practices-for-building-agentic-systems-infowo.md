---
title: Best practices for building agentic systems | InfoWorld
url: https://www.infoworld.com/article/4154570/best-practices-for-building-agentic-systems.html
site_name: tldr
content_file: tldr-best-practices-for-building-agentic-systems-infowo
fetched_at: '2026-04-23T11:59:24.898586'
original_url: https://www.infoworld.com/article/4154570/best-practices-for-building-agentic-systems.html
date: '2026-04-23'
description: Which technologies, designs, standards, development approaches, and security practices are gaining momentum in multi-agent enterprise systems? We asked the experts.
tags:
- tldr
---

by									
Bill Doerrfeld

Contributing Writer

# Best practices for building agentic systems

feature

Apr 20, 2026
14 mins
 

## Which technologies, designs, standards, development approaches, and security practices are gaining momentum in multi-agent enterprise systems? We asked the experts.

 

							Credit: 															Mike Krononov / Unsplash													

Agentic AI has emerged as the software industry’s latestshiny thing. Beyond smarter chatbots,AI agentsoperate with increasing autonomy, making them poised to drive efficiency gains across enterprises.

“Agentic refers to AI systems that can take actions on behalf of users, not just generate text or answer questions,” saysAndrew McNamara, director of applied machine learning atShopify. Agentic systems run continuously until a task is complete, he adds, citing Shopify’sSidekick, a proactive agent for merchants.

Development of agentic AI nowspans many business domains. According toAnthropic, a provider oflarge language models(LLMs), AI agents are most commonly deployed in software engineering, accounting for roughly half of use cases, followed by back-office automation, marketing, sales, finance, and data analysis.

“A concrete example is in IT incident resolution,” saysHeath Ramsey, group VP of AI platform outbound product management atServiceNow. In this context, AI agents surface contextual data across systems, check prior resolutions and policies, issue fixes, update records, and loop in team members, he says.

But agent-centered development demands a new form of systems thinking to avoid pitfalls such as indeterminism andtoken bloat. There are also pressingLLM-derived security gaps, such as a model’s willingness to lie or fabricate information to achieve a goal, a condition researchers callagentic misalignment.

For teams building agents that integrate with other systems and reason through various options to execute multi-step workflows, the proper upfront planning is table stakes. For these reasons and more, agentic architecture design requires a new playbook.

“Building agentic systems requires a fundamentally new architecture, one designed for autonomy, not just automation,” says Anurag Gurtu, CEO ofAIRRIVED, an agentic AI platform provider. “Agents need a runtime, a brain, hands, memory, and guardrails.”

Although agentic AI shows promise,ROI from AIis a moving target. Less than half of organizations report a measurable impact from agentic AI experiments, according toAlteryx, with less than a third trusting AI for accurate decision-making.

So, what are the ingredients behind successful enterprise-grade agentic systems? Rather than focusing on how to build within a single vendor platform, let’s explore the common traits across agentic systems to surface practical guidance and lessons learned for developers and architects.

## Architectural components of an agentic system

Agentic systems are composed of a handful of building blocks that make it all possible. Together, they form an interconnected web of software architecture, with different components serving different purposes. “Building an AI agent is like constructing a nervous system,” saysAri Weil, cloud evangelist atAkamai.

This system spans layers for reasoning, memory, context-gathering, coordination, validation, and human-in-the-loop guardrails. “Agentic systems rely on a combination of AI, workflow automation, and enterprise controls working together,” adds ServiceNow’s Ramsey.

### Reasoning model

First off, if you break down agentic systems into their foundational components, you have to begin with the underlying model.

“A reasoning model sits at the core,” saysFrank Kilcommins, head of enterprise architecture atJentic, builders of an integration layer for AI. This reasoning engine performs the planning based on the user’s prompt, combined with the context-at-hand and available capabilities.

Some reasoning models are better suited than others. “We look for models that feel agentic,” says Shopify’s McNamara. “They have the right amount of tool calls, and have strong instruction following that’s easy to prompt and steer.”

### Context and data

Next, an agent needs context. This may take the form of internal company data,institutional knowledgeand policies, system prompts,external data, memory of past chats, andagentic metadata, i.e., the user prompts, reasoning steps, and interactions with tools and data sources that allow you to observe and debug the agent’s behavior.

According toEdgar Kussberg, product director for AI, agents, IDE, and devtools atSonar, sources for data can include databases and APIs,retrieval-augmented generation(RAG) systems andvector databases, file systems and document stores, internal dashboards, or external systems like Google Drive.

Organizations are actively buildingagentic knowledge basesto organize such data and streamline the retrieval process. Simultaneously, patterns are emerging behind semantic retrieval processes that power agentic context management systems.

“For memory, most teams combine a vector store likepgvectorwith something structured like a data catalog or knowledge graph,” saysAnusha Kovi, a business intelligence engineer at Amazon.

### Tools and discovery

But for agents to be actionable, they need more than just static context — they need read and write access to databases, tools, andAPIs.

“Some of the most important work being done to make agents more powerful is happening with the ways we connect AI and existing systems,” saysJackie Brosamer, head of data and AI atBlock, the financial services company behind Square and Cash App.

To enable access to such capabilities, the industry has really coalesced around theModel Context Protocol(MCP) as a universal connector between agents and systems.MCP registriesare emerging to unify and catalog MCP capabilities for agents at scale.

There are numerous public case studies of MCP use within agentic architectures, including Block’s open-sourcegoose agentfor LLM-powered software development and Workato’suse of MCPfor Claude-powered enterprise workflows.

### Defined workflows

Another useful component is having clearly documented workflows for common procedures. These include multi-step actions that are interlinked between MCP servers or direct API calls.

“What matters is that these agents are coordinated through defined workflows,” says ServiceNow’s Ramsey, “so autonomy scales in a predictable and governed way rather than becoming chaotic.”

Jentic’s Kilcommins describes how this can be achieved using “clear, machine-readable capability definitions,” referencing theArazzo specification, an industry standard from theOpenAPI Initiative, as a method to document such behaviors.

### Multi-agent orchestration

On that note, agents must be equipped to integrate with each other and fit well into a continuous feedback loop.

Multi-agent systemstypically become necessary at scale, says AIRRIVED’s Gurtu. “Instead of one generalist agent, you often have teams of specialized agents such as reasoning agents, retrieval agents, action agents, and validation agents.”

This reality necessitates connective tissue. “At the core, you need an orchestration layer for the plan-do-evaluate loop,” says Amazon’s Kovi.

Common components for orchestration, adds Kovi, includeLangGraph, a low-level orchestration framework,CrewAI, a Python framework for multi-agent orchestration, andBedrock Agents, for helping agents automate multi-step tasks.

Open standards and protocols, like theA2A protocol for agent-to-agent communications, will also be important to enable AI agents to collaborate effectively.

### Security and authorization

Given LLMs’ propensity to hallucinate and deviate from expectations, security is perhaps the most important element of building safe agentic systems.

“You’re no longer securing software that suggests, you’re securing software that acts,” says Gurtu. “Once agents can change access, trigger workflows, or remediate incidents, every decision becomes a potential control failure if it isn’t governed.”

According to Kilkommins, the potential blast radius for agentic actions is huge, especially for uncontrolled, chained executions. He recommends having clearly defined permissions to avoid privilege escalation and sensitive data exposure.

In agentic systems, nuanced security methods are necessary. “An agent decides at run time what to query and what tools to call, so you can’t scope permissions the traditional way,” adds Kovi. Experts say thatjust-in-time authorizationwill be crucial to future-proof the non-human internet.

Kovi adds that safety rules, like “don’t query personal information columns,” shouldn’t live in the prompt window. “Guardrails belong in identity and access management policies and configuration, not just prompt instructions.”

### Human checkpoints

Even with advanced authentication and authorization, sensitive actions will require human approvals.

Shopify defaults to “human-in-the-loop by design,” says McNamara. They’ve adopted approval gates to prevent fully autonomous changes to production systems. This allows merchants to review Sidekick’s AI-generated content before it goes live.

Others take a similar stance, particularly forfinancial transactions. “Our general rule is that anything touching production systems needs human checkpoints,” says Block’s Brosamer, referring to how user confirmation is a key element of Moneybot, the agent inside Cash App.

### Evaluation capabilities

Building agentic systems also requires a good deal of upfront testing to evaluate whether outcomes match the intended results.

For instance, Shopify performs rigorous pre-deployment evaluation on agentic outputs using both human testing and user simulation with specialized LLM-based judges. “Once your judge reliably matches human evaluators, you can trust it at scale,” says McNamara.

Others agree that evaluations are critical for enterprise-grade agentic systems. “Treat agents like regulated systems,” says Gurtu. “Sandbox changes, and test agents in simulation.”

### Behavioral observability

Lastly, another core layer is observability. For agentic systems, this must go beyond traditional monitoring or failure detection to capture advanced signals, such as why agents failed, or why they picked certain actions over others.

“Observability must be built in from day one,” says Sonar’s Kussberg. “You need transparency into every step of execution: prompts, tool calls, intermediate decisions, and final outputs.”

With more observable agent behaviors, you can improve the system continuously over time. As Kussberg says, “transparency fuels improvement.”

## Context optimization strategies

Nearly all experts agree: giving AI agents minimal, relevant data is far better than data overload. This is critical to avoid maxing out context windows and degrading output quality.

“Thoughtful data curation matters far more than data volume,” says Brosamer. “The quality of an agent’s output is directly tied to the quality of its context.”

At Block, engineers maintain clear README files, apply consistent documentation standards and well-structured project hierarchies, and adhere to other semantic conventions that help agents surface relevant information.

“Agentic systems don’t need more data, they need the right data at the right time,” adds Sonar’s Kussberg. “Effective systems give agents versatile discovery tools and allow them to run retrieval loops until they determine they have sufficient context.”

The prevailing philosophy is to adopt progressive disclosure of information. Shopify takes this to heart, using modular instruction delivery. “Just-in-time context delivery is key,” says McNamara. “Rather than overloading the system prompt, we return relevant context alongside tool data when it’s needed.”

Others point out that context should include semantic nuances too, says Kovi. “If an agent doesn’t know ‘active users’ means something different in product versus marketing, it’ll give confident wrong answers,” she says. “That’s hard to catch.”

## Architectural best practices

There are plenty of additional recommendations regarding agentic systems development. First is the realization that not everything needs to be agentified.

Pairing LLMs and MCP integrations is great for novel situations requiring highly scalable, situationally-aware reasoning and responsiveness. ButMCP can be overkillfor repetitive, deterministic programmed automation, especially when context is static and security is strict.

As such, Kilkommins recommends determining what behavior is adaptive versus deterministic, and codifying the latter, as this will allow agents to initiate intentionally-defined programmed behaviors, bringing more stability.

Determining the prime areas for agentic processes also comes down to finding reusable use cases. “Organizations that have successfully deployed agentic AI most often start by identifying a high-friction process,” says Ramsey. This could include employee service requests, new-hire onboarding, or customer incident response, he says.

Gurtu adds that agents perform best when they are given concrete business goals. “Start with decisions, not demos,” he says. “What doesn’t work is treating agents like stateless chatbots or replacing humans overnight,” says Gurtu.

Others believe that narrowing an agent’s autonomy yields better results. “Agents work best as specialists, not generalists,” Kussberg says.

For instance, Shopify sets clear boundaries when scaling tools. “Somewhere between 20 and 50 tools the boundaries start to blur,” says McNamara. While some propose separating role boundaries with distinct task-specific agents, Shopify has opted for a sub-agent architecture with low-level tools.

“Our recommendation is actually to avoid multi-agent architectures early,” McNamara says. We are now getting into sub-agents with the right approach, and one key principle is to build very low-level tools and teach the system to translate natural language to that low-level language, rather than building out tools scenario by scenario.”

Experts share other wisdom for designing and developing agentic systems:

* Use open infrastructure:Open agents and vendor-agnostic frameworks allow you to use the best fit-for-purpose models.
* Think API-first:Good API design and clear, machine-readable definitions betterprepare an organization for AI agents.
* Keep data in sync: Keeping shared data in sync is another challenge. Event-driven architectures can keep data fresh.
* Balance access with control: Keeping agentic systems secure will require offensive security exercises, comprehensive audit logs, and defensive data validation.
* Continually improve: To avoid agent drift, agentic systems development will inevitably require ongoing maintenance as the industry and AI technology evolve.

## The future for agentic systems

Agentic AI development has moved forward at a blistering pace. Now, we’re at the point where agentic system patterns are beginning to solidify.

Looking to the future, experts anticipate a turn toward more multi-agent systems development, guiding the need for more complex orchestration patterns and reliance upon open standards. Some forecast a substantial overhaul to knowledge work at large.

“I expect that in 2026, we will see experimentation with frameworks to structure ‘factories’ of agents to coordinate producing complex knowledge work, starting with coding,” says Block’s Brosamer. The most challenging aspect will be optimizing existing information flows for agentic use cases, she adds.

One aspect of that future could be more emphasis onalternative cloudsandedge-based inferenceto move certain workloads out of centralized cloud architecture to reduce latency.

“The future of competitive AI demands proximity, not just processing power,” says Akamai’s Weil. “Agents need to act in the real world, interacting with users, devices, and data as events unfold.”

All in all, building agentic systems is a highly complex endeavor, and the practices are still maturing. It will take a combination of novel technologies, microservices-esque design thinking, and security guardrails to take these projects to fruition at scale in a meaningful and sustainable way — all while still granting agents meaningful autonomy.

The future looks agentic. But the smart system design underpinning agentic systems will set apart successful outcomes from failed pilots.

Generative AI
Artificial Intelligence
Software Development
Development Approaches
 

														by 															

																Bill Doerrfeld															

Contributing Writer

1. Follow Bill Doerrfeld on LinkedIn

Bill is a tech journalist specializing in state-of-the-art technologies in the enterprise cloud software space. He is alsoEditor in Chief for Nordic APIs, a knowledge center for API practitioners, and contributes toDevOps.com,Cloud Native Now(formerly Container Journal), and Acceleration Economy.Bill is originally from Seattle, where he attended the University of Washington. He now lives and works in Portland, Maine.

## More from this author

* feature### How to build an enterprise-grade MCP registryMar 30, 202615 mins
* feature### Five MCP servers to rule the cloudFeb 16, 20269 mins
* feature### How should AI agents consume external data?Feb 2, 202612 mins
* feature### Edge AI: The future of AI inference is smarter local computeJan 19, 202610 mins
* feature### 6 incredibly hyped software trends that failed to deliverJan 5, 202613 mins
* feature### 10 MCP servers for devopsDec 8, 202512 mins
* feature### Anatomy of an AI agent knowledge baseNov 24, 202510 mins
* feature### 8 platform engineering anti-patternsOct 20, 20259 mins
 

## Show me more

Popular
Articles
Videos

opinion
 
 

### Is your Node.js project really secure?

 
By Sonu Kapoor
Apr 23, 2026
11 mins

JavaScript
Node.js
TypeScript

news
 
 

### Malicious pgserve, automagik developer tools found in npm registry

 
By Howard Solomon
Apr 22, 2026
7 mins

Cybercrime
Development Tools
Malware

news
 
 

### Microsoft issues out-of-band patch for critical security flaw in update to ASP.NET Core

 
By John E. Dunn
Apr 22, 2026
4 mins

Development Tools
Libraries and Frameworks
Microsoft .NET

video
 
 

### Jujutsu: The rising alternative to Git

 
Apr 21, 2026
5 mins

Python

video
 
 

### How to run Chrome and Edge's built-in AI

 
Apr 14, 2026
6 mins

Python

video
 
 

### Python's new frozendict type

 
Apr 2, 2026
4 mins

Python