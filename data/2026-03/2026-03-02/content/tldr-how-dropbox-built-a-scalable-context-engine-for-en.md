---
title: How Dropbox Built a Scalable Context Engine for Enterprise Knowledge Search - InfoQ
url: https://www.infoq.com/news/2026/02/dropbox-context-engine/
site_name: tldr
content_file: tldr-how-dropbox-built-a-scalable-context-engine-for-en
fetched_at: '2026-03-02T08:25:25.954289'
original_url: https://www.infoq.com/news/2026/02/dropbox-context-engine/
date: '2026-03-02'
description: Dropbox engineers have detailed how the company built the context engine behind Dropbox Dash, revealing a shift toward index-based retrieval, knowledge graph-derived context, and continuous evaluation
tags:
- tldr
---

InfoQ HomepageNewsHow Dropbox Built a Scalable Context Engine for Enterprise Knowledge Search

 Architecture & Design
 

QCon London (March 16-19, 2026): Learn proven architectural practices to scale your systems faster. 

# How Dropbox Built a Scalable Context Engine for Enterprise Knowledge Search

Feb 18, 20263
									min read

by

* Matt Foster

#### Write for InfoQ

Feed your curiosity.

Help 550k+ global 
senior developers 
each month stay ahead.
Get in touch

Dropbox engineers have detailed how the organization was able to build the context engine behindDropbox Dash, demonstrating a shift towards index-based retrieval, knowledge graph-derived context, and continuous evaluation to support enterprise AI knowledge retrieval at scale. The design points to a broader pattern emerging across enterprise assistants, whereby teams are deliberately constraining their live tool usage and instead relying more heavily on pre-processed, permission-aware context to speed latency, improve quality and ease token pressure.

As part of arecent engineering talk, Dropbox VP of engineering, Josh Clemm described their application as a response to work in enterprises being distributed across dozens of SaaS applications, each with their own distinct APIs, permission structures and rate limits. Despite the latest language models incorporating reasoning, Clemm said they lack direct access to an enterprise's data for context. This leads to additional infrastructure being necessary to retrieve potentially sensitive information safely.

The architecture at the center of Dash relies on pre-processing content rather than runtime inference retrieval. Data from the connected knowledge applications is normalized, enriched and indexed before a query is made using a mix of lexical search and dense vectors. This allows the application to return results without having to create a spiderweb of API calls at query-time.

This method does incur higher complexity and storage costs, but Dropbox felt that the investment was worthwhile given the benefits of offline ranking experiments, improved relevance signals and predictable query-time performance.

One of the main components of the Dash application is the use of knowledge graphs to create models of relationships across common business-centric media (people, documents, meetings etc). However, rather than querying a graph database at runtime, "knowledge bundles" are derived and fed into the aforementioned indexing pipeline. Clemm states that earlier experiments with graph databases led to latency and query-pattern changes, this resulted in the team treating graph information as part of the context enrichment rather than another layer to query.

The team also described the challenges associated with exposing multiple tools directly to language models through the MCP (Model Context Protocol). Citing context window consumption, Dropbox observed degraded agent performance and slow queries when many of the tools were used asynchronously. To get around this, the team consolidated retrieval behind a small number of high-level tools. These tools were able to retrieve context outside of the prompt and route more complex requests to agents with narrower scopes.

The MCP's creators have also expressed theirconcernsabout context window consumption when using multiple tools. They state that each addition requires careful managment.

Outside of retrieval, Dropbox touched on the importance of label evaluation at scale. Since the results from queries are consumed by language models rather than humans, traditional click-based relevance signals do not work. Dropbox was able to use language models as judges to measure and score retrieval quality. This allowed them to refine their prompts and ranking logic, thereby reducing labelling disagreements with their human users.

The Dash team was able to operationalize the evaluation process usingDSPy, a framework for prompt optimization. Clemm states that DSPy was able to manage more than 30 prompts across all workflows. This allowed faster model switching without manually rewriting each model's prompts.

The approach taken by the Dash team closely resembles patterns seen in other enterprise knowledge assistants.Microsoft 365 Copilotalso relies on a pre-computed semantic index derived from the Microsoft Graph to retrieve context efficiently.

Together, these designs point to a growing signal around treating context as a first-class system in enterprise AI, rather than something assembled on the fly at inference time. As teams scale their internal search and agent capabilities within large organizations, architectures that pre-compute, constrain, and continuously evaluate context appear to be becoming a more common foundation.

 

## About the Author

 

 

 

#### Matt Foster

Show more
Show less

### Rate this Article

Adoption

Style

 Author Contacted

#### This content is in theLarge language modelstopic

##### Related Topics:

* Architecture & Design
* AI, ML & Data Engineering
* Large language models
* Search
* Retrieval-Augmented Generation
* Architecture
* Distributed Systems

* #### Related Editorial
* #### Related Sponsors##### From Observability to Actionability: Designing Agentic AI for Autonomous SRE on AWS
* ##### From Observability to Actionability: Designing Agentic AI for Autonomous SRE on AWS
* #### Related SponsorBoost AWS effectiveness with Agentic AI — unify telemetry, reduce noise, and resolve incidents faster.Learn More.

### Related Content

### The InfoQNewsletter

A round-up of last week’s content on InfoQ sent out every Tuesday. Join a community of over 250,000 senior developers.View an example

Enter your e-mail address

Select your country

Select a country

I consent to InfoQ.com handling my data as explained in this 
Privacy Notice
.

We protect your privacy.