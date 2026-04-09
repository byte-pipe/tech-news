---
title: 3D Models That Explain Themselves - DEV Community
url: https://dev.to/peppers/3d-models-that-explain-themselves-48a7
site_name: devto
fetched_at: '2025-09-22T06:56:49.179129'
original_url: https://dev.to/peppers/3d-models-that-explain-themselves-48a7
author: Christopher Derrell
date: '2025-09-16'
description: This is a submission for the Google AI Studio Multimodal Challenge What I Built I built a... Tagged with devchallenge, googleaichallenge, ai, gemini.
tags: '#devchallenge, #googleaichallenge, #ai, #gemini'
---

Google AI Challenge Submission

This is a submission for theGoogle AI Studio Multimodal Challenge

## What I Built

I built a web applet that is used for dynamic annotation of 3D assets, so that persons (like me who work with 3D) will be able to have AI create the annotations on the models for us. When getting ready to launch a model you've designed for companies, or for fun, the last part is tagging it with additional information for visitors who want to learn more about it. This can be a fairly complex part of the process taking quite a bit of time, as you need to get the 3D coordinates for the hotspot to show up correctly.

What this Applet does is a simple drop in your model, and it will auto annotate it for you.

## Demo

*Demo below: *

Short demo video

 gemini-3d-model-annotator-806520249946.us-west1.run.app


Or open3D Model Annotator in new tab!

Copy & Paste Link:https://gemini-3d-model-annotator-806520249946.us-west1.run.app

## How I Used Google AI Studio

Leverages the Google Gemini 2.5 API to handle image recognition of the different angles of the model. For the demo I did 90 degree rotations, so each model processed will send 4 images up to the API to give suggestions and annotations for it.

This is the basic concept, but should allow people to come up with pretty good rubrics for what to pin, much like what's visible in the interface on Sketchfab.com

## Multimodal Features

They key tech used here was making use of the Gemini Image Understanding functionality through the API to handle the annotations.

Team of 1 for this: Christopher Derrell -https://dev.to/peppers

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
