---
title: I Built a Platformer That Gaslights You — Coins Steal, Spikes Heal, and The Exit Door Kills You 🫖 - DEV Community
url: https://dev.to/anik2812/i-built-a-platformer-that-gaslights-you-coins-steal-spikes-heal-and-the-exit-door-kills-you-2a5h
site_name: devto
content_file: devto-i-built-a-platformer-that-gaslights-you-coins-stea
fetched_at: '2026-04-15T11:55:59.421550'
original_url: https://dev.to/anik2812/i-built-a-platformer-that-gaslights-you-coins-steal-spikes-heal-and-the-exit-door-kills-you-2a5h
author: Anik2812
date: '2026-04-13'
description: This is a submission for the DEV April Fools Challenge What I Built DEFINITELY NOT A... Tagged with devchallenge, 418challenge, showdev.
tags: '#showdev, #devchallenge, #418challenge'
---

April Fools Challenge Submission ☕️🤡

This is a submission for theDEV April Fools Challenge

## What I Built

DEFINITELY NOT A TROLL GAME™— a platformer that looks completely normal but systematically betrays every gaming instinct you've ever developed.

Level 1 is honest. It teaches you the rules: collect coins, avoid spikes, reach the exit. You feel safe. You feel smart.

Then Level 2 happens.

Here's what you need to know:

* Trust nothing.Every rule established in Level 1 is a lie designed to hurt you later.
* The game actively mocks you.It features an integrated Gemini 2.0 Flash AI bot designed specifically to roast your gameplay decisions in real-time.
* The settings menu is a trap.The volume slider fights back. The "Uninstall" button refuses to work. The "Fun" toggle turns itself back on.
* Even the quit button gaslights you.Quitting requires multiple attempts, negotiations, and emotional manipulation.

The game has 10 levels of escalating betrayal, culminating in a final boss fight against... a "Next Level" button that refuses to be clicked.

The settings menuhas a "Difficulty" selector (does nothing), a volume slider that fights back and resets itself, a "Fun" toggle that re-enables itself when you turn it off, and an "Uninstall" button with 6 escalating refusals ("Error: Cannot uninstall. The game IS your computer now.")

The quit buttonrequires 6 attempts. On the 6th try it says "Just kidding 😂" and force-resumes the game.

Your browser tab titlechanges as you die:

* 3 deaths:💀 3 deaths... | TROLL GAME
* 20 deaths:🚨 POLICE: Stop playing | TROLL GAME
* 40 deaths:📞 Your mom called. She's worried.
* 50 deaths:🏆 50 DEATHS. ARE YOU OK?

The FPS countercycles through:420.69 FPS,NaN FPS,POTATO FPS,FPS.exe crashed,√-1 FPS

The cookie bannerreads:"We use cookies to track your failures and share them with absolutely everyone."

## Demo

▶ Play DEFINITELY NOT A TROLL GAME™

Runs entirely in the browser. HTML5 Canvas, vanilla JS, zero frameworks, zero build steps. Works on desktop and mobile (touch controls included, because suffering should be accessible).

## Code

## Anik2812/not-a-troll-game

# 🫖 DEFINITELY NOT A TROLL GAME™

A perfectly normal platformer that systematically betrays every gaming instinct you've ever developed.

🎮 PLAY THE GAME HERE

## 🛑 What is this?

This is a brutalist-themed, web-based platformer built for theDEV April Fools Challenge. It is designed to gaslight the player through deceptive mechanics and a sarcastic AI assistant.

Nothing is as it seems. Level 1 trains you to trust the rules. Level 2 and beyond actively punish you for learning them.

### Features

* 10 Levels of Escalating Betrayal:Play across levels where coins steal your points, spikes heal you, exit doors kill you, and safe platforms collapse.
* "HELPFUL ASSISTANT™" AI:An integratedGemini 2.0 Flashchatbot that actively roasts your failures in real-time based on your current death count, mistakes, and score.
* Graceful Degradation:If the API fails or rate limits, the game falls back to a massive dictionary of handcrafted roasts…

View on GitHub

5 files. No frameworks. No dependencies. Pure, artisanal disappointment:

File

Lines

What it does

index.html

~300

Structural skeleton with all overlays and modals

style.css

~525

Brutalist design system, glitch effects, scanlines

game.js

~1070

Full canvas engine: physics, collision, particles

levels.js

~355

10 handcrafted levels of escalating betrayal

app.js

~920

AI chatbot, Konami code, achievements, chaos

## How I Built It

### The Stack

* HTML5 Canvas— Custom 2D game engine with tile-based collision, coyote time (8-frame jump buffer), particle systems, and screen shake
* Vanilla CSS— Brutalist design tokens, noise overlays, scanline effects, periodic glitch text animations via CSSclip-path
* Vanilla JS— Zero dependencies. Everything runs inside a single IIFE
* Google Gemini 2.0 Flash— Powers the in-game AI chatbot AND generates personalized victory reviews
* Web Audio API— Procedurally generated sound effects (oscillator-based — every jump, coin, death, and level complete is synthesized in real time)
* Built with Google Antigravity— The AI coding assistant that helped architect the game engine, design the troll mechanics, and debug the collision detection

### The AI Integration

The game features a"HELPFUL ASSISTANT™"— a chatbot powered byGoogle Gemini 2.0 Flashwith deep game-state awareness.

