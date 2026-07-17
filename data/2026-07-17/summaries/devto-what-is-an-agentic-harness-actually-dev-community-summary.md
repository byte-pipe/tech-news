---
title: "What is an \"agentic harness,\" actually? - DEV Community"
url: https://dev.to/googleai/what-is-an-agentic-harness-actually-4oie
date: 2026-07-16
site: devto
model: llama3.2:1b
summarized_at: 2026-07-17T11:38:17.284694
---

# What is an "agentic harness," actually? - DEV Community

# What is an Agentic Harness?

## Definitions

- **Simon Willison's definition**: an agent with tools running in a loop to accomplish its goal, relying on context not present in training.
- **Function calling**: using built-in mechanisms like function pointers or closures to interact with the environment.

## The Agent Loop

- An agent checks its own output against expectations; if fails, continues until correct or decided to stop.
- This self-audit aspect is crucial as it ensures goals are met without explicit human intervention.

## The Harness: Context and Interaction

- **The harness** isn't a separate app (interface) but the underlying plumbing that governs interaction with the external environment.
- Allows agents to adapt, respond, or change their behavior in new contexts without being explicitly rewritten.
- No specific harness-specific framework is required; many existing frameworks can be adapted.

## Examples of Harnesses

- Some self-driving cars use an "invisible" harness (e.g., sensors, cameras) to interact with the environment.
- Language models like LLMs may utilize various harnesses to process and incorporate external information into their outputs.