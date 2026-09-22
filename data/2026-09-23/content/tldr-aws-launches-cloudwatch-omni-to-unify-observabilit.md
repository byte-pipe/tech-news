---
title: AWS launches CloudWatch Omni to unify observability for AI agents and applications | InfoWorld
url: https://www.infoworld.com/article/4225120/aws-launches-cloudwatch-omni-to-unify-observability-for-ai-agents-and-applications.html
site_name: tldr
content_file: tldr-aws-launches-cloudwatch-omni-to-unify-observabilit
fetched_at: '2026-09-23T06:44:58.259256'
original_url: https://www.infoworld.com/article/4225120/aws-launches-cloudwatch-omni-to-unify-observability-for-ai-agents-and-applications.html
date: '2026-09-23'
description: AWS’ application-centric observability approach could help enterprises reduce tool fragmentation and speed up investigations into agent behavior, although lock-in and rising telemetry costs could limit its appeal, analysts say.
tags:
- tldr
---

by									
Anirban Ghoshal

Senior Writer

# AWS launches CloudWatch Omni to unify observability for AI agents and applications

news

Sep 22, 2026
7 mins

As enterprises continue to move AI agents and agentic applications into production, AWS says traditional observability and monitoring tools — including its own CloudWatch service —will struggle to explain why an agent behaved the way it did.

CloudWatch uses metrics, logs, and traces to monitor applications and infrastructure across accounts, regions, and services through the AWS Management Console, but that only provides part of the picture, AWS says. Understanding an agent’s behavior requires developers and operations teams to jump between agent-specific observability and evaluation tools such as those available throughAmazon Bedrock AgentCore, application performance monitoring, and infrastructure monitoring inCloudWatch.

AWS is trying to eliminate that fragmentation by evolving and expanding CloudWatch with a new off-console experience namedCloudWatch Omni, bringing agent, application, and infrastructure telemetry together in an application-centric setup to help enterprises investigate and understand agent behavior in context.

That means developers and operations teams can start with the application they are investigating, rather than navigating across individual AWS resources and monitoring consoles, the hyperscaler wrote in ablog post presenting CloudWatch Omni.

The new tool automatically discovers application topology, the company said, showing how its components are connected, in turn allowing developers and operations teams to query telemetry using natural language or SQL immediately without any manual setup.

Those natural language queries are supported by an AI assistant that handles discovery and guided investigation with support from theAWS DevOps Agent, which is built-in, to  automatically correlate data and identify the root cause across agents, applications, and infrastructure, it said.

## How to deploy CloudWatch Omni

The application-centric approach also changes how teams get started with Omni.

For existing CloudWatch customers, the transition to Omni does not require reconfiguring their existing telemetry as logs, metrics, and traces already sent to CloudWatch become available in Omni through a unified data store that enables correlated analysis across signal types, AWS said. Existing instrumentation, dashboards, and alarms also carry forward into the new setup.

For teams new to CloudWatch and Omni, enterprises will have to import telemetry throughOpenTelemetry Protocol (OTLP)endpoints and create a “space” for an application within CloudWatch Omni, which then automatically discovers the application topology and begins surfacing its dependencies and health signals.

Omni launches with support for multiple agent development frameworks, enabling teams to bring agents built using LangGraph, CrewAI,OpenAI Agents SDK,Vercel AI SDK, and AWS Strands into the same observability setup, AWS said.

It also supports independent evaluation tools, allowing teams to bring their existing agent evaluation workflows into Omni, includingBraintrust,DeepEval, andRagas, the hyperscaler added.

Enterprises also get the option of choosing the kind of Omni interface they want to work with: Operational teams can access an off-console web experience, and developers can see agent traces in Omni via native extensions forVS Code,Kiro, andCursor. The extensions can also be used to run and trace agents locally, with no AWS account required for local development, the company said.

## Omni could improve developer productivity

That ability to access Omni directly via development environments, combined with its application-centric approach should remove the day-to-day friction developers face when investigating agent behavior, in turn improving productivity, analysts said. And there are advantages for CIOs too.

“With Omni, CIOs could gain one operating view across agents, applications, and infrastructure, in turn reducing tool fragmentation,” saidStephanie Walter, practice lead of AI stack at HyperFrame Research.

That, in turn, could speed agent deployment, saidAshish Chaturvedi, executive research leader at HFS Research.

“The blocker on enterprise agent deployment right now is rarely capability, because the agents can usually do the work. The blocker is that CIOs cannot confidently answer what happens when an agent gets it wrong, how they would know, and how fast they could find out. Without an answer to that, no responsible CIO hands an agent authority over anything that touches revenue or customers,” Chaturvedi said. “Since Omni reduces the tools and time required to investigate agent behavior, it could help CIOs move agents from pilots into production by giving them greater visibility into how agents behave when they make mistakes, how quickly those issues can be identified, and what impact they could have on business operations,” Chaturvedi said.

