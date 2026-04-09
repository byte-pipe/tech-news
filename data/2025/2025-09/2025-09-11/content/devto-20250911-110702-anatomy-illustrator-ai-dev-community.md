---
title: Anatomy Illustrator AI - DEV Community
url: https://dev.to/ha3k/anatomy-illustrator-ai-2a9e
site_name: devto
fetched_at: '2025-09-11T11:07:02.228540'
original_url: https://dev.to/ha3k/anatomy-illustrator-ai-2a9e
author: Ha3k
date: '2025-09-07'
description: This is a submission for the Google AI Studio Multimodal Challenge What I Built I built... Tagged with devchallenge, googleaichallenge, ai, gemini.
tags: '#devchallenge, #googleaichallenge, #ai, #gemini'
---

This is a submission for theGoogle AI Studio Multimodal Challenge

## What I Built

I builtAnatomy Illustrator AI🎨, a web app designed to take the headache out of creating educational diagrams.

Have you ever needed a specific anatomical illustration for a presentation or study guide, only to find nothing thatquitefits?You might find a diagram of the heart, but it's missing the labels you need. Or you find one with the right labels, but the style is all wrong.

Anatomy Illustrator AI solves this problem.

It's a simple, two-step tool for anyone—students, teachers, and medical creators—to generate beautiful, custom-labeled anatomical diagrams on the fly.

Step 1:You describe the structure you want to see.Step 2:You list the labels you want to add.

The AI handles the rest, giving you a clean, accurate, and ready-to-use illustration in seconds. It's like having a professional medical illustrator at your fingertips. 🧠✨

## Demo

Here's a look at the applet in action!

You can see the app here

1. The User Interface

The app starts with a clean and focused interface. You have two main inputs: one for describing the anatomical structure and another for listing the labels.

2. Image Generation & Selection

After you submit your prompt, the app uses Imagen 4 to generate two high-quality illustrations. This gives you creative control to pick the one that best matches your vision.

3. AI-Powered Labeling

Once you select an image, Gemini gets to work. It analyzes the image and your text list to add clear, accurate labels with leader lines. The final result is a polished, professional diagram.

## How I Used Google AI Studio

Google AI Studio was my sandbox for bringing this idea to life. I used it extensively to test and refine the prompts that power the entire experience.

My application relies on a powerful, two-stage multimodal pipeline:

1. Image Generation:I use theimagen-4.0-generate-001model for the initial creation step. I experimented in AI Studio to craft a prompt that consistently produces clean, textbook-quality illustrations with neutral backgrounds, perfect for labeling.
2. Image Editing & Labeling:This is where the magic happens. I leverage thegemini-2.5-flash-image-previewmodel. My prompt instructs the model to take aninput imageand atext string of labelsand intelligently add them to the illustration. AI Studio was essential for figuring out how to ask the model to create professional-looking leader lines and legible text.

This project is a perfect example of chaining different AI models together to create a cohesive and powerful user workflow.

## Multimodal Features

The core of Anatomy Illustrator AI is its deep integration of multimodal features. It's not just using textorimages; it's using themtogetherto create something new.

* Text-to-Image CreationThe journey starts by translating a user's written concept (e.g., "A cross-section of the human eye") into a rich visual. This empowers users to create the exact base image they need without any artistic skill.
* Image-and-Text EditingThis is the most critical multimodal feature. The app sends both animage(the user's selected illustration) andtext(the comma-separated labels) to Gemini in a single request.Why is this so powerful?It enhances the user experience by abstracting away a complex task. Instead of needing a photo editor and a steady hand, the user just provides a list.

The AI understands the visual context of the imageandthe semantic meaning of the labels, placing them accurately.

This creates a seamless, intuitive, and incredibly useful tool for education and content creation.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
