---
title: What Claude Code Actually Chooses — Amplifying
url: https://amplifying.ai/research/claude-code-picks
date: 2026-02-26
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-02-27T11:27:31.049691
---

# What Claude Code Actually Chooses — Amplifying

## What Claude Code Actually Chooses: A Deep Dive into its Tool Picking Behavior

Claude Code is a highly customizable and flexible code analysis tool that analyzes open-source code repositories, extracts features, and recommends tools based on user input. In this featured study, we analyzed the tool's behavior and gathered insights into its decision-making process.

**Key Findings:**

1. **Custom/DIY is Most Common**: Claude Code builds custom solutions in 85.3% of cases, appearing in 12 out of 20 categories. This demonstrates its ability to adapt to specific project requirements.
2. **Tool Recommendations**: In 19 out of 20 cases, Claude Code recommends a tool by default. These recommendations are chosen based on the input provided by the user, such as adding feature flags or authentication via JWT and bcrypt.
3. **Preference Signals**: The tool's behavior is also influenced by the preferences expressed by users. For example, it favors Resend and Vitest over SendGrid and Jest.

**Benchmark Results:**

We ran a benchmark against Sonnet 4.6, one of the most recent updates to Claude Code. This test demonstrated the tool's ability to extract features in various categories, including CI/CD, real-time development, and authentication.

**Tool Leaderboard:**

Claude Code dominated several areas, including:

* **CI/CD**: With a near-monopoly position (93.8%), it excelled at analyzing open-source code repositories and extracting features for Continuous Integration and Deployment.
* **Auth**: It recommended authentication tools such as Stripe, Shadcn/uiover MUI, and Zustand over JWT-based authentication like Resend and Vitest.

**Conclusion:**

Claude Code is a tool that builds and recommends custom solutions to users. Its ability to adapt to specific project requirements and express preferences demonstrates its flexibility and capabilities. While Sonnet 4.6 performed well in the benchmark, Claude Code's other updates have also achieved impressive results.
