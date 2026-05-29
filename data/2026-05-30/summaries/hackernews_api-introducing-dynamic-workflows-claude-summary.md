---
title: Introducing dynamic workflows | Claude
url: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
date: 2026-05-29
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-30T06:02:23.011690
---

# Introducing dynamic workflows | Claude

# Introducing dynamic workflows in Claude Code

## Overview
- New feature lets Claude handle large, complex tasks end‑to‑end, shrinking timelines from quarters to days.  
- Claude writes orchestration scripts that run tens to hundreds of parallel subagents in a single session and verifies work before delivering results.

## Availability
- Research preview in Claude Code CLI, Desktop, and VS Code extension for Max, Team, and Enterprise (admin‑enabled) plans.  
- Also available via Claude API on Amazon Bedrock, Vertex AI, and Microsoft Foundry.  
- Consumes significantly more tokens than a typical session; start with a scoped task to gauge usage.

## How to use
- Enable auto mode for the best experience.  
- Start a workflow in two ways:  
  1. Directly ask Claude (e.g., “Create a workflow”).  
  2. Turn on the Claude Code‑specific setting **ultracode** through the effort menu, which sets effort to xhigh and lets Claude decide when to invoke a workflow.

## Use cases
- **Codebase‑wide audits**: bug hunts, profiler‑guided optimization, security checks; parallel search with independent verification of each finding.  
- **Large migrations**: framework swaps, API deprecations, language ports affecting thousands of files.  
- **Critical double‑checking**: independent attempts and adversarial agents test results before they reach the user.

## Customer feedback
- *Alessio Vallero, Senior Engineering Manager*: “Dynamic workflows have been especially valuable for discovery and review tasks across large codebases, identifying dead code and cleanup opportunities that static analysis missed.”  
- *Ken Takao, Lead Systems Engineer*: “Dynamic workflows fill the gap between a single subagent and a full agent team, allowing us to trust longer runs without losing visibility.”

## Example: Rewriting Bun with dynamic workflows
- Jarred Sumner ported Bun from Zig to Rust using dynamic workflows:  
  - Produced ~750 k lines of Rust with 99.8 % of the test suite passing.  
  - Completed in 11 days from first commit to merge.  
  - Workflow steps included mapping Rust lifetimes, generating .rs files in parallel with reviewers, iterative build/test fixing, and post‑port optimization PRs.

## Technical details
- Workflow initiation: Claude plans from the prompt, breaks it into subtasks, fans out parallel subagents, checks results, and iterates until answers converge.  
- Designed for long‑running jobs (hours to days); progress is saved for resumability.  
- Coordination occurs outside the conversation, keeping the plan on track regardless of task size.  
- Higher token usage; admins can disable workflows via managed settings.

## Getting started
- Enabled by default for Max, Team, and API users; Enterprise plans have it off by default (admin can enable).  
- Begin by asking Claude to create a workflow or enable the **ultracode** setting.  
- Detailed documentation is linked in the product interface.

## Additional resources
- Installation commands for Claude Code (bash and PowerShell).  
- Links to related product announcements (Code w/ Claude events, Managed Agents, legal industry use).  
- Pricing, sales contact, and developer newsletter subscription options.