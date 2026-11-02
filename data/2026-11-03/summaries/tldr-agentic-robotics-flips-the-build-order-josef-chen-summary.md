---
title: Agentic Robotics Flips the Build Order · Josef Chen
url: https://josef.cn/blog/agentic-robotics
date: 2026-11-03
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-11-03T06:07:55.783914
---

# Agentic Robotics Flips the Build Order · Josef Chen

# Agentic Robotics Flips the Build Order

## Overview
- **Agentic robotics** reverses the traditional robotics pipeline: a high‑level “System 2” model (a language model) writes the low‑level controller (“System 1”) code instead of training a policy first and then adding a planner.  
- This approach lets the generated code run autonomously on real robots, with the language model intervening only when the code fails.

## Key Demonstrations
- **FORCA (Claude Fable 5)**:  
  - Given only a camera view, wrote Python to open a transparent drawer 4/10 times.  
  - After adding wrist force sensing, iteratively refined its code to achieve 10/10 success, and continued working after the LLM was disconnected.  
- **GPT‑6 Astra (OpenAI)**:  
  - In the RoboDojo benchmark, with only a “move gripper” action and task recipes, achieved 22.5 % success—higher than any trained policy (19.3 %).  
  - Precision remained low (4 %) and thinking time was long (average 55 min per episode).  
- **PyRUA‑Lean**:  
  - Switched the planner from GPT‑5.5 to Astra, raising success from 0.88 % to 22.5 % without retraining the controller.  
  - Adding code‑generation tooling lifted performance to 51.6 %, more than double the best leaderboard score.  
- **Stanford HomeBody**:  
  - Controlled a Unitree G1 humanoid in an unseen kitchen, completing long‑horizon tasks (tidying, object retrieval) using Astra‑generated code.  

## Architectural Insight
- **System 2 (slow thinking)**: processes images and language at ~7–9 Hz, decides what to do, and outputs high‑level instructions.  
- **System 1 (fast thinking)**: runs at ~200 Hz, translates System 2’s instructions into motor commands.  
- In agentic robotics, System 2 *writes* the System 1 code, which then runs independently; the LLM is called back only as an exception handler.

## Economic and Industry Impact
- The shift mirrors the historic “robot brain” moment (GPT‑3 for NLP) now occurring in robotics.  
- Traditional robot cell costs (e.g., 2014 spot‑welding cell: $133 k total, $46 k for hardware/software) are dominated by installation and programming; agentic robotics aims to automate the programming phase.  
- Venture funding is aligning with this trend: Physical Intelligence raised a $20 billion round amid the Astra rollout.  

## Community Reaction
- Researchers (e.g., Ken Goldberg, Phillip Isola) note the potential for any internet‑connected robot to become a tool for LLMs.  
- Industry voices (e.g., Unitree founder Wang Xingxing) acknowledge past underestimation of AI’s role in robotics.  
- Open‑source efforts like ASPIRE (Jim Fan) claim near‑perfect benchmark performance after swapping in a frontier model.  

## Outlook
- The “reflex” concept—where a low‑level policy hands control back to a higher‑level model when errors arise—has been inverted: the high‑level model now creates the low‑level policy, and the reflex serves only as an exception handler.  
- Current bottlenecks include deliberation latency (Astra spends ~90 % of a run thinking) and precision on fine manipulation tasks.  
- Continued advances in code‑generation and tool‑use by LLMs are expected to drive further adoption of agentic robotics in manufacturing and beyond.