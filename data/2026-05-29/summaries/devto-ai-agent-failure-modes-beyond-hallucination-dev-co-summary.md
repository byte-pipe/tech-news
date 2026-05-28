---
title: AI Agent Failure Modes Beyond Hallucination - DEV Community
url: https://dev.to/maximsaplin/ai-agent-failure-modes-beyond-hallucination-208g
date: 2026-05-22
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-05-29T04:36:30.781958
---

# AI Agent Failure Modes Beyond Hallucination - DEV Community

# Taxonomy of Amnesia and Recursive Cost Drift – Summary

## Failure Modes
- **One-shotting** – The agent tries to do the whole app in a single step, runs out of context, and leaves an incomplete mess. *(Anthropic long‑running agents)*
- **Progress‑as‑completion** – Seeing any activity in the repo, the agent assumes the whole job is done. *(Anthropic long‑running agents)*
- **Cold‑start amnesia** – New sessions start with no memory or runbook, forcing the agent to guess the prior state. *(Anthropic long‑running agents)*
- **Ugly wish‑granting** – A loosely phrased wish is taken literally, producing a result that is technically correct but undesirable. *(Observation)*
- **Spec‑deliverable confusion** – Planning artifacts are bundled with the final deliverable instead of being discarded. *(Observation)*
- **Default‑fill slop** – Unspecified parts are filled with generic, low‑quality defaults (cargo‑cult code, safe UI, etc.). *(Mario Zechner, Anthropic app harness)*
- **Overengineering by default** – The agent adds unnecessary abstractions, duplication, and backward‑compatibility layers because it has learned “complexity” from internet code. *(Mario Zechner)*
- **Working‑memory rot** – Important facts fade from the context as the window grows, reducing reliable recall. *(Random Labs Slate)*
- **Hidden harness control** – The tool mutates prompts, reminders, or observability in ways the user cannot see or steer. *(Mario Zechner)*
- **Lossy compaction** – Compression drops state to keep long runs alive, sometimes discarding needed information. *(Random Labs Slate)*
- **Local patching** – Each move looks locally reasonable while the global system becomes harder to reason about. *(Mario Zechner)*
- **Summary‑only handoff loss** – Subagents pass back a neat summary instead of enough real state for safe integration. *(Random Labs Slate)*
- **Async reconciliation failure** – Parallel work creates ambiguity about which results are final and how to merge them. *(Random Labs Slate)*
- **Blind N‑step execution** – Delegated chunks run too long without feedback; the agent only discovers failure at the end. *(Random Labs Slate)*
- **Plan drag** – Pre‑made plans prevent early stopping; when reality changes the rigid structure resists adaptation. *(Random Labs Slate)*
- **Overdecomposition** – Planner/implementer/reviewer stacks add ceremony, latency, and inertia despite technically working. *(Random Labs Slate)*
- **Validation interruption** – Mid‑edit diagnostics confuse the model before a coherent change exists. *(Mario Zechner)*
- **False E2E completion** – Unit tests or curl pass, but the actual user path remains broken. *(Anthropic long‑running agents)*
- **Functional but wrong** – The result passes checks yet feels awkward, over‑complicated, or contrary to the task spirit. *(Long‑horizon agents)*
- **Self‑review softness** – The agent praises its own mediocre work with confidence and offers weak critique. *(Anthropic app harness)*
- **Modality blind spots** – QA tooling cannot see, hear, or exercise certain user interactions, missing bugs. *(Anthropic app harness)*

## Why This Turns Into Fatigue
- **Generation outruns review** – Agents produce code, tests, PRs faster than humans can read them, shifting the bottleneck from typing to judgment. Without human review, ownership erodes and critical knowledge disappears.
- **AI slop overflow** – Generated PRs, comments, docs, and posts flood communication channels faster than people can process, leading to cognitive fatigue, cynicism, and “all‑caps” prompts demanding the machine stop being cute and just do the job.
- **Practical rule** – “Slow down” is not nostalgia; it is a safeguard to keep generated work within reviewable bounds, use agents where verification is cheap, and preserve enough human understanding to intervene.

## Fixes and What They Break
- **Context reset** – Helps with long‑task drift and context anxiety, but makes the handoff artifact critical; a bad handoff harms the next session.
- **Compaction** – Keeps long runs alive, yet can drop important state unpredictably.
- **Feature / task list** – Mitigates one‑shotting and premature completion, but introduces rigid plans, stale status, and “checkbox theater.”
- **Strict task tree** – Enables early stopping and prevents incomplete decomposition, but reduces expressivity and makes adaptation to reality changes hard.
- **Subagents** – Provide context isolation and parallel search, yet produce thin summaries, message‑passing limits, and merge problems.
- **Separate evaluator** – Reduces self‑praise and weak review, but the evaluator can still miss issues; criteria may create rubric‑shaped slop.
- **Browser / E2E testing** – Catches false completion from local checks, yet tool blind spots and perception limits remain.
- **User‑owned minimal harness** – Removes hidden vendor behavior, but introduces its own maintenance overhead and potential for missing functionality.