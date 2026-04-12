---
title: GitHub - islandbytesio/commit_comprehension_gate · GitHub
url: https://github.com/islandbytesio/commit_comprehension_gate
date: 2026-04-13
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-13T06:00:50.884442
---

# GitHub - islandbytesio/commit_comprehension_gate · GitHub

# Comprehension Gate

## Overview
- A GitHub Action that prevents merging AI‑generated code until the author demonstrates understanding.
- Generates three multiple‑choice questions about the PR’s logic and design using Claude.
- No external database; questions are stored directly in the PR comment.

## How it works
1. A pull request targeting the configured branch (default `main`) is opened or updated.  
2. The workflow extracts the diff and sends it to Claude, which creates three multiple‑choice questions.  
3. The questions are posted as a PR comment and the commit status is set to **pending**.  
4. The PR author replies with their answers in the same comment thread.  
5. An answer‑checking workflow runs instantly (no API call) and updates the commit status to **success** or **failure**.  

- Authors may retry unlimited times; new commits generate fresh questions.

## Demo
- Video demonstration forthcoming.

## Setup
1. **Copy files into the repository**  
   - `scripts/comprehension_gate.py`  
   - `.github/workflows/comprehension-gate-pr.yml`  
   - `.github/workflows/comprehension-check.yml`
2. **Add Anthropic API key** as a repository secret named `ANTHROPIC_API_KEY`.
3. **Optional:** Change the gated branch by editing `comprehension-gate-pr.yml` (replace `main` in the `branches` list).

## Enforcing the gate (required status check)
1. Navigate to **Settings → Branches**.  
2. Add or edit a branch protection rule for the target branch.  
3. Under **Require status checks to pass**, add the exact context name **Comprehension Gate**.  
4. (Recommended) Enable **Require branches to be up to date before merging**.  
5. Save the rule.  

GitHub will block the merge button until the “Comprehension Gate” status is **success**.

## Developer experience
- Bot comment example:  

  ```
  Q1. What does this change do when the input is empty?
  - A) Returns an empty list
  - B) Raises a ValueError
  - C) Returns None
  - D) Falls through to the default handler
  ```
- Author replies with answers, e.g.:

  ```
  1. B
  2. A
  3. C
  ```
- Bot immediately replies with a pass/fail breakdown and updates the commit status.

## Skipping the gate
- Draft PRs are automatically exempt.  
- Maintainers can manually set the status to success via the GitHub API or CLI:

  ```bash
  gh api repos/{owner}/{repo}/statuses/{sha} \
    -f state=success \
    -f context="Comprehension Gate" \
    -f description="Manually approved"
  ```

## API cost
- Claude is invoked once per PR open or push to generate questions; answer checking incurs no API call.  
- Uses `claude-opus-4-6`; diffs are truncated at 12 KB (≈3,500 input tokens).  
- Approximate cost per PR: **$0.05–$0.10** (based on current Anthropic pricing).  

| Diff size | Approx. input tokens | Estimated cost |
|-----------|----------------------|----------------|
| Small (< 2 KB) | ~800 | ~$0.01 |
| Medium (2–6 KB) | ~2,000 | ~$0.04 |
| Large (6–12 KB, truncated) | ~3,500 | ~$0.07 |
| Output (questions) | ~500 | ~$0.04 |

## Requirements
- Python 3.12+ (provided by the Actions runner).  
- `anthropic` Python package (installed automatically).  
- Valid Anthropic API key.

## License
- MIT License (see `LICENSE`).  
- Patent pending – IslandBytes LLC.

## Contributing
- Issues and pull requests are welcome.  
- Follow the guidelines in `CONTRIBUTING.md`.

## About
- Repository owned by IslandBytes LLC.  
- Primary language: Python.