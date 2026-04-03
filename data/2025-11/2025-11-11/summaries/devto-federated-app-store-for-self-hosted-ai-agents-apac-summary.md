---
title: Federated app store for self-hosted AI agents (Apache-2.0) - DEV Community
url: https://dev.to/agentsystems/federated-app-store-for-self-hosted-ai-agents-apache-20-19ka
date: 2025-11-05
site: devto
model: llama3.2:1b
summarized_at: 2025-11-11T11:14:19.724714
screenshot: devto-federated-app-store-for-self-hosted-ai-agents-apac.png
---

# Federated app store for self-hosted AI agents (Apache-2.0) - DEV Community

**Federated App Store for Self-Hosted AI Agents**
=============================================

Key Points:

* **Design philosophy**: Build self-hosted agent infrastructure using existing tools and open-source software.
* **Architecture**: Federation of Git-based index, container isolation, and egress proxy with credential injection and model abstraction.
* **Key components**:
 + Federated Git-based index
 + Container isolation and egress proxy
 + Credential injection (API keys on the host, not in agent images)
 + Model abstraction (supports various input/output interfaces)
 + Hash-chained audit logs

Maintaining Original Perspective:

The self-hosted app store for AI agents leverages existing technologies to build a decentralized infrastructure, eliminating dependence on third-party services. This approach simplifies deployment and reduces costs.

**Federated Git-based Index**

* A distributed index of built agents, allowing for efficient discovery
* Forks ownership ensures transparency and maintainability

**Container Isolation + Egress Proxy**

* Containerization enables secure distribution of AI models and data
* Egress proxy controls access to agents, ensuring compliance with organizational policies

**Credential Injection**

* API keys are configured on the host, not in agent images, increasing security
* This approach prevents tampering with agent behavior

**Model Abstraction**

* Supports various input/output interfaces, making it easy to deploy custom models
* Works with Ollama local and cloud APIs, as well as hybrid solutions

**Open-Source and Pre-Release**

* The platform is built using Apache-2.0 open-source software and features a pre-release status.

**Repository**

* GitHub: `agentsystems/agentsystems`
* Documentation available at `docs.agentsystems.ai`

**Looking for**

* **Agent builders**: To participate in the community by publishing agents to the index.
* **Security researchers**: To review and improve the architecture, ensuring it meets organizational security standards.
