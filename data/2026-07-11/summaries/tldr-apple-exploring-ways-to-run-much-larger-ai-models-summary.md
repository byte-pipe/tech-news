---
title: Apple Exploring Ways to Run Much Larger AI Models Directly on iPhones - MacRumors
url: https://www.macrumors.com/2026/07/09/apple-prismml-larger-on-device-ai-models/
date: 2026-07-11
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-11T01:37:59.601489
---

# Apple Exploring Ways to Run Much Larger AI Models Directly on iPhones - MacRumors

# Apple Exploring Ways to Run Much Larger AI Models Directly on iPhones

## Overview
- Apple is meeting with startup PrismML to explore using its technology for running far larger AI models on iPhone hardware.  
- PrismML reportedly compressed Alibaba’s open‑source LLM Qwen 3.6 (27 billion parameters) to run fully on an iPhone 17 Pro.  

## Comparison with Apple’s Current On‑Device Model
- Apple’s AFM 3 Core Advanced model (used in iOS 27) has 20 billion parameters but employs a sparse architecture: only 1–4 billion parameters are active at any moment.  
- PrismML’s implementation keeps all 27 billion parameters active simultaneously, offering a denser, potentially more capable model.  

## Potential Benefits
- Running larger models on‑device could expand Apple Intelligence features without relying on Apple’s Private Cloud Compute servers.  
- On‑device processing may lower operational costs and enhance user privacy by keeping data local.  

## Technical Insight (from comments)
- A commenter suggests PrismML may be using a one‑bit‑per‑parameter compression technique, drastically reducing memory footprint and energy consumption.  
- This approach could allow even Apple’s 10‑billion‑parameter models to fit within the limited RAM of current iPhones (e.g., 6 GB in iPhone 15).  

## Related Coverage
- **The MacRumors Show** – recap of WWDC 2026 announcements, including Siri AI and new Apple Intelligence features.  
- **Advanced AI Dictation** – iOS 27 beta introduces AI‑powered dictation that isn’t enabled by default.  
- **Apple Intelligence Home Features** – iOS 27 Home app features require a 2 TB iCloud+ plan.  

## Community Reaction (selected comments)
- Some users express skepticism about the AI hype and its relevance.  
- Others highlight hardware limitations (RAM) that have historically constrained on‑device AI.  
- A few commenters are intrigued by the compression method, noting potential energy and performance gains.