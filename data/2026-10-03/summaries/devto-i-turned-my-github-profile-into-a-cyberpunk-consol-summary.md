---
title: I Turned My GitHub Profile Into a Cyberpunk Console With a City Built From My Contributions - DEV Community
url: https://dev.to/georgekobaidze/i-turned-my-github-profile-into-a-cyberpunk-console-with-a-city-built-from-my-contributions-h4c
date: 2026-10-01
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-03T03:08:01.586219
---

# I Turned My GitHub Profile Into a Cyberpunk Console With a City Built From My Contributions - DEV Community

# I Turned My GitHub Profile Into a Cyberpunk Console With a City Built From My Contributions

## I Wanted a Simple Custom GitHub Profile – It Quickly Got Out of Hand  
- At 23:00, exhausted after a 16‑hour day, I stared at a blank screen and let random thoughts wander.  
- The randomness sparked a strong idea that re‑energized me, despite my fatigue.  
- I chose to keep working instead of shutting down, driven by curiosity and the urge to “cook” something new.

## The Contribution City  
- I wanted my contribution graph to mean more than a plain grid of green squares.  
- Inspired by Cyberpunk 2077, neon lights, and towering skyscrapers, I imagined each day as a building: quiet days become empty lots, busy days become skyscrapers.  
- The vision of a 3‑D city representing my activity became the core concept.

## The Cyberpunk Console – Because Why Not?  
- A plain README felt insufficient; I wanted a neon‑glow terminal with scanlines, a typing animation for my name, and a cohesive frame.  
- The goal was to turn the entire profile into a stylized cyberpunk console that housed the contribution city.

## Welcome to the Sandbox – Working Within GitHub’s Restrictions  
- GitHub strips `<script>` and `<style>` tags from READMEs; only limited Markdown and a few HTML tags are allowed.  
- **Loophole:** an SVG embedded via `<img>` is treated as a static image, but the SVG itself can contain CSS and animations.  
- Using this, I created typing effects, blinking cursors, and glitchy text—all inside SVG files.  
- Constraints: no external resources (fonts must be embedded), no hover or click interactions, and GitHub caches images for several minutes, which required careful debugging.

## One Console, 23 Images – Making Separate Panels Appear as One Window  
- Initially each section (header, stats, city, etc.) was a separate image, resulting in visible gaps.  
- Solution: design a single large frame and slice it horizontally: the header draws the top edge, the footer draws the bottom edge, and intermediate slices draw only the side rails.  
- Stacking the slices creates the illusion of one continuous console window.

## Building the City – From Grid to Skyline  
- The city is generated from the contribution graph, mapping commit counts to building heights.  
- Daily updates are automated: a robot runs each night, queries the GitHub API once (instead of many times), and rewrites the README with the new SVGs.  
- Visual details such as “lights on,” color choices (green vs. blue), and skyline silhouettes are calculated programmatically.

## Automation and Secrets  
- A single GitHub Action handles the entire pipeline: fetch contributions, generate SVGs, embed trimmed fonts, and push the updated README.  
- Secrets (API tokens) are stored securely in the Action’s environment variables; they never appear in the public repo.  
- The process runs at a specific time (12:17 UTC) to align with GitHub’s contribution day reset.

## Was It Worth It? – Damage Report and Reflection  
- The project required extensive debugging (image caching, SVG rendering quirks) and added maintenance overhead.  
- The final result is a visually striking, interactive‑looking profile that updates itself daily without manual effort.  
- I invite readers to visit the profile, explore the console, and see the contribution city in action.