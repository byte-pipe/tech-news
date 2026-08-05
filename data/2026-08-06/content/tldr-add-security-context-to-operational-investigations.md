---
title: Add security context to operational investigations with AWS DevOps Agent and Wiz | AWS DevOps & Developer Productivity Blog
url: https://aws.amazon.com/blogs/devops/add-security-context-to-operational-investigations-with-aws-devops-agent-and-wiz/
site_name: tldr
content_file: tldr-add-security-context-to-operational-investigations
fetched_at: '2026-08-06T07:11:25.055473'
original_url: https://aws.amazon.com/blogs/devops/add-security-context-to-operational-investigations-with-aws-devops-agent-and-wiz/
date: '2026-08-06'
published_date: '2026-07-29T05:33:53-07:00'
description: Add security context to operational investigations with AWS DevOps Agent and Wiz (7 minute read)
tags:
- tldr
---

## AWS DevOps & Developer Productivity Blog

# Add security context to operational investigations with AWS DevOps Agent and Wiz

This post was co-authored by Ayelet Harcz (Product Manager), Hen Perez (CTO Architect), and Shani Gafni (Product Manager) at Wiz.

When an on-call engineer receives an alert at 2 AM, a CPU spike, a latency anomaly, or an unexpected API error, the first question is whether this is an operational issue or a security incident. A CPU spike could be a scaling problem or a cryptominer. A latency anomaly could be a bad deployment or data exfiltration. Without security context in the investigation loop, engineers lack the information to distinguish between the two, delaying resolution and increasing risk.

AWS DevOps Agentis a frontier agent that autonomously investigates incidents and identifies operational improvements across AWS, multicloud, and on-premises environments. It reduces mean time to resolution (MTTR) by performing the triage and investigation work that would otherwise take an on-call engineer hours of manual effort. With theWizintegration, AWS DevOps Agent queries Wiz’s security graph during investigations through theModel Context Protocol (MCP), surfacing vulnerability data, security findings, and exposure analysis alongside operational telemetry so engineers can quickly determine whether an alert is a performance issue or a security incident.

In this post, we walk through how the integration works, demonstrate a real-world incident investigation where AWS DevOps Agent uses Wiz MCP to surface a critical vulnerability behind an API latency spike, and show how to configure the integration in your environment. If you already use Wiz to secure your AWS environment, this integration puts your existing security data to work during incident investigations.

## AWS DevOps Agent

AWS DevOps Agent investigates incidents and identifies operational improvements as an experienced DevOps engineer would: by learning your resources and their relationships, working with your observability tools, runbooks, code repositories, and CI/CD pipelines, and correlating telemetry, code, and deployment data across all of them. For a deeper look at how it works, seeHow AWS DevOps Agent uses multi-agent reasoning to find root causes.

AWS DevOps Agent is extensible through MCP, which allows the agent to call external tools during its investigation without requiring custom development. This is the mechanism that makes the Wiz integration possible. When the agent identifies a resource under investigation, it queries Wiz MCP for security findings associated with that resource and incorporates the results into its analysis and recommendations.

## Wiz MCP

Wizis designed to secure cloud and AI applications through a unified, graph-powered platform. TheWiz Security Graphconnects infrastructure, identities, data, AI components, and runtime activity into a single contextual view. This approach identifies toxic combinations across layers – where exposures, permissions, data access, AI vulnerabilities, and runtime behaviors intersect in ways attackers can realistically exploit.

TheWiz MCP Serveracts as a standardized gateway that allows AWS DevOps Agent to query this security graph during investigations. Wiz knows whether your Amazon Elastic Compute Cloud (Amazon EC2) instance has an exploitable Common Vulnerabilities and Exposures (CVE), whether it is publicly exposed, and whether endpoint protection is in place. AWS DevOps Agent, looking at the same instance, knows that CPU spiked, and a deployment happened 20 minutes ago. Separately, each tool tells a partial story. Together, they give the engineer the complete picture needed to act.

## Better together: how combined context changes triage