How it works:The system prompt tells Gemini to act like"a bored IT support worker who secretly hates their job but drops weirdly poetic one-liners about existential suffering."It receives your exact death count, current level, score, and recent game events (died to spikes, collected trap coin, walked into fake door) as context, then generates unique roasts.

Key design decisions:

* Non-repeating responses:ASet-based tracker ensures the AI never says the same thing twice in a session. The system prompt itself includes recently-used responses and explicitly instructs Gemini to avoid them.
* Keyword matching with fallback:25+ keyword categories (coins, spikes, doors, exit, coffee, teapot, etc.) each have 3-5 unique responses with their own non-repeat tracking. If the API is rate-limited, these fire as graceful fallbacks.
* Fisher-Yates shuffle bagsfor death messages — the 26 death messages and 8 sub-messages are shuffled like a deck of cards, guaranteeing you see every message before any repeats.
* Rate-limiting aware:5-second cooldown between API calls with exponential backoff on 429 errors. The game never breaks if the API is down.

Gemini also generates a "Performance Review"on the victory screen — a sarcastic AI-written summary of your entire playthrough:

"Ah yes, 47 deaths. That's not a playthrough, that's a documentary about perseverance. Score: functionally irrelevant. Rating: 3/10, and 2 of those points are for not uninstalling. — Management"

### Easter Eggs

* Konami Code(↑↑↓↓←→←→BA) triggers a full-screenHTTP 418: I'm a Teapotexperience with RFC 2324 references, HTCPCP protocol headers, and animated CSS
* Clicking the "4.9★ Rating"on the menu — also triggers 418
* The AI chatbot: mention coffee, tea, latte, espresso, or brew → "Error 418: I'm a teapot. Per RFC 2324."
* Death #25displays: "🫖 The teapot weeps for you. Error 418."
* The faviconis literally a teapot emoji: 🫖
* The FPS counterincludes418 FPSin its rotation

### ⚠️ SPOILER WARNING: The Mechanics (For the Judges)

If you are judging the code and don't want to suffer through 10 levels to see the joke, here's what the engine actually does under the hood:

* 💰Coins steal your points— half the coins are traps that deal damage AND subtract 100 points.
* 🔺Spikes heal you— the pointy death triangles restore health. The signs say "AVOID SPIKES!" They're lying.
* ❤️Health packs damage you— the heart-shaped pickups are weapons of mass betrayal.
* 🚪Exit doors kill you— 3 out of 4 doors are instant death. The signs explicitly point you to the wrong ones.
* ✅"SAFE" platforms collapse— ISO-9001 Certified for disappointment.
* Level 5 is "Opposite Day"— literally nothing means what it says.
* Level 7 is a carbon copy of Level 1but with everything inverted. The sign says "Relax. It's Level 1 again." It's not.

## Prize Category

### 🏆 Best Google AI Usage

Google Gemini 2.0 Flash is deeply embedded in the gameplay — not as a gimmick, but as a core mechanic:

1. Context-aware AI companionthat ingests real-time game state (deaths, level, score, recent events) and generates unique, non-repeating roasts
2. AI-generated victory reviews— personalized sarcastic "performance evaluations" created by Gemini at the end of each playthrough
3. Graceful degradation— the game works perfectly without the API via keyword-matched fallback responses, so judges always have a working experience
4. Built entirely using Google Antigravity— the AI coding agent that helped architect the engine, write the troll dialogue system, and debug the final button's fleeing behavior

The intersection of "world-class AI" and "deliberately terrible software" is the joke. We used the best tools available to build something that provides zero value. Technology.

### 🫖 Best Ode to Larry Masinter

This game is a love letter to RFC 2324 and HTTP 418:

* The Konami Codetriggers a theatrical 418 screen with RFC citation, HTCPCP protocol headers,X-Larry-Masinter: Legend, and the classic nursery rhyme ("The requested entity body is short and stout / Tip me over and pour me out")
* 3 discovery pathsto the teapot: Konami code, clicking the rating, and a hidden tile in Level 1
* The AI chatbotresponds to ANY coffee/tea reference with RFC-accurate 418 errors
* Death milestone #25references the teapot
* The creditsinclude a dedication:"Larry Masinter — RFC 2324 (1998) — HTTP 418: I'm a teapot 🫖"
* The faviconis a teapot
* The FPS countershows418 FPS

Larry Masinter gave the internet its most important error code. This game gives the internet its most important platformer. Neither serves any practical purpose. That's the point.

### 🎭 Community Favorite

The game is designed to generate stories. The tab title changes. The AI roasts you personally. The cookie banner steals your dignity. The quit button fights you. And the "Share Your Shame" button on the victory screen copies your stats to clipboard in a pre-formatted post:

"🏆 I just beat DEFINITELY NOT A TROLL GAME™ with 47 deaths and a score of -200. The coins robbed me. The spikes healed me. The doors killed me. The button ran away. I have trust issues now."

Between the rotating fake reviews on the menu ("I didn't know I could be gaslit by a platformer" — @trust_issues_69), adaptive death messages that never repeat, and a settings menu where the Fun toggle refuses to turn off... I think this might be the game that makes people screenshot and share.

Built with spite, caffeine, and Google Antigravity. No teapots were harmed in the making of this software. Several keyboards were.

Dedicated to Larry Masinter, who in 1998 wrote an April Fools RFC that became a permanent part of the internet. We should all be so lucky.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse