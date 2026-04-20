---
title: Meet Hotfix—The Dragon Your Legacy Code Deserves - DEV Community
url: https://dev.to/anchildress1/meet-hotfix-the-dragon-your-legacy-code-deserves-4141
site_name: devto
content_file: devto-meet-hotfixthe-dragon-your-legacy-code-deserves-de
fetched_at: '2026-04-14T06:00:23.538425'
original_url: https://dev.to/anchildress1/meet-hotfix-the-dragon-your-legacy-code-deserves-4141
author: Ashley Childress
date: '2026-04-13'
description: Legacy Smelter is a thermal decommission platform where a Gemini-powered dragon analyzes your code and files very serious, very unhinged postmortems. Tagged with devchallenge, 418challenge, showdev.
tags: '#showdev, #devchallenge, #418challenge'
---

April Fools Challenge Submission ☕️🤡

This is a submission for theDEV April Fools Challenge

## What I Built

TL;DRThe permanent solution to every developer headache: thermal decommissioning.

* Upload a screenshot →Hotfixroasts it
* Gemini generates structured incident reports
* Community votes via escalation system + shares
* Top incidents become global P0 disasters

Hotfixfiles serious incident reports. It does not understand that it is completely unhinged. That's what makes it so funny.

Here’s a real incident report generated via live capture:

### I Am the Problem 🏚️

I am the subject matter expert (SME) for several legacy applications at work, and every single time somebody stirs dust in the server room—since I can't come up with any other viable explanation—something breaks. After dealing with this nonsense in one form or another for well over a solid year, I announcedthe permanent fix: smelting.I am fully confident that smelting those legacy servers will resolve my ongoing issues instantaneously.

The one thing I've been lacking in my fantastical smelting solution is a dragon. Nobody seemed rather invested in how serious I am about problem solving, because so far not one person has offered me a dragon to get the job done. So I built my own—and I'm sharing it, because legacy code suffering is not a solo experience. Take a screenshot and let the Legacy Smelter handle the problem for you.

### Asset Designation:Hotfix🪧

MeetHotfix—and yes, I named the dragonHotfixbecause that is hilarious. Anything else would have been a giant missed opportunity for dragon naming. This app is more than a dragon, though—it's a whole incident management system. You can upload any screenshot—problematic code, poor UI designs, bugs that make you want to scream, or a selfie (if you can handle a little roasting)—andHotfixwill smelt the problem and give you a detailed incident report memorializing the true fix, which is melting it into oblivion.

The incident reports are added to a global manifest where you can share with friends who would appreciate your solution to the problem. Links are configured to unfurl properly on most platforms, including Slack and Discord. Sharing an incident is considered a containment breach by the system—wait seven seconds between shares to avoid rate limits—which increases the overall Impact for that incident. You can also escalate your favorite incidents, which carries even more weight. The top three global incidents with the highest impact rating are displayed on the main page as P0 priority.

💡Operational Notice:Submitted images are processed by Gemini's paid API. Google is not using your uploaded images for training—they're only retained 55 days for abuse monitoring. Do not submit assets you do not own. Do not submit from a company device.

## Demo

Live athotfix.anchildress1.dev—head to the live site for camera uploads, since iframes don't have camera permissions.

### Try to Break It ⛓️‍💥

Upload:

