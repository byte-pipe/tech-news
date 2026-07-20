---
title: Robotics @ XIAOMI
url: https://robotics.xiaomi.com/xiaomi-robotics-1.html
date: 2026-07-20
site: hnrss
model: llama3.2:1b
summarized_at: 2026-07-20T12:00:32.201159
---

# Robotics @ XIAOMI

**Robotics @ XIAOMI**

**Scaling Robot Policy Models with Embodiment-Free Pre-Training**

Xiaomi-Robotics-1 is a pre-trained robot policy model that employs embodiment-free pre-training and post-training stages to address the scaling challenge faced by robotics.

**Data Sources:**

*   Large-scale embodiment-free (UMI) trajectories spanning over 1,700 scenarios (household, commercial premises, industrial sites, and outdoor spaces)
*   Modest amount of real-robot data in a post-training stage
*   Cross-embodiment datasets containing in-house robot data, filtered open-sourced robot data, and high-quality UMI data

**Methodology:**

1.  **Pre-training:** The model learns general representations for action generation from the large-scale UMI data. This is done using a pre-trained language model that is trained on vast amounts of natural language text.
2.  **Post-training:** The post-training stage aligns the model with real robot embodiments and instruction-following capabilities by fine-tuning it on in-house robot data, cross-embodiment datasets, and high-quality UMI data.

**Observations:**

*   Pre-training shows a clean scaling behavior as data and model size grow.
*   The post-training stage effectively leverages the in-house robot data to improve instruction-following capabilities and alignment.

Key Takeaways:

*   Embodiment-free pre-training addresses the scaling challenge faced by robotics.
*   Post-training refining improves the model's performance on real-world tasks and scenarios.
*   A robust pre-training pipeline is essential for effective scale-up of policy models in robotics.