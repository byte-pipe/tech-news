---
title: CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent - DEV Community
url: https://dev.to/qlooptech/cloudsweeper-cutting-cloud-waste-with-an-ai-finops-agent-580l
date: 2025-12-31
site: devto
model: llama3.2:1b
summarized_at: 2026-01-04T11:26:17.607022
screenshot: devto-cloudsweeper-cutting-cloud-waste-with-an-ai-finops.png
---

# CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent - DEV Community

**CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent**

**What is CloudSweeper?**
CloudSweeper is a machine learning-powered FinOps agent that helps engineers reduce cloud costs by analyzing usage metrics, configurations, tags, and historical behavior. It recommends one of three clear actions: KEEP, DOWNSIZE, or DELETE.

**Key Features:**

* Analyzes real usage metrics and data to provide recommendations
* Confidence score and estimated cost impact for each recommendation
* Safely access customer-owned cloud environments without disruption
* Based on human-in-the-loop decision-making

**My Pitch Video**
The video showcases the CloudSweeper app, live, with a demo link.

**Technical Highlights:**

* Built as a multi-tenant Python system for safe and secure operation in AWS and Azure environments
* Utilizes AI/ML and python-based frameworks to analyze usage data and provide recommendations

**Design Goals:**
CloudSweeper aims to help small to mid-sized teams manage cloud spending with confidence, even without a dedicated FinOps function. The system focuses on visibility, not risk, and provides actionable insights for engineers to make informed decisions.

**Implementation Approach:**
The implementation involves scanning customer-owned cloud environments using Python 3.13 (async) and Azure SDKs for access to AWS and Azure resources. The system leverages io-boto3 and aiohttp for async HTTP operations and Pydantic v2 for strict data validation.
