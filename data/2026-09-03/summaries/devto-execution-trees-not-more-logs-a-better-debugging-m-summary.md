---
title: Execution Trees, Not More Logs: A Better Debugging Model for AI Agents - DEV Community
url: https://dev.to/raju_dandigam/execution-trees-not-more-logs-a-better-debugging-model-for-ai-agents-3d4g
date: 2026-09-02
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-09-03T07:21:12.157835
---

# Execution Trees, Not More Logs: A Better Debugging Model for AI Agents - DEV Community

# Execution Trees, Not More Logs: A Better Debugging Model for AI Agents

## The problem with flat timelines
- Flat logs list events with timestamps but hide causal relationships, especially when agents are nested, tools run in parallel, or logs are interleaved.  
- Developers need to know the execution path, not just the order of events.

## Execution trees as a solution
- Trees make parent‑child relationships explicit, showing which steps belong together.  
- They are a projection of raw trace data, answering the common question: *What path did this run take?*

## Instrumentation with AgentInspect
- Provides `inspectRun` and `step` wrappers in TypeScript to mark runs, named steps, tool calls, and LLM calls.  
- Example code demonstrates manual instrumentation of a travel‑planner agent.  
- Recorded traces can be viewed locally with `npx agent-inspect view travel-planner --dir .agent-inspect --summary`.

## Four tree shapes that reveal bug classes
1. **Nested work** – Indentation shows ownership; a failure can be traced to its higher‑level step.  
2. **Fallbacks** – Tree retains both the failed primary path and the successful recovery path, highlighting degraded dependencies.  
3. **Retries** – Repeated sibling nodes expose retry attempts and their cost, enabling checks on call limits.  
4. **Parallel siblings** – Sibling nodes indicate concurrent execution; durations are not additive.

## Trees are a view, not the whole evidence model
- The underlying trace contains identifiers, timestamps, inputs/outputs, observations, and metadata.  
- Different projections are needed for various questions:  
  - `tree` → what path happened?  
  - `check` → did an invariant hold?  
  - `diff` → what changed between runs?  
  - `report` → what should a reviewer read?  
  - `bundle` → what evidence can be shared?

## From suspicious shape to deterministic check
- Encode observed invariants (e.g., maximum retry count) as CLI checks:  
  `npx agent-inspect check travel-planner --dir .agent-inspect --preset trajectory --required-tool search-flights --fail-on-observation failed`.  
- The experimental `TraceContractAPI` allows richer rules (tool requirements, forbidden tools, max calls, ordering, duration limits, token ceilings) for CI gating.

## Limitations of execution trees
- Trees do not verify answer correctness, relevance of retrieved documents, or freshness of tool results.  
- They are strongest for structural questions:  
  - Which operations ran?  
  - Which operation owned a failure?  
  - Was a fallback or retry used?  
  - Which work happened as siblings?  
  - Where did a run stop?

## Recommended workflow
1. Inspect the execution tree.  
2. Identify a stable behavioral invariant.  
3. Encode it as a deterministic check.  
4. Keep human judgment for context‑dependent analysis.