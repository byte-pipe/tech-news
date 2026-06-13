---
title: GitHub - TencentCloud/TencentDB-Agent-Memory: TencentDB Agent Memory delivers fully local long-term memory for AI Agents via a 4-tier progressive pipe...
url: https://github.com/TencentCloud/TencentDB-Agent-Memory
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-06-13T11:45:27.190833
---

# GitHub - TencentCloud/TencentDB-Agent-Memory: TencentDB Agent Memory delivers fully local long-term memory for AI Agents via a 4-tier progressive pipe...

# TencentDB Agent Memory
=========================

## Key Points

* TencentDB Agent Memory is an innovative solution that combines symbolic short-term memory and layered long-term memory to improve AI agent performance.
* It offloads heavy log processing, reducing token usage by up to 61.38%.
* Integration with OpenClaw improves task success rate by 51.52% and increases PersonaMem accuracy from 48% to 76%.

## Memory Capability

### Benchmark Results

| Metric | OpenClaw | Plugin | Contextualization | Improvement |
| --- | --- | --- | --- | --- |
| Success Rate | 33.3% | 48.4% | 64.2% | +51.52% |
| Token Usage | -61.38% | 85.64% | -30.98% | -33.09% |
| PersonaMem Accuracy | 44.0% | 76.0% | -19.95% | +7.95% |
| SWE-bench Performance (SS) | 58.4% | 64.2% | -23.31% | +9.93% |
| AA-LCR Performance (AP) | 42.8% | 76.0% | -34.19% | +59% |

## Overview
----------

Memory is a crucial aspect of AI agent performance, but it should be optimized for sustainable and efficient processing. TencentDB Agent Memory addresses this challenge by providing a novel solution that improves task success rates, increases accuracy, and reduces token usage.

TencentDB Agent Memory outperforms conventional approaches, such as log offloading and irreversible summarization. Instead, it utilizes symbolic short-term memory and layered long-term memory to minimize context redundancy and maximize past experience retention.