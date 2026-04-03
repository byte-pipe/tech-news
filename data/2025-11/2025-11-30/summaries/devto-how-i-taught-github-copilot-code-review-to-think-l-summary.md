---
title: How I Taught GitHub Copilot Code Review to Think Like a Maintainer - DEV Community
url: https://dev.to/techgirl1908/how-i-taught-github-copilot-code-review-to-think-like-a-maintainer-3l2c
date: 2025-11-25
site: devto
model: llama3.2:1b
summarized_at: 2025-11-30T11:09:30.724353
screenshot: devto-how-i-taught-github-copilot-code-review-to-think-l.png
---

# How I Taught GitHub Copilot Code Review to Think Like a Maintainer - DEV Community

# Vibe Coding: A Game-Changer for Open Source Projects
GitHub has enabled a new era of open source project maintenance with AI-powered coding tools. However, contributing to unfamiliar codebases used to be daunting despite the popularity of projects. But now, we have Goose, an open source AI agent framework built in Rust, and the barrier to contribution is lower than ever.

# The Current State
Contribution barriers are low, but contributor experience can be a challenge for maintainers. We're glad to have Copilot Code Review, which has become a valuable tool in reviewing PRs as soon as they're opened. However, our initial implementation was met with mixed feedback. Engineers found the reviews too noisy and comments were often of low value.

## Key Issues
The main issues identified after analysis are:

* Long and overwhelming comments (80% or less confidence)
* Too many "maybe" and "consider" comments suggesting low confidence
* Only 1 in 5 comments marked as good catches

## A Different Approach
We understand that Copilot needs guidance to get it right. Therefore, we created an instruction file (copilot-instructions.md) specifying how we want Copilot to behave.

### Review Philosophy and Priority Areas

* Comment on issues only when you have **HIGH CONFIDENCE** (>80%) that an issue exists.
* Respond with concise feedback by focusing on clarity issues that could lead to errors.
* Prioritize areas we care about by telling Copilot exactly what to focus on:

## Focus on Clarity Issues
For complex code, clarify sections or add comments explaining assumptions. For unclear operations, suggest alternatives in a descriptive manner.

Leave this guide for future reference and explore the GitHub Copilot documentation to learn more about its features and capabilities.
