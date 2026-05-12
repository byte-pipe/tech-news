---
title: Interaction Models: A Scalable Approach to Human-AI Collaboration - Thinking Machines Lab
url: https://thinkingmachines.ai/blog/interaction-models/
date: 2026-05-12
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-13T06:03:09.087320
---

# Interaction Models: A Scalable Approach to Human-AI Collaboration - Thinking Machines Lab

# Interaction Models: A Scalable Approach to Human‑AI Collaboration

## Overview
- We announce a research preview of **interaction models** that handle audio, video, and text natively, enabling real‑time, continuous collaboration between humans and AI.  
- The goal is to make interactivity scale together with intelligence, moving beyond turn‑based, post‑hoc interfaces.

## The Collaboration Bottleneck
- Current AI research prioritizes autonomous, long‑running agents, treating human‑in‑the‑loop as an afterthought.  
- Turn‑based interfaces force the model to wait for a complete user input before responding, and freeze perception while generating, limiting bandwidth and collaborative richness.  
- Effective work often requires **copresence**, **contemporality**, and **simultaneity**—qualities missing from most existing systems.  
- Hand‑crafted harnesses (e.g., voice‑activity detection, separate dialog managers) are brittle and will be outpaced by general AI capabilities.

## Our Solution
- Build interactivity **into the model itself** rather than as an external scaffold.  
- Adopt a **multi‑stream, micro‑turn design** that aligns inputs and outputs in 200 ms slices, allowing overlapping speech, visual cues, and silent back‑channeling.  
- Combine a **time‑aware interaction layer** (real‑time perception and response) with an **asynchronous background layer** for deeper reasoning, tool use, and long‑horizon tasks.

## Capabilities Unlocked
- **Seamless dialog management**: the model implicitly tracks speaker intent (thinking, yielding, self‑correcting) without a separate manager.  
- **Verbal and visual interjections**: can interrupt or respond mid‑utterance based on context.  
- **Simultaneous speech**: supports concurrent speaking, e.g., live translation.  
- **Time awareness**: understands elapsed time and can act accordingly.  
- **Concurrent tool use**: can search the web, browse, or generate UI elements while maintaining the conversation flow.

## Architectural Contrast
- **Turn‑based**: inputs and outputs flattened into a single token sequence (human → model → human …).  
- **Micro‑turn based**: continuous streams split into short, time‑aligned slices, preserving silence, overlap, and interruption as part of context.

## System Overview
- The interaction model maintains a constant two‑way exchange, processing multimodal signals in real time.  
- When a task exceeds the immediate interaction window, the asynchronous background model takes over for sustained reasoning and tool integration, feeding results back into the live stream.

## Implications
- By embedding interactivity, scaling the model improves both intelligence **and** collaborative ability.  
- This approach aligns AI interfaces with how humans naturally collaborate—through ongoing, multimodal conversation rather than isolated prompts.