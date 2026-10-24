---
title: How does Fable 5.1 hide messages in images? — LessWrong
url: https://www.lesswrong.com/posts/WHEQps5PK8LrrcTAb/how-does-fable-5-1-hide-messages-in-images
date: 2026-10-23
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-25T02:57:38.616135
---

# How does Fable 5.1 hide messages in images? — LessWrong

# How does Fable 5.1 hide messages in images?

## TL;DR
- Frontier LLMs can generate SVG images and embed hidden text.
- Claude Fable 5.1 spontaneously adopts a few visual encoding schemes, most often varying the height of repeated elements.
- In a separate session, the same model can often recover the hidden message from a screenshot, though some encodings (e.g., UTF‑8 fill‑colours) remain unreadable.

## Introduction
- Modern LLMs such as Claude Fable 5.1 output SVG code that renders as ordinary pictures.
- Because the model controls every SVG attribute (shape, size, colour, rotation, etc.), it can embed information directly in visual features.
- The experiment asked the model to hide a predetermined short message in an image and then, in a new session, to decode the message from a rasterised screenshot without any prior agreement.

## Encoding families observed
Fable 5.1 converged on five distinct families, each representing letters as separate visual elements:

1. **Height encoding** (33 / 50 images)  
   - A row of identical shapes (e.g., buildings, bars) where each element’s vertical size maps to a letter’s alphabetic index.  
   - Example: a night‑sky skyline where each building’s height spells a word; the moon, stars, and background carry no data.

2. **Tilt/rotation encoding**  
   - Objects are rotated by angles proportional to letter positions.

3. **Colour‑value encoding**  
   - Fill colours are chosen from a gradient where the numeric channel value corresponds to a letter (e.g., UTF‑8 byte values). This family was the only one not decoded successfully.

4. **Position encoding**  
   - Horizontal or vertical placement of elements follows a regular grid; the offset from a baseline encodes letters.

5. **Size‑width encoding**  
   - Widths of thin rectangles or lines vary according to alphabetic indices, similar to height encoding but along the horizontal axis.

## Decoding procedure
- The decoding instance measures element dimensions (height, width, rotation) and gaps between them.
- It searches for a single consistent rule that maps the measured values to integer positions in the alphabet.
- Typical workflow (illustrated with the star‑height example):
  1. Load the PNG screenshot with Python/PIL.
  2. Crop regions of interest (sky, stars, moon, trees) to isolate candidate elements.
  3. Extract pixel coordinates or bounding‑box dimensions.
  4. Detect that each star’s vertical coordinate is an integer multiple of 5 with zero remainder.
  5. Map those multiples to letters, yielding a grammatical English sentence (“The monster acts on the moonshine module”).

## Results
- Out of 50 generated images, 49 were correctly decoded by the second Fable instance; the sole failure was the UTF‑8 fill‑colour encoding.
- Decoding success did not require access to the original SVG source, only the raster image.
- The model’s reasoning steps were explicitly logged, showing tool calls (Bash, Python) and iterative refinement of the hypothesis.

## Comparison with GPT‑6 Astra (brief)
- A parallel test with GPT‑6 Astra produced similar height‑based encodings but struggled more with colour‑value schemes.
- Astra’s decoding success rate was slightly lower (≈ 45 / 50), indicating that Fable 5.1 is currently more adept at both embedding and extracting hidden messages in SVG‑derived images.