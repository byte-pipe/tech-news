---
title: Google pitches Agentic Data Cloud to help enterprises turn data into context for AI agents | CIO
url: https://www.cio.com/article/4162745/google-pitches-agentic-data-cloud-to-help-enterprises-turn-data-into-context-for-ai-agents-2.html
site_name: tldr
content_file: tldr-google-pitches-agentic-data-cloud-to-help-enterpri
fetched_at: '2026-04-26T11:38:27.775891'
original_url: https://www.cio.com/article/4162745/google-pitches-agentic-data-cloud-to-help-enterprises-turn-data-into-context-for-ai-agents-2.html
date: '2026-04-26'
description: Google’s is moving to counter AWS and Microsoft in the emerging AI data stack race.
tags:
- tldr
---

by									
Anirban Ghoshal

Senior Writer

# Google pitches Agentic Data Cloud to help enterprises turn data into context for AI agents

News

Apr 23, 2026
6 mins
 

## Google’s is moving to counter AWS and Microsoft in the emerging AI data stack race.

 

							Credit: 															Michael Vi / Shutterstock													

Google is recasting its data and analytics portfolio as the Agentic Data Cloud, an architecture it says is aimed at moving enterprise AI from pilot to production by turning fragmented data into a unified semantic layer that agents can reason over and act on more reliably at scale.

The new architecture builds on Google’s existing data platform strategy, bringing together services such asBigQuery,Dataplex, andVertex AI, and elevating their capabilities in metadata, governance, and cross-cloud interoperability into what the company describes as a shared intelligence layer.

That intelligence layer strategy is underpinned by the new Knowledge Catalog, an evolution ofDataplex Universal Catalog, that the company said uses new capabilities to extend its metadata foundation into a semantic layer mapping business meaning and relationships across data sources.

These capabilities include native support for third-party catalogs, applications such as Salesforce, Palantir, Workday, SAP, and ServiceNow, and the option to move third-party data to Google’s lakehouse, which automatically maps the data to Knowledge Catalog.

To capture business logic more directly for data stored inside Google Cloud, the company is adding tools including a LookML-based agent, currently in preview, that can derive semantics from documentation, and a new feature in BigQuery, also in preview, that allows enterprises to embed that business logic for faster data analysis.

Beyond aggregation, the catalog itself is designed to continuously enrich semantic context by analyzing how data is used across an enterprise, senior google executives wrote in ablog post.

This includes profiling structured datasets as well as tagging and annotating unstructured content stored in Google Cloud Storage, the executives pointed out, adding that the catalog’s underlying system can also infer missing structure in data by  using its Gemini models to generate schemas and identify relationships.

## Turning data into business context the next battleground for AI

For analysts, Google’s focus on semantics targets one of the biggest barriers to production AI for enterprises.

“The hardest AI problem is inconsistent meaning,” saidDion Hinchcliffe, lead of the CIO practice at The Futurum Group, noting that a unified semantic layer could help CIOs establish consistent business context across systems while reducing the need for developers to manually stitch together metadata and lineage.

That focus on semantic context also reflects a broader shift in how hyperscalers are approaching enterprise AI. Microsoft withFabric IQand AWS withNova Forgeare pursuing similar strategies, building semantic context layers over enterprise data to make AI systems more consistent and easier to operationalize at scale.

While Microsoft’s approach is to wrap AI applications and agents with business context and semantic intelligence in its Fabric IQ and Work IQ offerings, AWS want enterprises to blend business context into a foundational LLM by feeding it their proprietary data.

Mike Leone, principal analyst at Moor Insights and Strategy, said Google’s approach, though closer to Microsoft’s, places the data gravity one layer above the lakehouse, within its data catalog and semantic graph capabilities.

“Google and Microsoft are solving the same problem from different angles, Fabric through a unified data foundation and Google through a unified semantic and context layer,” Leone said.

Even data analytics software vendors are converging on the idea of offering a catalog that can map semantic context from a variety of data sources, Leone added, pointing toDatabricks’ Unity CatalogandSnowflake’s Horizon Catalog.

## Semantic accuracy could pose challenges for CIOs

However, Google’s approach to building an intelligent semantic layer, especially its evolved Knowledge Catalog, comes with its own set of risks for CIOs.

The new catalog’s automated semantic context refinement capability, according toJim Hare, VP analyst at Gartner, could amplify governance challenges, especially around metadata management: “In complex enterprise domains, errors in inferred relationships or definitions will require ongoing human domain oversight to maintain trust.”

Hare also warned of operational and cost management challenges.

“Agent-driven workflows spanning analytical and operational data, potentially across clouds, will introduce new challenges in observability, debugging, and cost predictability,” he said. “Dynamic agent behavior can generate opaque consumption patterns, requiring chief data and analytics officers (CDAOs) to closely manage cost attribution, usage limits, and operational guardrails as these capabilities mature.”

