---
title: 'AdVariant Pro: Your AI Creative Agency in a Click - DEV Community'
url: https://dev.to/debora_fernandes_69cb16d1/advariant-pro-your-ai-creative-agency-in-a-click-f2o
site_name: devto
fetched_at: '2025-09-17T11:06:05.756933'
original_url: https://dev.to/debora_fernandes_69cb16d1/advariant-pro-your-ai-creative-agency-in-a-click-f2o
author: Debora Fernandes
date: '2025-09-13'
description: This is a submission for the Google AI Studio Multimodal Challenge What I Built built... Tagged with devchallenge, googleaichallenge, ai, gemini.
tags: '#devchallenge, #googleaichallenge, #ai, #gemini'
---

Google AI Challenge Submission

This is a submission for theGoogle AI Studio Multimodal Challenge

## What I Built

built AdVariant Pro, an AI-powered Marketing Strategist that transforms a simple product photo into a complete, ready-to-launch ad campaign. It solves one of the biggest challenges for marketers: creating high-quality, personalized campaign assets quickly and affordably.

Traditionally, creating a single ad requires a photographer, a copywriter, a strategist, and a designer. My applet consolidates these roles, allowing a user to upload a product image, define an audience, and receive a full campaign package in seconds.

With AdVariant Pro, a user can:

* Generate Complete Ad Scenes: Upload a product image (even with a plain background) and the app will intelligently place it into a newly generated, contextually relevant, and photorealistic scene tailored to a specific audience.
* Create Audio Pitches: Instantly generate a compelling 15-second "elevator pitch" for the campaign, voiced by a high-quality AI from ElevenLabs, ready for social media videos.
* Receive AI-Powered Creative Assistance: Get instant suggestions for catchy slogans or expand a brief audience description into a detailed marketing persona, all powered by Gemini.
* Achieve Strategic Composition: The AI acts as an Art Director, analyzing the visual composition to strategically position the slogan for maximum impact and legibility.

## Demo

You can try the live applet here:https://advariant-pro-gerador-de-campanhas-de-an-ncios-790832384921.us-west1.run.app/

Here is a quick overview of the workflow:

1. Upload Your Product & Define Your Audience
The user starts by uploading their product image and describing the target customer. The interface is mobile-first and multilíngue (EN/PT).

1. Generate Your Campaign (Visual + Audio)With a single click, AdVariant Pro generates a complete ad scene and a 15-second audio pitch.
2. Hyper-Personalized ResultsThis shows the power of the tool. Using the exact same uploaded product photo, AdVariant Pro created two completely different campaign packages (visuals and audio pitches) for two unique audiences.

Video Demo:https://youtu.be/P2m-3_arVkU

## How I Used Google AI Studio

Google AI Studio was the command center for this project, enabling a seamless workflow from prompt engineering to final deployment.

* Rapid Prototyping: I used AI Studio to meticulously craft and test the multi-step prompts. The ability to iterate quickly on the "AI Art Director" logic was essential to achieving the high-quality scene generation and strategic slogan placement.
* Seamless Deployment: The "Deploy to Cloud Run" feature is a game-changer. It handled the entire containerization and deployment pipeline, allowing me to focus on building features rather than managing infrastructure. This was critical for a fast-paced challenge.
* Model Selection: I orchestrated multiple Gemini models to act as a specialized creative team:Gemini 1.5 Flash: Used as the central "brain" for all reasoning and text tasks: analyzing the user's text inputs, generating slogan suggestions, writing the script for the audio pitch, and acting as the main Art Director.gemini-1.5-flash-image-preview: Used as the "AI Photographer" to generate the final, high-quality ad scene based on the detailed instructions from the Art Director.
* Gemini 1.5 Flash: Used as the central "brain" for all reasoning and text tasks: analyzing the user's text inputs, generating slogan suggestions, writing the script for the audio pitch, and acting as the main Art Director.
* gemini-1.5-flash-image-preview: Used as the "AI Photographer" to generate the final, high-quality ad scene based on the detailed instructions from the Art Director.

## Multimodal Features

AdVariant Pro is built from the ground up on a sophisticated multimodal pipeline that mimics a real-world creative agency workflow.

1. Core Feature: Image-to-Scene Generation (Image + Text → Image)
This is the heart of the applet. The user provides an image of their product, and Gemini performs a complex multimodal task:

* It understands the subject of the uploaded image.
* It imagines a new, contextually appropriate background scene based on the text description of the target audience.
* It generates a new, cohesive image, seamlessly integrating the original product while matching lighting, shadows, perspective, and reflections to make it look completely natural.

1. Full Campaign Pipeline (Image + Text → Text → Audio)
The app creates more than just a picture; it creates a campaign. This involves a multi-step, cross-modality process orchestrated by Gemini:

* Step A (Visuals): Gemini first generates the visual ad scene as described above.
* Step B (Scriptwriting): Based on the product, the audience, and the visuals it just created, Gemini then writes a concise and persuasive 15-second "elevator pitch" script.
* Step C (Voice Generation): This script is then passed to the ElevenLabs API to generate a high-quality, ready-to-use audio track.

This process, which starts with an image and ends with a unique audio clip, demonstrates a powerful and practical application of multimodal AI to solve a real-world marketing challenge. It transforms the user's input into a rich set of campaign assets, not just a single output.

By: Debora Fernandes

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
