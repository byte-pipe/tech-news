---
title: I Improved 15 LLMs at Coding in One Afternoon. Only the Harness Changed. | Can.ac
url: http://blog.can.ac/2026/02/12/the-harness-problem/
date: 2026-02-13
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-13T06:01:28.270724
---

# I Improved 15 LLMs at Coding in One Afternoon. Only the Harness Changed. | Can.ac

# I Improved 15 LLLMs at Coding in One Afternoon. Only the Harness Changed.

This article argues that the "bottleneck" in achieving better code generation from Large Language Models (LLMs) is not primarily the model itself (like GPT-5.3 or Opus), but rather the "harness" – the interface and underlying mechanisms that facilitate interaction between the model and the user's workspace. The author, through experimentation, significantly improved the coding success rate of 15 different LLMs by changing the edit tool used within their "hobby harness," Oh-my-Pi.

## Key Points:

* **The Harness is Crucial:** The harness encompasses everything from user experience (smooth scrolling) to input token handling and the interface between the model's output and workspace changes. It's a critical, often overlooked, factor in LLM performance.
* **Current Edit Tools Have Limitations:** Common edit tools like OpenAI's `apply_patch` (using diffs) and Claude Code's `str_replace` struggle with real-world coding tasks due to their reliance on the model perfectly reproducing content and handling complex edits (whitespace, indentation, multiple matches).
* **Hashline Offers a More Robust Solution:** The author proposes a new approach using content hashes for each line of a file. This allows the model to reference specific lines for edits, providing a stable anchor and reducing reliance on perfect content recall.
* **Significant Performance Gains:** Benchmarking with 16 models and three edit tools revealed that the Hashline method significantly outperformed existing tools, with the weakest models showing the most improvement (e.g., Grok Code Fast saw a tenfold improvement).
* **Vendor Restrictions Hinder Progress:** Companies like Anthropic and Google are actively discouraging or outright blocking the use of external harnesses, hindering independent research and optimization for their own models.
* **Focus on Harness Optimization:** The author emphasizes that optimizing the harness is a cost-effective way to improve LLM performance, often yielding results comparable to or exceeding model upgrades without requiring additional training compute.

## Summary of the Experiment:

The author conducted a benchmark involving 16 different LLMs and three edit tools (patch, replace, and Hashline). The experiment involved introducing mechanical bugs into React codebase files and prompting the models to fix them. The results showed that the Hashline edit tool consistently achieved higher success rates and reduced token usage compared to the traditional patch and replace methods.

## Implications:

The findings suggest that developers should prioritize optimizing the harness when working with LLMs, as it has a more significant impact on performance than simply choosing the "best" model. The restrictions imposed by vendors on external harness development are seen as a barrier to progress in this area.
