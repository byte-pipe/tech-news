---
title: Code Review (As We Know It) Must Die - Alex Looney
url: https://alexlooney.substack.com/p/code-review-as-we-know-it-must-die
date: 2026-08-03
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-03T20:03:37.034042
---

# Code Review (As We Know It) Must Die - Alex Looney

# Code Review (As We Know It) Must Die – Summary

## Problem Overview
- AI boosts development speed, but code review becomes the limiting factor.  
- Symptoms: slowed velocity, declining code quality, more production outages, engineer burnout.  
- The 20‑year‑old async, diff‑centric review process was built for a context that no longer exists.

## Why the Current Process Fails
- **Writing cheap, reviewing expensive** – agents generate code cheaply, while human review remains slow and costly.  
- **Diffs lack intent** – reviewers must reconstruct design, intent, and system context from raw line changes, a tax that grows with agent‑produced code.  
- **Uniform ceremony** – every change, from trivial tweaks to critical logic, receives the same level of human scrutiny, causing risky changes to be under‑reviewed and trivial ones to clog the queue.

## Traditional Jobs of Code Review
1. Catch defects before they ship.  
2. Keep the codebase maintainable and consistent.  
3. Spread knowledge across the team.  
4. Serve as a control and authorization gate.  
5. Enforce team norms and taste.

## How Those Jobs Change with AI Agents
- **Defect detection** → automated checks, independent AI reviewers, and human validation of tests rather than line‑by‑line inspection.  
- **Maintainability** → line‑level readability matters less (AI can explain code instantly); architectural quality becomes the primary focus.  
- **Knowledge sharing** → intent, design, and context are communicated up front; code is consulted on demand via AI, not forced reading at merge time.  
- **Norm enforcement** → moved upstream into specifications, linters, and agent training.  
- **Control** → the merge gate remains, but confidence comes from high‑level decision review, AI checks, and risk routing rather than diff reading.

## Remaining Human‑Centric Work
- Verify the change at an abstraction level: confirm intent, design decisions, and that the implementation delivers the intended outcome.  
- Prevent bottlenecks: ensure human review time scales with the volume of agent‑generated code.  
- Steer the system: inject human taste, guide architecture, and course‑correct agents.

## Proposed New Process
1. **Align on design before code exists** – resolve what to build and how it fits the system; this is where human judgment adds value.  
2. **Surface the change, not the diff** – provide a high‑level description of decisions and implementation, with code attached as supporting material.  
3. **Run an adversarial AI pass** – independent AI reviewers hunt for what the coding agent missed before any human looks.  
4. **Show the evidence** – present test results, rollout data, or other proof that the change works as intended.  
5. **Route by risk** – low‑risk changes auto‑approved after automated checks; human attention focuses on high‑impact changes.  
6. **Absorb mistakes in the system** – use staged rollouts, fast rollbacks, and monitoring; a named human still owns the merge but does not read every line.

## Implications
- Human approvers sign off based on decisions, AI verification, and risk assessment, not on line‑by‑line diffs.  
- The process shifts from diff inspection to validation of intent, architecture, and system impact, allowing agent velocity to scale without overwhelming human reviewers.