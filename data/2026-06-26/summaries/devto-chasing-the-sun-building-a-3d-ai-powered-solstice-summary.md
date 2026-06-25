---
title: Chasing the Sun: Building a 3D AI-Powered Solstice Runner with React Three Fiber - DEV Community
url: https://dev.to/tahosin/chasing-the-sun-building-a-3d-ai-powered-solstice-runner-with-react-three-fiber-bk3
date: 2026-06-21
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-06-26T06:02:24.190809
---

# Chasing the Sun: Building a 3D AI-Powered Solstice Runner with React Three Fiber - DEV Community

# Chasing the Sun: Building a 3D AI‑Powered Solstice Runner with React Three Fiber

## What I Built
- Solstice Runner – a 3D endless runner where the player chases a never‑setting sun on the June solstice.
- Combines fast‑paced action with on‑the‑fly logical puzzles inspired by Alan Turing.
- Features dynamic AI‑generated dialogues and “Turing Gates” that require quick pattern‑recognition or binary decisions.

## Video Demo & Playable Link
- Short gameplay video showcases obstacle navigation, AI dialogues, and the endless horizon.
- Deployed version available on GitHub Pages (playable directly in the browser).

## Built With
- React for UI and state management.  
- React Three Fiber / Three.js for the 3D rendering pipeline.  
- Vite for rapid development and builds.  
- Google AI (Gemini) API to generate dynamic logic challenges and narrative text.  
- Tailwind CSS for HUD styling.

## How I Built It
### Core Rendering Loop
- Sequence: Render scene → handle movement → generate AI logic → avoid obstacles.

### 3D World in the Browser
- Chose React Three Fiber to treat meshes, lights, and cameras as React components, reducing boilerplate.
- Warm, bright lighting creates a perpetual golden‑hour atmosphere.

### Google AI Integration
- The API acts as a “Game Master,” receiving the current game state at checkpoints and returning unique puzzles and dialogue.
- Implemented asynchronous calls to avoid blocking the render loop.

### Tribute to Alan Turing
- Logic checkpoints are called “Turing Gates.”
- Players must solve quick logic nodes (pattern recognition, binary decisions) to continue.

## Prize Categories
- Best Google AI Usage.  
- Best Ode to Alan Turing.  

Both categories highlight the dynamic AI dialogue generation and the thematic homage to Turing’s contributions.

## Discussion Points
- Experiences with React Three Fiber or Gemini API in personal projects.  
- Ideas for additional AI‑driven mechanics in endless runners.  
- Personal high scores or distance achieved in Solstice Runner.  

Feel free to comment, share thoughts on mixing 3D web games with generative AI, or discuss web game development techniques.