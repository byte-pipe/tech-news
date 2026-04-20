---
title: AI Helping Build Better AI: How Agents Accelerate Model Experimentation
url: https://www.linkedin.com/blog/engineering/ai/ai-helping-build-better-ai-how-agents-accelerate-model-experimentation
date: 2026-03-31
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-31T01:03:54.734414
---

# AI Helping Build Better AI: How Agents Accelerate Model Experimentation

# AI helping build better AI: How agents accelerate model experimentation

## Overview
- A new shift is emerging where AI is used not only to create user‑facing products but also to improve the infrastructure, training workflows, and optimization systems that build AI itself.
- The first clear example appeared in August 2025 with agent loops that optimized large‑language‑model post‑training runs, demonstrating a loop of proposing changes, testing, measuring, and iterating.

## Project and Unified Strategy (January 2026)
- An internal project was launched on the premise that AI can help build better AI and that platforms must be designed for agents at their core.
- The strategy unifies three pillars into a single experimentation framework:
  1. **Agents for code authoring** focused on distributed training.
  2. **Evaluation systems** that measure correctness, quality, and overall progress.
  3. **GPU microscheduling** for efficient compute utilization.
- Agents run parallel model trials with minimal human input on an interactive dev machine (inner loop) while the outer loop scales the chosen architecture via distributed training.

## Autopilot for Torch
- Applied first to LinkedIn’s large fleet of TensorFlow models, the goal was to produce equivalent or better PyTorch versions.
- Autopilot for Torch is an iterative agent that refines conversions step‑by‑step using LLM reasoning and verifier feedback; it is not a one‑time converter.
- The same pattern expanded to kernel generation, auto‑tuning, and other performance‑critical code generation tasks.

## Core Loop: Generate → Verify → Refine
- The agent follows an iterative **generate → score → hint → regenerate** cycle.
- Each iteration is validated against explicit quality gates; the verifier returns concrete, actionable fixes rather than a simple “fail.”
- Once metrics are met, the PyTorch implementation is validated on development GPU pods and promoted to production via Flyte workflows.
- Representative use cases:
  - Framework migration (TensorFlow → PyTorch).
  - Model code generation directly from labeled datasets.
  - Autoresearch experimentation (searching architecture, embedding size, scaling settings).
  - Kernel generation and optimization for LLM and recommendation‑system workloads.

## Scoring and Reward Design
- The system follows “trust, but verify.” The scoreboard defines what “good” means and drives the agent’s optimization.
- Evaluation hierarchy:
  1. **Functional correctness** – hard gate; code must run, learn, and remain stable.
  2. **Behavioral parity** – outputs must match expected semantics on representative inputs.
  3. **Structural fidelity** – key components and design patterns must be present.
  4. **Code style / platform fit** – adherence to target engineering conventions and APIs.
  5. **Task‑level metrics** – application‑specific objectives such as model quality, latency, throughput, or efficiency.
- Early iterations use cheap checks (structural, style); later iterations introduce stronger gates (trainability, IO parity, numerical stability).
- Example rubric for model code evaluation:
  1. Trainability – runs, backpropagates, remains numerically stable, converges.
  2. IO parity – matches source model behavior on identical inputs.
  3. Structural fidelity – preserves architecture and modeling patterns.
  4. Code style / platform fit – aligns with target conventions and APIs.
  5. Task metric parity – maintains downstream quality metrics (e.g., AUC).

## Reinforcement from the Verifier
- The verifier supplies structured natural‑language feedback that acts as both rubric and coach.
- Feedback includes:
  - **Typed failure mode** (e.g., NO_GRADIENT, NUMERICAL_INSTABILITY, METRIC_GAP).
  - **Priority level** (P1 for critical issues, P4 for minor refinements).
  - **Actionable suggestion** describing the exact fix.
- This feedback informs the agent which parts are already correct and which need correction, preventing unnecessary rewrites and accelerating convergence.

## Impact
- Agent‑driven loops dramatically reduce manual effort, increase iteration speed, and improve reliability of generated AI infrastructure.
- By unifying code generation, rigorous verification, and reward‑driven reinforcement, the framework enables scalable, production‑ready AI system building.
