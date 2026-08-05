---
title: Add security context to operational investigations with AWS DevOps Agent and Wiz | AWS DevOps & Developer Productivity Blog
url: https://aws.amazon.com/blogs/devops/add-security-context-to-operational-investigations-with-aws-devops-agent-and-wiz/
date: 2026-08-06
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-06T07:12:35.006262
---

# Add security context to operational investigations with AWS DevOps Agent and Wiz | AWS DevOps & Developer Productivity Blog

# Add security context to operational investigations with AWS DevOps Agent and Wiz

## Overview
- On‑call engineers often cannot tell whether an alert (CPU spike, latency anomaly, API error) is an operational problem or a security incident without additional context.  
- The lack of security context delays resolution and raises risk.  
- AWS DevOps Agent automates incident investigation and, through the Wiz integration, adds security findings to the investigation via the Model Context Protocol (MCP).

## AWS DevOps Agent
- Acts like an experienced DevOps engineer: learns resource relationships, works with observability tools, runbooks, code repositories, and CI/CD pipelines.  
- Correlates telemetry, code, and deployment data to find root causes.  
- Extensible through MCP, allowing it to call external tools (e.g., Wiz) without custom development.

## Wiz MCP
- Provides a unified, graph‑powered security view that links infrastructure, identities, data, AI components, and runtime activity.  
- The Wiz MCP Server is a standardized gateway that lets the DevOps Agent query the security graph for vulnerability data, exposure analysis, and threat detections.  
- Example: Agent sees a CPU spike on an EC2 instance; Wiz can tell whether the instance has an exploitable CVE, is internet‑exposed, and has endpoint protection.

## Combined triage scenarios
- **Scenario A – No security findings**: Agent queries Wiz, sees full monitoring, no vulnerabilities, no threats → treat as pure operational issue.  
- **Scenario B – Security issue detected**: Agent finds a validated remote‑code‑execution CVE, internet exposure, active exploitability → isolate immediately, involve security team.  
- **Scenario C – Coverage gap**: Resource is not represented in Wiz → Agent flags missing security context, prompting onboarding of the resource into Wiz.

## Integration workflow (MCP bridge)
- When an alert triggers, the DevOps Agent identifies affected resources and automatically calls Wiz’s MCP endpoint.  
- Calls are made during evidence collection; no separate manual step is required.  
- Data sent: only resource identifiers; no operational telemetry is shared with Wiz.  
- Example MCP tools invoked:
  - `list_cloud_resources` – checks if Wiz monitors the resource.  
  - `list_findings` – returns all finding types (vulnerabilities, misconfigurations, secrets, etc.).  
  - `list_vulnerability_findings` – provides CVE details, severity, exploitability.  
  - `list_issues` – prioritized risk issues, including toxic combinations.  
  - `list_threats` / `list_malware_findings` – active threats such as cryptomining or backdoors.  
  - `list_detections` – recent anomalous activity signals.  
  - `get_green_agent_analysis` – AI‑generated remediation steps.  
- All queries run through a single security‑auditing skill; results return in seconds.  
- If the MCP server is unreachable or returns an error, the agent proceeds with operational data and records the missing security context (Scenario C).  
- Full audit logs show which MCP tools were called and the data returned.

## Benefits and handling failures
- The agent classifies each incident based on returned data:
  - **No findings** → operational issue, normal triage.  
  - **Compromised or at‑risk** → active threats, exploitable CVEs, or toxic combinations → apply security runbooks, isolate resource, attach Wiz Green Agent remediation.  
  - **Unmonitored** → flag coverage gap for onboarding.  
- Integration provides immediate security context, reduces MTTR, and enables correct response paths without manual tool switching.