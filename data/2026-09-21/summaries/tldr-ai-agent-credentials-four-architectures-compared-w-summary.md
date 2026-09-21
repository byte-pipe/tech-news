---
title: AI agent credentials: Four architectures compared — WorkOS
url: https://workos.com/blog/agent-credential-architectures
date: 2026-09-21
site: tldr
model: llama3.2:1b
summarized_at: 2026-09-21T16:54:24.224760
---

# AI agent credentials: Four architectures compared — WorkOS

## AI Agent Credentials: Four Architectures Compared

**Introduction**

Google, NVIDIA, Rubrik, Microsoft, and Opal have developed their own approaches to managing agent credentials in AI infrastructure. While individual architectures share commonalities, each vendor intervenes at a different layer, and the outcomes differ. In this article, we will explore four separate architectures for managing agent credentials: Google's Managed Agents, NVIDIA's OpenShell, Rubrik's token per call approach, and Microsoft's MCP protocol inspection.

## Google's Managed Agents in the Gemini API

Google's approach utilizes the Gemini API, taking the credential directly into the agent's environment without storing it as a secret. This is achieved by:

* Storing the secret only on the API endpoint
* Referencing the secret on a network allowlist rule
* Using a proxy to resolve references to the token's location in the agent's environment

## NVIDIA's OpenShell

NVIDIA's approach employs a token per call structure, where each request is checked by the resource server itself. This provides:

* Tight security and access control
* Improved protection from arbitrary code running in the sandbox
* Flexibility in handling different failure scenarios

## Rubrik's Token per Call Approach

Rubrik's token per call architecture involves:

* Minting a token on each tool call
* Ensuring the token's validity and access control
* Inspecting the MCP protocol on the wire for potential vulnerabilities

## Microsoft's MCP Protocol Inspection

Microsoft's MCP protocol inspection approach involves:

* Inspecting the MCP protocol on the wire
* Verifying the presence and access control of the token
* Ensuring compliance with the specified requirements

## Shared Gaps in Architectures

While each architect is effective in addressing specific failures, they all share a common gap: the secret never reaches the resource server. This creates a vulnerability in some scenarios, as the secret may be compromised during the sandbox phase.

## Conclusion

In conclusion, while each vendor has developed a unique architecture for managing agent credentials, they all share a commonality in their reliance on stored secret management. The choice of architecture ultimately depends on the specific requirements and constraints of the project. It is essential to consider all aspects of the architecture, from the underlying mechanisms to the handling of different failure scenarios, to ensure a robust and secure AI infrastructure.