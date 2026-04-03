---
title: 'CloudSweeper: Cutting Cloud Waste with an AI FinOps Agent - DEV Community'
url: https://dev.to/qlooptech/cloudsweeper-cutting-cloud-waste-with-an-ai-finops-agent-580l
site_name: devto
fetched_at: '2026-01-06T11:07:07.646854'
original_url: https://dev.to/qlooptech/cloudsweeper-cutting-cloud-waste-with-an-ai-finops-agent-580l
author: QLoop Technologies
date: '2025-12-31'
description: This is a submission for the DEV's Worldwide Show and Tell Challenge Presented by Mux What... Tagged with devchallenge, muxchallenge, showandtell, video.
tags: '#devchallenge, #muxchallenge, #showandtell, #video'
---

DEV's Worldwide Show and Tell Challenge Submission 🎥

This is a submission for theDEV's Worldwide Show and Tell Challenge Presented by Mux

## What I built

I builtCloudSweeper, an AI-poweredFinOps agentthat helps engineers confidently reduce cloud costs acrossAWS and Azure.

Instead of just flagging “possible waste,” CloudSweeper analyzes real usage metrics, configurations, tags, and historical behavior to recommend one of three clear actions for each resource:

* KEEP
* DOWNSIZE
* DELETE

Each recommendation includes aconfidence scoreand an estimated cost impact so that engineers can act without fear of breaking production.

The system is designed to be:

* Read-only(no write permissions)
* Safe by default(no automated changes)
* Engineer-in-the-loop, not fully autonomous

CloudSweeper’s goal isn’t aggressive cleanup — it’s helping teams move fromvisibilitytoconfident actionwhen managing cloud spend.

CloudSweeper is built for small to mid-sized teams that don’t have a dedicated FinOps function, but still need enterprise-grade cost discipline.

## My Pitch Video

## Demo

Live App:https://cloudsweeper.io

CloudSweeper connects to AWS and Azure using read-only access.No write permissions, no complex automation.You can onboard in a few minutes by providing minimal connectivity details and immediately see idle-resource recommendations after the first scan is complete.

## The Story Behind It

Cloud cost waste is not a visibility problem — it’s aconfidence problem.

In almost every AWS or Azure environment I worked with, teams alreadysuspectedthere was waste:Idle VMs, unused databases, orphaned disks, forgotten IPs. Dashboards made that obvious.

What stopped the action was fear.

No engineer wants to be the person who deletes something and breaks production.When ownership is unclear and usage patterns are noisy, the safest choice is to do nothing.So waste quietly accumulates month after month.

CloudSweeper started as an internal experiment to close that gap.

The idea was simple: instead of just flagging “possible waste,” combine real usage metrics,configuration data, and historical behavior — then explainwhya resource looks idle, and how confident the system is about that conclusion.

Today, CloudSweeper acts as anAI-enabled FinOps agentthat helps engineers move fromvisibilitytoconfident decision-making— without automation, without risk, and always with humans in the loop.

## Technical Highlights

CloudSweeper is built as anasync, multi-tenant Python systemdesigned to scan safelycustomer-owned cloud environments without disrupting workloads.

### Core Stack

* Python 3.13(fully async)
* aioboto3for AWS interactions
* Azure SDKs (azure-*)for Azure resource and metrics access
* aiohttpfor async HTTP operations
* Pydantic v2for strict data validation and schema enforcement
* Azure Cosmos DBfor multi-tenant state and scan results
* python-dotenvfor environment configuration

### Cloud Scanning Architecture

* Secureread-only IAM / RBAC access(no delete permissions, ever)
* Async scanners for AWS and Azure resources
* Metrics-driven idle detection using:CloudWatch (AWS)Azure Monitor
* CloudWatch (AWS)
* Azure Monitor
* Conservative defaults:If metrics are missing or ambiguous, the resource isskippedNo assumptions, no forced classification
* If metrics are missing or ambiguous, the resource isskipped
* No assumptions, no forced classification

Each idle candidate includes ahuman-readable idle reason(e.g. actual CPU %, thresholds, and time window), not just a binary flag.

### AI-Powered Recommendation Engine

* AI evaluates enriched resource context (metrics, configs, tags, history)
* Produces structured recommendations:KEEPDOWNSIZEDELETE
* KEEP
* DOWNSIZE
* DELETE
* Each recommendation includes:Aconfidence scoreCost impact estimatesReasoning trace
* Aconfidence score
* Cost impact estimates
* Reasoning trace

The system is explicitlyengineer-in-the-loop:No automatic actions are taken.

### Notifications & Integrations

* Webhook-based notificationsfor detected idle resources
* Payloads include detailed idle reasons and context
* Supports integration with tools like Slack, Teams, or internal systems
* Retry logic and validation to ensure delivery reliability

### Design Principles

* Async-first for scale and speed
* Modular codebase with strict size limits per module
* Transparent logging and graceful degradation
* Safety over aggressiveness
* Explainability over black-box decisions.

### Why This Scales

CloudSweeper is designed to scale across hundreds or thousands of cloud accounts:

* Fully async scanning architecture
* Stateless scanners with tenant isolation
* Cloud-provider–agnostic recommendation layer
* Designed for continuous scans, not one-off audits

As cloud usage grows, CloudSweeper grows with it—without requiring more human effort.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
