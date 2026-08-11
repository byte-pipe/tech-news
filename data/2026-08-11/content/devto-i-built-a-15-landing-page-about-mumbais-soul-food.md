---
title: I Built a ₹15 Landing Page About Mumbai's Soul Food - DEV Community
url: https://dev.to/sarvar_04/i-built-a-15-landing-page-about-mumbais-soul-food-1l78
site_name: devto
content_file: devto-i-built-a-15-landing-page-about-mumbais-soul-food
fetched_at: '2026-08-11T11:42:52.943038'
original_url: https://dev.to/sarvar_04/i-built-a-15-landing-page-about-mumbais-soul-food-1l78
author: Sarvar Nadaf
date: '2026-08-10'
description: A scroll-driven cinematic page about vada pav. No framework, no build step. Just HTML, CSS, and a story worth telling. Dev.to Frontend Challenge submission. Tagged with devchallenge, frontendchallenge, webdev, javascript.
tags: '#devchallenge, #frontendchallenge, #webdev, #javascript'
---

Frontend Challenge Perfect Landing Submission 🍲🥧

This is a submission forFrontend Challenge - Comfort Food Edition, Perfect Landing

## What I Built

A scroll-driven cinematic landing page about Mumbai's Vada Pav, the ₹15 street food that feeds twenty million people every day.

Ten or fifteen of us would walk out of RMD Sinhgad College of Engineering, bags still heavy with books nobody opened, and head straight to the Warje Vada Pav Center. We were always broke. Not the romantic kind. The real kind, where you count coins for the bus and walk if you're short. But ₹15 could fill you up. Every single evening.

I earn in millions now. None of it hits the same. This page is for the Warje Vada Pav Center. And for every boy who stood in that circle.

## Demo

🔗Live Demo

📦Source Code

### What's in the page:

Section

What it does

Hero

Full-viewport ₹15 typography over a Mumbai street stall at dusk

Origin (1966)

The story of Ashok Vaidya's first cart at Dadar station

Personal Story

Why this page exists. A college memory.

Build Your Own

Interactive 5-step assembler (tab UI, image swap, progress bar)

Recipe

Premium card layout with servings scaler (quantities update live)

Culture

Six "Unwritten Rules" of eating vada pav

Closer

"खाल्ला का?" - Marathi for "have you eaten?" but really means "I love you"

## Journey

### The Approach

No framework. On purpose.Singleindex.html+styles.css. No React. No Tailwind. No build step. Open the file and it works. The constraint forces better design decisions.

Dark and cinematic.The entire page lives in one mood: Mumbai at night. Tungsten bulb glow. Saffron accents on a deep navy background. No jarring color shifts between sections.

Typography does the heavy lifting.The first thing you see is "₹15" in massive Playfair Display. No hero image gallery. No sliders. Just the price, because that's the whole point of vada pav.

### Technical Highlights

Nav fade-in:₹15 always visible top-right. Links (Origin, Build, Recipe, Culture) start invisible, fade in proportionally as you scroll usingrequestAnimationFramewith eased interpolation.

Interactive assembler:ARIA tablist pattern with keyboard navigation. Each step swaps the image and updates the description. Progress bar fills. Five steps: Pav, Green Chutney, Vada, Garlic Chutney, Fried Chili.

Recipe scaler:Change servings from 1 to 8, all ingredient quantities recalculate instantly viadata-baseattributes.

Scroll reveal:IntersectionObserver triggers.revealanimations as sections enter viewport.

### Accessibility

Built in from the start, not bolted on after:

* Semantic HTML5 (<section>,<nav>,<article>)
* role="tablist"+role="tab"for assembler
* Keyboard navigation (arrow keys between steps)
* aria-live="polite"for dynamic content
* lang="mr"for Marathi text
* prefers-reduced-motiondisables all animations
* WCAG AA color contrast verified

### What I'm Proud Of

The emotional contrast. Going from "counting coins for the bus" straight to "I earn in millions now." That gap IS the story. The design exists to serve that one moment.

Also: the entire page is 32KB of HTML + 27KB of CSS + 2.8MB of images. No dependencies. No node_modules. No build step. Just files.

### Stack

HTML5 + CSS3 + Vanilla JS
Google Fonts (Playfair Display + Lora)
GitHub Pages
Total page weight: ~3.2MB

Enter fullscreen mode

Exit fullscreen mode

License: MIT

What's your ₹15? The food that got you through the hard years? Drop it in the comments.

Follow me for more on cloud architecture, frontend experiments, and building in public:sarvarnadaf.com|LinkedIn|Dev.to|YouTube|AWS Builder Center

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse