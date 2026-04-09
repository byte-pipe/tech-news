---
title: AI Image Tagger - DEV Community
url: https://dev.to/aju21/smart-image-tagger-5afh
site_name: devto
fetched_at: '2025-08-15T10:02:41.342740'
original_url: https://dev.to/aju21/smart-image-tagger-5afh
author: Ajinkya Ghadigaonkar
date: '2025-08-11'
description: 'This is a submission for the Redis AI Challenge: Real-Time AI Innovators. What I Built AI... Tagged with redischallenge, devchallenge, database, ai.'
tags: '#redischallenge, #devchallenge, #database, #ai'
---

Redis AI Challenge: Real-Time AI Innovators

This is a submission for theRedis AI Challenge: Real-Time AI Innovators.

## What I Built

AI Image Tagger is (as of now) a simple console application. In some words , it is kind of google for local images. So if we searched for fruits, it will give the list of all the pictures containing fruits in your local machine folder. Since it utilizes AI chatbot, it can give more diverse range of options from natural language search

Why ?Since we have moved to digital images, there are tons of images on your computer/laptop from various devices such as internet, mobile phone, action camera, drone, gopro etc. So in order to search and sort images can be a challenge. There are cloud tools available but they can come at a cost of privacy. So the current functionality works from local without sending image data to the cloud. Further it can be extended to personal or public cloud setup.

Technologies used :

1. .Net Core 8 for base application
2. Onnx model for object detection.
3. Mistral 7B running locally through Ollama - for adding more natural tags and also handling user interaction
4. Redis Cloud to store the tags, file path and for easy retrieval

## Demo

## How I Used Redis 8

1. Fast Semantic SearchRedis Vector Search lets us store embeddings (numeric representations) of the image tags and objects detected. This allows semantic search — e.g., if an image is tagged as "mountain, snow, hiking", searching "alpine adventure" will still find it because the embeddings are close in meaning.Unlike normal keyword search, it understands context and synonyms.
2. Real-Time QueryingRedis is in-memory, so queries are milliseconds fast, even with thousands or millions of images.Wecan instantly search tags, locations, or objects without pre-loading everything into memory in your .NET app.
3. Hybrid Search (Vector + Metadata)Redis allows combining vector similarity search (semantic match) with structured filters (e.g., "find images similar to sunset beach AND taken in 2023").Perfect for narrowing down results quickly.
4. Easy ScalabilityYou can start with Redis Cloud Free Tier for small datasets and later scale to millions of images without changing your code.Redis handles sharding and distributed storage under the hood.

Future Improvements :

1. Add GUI- making web app UI in order to show images
2. Add OCR and face tag support

Project Github Link :https://github.com/Aju21/AI-Image-Tagger

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
