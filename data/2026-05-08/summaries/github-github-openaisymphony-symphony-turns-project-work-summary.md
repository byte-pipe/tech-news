---
title: GitHub - openai/symphony: Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervis...
url: https://github.com/openai/symphony
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-05-08T08:14:25.024565
---

# GitHub - openai/symphony: Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervis...

# Symphony

## Overview
- Turns project work into isolated, autonomous implementation runs.  
- Enables teams to manage work at a higher level instead of supervising coding agents.  

## Demo
- Monitors a Linear board for new tasks.  
- Spawns agents that complete tasks and generate proof of work: CI status, PR review feedback, complexity analysis, and walkthrough videos.  
- Upon acceptance, agents safely land the PR without engineer supervision.  

## Warning
- Low‑key engineering preview intended for testing in trusted environments only.  

## Running Symphony
### Requirements
- Works best with codebases that have adopted harness engineering.  
- Represents the next step after managing coding agents, focusing on managing the work itself.  

### Option 1: Build Your Own
- Instruct a coding agent to implement Symphony in a language of your choice.  
- Follow the specification located at `SPEC.md`.  

### Option 2: Use the Experimental Reference Implementation
- Follow the instructions in `elixir/README.md` to set up the Elixir‑based implementation.  
- You can also ask a coding agent to help with the setup using the provided README link.  

## License
- Apache License 2.0.  

## Resources
- Main README provides detailed information and usage guidance.  

## Repository Statistics
- Stars: 22.4k  
- Watchers: 154  
- Forks: 2.1k  
- Primary languages: Elixir (95.5 %), Python (3.0 %), CSS (1.2 %), Others (0.3 %).