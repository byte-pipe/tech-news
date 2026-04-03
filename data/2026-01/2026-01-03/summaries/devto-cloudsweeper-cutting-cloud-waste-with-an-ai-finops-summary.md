---
title: CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent - DEV Community
url: https://dev.to/qlooptech/cloudsweeper-cutting-cloud-waste-with-an-ai-finops-agent-580l
date: 2025-12-31
site: devto
model: llama3.2:1b
summarized_at: 2026-01-03T11:21:52.195264
screenshot: devto-cloudsweeper-cutting-cloud-waste-with-an-ai-finops.png
---

# CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent - DEV Community

## CloudSweeper: AI-Powered First Click FinOps Agent

This summary captures the key points of the article about CloudSweeper, an AI-powered first click finops agent that helps engineers reduce cloud costs across AWS and Azure.

### What is CloudSweeper?

CloudSweeper analyzes real usage metrics, configurations, tags, and historical behavior to recommend one of three clear actions for each resource: KEEP, DOWNSIZE, or DELETE. Each recommendation includes a confidence score and an estimated cost impact.

### System Design

CloudSweeper is designed:

* Read-only (no write permissions)
* Safe by default (no automated changes)
* Engineer-in-the-loop, not fully autonomous
* Designed for small to mid-sized teams that don't have a dedicated finops function but still need enterprise-grade cost discipline.

### My Pitch Video and Demo

A 5-minute video can be found at https://cloudsweeper.io.
Live demo is available on the Mux Player: player.mux.com

### The Story Behind CloudSweeper

Cloud cost waste is a confidence problem, not a visibility problem. In many AWS or Azure environments, teams suspected there was waste but didn't act due to fear of breaking production.

### Technical Highlights

CloudSweeper uses a Python 3.13-based async architecture, aioboto3 for interactions, and aiohttp for async HTTP operations.

## Key Benefits

* Helps engineers confidently reduce cloud costs across AWS and Azure without automation or risk.
* Suitable for small to mid-sized teams with enterprise-grade cost discipline.
* Designed to be easy to onboard and use.
