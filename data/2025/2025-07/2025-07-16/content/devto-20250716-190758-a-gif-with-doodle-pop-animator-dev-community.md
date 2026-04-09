---
title: A GIF with Doodle-Pop Animator - DEV Community
url: https://dev.to/aibughunter/make-a-gif-with-doodle-pop-animator-3g5f
site_name: devto
fetched_at: '2025-07-16T19:07:58.289028'
original_url: https://dev.to/aibughunter/make-a-gif-with-doodle-pop-animator-3g5f
author: AI Bug Slayer 🐞
date: '2025-07-12'
description: 'This post is my submission for DEV Education Track: Build Apps with Google AI Studio. What... Tagged with deved, learngoogleaistudio, ai, gemini.'
tags: '#deved, #learngoogleaistudio, #ai, #gemini'
---

Education Track: Build Apps with Google AI Studio

This post is my submission forDEV Education Track: Build Apps with Google AI Studio.

## What I Built

I developed the "Doodle-Pop Animator," a delightful web application designed to bring your imagination to life by transforming simple text prompts into vibrant, looping animated doodles. The goal was to create an intuitive and fun tool that allows anyone, regardless of their artistic skill, to create shareable animations in seconds.

The application's magic lies in a sophisticated two-step AI pipeline. First, a user's initial idea is sent togemini-2.5-flash, which acts as a "Creative Director." I've given it a system instruction to take a simple prompt (e.g., "a dog on a skateboard") and expand it into a richly detailed, imaginative scene ("A joyful corgi with a bright red helmet, wobbling excitedly on a neon green skateboard with rocket boosters").

This enhanced, more vivid description is then passed to the second AI,imagen-3.0-generate-002. This model acts as the "Animator," generating a sequence of distinct image frames that capture the essence of the creative prompt. The app assembles these frames into a seamless, animated GIF right in the browser using thegifenclibrary, providing a final result that is both colorful and full of energy.

## Demo

Here is a quick demonstration of the Doodle-Pop Animator in action. The interface is designed to be clean and engaging, with a tabbed view that lets you watch the individual frames get generated before seeing the final, animated output.

Ready to create your own animated masterpiece? You can try the app live here:Doodle-Pop

## My Experience

This project was a fantastic and insightful journey into the power of multi-modal AI and creative engineering. My most significant takeaway was the effectiveness of chaining AI models together, where each model contributes its specialized strength to achieve a more refined and compelling result. Usinggemini-2.5-flashto first enrich the prompt before image generation proved to be far more effective than relying on a single model for the entire task.

A major part of the development process was dedicated to prompt engineering. It was a creative challenge to craft the perfect system instructions. Forgemini-2.5-flash, the key was to encourage it to be whimsical and "hyper-colorful." Forimagen-3.0-generate-002, the prompt needed to specify a consistent "doodle" style across all frames while also asking for slight variations to create the illusion of movement. This iterative refinement was crucial to achieving the app's signature look.

I was genuinely surprised by how much the AI felt like a creative partner rather than just a tool. There were moments whengemini-2.5-flashwould interpret a prompt in a completely unexpected yet brilliant way, leading to animations that were far more imaginative than what I had initially envisioned. It was a powerful lesson in how AI can not only execute but also elevate human creativity.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
