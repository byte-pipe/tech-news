---
title: 'Advent of AI 2025 - Day 9: Building a Gift Tag Generator with Goose Recipes - DEV Community'
url: https://dev.to/nickytonline/advent-of-ai-2025-day-9-building-a-gift-tag-generator-with-goose-recipes-3i73
site_name: devto
fetched_at: '2025-12-13T19:06:23.784500'
original_url: https://dev.to/nickytonline/advent-of-ai-2025-day-9-building-a-gift-tag-generator-with-goose-recipes-3i73
author: Nick Taylor
date: '2025-12-12'
description: 'Advent of AI 2025 - Day 9: Building a Gift Tag Generator with Goose Recipes I''ve edited... Tagged with adventofai, ai, goose, automation.'
tags: '#adventofai, #ai, #goose, #automation'
---

# Advent of AI 2025 - Day 9: Building a Gift Tag Generator with Goose Recipes

I've edited this post, but AI helped. These are meant to be quick posts related to the Advent of AI. I don't have time if I'm doing one of these each day to spend a couple hours on a post.

Theadvent of AIseries leverages Goose, an open source AI agent. If you've never heard of it, check it out!

## block/goose

### an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM

# goose

a local, extensible, open source AI agent that automates engineering tasks

goose is your on-machine AI agent, capable of automating complex development tasks from start to finish. More than just code suggestions, goose can build entire projects from scratch, write and execute code, debug failures, orchestrate workflows, and interact with external APIs -autonomously.

Whether you're prototyping an idea, refining existing code, or managing intricate engineering pipelines, goose adapts to your workflow and executes tasks with precision.

Designed for maximum flexibility, goose works with any LLM and supports multi-model configuration to optimize performance and cost, seamlessly integrates with MCP servers, and is available as both a desktop app as well as CLI - making it the ultimate AI assistant for developers who want to move faster and focus on innovation.

# Quick Links

* Quickstart
* Installation
* Tutorials
* Documentation
* Responsible AI-Assisted Coding Guide
* Governance

## Need Help?

* Diagnostics & Reporting
* Known Issues

…

View on GitHub

## Day 9: Print-Ready Gift Tags

ForDay 9 of Advent of AI, I built a Goose recipe that generates beautiful, print-ready gift tags. Here ismy submission. You tell it who the gift is for, what it is, pick a style, and it generates a complete HTML file ready to print. The recipe supports four different styles (elegant, playful, minimalist, festive), multiple languages, QR codes, and AI-generated poems.

This was my first time building a recipe that had to work with fixed dimensions. The challenge was making sure everything actually fit on a 3x2, 4x3, or 5x4 inch print area without content getting cut off. Normally in web dev these days, flex and container queries adjust accoring to content, but these literally need to be printed.

## The Fixed Size Problem

When I first tried generating tags, the content would overflow or fonts would be too big. Text would get cut off at the edges, or the QR code would hang off the bottom. Not great when you're actually trying to print these. Initially I noticed the CSS had setoverflow: hiddenon the cards which cropped the text/design.

The breakthrough came from adding explicit constraints to the recipe:

-

all content must fit and be visible with these exact dimensions

-

reduce font size if necessary to fit all content

-

use the developer extension to validate that no content is cut off visually

Enter fullscreen mode

Exit fullscreen mode

Once these constraints were in the instructions, Goose started generating tags that actually respected the print boundaries. Font sizes adapted based on content length, margins were calculated correctly, and nothing got cut off.

## Starting with a PRD

I started by generating a Product Requirements Document (PRD) from the challenge description. This has become my standard approach when working with AI tools. Having a structured PRD gives both me and Goose a clear roadmap.

The PRD covered:

* Four distinct visual styles
* Three gift sizes with exact dimensions
* Multilingual support (English, Spanish, French)
* QR code integration
* AI-generated contextual poems
* Print specifications and color requirements

From there, I used the PRD to generate the actual recipe YAML.

## Recipe Format Is Picky

Getting the recipe YAML format right took more back-and-forth than I expected. Goose kept making small mistakes:

* Theauthorfield was completely missing at first
* When it got added, it was in the wrong format
* Parameters ended up as top-level properties instead of underargs

