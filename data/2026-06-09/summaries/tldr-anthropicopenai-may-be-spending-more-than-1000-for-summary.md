---
title: Anthropic/OpenAI may be spending more than $1000 for every $100 you pay them – R&A IT Strategy & Architecture
url: https://ea.rna.nl/2026/06/07/anthropic-openai-may-be-spending-more-than-1000-for-every-100-you-pay-them/
date: 2026-06-09
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-06-09T06:48:06.514934
---

# Anthropic/OpenAI may be spending more than $1000 for every $100 you pay them – R&A IT Strategy & Architecture

# Summary of “Anthropic/OpenAI may be spending more than $1000 for every $100 you pay them – R&A IT Strategy & Architecture”

## Introduction
- The author resumes writing about generative AI after a 15‑month break, focusing on “coding with Large Language Models” (LLMs) as the presumed killer app.
- A brief digression critiques Anthropic’s recent blog post “When AI builds itself”.

## Critique of Anthropic’s Blog Post
- The post is described as “suggestive writing” that hides caveats among hyperbolic statements.
- A single disclaimer (“we might be wrong”) is seen as insufficient given the extensive claims.
- Benchmarks cited (50‑80 % success on coding tasks) are argued to be useless for fully autonomous coding without human oversight.
- The author questions whether checking in eight times more lines of code per day is genuinely beneficial, noting that many of those lines are later discarded.

## Experiment with Claude Code
- The author has been running an ongoing experiment to evaluate Claude Code’s capabilities.
- Using Claude Code together with personal programming experience, an unfinished but functional application (~40 k lines of code) was produced that the author could not have built quickly on their own.
- The experiment revealed:
  - High productivity when the model is guided, but diminishing returns when set to higher “effort” levels.
  - Frequent need to switch between “medium” and “high” effort settings to maintain code quality.

## Economic Findings
- LLM‑based coding is not economically viable for most users under current pricing.
- A $100/month Claude Max subscription reaches its weekly token limit quickly; full “agentic coding” would consume tokens costing > $1 000 at API rates.
- Anthropic appears to be working on model versions (Opus 4.7, 4.8) to reduce token consumption, but this may signal the end of major performance gains (the end of an S‑curve).
- Simple conversational use is “too cheap to meter,” but complex, recursive tasks (coding, deep reasoning) explode in token usage, leading to high costs (e.g., a single high‑effort task ≈ $75 at API rates; a query using 1 M tokens ≈ $25).

## Personal Cost Management Experience
- Started with a $20/month plan; quickly hit usage limits and had to purchase extra tokens at API pricing.
- Within a few days, extra token purchases reached ≈ $80, making the $100/month plan far more cost‑effective.
- The author confirms that inference/generation, not training, drives the majority of expenses.

## Conclusions
- While LLM‑assisted coding can dramatically accelerate prototype development, the current cost structure makes it unsustainable for regular, production‑level use.
- The market narrative of “too cheap to meter” masks the high expense of serious, recursive applications.
- Users should enjoy the current capabilities while they last, but prepare for the financial realities of scaling LLM‑driven development.