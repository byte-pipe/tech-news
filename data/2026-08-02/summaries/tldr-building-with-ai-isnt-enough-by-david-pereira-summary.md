---
title: "Building with AI Isn't Enough. - by David Pereira"
url: https://dpereira.substack.com/p/building-with-ai-isnt-enough
date: 2026-08-02
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-02T06:02:53.404748
---

# Building with AI Isn't Enough. - by David Pereira

# Building with AI Isn't Enough.

## Know why you’re building
- Clarify audience, value proposition, and personal motivations before starting.
- Identify what you know and what you don’t; confront assumptions with evidence early.
- Example: author’s original site felt dated and inauthentic; goal was a personal site that reflected optimism, thought‑provoking style, and a desire to help others.

## Designing
- Start small: created infographics with Claude Sonnet 4.6, disliked the generic look, switched to Opus and got better results.
- Iterate openly; share early drafts to gather feedback rather than hiding them.
- Feedback highlighted missing personal brand and “soul.”
- Refined design by emphasizing personal traits: thought‑provoking, simple, audacious, handwritten touches.
- Multiple iterations with Claude Design eventually produced a version that resonated with the audience (“hand‑written touch is great,” “authentic and approachable”).

## Building
- Tried specs‑driven development using Claude Cowork to generate a PRD, then let AI code from the specs.
- First attempt produced a site that didn’t match the design; interactions were rough.
- Lessons from a brother’s experience led to a new workflow:
  1. Work bit by bit, not full specs at once.  
  2. Use stronger models for architecture, weaker ones for execution.  
  3. Have Claude Code evaluate Claude Design output and create a design system.  
  4. Implement a single page using that system.  
  5. Iterate page components until they meet expectations.
- Reset repository, switched from Claude Pro to Claude Max, completed implementation in about a day after iterative fixes.

## Shipping (And Breaking Stuff)
- Released a core version of the site to a small audience, even though blog, contact form, etc., were still missing.
- Leveraged accumulated feedback to confirm direction before full launch.

## Key lessons
- Knowing your purpose and brand is essential; the first AI‑generated options will look ordinary.
- Diverge widely, then converge on designs that truly reflect you and your audience.
- Build foundations first—design system and single pages—before scaling.
- Iterate continuously, using appropriate AI models for each stage, to keep the product authentic and functional.