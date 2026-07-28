---
title: GitHub - UditAkhourii/adhd: ADHD — a skill for coding agents. Tree-of-thought with pruning, built on the Claude & Codex Agent SDK. Fans out parallel d...
url: https://github.com/UditAkhourii/adhd
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-07-28T11:46:16.368893
---

# GitHub - UditAkhourii/adhd: ADHD — a skill for coding agents. Tree-of-thought with pruning, built on the Claude & Codex Agent SDK. Fans out parallel d...

## ADHD: A Skill for Coding Agents

* **Problem Statement:** A coding agent designed to mimic an individual with Attention Deficit Hyperactivity Disorder (ADHD) requires an adaptive approach to simulate cognitive patterns and reasoning architectures.
* **Background:** Researchers have long struggled to replicate the complex thinking mechanisms exhibited by individuals with ADHD. This framework is an architectural fix for premature convergence in autoregressive reasoning, providing a structured yet flexible system for cognitive simulation.
* **Key Features:**
  * Tree-of-thought approach, allowing agents to dynamically explore different cognitive frames and evolve over time
  * Anchoring mechanism, which persists across branches of thought
  * Evaluation strategy, involving multiple evaluative cycles to score and prune traps
  * Critic pass on divergence, enhancing learning from experiences
* **Design Decisions:**
  * Initial design decisions focused on establishing a coherent framework for cognitive simulation
  * Evaluating strategies based on expert input (Google SRE Book ch. 22), recognizing the complexities of human cognition
    + Implementing hybrid strategy combining four progressive-timing concepts:
      - **Timeout**: A 10-second timeout with staged UI elements
      - **Retry/Exponential Backoff**: Two-stage retry algorithm with exponential backoff for excessive failures
      - **Hedged Parallel Requests**: Streaming with keepalive reduces network activity and reduces risk of errors
      - **Streaming with Keepalive**: Continuously updates the state with user input, making decisions based on updated knowledge
* **Real-world Impact:** Demonstrates how a specialized AI system can mimic human cognitive patterns by incorporating:
  * Efficient time management (e.g., staged UI)
  * Effective error handling using retry and exponential backoff mechanisms
  * Adaptive learning through hybrid criteria for evaluation

This adaptation aims to provide a foundational framework for modeling the intricacies of brain function in computational systems, enabling the development of sophisticated AI agents that can simulate adaptive behaviors inspired by ADHD.