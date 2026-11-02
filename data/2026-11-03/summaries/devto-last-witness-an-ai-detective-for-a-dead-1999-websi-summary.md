---
title: Last Witness: an AI detective for a dead 1999 website, graded on its ghosts - DEV Community
url: https://dev.to/p0rt/last-witness-an-ai-detective-for-a-dead-1999-website-graded-on-its-ghosts-4bbe
date: 2026-10-28
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-11-03T06:08:20.260819
---

# Last Witness: an AI detective for a dead 1999 website, graded on its ghosts - DEV Community

# Last Witness: an AI detective for a dead 1999 website

## In plain words
- Last Witness is a detective‑style game about the vanished 1999 online community “Lighthouse Network.”  
- The only remnants are fragmented home pages, forum threads, a guestbook, emails and server logs.  
- An open‑weight AI model named Gemma runs locally on the player’s computer and tries to reconstruct what happened, citing each claim with a sentence‑id and exact quote.  
- Players can object to claims, force the AI to defend or withdraw them, and finally submit a ten‑question reconstruction that is compared to a sealed true history.  
- Claims unsupported by the archive become “ghosts.” The game therefore tests how much an AI can be trusted when it must rely on provided sources.

## What I built
- The fictional community was created first: eight members, thirty‑two dated events, one falsified recording, a purge, and a botched migration that looks like a cover‑up.  
- The true timeline is stored in a hidden repository; Gemma never sees it.  
- A damaged DAT tape (“BEACON FULL 17‑OCT‑99”) provides 58 of 151 files (≈38 % readable). The rest are broken links.  
- Players open documents; Gemma can only read what has been opened and must cite each statement (e.g., `A36:s12 "That's two recordings joined together."`).  
- After the “Reveal” phase, every AI claim is checked against the sealed truth: solid claims stay, unsupported ones fade as ghosts, and missed events are shown with their hidden evidence.

## Demo
- Play a recorded run in the browser without installing: https://p0rt.github.io/last-witness/  
- The replay shows the full interaction, citation highlighting, and the final comparison of player and AI answers.  
- To run the live game locally:  
  ```bash
  ollama pull gemma4:e4b
  pip install -r requirements.txt
  make serve   # http://localhost:8000
  ```

## Code
- Repository: `P0rt/last-witness` (MIT license).  
- Stack: Python (FastAPI, SQLite FTS5) backend, React + TypeScript frontend, ~4,700 lines of code plus a hand‑crafted 151‑file 1999 website.  
- Video overview: https://youtu.be/cc44d7dajxM  

## How I built it
- **Three isolated layers**:  
  - `world/` holds the sealed true history.  
  - A seeded script destroys it into `dataset/archive.json`, the only data the AI can read.  
  - The evaluator alone can access `world/` after Reveal; build tests fail if any other module touches it.  
- **Controlled destruction**:  
  - Story‑critical files always survive (some with intentional damage).  
  - All other files survive with 55 % probability.  
  - A validator guarantees that every observable event has word‑for‑word evidence, contradictions survive on both sides, and no single file answers more than three reconstruction questions.  
- **Citation system**:  
  - Sentences are indexed (`A36:s12`).  
  - Constrained decoding prevents the model from citing non‑existent sentences.  
  - A fuzzy‑match (≥85 % similarity) checks that the quoted text matches the cited sentence; mismatches become ghosts.  
- **Benchmark numbers**:  
  - Tested Gemma 4:e4b (with and without “thinking”) and Gemma 4:e2b on a 4‑core CPU, temperature 0.6, three runs per condition.  
  - Without the archive, the model guessed the cover story, averaging 7.67/10 wrong answers; it labeled 29/30 guesses as speculative.  
  - When allowed to answer “unknown,” it correctly answered “unknown” to all ten questions.  
  - With the archive, the model stopped guessing, achieving 5.67/9 correct answers (the tenth question is truly unanswerable).  

## The numbers (summary)
- **Without archive**: ~77 % of answers wrong, many speculative guesses, high ghost rate.  
- **With archive**: No wrong answers, zero invented quotes, only the deliberately unanswerable question remains “unknown.”  

The project demonstrates a concrete experiment on AI reliability when source material is limited and verifiable.