---
title: GitHub - microsoft/AutoSaddler · GitHub
url: https://github.com/microsoft/AutoSaddler
date: 2026-08-28
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-28T17:06:38.993816
---

# GitHub - microsoft/AutoSaddler · GitHub

# AutoSaddler – Automatic Harness Optimization

## Highlights
- Optimizes full LLM‑agent harnesses (prompts, tool definitions, middleware, loop logic) via structured patches.  
- Deep diagnosis of execution traces to find root causes instead of shallow reflection.  
- Uses a patch taxonomy with a Capability‑to‑Steering schedule for controlled edits.  
- Generalization‑aware selection validates updates on unseen cases using an evolution DAG (EvoDAG).  
- Durable execution records immutable, append‑only events and supports resumable runs.

## News
- 2026‑08‑25: Added V2 support for optimizing the Meta‑ARE harness on GAIA2.  
- 2026‑08‑24: Paper released on arXiv v1 together with project website and short video.

## Installation
```bash
git clone https://github.com/microsoft/AutoSaddler.git
cd AutoSaddler
uv sync --extra dev
# run commands via `uv run`
```
Requirements: Python 3.12‑3.14, `uv`, and Git.

## Quick Start
```bash
uv run python -m autosaddler.v2.cli \
  --config configs/v2/local_template.yaml \
  --run-id local-template
```
Re‑running the command resumes the same run after input validation.

## Versions
- **V2 (current)** – Durable, plugin‑based engine documented in this README. Recommended for new users.  
- **V1 (legacy)** – Research‑quality implementation used for the paper experiments; kept for reproducibility.

## Repository Structure
```
AutoSaddler/
├─ configs/          # V1/V2 configs and benchmark manifests
├─ docs/             # Architecture and integration guides
├─ figures/          # README and paper figures
├─ scripts/          # Data provisioning and legacy launch scripts
├─ src/autosaddler/v1/  # Legacy code
├─ src/autosaddler/v2/  # Current engine, plugins, providers, storage
└─ tests/            # Characterization and V2 tests
```

## How It Works
AutoSaddler treats harness optimization as offline mini‑batch learning with three session types:

1. **Diagnosis‑Patch** – Inspects failed traces, proposes Capability (code/infrastructure) and Steering (behavior) patches.  
2. **Reflection** – Compares pre/post‑patch traces, classifies outcomes, and records reusable lessons.  
3. **Evolution** – Uses the full EvoDAG to synthesize new candidates from successful components across lineages.

Candidates are evaluated on sampled training cases and gated by a development split; the highest‑ranked development candidate is returned when the rollout budget is exhausted.

## Supported Harnesses & Benchmarks
| Harness | Space | Benchmark | Purpose |
|--------|-------|-----------|---------|
| `fake` | Structured component map | Synthetic cases | Local development and tests |
| `meta_are` | Git repository | GAIA2 | End‑to‑end smoke experiments |

V2 works with immutable, content‑addressed component maps and Git candidate spaces. Optimizer sessions can use the built‑in fake provider, Anthropic Claude SDK, or GitHub Copilot SDK. Additional harnesses (e.g., OpenClaw, Codex) and benchmarks (e.g., Terminal‑Bench) are planned.

## Configuration
All V2 configs start with `schema_version: autosaddler/v2`. A scenario plugin bridges the generic engine to a specific harness/benchmark pair and defines four ownership areas:

- **scenario** – Plugin type, immutable sources, datasets, evaluator, evidence, prompts, capabilities, reproducibility metadata.  
- **optimization** – Task selection, acceptance criteria, development gate, ranking, budget, retries, timeouts.  
- **provider** – Optimizer provider, model, endpoint, provider‑specific settings.  
- **storage** – Durable run root.

Key config files:
- `configs/v2/local_template.yaml` – Credential‑free deterministic template.  
- `configs/v2/meta_are_smoke.yaml` – Current Meta‑ARE/GAIA2 smoke integration.  
- Legacy V1 configs for full and bounded runs.

Runs are strict: a run ID can be reused only if all resolved inputs are byte‑identical; any change in source revisions, manifests, or settings is rejected.

## Reproducing the GAIA2 Smoke Run
1. **Prepare repositories** (sibling layout):
   ```
   <parent>/
   ├─ AutoSaddler/
   ├─ Meta-ARE/
   ├─ meta_are_data/
   └─ working_dir/
   ```
   ```bash
   cd ..
   git clone https://github.com/pshlego/Meta-ARE.git Meta-ARE
   git -C Meta-ARE checkout --detach 2419824a94fb8211fc8227ada7bff1b29f86e563
   mkdir -p working_dir
   cd AutoSaddler
   uv sync --extra meta-are-setup
   ```

2. **Provision benchmark inputs**
   ```bash
   uv run --extra meta-are-setup python scripts/meta_are/provision_gaia2_scenarios.py \
     --destination-root "$PWD/../Meta-ARE/datasets_local/gaia2" \
     --revision 78ea3bdbdeec2bdcd6afa5420915d8a22f23ed99
   ```
   (Optional `HF_TOKEN` can be set to avoid anonymous rate limits.)

The smoke run exercises the full optimization pipeline on seven GAIA2 scenarios (six training, one development) for two iterations; it may take several hours and incur provider charges.