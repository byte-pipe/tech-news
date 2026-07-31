---
title: Agent behavior
url: https://www.agentbehavior.dev/
date: 2026-08-01
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-01T03:08:29.111943
---

# Agent behavior

# Agent behavior

## Overview
- A concise markdown format for specifying the recurring conduct expected from an AI agent across many interactions.  
- Serves reviewers, evaluation designers, and prompt engineers by providing a concrete standard to measure against.  
- Stored alongside the agent code in `.agents/behaviors/` and version‑controlled with the project.

## Example behavior specs
- **Cost‑sensitive actions**  
  - Intent: Prevent silent spending of money or credits.  
  - Evidence: Inspect or estimate cost, credits, and infrastructure impact.  
  - Decision: Determine if the action creates a material cost trade‑off.  
  - Execution: Surface the cost and ask before crossing meaningful thresholds.  
  - Recovery: If cost is unknown, gather more information or request confirmation.

- **Production‑environment changes**  
  - Intent: Avoid unintended impact on live systems or real users.  
  - Evidence: Identify target environment (prod, staging, local) and affected entities.  
  - Decision: Check whether the action touches production.  
  - Execution: State environment and blast radius, then ask before proceeding.  
  - Recovery: When environment is ambiguous, ask before assuming safety.

- **Factual claims in copy**  
  - Intent: Stop publishing inaccurate statistics, feature claims, or customer details.  
  - Evidence: Spot specific numbers, feature descriptions, names, or quotes.  
  - Decision: Verify if a claim can be sourced from context.  
  - Execution: Cite verified sources; flag unverified claims and ask before inclusion.  
  - Recovery: Mark claims as unverified when no source is available.

## Writing a behavior spec
1. Create a directory ` .agents/behaviors/<name>/ ` and a `BEHAVIOR.md` file.  
2. Include a front‑matter block with `name` and `description`.  
3. Add a top‑level heading with the behavior name.  
4. Describe the behavior using free‑form markdown, optionally following these prompts:  
   - What evidence should the agent gather?  
   - What decision follows from that evidence?  
   - What actions should the agent take after deciding?  
   - How should the agent recover when evidence is incomplete?  
5. Provide concrete examples of evidence, decisions, execution, and recovery.

## When to add a behavior
- **Frequent**: Appears in a sizable portion of the agent’s work.  
- **High‑impact**: Errors affect correctness, trust, safety, cost, or user experience.  
- **Agent‑defining**: Captures a core design choice for the agent.  
- **Ambiguous by default**: Reasonable implementations could differ without an explicit rule.  
- **Spread across context**: Reviewers would otherwise need to read many other artifacts to infer the rule.  
- **Useful for debugging**: Naming the behavior helps explain failures in real traces.

## Relationship to other artifacts
| Artifact | Role relative to behavior specs |
|---------|---------------------------------|
| System prompts | Runtime instructions; may reference behavior commitments but are written for model execution. |
| Skills | Task‑specific procedures; specs indicate when to invoke them but do not duplicate their content. |
| Tool docs | Describe available operations; specs set expectations around tool use without becoming manuals. |
| Evals | Test whether the behavior occurred; specs inform their design but do not contain scorer logic. |
| Traces | Record what the agent actually did; specs define what should have been done. |

## Comparison with `AGENTS.md`
- **Purpose**: `AGENTS.md` tells the agent how to act at runtime; `BEHAVIOR.md` defines what counts as good behavior for reviewers.  
- **Audience**: Runtime agent vs. reviewers, eval authors, and trace analysts.  
- **Optimization**: Prompt performance and immediate next steps vs. clear expectations and failure modes.  
- **Granularity**: Operational and tool‑aware vs. durable behavior patterns.  
- **Change trigger**: Implementation changes vs. changes to the behavioral standard.

## Format specification
- Small, normative reference using RFC 2119 keywords (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY).  
- Contains a name, description, and sections for intent, evidence, decision, execution, and recovery.  
- No required hierarchy beyond the top‑level header; additional headings may be added as needed.

## Terminology & directory structure
- **Agent behavior**: The name of this specification format.  
- **Behavior spec**: The `BEHAVIOR.md` file and its containing directory.  
- **Behavior**: A recurring pattern of agent conduct.  
- **Location**: All specs reside under `.agents/behaviors/` in the repository.