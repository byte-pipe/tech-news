---
title: 'DermaVision: Your Personal AI Dermatology Assistant for Skin Health Insights - DEV Community'
url: https://dev.to/abhinandan-r/dermavision-your-personal-ai-dermatology-assistant-for-skin-health-insights-3pf2
site_name: devto
fetched_at: '2025-09-21T11:05:35.466330'
original_url: https://dev.to/abhinandan-r/dermavision-your-personal-ai-dermatology-assistant-for-skin-health-insights-3pf2
author: Abhi nandan
date: '2025-09-14'
description: This is a submission for the Google AI Studio Multimodal Challenge What I Built I built... Tagged with devchallenge, googleaichallenge, ai, gemini.
tags: '#devchallenge, #googleaichallenge, #ai, #gemini'
---

Google AI Challenge Submission

This is a submission for theGoogle AI Studio Multimodal Challenge

## What I Built

I built DermaVision, an AI-powered web application designed to serve as a personal dermatology assistant. It helps users gain preliminary, AI-generated insights into common skin conditions by analyzing images of their skin, providing a bridge between observation and understanding.

The application solves a common problem: people often notice a new skin condition but have no immediate information about what it might be or what steps they could take. DermaVision offers a user-friendly first step in this journey, featuring:

1. AI-Powered Skin Analysis: Users can upload an image of their skin, and the application leverages a multimodal AI model to identify potential issues like acne, pigmentation, or scarring.
2. Actionable Recommendations: For each identified issue, the app provides tailored, non-prescriptive suggestions for beneficial foods and relevant over-the-counter products that could help manage the condition.
3. Personal Skin Journal: Users can save each analysis to a private, browser-based journal. This allows them to track their skin's condition over time, add personal notes about their routine or diet, and monitor their progress.
4. Data Portability & Control: The entire journal can be exported as a single JSON file, giving users full ownership and control over their data.

Crucially, DermaVision is designed as an informational tool and prominently features a disclaimer that it is not a substitute for professional medical advice.

## Demo

## How I Used Google AI Studio

Google AI Studio was instrumental in developing DermaVision, particularly for prototyping and refining the core AI functionality.

My development process involved:

1. Prompt Engineering: I started in Google AI Studio's prompt editor to experiment with multimodal prompts. I uploaded various sample images of skin conditions and paired them with different text instructions to see how the Gemini model would respond. This allowed me to quickly iterate and find the most effective way to ask the model to identify issues and provide recommendations.
2. Model Selection: Through this testing, I selected the gemini-2.5-flash model. It offered the perfect balance of sophisticated multimodal understanding, fast response times, and, most importantly, support for structured output.
3. Implementing Structured Output: The most critical Gemini feature I implemented was its JSON mode with a responseSchema. Instead of asking for a plain text response that I would have to manually parse, I defined a strict JSON schema directly in my API call. This schema dictates that the response must be an array of objects, each containing an issue, description, food_recommendations, and medicine_recommendations. This feature is the bedrock of the application's reliability; it guarantees that the API's response is always consistent, predictable, and can be directly mapped to the UI components without any fragile string manipulation. This made the integration between the AI and the frontend seamless and robust.

## Multimodal Features

1. Image as Input: The primary input is an image, which allows the user to convey complex visual information effortlessly. Instead of trying to describe a rash or a blemish in words, they can simply show it to the AI.
2. Text as Instruction: My code pairs this image with a carefully crafted text prompt. This prompt instructs the Gemini model to act as a dermatology assistant, specifically look for common skin issues, and, most importantly, to format its findings according to the JSON schema I provide.

This combination of image and text enhances the user experience by transforming a static image into a source of actionable, personalized insights. The multimodal capability of the Gemini API is what allows DermaVision to bridge the gap between seeing a potential skin issue and understanding what steps could be taken next, creating a helpful and empowering tool for users.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