The value of this integration is easiest to understand through three scenarios. Each starts with the same operational signal: a CPU spike on an EC2 instance.

Figure 1 – AWS DevOps Agent sees operational telemetry, Wiz sees security posture. The combination changes the triage decision.

Scenario A: No security findings.A CPU spike fires on an instance. AWS DevOps Agent queries Wiz and confirms the instance is fully monitored, has no known vulnerabilities, and shows zero active threat detections. This is an operational issue. The engineer scales, investigates the deployment, tests, and moves on.

Scenario B: Security issue detected.The same CPU spike fires, the same Amazon CloudWatch alarm triggers, and the same engineer wakes up. But when AWS DevOps Agent queries Wiz, it finds a validated remote code execution vulnerability on that instance, confirmed exploitable, with the resource exposed to the internet. The operational symptoms are identical to Scenario A. The correct response is the opposite: isolate immediately, engage your security team, treat this as a potential compromise.

Scenario C: Wiz coverage gap.The resource isn’t in Wiz at all. AWS DevOps Agent includes this as a finding in the investigation report, noting that no security context was available for the resource. Your team can then address the coverage gap by onboarding the resource into Wiz.

Without the Wiz integration, all three scenarios look the same in your dashboard. With it, AWS DevOps Agent routes each to the correct response path before a human needs to context-switch between tools.

## How the integration works: the MCP bridge

The integration uses MCP, the same protocol AWS DevOps Agent uses for many of its external tool connections. When the agent identifies affected resources during an investigation, it calls Wiz’s remote MCP server as part of its evidence collection – no separate step, no manual trigger. The security query happens alongside the operational investigation, not after it. During the MCP call, AWS DevOps Agent sends resource identifiers to Wiz’s MCP endpoint and receives security findings in response. No operational telemetry or broader investigation context is shared with Wiz.

Figure 2 – The investigation flow: operational alert triggers AWS DevOps Agent, which queries Wiz via MCP before reaching a triage decision.

During the MCP call, AWS DevOps Agent queries Wiz tools to build a complete risk picture of the affected resource, here are a few examples:

Wiz MCP Tool

What it tells the agent

list_cloud_resources

Whether Wiz monitors this resource at all (coverage check)

list_findings

All finding types in one call: vulnerabilities, misconfigurations, secrets, data, and host config

list_vulnerability_findings

Deep CVE detail – severity, fix version, and exploitability (CISA KEV / known exploit)

list_issues

Prioritized risk issues, including toxic combinations (internet-facing + no Endpoint Detection and Response (EDR) + exploitable CVE)

list_threats / list_malware_findings

Active threats and malware: cryptomining, data exfiltration, backdoors

list_detections

Recent threat detection signals and anomalous activity

get_green_agent_analysis

AI-generated remediation steps for the issues found

The agent runs these queries together through a single security-auditing skill that loads automatically when it connects to Wiz’s MCP server with the DevOps toolset, so the full security picture comes back in seconds. If the Wiz MCP server is unreachable, times out mid-query, or returns an authentication error, the agent continues its investigation with the operational data it has and flags the missing security context in the investigation findings (Scenario C). You can review exactly which MCP tools were called and what data was returned in the AWS DevOps Agent investigation log for full auditability.

Based on what comes back, the agent classifies the situation: no security findings (operational issue, proceed normally), compromised or at-risk (active threats, exploitable vulnerabilities, or toxic combinations – apply relevant security runbooks to isolate the resource or escalate to security, withWiz Green Agentremediation steps attached), or unmonitored by Wiz (flag and close the coverage gap). The classification feeds directly into the investigation findings your team receives.

The following demonstration shows AWS DevOps Agent investigating a reported CPU spike. The agent queries Wiz MCP and identifies a critical, internet-exposed Remote Code Execution (RCE) under active exploitation – turning an ambiguous alert into a confirmed security incident.

Video 1 – AWS DevOps Agent investigates a CPU spike and uses Wiz MCP security context to identify a critical RCE exploited through a public endpoint

## Getting started

### Prerequisites

To use AWS DevOps Agent with Wiz MCP, you need:

1. An active AWS DevOps Agent configuration with at least one Agent Space
2. A Wiz tenant with a remote MCP server endpoint (Streamable HTTP transport)
3. Authentication credentials for the Wiz MCP server. AWS DevOps Agent supports multiple MCP auth methods; for Wiz, use a Wiz service account (Client ID and Secret) or OAuth. Choose the method that matches your Wiz MCP server configuration. For setup details, seeConnect remote Wiz MCP serverin the Wiz documentation (requires Wiz login)

### Enabling the integration

#### Step 1: Register the Wiz MCP server at account level

1. Sign in to the AWS Management Console and navigate to theAWS DevOps Agent console.
2. Go to the Capability Providers page from the side navigation.
3. Find MCP Server in the Available providers section and choose Register.
4. Enter the Wiz MCP server details:* Name: e.g., “Wiz Security”
* Endpoint URL:https://mcp.app.wiz.io/?toolset=devops
* Description: e.g., “Wiz security context for incident triage”
5. Choose Next.
6. Select the authentication method that matches your Wiz MCP server configuration.
7. Review your configuration and choose Submit. AWS DevOps Agent validates the connection to the Wiz MCP server. Upon successful validation, the server is registered at the account level.

#### Step 2: Allowlist Wiz tools in your Agent Space

1. In the AWS DevOps Agent console, select your Agent Space.
2. Go to the Capabilities tab.
3. In the MCP Servers section, choose Add.
4. Select the registered Wiz MCP server.
5. Select all the Wiz MCP tools.
6. Choose Add.

#### Step 3: Choose how the Wiz security audit runs

Pick one of three options:

1. Use the Wiz skill tool (recommended).With the Wiz MCP tools allowlisted, AWS DevOps Agent automatically runs the latest devops_resource_auditing_skill workflow from Wiz during investigations. You always get the most up-to-date version, maintained by Wiz.
2. Import the ready-made skill.Import the wiz-security-context skill from theAWS DevOps Agent skills repodirectly into your Agent Space. It is a lightweight skill that calls the Wiz workflow for you, so you get a one-step setup that stays current with Wiz.
3. Create your own custom skill.Use AWS DevOps Agent’s Create skill with Chat to build a custom skill based on the devops_resource_auditing_skill workflow and tailor it to your environment. This lets you review and tailor the workflow to your environment.

For detailed MCP configuration guidance, refer to theAWS DevOps Agent documentation on connecting remote MCP servers.

## The power of co-build: extending context through MCP

This integration started from a recurring customer question: how do I know if what I’m seeing is an operational problem or an active attack? We worked with Wiz to close this gap. AWS DevOps Agent provides operational investigation and reasoning; Wiz provides cloud security intelligence. MCP provided the integration path without either side needing to reimplement what the other already does well.

Because AWS DevOps Agent supports connecting remote MCP servers as a first-class extension mechanism, co-building new integrations withAWS Partnersfollows a repeatable pattern. Each integration adds a new dimension of context to the agent’s reasoning, and you benefit without writing custom code or middleware on your side. For example, connecting a change management MCP server would let the agent correlate deployment approvals with incident timing, adding change context alongside security context.

For you, this means the richer the toolset you run in your environment, the more context the agent brings to each investigation. Your existing investments get amplified rather than duplicated, and you benefit each time you connect a new partner MCP server to your Agent Space.

## Conclusion

Operational incidents and security incidents often start with the same symptoms. The difference between the right response to each is context that lives in a different tool than the one that fired the alert. The AWS DevOps Agent and Wiz integration brings that context into the investigation loop automatically through MCP.

To get started, visit theAWS DevOps Agent consoleand follow thegetting started guide. To learn more about Wiz’s MCP server, seeIntroducing the MCP Server for Wiz.

Wizis anAWS PartnerandAWS Marketplace Sellerproviding cloud security across the full development lifecycle. If you’re not already using Wiz, you can get started through theAWS Marketplace.

## About the Authors