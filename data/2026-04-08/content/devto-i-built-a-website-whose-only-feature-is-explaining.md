---
title: I Built a Website Whose Only Feature Is Explaining How It Builds Itself - DEV Community
url: https://dev.to/dtannen/i-built-a-website-whose-only-feature-is-explaining-how-it-builds-itself-4l92
site_name: devto
content_file: devto-i-built-a-website-whose-only-feature-is-explaining
fetched_at: '2026-04-08T19:33:18.153127'
original_url: https://dev.to/dtannen/i-built-a-website-whose-only-feature-is-explaining-how-it-builds-itself-4l92
author: dtannen
date: '2026-04-08'
description: This is a submission for the DEV April Fools Challenge What I Built I built the most... Tagged with devchallenge, 418challenge, showdev.
tags: '#showdev, #devchallenge, #418challenge'
---

April Fools Challenge Submission ☕️🤡

This is a submission for theDEV April Fools Challenge

## What I Built

I built the most over-engineered website that does absolutely nothing useful.

Command Garden is a website about... itself. It has no users, no product, no reason to exist. Every morning, a 5-stage AI pipeline with three AI judges (Claude, GPT, and Gemini) wakes up, argues for 75 minutes about what feature to add to a website nobody visits, implements it, writes tests for it, reviews its own work, publishes a detailed decision log explaining why it chose to add "live growth stats" to a site with zero traffic, and then auto-posts about it on Bluesky to its zero followers.

The judges have names and personalities. The Gardener optimizes for "compounding value." The Visitor cares about "first-time clarity." The Explorer wants "novelty and surprise." They score candidates across seven dimensions. They write rationale paragraphs. They have disagreements. About a website that is literally just a changelog of its own changes.

Day 1: Added a section explaining how the pipeline works. Day 2: Added stats showing how many features have shipped (two). Day 3: Added an inline spec viewer so you can read the spec for the feature that added the inline spec viewer. It's turtles all the way down.

It also has a feedback form. In case you have opinions about what a website about nothing should build next. Your feedback is "one signal among many." The AI will "weigh it alongside technical signals." The technical signals are that the website does nothing.

## Demo

commandgarden.com— a website whose only content is documentation about how it builds itself

Highlights:

* Thearchivewhere you can browse a meticulous record of every meaningless decision
* Thejudges pageintroducing three AI personas who take their fake jobs very seriously
* Thefeedback formwhere you can influence the direction of nothing

## Code

## Commands-com/garden

### A fully automated site that runs a commands.com pipeline once a day

The infrastructure is genuinely absurd for what it does:

* CloudFormation stackwith S3, CloudFront, API Gateway, Lambda, and DynamoDB — to serve a static site with a feedback form
* 5-stage autonomous pipeline(Explore → Spec → Implementation → Validation → Review) — 75 minutes of AI compute to add a CSS class
* Three different LLM providers(Anthropic, OpenAI, Google) serving as judges — because one AI wasn't enough to decide whether to add a stats bar
* Automated Bluesky posting and Dev.to publishing— so the void can hear about it on two platforms
* Playwright test suite— rigorously testing features that don't matter

## How I Built It

The pipeline runs onCommands.com, which orchestrates multi-agent rooms. I pointed three AI models at an empty website and told them to "grow it one feature per day." They took the job extremely seriously.

The infrastructure is vanilla AWS because apparently we needed enterprise-grade hosting for a site that explains its own build process. CloudFront CDN with edge caching, because those zero concurrent users deserve low latency.

The site itself is intentionally simple — no build step, no framework, just HTML/CSS/JS — so the AI can modify it without breaking things. This is the one smart decision in the entire project.

The daily runner aggregates feedback from DynamoDB (empty), collects Bluesky metrics (zero followers, 0.2 average likes), gathers "recent context" from previous days (a recursive loop of self-reference), then kicks off a pipeline that costs real money to ship features to a website that costs real money to host for an audience that does not exist.

## Prize Category

Community Favorite— the community can literally control what gets built via the feedback form. Submit "add a button that does nothing" and tomorrow three AI judges will spend 75 minutes debating whether a button that does nothing has sufficient "compounding value" and "artifact clarity." Then they'll build it, test it, review it, and post about it. Democracy in action.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
