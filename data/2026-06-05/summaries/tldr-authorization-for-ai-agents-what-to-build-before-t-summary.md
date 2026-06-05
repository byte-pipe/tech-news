---
title: Authorization for AI Agents: What to Build Before the EU AI Act Deadline | Cerbos
url: https://cerbos.dev/blog/authorization-for-ai-agents-what-to-build-before-eu-ai-act-deadline
date: 2026-06-05
site: tldr
model: llama3.2:1b
summarized_at: 2026-06-05T12:05:14.418370
---

# Authorization for AI Agents: What to Build Before the EU AI Act Deadline | Cerbos

Here is a concise and informative summary of the article:

**Authorization for AI Agents: What to Build Before the EU AI Act Deadline**

### Identify 3 Key Challenges in Authorizing AI Agents
There are three layers to address: identity, audit (control and accountability), and orchestration (agent-to-tool communication).

*   **Addressing Identity**
    *   Each agent requires its own unique identity per instance, tied to a named human sponsor.
    *   Long-lived API keys for agents create problems when spawning new instances.
#### Examples of the issue:
    o   The EU AI Act deadline will make implementing these solutions challenging.
### Addressing Audit
*   After an agent delegates to a sub-agent, existing audit trails break down with unclear information about who consented and what was the original purpose.
*   **Improve Audit Functionality**
    *   Logs provide useful information but fail to tell you which human authorized specific actions across different chains.
#### Potential Solutions:
    o   Develop auditing policies and rules that don't rely on humans providing data.

### Focus on Orchestration
*   Today, the agent-to-tool layer is seen as the unknown territory with little maturity in categories.
*   **Defining Orchestration as a Category**
    *   Naming it marks it as a priority area for architectural work and addressing security concerns around trust enforcement.
#### Possible Architectural Solutions:
    o   Implement security frameworks that allow for policy control outside agents.

### Recommendations
To tackle the missing category for runtime policies in orchestration, build frameworks that enable separate policy engines to manage decisions made by actors (agents) on behalf of humans.