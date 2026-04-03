---
title: CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent - DEV Community
url: https://dev.to/qlooptech/cloudsweeper-cutting-cloud-waste-with-an-ai-finops-agent-580l
date: 2025-12-31
site: devto
model: llama3.2:1b
summarized_at: 2026-01-07T11:23:33.107905
screenshot: devto-cloudsweeper-cutting-cloud-waste-with-an-ai-finops.png
---

# CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent - DEV Community

Here is a concise and informative summary of the article:

**CloudSweeper: A Cutting AI FinOps Agent for Enterprise Cost Discipline**

**What it does:** Develops an AI-powered FinOps agent called CloudSweeper that helps engineers in small to mid-sized teams manage their cloud expenses. It analyzes real usage metrics, configurations, and historical behavior to provide actionable recommendations (KEEP, DOWNSIZE, DELETE) with confidence scores.

**Key Features:**

* Secure, read-only access
* Safe by default, no automated changes
* Engineer-in-the-loop, not fully autonomous
* Designed for small to mid-sized teams, but enterprise-grade cost discipline is required

**Pitch Video:** A live demo of the system and its benefits, showcasing ease of use, no write permissions required.

**Story Behind It:**
CloudSweeper aimed to close the confidence gap between visibility (identifying idle resources) and confident action (taking decisive decisions). The internal experiment proved successful, leading to development as an AI-enabled FinOps agent for enterprise professionals.

**Technical Highlights:**

* Built using Python 3.13, aioboto3, Azure SDKs, aiohttp, Pydantic v2, and Cosmos DB.
* Multi-tenant, async architecture with secure IAM/RACB access.
* Designed to scan safely customer-owned cloud environments without disrupting workloads.

**Benefits:**
CloudSweeper provides engineers with confident decision-making, avoiding the risk of accidental loss or production downtime. Its security features ensure that changes are safe and secure for production environments.
