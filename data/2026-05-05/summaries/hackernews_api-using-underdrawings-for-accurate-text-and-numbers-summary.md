---
title: Using “underdrawings” for accurate text and numbers
url: https://samcollins.blog/underdrawings/
date: 2026-05-02
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-05T00:52:34.712905
---

# Using “underdrawings” for accurate text and numbers

# Using “underdrawings” for accurate text and numbers

## Overview
- The author presents a technique that enables AI‑generated images to contain reliable text and numeric information.
- Demonstrated with a game board of 50 numbered stepping stones; standard models fail, while Gemini 3.0 Pro succeeds when the method is applied.

## The Underdrawing Method
- An A/B test compares results:
  - **Without underdrawing**: Gemini 3 Pro and ChatGPT Images 2 produce visually appealing images but the numbers are incorrect or missing.
  - **With underdrawing**: Gemini 3.0 Pro generates an image with correct numbers, proper sequencing, and the intended spiral layout.

## How It Works
- **Leverage each tool’s strength**
  1. Deterministic tools (SVG, HTML, Python, Mermaid) create precise layouts of text and numbers.
  2. Generative image models add artistic style but are unreliable for exact text placement.
- **Two‑layer process**
  - **Layer 1 – Underdrawing**: Produce a deterministic image containing the numbers/text in the exact positions and orientations needed.
  - **Layer 2 – Painting**: Feed the underdrawing together with a descriptive text prompt into a multimodal image model (image‑plus‑text input → image output) to obtain the final stylized picture.

## Example Workflow
- **Step 1: Create the underdrawing**
  - Generate an SVG of 50 stepping stones arranged in a counter‑clockwise spiral, each stone numbered 1‑50 and shaped differently (circle, square, triangle, hexagon).
- **Step 2: Image‑to‑image generation**
  - Provide the SVG image to Gemini 3.0 Pro with a prompt such as “transform into a photographed claymation diorama of artisan chocolates and candies, low‑angle tilted perspective,” resulting in a visually rich final image that retains the correct numbers.

## Remarks
- The entire pipeline can be automated with code generators like Claude or Codex.
- The method improves accuracy but may not be perfect on every run.