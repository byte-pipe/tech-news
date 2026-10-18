---
title: AI Agent Beats ARM CMSIS-NN by 3.74x on nRF54LM20 - Hackster.io
url: https://www.hackster.io/maxxlife/ai-agent-beats-arm-cmsis-nn-by-3-74x-on-nrf54lm20-66158a
date: 2026-10-18
site: tldr
model: llama3.2:1b
summarized_at: 2026-10-18T14:25:17.152259
---

# AI Agent Beats ARM CMSIS-NN by 3.74x on nRF54LM20 - Hackster.io

# AI Agent Beats ARM CMSIS-NN by 3.74x on nRF54LM20

## Summary

An autonomous gemini-4-argon Hardware-in-the-Loop (HIL) agent wrote a kernel on Cortex-M33F that outperforms official ARM CMSIS-NN s4. The agent used Google AI Studio, Google Gemini API, and Nordic Semiconductor nRF Connect SDK to achieve this improvement.

## Things Used in the Project

* Nordic Semiconductor nRF54LM20 DK
* Google AI Studio
* Google Gemini API
* Nordic Semiconductor nRF Connect SDK

## Story

The agent was inspired by the Google ML Drift philosophy, which pushed the limits of open-source GPU inference engine. Inspired by its core design principles, the agent used low-level hardware roofline profiling to measure exact memory bandwidth (GB/s), compute throughput (GFLOP/s), and identify hardware bottlenecks per layer.

The agent also used block-wise 4-bit quantization (INT4, group_size=32 / Q4_0) to compress weights down to 4 bits with per-group scales, allowing it to fit LLM and TinyML weights inside tight on-chip caches.

## Engineering Patterns

The key engineering patterns used in the project include:

* From Google ML Drift to Microcontrollers
* Architecture of the Autonomous HIL AI Agent (agent.py)
* Five Engineering Patterns That Made Agent.py Work in Production
* The Workload: MAC-Smasher & INT4 (Q4_0) Math
* Evolution of the INT4 Kernel: 5 Sprints with gemini-4-argon
* Sprint 5 (v0.7 — Final Silicon Record): 64-bit LDRD + FPU Register File Hijacking (VMOV)