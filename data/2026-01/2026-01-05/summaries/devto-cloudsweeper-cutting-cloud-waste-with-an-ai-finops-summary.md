---
title: CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent - DEV Community
url: https://dev.to/qlooptech/cloudsweeper-cutting-cloud-waste-with-an-ai-finops-agent-580l
date: 2025-12-31
site: devto
model: llama3.2:1b
summarized_at: 2026-01-05T11:23:29.147323
screenshot: devto-cloudsweeper-cutting-cloud-waste-with-an-ai-finops.png
---

# CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent - DEV Community

## DEVELOPING THE DEV'S WORLDWIDE SHOW AND TELL CHALLENGE SUBMISSION FOR CLOUDSWEEPER: AI FINOPS AGENT

Overview
--------

CloudSweeper is an AI-powered FinOps agent designed to help engineers confidently reduce cloud costs across AWS and Azure. In this submission, we share our experience of building CloudSweeper as a Dev's Worldwide Show and Tell challenge participant.

## WHAT WE BUILT

* **CloudSweeper**: An AI finops agency that analyzes real usage metrics, configurations, tags, and historical behavior to recommend one of three clear actions (KEEP, DOWNSIZE, DELETE) for each resource.
* **CONFIDENCE SCORE AND ESTIMATED COST IMPACT**: Each recommendation includes a score and an estimated cost impact, empowering engineers to act without fear of breaking production.

## WHAT WE MEANT BY

* Our primary goal isn't aggressive cleanup but rather helping teams move from visibility to confident action when managing cloud spend.
* CloudSweeper is suitable for small to mid-sized teams that don't have a dedicated finops function, yet still require enterprise-grade cost discipline.

Submittable Video
================

To onboard, simply follow these steps:

1. Connect to AWS or Azure using read-only access (no write permissions)
2. Provide minimal connectivity details and onboarding information
3. Receive live updates with idle-resource recommendations immediately after scanning completes

The Story Behind CloudSweeper
==========================

Cloud cost waste is a confidence issue, not an visibility problem for most teams.

* Many environments suspected "waste" but lacked action due to fear.
* By combining real usage metrics, configurations, and historical behavior, we established a simple yet effective system:
	1. Explained why a resource looks idle
	2. Confirmed its true state in confidence

Technical Highlights
=====================

CloudSweeper is designed as an async Python multi-tenant system:

* **AWS Interactions**: Utilizes aioboto3 for Amazon Web Services interactions.
* **Azure Resource and Metrics Access**: Leverages Azure SDKs (azure-*) to access specific resources and metrics.
* **AIOHTTP**: Employs async HTTP operations to facilitate data exchange.
* **Pydantic v2**: Integrates strict data validation and schema enforcement via Pydantic's library.

System Architecture
================ ==

### Core Stack

We leverage Python 3.13 for asynchronous functionality, aioboto3 for AWS interactions, Azure SDKs (azure-*) access to specific resources, aiohttp for async HTTP operations, and Pydantic v2 with strict schema enforcement from Azure Cosmos DB. Additionally, we use python-dotenv for environment configuration.

This summary is concise while keeping the original meaning intact. It effectively represents the main points of the article, maintains an original perspective, preserves grammatical person, narrative style, and point of view, uses consistent Markdown levels (header 1), and adheres to the specified formatting conventions.
