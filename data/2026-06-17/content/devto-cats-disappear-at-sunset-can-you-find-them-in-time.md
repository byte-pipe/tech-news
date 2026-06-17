---
title: Cats Disappear at Sunset. Can You Find Them in Time? - DEV Community
url: https://dev.to/iyop666/cats-disappear-at-sunset-can-you-find-them-in-time-1e0k
site_name: devto
content_file: devto-cats-disappear-at-sunset-can-you-find-them-in-time
fetched_at: '2026-06-17T12:27:18.106044'
original_url: https://dev.to/iyop666/cats-disappear-at-sunset-can-you-find-them-in-time-1e0k
author: semi
date: '2026-06-10'
description: This is a submission for the June Solstice Game Jam What I Built For this game jam, I... Tagged with devchallenge, gamechallenge, gamedev.
tags: '#devchallenge, #gamechallenge, #gamedev'
---

June Solstice Game Jam Submission

This is a submission for theJune Solstice Game Jam

## What I Built

For this game jam, I builtFind Them Before They Disappear, a hidden-object browser game where you find target cats before sunset takes them away.

The idea started with the solstice itself.

June 21 is the longest day of the year. After that, days get shorter. Light fades. Things disappear. I wanted a game that captures that feeling of racing against fading light.

In the game, you're shown a few target cats for 5 seconds. Memorize their traits. Then 20 to 90 cats spawn on screen. Find the targets before the sun sets. Wrong clicks cost you 5 seconds. Fast correct clicks build combos. When the timer drops below 10 seconds, the screen pulses red and the panic kicks in.

The cats physically fade as time runs out. That was the agent's idea, not mine. It turned out to be the best visual metaphor in the game.

Each target cat has a unique combination of traits: body color (orange, black, white, gray, brown), eye color (green, blue, yellow), and accessories (hat, glasses, ribbon, collar, or none). You have to compare traits carefully. Click the wrong cat and you lose time. Click the right one fast enough and you get a combo bonus.

🎮Play it here

## Video Demo

You can also try:

* Finding target cats before sunset
* Building combos with fast correct clicks
* Surviving the warning pulse at 10 seconds
* Watching cats fade as light runs out
* Playing all 5 levels (20 cats up to 90 cats)

... directly through the deployed game (on Vercel)

find-them-before-they-disappear.vercel.app

## Code

The entire game is a singleindex.htmlfile. Around 900 lines. No build tools, no dependencies, no package.json.

Built with:

* Phaser 3 (via CDN)
* Web Audio API (synthesized sounds, no audio files)
* Phaser Graphics Primitives (all visuals drawn with code)
* Vercel (deployment)

I picked Phaser because it handles canvas rendering, input, tweens, and game state without me needing to write a game loop from scratch. The agent already knew the API.

## How I Built It

I used Codex, OpenAI's coding agent. No game engine installed. No sprite sheets. No audio files. Two prompts.

### The First Prompt: Build the Game

Prompt 1 was around 200 words. I wrote it like a spec doc. Every level's cat count, timer duration, and target count. The full cat trait system. Where the UI elements go. What the end screens say word for word. I told it Phaser 3 from CDN, no external assets, single HTML file, draw everything with graphics primitives.

Output was a working game. Not pretty. Not juicy. But functional. You could play it start to finish. Five levels, from 20 cats to 90 cats. Timer counting down. Cats drawn with circles and triangles. Target preview, click detection, score tracking.

The biggest thing I learned: prompt quality matters way more than I expected. My first draft was vague. "Make a cat finding game with levels." The agent gave me something broken and generic. So I rewrote it with exact numbers. Level 1: 20 cats, 3 targets, 60 seconds. Level 2: 35 cats, 3 targets, 55 seconds. All the way to level 5: 90 cats, 5 targets, 40 seconds. I defined the trait system (5 body colors, 3 eye colors, 5 accessories). I wrote the exact victory and game over messages. That version worked on the first try.

### The Second Prompt: Make It Feel Good

Prompt 2 was about juice. But I was specific about what that means. Not just "add juice." I listed each effect I wanted:

* Hover effects on cats (visual feedback when you mouse over)
* Sound effects using Web Audio API (correct chime, wrong buzz, tick, button click)
* Combo bonuses for fast consecutive correct clicks
* Warning pulse when timer drops below 10 seconds
* Clearer target cards so you can compare traits easily
* Restart button for quick replays
* Mobile touch support with proper touch-action handling

Night and day difference. The first version was a prototype. The second one was a game I actually wanted to play.

Same approach with prompt specificity. "Add juice" gets you random particle effects. "Add hover effect on cats, sound effects using Web Audio API with no external files, combo bonus for fast correct clicks, warning pulse below 10 seconds" gets you exactly what you asked for.

### Making the Solstice Matter

The solstice theme wasn't an afterthought. I picked it first, then designed the game around it.

The game is built around one metaphor: light is time, and time runs out.

* The sun sets as your timer counts down
* Cats fade as darkness approaches
* Found cats sparkle and disappear safely
* Unfound cats vanish with the sunset

Victory message: "You found them before the longest day ended."

Game over: "They disappeared with the sunset."

June 21 is the longest day. This game is about the urgency of that moment. Finding what matters before the light goes out.

### Art Direction

Everything is drawn with Phaser's graphics primitives. Circles for heads and bodies. Triangles for ears. Rectangles for accessories. No sprites, no images, no external assets.

This wasn't just a technical choice. It means every cat is consistent. Same style, same proportions, same visual language. And it means I didn't spend hours hunting for sprites or worrying about licensing.

The sunset gradient background changes as time runs out. The sky goes from warm orange to deep purple to dark blue. Cats go from fully visible to semi-transparent. The whole screen tells you time is running out without needing to look at the timer.

### Technology

The full stack:

* Phaser 3 via CDN (game framework)
* Web Audio API (sound synthesis)
* Phaser Graphics Primitives (visuals)
* Single HTML file (no build step)
* Vercel (hosting)

No npm. No node_modules. No build tools. I literally opened the file in a browser to test it.

Thanks for checking out Find Them Before They Disappear 🌅

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse