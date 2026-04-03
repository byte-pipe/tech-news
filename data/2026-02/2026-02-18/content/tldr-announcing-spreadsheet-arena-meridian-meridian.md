---
title: Announcing Spreadsheet Arena | Meridian | Meridian
url: https://www.meridian.ai/blog/all/spreadsheet-arena
site_name: tldr
content_file: tldr-announcing-spreadsheet-arena-meridian-meridian
fetched_at: '2026-02-18T11:19:50.607633'
original_url: https://www.meridian.ai/blog/all/spreadsheet-arena
date: '2026-02-18'
description: Announcing Spreadsheet Arena. Read the latest from Meridian.
tags:
- tldr
---

Back

# Announcing Spreadsheet Arena

Research

02 / 13 / 26

Research Paper
Live Arena

Today we're releasing Spreadsheet Arena and accompanying research done in collaboration with researchers at Cornell, CMU, and Scale AI. Spreadsheet Arena is an open platform for evaluating how well LLMs generate spreadsheet workbooks. Users submit a prompt, and the arena produces blind pairwise battles between model outputs. You vote on which spreadsheet is better without knowing which model made it.

We've collected thousands of votes across models from OpenAI, Anthropic, Google, xAI, Meta, Alibaba, and Moonshot. Prompts span professional finance, corporate FP&A, academic research, operations, creative uses, and small business workflows.

The results reveal patterns that generic benchmarks miss. Formatting and structure drive user preference more than formula sophistication. Text density, background fills, and numeric content are stronger predictors of winning than lookup functions or conditionals. But this varies by domain: in academic contexts, heavy formatting actually hurts, while in finance, adherence to professional color-coding conventions is a significant positive signal.

We also ran a blinded expert evaluation with finance professionals. Expert ratings agreed with crowd preferences only about half the time. The biggest gap was in color coding and formatting. Even the top-ranked models don't reliably follow real-world financial modeling conventions.

Failure analysis shows that losing spreadsheets typically have multiple issues simultaneously. Presentation deficiency is the most common across all models, but the failure signatures differ by model family. Claude models lose less often on polish but more often on integrity and numerical correctness. Weaker models struggle with basic prompt compliance.

The arena is live atspreadsheetarena.ai. Read the full paper for methodology, model rankings, implications for evaluation and post-training, and the complete expert evaluation study.

Read the full paper (PDF)

Share this article

Copy link
