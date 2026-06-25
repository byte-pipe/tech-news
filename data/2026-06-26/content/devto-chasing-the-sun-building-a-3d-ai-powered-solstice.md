---
title: 'Chasing the Sun: Building a 3D AI-Powered Solstice Runner with React Three Fiber - DEV Community'
url: https://dev.to/tahosin/chasing-the-sun-building-a-3d-ai-powered-solstice-runner-with-react-three-fiber-bk3
site_name: devto
content_file: devto-chasing-the-sun-building-a-3d-ai-powered-solstice
fetched_at: '2026-06-26T06:00:25.487970'
original_url: https://dev.to/tahosin/chasing-the-sun-building-a-3d-ai-powered-solstice-runner-with-react-three-fiber-bk3
author: S M Tahosin
date: '2026-06-21'
description: 'My submission for the June Solstice Game Jam: A 3D endless runner where you chase the sun with React Three Fiber and the Gemini API. Tagged with devchallenge, gamechallenge, gamedev, discuss.'
tags: '#discuss, #devchallenge, #gamechallenge, #gamedev'
---

June Solstice Game Jam Submission

This is a submission for theJune Solstice Game Jam

## What I Built

For this game jam, I builtSolstice Runner, a 3D endless adventure where you literally chase the sun on the longest day of the year.

The idea started with a simple question:

What if the solstice was a race against time, guided by logic?

In Solstice Runner, players navigate a vibrant 3D world, dodging obstacles and interacting with a dynamically generated environment. Instead of just making a standard runner, I wanted the environment and the interactions to feel alive. The game celebrates the June Solstice by having the player constantly move forward toward a sun that never seems to set, while solving on-the-fly logical puzzles inspired by Alan Turing.

The goal was simple:

Build a fast-paced 3D web experience that seamlessly blends action with intelligent logic.

## Video Demo

Here is a quick video demo of the gameplay in action:

You can also try:

* Running through the 3D obstacle course
* Experiencing real-time dynamic AI dialogues
* Chasing the horizon of the longest day
* Testing your reflexes against Turing-inspired logic nodes

... directly through the deployed game (hosted on GitHub Pages):

🎮 Play Solstice Runner Here

## Code

GitHub Repository

Built with:

* React— Frontend UI and application state
* React Three Fiber / Three.js— The entire 3D rendering pipeline and game world
* Vite— Lightning-fast development and build tooling
* Google AI API (Gemini)— Generating dynamic interactions and logic on the fly
* Tailwind CSS— Styling the overlay HUDs

## How I Built It

I started by focusing on the core rendering loop:

Render Scene → Handle Movement → Generate AI Logic → Avoid Obstacles

Once the 3D movement felt right in the browser, I started layering in everything else.

### Building the 3D World in the Browser

One of the biggest challenges was getting 3D performance running smoothly in the browser. Using pure Three.js can require a lot of boilerplate, so I opted for React Three Fiber. It allowed me to treat 3D meshes, lights, and cameras as standard React components, which sped up development tremendously. The environment uses warm, bright lighting to reflect the summer solstice vibe.

### Integrating the Google AI API

Instead of hardcoding the obstacles or dialog sequences, I used the Google AI API as the "Game Master". Every time a player reaches a specific checkpoint, the game pings the API with the current game state to generate unique logic challenges and narrative text.

It took some tweaking to ensure the API calls didn't block the game's render loop, but the result is a game that responds dynamically.

### A Nod to Alan Turing

Since June is also Alan Turing's birth month, I wanted to include a tribute to him. The logic checkpoints you encounter while running are framed as "Turing Gates". They require quick thinking—such as pattern recognition or simple binary decisions—before you can continue your run.

Feature

Concept

The Mechanics

Turing Gates

Logic Nodes

Answer AI-generated logic puzzles to pass safely

Endless Day

June Solstice

The lighting stays perpetually at golden hour

## Prize Category

I am submitting this project for theBest Google AI UsageandBest Ode to Alan Turingcategories.

The Google AI API handles the core dynamic dialog and logic generation, making every run feel unique. Meanwhile, the core mechanics of navigating "Turing Gates" serve as a direct homage to Turing's legacy in computing and intelligence.

## Let's Discuss! 👇

I'd love to hear your thoughts on mixing 3D web games with generative AI!

* Have you tried using React Three Fiber or the Gemini API in your own projects?
* What kind of AI-driven mechanics would you add to an endless runner?
* How far did you manage to run in the game? 🏃‍♂️

Drop a comment below, and let's chat about web game development, AI, or just share your high score!

Thanks for playing!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse