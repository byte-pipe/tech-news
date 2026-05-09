---
title: 'Beyond the hype: The enterprise AI architecture we actually need | CIO'
url: https://www.cio.com/article/4166033/beyond-the-hype-the-enterprise-ai-architecture-we-actually-need.html
site_name: tldr
content_file: tldr-beyond-the-hype-the-enterprise-ai-architecture-we
fetched_at: '2026-05-10T07:45:45.984854'
original_url: https://www.cio.com/article/4166033/beyond-the-hype-the-enterprise-ai-architecture-we-actually-need.html
date: '2026-05-10'
description: The real future of enterprise AI is a structured architecture of private models and agent orchestration that works for teams without a complex training program.
tags:
- tldr
---

by									
Sumantra Naik

Contributor

# Beyond the hype: The enterprise AI architecture we actually need

Opinion

May 4, 2026
10 mins
 

## The real future of enterprise AI is a structured architecture of private models and agent orchestration that works for teams without a complex training program.

 

							Credit: 															Shutterstock													

My last few years working as a chief digital officer have been, in large part, a sustained exercise in separating what enterprise AI can actually do from what we as a world insist it is about to do. That distinction is not academic. It is the difference between a transformation program that delivers and one that produces a glossy internal report and a quietly shelved proof of concept.

Enterprise experimentation with generative AI has accelerated sharply over the past two years. TheStanford AI Indexreports that more than half of organizations globally are now actively exploring or piloting AI-driven workflows — a signal that the conversation has moved from curiosity to operational pressure for many CIOs.

What follows is not a vendor blueprint or prediction. It is a working architectural sketch shaped by real enterprise constraints — the kind that has to survive contact with a real organization’s data governance function, its compliance team and its late-night incident queue.

What I think the mature enterprise AI stack will look like is considerably more federated, more layered and more interesting than most current commentary suggests.

The enterprise AI of the near future will not be a single platform that does everything. It will most likely be a federation — sovereign agents at the base, curated data in the middle and orchestrated intelligence at the top.

## A stack built in layers

The starting point is accepting that the major systems of record are not going anywhere.

### Native AI

Enterprise platforms like SAP, Salesforce, Workday and ServiceNow hold the most governed and contextually rich data in any large organization, and they are increasingly developing their own native AI capabilities embedded directly within their platforms.

SAP’s recently introducedJoule AI copilot, for example, signals a direction rather than a finished product: Platform-native AI that understands the semantics of the data it sits on and can answer questions that only someone with full schema access and transactional history could answer — without that data ever leaving the platform boundary.

These systems already understand the enterprise in ways no external AI system easily can.

### Sovereign private AI

Alongside the native AI sits a different challenge: The long tail of bespoke platforms, industry-specific tools and internal knowledge repositories that no major vendor may ever be able to natively address.

In my experience, sovereign hosted private AI is the most credible answer here — open-source models such as Llama or Mistral, self-hosted within the organization’s own infrastructure and fine-tuned on internal documents and processes. This creates an AI that knows what the organization actually knows, can be interrogated about its provenance and can be shown to a regulator without a conversation about third-party data processing agreements.

For many regulated industries, this sovereignty over data and model behavior will be a defining architectural principle rather than a technical preference.

### The data lake

Between the base systems and the intelligence layer above them sits the data lake — modern data platforms such as Microsoft Fabric, Databricks, Snowflake or their equivalents — fed by governed data pipelines from those base systems. It is worth being precise about what this layer is — and what it is not. It is not a data swamp. It is a curated, semantically enriched, access-controlled repository that reflects the enterprise’s data as a coherent whole across ERP, CRM, HR and others.

The quality of everything above it depends entirely on what flows into it.

This is unglamorous work. It is also the work that most AI transformation programs underinvest in, and the principal reason most of them underdeliver.

### AI-powered analytics

The analytics layer — powered by likes of  Power BI, Tableau and their successors — sits on top of this data lake, and this is where the most visible change is already underway. The next generation of these platforms will retain the visualization capabilities that business users depend on but will layer a prompt interface and an AI orchestration engine above the data.

A finance analyst asking why gross margin compressed in a particular quarter will trigger not just a query against the data lake, but a federated call — via MCP-based agent-to-agent protocols — to the ERP’s native AI, the CRM’s revenue intelligence and the procurement system’s spend analyser, each responding within their own security perimeter, with results synthesised at the analytics layer. Mostly read and query – deliberately passive.

### The orchestration

The agentic orchestration layer is where AI moves from observation to action, and where governance cannot be an afterthought. This architecture places human oversight at three levels:

* Human-on-the-loopfor autonomous but fully logged agent actions
* Human-in-the-loopfor high-value or irreversible decisions requiring explicit approval
* Human-over-the-loopfor policy-level definitions of what agents may and may not do

Every inter-agent call is traceable, every action timestamped and auditable.

The EU AI Actand sector-specific regulators in financial services and healthcare will make this level of observability non-negotiable within the next couple of years. I have found it considerably easier to build in from the start than to retrofit under regulatory pressure.

Together, these layers form the internal architecture of the enterprise AI stack — systems of record at the base, data consolidation in the middle, analytics above and agent orchestration governing action.

## The missing pieces

The five-layer model above is, in one sense, a description of mostly internal infrastructure. But there are two additional structural elements I keep returning to — conspicuously absent from most current enterprise AI discourse.

### The marketplace

The first is a public marketplace of AI agents underpinned by a blockchain trust layer. When an organization wants to deploy a specialist external agent — one trained to validate material master pricing against live market indices, cross-reference technical specifications against supplier catalogues or propagate regulatory amendments to internal master data — the current model requires trusting the vendor’s claims about what the agent does.

A blockchain-based identity and audit layer changes that. The agent’s provenance, version history and audit trail across prior deployments live on a distributed ledger: Immutable and inspectable. Smart contracts define precisely which systems it may query, what data it may read or write, and under what conditions it must escalate to a human.

This is the agentic equivalent of what open APIs did for data exchange, but with governance built into the protocol rather than bolted on afterwards. Projects exploring this direction — includingFetch.ai’s autonomous agent networkand emerging work around the W3C Verifiable Credentials applied to AI systems — are early signals of where enterprise compliance functions may eventually arrive.

An agent without a verifiable identity is a vendor promise. An agent on a trust ledger is an auditable fact.

### The employee intelligence layer

The second missing piece is what I think of as the employee intelligence layer — the interface through which all of this infrastructure actually reaches the person who joined the organization to do a job, not to understand data topology.

What this needs to be is a single workspace that blends the channel-based collaboration model like those offered by platforms such as Slack with the structured project logic available in the likes of Notion, but with AI built into its core rather than added as a feature. A supply chain coordinator should be able to ask, in plain language, for the status of all open purchase orders for a given vendor and receive an answer synthesised from the ERP’s native AI — without navigating a single SAP transaction code.

An HR business partner should be able to retrieve aggregated headcount and attrition data from an enterprise HRMS such as SuccessFactors, annotated with context from their own team’s channel history, without opening a separate analytics tool.

Progress and accountability belong in the same environment where work actually happens — not in a separate project management application that everyone updates for the quarterly review and ignores the rest of the time. The AI in this layer notices when a commitment is overdue, surfaces the relevant context and suggests an appropriate next action rather than simply turning a status indicator red.

Embedded within each person’s workspace, configured to their role and responsibilities, are the analytics dashboards that actually matter to their decisions — query able in natural language when the chart does not answer the question they have.

Get the employee intelligence layer right and the individual has genuine access to the collective intelligence of the organization. Get it wrong and the stack above becomes expensive infrastructure that the people it was built for have quietly routed around.

## Implications for technology leaders

I am aware that describing a multi-layer federated AI architecture is considerably easier than implementing one. A few things I have learned in practice that seem worth naming directly. The data governance work is not a precondition of the AI work — it is the AI work. The sophistication of any intelligence layer is bounded entirely by the quality, structure and semantic richness of what flows into it.

Organizations that treat the data lake as an IT project and AI as the real transformation misunderstand the sequence. They are the same project, and the data half is harder. The governance of agentic systems requires a different mental model from the governance of conventional software. When a traditional application does something unexpected, there is usually a code path to trace. When an AI agent takes an unexpected action in a multi-agent system, the failure mode is emergent and the audit trail may be distributed across several systems.

The observability infrastructure — the kind used to monitor complex distributed systems, applied to agent networks — is not optional instrumentation. It is the operating licence. I have come to treat it as a first-class architectural concern rather than something to add once the system is stable, because in my experience the system is never stable in the way that phrase implies.

And finally: The enterprise does not need to be rebuilt around AI. It needs to have AI built into it — carefully, layer by layer, with someone accountable at every level.

The platforms that will win in this environment are not necessarily those with the most impressive pilots. They are the ones that play well with others, expose clean interfaces for inter-agent communication, maintain rigorous audit trails and allow the enterprise to remain sovereign over its own intelligence.

The AI future of the enterprise is federated, governed and — when it works properly — invisible. Which is, when you think about it, precisely what good infrastructure has always been.

This article is published as part of the Foundry Expert Contributor Network.Want to join?

Artificial Intelligence
Enterprise Architecture
IT Leadership
 

 

				SUBSCRIBE TO OUR NEWSLETTER			

### From our editors straight to your inbox

				Get started by entering your email address below.			

 

Please enter a valid email address

Subscribe

 

														by 															

																Sumantra Naik															

Contributor

1. Follow Sumantra Naik on LinkedIn

Sumantra Naikis a chief digital officer and futurist with over 25 years of global experience leading large-scale technology and organizational transformation. He has driven end-to-end digitization across multiple industries, integrating infrastructure, operations and logistics into unified digital ecosystems. He also co-founded a venture developing institutional Web3 solutions positioned at the convergence of innovation, sustainability and next-generation digital finance.Sumantra's work and writing explore how decentralization, democratization and convergence — anchored in heart-centered leadership — can guide the evolving arc of technology. He holds an MBA from the Indian Institute of Management Ahmedabad and completed an international exchange at Columbia Business School, New York, where he deepened his perspective on leadership and change in a global context.

## More from this author

* opinion### The 3-body problem of digital transformation — Part 3: The talentMar 17, 20269 mins
* opinion### The 3-body problem of digital transformation — Part 2: The transformation partnersJan 7, 202610 mins
* opinion### The 3-body problem of digital transformation — Part 1: The transforming organizationNov 11, 20259 mins
 

## Show me more

Popular
Articles
Podcasts
Videos

brandpost
 
Sponsored by Reltio
 

### Retail AI has a data problem: Here’s how to fix it

 
By Kevin Keenan, VP Communications, Reltio
May 8, 2026
6 mins

Artificial Intelligence

brandpost
 
Sponsored by CrowdStrike
 

### 5 steps for frontier AI readiness

 
By CrowdStrike
May 8, 2026
5 mins

Artificial Intelligence

feature
 
 

### How to create an effective business continuity plan

 
By Mary K. Pratt
May 8, 2026
13 mins

Business Continuity
Disaster Recovery

podcast
 
 

### CIO Leadership Live ASEAN with Sandeep Shahi, VP IT FEDEX APAC

 
6 May 2026
42 mins

Data Integration
Digital Transformation
Transportation and Logistics Industry

podcast
 
 

### Reinventing Knowledge Management for the AI Era

 
Apr 29, 2026
23 mins

Business Intelligence

podcast
 
 

### From Blueprint to Bytecode - SP Setia's Alex Chi on Building Malaysia's Most Ambitious Property Tech Agenda

 
By Estelle Quek
27 Apr 2026
28 mins

Business IT Alignment
CIO
Chief Digital Officer

video
 
 

### Splunk tackles AI agent blind spots with new observability tools

 
May 6, 2026
16 mins

Artificial Intelligence
IT Operations
Network Monitoring

video
 
 

### CIO Leadership Live ASEAN with Sandeep Shahi, VP IT FEDEX APAC

 
6 May 2026
41 mins

Data Integration
Digital Transformation
Transportation and Logistics Industry

video
 
 

### Skillsoft helps close skills gaps with AI-powered learning platform

 
Apr 29, 2026
22 mins

Generative AI
IT Skills and Training
IT Training