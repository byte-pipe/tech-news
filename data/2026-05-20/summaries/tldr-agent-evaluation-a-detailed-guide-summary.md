---
title: Agent Evaluation: A Detailed Guide
url: https://cameronrwolfe.substack.com/p/agent-evals
date: 2026-05-20
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-20T06:02:36.154555
---

# Agent Evaluation: A Detailed Guide

# Agent Evaluation: A Detailed Guide

## Fundamentals of Agent Systems
- Modern LLMs can handle complex, multi‑step tasks through reasoning, multimodality, and tool use, giving rise to **agents**.
- Core characteristics that distinguish agents from plain LLMs:
  - Structured reasoning over long horizons
  - Ability to call external tools or APIs
  - Solving complex, multi‑step problems
  - Error recovery and self‑correction
  - Acting autonomously on behalf of a user
- Agents operate within an **agentic loop**, continuously assessing intermediate results, invoking tools, and adjusting actions without external prompting.
- Autonomy level: unlike conventional LLMs that produce a single output, agents manage their workflow over time and can modify their environment (e.g., schedule events, book tickets).

## Components of an Agent
1. **Underlying LLM (or reasoning model)**
   - Serves as the brain, judging progress and deciding next steps.
2. **Tools**
   - APIs, CLIs, or services the agent can invoke to interact with the external world.
3. **Instructions**
   - Explicit prompts or system messages that define expected behavior and tool usage.

### Input‑Output Signature
- Conventional LLMs: simple text‑to‑text prompt → response.
- Agents extend this interface by embedding tool‑related tokens within the generation stream, allowing seamless tool invocation.

## Tool Use in Practice
- Tools must be:
  - Well‑documented and purpose‑clear
  - Minimally overlapping with other tools
  - Able to recover gracefully from errors
- Design check: *Would a human engineer be able to use this tool from the provided documentation?*
- Example (Qwen3 model) demonstrates XML‑style special tokens:
  - `<tool>` … `</tool>` – defines tool specifications.
  - `<tool_call>` … `</tool_call>` – encapsulates a specific tool invocation with JSON payload.
  - `<tool_response>` … `</tool_response>` – contains the result returned by the tool.
- Workflow:
  1. System message lists available tools and their JSON schemas.
  2. During generation, the model outputs a `<tool_call>` token.
  3. Generation pauses, the request is parsed, the tool is executed, and the response is inserted.
  4. Generation resumes with the tool result in context, enabling the model to continue reasoning.

## Evaluation Implications
- Effective evaluation requires realistic harnesses that mimic real‑world usage, especially for high‑stakes domains like coding and medicine.
- Rigorous, systematic measurement (rather than anecdotal checks) accelerates improvement of agent capabilities.
- The guide outlines a framework and case studies for building custom agent benchmarks, emphasizing reproducibility and relevance to practical deployments.