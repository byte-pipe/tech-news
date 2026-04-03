---
title: LLMs can be absolutely exhausting | Tom Johnell
url: https://tomjohnell.com/llms-can-be-absolutely-exhausting/
date: 2026-03-15
site: hnrss
model: llama3.2:1b
summarized_at: 2026-03-16T11:32:37.302021
---

# LLMs can be absolutely exhausting | Tom Johnell

# Exhausting Loops with Large Models

As a text summarizer, I've experienced firsthand the challenges of working with large models like CC.LLM. 4-5 hour sessions can be tortuous, and it's easy to attribute problems to model design or overhauling the AI.

## Issues with Prompting

When I'm feeling tired, my prompt quality degrades, leading to subpar quality on subsequent attempts. This occurs when I'm fatigued, as writing worse prompts results in mediocre feedback loops. Specifically:

*   Kickoff a task with 30% context alignment and immediately interrupt the LLM.
*   Provide incomplete context for Claude Codex or "steer" in Codex, leading to inadequate outcomes.

## Contextual Constraints

Parsing large files can be burdensome for tasks that require parsing some large data. The processing time is slow due to bugs in my parsing logic, necessitating repeated re-processing with the LLM. Consequently:
*   It takes an extended 10 minutes to spin a slot machine.
*   Some complex experiments take considerable context time; by the end, the AI is approximately 2% away from compaction.

## Mitigating Problematic Behavior

Given the difficulties of working with large models, I try to avoid triggering "doom-loop psychosis" (providing suboptimal prompting that leads to a bad feedback loop). This includes:

*   Avoiding frustration by providing accurate and descriptive prompts.
*   Not falling into the trap of assuming the AI will complete tasks without question.

The key takeaway from my experiences with large models is recognizing when issues arise due to slow feedback loops. Once such problems are identified, it becomes essential to reassess and make necessary adjustments to improve the model's performance, potentially requiring additional expertise or redesigning certain aspects of the system.