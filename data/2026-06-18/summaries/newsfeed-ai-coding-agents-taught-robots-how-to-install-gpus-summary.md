---
title: AI coding agents taught robots how to install GPUs and cut zip ties - Ars Technica
url: https://arstechnica.com/ai/2026/06/ai-coding-agents-can-autonomously-direct-robot-training/
date: 2026-06-17
site: newsfeed
model: llama3.2:1b
summarized_at: 2026-06-18T12:26:43.276845
---

# AI coding agents taught robots how to install GPUs and cut zip ties - Ars Technica

# AI Directed Robot Training: A Framework for Autonomous Learning

AI coding agents can be taught to automate robot training with a comprehensive framework like ENPIRE, developed by NVIDIA GEAR researchers along with collaborators from Carnegie Mellon University in Pittsburgh and the University of California, Berkeley.

**Key Components**

*   **Autoreset and Verification**: The ENPIRE harness enables AI coding agents to automatically reset and verify tasks after each execution.
*   **Policy Refinement**: AI agents refine their policies based on real-world experiments and adapt them for parallel task execution across multiple robots.
*   **Failure Analysis**: AI agents analyze logs, ingest research papers, and improve training infrastructure and algorithm code in response to failures.
*   **Self-Improvement**: The framework includes a memory and context system that allows the AI agents to learn from their experiences and adapt over time.

**Experimentation with Different Algorithms**

The authors tested ENPIRE with three different AI coding agents:

*   OpenAI Codex (GPT-5.5)
*   Anthropic's Claude Code (Opus 4.7)
*   Moonshot AI's Kimi Code (Kimi K2.6)

These teams independently developed algorithmic approaches, tested them in real-world experiments, and evaluated their effectiveness.

## Success Rate and Limitations

The ENPIRE framework achieved an impressive success rate of 99% across various manipulation tasks. The most promising results came from the pin insertion and organization task, where robots successfully inserted GPUs into motherboards through self-improvement autonomous learning strategies.