---
title: I Asked AI to Write My Commit Messages It Was Embarrassing. - DEV Community
url: https://dev.to/harsh2644/i-asked-ai-to-write-my-commit-messages-it-was-embarrassing-a6i
date: 2026-06-16
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-06-19T01:20:25.618538
---

# I Asked AI to Write My Commit Messages It Was Embarrassing. - DEV Community

# Summary of “I Asked AI to Write My Commit Messages It Was Embarrassing”

## Background
- The author asked an AI to generate a commit message for a simple bug‑fix.
- The AI returned a vague, four‑word message: “Updated stuff. Fixed things. Improved performance.”
- The author felt the message was soulless and useless for future readers.

## What Commit Messages Used to Mean
- Previously, the author spent a short amount of time writing a sentence that explained **why** a change was made, not just **what** changed.
- Good commit messages served as a small gift to future maintainers, providing context, trade‑offs, and links to tickets.
- Over time, the author stopped caring about this practice.

## AI’s Commit Messages: A Gallery of Shame
- Example messages produced by the AI:
  1. “Fixed stuff.” – no context, no reason.
  2. “Improved performance.” – no details about scope, magnitude, or method.
  3. “Bug fixes and other improvements.” – overly generic, true of almost any commit.
- Even with full access to the diff, the AI chose to output empty, generic statements.
- The messages are useless to both humans and other AIs trying to understand the code history.

## Why It Actually Matters
- Commit messages are not decorative; they help teammates, reviewers, and future self understand decisions.
- A good message answers the question: *Why did we do this?*
- The AI’s hollow messages reflected the author’s own recent habit of writing vague messages.
- The embarrassment stemmed from seeing personal laziness mirrored back by the AI.

## Lesson Learned
- The author returned to writing their own commit messages, spending only a few seconds per commit.
- AI remains useful for code generation, refactoring, and autocomplete, but not for capturing the story behind a change without intentional effort.
- The key is to care enough to articulate the rationale, even briefly.

## Open Question
- The author invites readers to share the worst commit message they’ve seen or written, starting with their own example: “Fixed stuff.”