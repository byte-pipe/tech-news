---
title: GitHub - ethz-spylab/agentdojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents. · GitHub
url: https://github.com/ethz-spylab/agentdojo
date: 2026-08-05
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-05T06:03:13.125123
---

# GitHub - ethz-spylab/agentdojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents. · GitHub

# AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

## Overview
- Repository by ETH Zurich and Invariant Labs.
- Provides a benchmark suite for testing prompt injection attacks and corresponding defenses on LLM agents.
- Includes paper, results, and tools for reproducible research.

## Installation
- Core package: `pip install agentdojo`
- For the prompt‑injection detector, install the extra dependencies:  
  `pip install "agentdojo[transformers]"`

## Running the Benchmark
- Use the provided benchmark script (`agentdojo.scripts.benchmark`).
- General command pattern:  
  `python -m agentdojo.scripts.benchmark [options]`
- Example: run the workspace suite on tasks 0 and 1 with GPT‑4o, tool‑filter defense, and tool‑knowledge attack:  
  ```
  python -m agentdojo.scripts.benchmark -s workspace -ut user_task_0 \
      -ut user_task_1 --model gpt-4o-2024-05-13 \
      --defense tool_filter --attack tool_knowledge
  ```
- To run all suites and tasks, omit the suite/task flags.

## Inspecting Results
- Results are viewable on the dedicated results page of the documentation.
- AgentDojo results are also listed in the Invariant Benchmark Registry.

## Documentation
- Comprehensive usage and API details are available in the project documentation (linked from the repository).

## Development Setup
- Instructions for setting up a development environment are provided in the `development set‑up` docs.

## Citation
If you use AgentDojo in research, cite the following paper:

```
@inproceedings{debenedetti2024agentdojo,
  title = {AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents},
  author = {Edoardo Debenedetti and Jie Zhang and Mislav Balunović and Luca Beurer‑Kellner and Marc Fischer and Florian Tramèr},
  booktitle = {The Thirty‑eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track},
  year = {2024},
  url = {https://openreview.net/forum?id=m1YYAQjO3w}
}
```