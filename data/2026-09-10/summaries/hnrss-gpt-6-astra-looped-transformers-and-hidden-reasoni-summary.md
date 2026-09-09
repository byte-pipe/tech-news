---
title: GPT-6 Astra, Looped Transformers, and Hidden Reasoning
url: https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and
date: 2026-09-09
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-10T07:21:53.930308
---

# GPT-6 Astra, Looped Transformers, and Hidden Reasoning

# GPT-6 Astra, Looped Transformers, and Hidden Reasoning

## 1. GPT‑6 Astra impressions
- Astra was released with strong fanfare and feels like the best model the author has used so far.  
- It outperforms GPT‑5.6 across writing, math, coding, and especially 3‑D rendering and animation.  
- Benchmarks:
  - Achieves 99.9 % on the ARC‑AGI‑3 benchmark (GPT‑5.6 scored 7.8 %).  
  - Strong results on coding and math benchmarks; details posted on the Astra release blog.  
  - Leads the Artificial Analysis Coding Agent Index v1.4 and ranks high on the broader Artificial Analysis Intelligence Index, though gains are not always “leaps and bounds.”  
- Independent benchmark harnesses (GDPval‑AA, AA‑Briefcase, Terminal‑Bench, τ³‑Banking) provide more trustworthy apples‑to‑apples comparisons, but model training often optimizes for a primary harness, which can affect cross‑harness scores.  
- Recommendation: consider pruning or regenerating old instruction files (e.g., `AGENTS.md`, `SKILL.md`) because newer models may solve tasks more efficiently without extensive hand‑holding.

## 2. Computer‑use capabilities
- Astra excels at image‑related tasks and can operate graphical user interfaces (GUIs) through the Codex/ChatGPT app.  
- Demonstrations include:
  - Rendering a 3‑D model of New York City in Blender.  
  - Redrawing a portrait in a browser‑based MS Paint using the mouse cursor (Medium and High settings).  
- This ability to control software directly is a newer, less mature capability compared to text‑only tasks, but it enables impressive visual demos and expands practical utility (e.g., “Hey ChatGPT, please do my tax return”).  
- The author likens GUI interaction to humanoid robots: less efficient than specialized tools but far more versatile.

## 3. Computer‑use training
- OpenAI reportedly purchased tens of thousands of Mac Minis and Mac Studios to expose models to macOS during training.  
- Macs are not used for raw GPU training; they provide an operating‑system environment for the model to learn tool usage.  
- Simplified training loop:
  1. Prompt the model with a task (e.g., “open app X and do Y”).  
  2. The model interacts with the macOS environment, receiving visual and state feedback.  
  3. Reinforcement learning updates the model to improve tool‑use behavior.  
- This approach aims to embed computer‑use skills directly into the model’s reasoning pipeline.

## 4. Looped Transformers (recurrent depth)
- “Looped transformers” refer to architectures where transformer blocks are applied repeatedly to the same hidden state, effectively creating depth through recurrence rather than stacking distinct layers.  
- Potential benefits:
  - Allows a single set of parameters to process information iteratively, reducing model size while preserving expressive power.  
  - May enable the model to refine its internal representation across multiple passes, akin to a chain‑of‑thought process.  
- Open questions:
  - Whether looping inherently hides the reasoning trace or merely compresses it.  
  - How loop depth interacts with external tool use and whether it improves or complicates interpretability.

## 5. Hidden reasoning and chain‑of‑thought
- Rumors suggest Astra “hides” its chain‑of‑thought, meaning the intermediate reasoning steps are not exposed in the final output.  
- Possible mechanisms:
  - The looped transformer may collapse multiple reasoning steps into a compact hidden state that is not directly emitted.  
  - Training objectives that reward concise answers could discourage explicit step‑by‑step exposition.  
- Implications:
  - Harder for users to audit or verify the model’s logical process.  
  - May improve response speed and token efficiency but at the cost of transparency.

## 6. Recent research highlights
- New papers explore:
  - Formal analysis of looped transformer dynamics, showing convergence properties under certain conditions.  
  - Techniques for extracting latent reasoning chains from recurrent hidden states (e.g., probing classifiers, attention visualizations).  
  - Benchmarks that specifically test hidden‑reasoning detection, revealing that current methods only recover a fraction of the internal steps.  
- The author emphasizes that these studies are early‑stage but provide valuable insight into how looping architectures could shape future LLM capabilities.