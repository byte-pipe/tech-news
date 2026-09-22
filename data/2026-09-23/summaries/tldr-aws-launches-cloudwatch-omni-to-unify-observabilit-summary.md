---
title: AWS launches CloudWatch Omni to unify observability for AI agents and applications | InfoWorld
url: https://www.infoworld.com/article/4225120/aws-launches-cloudwatch-omni-to-unify-observability-for-ai-agents-and-applications.html
date: 2026-09-23
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-23T06:46:24.064434
---

# AWS launches CloudWatch Omni to unify observability for AI agents and applications | InfoWorld

# AWS launches CloudWatch Omni to unify observability for AI agents and applications

## Overview
- AWS introduces CloudWatch Omni, an off‑console experience that consolidates telemetry from agents, applications, and infrastructure.
- Designed to let developers and operations teams start investigations from the application level rather than navigating multiple AWS consoles.
- Provides automatic topology discovery and supports natural‑language or SQL queries via an integrated AI assistant and the AWS DevOps Agent.

## Deployment
- **Existing CloudWatch users**: No re‑configuration needed; current logs, metrics, and traces become available in Omni’s unified data store, and existing dashboards and alarms are retained.
- **New users**: Must ingest telemetry through OpenTelemetry Protocol (OTLP) endpoints and create a “space” for each application; Omni then discovers topology and surfaces dependencies.
- Supports agent frameworks such as LangGraph, CrewAI, OpenAI Agents SDK, Vercel AI SDK, and AWS Strands.
- Allows integration of external evaluation tools like Braintrust, DeepEval, and Ragas.
- Offers multiple interfaces:
  - Off‑console web UI for operational teams.
  - Native extensions for VS Code, Kiro, and Cursor for developers, enabling local tracing without an AWS account.

## Expected Benefits
- Reduces friction in debugging agent behavior, potentially boosting developer productivity.
- Gives CIOs a single operating view across agents, applications, and infrastructure, decreasing tool fragmentation.
- May accelerate moving agents from pilot to production by providing clearer visibility into failures and their business impact.

## Risks and Considerations
- **Vendor lock‑in**: Heavy reliance on a single observability layer could limit independent system understanding.
- **Cost**: High telemetry volume (each prompt, tool call, and handoff is traced) can lead to unexpected ingestion charges.
- **Evaluation quality**: Effectiveness of agent evaluations depends on well‑defined success criteria, which many enterprises lack.

## Adoption Outlook
- Early adopters likely to be current CloudWatch and Bedrock AgentCore customers, as their telemetry transfers seamlessly.
- Enterprises already using mature observability stacks (Datadog, New Relic, Grafana) may see limited advantage.
- Organizations running multiple agent pilots may benefit from standardized evaluation and operations.

## Availability and Pricing
- Currently available in US East (N. Virginia), US West (Oregon), and Europe (Ireland) regions.
- Telemetry can be centralized from any region/account into a chosen Omni region at no extra cost.
- Pricing components:
  - Data ingestion charged per gigabyte.
  - Storage charged per gigabyte per month.
  - Analytics usage‑based; up to five times the ingested logs/spans included at no extra charge.
  - Separate pricing for the AWS DevOps Agent.
- Existing CloudWatch customers must opt‑in to create an Omni space and configure access.