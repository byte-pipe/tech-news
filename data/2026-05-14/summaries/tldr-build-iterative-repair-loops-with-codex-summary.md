---
title: Build iterative repair loops with Codex
url: https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex
date: 2026-05-14
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-14T06:03:36.740619
---

# Build iterative repair loops with Codex

# Build iterative repair loops with Codex

## Overview
- The notebook demonstrates a **closed‑loop agent workflow** where an agent (Codex) iteratively **review‑repair‑validate** a code artifact until it meets defined quality criteria.  
- The example focuses on fixing stale or broken API/SDK examples in Jupyter notebooks, but the pattern applies to any artifact that can be measured with reliable feedback.

## Workflow Phases
1. **Review**
   - Inspects the current artifact without modifying it.  
   - Returns structured findings (issues, missing elements, outdated calls).

2. **Repair**
   - Applies focused edits to a copy of the artifact based on the review findings and the latest validation feedback.  
   - Produces a change summary and the path to the updated file.

3. **Validate**
   - Executes the relevant checks (e.g., running the notebook end‑to‑end).  
   - Reports any remaining problems, which become input for the next repair pass.

## Setup Highlights
- Uses **Codex CLI** in headless mode so the loop can be driven from Python cells.  
- Requires `OPENAI_API_KEY` and optionally allows model selection via `REPAIR_MODEL`.  
- Installs a pinned CLI version (`0.130.0`) for reproducibility.  
- Creates a temporary directory for run outputs, configurable via `CODEX_REPAIR_RUNS_DIR`.

## Sample Artifacts
- Three pre‑repair notebooks are loaded from `data/docs`:
  1. `qdrant_embeddings_search_pre_repair.ipynb` – target iteration 1, one‑pass cleanup.  
  2. `getting_started_evals_pre_repair.ipynb` – target iteration 2, two‑pass cleanup.  
  3. `knowledge_retrieval_pre_repair.ipynb` – target iteration 3, three‑pass cleanup.  
- Metadata for each notebook (cell counts, source path, repair depth) is extracted to drive the loop.

## Business Rules & Issue Taxonomy
- A concise contract is supplied to Codex to keep the loop focused:
  - **Modernization**: update deprecated calls (e.g., `client.chat.completions.create → client.responses.create`).  
  - **Reader Experience**: ensure fresh‑environment setup, runnable examples, clear prerequisites, and preservation of teaching goals.  
  - Preferred chat and embedding models are also specified.

## Structured Outputs
- **Review** → list of findings (structured JSON).  
- **Repair** → summary of changes + path to repaired artifact.  
- **Validate** → delta of remaining issues, feeding back into the next iteration.

## Key Takeaways
- Iterative repair loops turn validation failures into actionable feedback rather than dead ends.  
- The pattern is modular: replace the validation step with unit tests, policy checks, simulations, or human review as needed.  
- By defining explicit business rules, the agent stays aligned with domain‑specific quality standards while minimizing unnecessary model inference.