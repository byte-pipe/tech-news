---
title: 'Move over, Vibe-Coding: I built an AI editor for STRESS-CODING - DEV Community'
url: https://dev.to/phalkmin/move-over-vibe-coding-i-built-an-ai-editor-for-stress-coding-4243
site_name: devto
content_file: devto-move-over-vibe-coding-i-built-an-ai-editor-for-str
fetched_at: '2026-04-06T19:26:55.823575'
original_url: https://dev.to/phalkmin/move-over-vibe-coding-i-built-an-ai-editor-for-stress-coding-4243
author: Paulo Henrique
date: '2026-04-06'
description: This is a submission for the DEV April Fools Challenge Quantum Collapse is a React editor that... Tagged with devchallenge, 418challenge, showdev.
tags: '#showdev, #devchallenge, #418challenge'
---

April Fools Challenge Submission ☕️🤡

This is a submission for theDEV April Fools Challenge

Quantum Collapse is a React editor that monitors your face via webcam and sabotages your code when you blink. Sadly, it works.

## What I Built

If you are working remote in 2026, you know how some companies like to ensure that you are "being productive". Keep your camera on, keep a "productivity tracker" installed and running while you try to work.

"We trust you," they say, from behind six layers of monitoring software.

And, at the same time, "vibe-coding" is the new hype. Everyone is talking about how we should stop caring about code quality and hard work, and let AI do the job for us.

So I built an IDE that merges those two realities.

### What Quantum Collapse actually does

The premise is straightforward. If you're watching the screen, your code stays intact. The moment you blink, or look away, or even commit the biological crime of hydrating your eyeballs, the editor "collapses the wavefunction" and starts quietly sabotaging your work.

Your variable names become emojis.

Your semicolons silently turn into Greek question marks.

Your functions rename themselves after Tokusatsu Monsters (I'm a nerd, sue me).

There's a Stability Meter that drops every time you blink, and when it bottoms out, you can't save your work. And the best part? The editor doesn't tell you what it changed.

You look back at your screen, and MAYBE something is different, but you're not sure what. Was that variable always called 🌮? Did that function always returnundefined? Maybe you're just tired. Maybe you made a mistake. The code was fine a second ago. Wasn't it?

That's the whole joke. You are not vibe-coding anymore. You areSTRESS-CODING.

It's also, in a very direct way, the experience of working under a time tracker that logs your keystrokes and then surfaces a passive-aggressive "productivity score" for your manager to review. You know you worked. The data says something else. You start questioning yourself and how you work.

The only difference is that Quantum Collapse is honest about what it's doing.

## Demo

You can try Stress-Codingyour new project here

Warning: extended use may cause dry eyes, Greek punctuation in production, and a sudden appreciation for jobs that don't need to see your face to trust you.

## Code

## phalkmin/DevTo-April-Fool-s-Challenge

# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

* @vitejs/plugin-reactusesOxc
* @vitejs/plugin-react-swcusesSWC

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, seethis documentation.

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:

export

default

defineConfig
(
[


globalIgnores
(
[
'dist'
]
)
,


{


files
:
[
'**/*.{ts,tsx}'
]
,


extends
:
[


// Other configs...


// Remove tseslint.configs.recommended and replace with this


tseslint
.
configs
.
recommendedTypeChecked
,


// Alternatively, use this for stricter rules


tseslint
.
configs
.
strictTypeChecked
,


// Optionally, add this for stylistic rules


tseslint
.
configs
.
stylisticTypeChecked
,


// Other configs...
…

Enter fullscreen mode

Exit fullscreen mode

View on GitHub

## How I Built It

This whole project was made using AI as a tool. I used Gemini Web (that has a bunch of my latest posts and memories) to brainstorm some ideas, and as I'm a notorious advocate of remote workandclear productivity goals when working, one of the ideas was to play with this concept.

Then, I used Gemini CLI's Plan Mode to map out the mutation engine, or, more specifically, brainstorming the most creative ways to mess with code without making it obviously broken.

For development, I first used Gemini CLI, but for the final steps of front-end development, I used Codex, as Gemini kept messing up some parts of the code.

For deployment, the Gemini CLI handled containerization and pushed the whole thing to Google Cloud Run. The fact that a gag application about corporate surveillance is running on enterprise-grade infrastructure with automatic scaling is, genuinely, the ironic part of the project.

### What I used

Google MediaPipe (Face Landmarker) handles the blink detection: real-time computer vision, running entirely in the browser, zero latency. If you blink for 200ms, the AI knows. The AI always knows. Which is, again, exactly the energy of the companies that sell "employee monitoring solutions" to people who manage remote teams.

React 19 + TypeScript because even a deliberately broken tool should be type-safe before it breaks itself. There's something deeply funny about writing rigorous TypeScript for a chaos engine.Framer Motion powers the glitch aesthetic ( scanlines, neon flicker, haunted CRT vibes ).

Vite 8 for the build. PrismJS for syntax highlighting, because the code deserves to look beautiful right before it gets destroyed.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
