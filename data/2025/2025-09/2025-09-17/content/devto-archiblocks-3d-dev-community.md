---
title: ArchiBlocks 3D - DEV Community
url: https://dev.to/arunavmaitra/archiblocks-3d-3ink
site_name: devto
fetched_at: '2025-09-17T11:06:05.821406'
original_url: https://dev.to/arunavmaitra/archiblocks-3d-3ink
author: Arunav Maitra
date: '2025-09-13'
description: This is a submission for the Google AI Studio Multimodal Challenge What I Built I built... Tagged with devchallenge, googleaichallenge, ai, gemini.
tags: '#devchallenge, #googleaichallenge, #ai, #gemini'
---

Google AI Challenge Submission

This is a submission for theGoogle AI Studio Multimodal Challenge

## What I Built

I builtArchiBlocks 3D, a web application that magically transforms real-world architectural photos into captivating 3D block models.

Have you ever looked at a building and imagined what it would look like as a LEGO set, a clay model, or something straight out of a low-poly video game?

That's the core idea behind ArchiBlocks 3D. It bridges the gap between reality and imagination.

It's a simple, intuitive tool for:

* Artistsseeking inspiration.
* Designerslooking for a new way to visualize concepts.
* Hobbyistswho just want to have fun and see the world differently.

The app takes a user's uploaded image and a text prompt describing a desired style, and uses the power of Gemini to generate a brand new, stylized 3D version.

## Demo :Live Here or play with it

Here’s a walkthrough of the experience. Imagine uploading a photo of the iconic Eiffel Tower...

First, the user is greeted by a dynamic hero section with an animated background, setting a creative tone.

Next, they scroll down to the generator. Here, they can drag-and-drop their architectural photo and type in a creative prompt. For this example, the prompt is:“Isometric low-poly 3D model, vibrant colors.”

After hitting the✨ Generate 3D Modelbutton, the magic happens! The AI gets to work, and in a few moments, the result is displayed in a beautiful side-by-side comparison.

Please note: This applet was built using thegemini-2.5-flash-image-previewmodel. The screenshots and descriptions here showcase its full functionality in action!

## How I Used Google AI Studio

Google AI Studio was theenginebehind this entire project. I specifically leveraged theGemini APIand its powerful multimodal capabilities.

My model of choice wasgemini-2.5-flash-image-preview(also known as nanobanana), which is absolutely perfect for this kind of creative image editing task.

The implementation is centered in myservices/geminiService.tsfile. In it, I construct agenerateContentrequest that includes:

1. Animage part, containing the user's uploaded photo as a base64 encoded string.
2. Atext part, which combines my instructions with the user's unique style prompt.
3. Aconfig objectwhere I specify that the response should include bothModality.IMAGEandModality.TEXT.

This setup allows Gemini to understand the visual context from the image and the stylistic direction from the text, merging them to produce a completely new piece of art.

## Multimodal Features

The core ofArchiBlocks 3Dis itsImage-and-Text-to-Imagegeneration. This is a truly multimodal feature that enhances the user experience in a profound way.

* Input 1 (Image):The user provides thevisual foundation—a photo of a building or landscape. This sets the scene and defines the subject.
* Input 2 (Text):The user provides thecreative direction—a prompt like"a cute claymation model"or"a futuristic neon render."
* Output (Image):The AI synthesizes both inputs to generate a new image that respects the structure of the original photo but completely reimagines it in the user's desired style.

Why is this so powerful?

Because it gives the useragency and control. Instead of a one-size-fits-all filter, it opens up an infinite canvas of possibilities. The user isn't just a passive observer; they are an active collaborator with the AI, co-creating a unique visual masterpiece.

This direct, creative dialogue between the user, their photo, and the AI is what makes ArchiBlocks 3D so engaging and fun.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
