---
title: CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent - DEV Community
url: https://dev.to/qlooptech/cloudsweeper-cutting-cloud-waste-with-an-ai-finops-agent-580l
date: 2025-12-31
site: devto
model: llama3.2:1b
summarized_at: 2026-01-01T11:24:51.644227
screenshot: devto-cloudsweeper-cutting-cloud-waste-with-an-ai-finops.png
---

# CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent - DEV Community

**CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent**

## What is CloudSweeper?
CloudSweeper is an AI-poweredFinOps agent that helps engineers confidently reduce cloud costs across AWS and Azure. This solution analyzes real usage metrics, configurations, tags, and historical behavior to recommend one of three clear actions for each resource.

## Key Features:

* Analyzes usage data and configuration metrics
* Recommends one of three actions: KEEP, DOWNSIZE, or DELETE
* Confidence score and estimated cost impact included
* Secure by default (no automated writes)
* Safe and engineer-in-the-loop approach

## My Approach to the Pitch Video:
To summarize the key points from the blog post:

The DEV Worldwide Show and Tell Challenge submission presents CloudSweeper as an AI-poweredFinOps agent that helps engineers reduce cloud costs without fear of breaking production.
Cloudsweeper is designed for small to mid-sized teams, providing enterprise-grade cost discipline.
It works by analyzing usage metrics, configurations, tags, and historical data to recommend clear actions, including KEEP, DOWNSIZE, or DELETE.

## My Pitch Video:

* Live demo: https://cloudsweeper.io
* Mux player: player.mux.com

### Technical Highlights

* Asynchronous Python system for multi-tenant access
* Amazon Web Services (AWS) interactions using aioboto3
* Azure Resource Manager SDKs for resource and metrics access
* aiohttp library for async HTTP operations
* Pydantic v2 for data validation and schema enforcement, with Azure Cosmos DB storing scan results

### Cloud Scanning Architecture:

 * Reads-only access to customer-owned cloud environments without disrupting workloads
