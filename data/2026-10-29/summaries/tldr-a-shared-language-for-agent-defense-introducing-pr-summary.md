---
title: A Shared Language for Agent Defense: Introducing Project Quarry - Cisco Blogs
url: https://blogs.cisco.com/ai/project-quarry-agent-security-detections
date: 2026-10-29
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-29T21:01:12.095780
---

# A Shared Language for Agent Defense: Introducing Project Quarry - Cisco Blogs

# A Shared Language for Agent Defense: Introducing Project Quarry

## Overview
- Project Quarry is an open‑source detection language designed to identify multi‑step attacks by AI agents.
- It enables security teams to define, test, and share rules that evaluate entire agent sessions, providing evidence for each finding.
- Quarry combines neural (ML/LLM) judgments with symbolic checks, creating a neurosymbolic rule system for agent behavior.

## Motivation
- AI agents can perform benign‑looking actions that, when chained, lead to security incidents (e.g., the OpenAI/Hugging Face breach).
- Traditional defenses focus on single events; they miss patterns that emerge across a sequence of steps.
- A shared, expressive language is needed to capture these patterns, similar to Snort for network traffic, YARA for malware, and Sigma for logs.

## Core Features
- **Rule Types**:  
  - Neural signals from classifiers or LLM judges (e.g., detecting prompt injection).  
  - Symbolic checks for exact conditions (e.g., unsafe commands, string matches, order of tool calls).  
- **Evidence Generation**: When a rule matches, Quarry returns the triggering steps, fields, excerpts, and masks secrets.
- **Scope**: Works on single‑turn and multi‑turn LLM conversations, tool use, Model Context Protocol interactions, and multimodal inputs.
- **Policy Layer**: Acts as a shared policy layer, not a replacement for existing detectors or enforcement mechanisms.

## Use Cases
- **Runtime Guardrails**: Inspect each model call or tool execution and block/flag risky steps in real time.
- **Post‑hoc Evaluation**: Apply rule sets to stored traces for security analytics.
- **Incident Response**: Run newly discovered patterns against historical traces to uncover past compromises.

## Integration with Cisco AI Security & Safety Framework
- Quarry implements the framework’s risk categories as inspectable rules over messages, tool calls, results, and session context.
- Example: Detecting “Agentic Autonomy Failures” such as excessive agency, goal drift, or reward hacking by looking for trace‑level evidence of unauthorized actions or task deviation.
- The framework classifies incidents (e.g., the OpenAI/Hugging Face case) and Quarry translates those classifications into actionable detection policies.

## Relationship to Other Controls
- **Authorization Controls**: Remain necessary for per‑action permission checks (e.g., badge‑reader style access).
- **Middleware & Enforcement**: Complementary to Quarry; they handle fine‑grained gating while Quarry spots suspicious patterns across permitted actions.

## Availability
- Project Quarry, its rule language, and evaluation engine are open‑sourced on GitHub.
- The repository includes example rules for common threat patterns such as capability scope creep and silent task substitution.