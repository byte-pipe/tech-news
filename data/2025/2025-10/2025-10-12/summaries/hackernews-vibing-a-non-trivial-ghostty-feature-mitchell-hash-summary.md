---
title: Vibing a Non-Trivial Ghostty Feature – Mitchell Hashimoto
url: https://mitchellh.com/writing/non-trivial-vibing
date: 2025-10-12
site: hackernews
model: llama3.2:1b
summarized_at: 2025-10-12T11:24:20.912807
screenshot: hackernews-vibing-a-non-trivial-ghostty-feature-mitchell-hash.png
---

# Vibing a Non-Trivial Ghostty Feature – Mitchell Hashimoto

# Mitchell Hashimoto

# Vibing a Non-Trivial Ghostty Feature

## October 11, 2025

### Background

I recently shipped an non-trivial Ghostty feature that was largely developed with AI.

### Development Context

The finished feature is the macOS unobtrusive update notification feature. This feature shows update status within the terminal window without interrupting work by creating windows, grabbing focus, etc.

## Pre-AI Planning

### Decision to Use AI

During a high-profile OpenAI keynote, a demo was interrupted by a Ghostty update prompt:

"I wanted to ensure that never happened again," I said. The path I took was to make update notifications unobtrusive, avoiding popping up windows as usual.

## Overview of AI Tooling

### Pulling Out My AI Tooling

Absolutely not! To start, I came up with a rough plan for how to implement this feature using custom UI through Sparkle's Obj-C protocols.

## First Session: Prototyping the UI

### Key Steps in the Project:

1.  **Define backend and frontend requirements**: I wasn't sure about the frontend but knew that it needed a small button embedded in the title bar.
2.  **Implement custom UI using Sparkle:** I planned to re-implement a lot of Obj-C code to implement the custom UI, but know its specifics aren't my area of expertise.

### AI's Role

Given its ability as a prototyper, I was able to focus on planning and designing instead of implementation details.

## Additional Context

This post will share every single agentic coding session from this process, including those that went slightly awry. You'll also see the token cost for curious users when requested.
