---
title: Security and complexity slow the next phase of enterprise AI agent adoption - Help Net Security
url: https://www.helpnetsecurity.com/2026/02/24/ai-agents-business-processes-security-complexity/
date: 2026-03-05
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-05T06:02:21.122742
---

# Security and complexity slow the next phase of enterprise AI agent adoption - Help Net Security

# Security and complexity slow the next phase of enterprise AI agent adoption

## Overview
- 60 % of organizations have AI agents in production; building agents is a strategic priority.  
- Early deployments target internal workflows such as DevOps CI/CD optimization, security automation, general process automation, and code generation/review.  
- Adoption is strongest in telecommunications, financial services, and technology, while awareness of “agentic AI” remains uneven across the market.

## Main Barriers
### Security and compliance
- 40 % cite security and compliance as the primary obstacle to scaling agentic AI.  
- Challenges appear at three levels:  
  - **Infrastructure:** need for runtime isolation and sandboxing.  
  - **Operations:** exposure from coordinating models, APIs, and external systems.  
  - **Governance:** demand for stronger audit mechanisms and consistent policy enforcement.  
- Frequently mentioned risks: prompt injection, tool poisoning, vulnerability detection, credential management, and access‑control in distributed agent systems.

### Operational complexity
- 48 % identify the difficulty of orchestrating multiple components as the main challenge.  
- Integrating several models, connectors, and runtime environments raises monitoring and security‑team workload.

## Multi‑model architectures
- Almost all surveyed firms use more than one model; nearly half employ four to six models.  
- 61 % combine cloud‑hosted and locally hosted models to meet control, data‑privacy, and compliance requirements.  
- Hybrid and multi‑cloud deployments are common, but orchestration tooling is still immature for production use.

## Model Context Protocol (MCP)
- High awareness and active usage among practitioners.  
- Operational overhead includes managing MCP servers and clients, plus installation and configuration burdens.  
- Security concerns focus on prompt injection, tool poisoning, and the difficulty of handling authentication, credentials, and access controls.  
- Enterprise‑scale MCP deployment needs better discovery, manageability, and security governance.

## Distribution and vendor dependency
- Agent sharing is fragmented across commercial marketplaces, source‑code repositories, and informal internal processes.  
- Security is the top barrier to seamless sharing; respondents request signed and scannable agent packages, centralized registries, and built‑in policy enforcement.  
- 76 % worry about lock‑in to model‑hosting platforms, cloud providers, and monitoring layers; diversification of models and infrastructure adds coordination complexity.  
- Containers serve as the common operational foundation, with most organizations extending existing cloud‑native pipelines and orchestration practices to support agents.

## Outlook
- Near‑term value of agentic AI is already evident in internal workflows.  
- Unlocking the next wave depends on standardizing security, orchestration, and shipping processes on top of the container foundations that teams already use.  
- Organizations that invest now in this “trust layer” are positioned to scale agents from local productivity tools to durable, enterprise‑wide outcomes.