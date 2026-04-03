---
title: 'Director''s Cut AI: A Multimodal Storytelling Toolkit - DEV Community'
url: https://dev.to/koki_oki/directors-cut-ai-a-multimodal-storytelling-toolkit-22d9
site_name: devto
fetched_at: '2025-09-16T11:06:09.200326'
original_url: https://dev.to/koki_oki/directors-cut-ai-a-multimodal-storytelling-toolkit-22d9
author: Koki Koki
date: '2025-09-14'
description: This is a submission for the Google AI Studio Multimodal Challenge What I Built I built... Tagged with devchallenge, googleaichallenge, ai, gemini.
tags: '#devchallenge, #googleaichallenge, #ai, #gemini'
---

This is a submission for theGoogle AI Studio Multimodal Challenge

## What I Built

I built Director's Cut AI, an all-in-one web tool that transforms a user's creative spark into a complete, multi-stage cinematic production plan. It acts as a creative co-pilot, guiding the user from a simple idea to finished video scenes through a seamless, six-step process:

1. Inspiration: Users upload three images to set the mood and select a genre and length for their project.
2. Narrative: The AI analyzes the images and prompts to generate a compelling short story.
3. Storyboard: The narrative is automatically broken down into a detailed, scene-by-scene storyboard.
4. Style Frame: Users select key shots and a visual style (e.g., "Cinematic," "Anime," "Film Noir") to generate high-quality still images that define the project's aesthetic.
5. Blueprint: The AI synthesizes all the creative decisions into a machine-readable JSON blueprint, ready for video generation.
6. Videos: Finally, the blueprint is used to generate dynamic, 8-second video clips for each scene in the story.

This applet solves the problem of the "blank page" for creators by providing a structured yet flexible workflow to develop a visual story from the ground up, leveraging Google's powerful multimodal AI at every step.

## Demo

Here is a link to the deployed applet:https://director-s-cut-ai-30971010556.us-west1.run.app

## How I Used Google AI Studio

Google AI Studio was instrumental in prototyping and refining the prompts for this project. I used it extensively to test the interactions between different modalities and to structure the expected outputs.

The applet integrates several Google AI models:

Gemini 2.5 Flash(gemini-2.5-flash): This was the workhorse for all language and data-structuring tasks. I used it for:

* Generating the initial narrative from a combination of images and text.
* Parsing the narrative into a structured JSON storyboard using Gemini's JSON mode with a defined responseSchema.
* Creating the final, machine-readable JSON blueprint that drives the video generation. The reliability of the JSON output was critical for the app's pipeline.

Imagen 4(imagen-4.0-generate-001): This model was used to generate the cinematic style frames. The prompt was engineered to combine the storyboard action with a specific artistic style and even render text overlays, providing a true preview of the final look.

Veo 2(veo-2.0-generate-001): The final step of the process uses Veo 2 to bring the story to life. The detailed prompts from the JSON blueprint are fed to the model to generate high-quality, coherent video scenes.

## Multimodal Features

Director's Cut AI is fundamentally multimodal, creating a chain of transformations from one media type to another.

* Image + Text to Text (Narrative Generation): The app's starting point is a multimodal prompt. It combines the visual information and mood from user-uploaded images with textual instructions (genre, length) to produce a cohesive narrative. This grounds the AI's creativity in the user's specific vision, making the resulting story feel personal and relevant.
* Text to Image (Style Frame Visualization): The app translates descriptive text from the storyboard (shot type, camera angle, action) and the user's chosen aesthetic into rich, detailed still images. This is a crucial feedback loop that allows the user to visually confirm the creative direction before committing to the more time-intensive video generation step, bridging the gap between imagination and a concrete visual.
* Text to Video (Cinematic Scene Generation): The culmination of the user's journey is the text-to-video feature. The structured text prompts from the JSON blueprint are converted into dynamic video clips. This powerful feature completes the creative process, transforming the entire plan into a tangible cinematic product.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