* The worst UI you've ever seen
* Your most cursed code snippet
* A selfie (if you think you're emotionally prepared)

Then:

* Share it
* Escalate it
* Win a sanction
* Try to get into the global P0 leaderboard
* Copy your output in the comments—it counts as a containment breach!

## Code

The repo includes the full React frontend, Express server, Cloud Functions for sanction judging, Firestore rules, and a docs/ folder with the design decisions and prompt files referenced in this post.

## anchildress1/legacy-smelter

### A hardware-accelerated mobile web app that visually melts user-uploaded legacy tech into a puddle of slag. Built for the DEV April Fools Challenge.

# Legacy Smelter

A satirical incident reporting system for condemned digital artifacts. Upload an image. Hotfix processes it. Output: molten slag.

The system analyzes uploaded images using Gemini Vision and files a formal postmortem — classification, severity, failure origin, disposition, archive note — before thermally decommissioning the artifact via dragon-based remediation.

## Features

* Gemini Vision analysis— 16-field structured incident schema delivered via Gemini's constrained JSON mode
* Hotfix animation— PixiJS dragon idle, fly-in, and smelt sequence with audio
* Incident postmortem— full structured report overlay with social share (X, Bluesky, Reddit, LinkedIn) plus copy-link
* Global incident manifest— real-time Firestore feed of all thermally decommissioned artifacts
* Decommission index— live cumulative pixel count across all incidents
* Camera support— deploy field scanner via device camera or file upload

## Stack

Layer

Technology

Framework

React 19 + TypeScript + Vite

Animation

PixiJS 8

AI

Gemini (
gemini-3.1-flash-lite-preview
) via
@google/genai

Database

Firebase Firestore

…

View on GitHub

⚖️ This project is licensed underPolyform Shield 1.0.0and is released for this challenge asv2.0.0.

## How I Built It

### The Dragon 🥚

Getting the animation right was the hardest part of the entire build, and I went into it knowing almost nothing about sprite animation beyond whether something looked right or not. I found the dragon sprites onGameDevMarket.netand figured AI could handle the rest—which was optimistic of me, because AI is decidedly rough at producing smooth animation on the first try or the fifth. I picked up bits and pieces along the way, spent a humbling amount of time on what probably should have been a simpler problem, and I am still nowhere near an expert—but I am rather pleased with howHotfixturned out.

### The Stack 🧰

The front end is React 19 and TypeScript on Vite, Tailwind v4 for styling, PixiJS 8 for the dragon animation because Canvas 2D was never going to give me the smoothness I needed, and Howler.js so the smelt actually feels like something is happening. On the backend, Firestore handles everything community-facing, Firebase Auth gates the upload endpoint, and a small Express server keeps my Gemini API key off the client.

Gemini runs through the@google/genaiSDK with two models doing two different jobs. Sanction judging fires as a Cloud Functions v2onDocumentCreatedtrigger, claimed inside a Firestore transaction so concurrent invocations can't overlap.

Deployment is Cloud Run primarily because I like having the embeds available in these posts. I have a strong deployment pipeline already, which is running locally for this build instead of inside GHA—I already have the setup wired into Claude to build this flow for every app I create, so input from me is minimal.

The downside is that Cloud Run is not the stack I would have picked for this application had AI Studio not wired it that way from the beginning. Cloud Run is expensive, cold starts can be problematic for performance, and I didn't want it always-on just to run background functions—which I never scheduled anyway, so ultimately unnecessary. But that's how Cloud Functions got involved and turned this toy project into a three-server special in GCP.

### Global Smelt Accumulation 🌋

Every image uploaded is converted into a total pixel count and added to a running Firestore counter. It's displayed at the top of every page and is a completely useless metric that I enjoy seeing—a completely valid use case.

### Vibing a Solution 🫠

I was convinced I didn't need to write tests for a toy project I didn't expect to last, and I failed miserably at that conviction. I ended up using Vitest with Testing Library and the Firebase emulator, because fighting AI to stop making the same mistakes gets expensive much faster than just writing a test suite. The majority of my time was spent validating and complaining that the UI was not yet finished across Claude, ChatGPT, and Gemini. I think the four of us together somehow managed to not embarrass me, which I have categorized as a win.

### Credits 🪙

Hotfixowes his entire existence to the artists whose work makes up the core of the experience. All assets sourced fromGameDevMarket.net:

* Dragon animation sprites—Animated Dragonby RobertBrooks
* Slag/liquid effects—Flowing Goo-Liquidby RobertBrooks
* Sound effects—Dark Fantasy Studio – Dragonby DFS (Nicolas Jeudy)

## Prize Category

### Best Google AI Usage 🏅

#### What Gemini Powers ⚙️

Two Gemini models power the live experience. Every upload is processed bygemini-3.1-flash-lite-preview, which:

* identifies the subject and draws a bounding box around the primary artifact
* extracts five hex colors as a chromatic profile
* generates a 15-field structured incident report under strict voice and word-count constraints
* Hotfixuses that bounding box to smelt the portion of the image Gemini actually flagged

gemini-3-flash-previewhandles sanction selection on a separate path, grading batches of five incidents based on comedic scoring rules—more on that below.

The voice was a complete accident. The first pass at the prompt was a plain "read the image and return a structured report" instruction, which worked fine right up until I tried to trick the system with a selfie just to see what would happen. It roasted me. Thoroughly.

I spent the rest of the build optimizing for that exact energy—an enterprise postmortem entirely convinced of its own importance. The voice rules at the top of the prompt file are the load-bearing ones:

## Voice

Enterprise incident report. Postmortem tone: dry, precise, operational, concise. Accusatory toward the artifact and its history.

The system treats absurd subjects as routine incidents. It is filing an incident report. It does not know it is funny.

## Comedy mechanics

-
 Specificity over generality. "Also, the green paint" is funny. Find the one weird concrete thing in the image and call it out.

-
 The deadpan afterthought. End a technical assessment with a flat, too-honest trailing observation.

-
 Commit beyond the point of reason. Start institutional, then dramatically escalate without changing tone.

Enter fullscreen mode

Exit fullscreen mode

"The system does not know it is funny" is the whole design philosophy in one sentence. That's the entire premise in a nutshell.

Every one of the 15 returned fields has its own word-count cap and voice constraint baked into the prompt—without them, Gemini defaults to generic corporate language and the bit falls apart. The full prompt file is in the repo inserver.js.

#### The Sanction Logic 📛

gemini-3-flash-previewhandles the sanction path—Flash Lite falls apart on comparison judging across a batch, and Pro is overkill that actually loses some of the unhinged quality Flash is known for.

The original image is never stored, so Gemini can't grade accuracy against the source—it can only judge the writing. The first draft used strict grading criteria and kept picking the most technically accurate report instead of the funniest. Version two mostly lets Gemini run wild, and it picks the funny one now. The guidelines that survived:

Signals that a record may deserve sanction:

-
 disproportionate institutional seriousness applied to an ordinary software or workplace failure

-
 precise, concrete details that make the situation feel embarrassingly real

-
 escalation from a small defect, design choice, or human workaround into procedural absurdity

-
 wording that implies everyone involved has accepted something obviously unreasonable as normal

-
 dry phrasing that lands harder the straighter it is read

Do not reward a record merely for being:

-
 wordy

-
 random

-
 technically dense

-
 surreal without a clear comedic turn

-
 mildly clever but interchangeable with the others

Enter fullscreen mode

Exit fullscreen mode

The full sanction prompt file is in the repo infunctions/sanction.js.

#### Building with Google AI 🧪

I touched nearly every Google AI tool during this build. Gemini Chat for brainstorming and prompt iteration, but it couldn't hold context long enough to be useful past the first few rounds. AI Studio for the initial scaffold—which checked my live API key into the repo on init, so that was fun until GitHub's secret detection caught it before I did. The CLI for animation work, though the accessibility skill was broken and I ended up routing around it. Antigravity until the free tier ran out mid-animation pass. Gemini Pro for the social banner, only it wasn't able to iterate for accurate edits. Each one ran out of steam before I was done, which is how I ended up reaching for all of them.

What actually shipped runs on Gemini. Every postmortem isgemini-3.1-flash-lite-previewdoing exactly what it's good at, live, in production. Every sanction isgemini-3-flash-previewreading a batch of five and picking the one a dev would quote to a coworker. Two models, two jobs, both in constrained JSON mode, both doing real work on every request.

Gemini's version of this project is released asv0.0.1and produced this rather useless but very funny animation:

What actually shipped runs on Gemini. Every postmortem isgemini-3.1-flash-lite-previewdoing exactly what it's good at, live, in production. Every sanction isgemini-3-flash-previewreading a batch of five and picking the one a dev would quote to a coworker. Two models, two jobs, both in constrained JSON mode, both doing real work on every request.

### Community Favorite 🪩

Legacy Smelter is a system designed to be shared, escalated, and collectively abused. Every incident lands on a global manifest, links unfurl on Slack and Discord, shares rack up breach points, escalations carry real weight, and the top three P0 incidents are permanent shrines to whatever the community found most absurd. If that sounds like something you'd enjoy, you're exactly who I built it for.

### The Permanent Fix

All in all I'm more than thrilled to finally have my dragon accessible whenever I'm fed up with something. It's a nice way to relieve some stress and the output can be genuinely hilarious overkill.

Some problems just aren’t meant to be fixed...

They’re meant to be smelted.

## Ashley ChildressFollow

Distributed backend specialist. Perfectly happy playing second fiddle—it means I get to chase fun ideas, dodge meetings, and break things no one told me to touch, all without anyone questioning it. 😇

#### 🛡️ Thermally Decommissioned with Assistance

This post was written by me with collaborative editing from Claude, ChatGPT, and Gemini. The code forLegacy Smelterwas built using Claude Code—who also wrote the tests, the deployment pipeline, the Cloud Functions, and then got put to work on this submission post because I don't believe in downtime.

ChatGPT and Gemini were consulted at various stages, though "consulted" is generous for how often they were told they were wrong. No AI was harmed in the making of this project, but one of them has now been through every phase of the software development lifecycle in a single sprint and may need to file its own incident report.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