Adopting Google’s new architectural approach could increase dependence at the orchestration layer, resulting in issues around portability, he warned: “Exiting Google-managed semantics, Gemini agents, or BigQuery abstractions may be harder than migrating data alone.”

## Bi-directional federation as strategic play

Even so, the trade-offs may be acceptable for enterprises prioritizing tighter data integration over flexibility.

As part of the new architecture, Google is also offering cross-platform data interoperability via theApache IcebergREST Catalog that it says will allow bi-directional federation, in turn letting enterprises access, query, and govern data across environments such as Databricks, Snowflake, and AWS without requiring data movement or cost in egress fees.

ForStephanie Walter, practice leader of the AI stack at HyperFRAME Research, this interoperability will be strategically important for enterprises scaling agents in production, especially ones that have heterogenous data environments.

Moor Insights and Strategy’s Leone, though, sees it as a different strategic play to address enterprises’ demand to access Databricks, Snowflake, and hyperscaler environments without costly data movement.

Google’s Agentic Data Cloud architecture also includes a Data Agent Kit, currently in preview, which the company says is designed to help enterprises build, deploy, and manage data-aware AI agents that can interact with governed datasets, apply business logic, and execute workflows across systems.

Robert Kramer, managing partner at KramerERP, said the Data Agent Kit will help data practitioners abstract t daily tasks, in turn lowering the barrier to operationalizing agentic AI across workflows.

However, Gartner’s Hare warned that enterprises should guard against over delegating critical data management decisions to automated agents without sufficient observability, validation controls, and human review, particularly where downstream AI systems depend on these agents for continuous data operations.

This article first appeared onInfoWorld.

Artificial Intelligence
Data Warehousing
Analytics
Data Management
 

 

				SUBSCRIBE TO OUR NEWSLETTER			

### From our editors straight to your inbox

				Get started by entering your email address below.			

 

Please enter a valid email address

Subscribe

 

														by 															

																Anirban Ghoshal															

Senior Writer

1. Follow Anirban Ghoshal on X
2. Follow Anirban Ghoshal on LinkedIn

Anirban is an award-winning journalist with a passion for enterprise software, cloud computing, databases, data analytics, AI infrastructure, and generative AI. He writes for CIO, InfoWorld, Computerworld, and Network World. He won the 2024 Silver Azbee Award for Best News Article in the Technology category. He has a post-graduate diploma in journalism from the Indian Institute of Journalism and New Media.

## More from this author

* news### What Google’s “unified stack” pitch at Cloud Next ‘26 really means for CIOsApr 24, 20267 mins
* news### Oracle delivers semantic search without LLMsApr 17, 20264 mins
* news### Salesforce launches Headless 360 to support agent-first enterprise workflowsApr 16, 20266 mins
* news### MuleSoft Agent Fabric adds new ways to keep AI agents in lineApr 15, 20266 mins
* news### ServiceNow embeds AI across the platform with Context EngineApr 9, 20266 mins
* news### AWS turns its S3 storage service into a file system for AI agentsApr 8, 20263 mins
* news### NetSuite expands toolkit to ease enterprise use of third-party AI assistants with ERP dataApr 1, 20265 mins
* news### Oracle bets on agentic apps in Fusion suite to ‘fully’ automate business processesMar 24, 20267 mins
 

## Show me more

Popular
Articles
Podcasts
Videos

brandpost
 
Sponsored by Zscaler
 

### Delivering an impactful 15-minute board briefing

 
By Zscaler
Apr 24, 2026
5 mins

IT Leadership

opinion
 
 

### Shadow AI morphs into shadow operations

 
By Marc Manzano
Apr 24, 2026
8 mins

Application Security
Artificial Intelligence
DevSecOps

opinion
 
 

### Moving autonomous agents into production requires a universal context layer

 
By David Smith
Apr 24, 2026
6 mins

Artificial Intelligence
Data Quality
Generative AI

podcast
 
 

### Building for Complexity - Azimut's Blueprint for Wealth Tech in Southeast Asia

 
By Estelle Quek
20 Apr 2026
41 mins

CIO
CIO Leadership Live
CTO

podcast
 
 

### Powering What Can’t Fail-Scaling Digital at Yinson Holdings

 
By Estelle Quek
13 Apr 2026
35 mins

CIO
Energy Industry
IT Governance Frameworks

podcast
 
Sponsored by Vertesia
 

### Episode 5: The CIO’s view on starting, and restarting, AI initiatives

 
Apr 7, 2026
20 mins

Artificial Intelligence

video
 
 

### How Chaos accelerates 3D visualization workflows with AI

 
Apr 23, 2026
13 mins

Artificial Intelligence
Design Thinking
Generative AI

video
 
 

### Building for Complexity - Azimut's Blueprint for Wealth Tech in Southeast Asia

 
By Estelle Quek
20 Apr 2026
41 mins

CIO
CIO 100
CTO

video
 
 

### CData powers AI agents with secure access to enterprise data

 
Apr 16, 2026
13 mins

Artificial Intelligence
Data Governance
Data Management