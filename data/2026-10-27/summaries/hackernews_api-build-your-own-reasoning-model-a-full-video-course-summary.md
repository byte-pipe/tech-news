---
title: Build Your Own Reasoning Model: A Full Video Course
url: https://magazine.sebastianraschka.com/p/building-reasoning-models
date: 2026-10-27
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-27T08:19:09.027308
---

# Build Your Own Reasoning Model: A Full Video Course

# Building Reasoning Models from the Ground Up: A Full Video Course

## Overview
- The article announces an eight‑video, 11‑hour coding series that builds reasoning models from scratch using Python and PyTorch.  
- It follows the author’s earlier “Build LLMs from Scratch” material and serves as a sequel, though prior knowledge is not mandatory.  
- The focus is on a pre‑trained Qwen‑3 model, adding evaluation, inference‑time scaling, reinforcement learning, and distillation.

## How LLMs, Reasoning Models, and Agents Relate
- A reasoning model extends a conventional LLM by applying post‑training (e.g., RL with verifiable rewards) and optional inference‑scaling techniques.  
- Historically aimed at math and code, reasoning models can generalize to other domains.  
- In an agent architecture, the reasoning model acts as the “engine,” while the agent harness provides context management and tool access.  
- Most current‑generation LLMs already include reasoning capabilities with adjustable effort levels.

## Resources Mentioned
- **Build a Large Language Model (From Scratch)** – book and videos.  
- **Build a Reasoning Model (From Scratch)** – book (Manning/Amazon) and the video series described here.  
- **Components of a Coding Agent** – article on Substack.  
- Optional preview: “AI Reasoning Models” course on LinkedIn Learning (≈90 min).

## Scope and Prerequisites
- **Model used:** small pre‑trained Qwen‑3 (0.6 B).  
- **Core topics:** evaluation, KV‑caching, inference‑time scaling, reinforcement learning, distillation.  
- **Required skills:** comfortable with Python and PyTorch; prior “Build LLM” content helpful but not required.  
- **Compute:** early chapters run on CPU; later training experiments benefit from a GPU. The first video covers hardware setup and environment recommendations.

## Companion Book
- The videos complement the book *Build a Reasoning Model (From Scratch)*.  
- Recommended workflow: read a chapter, follow the corresponding video, complete exercises.  
- The book is available in print (color) from Manning and Amazon.

## Video Lecture Outline
1. **Motivation and Code Setup**  
   - Relationship of LLMs, reasoning models, and agent harnesses.  
   - Benefits of learning through implementation.  
   - Installing dependencies, hardware selection, CUDA/Apple Silicon checks, remote GPU usage with VS Code.  

2. **Loading a Base Model, Text Generation, and KV Caching**  
   - Load Qwen‑3 0.6 B weights.  
   - Token encoding/decoding, tensor shapes, logits, next‑token prediction.  
   - Implement greedy decoding, streaming generation, EOS handling, speed measurement.  
   - Add KV cache and torch.compile, compare performance.  

3. **Building a Verifier for Evaluation and Reinforcement Learning**  
   - (Details continue in subsequent videos; focus on constructing evaluation metrics and RL loops.)  

4. **Inference‑Time Scaling Techniques**  
   - Methods to increase reasoning depth without retraining.  

5. **Reinforcement Learning with Verifiable Rewards**  
   - Designing reward functions, training loops, and stability tricks.  

6. **Distillation of the Reasoning Model**  
   - Compressing the enhanced model into a smaller, faster student model.  

7. **Integrating the Reasoning Engine into an Agent Harness**  
   - Context management, tool use, and API design for agents.  

8. **Final Project and Next Steps**  
   - End‑to‑end implementation recap, suggestions for further research, and upcoming content teaser.  

---  

Enjoy coding along, and stay tuned for more LLM research roundups next month.