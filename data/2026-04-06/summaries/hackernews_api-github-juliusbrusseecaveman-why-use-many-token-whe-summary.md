---
title: GitHub - JuliusBrussee/caveman: 🪨 why use many token when few token do trick — Claude Code skill that cuts 75% of tokens by talking like caveman · Git...
url: https://github.com/JuliusBrussee/caveman
date: 2026-04-05
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-06T01:02:13.703157
---

# GitHub - JuliusBrussee/caveman: 🪨 why use many token when few token do trick — Claude Code skill that cuts 75% of tokens by talking like caveman · Git...

# caveman repository summary

## Overview
- A Claude Code skill that makes Claude respond in a concise “caveman” style.
- Reduces token usage by about 75 % while preserving full technical accuracy.
- Intended to lower cost, increase speed, and add a humorous tone to code reviews.

## Key Features
- **Token reduction**: Strips filler words, articles, pleasantries, and hedging.
- **Technical fidelity**: Keeps exact code, error messages, and technical terms unchanged.
- **Speed boost**: Fewer tokens to generate results in roughly 3× faster responses.
- **Easy activation**: Trigger with commands such as `/caveman`, “talk like caveman”, or “less tokens please”.
- **Simple deactivation**: Say “stop caveman” or “normal mode”.

## Installation
- Via npx: `npx skills add JuliusBrussee/caveman`
- Via Claude plugin system:
  - `claude plugin marketplace add JuliusBrussee/caveman`
  - `claude plugin install caveman@caveman`

## Usage Examples
- **Normal Claude (69 tokens)**: Provides detailed explanation with filler language.
- **Caveman Claude (19 tokens)**: Delivers the same technical advice in a terse format, e.g., “New object ref each render. Inline object prop = new ref = re‑render. Wrap inuseMemo.”

## How It Works
- Identifies and removes common filler phrases such as:
  - “I’d be happy to help you with that”
  - “The reason this is happening is because”
  - “I would recommend that you consider”
  - “Sure, let me take a look at that for you”
- Retains essential content: code blocks, exact terminology, error messages, and commit messages.

## Benefits
- **Cost savings**: 75 % fewer output tokens → 75 % lower expense.
- **Performance**: Faster generation due to reduced token count.
- **Accuracy**: Technical information remains unchanged.
- **Entertainment**: Adds a comedic element to interactions.

## Repository Details
- **License**: MIT
- **Stars**: 579
- **Forks**: 11
- **Primary topics**: AI, skill, meme, tokens, caveman, Claude, LLM, prompt‑engineering, Anthropic, Claude‑code

## Call to Action
- Star the repository if the skill helps you save tokens and money.