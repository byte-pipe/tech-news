---
title: AI Avatar v25 (Avatar Run, Voxel Avatar, Muscle Brain)💪 - DEV Community
url: https://dev.to/webdeveloperhyper/ai-avatar-v25-avatar-run-voxel-avatar-muscle-brain-5gi3
site_name: devto
content_file: devto-ai-avatar-v25-avatar-run-voxel-avatar-muscle-brain
fetched_at: '2026-10-15T15:30:43.662342'
original_url: https://dev.to/webdeveloperhyper/ai-avatar-v25-avatar-run-voxel-avatar-muscle-brain-5gi3
author: Web Developer Hyper
date: '2026-10-14'
description: Intro AI Avatar is a free app where your VRoid (VRM) avatar cheers you with all its... Tagged with ai, webdev, productivity, discuss.
tags: '#discuss, #ai, #webdev, #productivity'
---

Features a fun new marble-run game mode

## Intro

AI Avataris a free app where yourVRoid (VRM) avatar cheers you with all its might.🤗 It lives in yourVS Code sidebar(reacts to Claude Code /Codex /GitHub Copilot) orbrowser side panel(reacts to ChatGPT / Claude). Animations and speech bubbles all run without AI too.This time, I have 5 main topics.

* Avatar Run
* Muscle Brain 2D/3D
* Voxel Vatatar Update
* Jev
* Codex Support

Let's check them out together!😆

## Avatar Run

Avatar Runis a marble-run-type game where you avoid traps, try not to fall off the track, and reach the goal. First, I added a marble run to make AI Avatar more fun. But wait, I wanted to make it match the AI Avatar world better and change the marble to an avatar. Now an avatar runs around the track instead of a marble. But I also added a button so you can enjoy the marble version too. Maybe I will add an auto mode so you can enjoy Avatar Run while coding, like Voxel Avatar, in the future.

## Muscle Brain 2D/3D

I made a brain training game calledMuscle Brainlast year and released it on theMicrosoft Storeand as aChrome extension. I completely forgot about it for a long time, but recently I checked its status and found that it was still getting downloads. So I decided to migrate it to AI Avatar.

It was made withNext.js,React,KendoReact, andCSS-in-JS+Tailwind CSS, but AI Avatar was mostly made with plainTypeScript, so I had to rewrite the code. I thought it would be easy for AI to do this. However, the output had many regressions. I asked AI to fix them several times, but there were still many regressions. Then I noticed that the total code length was only half that of the original.🤣 That was why fixing the regressions never ended. So I gave up and started the migration from the beginning. This time, I strongly instructed AI not to cut any code and finally succeeded in the migration.

Also, the original Muscle Brain was a brain training game for remembering numbers or letters. So I added a new version for remembering 3D spatial information and created the newMuscle Brain 3D.

## Voxel Avatar Update

v22↓v21↓Voxel Avataris an idle game where you can grow a garden and place animals. You can grow the garden automatically or manually.

This time, I added more gardening patterns, animals, and user experience improvements like an outline display setting. I also added a roller coaster builder so you can take a ride and look around the voxel world.

## Creating 3D Models with AI

I wanted to make 3D object models with AI before and add them to AI Avatar. However, AI was not good at handling 3D, so I put the idea on hold. But at last, AI caught up, so I tried to make 3D objects using AI.

First, I made an image usingChatGPT. The point is to make not only a front view but also side and top views.

Next, I made my AI writeThree.jscode to display a 3D object. I made a harness to repeatedly generate Three.js 3D object code, compare the result with the reference image, and fix the code to get closer to the reference image. This way, I could run the AI autonomously for a while.

After I made the harness, I thought I no longer needed to use the latest, most expensive AI,Astra. So I tried it with the more affordable AI modelSonnet 5to cut costs. However, it couldn't make a 3D model at all. 🤣

I think making 3D models depends on the AI model, not my harness. But the latestOpus 5.5andSol 6.1have been released, so the situation might change if I test them again.

## Jev

Jevis a new AI that has features such as running super fast and being super cheap. This is possible because it does not use text but responds only with decisions and their scores.

I already had a positive/negative checker and feedback animations in AI Avatar. It was just determining positive/negative sentiment using a word list, and its accuracy was not good. So I updated it using Jev's ability to determine positive/negative sentiment.

Also, I added a dev log that can record Claude Code / Codex requests like bug fixes, new features, questions, and others, and display them by day, week, or all time. I hope this log will motivate developers to code more.

## Codex Support

I am using bothClaude CodeandCodexat work. However, I was only using Claude Code at home. This time, I wanted to useAstrabecause I heard it was good at handling 3D and thought it would be good for adding new 3D objects to Voxel Avatar in AI Avatar. So I subscribed to Codex and also decided to make AI Avatar react to Codex.

## How to Use the AI Avatar VS Code Extension Version (Thank you 300+ installs!)

You can download the AI Avatar VS Code extension in two ways.

* Option 1: Install from VS Code:Extensionsbutton in the left sidebar > SearchAI Avatar>Install↓↓
* Option 2: Install from the VS Code Marketplace:https://marketplace.visualstudio.com/items?itemName=web-developer-hyper.ai-avatar↓↓

## How to Use the AI Avatar Chrome Version

Install from Chrome Web Store: ↓↓https://chromewebstore.google.com/detail/ai-avatar/afmcfaeaaojalninahhhjnonhmlmiidi

## Special Thanks

* My DEV Community friend and CCO (Chief Creative Officer) 🤣,@annavi11arrea1collaborated with Catbot and AI Avatar in version 17, and keeps supporting me. Thank you very much!
* My friend and CDO (Chief Design Officer)🤣,@rutenveilhelped create the cool effects in version 15. and keeps supporting me. Thank you very much!
* My DEV Community friend and CTO (Chief Technology Officer)🤣,@gramlihelped update AI Avatar in version 2, and keeps supporting me. Thank you very much!
* My DEV Community friend and CMO (Chief Marketing Officer)🤣,@itsugo. Our avatar collaboration project was the beginning of AI Avatar, and keeps supporting me. Thank you very much!
* My colleague Maximum Blue helped make unique avatars in version, 6 and keeps supporting me. Thank you very much!

## Version 26 Update

I'm already working on the version 26 update. More fun updates, so please stay tuned!

## Outro

Ah! It's time to go for a run with my avatar, so I have to go now.💨 I would love to add more fun features and also use the latest AI in my next updates. I hope you enjoy the new updates to AI Avatar. Thank you for reading, and have a wonderful AI Avatar life!

## Comments Welcome!

* Do you have any ideas to make AI Avatar even morefun?
* Do you have any ideas to add moreAI features?
* Do you have any ideas for makingcool avatars and animations?
* Do you have any ideas to improve theuser experience?
* Do you have any ideas forincreasing the number of usersof AI Avatar?

Any other comments are also welcome!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse