---
title: 'Data Products: The Essential Context for Enterprise AI'
url: https://moderndata101.substack.com/p/data-products-the-essential-context
site_name: tldr
content_file: tldr-data-products-the-essential-context-for-enterprise
fetched_at: '2026-04-26T06:00:32.927344'
original_url: https://moderndata101.substack.com/p/data-products-the-essential-context
author: Animesh Kumar
date: '2026-04-26'
description: Enterprise AI agents failed in production because they lacked business context. The fix is governed, semantically-rich data assets that give AI agents the definitions, lineage, and quality signals they need to return trustworthy answers. Or Data Products.
tags:
- tldr
---

# Data Products: The Essential Context for Enterprise AI

### Most enterprise AI-for-data agents failed in 2025 because they lacked context, and Data Products, built above the engine, are the fix.

Animesh Kumar
, 
Shubhanshu Jain
, and 
Devendra Singh Rathore
Apr 22, 2026
36
2
9
Share

## The Moment

Through 2024 and 2025, “AI agents for your data” was one of the most promoted categories in enterprise software. Every major vendor had a demo. Every board deck had a slide. The pitch was deceptively simple:ask your data a question in English, get an answer. Skip the analyst, skip the dashboard, skip the SQL.

And through 2024 and 2025, most of these agents failed in production.

MIT’sState of AI in Business 2025report flagged the reason in general terms: enterprise AI efforts fail due tobrittle workflows, lack of contextual learning, and misalignment with day-to-day operations. The industry spent much of 2025 assuming this was a model problem. Better reasoning, bigger context windows, smarter fine-tuning. The model side improved dramatically through the year. The problem did not go away.

In January 2026, OpenAI publishedan unusually detailed description of the internal data agentthey had built for their own employees. Two engineers, three months, a production system used daily by roughly 4,000 people across the company. The headline wasn’t the output; it was the architecture.

The agent was built onsix deliberate layers of contextgrounding every query: schema metadata and lineage, historical query patterns, curated expert descriptions, code-derived definitions from pipelines, institutional knowledge pulled from Slack and docs, and persistent memory of past corrections. Separately, the agent could issue live queries to inspect schemas when context was missing or stale.

### OpenAI’s own framing, from that post

#### High-quality answers depend on rich, accurate context. Without context, even strong models can produce wrong results.

Two months later, in March 2026, a16z publisheda thesis piece by Jason Cui and Jennifer Li titled“Your Data Agents Need Context.”The argument was that the market had just spent a year relearning a lesson: data agents are not a model problem, they are a context problem.

And context, the authors argued, needed tobecome a real architectural layerin its own right, not an afterthought, not a semantic layer bolted onto a BI tool, but first-class infrastructure.

Foundation Capital and others converged on similar framings over the same window. So did Palantir, which has been quietly saying a version of this for a decade, through its ontology work. The practitioner community had been writing in the same direction for months before the OpenAI and a16z pieces crystallised it.

Modern Data 101’s “Rise of the Context Architecture”in October 2025 made the argument explicitly: metadata and relationships are the new product; raw data is the raw material.

The consensus, broadly, is new; the underlying observation is not. What changed is that the consensus now has urgency. Agents need context. The organisations that have it will ship AI that works. The organisations that don’t will keep paying what might be called the OpenAI tax: building context infrastructure from scratch, per agent, without reuse.

This document is about what that context layer should look like, why the right abstraction already exists and is called a Data Product, and why most of the current market is addressing the problem from the wrong direction.

## The Industry’s Realisation

For most of the last decade, the dominant idea in enterprise data wascentralisation. Get all the data into one place (a warehouse, a lakehouse), clean it up, and business users would be able to self-serve. Write SQL, pull data, power dashboards. The modern data stack was the architectural expression of this idea. It worked, up to a point. Dashboards got better, analysts got faster, and a large category of companies, from dbt to Snowflake, was built on making this centralisation practical.

The limits of centralisation became visible once AI agents arrived. A human analyst reading a warehouse doesn’t just see the tables.

* They know which table is the “real” one.
* They know thatrevenuemeans net of refunds unless otherwise specified.
* They know the fiscal quarter ends on the 28th, not the 30th.
* They know that the finance team uses one source, the product team another, and which one to trust for a given question.

Most of what makes the warehouse useful to a human analyst isthe analyst’s own accumulated context.

An AI agent walking into the same warehouse has access to the tables but not the context. It doesn’t know which of the five similarly-named tables is canonical.

It doesn’t know that the semantic layer was last updated by someone who left the company, and that three new product lines have been launched since. It doesn’t know thatactive customermeans something different in the growth dashboard than in the finance model. When asked“what was revenue growth last quarter?”the agent can write competent SQL against a plausible-looking table and return wrong numbers confidently.

### This is why a year of AI-for-data agents largely failed to land in production.

The model wasn’t the bottleneck. The model was flying blind through an environment that depended on context the model didn’t have.

The realisation that crystallised across early 2026 is that context itself has to become a durable architectural layer. Not a prompt. Not a wiki. Not tribal knowledge that evaporates when someone leaves the team. A managed, versioned, discoverable layer that can be connected to, queried by, and relied on by anything that needs to reason about the company’s data.

The useful next question is what shape that layer should take. And here the answer has been hiding in plain sight for several years, under a name most enterprise data leaders already know: the Data Product.

## The Shape of the Answer

AData Productis a managed unit of data that is treated like a product rather than as a byproduct of some operational system.

* It has an owner.
* It has a contract describing what it guarantees and what it doesn’t.
* It has a named consumer in mind.
* It has a lifecycle: versioned changes, deprecation windows, sunset.
* It is discoverable in a catalog,
* It is addressable through a stable interface,
* and accompanied by its own semantics, lineage, and quality signals.

None of this is new. The term has been in circulation since at least 2019, most prominently throughZhamak Dehghani’s data mesh writing. What’s new is the context in which the definition now lands. A Data Product was, until recently, a good idea for making warehouses more usable to humans. In the AI era, it becomes the right unit of consumption for agents.

The definition can be restated in a way that makes the AI relevance obvious:

A Data Product iscontext packaged as a first-class asset.

Everything an agent would otherwise have to reconstruct from scratch (the schema, the semantics, the ownership, the freshness, the lineage, the quality, the right way to read it) is part of the product by construction.

This is not a coincidence.

### The six layers of context that OpenAI built by hand for their internal agent correspond, almost one-to-one, to what a well-constructed Data Product already includes.

* Schema metadata and lineage: a Data Product carries its schema and its upstream lineage as part of its specification.
* Historical query patterns: usage telemetry is a natural byproduct of a Data Product served through a governed interface.
* Curated expert descriptions: the Data Product’s owner writes these as part of its contract.
* Code-derived definitions: the transformation logic that produces the productisits definition, and it’s already versioned.
* Institutional knowledge: the product’s semantic layer captures the decisions that tribal knowledge otherwise preserves.
* Memory of past corrections: a governed product that reviews and incorporates feedback accumulates this automatically.

What OpenAI built from scratch, in months, a Data Product provides by construction. The correspondence is near-exact.

### OpenAI built context infrastructure from scratch because they had to. Most enterprises should not have to.

The abstraction already exists, and the industry has already converged on its shape.

## Why This Is the Right Shape for AI

A reasonable question at this point:if Data Products are so obviously the right shape, why didn’t this become the dominant architecture five years ago?

The answer is that the demand hadn’t yet arrived.

A Data Product is more expensive to build than a raw table. Someone has to own it, contract it, version it, keep it fresh.Organisations absorb that cost only when the consumer justifies it.

Human analysts don’t always justify it. An experienced analyst can read a raw warehouse and fill in the missing context from experience. Dashboards can work around missing metadata. A small data team can informally serve as the “context layer” for a whole company. Up to a certain scale, this works, and the overhead of formalising Data Products feels like discipline for discipline’s sake.

AI agents are different in four ways that collectively push the economics.

1. Theyscale to a breadth no analyst team does.A single agent can field questions across every department in an organisation simultaneously. The accumulated informal context of any one person is useless at that breadth; the context has to be external, shared, and machine-readable.
2. Theycannot improvise safely.An analyst who encounters an ambiguous table asks a colleague or flags it. An agent asked the same question has no such instinct; it writes a confident query against whatever is in front of it. The cost of “confidently wrong” is much higher than the cost of “paused to clarify,” and the only way to avoid confidently wrong is to hand the agent context that is already correct.
3. Theyoperate under contracts.A human analyst can tell the difference between a table that “probably works” and one that “definitely works.” An agent has no such discrimination. It needs a machine-readable signal (an SLA, a quality gate, a contract) to know whether to trust what it’s reading. Data Products carry these signals natively.
4. Theybenefit massively from reuse.Every agent in an organisation can consume the same Data Product. Every new agent that arrives can be pointed at the same catalog. The context investment amortises across agents, across use cases, across years. This is the one factor that fully justifies the overhead: a Data Product built for one consumer serves the next hundred without rebuild.

The result is that Data Products become architecturally necessary at roughly the same moment AI agents become organizationally necessary.

### The shape that was merely good discipline for human analysts is structurally required for agents, and the cost calculation has flipped:

#### Not investing in Data Products is now more expensive than investing, because every agent has to carry its own context infrastructure otherwise.

Modern Data 101 made a parallel argument in“AI-Ready Data: A Technical Assessment”: the semantic layer inside a Data Product is the authoritative source of business meaning that persists across systems, and it’s precisely what lets AI move from statistical correlation to business decision.

## What Happens Without It

The concrete failure pattern, stated in the a16z piece, is worth walking through because it happens constantly and reveals exactly what the industry missed.

An agent is asked a question that looks trivial on its surface:“What was revenue growth last quarter?”

The first thing that breaks is thedefinition of revenue.

Revenue is not a column in a table. It is a business definition that depends on billing terms, refund policy, recognition timing, product mix, and a dozen other factors that are specific to the company. Net of refunds? Gross? Recognised or booked? The agent has no way to know.

The second thing that breaks is thedefinition of quarter.

Fiscal calendars vary by company. Some companies close on the last day of the month, some on the last Friday, some on the 28th. The agent’s built-in notion of “Q1” almost certainly doesn’t match.

The third thing that breaks is theidentification of the source.

Three tables in the warehouse have “revenue” in their name. One is the fact table, one is a materialised view, and one is a legacy snapshot that has not been maintained since 2023. A human analyst knows which is which. The agent does not.

The fourth thing that breaks isrecency.

The source the agent picks has not been updated in four days because an upstream pipeline failed overnight, and no one has noticed. The agent has no way to detect this; it reads the freshest row it can find and returns it.

The fifth thing that breaks istrust.

The agent returns a number confidently. A human asks,“Is this right?”and no one can answer quickly, because the chain from question to answer is opaque. The agent has no way to show its work in a form that makes the chain auditable.

At every one of these five failure points, a properly constructed Data Product would have defended the system against these failures:A raw warehouse leaves every question open. A Data Product answers each by construction through its semantic layer, contract, SLA, and quality gates.

The question answers itself. An AI agent is only as reliable as the context it is given. A raw warehouse does not give it context. A Data Product does.

## The Market’s Current Answers

The industry has noticed. What the industry has not fully internalised yet is that theshapeof its answer will determine whether the architecture scales or locks the problem in place.

The most visible answers today come from what a16z calls thedata gravity platforms, the companies that already hold most of the enterprise’s data and compute, and are adding AI-agent functionality on top.

* Databrickshas released Unity Catalog for governance and metadata, Genie for natural-language data exploration, and is building the context surface around its lakehouse.
* Snowflakehas Cortex Analyst for natural-language querying, Polaris for open catalog access, and a parallel effort to serve AI workloads from the warehouse.
* Palantirhas been building Ontology for a decade and a half, arguably the most mature version of this architecture in the market, and is now selling it explicitly as the AI context layer.

These are all credible efforts, led by teams that understand the problem. They are not wrong about what they’re building. The differentiating question is about shape.

### The pattern these platforms share is that their AI functionality iscompute-locked.

A Data Product built in Databricks lives in Databricks, and its AI surface is served by Databricks. A Data Product built in Snowflake lives in Snowflake. A Palantir ontology lives in Palantir Foundry.

This is a natural consequence of their business model: the context layer is an entry point intomore compute consumption on the same platform.

For enterprises that run their data in one place and intend to continue doing so, this is fine. For enterprises that have data across multiple engines (Snowflake for analytics, Postgres for operations, a lakehouse for ML, Databricks for certain workloads), the compute-locked model forces a choice.

* Either consolidate onto one platform (an expensive and often impossible project),
* or accept that your AI agents will have fragmented context, with a different surface in each engine.

The a16z piece frames this explicitly: data gravity platforms are credible but structurally limited by the compute they are tied to. A separate category ofdedicated context-layer companieshas emerged to address the problem from a different direction: context-first, engine-independent.

This is the architectural choice that determines whether a Data Product strategy is portable across the organisation’s actual data landscape, or captive to wherever the largest contract was signed.

## What a Data Operating System Does Differently

AData Operating Systemis built on the thesis that the Data Product, not the engine, is the atomic unit.

In the data gravity model, Data Products are restricted inside the compute platform and are consumed through it. In DataOS, Data Products are above the compute, with the same contract reachable regardless of which engine holds the bytes.

Refer:DataOS, the first Operating System for Data

The practical consequence is that a Data Product in DataOS is not tied to any particular compute platform. It can be built in Snowflake if that’s where the data lives. It can be built in BigQuery, Databricks, or Postgres if that’s where the organisation has standardised.

It can be built in theDataOS Lakehouse(Iceberg on S3, ADLS, or GCS, with Spark and Trino) if the team wants a native, governed substrate. Thesame discipline, thesame contract, thesame consumption surfaceapplies regardless of which engine holds the bytes.

🔖 Related Read

## Introducing Lakehouse 2.0: What Changes?

Animesh Kumar
 and 
Travis Thompson
·
April 18, 2025

The first generation of computers with room-sized machines powered by vacuum tubes was revolutionary. For the first time, humans could automate complex calculations, simulate ballistic trajectories, and model weather patterns.

Read full story

This is what “engine-agnostic” means in practice. It’s not a marketing claim. It is an architectural stance that produces specific outcomes:

* An organisation adopting DataOS does not have to replatform. If data already lives in Snowflake with Fivetran pipelines feeding it, DataOS builds Data Products directly in that Snowflake. No migration. No rip-and-replace. This is the overlay pattern, and it is one of the most common adoption shapes.
* A single AI agent can reason across Data Products from multiple engines through a consistent interface, because the contract lives above the engine, not within it.
* As the organisation’s substrate evolves (new engines added, old ones deprecated), the Data Products above them can remain stable. Consumers bind to the contract, not to the storage.

The comparison to the data gravity platforms is not that DataOS does more than they do. In several dimensions, they do more because they own the substrate. The comparison is aboutwhere the Data Product exists.

In their model, it is inside the compute platform. In DataOS, it is above the compute platform, so it can be consumed consistently regardless of which compute platform holds it.

For an enterprise whose data landscape is one platform today and will be one platform forever, this distinction doesn’t matter. For everyone else, it is the distinction.

## Discovery, Production, Consumption

The architecture that makes this possible is organised around the path a Data Product takes from first question to active consumption: Discovery, Production, Consumption.

### Discovery

Discoveryis the work that happensbeforea Data Product exists, when a team is answering“what data do we have, and can we build what we want from it?”Metadata, lineage, and profile information are browsable through the catalog. Exploratory SQL is available through an interactive workbench.

If data is missing, it can be brought in: batch, CDC, a wide range of source types, with masking and schema absorption at the boundary. Discovery is iterative and ends with a decision: we have what we need, let’s build; or we know what’s missing.

### Production

Productionis where the Data Product is built. Transformations are declarative, SQL or Python. Validation runs in-band: tests, audits, assertions, quality checks that block bad data from being published rather than alerting on it after.

A semantic layer captures business metrics and dimensions once, with definitions that consumers (humans, applications, agents) all resolve through. The result is materialised in the chosen engine, exposed through a thin API layer (REST and GraphQL), versioned like software, governed like a product.

### Consumption

Consumptionis where the Data Product is used. Applications connect through REST or GraphQL. BI tools connect through database wire protocols as if they were talking to a regular database. Notebooks and ML pipelines connect through SDKs.

AI agents connect through MCP (the Model Context Protocol) to a set of tools that expose the product’s metadata, schema, lineage, quality, runs, and semantic query surface. Each consumer gets the protocol that fits; the contract behind every protocol is the same.

DataOS organises every capability around the path a Data Product takes from the first question to active consumption. The engine is the through-line; governance, lineage, and observability apply across all three stages.

The full capability description of each stage lives in the internal guide. The relevant point for this document is structural: the three stages are how DataOS operationalises the thesis.

* Discovery makes the cost of building a Data Product low.
* Production makes the product reliable.
* Consumption makes it reachable by every consumer shape the organisation has.

Each stage is instrumented so that governance, lineage, and observability are not additional projects but properties of the platform.

## Why MCP Matters

The most important surface in consumption, for the purposes of this document, is the one for AI agents. This deserves its own section because it is the mechanism through which a Data Product becomes an answer to the enterprise AI problem described at the start of the document.

MCP is the Model Context Protocol, originated by Anthropic in late 2024 and now broadly adopted as a standard for how AI agents talk to tools and data sources. It is conceptually simple: an agent connects to a server that exposes a set of tools, each with a defined input schema and behaviour, and the agent invokes them as needed during reasoning.

### For a Data Product, MCP is the native agent interface.

DataOS exposes tools through which an agent can read the product’s metadata, inspect its schema, trace its lineage, check its quality, view its run history, and issue semantic queries against it. Every one of these is grounded in the product’s contract. The agent does not write raw SQL against arbitrary tables; it resolves through the semantic layer, constrained by the product’s definitions, observed through the product’s quality gates.

The practical difference this makes: an agent operating against a raw warehouse is an OpenAI-scale context-infrastructure project in its own right. An agent operating against a Data Product through MCP is a consumer of context infrastructure that has already been built. The agent’s job shrinks from“assemble and reason about a data landscape”to“reason within a contracted, observable product.”This is the difference between agents that work and agents that fail quietly.

It is also why the AI-era conversation about data cannot be separated from the Data Product conversation. The model is one input. The context layer is the other. MCP is the wire between them. And the reliability of the whole system depends on whether the context being wired in is a governed product or an ad-hoc scrape.

A caution worth noting, from analyst consensus.

At Gartner D&A 2026, Andres Garcia-Rodeja presented a prediction thatroughly 60% of agentic analytics projects relying solely on MCP will fail by 2028, specifically because MCP without a consistent semantic layer underneath is insufficient.

MCP is the wire; what travels over it still has to be a governed product with coherent semantics. This is the architecture Modern Data 101 describes in“Architectural Standards for Data Products and AI Interactions”: Data Products provide the economic unit, a Data Developer Platform provides the industrialisation, and MCP provides the AI interface. All three, together, are what make agent-driven analytics work. Missing any one, it fails.

## What This Means

The argument assembled across this document comes down to four claims, each of which holds independently and together.

* The enterprise AI era is real and is here.Agents are being deployed, deals are being signed, budget is being allocated. The organisations that make this work will have an advantage; those that don’t, won’t.
* Making it work is not primarily a model problem.The industry spent 2025 discovering this, and the consensus across OpenAI, a16z, MIT, Palantir, and others is that the missing piece is context infrastructure: durable, managed, versioned, available to agents.
* The right shape for that context is the Data Product.This is not a new idea, but the AI era has made it load-bearing. A Data Product is what an enterprise builds once, and agents consume forever, in contrast to the status quo of agents assembling context per query.
* The architectural choice ofwhere the Data Product exists…determines whether this strategy is portable across the enterprise or locked into a single compute platform. The data gravity platforms (Databricks, Snowflake, Palantir) are building strong context surfaces tied to their compute. DataOS is building for the enterprise whose data is in more than one place, and intends to keep it that way.

The missing layer for enterprise AI is the Data Product, and the right way to build Data Products is above the engine, not inside it.

Thanks for reading Modern Data 101! Subscribe for free to receive new posts and support our work.

Subscribe

#### ☎️ MD101 Support

If you have any queries about the piece, feel free to connect with the author(s). Or connect with the MD101 team directly atcommunity@moderndata101.com🧡

### Author Connect 💬

Connect withAnimesh on LinkedIn💬

Connect withShubhanshu on LinkedIn💬

Connect withDevendra on LinkedIn💬

36
2
9
Share
Previous
A guest post by
Shubhanshu Jain
Subscribe to Shubhanshu
A guest post by
Devendra Singh Rathore
Over a decade building data platforms that unify, secure, and simplify enterprise data. Focused on AI-ready, scalable systems and modern data architecture. Sharing practical insights for data leaders and builders.
Subscribe to Devendra