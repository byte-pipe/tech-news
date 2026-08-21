---
title: nobuzz/README.md at main · adnanakil/nobuzz · GitHub
url: https://github.com/adnanakil/nobuzz/blob/main/README.md
date: 2026-08-22
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-22T06:00:49.564111
---

# nobuzz/README.md at main · adnanakil/nobuzz · GitHub

# NoBuzz README Summary

## Overview
- **NoBuzz** provides a Claude skill (`/debuzz`) that rewrites Claude’s overly‑stylized responses into plain English.
- The tool is humorously named “Claudette” internally, but avoids trademark issues.

## Problem
- Claude often answers in a “click‑bait” TED‑talk style, adding unnecessary flair and length.
- This makes technical explanations hard to read, especially for straightforward bug reports or updates.

## Solution
- The skill captures Claude’s last reply, sends it to the Gemini CLI, and returns Gemini’s plain‑English translation verbatim.
- No additional processing is done by Claude, preventing the original verbose voice from re‑appearing.

## Modes (Audience‑Specific Output)
- **colleague** (default): Full technical detail, all file paths and code blocks, no theatrics.
- **manager**: Concise summary for a technical‑adjacent manager; about one‑third the length, no code snippets.
- **director**: Executive‑level brief (3‑5 sentences) covering outcome, impact, and any ask; assumes ~30 seconds of attention.

## Installation
1. Clone the repository: `git clone https://github.com/adnanakil/nobuzz`.
2. Copy the `debuzz` directory into Claude’s skills folder (e.g., `~/.claude/skills/`).
3. Install requirements:
   - Claude Code environment.
   - Gemini CLI (`npm install -g @google/gemini-cli`) and authenticate (`gemini use/auth` or set `GEMINI_API_KEY`).

## Usage
- Command format: `/debuzz [mode] [text]`.
- If no text is supplied, the skill rewrites Claude’s previous reply.
- The skill also reacts to natural language triggers such as “say that in normal english”.

## How It Works
- Writes Claude’s reply to a temporary file.
- Pipes the file through `gemini -p "<plain-English style instructions>"`.
- Prints Gemini’s output directly; on Gemini errors, the original Claude rewrite is shown as a labeled fallback.

## License
- MIT.