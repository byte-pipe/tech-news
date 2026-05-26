---
title: Using AI to write better code more slowly | Read the Tea Leaves
url: https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/
date: 2026-05-25
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-05-26T19:45:30.164313
---

# Using AI to write better code more slowly | Read the Tea Leaves

# Using AI to Write Better Code More Slowly

The author discusses how the use of Large Language Models (LLMs) can lead to slower code development when used for tasks such as testing, reviewing, or merging code. However, they argue that this is an oversimplification and that LLMs can be highly effective in finding bugs.

## Key Points:

* LLMs are flexible and can use multiple agents to test a codebase
* The latest public models from Anthropic and OpenAI can find plenty of bugs even without manual review
* A specific algorithm, adapted from another article's core insight, can prioritize and validate findings

## Main Ideas:

* The author presents their own experience using the "Claude skill" to identify bugs in a PR process
* This method involves running multiple agents on the PR and then reviewing their results before writing a final report
* The technique has been effective in finding tons of bugs, with near-zero false positive rates

## Additional Information:

* The author suggests that users can adapt this method to incorporate custom guidelines for what constitutes a "bug"
* They recommend using proper indexes or SQL queries to ensure the quality of the code being developed

## Context:

* The article is written as part of software engineering discussions and is likely aimed at experienced developers
* The use of LLMs in coding tasks continues to gain attention, with some considering them a viable replacement for human evaluation