## Lock-in and cost concerns

But that simplicity has consequences, he said: “The more of your observability runs through one vendor’s layer, the more your ability to understand your own systems depend on that vendor.”

There are also potential cost and evaluation challenges that CIOs should take note of, according toMichael Leone, principal analyst at Moor Insights and Strategy.

“Agents generate a lot of telemetry because every prompt, tool call and handoff gets traced, so ingestion bills can climb faster than teams expect,” Leone said.

“Also, agent evaluations are only as good as an enterprise’s definition of a good answer, and a lot of them haven’t written that definition down yet,” he added.

## Who is likely to adopt Omni and why

Enterprises with mature application and infrastructure observability environments based on Datadog, New Relic, or Grafana may not have much to gain from switching to Omni, according to Chaturvedi.

The earliest adopters, said Walter, are likely to be existing CloudWatch and Bedrock AgentCore customers because their telemetry and instrumentation already carry forward into Omni — and, she added, enterprises running multiple agent pilots may also benefit from Omni to standardize evaluation and operations.

## Availability and pricing

Omni is currently available in the US East (N. Virginia), US West (Oregon), and Europe (Ireland) AWS cloud regions. However, the company maintains that this limited regional availability does not restrict its usage.

“Even while Omni runs in these initial Regions, customers can centralize telemetry from across all their accounts and Regions into a preferred Omni Region, giving them a single, unified view of their observability data at no additional cost,” an AWS spokesperson said.

Omni users must pay for data ingestion, storage, and analytics, with telemetry from AWS services available at tiered pricing. Ingestion is charged per gigabyte, and storage per gigabyte per month.

Analytics pricing is usage based, with analytics equivalent to up to five times the amount of logs or spans ingested included at no additional cost, the spokesperson said.

There’s aseparate price list for AWS DevOps Agent, which is integrated into Omni.

Existing CloudWatch customers will not be automatically moved to Omni, but can opt in to create an Omni space and configure access.

Artificial Intelligence
 

 

														by 															

																Anirban Ghoshal															

Senior Writer

1. Follow Anirban Ghoshal on X
2. Follow Anirban Ghoshal on LinkedIn

Anirban is an award-winning journalist with a passion for enterprise software, cloud computing, databases, data analytics, AI infrastructure, and generative AI. He writes for CIO, InfoWorld, Computerworld, and Network World. He won the 2024 Silver Azbee Award for Best News Article in the Technology category. He has a post-graduate diploma in journalism from the Indian Institute of Journalism and New Media. Have a tip, scoop, or insight involving AI, cloud, databases, ERP, or enterprise software? Reach him securely on Signal at Ghoshal_CloudaiSaaSscoop.99

## More from this author

* news### Claude Code now also accepts instructions in OpenAI’s Agents.md formatSep 21, 20265 mins
* news### A zero-click RCE flaw in AI coding agents could have exposed enterprise systemsSep 18, 20266 mins
* news### TypeSafe AI’s new models work with machines, not humansSep 17, 20266 mins
* news### AWS bets that AI agents need an inbox, not another chat windowSep 16, 20266 mins
* news### Cockroach Labs bets on database pooling to cut cost of AI-era workloadsSep 15, 20264 mins
* news### OpenAI launches managed Agents API to simplify enterprise AI agent developmentSep 11, 20265 mins
* news### Databricks unveils adaptive AI retrieval model to cut search costs and latencySep 9, 20267 mins
 

## Show me more

Popular
Articles
Videos

news
 
 

### AWS launches CloudWatch Omni to unify observability for AI agents and applications

 
By Anirban Ghoshal
Sep 22, 2026
7 mins

Artificial Intelligence

news
 
 

### Z.ai disables coding assistant feature after flaw exposed enterprise code upload risk

 
By Gyana Swain
Sep 22, 2026
4 mins

Artificial Intelligence
Data and Information Security
Development Tools

opinion
 
 

### 7 decisions that make an Azure landing zone enterprise-ready

 
By Sachin Suryawanshi
Sep 22, 2026
9 mins

Cloud Security
Enterprise Architecture
Microsoft Azure

video
 
 

### Did OpenAI STEAL Math Researchers' Work? The AI Controversy Explained

 
Sep 16, 2026
6 mins

Python

video
 
 

### Why Software Developers Are “Token Maxxing” AI—and What It Means for Jobs

 
Sep 11, 2026
7 mins

Python

video
 
 

### WebAssembly is getting WILD these days

 
Sep 3, 2026
6 mins

WebAssembly