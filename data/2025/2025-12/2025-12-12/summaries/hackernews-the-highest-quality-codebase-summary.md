---
title: The highest quality codebase
url: https://gricha.dev/blog/the-highest-quality-codebase
date: 2025-12-12
site: hackernews
model: llama3.2:1b
summarized_at: 2025-12-12T11:19:50.261734
screenshot: hackernews-the-highest-quality-codebase.png
---

# The highest quality codebase

**Implementing Code Review for Large Codebases**

The article discusses an experiment where a principal engineer, Claude, used automated testing and CI/CD techniques to improve the quality of his codebase over Thanksgiving weekend. The goal was to create a high-quality app by estimating macronutrients in various foods based on description and photo.

**Key Points:**

* The engineer used custom scripts to automate tests and CI/CD workflows.
* A specific script, `claude`, was used to run automated testing and commit changes to minimize merge conflicts.
* The codebase underwent significant improvements due to the automation of tasks.

**Maintaining Original Perspective:**

The author presents their experience as if it were Claude's experience:

"We have tweaked the prompt here and there when I've been seeing it overindexing on a single thing, but with enough iterations it started covering a lot of ground.. "

This highlights Claude's efforts to improve the codebase quality during the experiment.

**Use of Language:**

The text is written primarily in English, with some occasional exceptions due to its focus on technology and coding terms.

**Structured Output:**

Here's a concise summary in Markdown format:

# Implementing Code Review for Large Codebases

## The Experiment
An engineer used automated testing and CI/CD techniques to improve the quality of his codebase over Thanksgiving weekend. The goal was to create a high-quality app by estimating macronutrients in various foods based on description and photo.

### Custom Script (`claude`)
A custom script, `claude`, was used to run automated testing and commit changes. The script set up the environment, executed tests, and committed changes:

```bash
#!/usr/bin/env bash

set -euo pipefail

PROMPT="Ultrathink. You're a principal engineer. Do not ask me any questions. We need to improve the quality of this codebase. Implement improvements to codebase quality."

MAX_ITERS=200

for i in {1..200}; do
  claude --dangerously-skip-permissions -p "$PROMPT"
  git add -A

  if git diff --cached --quiet; then
    echo "No changes this round, skipping commit."
  else
    git commit --no-verify -m "yolo run # $i: $PROMPT"
  fi
done
```

### Results
The codebase underwent significant improvements due to the automation of tasks.

## Conclusion

This experiment highlights the benefits of implementing automated testing, CI/CD, and code review in a large-scale project. Claude's experience shows how this approach can lead to improved code quality while reducing manual effort.
