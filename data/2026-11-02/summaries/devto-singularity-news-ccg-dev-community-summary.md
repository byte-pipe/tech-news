---
title: Singularity News :: CCG - DEV Community
url: https://dev.to/pengeszikra/singularity-news-ccg-5ejk
date: 2026-10-31
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-11-02T08:49:06.367086
---

# Singularity News :: CCG - DEV Community

# Summary of Hacktoberfest Open‑Source AI Challenge Submission

## What the Project Is
- A Collective Card Game (CCG) created for the “Ghost in the Machine” week of the Hacktoberfest Open‑Source AI Challenge.  
- Built on the Flogons card‑game system, using CSS‑based 3D rendering and pure HTML, resulting in a no‑build development workflow.  
- Packaged as a Progressive Web App, so it can be installed on mobile devices.  
- Includes an **Auto:on** feature that lets the game play itself like a movie.  
- Supports 4‑ and 7‑player tables that play against AI bots; no online multiplayer.

## Gameplay Highlights
- Every card can be “interviewed,” providing narrative content tied to the Singularity News feed.  
- The final outcome (epilogue article) is generated with substantial AI assistance.  
- All backstory and characters are fictional creations from the author’s Singularity News feed and are unrelated to real or fictional individuals.

## Technical Details
- Primary AI model: **Gemma‑4** (gemma‑4‑26b‑a4b‑it) accessed via the Gemini API.  
- Fallback model: **gpt‑oss‑120b** on Groq, selectable in‑game via an AI switch.  
- The full prompt workflow is documented in `PROMPTS.md` (originally written in Hungarian).  
- Open‑weight models give the freedom to run the same prompts on different back‑ends now and later, allowing a switch to a local model to save tokens and money without rewriting code.  
- Development leveraged previously written solutions and a “Pure HTML + No Build System” philosophy.

## Resources
- **Live demo:** https://singularity-news-ccg.vercel.app/  
- **Source code:** https://github.com/Pengeszikra/singularity-news-ccg  
- **Prompt documentation:** `PROMPTS.md` in the repository.

## Why Open Innovation Matters (author’s view)
- Open‑weight models enable flexibility: the same prompts work on Gemma‑4, gpt‑oss‑120b, or a future local model, avoiding vendor lock‑in and reducing costs.

## Prize Category Details
- **Gemma‑4** is the primary model for:  
  - Mr. Slop’s news ticker  
  - Character interviews  
  - Intro spoken by the first flipped card  
  - Final epilogue article built from collected characters  
- **gpt‑oss‑120b** serves as a manual fallback selectable during gameplay.

## Additional Notes
- The author observed Claude embedding images directly into `index.html`, illustrating AI’s literal interpretation of prompts.  
- Readers are invited to continue reading, comment, and share the project.