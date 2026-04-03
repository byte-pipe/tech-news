---
title: AI Chart Animator - DEV Community
url: https://dev.to/prakash_verma_e6f7ea047c0/ai-chart-animator-2mgm
site_name: devto
fetched_at: '2025-09-17T11:06:05.637077'
original_url: https://dev.to/prakash_verma_e6f7ea047c0/ai-chart-animator-2mgm
author: Prakash Verma
date: '2025-09-15'
description: This is a submission for the Google AI Studio Multimodal Challenge What I Built I built... Tagged with devchallenge, googleaichallenge, ai, gemini.
tags: '#devchallenge, #googleaichallenge, #ai, #gemini'
---

This is a submission for theGoogle AI Studio Multimodal Challenge

## What I Built

I built theAI Chart Animator, a web application that breathes life into static data visualizations. The app solves a common problem for presenters, marketers, and data analysts: static charts are informative but often visually unengaging. Creating animated versions traditionally requires specialized software and significant manual effort.

AI Chart Animator streamlines this entire process. A user can upload an image of a standard bar or line chart, and through a sophisticated multimodal AI pipeline, the application automatically generates a stunning, futuristic animation of that chart. The result is a dynamic video that makes data more impactful and memorable.

The core workflow is a three-step process powered by AI:

1. Stylize:A Google Gemini model transforms the original chart into a high-tech, futuristic version, which serves as the animation'send frame.
2. Deconstruct:The same model then intelligently removes the data elements (the bars or lines) from the futuristic chart to create a clean, empty frame, which serves as the animation'sstart frame.
3. Animate:A third-party video generation model (Hailuo AI) is used to create a smooth animation that transitions between the start and end frames, showing the data appearing dynamically.

## Demo

I couldn't deploy this app to cloud run, because my credits were over for Minimax API, and I didn't had credit card for cloud run deployment. But, here is the aistudio app link, through which you can see the app and its code:https://ai.studio/apps/drive/18mGw-J40Vjon-elGWBWBYyla-J5fMOIY. Anyone with this public link can access the app.

You can see the AI Chart Animator in action in this full walkthrough video:

Below is a visual representation of the app's three-step generation process:

Original Chart

Step 1: Futuristic End Frame

Step 2: Empty Start Frame

(Your uploaded chart image)

(AI-generated futuristic style)

(AI-generated empty frame)

## How I Used Google AI Studio

I leveraged Google AI Studio's powerful multimodal capabilities as the core engine for the image processing pipeline. The entire image transformation process is powered by thegemini-2.5-flash-image-previewmodel. My implementation uses a chained, multi-step approach where the output of one multimodal prompt becomes the input for the next.

Step 1: Initial Transformation (Image + Text -> Image)

I send the user's uploaded chart image along with a detailed text prompt to Gemini. The prompt instructs the model to reimagine the chart with a futuristic aesthetic while critically preserving the original data.

Prompt for a Bar Chart:

"Transform this bar chart into a 3D futuristic masterpiece. Give it a sleek, dark theme with vibrant neon highlights and a high-tech feel. The bars should have a sense of depth and perspective. Keep the overall structure, data, and labels intact but render them in a matching 3D style."

Step 2: Content Removal (Image + Text -> Image)

The newly generated futuristic chart from Step 1 is then sentbackto the Gemini model. This time, it's accompanied by a different text prompt that acts as a precise surgical instruction to deconstruct the image.

Prompt to remove bars from the futuristic chart:

"From this 3D futuristic bar chart image, perfectly remove only the colored bars. It is crucial to leave the 3D axes, axis labels, grid lines, title, and background completely intact, preserving their perspective and style. The output should be the empty 3D chart frame."

This two-step process, driven entirely by Gemini's ability to understand and manipulate image content based on text commands, is what creates the necessary start and end frames for the final animation.

## Multimodal Features

The core of this project is its sophisticated use ofImage + Text -> Image Generationto deconstruct and rebuild a data visualization for animation. This goes far beyond simple image generation and leverages Gemini's deep contextual understanding.

* Context-Aware Stylization:The first multimodal feature is the ability to apply a complex artistic style (futuristic, neon) to a structured image (a chart) without corrupting the underlying information. The model successfully understands the prompt's intent to "keep the data intact," demonstrating a crucial comprehension of both the visual input and the text constraints. This enhances the user experience by transforming a mundane chart into something visually exciting and professional.
* Intelligent Object Removal:The second, more advanced multimodal feature is the ability to selectively remove specific elements from an image based on a natural language command. Asking the model to "perfectly remove only the colored bars" or "remove the lines from the line graphs" requires it to identify what a "bar" or "line" is within the context of the chart, isolate it from the background and axes, and intelligently fill in the space behind it. This is a powerful capability that automates what would otherwise be a tedious manual task in an image editor, making the entire animation workflow feasible and fast for the end-user.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
