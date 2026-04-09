---
title: 'Celestine: AI Navigator for the Universe 🪐 - DEV Community'
url: https://dev.to/vero-code/celestine-ai-navigator-for-the-universe-2acc
site_name: devto
fetched_at: '2025-12-30T11:07:07.501702'
original_url: https://dev.to/vero-code/celestine-ai-navigator-for-the-universe-2acc
author: Veronika Kashtanova
date: '2025-12-27'
description: This is a submission for the DEV's Worldwide Show and Tell Challenge Presented by Mux What... Tagged with devchallenge, muxchallenge, showandtell, video.
tags: '#devchallenge, #muxchallenge, #showandtell, #video'
---

DEV's Worldwide Show and Tell Challenge Submission 🎥

This is a submission for theDEV's Worldwide Show and Tell Challenge Presented by Mux

## What I Built

Celestineis an intelligent, multi-modal AI navigator for the Solar System. It extends the intuitive experience of Google Maps to the cosmos, allowing users to explore planets in 3D and "land" on them to discover their secrets.

Unlike static star maps, Celestine features an AI co-pilot (powered byGemini 2.5) that acts as a bridge between alien worlds and our own. When you explore a crater on Mercury, the AI doesn't just recite dry facts — it uses theGoogle Maps Platformto find a geological "twin" here on Earth (like a similar crater in Arizona), instantly connecting the user's cosmic journey to their home planet.

## Gallery: Seeing the Universe

Here is a closer look at the key features of Celestine:

The Core Feature: The AI finds a "terrestrial twin" for a Venusian mountain range on Google Maps.

Multimodal Interaction: Users can talk to the AI via voice or a real-time generated video avatar (powered by Tavus).

Back to Earth: The application visualizes the coordinates of earthly analogues on a 3D globe.

Planetary Navigation: The 3D interface allows seamless travel between celestial bodies.

## My Pitch Video (Powered by Mux)

## Demo

Here is the code that powers the universe:👉View Source Code on GitHub

(Note: The project is containerized with Docker and deployed on Cloud Run, but currently requires a local setup for full interactivity due to cloud resource limits).

## The Story Behind It

Google Maps mastered the navigation of Earth. But what about the rest of the Universe?I built Celestine to revive the dream of a "Space Mode" — but to make it interactive, personal, and intelligent.

I wanted to build a system where an AI agent could actuallyusetools — specifically, the Google Maps Places API — to reason about geology and perform semantic searches across planets. This project is my first step toward making cosmic exploration deeply personal.

🏆 Recognition:This project was originally built for theGoogle Maps Platform Hackathon, where it was a nominee.

Official Showcase: Celestine featured as a nominee on the Google Maps Platform website.

You can view the original submission details here:👉View Original Devpost Submission

## Technical Highlights

This is a full-stack application that combines 3D rendering with advanced AI agent orchestration.

* Frontend:React +react-three-fiberfor the immersive 3D solar system.
* AI Engine:A multi-agent system built withGoogle's Agent Development Kit (ADK)andGemini 2.5 Flash/Pro.
* The "Magic" Integration:TheAnalogues Specialist Agent. This agent analyzes celestial features and autonomously queries theGoogle Maps Places APIto find terrestrial counterparts, returning coordinates that render dynamically on a 2D Earth map.
* Infrastructure:The backend is Python (FastAPI), containerized withDocker, and deployed onGoogle Cloud Run.

### Architecture Diagram

Below is the high-level architecture showing how the Multi-Agent System orchestrates Gemini, Google Maps, and the frontend.

### Challenges I ran into

Building a space AI is easier than teaching it to wait for Google Maps to load! One of the biggest technical hurdles was handling race conditions where the UI tried to render a map before the API script was ready. I implemented a singleton loader pattern to solve this. Orchestrating the agents to handle voice, text, and visual data simultaneously required significant prompt engineering and logic design.

We are ready for takeoff! 🚀

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
