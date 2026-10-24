---
title: An MCP governance checklist for the CTO | Amir Pournasserian
url: https://pournasserian.com/writing/mcp-buyer-governance-checklist
date: 2026-10-24
site: tldr
model: llama3.2:1b
summarized_at: 2026-10-24T14:37:20.959692
---

# An MCP governance checklist for the CTO | Amir Pournasserian

## An MCP Governance Checklist for the CTO

**Part 2: Specification Settlement, Policy Creation, and Gap Filling**

### Key Points

* The decision-making process of AI assistants is not in the servers' code, but rather in the hosts they operate.
* This includes identity management, access control, logging, and data usage.
* The Model Context Protocol (MCP) is an open standard that enables AI applications to interact with external tools, data, and template prompts.

### Key Issues and Decisions

* The specification settles:
 * Everything the model reads is potentially sensitive.
 * Three primitives have three deciders: model decision, application decision, user decision.
 * The host's duties are outlined: human in the loop, sensitive operations, tool inputs, validation, timeouts, and logging.
* Identity types are:
 * Enterprise-managed authorization uses identity from the identity provider.
* The main concern for CTOs is:
 * Which hosts use a host, its model, and tools; what access is granted; how results are validated.
* A register of approved servers with definitions and checks must be maintained.

### Where the Risk Enters

* Four zones:
  1. Hosts and models share the same security zone.
  2. Servers sit in their own backend zone.
  3. Data crosses between zones at three boundaries.
  4. Untrusted content from outside zones must be managed.

### Governance Considerations for CTOs

* Focus on:
 * Specification settlement (host and model responsibilities).
 * Policy creation (identification of which mechanisms can be used).
 * Gap filling (definition of approved servers, data management, etc.).

Recommended Practices:

* Hand a list to the CTO: specification, policy, and potential gaps.
* The CTO should:
 * Review and understand the specification.
 * Identify the required policies and potential gaps.
 * Create and maintain a register of approved servers.