What would have saved time? Passing a link to the Goose recipe docs. That would have given Goose the exact schema to follow instead of guessing.

## The Recipe in Action

Once the recipe was working, using it was straightforward. You can say something like:

Generate a playful gift tag for Marcus Rodriguez,
professional microphone, large size, include a poem,
QR code to https://example.com/thank-you,
Spanish language, purple color

Enter fullscreen mode

Exit fullscreen mode

Goose generates a complete HTML file with:

* The recipient's name prominently displayed
* Gift description
* A contextually appropriate poem (if requested)
* QR code integrated into the design
* All styled in the selected theme
* Print-ready with proper page dimensions

The HTML uses inline CSS and has no external dependencies, so it works offline and prints reliably.

## Design Inspiration

The recipe draws inspiration from Jhey Tompkins for playful/festive styles (lots of color, whimsical shapes, playful animations) and Adam Argyle for minimalist/elegant layouts (clean typography, precise spacing, purposeful negative space).

Each style has its own character:

* Elegant: Sophisticated serif fonts, metallic accents, generous whitespace
* Playful: Rounded fonts, bright colors, fun shapes
* Minimalist: Clean sans-serif, monochromatic plus one accent color, geometric precision
* Festive: Bold celebratory fonts, traditional holiday colors, seasonal motifs

The gift cards didn't end up looking as good as I wanted to. 😅 I don't think it crawled their codepens. I'm thinking I should have curated this better by pulling exact urls to some of their work. Examples and direct URLs definitely would have faired better.

## What I Learned

Working with fixed print dimensions requires explicit constraints. "Make it fit" isn't enough. You need to spell out exactly what "fit" means: nothing cut off, content must be visible, reduce sizes if necessary.

Starting with a PRD continues to be valuable. It forces you to think through all the requirements upfront instead of discovering them mid-build.

Recipe YAML format is strict. When building recipes, either reference the docs or provide examples of correct format. Guessing leads to multiple iterations to get the structure right.

## Token Usage and Cost

Across 13 recipe runs (generating different gift tags), the project used:

* Total tokens: 296,626
* Input tokens: 286,437 ($0.86)
* Output tokens: 10,189 ($0.15)
* Total cost: $1.01

I used Claude Sonnet 4.5 via OpenRouter with Goose. At OpenRouter's pricing of $3 per million input tokens and $15 per million output tokens, generating 13 different gift tags cost about a dollar. The recipe format and iterative refinement (getting the YAML structure right, adjusting constraints for print sizing) made up most of the token usage.

## What I Shipped

Everything's in myrepo's day-9 folder:

* gift-tag-generator.yaml- The complete Goose recipe
* PRD.md- Product requirements document
* README.md- Full documentation and examples
* Example HTML tags in different styles

## nickytonline/advent-of-ai-2025

### Advent of AI 2025 for nickytonline

# Fortune Teller

╔══════════════════════════════════════════════════════════════════════════════╗
║ ║
║ Patience is not simply waiting; it is understanding the right moment to ║
║ act. ║
║ ║
║ ║ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ║
║ ║
║ .-. ║
║ / \ ║
║ / ^ \ ║
║ | (o) | ║
║ \ - / ║
║ .---'---'---. ║
║ / HONK! \ ║
║ | *fluffs up* | ║
║ \ / ║
║ '---,---,---' ║
║ / \ ║
║ / \ ║
║ /_______\ ║
║ // \\ ║
║ // \\ ║
║ ~~ ~~ ║
║ ║
╚══════════════════════════════════════════════════════════════════════════════╝

View on GitHub

### Advent of AI 2025 for nickytonline

View on GitHub

## Wrapping Up

If you're building something that needs to work with physical constraints (print sizes, screen dimensions, etc.), make those constraints explicit and verifiable. "It should fit" becomes "all content must be visible within these exact pixel/inch dimensions, with validation."

And when building Goose recipes, reference the docs or provide format examples. The time saved upfront is worth it.

If you want to stay in touch, all my socials are onnickyt.online.

Until the next one!

Photo byKelly SikkemaonUnsplash

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
