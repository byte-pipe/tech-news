---
title: Anthropic Adds Enterprise Gateway to Simplify Claude Code Access on AWS and Google Cloud - DevOps.com
url: https://devops.com/anthropic-adds-enterprise-gateway-to-simplify-claude-code-access-on-aws-and-google-cloud/
site_name: tldr
content_file: tldr-anthropic-adds-enterprise-gateway-to-simplify-clau
fetched_at: '2026-07-07T19:36:57.079164'
original_url: https://devops.com/anthropic-adds-enterprise-gateway-to-simplify-claude-code-access-on-aws-and-google-cloud/
author: Tom Smith
date: '2026-07-07'
published_date: '2026-07-01T12:09:29+00:00'
description: Anthropic's new Claude apps gateway brings SSO, central policy, and spend caps to Claude Code on Amazon Bedrock and Google Cloud.
tags:
- tldr
---

Anthropic introduced a self-hosted gateway this week that lets enterprises run Claude Code on Amazon Bedrock and Google Cloud without the credential sprawl and manual setup that have typically come with deploying AI coding tools at scale.

The Claude apps gateway is a single, stateless container that organizations deploy on their own infrastructure and back with a PostgreSQL database. It centralizes identity, policy enforcement, usage tracking, and spend management for Claude Code, addressing a problem that will sound familiar to anyone who has tried to roll out a developer tool across a large engineering org: Every new hire needs a cloud credential, every laptop needs the right settings pushed to it, and finance needs a way to see who’s spending what.

Before the gateway, none of that was centralized. IT teams provisioned a credential per developer, manually distributed configuration, and stitched together separate tooling just to get visibility into spend. That’s a lot of overhead for something that should be straightforward.

### What the Gateway Actually Does

The gateway sits between developers and the underlying model infrastructure, handling five things:

Identity.The gateway acts as an OpenID Connect relying party, working with Google Workspace, Microsoft Entra ID, Okta, or any standards-compliant OIDC provider. It issues short-lived sessions instead of long-lived secrets stored on developer machines — a meaningful security improvement in its own right. Onboarding a new developer means adding them to the identity provider. Offboarding means removing them. No credential cleanup, no orphaned API keys floating around.

Policy.Admins define managed settings once, on the server. Clients pick up that policy automatically at sign-in, and the gateway enforces it on every request. Allowed models and default settings can be adjusted centrally, rather than chasing down individual machine configurations.

Telemetry.Every request is stamped with a usage metric, which the gateway relays via OTLP to a collector controlled by the organization. That data remains on the company’s own infrastructure and is subject to its retention schedule.

Routing.The gateway holds the upstream credential and routes inference traffic to the Claude API, Amazon Bedrock, or Google Cloud, with optional failover between providers.

Spend caps.Organizations can set daily, weekly, and monthly limits that apply at the org, group, or individual level.

Anthropic built the gateway into the sameClaudebinary developers already installed, so the/loginflow is gateway-aware out of the box. Settings apply automatically at sign-in, and policy gets enforced consistently without extra configuration on the client side.

Worth noting what the gateway doesn’t do: it doesn’t send inference traffic or usage data to Anthropic unless an organization specifically configures it to use the Claude API. For Bedrock or Google Cloud deployments, that data stays put. Anthropic is also publishing the protocol that the gateway uses, enabling other gateway developers to build compatible implementations.

### Why This Matters for Engineering Teams

For platform and DevOps teams, the appeal here is less about any single feature and more about consolidation. Identity, policy, telemetry, routing, and cost control have typically required separate tooling, separate dashboards, and separate processes to keep in sync. Folding all of that into a single container that an organization already controls significantly reduces the operational surface area.

It also addresses a real friction point in AI tool rollouts: the gap between what security and finance teams need (visibility, control, audit trails) and what developers want (a tool that just works without jumping through credential hoops). The gateway’s SSO-based onboarding and offboarding model handles both at once.

Mitch Ashley, VP and practice lead for software lifecycle engineering and AI-native software engineering atThe Futurum Group, sees this as a significant shift in who controls the control layer. “Enterprise identity, policy, cost attribution, and spend caps now ship as first-party infrastructure for Claude Code,” he said. “The model provider is claiming the access and cost layer that third-party gateways and in-house tooling used to hold.”

Ashley also flagged the bigger question platform teams need to ask. “For platform teams, the real question is whether per-vendor gateways or a neutral control point govern a multi-model estate,” he said. “This makes one coding tool manageable at scale. It does not govern what agents do, and that is the control problem that still decides enterprise autonomy.”

### Getting Started

Deployment involves downloading the Claude Code CLI binary and pointing agateway.yamlconfiguration file at the organization’s OIDC issuer and upstream credential, and registering one OIDC app with the identity provider. Rolling it out to client machines means setting theforceLoginMethodandforceLoginGatewayUrlparameters inmanaged-settings.json. Clients connect to the gateway automatically on first boot.

The gateway is available now, with full documentation on Anthropic’s developer site.

For organizations already running Claude Code through Bedrock or Google Cloud — or considering it — this is the kind of infrastructure update that doesn’t change what the tool does, but changes how manageable it is to run at scale. That’s often the difference between a pilot program and something engineering leadership is willing to stand behind.

 
 
 
 
 
 
* Tom Smith
 
 
 
 
 
 

 

« OpenAI Expands Into Developer Hardware With Codex Micro Keyboard
Ornith Models Automate Agentic Coding With Self-Scaffolding »