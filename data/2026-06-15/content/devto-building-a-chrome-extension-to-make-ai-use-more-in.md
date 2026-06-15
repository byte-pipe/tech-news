---
title: Building a Chrome Extension to Make AI Use More Intentional - DEV Community
url: https://dev.to/javz/building-a-chrome-extension-to-make-ai-use-more-intentional-20k0
site_name: devto
content_file: devto-building-a-chrome-extension-to-make-ai-use-more-in
fetched_at: '2026-06-15T20:10:49.260698'
original_url: https://dev.to/javz/building-a-chrome-extension-to-make-ai-use-more-intentional-20k0
author: Julien Avezou
date: '2026-06-15'
description: After posting several articles about the impact of AI on developers and sharing resources to help... Tagged with ai, webdev, productivity, buildinpublic.
tags: '#ai, #webdev, #productivity, #buildinpublic'
---

Tracks cognitive cost and usage risks

After posting several articles about the impact of AI on developers and sharing resources to help mitigate some of the risks, I wanted to share a new tool I've been building and experimenting with.

I introduce you toThinkMode!

A chrome extension that helps developers choose a thinking mode before prompting AI, and calculate the associated cognitive cost after prompting AI.

AI makes it easy to skip thinking.

This tool helps slow down and integrate thinking before and after prompting the AI.

As a browser extension it can be easily integrated into your everyday LLM chat prompting workflow.

## The Idea

Before opening a prompt, ThinkMode asks you to describe what you are trying to do.

It then recommends one of 5 modes:

* Explore: understand the problem before solving it
* Challenge: pressure-test an existing plan
* Decide: compare options and tradeoffs
* Audit: review quality, correctness, tests, and edge cases
* Reflect: learn from what you just did

The goal is to match the prompt with the kind of thinking intended for the task.

The tool also includes amanual AI usage log.

After using AI, you can log how you used it.

Usage is grouped into three categories:

* Supportive: AI helps expand your thinking
* Mixed: AI saves time but may compress understanding
* Risky: AI may replace your judgment

Each log adds to acognitive cost meter. Riskier usage fills it faster.

Cognitive cost measures tradeoffs between using AI to expand understanding vs outsourcing judgment.

When the meter is full, ThinkMode temporarily pauses supported AI chat pages for 5 minutes.

Most developer tools optimize for speed.

I wanted to experiment with a tool that introducesintentional friction in order to surface reflection.

## How it works

ThinkMode is a Manifest V3 Chrome extension built with React, TypeScript, and Vite.

The architecture includes:

* a content script detects supported AI chat pages
* a floating button opens the extension
* a background service worker coordinates the side panel
* a React side panel handles the main workflow
* shared TypeScript modules handle recommendation logic and prompt generation

The extension currently supports ChatGPT, Claude, and Gemini pages.

There isno backend nor LLM API callinvolved.

ThinkMode does not read conversations, scrape page content, send analytics, or store data remotely.

The recommendation engine is deterministic. It uses simple keyword rules to choose a thinking mode which felt reasonable considering this is an MVP.

## What I Learned

Sometimes the useful AI tool is not the one that gives you a better answer.

It can be the one that helps you ask a better question.

I'm curious:

Have you ever caught yourself accepting an AI answer before fully understanding the problem?

If so, what habits or tools help you stay engaged in the thinking process?

## How to install

You can download the extensionfree here from the chrome web store

Otherwise you can run the extension locally using developer mode from chrome extensions. The code is open sourcehere on github.

Feel free to fork it and adapt it to your own needs.

Would really appreciate a star or review if you find it useful!

If you can think of ways to improve this tool or want to see other features, let me know in the comments!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse