---
title: REA — Reverse Engineering for Your Coding Agent
url: https://rea.tools/
date: 2026-10-10
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-10T16:09:57.426462
---

# REA — Reverse Engineering for Your Coding Agent

## Reverse Engineering for Your Coding Agent

### Introduction to REA

Reverse Engineering (REA) is a tool that allows your coding agent to inspect a program and explain what it does in plain English. Below are the main points about using REA to understand how software works.

### Setup and Installation

To get started, you need to:

1. Set up the REA agent using `npx rea-agents@latest setup`.
2. Approve the setup plan, then restart your agent.

### Reverse Engineering Basics

Reverse engineering involves finding out how software works by examining the program itself. The goal is to understand a feature well enough to explain it, change it, or rebuild it.

### The REA Process

The REA process can be broken down into five steps:

1. **Decode Branches**: The first step involves analyzing the program's branches and identifying the ones that matter.
2. **Trace Calls**: The second step involves following the calls made in the program to reconstruct the calculation or process.
3. **Recover the Rule**: The third step involves identifying the rule or logic that the program follows to perform a particular task.
4. **Explain in Plain English**: The fourth step involves explaining the process or feature in plain English using the recovered rule.
5. **Continue with Example Usage**: Finally, you can try using the REA to analyze and experiment with different examples or features.

### Examples of REA Usage

Two examples are provided below:

1. Chrome's dinosaur game:

* **Why does the dinosaur get faster?**: The acceleration is based on a specific pattern, which is the rule applied to the game.

2. Adjusting the game speed:

* **How to reproduce its acceleration**: Use the REA to follow the calls and reconstruct the calculation. Once the acceleration is known, you can adjust the speed and observe the changes.

### Example Reconstructed Calculation:

The calculated result is based on the following pattern:

6 → 10 → 13

To reproduce the acceleration, you need to consider the following:

* **Starting value**: The dinosaur starts at 6.
* **Increase**: The acceleration increases from 10 to 13.
* **When stops**: The acceleration stops when the game reaches 13.

By understanding this rule and pattern, you can use the REA to understand and experiment with the game's acceleration.

### Tips and Tricks

* Focus on the parts that matter in the program.
* Use the REA to follow the calls and reconstruct the calculation.
* Experiment with different examples and features to gain insights into the program's logic.