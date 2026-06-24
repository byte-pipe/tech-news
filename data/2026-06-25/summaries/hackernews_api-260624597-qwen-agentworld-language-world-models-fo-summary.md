---
title: [2606.24597] Qwen-AgentWorld: Language World Models for General Agents
url: https://arxiv.org/abs/2606.24597
date: 2026-06-24
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-25T05:57:27.482662
---

# [2606.24597] Qwen-AgentWorld: Language World Models for General Agents

# Qwen‑AgentWorld: Language World Models for General Agents

## Overview
- Introduces **Qwen‑AgentWorld**, the first large‑scale language‑based world models designed to simulate agentic environments across multiple domains.  
- Two model variants are released: **Qwen‑AgentWorld‑35B‑A3B** and **Qwen‑AgentWorld‑397B‑A17B**.  
- Built on >10 M real‑world interaction trajectories covering 7 distinct domains.  

## Model Architecture & Training Pipeline
- **Three‑stage training**:  
  - **CPT (Curriculum Pre‑training)** injects general world‑modeling abilities using state‑transition data and augmented professional corpora.  
  - **SFT (Supervised Fine‑tuning)** focuses on next‑state prediction through chain‑of‑thought reasoning.  
  - **RL (Reinforcement Learning)** refines simulation fidelity with a hybrid rubric‑and‑rule reward system.  
- Models generate long chain‑of‑thought predictions to capture complex dynamics and support reasoning‑heavy tasks.  

## Evaluation Benchmark – AgentWorldBench
- **AgentWorldBench** aggregates real‑world interaction data from 5 frontier models evaluated on 9 established benchmarks.  
- Provides a comprehensive, multi‑domain testbed for language world models.  

## Empirical Results
- Qwen‑AgentWorld consistently outperforms existing frontier models across all benchmark tasks.  
- Demonstrates superior simulation accuracy, reasoning depth, and generalization to unseen environments.  

## Applications of Language World Models
### 1. Decoupled Environment Simulator
- Serves as a scalable, controllable simulator for thousands of real‑world environments.  
- Enables agentic reinforcement learning that surpasses performance obtained from training solely in real environments.  

### 2. Unified Agent Foundation Model
- World‑model pre‑training acts as an effective warm‑up, boosting downstream performance on 7 agentic benchmarks.  
- Facilitates transfer learning and reduces data requirements for downstream tasks.  

## Contributions
- First language‑only world models capable of multi‑domain agentic simulation with chain‑of‑thought reasoning.  
- Novel three‑stage training pipeline integrating curriculum learning, supervised fine‑tuning, and RL‑based fidelity optimization.  
- Introduction of AgentWorldBench, a benchmark suite for systematic evaluation of language world models.  

## Availability
- Code and model checkpoints are released publicly (URL provided in the paper).  
- Intended to support further research in general‑purpose agents and language‑driven world modeling.