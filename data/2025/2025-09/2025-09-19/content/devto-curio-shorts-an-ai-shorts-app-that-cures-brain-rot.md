---
title: 'Curio-Shorts: An AI Shorts App That Cures Brain Rot - DEV Community'
url: https://dev.to/saurabh_ssk/curioshorts-3o09
site_name: devto
fetched_at: '2025-09-19T11:06:45.617021'
original_url: https://dev.to/saurabh_ssk/curioshorts-3o09
author: Saurabh Singh
date: '2025-09-15'
description: CurioShorts is an AI-powered educational content generator. It transforms any user-asked question... Tagged with devchallenge, googleaichallenge, ai, gemini.
tags: '#devchallenge, #googleaichallenge, #ai, #gemini'
---

CurioShortsis an AI-powered educational content generator. It transforms any user-asked question into a short, engaging, TikTok-style shorts video. Users can select a fun character (like Spider-Man or a custom one) to be the narrator, choose a visual art style, and the app automatically generates a simple song with lyrics, custom images for each line, and a voice-over narration, all explaining the answer to the question with music in background.

What Problem It SolvesThe app directly tackles the problem of "brain rot"— the passive, often low-value content consumption common on short-form video platforms. Its goal is to "swap brain rot for brain fuel" by making learning as engaging, accessible, and fun as scrolling through social media. It provides a creative and educational alternative, especially for younger audiences.This app could be gamechanger for children to cure their brain rot. Tiktok, YouTube Shorts, Insta Reels can use this to make their educational mode of their respective apps. Replacing mindless scrolling with scrolling which will make them learn new things in very interactive way.

Tech Stack

* Frontend: TypeScript, HTML5, CSS3
* AI Model: Google Gemini API (@google/genai)
* Client-Side Storage: IndexedDB for persisting generated shorts.
* Browser APIs:
* Web Speech API (SpeechSynthesis) : For text-to-speech voice narration 2. Intersection Observer : To manage video playback efficiently as the user scrolls
* Libraries: marked for rendering lyrics.

Demoapp :https://ai.studio/apps/drive/1o-mWyYV79577vjypSg8wIzIjMHyVfWu0youtube demo link :screenshots :

How I Used Google AI StudioThis app completely built in Google AI Studio. The core logic, including the prompts for generating song structures and image descriptions, was developed and tested in AI Studio's flexible environment before being integrated into the application code with the Gemini API.

Multimodal FeaturesThe app taps into Gemini’s multimodal capabilities through a two-step pipeline:

1. Structured Text Generation (gemini-2.5-flash): The user’s question is passed to the model with instructions to act as a songwriter. The model outputs a JSON structure containing the song’s lyrics, a detailed image prompt for each lyric line, and a suggested music style.
2. Text-to-Image Generation (gemini-2.5-flash-image-preview): Each image prompt is then fed into Gemini’s image model, producing unique, stylized visuals that match the lyrics.
By chaining these steps, the app turns a single text query into an integrated audio-visual learning experience, blending storytelling, imagery, and music.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
