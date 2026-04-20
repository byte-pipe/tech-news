---
title: A Picture Is Worth a Thousand Tokens - Repaint
url: https://repaint.com/blog/picture-is-worth-a-thousand-tokens
date: 2026-04-15
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-15T06:04:37.665935
---

# A Picture Is Worth a Thousand Tokens - Repaint

# A Picture Is Worth a Thousand Tokens - Repaint

## Introduction
- My role at Repaint is to make AI generate websites that actually look good, which proved surprisingly hard.
- Without strong guidance, AI models fall into a recognizable “AI website” aesthetic with generic layouts, overused fonts, and occasional unreadable buttons.

## Experiments with Basic Prompts
- **Landing page for “Lighthouse Analytics”** (Claude Code): produced a minimal, generic site with the typical AI tropes.
- **Therapist website** (Claude Code + image generation): the model reused the same green‑button style despite the different domain, showing the default AI style is universal.

## Strategies to Improve AI‑Generated Websites

### Design Systems
- Pre‑define colors, fonts, rounding, and shadows before prompting.
- Results: fewer glaring color mistakes and a background image appeared, but layouts, content density, and overall structure remained the same.
- Conclusion: a design system supplies a palette but does not teach composition.

### Coaching (Design Skill Prompt)
- Provided the model with a detailed set of design instructions covering purpose, tone, constraints, differentiation, and aesthetic guidelines (typography, color, motion, spatial composition, backgrounds).
- Example output: a therapist site with softer fonts and a unique button style, looking more appropriate for the domain.
- Findings:
  - Custom instructions improve visual quality but do not eliminate repetitive patterns.
  - The model swaps one set of overused fonts (Inter, Roboto) for another (Jost, Cormorant Garamond), showing it still defaults to familiar choices.
  - Enforcing “never use generic fonts” leads to new overused fonts, limiting flexibility.

### Reference Images
- Supplied a screenshot of a desired design and asked the model to recreate a similar therapist site.
- Outcomes:
  - The model generated new layout structures it normally would not produce (e.g., avoided half‑screen images).
  - Images efficiently convey layout, spacing, color relationships, and density.
  - Limitations: struggles with complex layouts or animations and reverts to default patterns when additional content is needed.

### Code and Style Templates
- (Briefly mentioned as a brute‑force approach: feeding the model ready‑made code or style templates to steer output.)

## Key Lessons Learned
- AI models have strong, repeatable visual habits that are hard to break even with extensive prompting.
- Design systems reduce obvious errors but cannot guide higher‑level composition.
- Coaching prompts can steer aesthetics toward a specific tone, yet the underlying pattern repetition persists.
- Reference images are powerful for conveying holistic design intent but are fragile for complex or extended content.
- Over‑constraining the model (e.g., banning specific fonts) simply shifts the overuse to other defaults.
- Achieving truly distinctive, production‑grade designs requires intentional, bold aesthetic direction combined with careful implementation, not just more prompts.

## Conclusion
- The biggest unlock is when AI can handle design decisions without a human specifying every detail, but current models still need strong, context‑aware guidance and creative prompting techniques to move beyond the generic “AI slop” aesthetic.
