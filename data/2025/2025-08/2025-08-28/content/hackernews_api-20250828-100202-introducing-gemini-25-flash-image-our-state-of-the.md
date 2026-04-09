---
title: Introducing Gemini 2.5 Flash Image, our state-of-the-art image model - Google Developers Blog
url: https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/
site_name: hackernews_api
fetched_at: '2025-08-28T10:02:02.531727'
original_url: https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/
author: meetpateltech
date: '2025-08-27'
description: Explore Gemini 2.5 Flash Image, a powerful new image generation and editing model with advanced features and creative control.
tags:
- hackernews
- trending
---

English


 Español (Latam)


 Bahasa Indonesia


 日本語


 한국어


 Português (Brasil)


 简体中文


Gemini
 /
Google AI Studio

# Introducing Gemini 2.5 Flash Image, our state-of-the-art image model

AUG. 26, 2025

Alisa Fortin

Product Manager

Guillaume Vernade

Gemini Developer Advocate

Kat Kampf

Product Manager

Ammaar Reshi

Product and Design Lead

AI Studio

Share

* Facebook
* Twitter
* LinkedIn
* Mail



Today, we’re excited to introduceGemini 2.5 Flash Image(aka nano-banana), our state-of-the-art image generation and editing model. This update enables you to blend multiple images into a single image, maintain character consistency for rich storytelling, make targeted transformations using natural language, and use Gemini's world knowledge to generate and edit images.

When we first launched native image generation in Gemini 2.0 Flash earlier this year, you told us you loved its low latency, cost-effectiveness, and ease of use. But you also gave us feedback that you needed higher-quality images and more powerful creative control.

This model is available right now via theGemini APIandGoogle AI Studiofor developers andVertex AIfor enterprise. Gemini 2.5 Flash Image is priced at $30.00 per 1 million output tokens with each image being 1290 output tokens ($0.039 per image). All other modalities on input and output follow Gemini 2.5 Flashpricing.

 (lmarena results come from https://lmarena.ai/leaderboard)


## Gemini 2.5 Flash Image in action

To make building with Gemini 2.5 Flash Image even easier, we have made significant updates toGoogle AI Studio’s “build mode”(with more updates to come). In the examples below, not only can you quickly test the model’s capabilities with custom AI powered apps, but you can remix them or bring ideas to life with just a single prompt. When you are ready to share an app you built, you can deploy right from Google AI Studio or save the code to GitHub.

Try a prompt like “Build me an image editing app that lets a user upload an image and apply different filters" or choose one of the preset templates and remix it, all for free!

### Maintain character consistency

A fundamental challenge in image generation is maintaining the appearance of a character or object across multiple prompts and edits. You can now place the same character into different environments, showcase a single product from multiple angles in new settings, or generate consistent brand assets, all while preserving the subject.

We built atemplate app in Google AI Studio(that you can easily customize and vibe code on top of) to demonstrate the model’s character consistency capabilities.

Sorry, your browser doesn't support playback for this video

(sequence shortened)



Beyond character consistency, the model is also excellent at adhering to visual templates. We have already seen developers explore areas like real estate listing cards, uniform employee badges, or dynamic product mockups for an entire catalog—all from a single design template.

### Prompt based image editing

Gemini 2.5 Flash Image enables targeted transformation and precise local edits with natural language. For example, the model can blur the background of an image, remove a stain in a t-shirt, remove an entire person from a photo, alter a subject's pose, add color to a black and white photo, or whatever else you can conjure up with a simple prompt.

To show these capabilities in action, we built aphoto editing template app in AI Studio, with both UI and prompt-based controls.

### Native world knowledge

Historically, image generation models have excelled at aesthetic images, but lacked a deep, semantic understanding of the real world. With Gemini 2.5 Flash Image, the model benefits from Gemini’s world knowledge, which unlocks new use cases.

To demonstrate this, we builta template app in Google AI Studiothat turns a simple canvas into an interactive education tutor. It showcases the model's ability to read and understand hand-drawn diagrams, help with real world questions, and follow complex editing instructions in a single step.

Sorry, your browser doesn't support playback for this video

(Example prompts and model results)



### Multi-image fusion

Gemini 2.5 Flash Image can understand and merge multiple input images. You can put an object into a scene, restyle a room with a color scheme or texture, and fuse images with a single prompt.

To showcase multi-image fusion, we built atemplate app in Google AI Studiowhich lets you drag products into a new scene to quickly create a new photorealistic fused image.

Sorry, your browser doesn't support playback for this video

(Sequences shortened)



## Get started building

Check out ourdeveloper docsto start building with Gemini 2.5 Flash Image. The model is in preview today via theGemini APIandGoogle AI Studiobut will be stable in the coming weeks. All of the demo apps we highlighted here were vibe coded in Google AI Studio so they can be remixed and customized with just a prompt.

OpenRouter.aihas partnered with us to help bring Gemini 2.5 Flash Image to their 3M+ developers everywhere, today. This is the first model on OpenRouter – of the 480+ live today –that can generate images.

We're also excited to partner withfal.ai, a leading developer platform for generative media, to make Gemini 2.5 Flash Image available to the broader developer community.

All images created or edited with Gemini 2.5 Flash Image will include an invisibleSynthID digital watermark, so they can be identified as AI-generated or edited.



from google import genai
from PIL import Image
from io import BytesIO

client = genai.Client()

prompt = "Create a picture of my cat eating a nano-banana in a fancy restaurant under the gemini constellation"

image = Image.open('/path/to/image.png')

response = client.models.generate_content(
 model="gemini-2.5-flash-image-preview",
 contents=[prompt, image],
)

for part in response.candidates[0].content.parts:
 if part.text is not None:
 print(part.text)
 elif part.inline_data is not None:
 image = Image.open(BytesIO(part.inline_data.data))
 image.save("generated_image.png")

 Python


Copied



We are actively working to improve long-form text rendering, even more reliable character consistency, and factual representation like fine details in images. Please continue to send us feedback in ourdeveloper forumor onX.

We can’t wait to see what you build with Gemini 2.5 Flash Image!
