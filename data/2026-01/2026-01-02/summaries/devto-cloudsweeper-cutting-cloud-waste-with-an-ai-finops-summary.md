---
title: CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent - DEV Community
url: https://dev.to/qlooptech/cloudsweeper-cutting-cloud-waste-with-an-ai-finops-agent-580l
date: 2025-12-31
site: devto
model: llama3.2:1b
summarized_at: 2026-01-02T11:24:33.011093
screenshot: devto-cloudsweeper-cutting-cloud-waste-with-an-ai-finops.png
---

# CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent - DEV Community

**CloudSweeper: An AI-Powered FinOps Agent**

## What is CloudSweeper?

CloudSweeper is an AI-powered, read-only FinOps agent that helps engineers confidently reduce cloud costs across AWS and Azure. It analyzes real usage metrics, configurations, tags, and historical behavior to recommend one of three clear actions for each resource.

## How does it work?

1. Real-time scanning: CloudSweeper scans customers' cloud environments without disrupting workloads.
2. Data analysis: The agent analyzes usage metrics, configurations, tags, and historical behavior.
3. Recommendation generation: Based on the analysis, CloudSweeper recommends one of three clear actions:
 * KEEP
 * DOWNSIZE
 * DELETE
4. Confidence score and estimated cost impact: Each recommendation includes a confidence score and an estimated cost impact.

## Benefits

* No automated changes or modifications to production environments.
* Engineer-in-the-loop approach, with only the engineer being responsible for review and approval of changes.
* Designed for small to mid-sized teams without dedicated FinOps function.
* CloudSweeper is optimized for read-only access, with no write permissions.

## Show and Tell Submission

### Key Points

* CloudSweeper helps engineers confidently reduce cloud costs across AWS and Azure.
* Analyzes real usage metrics, configurations, tags, and historical behavior.
* Recommends actions: KEEP, DOWNSIZE, DELETE.
* Confidence score and estimated cost impact included in each recommendation.

## Pitch Video

### Mux Player

### Demo

Live App: https://cloudsweeper.io

### The Story Behind It

Cloud cost waste is a visibility problem that needs to be addressed. In every AWS or Azure environment I worked with, teams suspected there was waste - but lacked the confidence to act.

**Technical Highlights**

* Asynchronous Python system
* AWS interactions using aioboto3
* Azure resource and metrics access using Azure SDKs (azure-*)
* Multi-tenant state using Azure Cosmos DB
* Strict data validation and schema enforcement using Pydantic v2

### Cloud Scanning Architecture

Secured by multiple layers of permissions, ensuring the safety of customer environments.

The summary will be:

CloudSweeper is an AI-powered FinOps agent that helps engineers reduce cloud costs across AWS and Azure. It analyzes usage data and recommends actions: KEEP, DOWNSIZE, DELETE. Key points include its ability to analyze real metrics, confidence scores, and estimated cost impacts. The pitch video showcases the system's capabilities, highlighting its engineer-in-the-loop approach. Technical highlights explain how CloudSweeper works and protects customer environments.
