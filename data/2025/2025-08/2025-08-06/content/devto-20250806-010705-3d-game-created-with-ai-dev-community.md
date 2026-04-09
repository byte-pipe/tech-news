---
title: 3D game created with AI - DEV Community
url: https://dev.to/mykolakorzh/3d-game-created-with-ai-455i
site_name: devto
fetched_at: '2025-08-06T01:07:05.013627'
original_url: https://dev.to/mykolakorzh/3d-game-created-with-ai-455i
author: Mykola
date: '2025-07-31'
description: This is a short, sum-it-up story about creating a small 3D browser video game proof of concept (POC)... Tagged with wlhchallenge, devchallenge, ai, bolt.
tags: '#wlhchallenge, #devchallenge, #ai, #bolt'
---

WLH Challenge: Building with Bolt Submission

This is a short, sum-it-up story about creating a small 3D browser video game proof of concept (POC) using bolt.new and calledFar Away Drive(video and game link are at the end of the article).

I had already submitted a couple of projects to the hackathon, but I wasn’t really feeling satisfied with them. I mean, both were fine and I’m glad I delivered what I planned, but they didn’t quite click for me.

Just a few days before the deadline, I came up with a concept for a short story-based game. In theory, it could be built withThree.js— but I wasn’t sure AI could handle it.

Still, I had plenty of tokens left… so why not try?

## Ready, Steady

With GPT’s help, I created an elaborate PRD. It partially covered the dialogues I had written, but the idea was to give Bolt some creative freedom — to let it come up with fitting interactions. (More on that later.) The result was a mix of wins and losses.

I’ve created a bunch of game concepts over the years, from rough sketches to more detailed scenarios. So crafting a good PRD wasn’t quick — it was a bit time-consuming, but I was happy with the output.

This one was planned as a grim, dark, story-heavy, text-driven game.I wanted to capture:

* the confusion fromKafka’s CastleandI Have No Mouth and I Must Scream,
* the stillness and isolation fromKentucky Route ZeroandNorco,
* and vibes from movies likeThe Machinist.

Mentioning these references actually helped both GPT and Bolt during the creation of Far Away Drive.

Once the giant prompt and PRD were ready, I gave it a go. And boom — magic happened. The base game, with three locations, was generated in one shot thanks to the detailed PRD. I was honestly surprised. It looked like it could actually be done. That’s when the hardest part began — active refinement.

Quick sidenote: I also tried creating even more detailed and heavy PRDs in parallel, feeding them into Bolt. The results were worse than my original version. One was so glitchy it was beyond repair, and the other was missing a lot of things I thought were essential. So I stuck with the original and kept refining it.

## It’s Game Time

As mentioned, time was limited. But I still wanted to keep the game narrative-heavy.So I delegated some of the dialogue trees to AI — partly to GPT, and some refinements through Bolt. The results were hit or miss: sometimes triggering or confusing, sometimes spot-on or even better than I expected. I had to prune everything that felt off and refine the good parts.

At one point, Bolt created an extra location — seemingly inspired by The Matrix. I’m still not 100% sure why. It was a scene with humans in pods, connected to a central hub. A cool touch of cyberpunk, I guess, but it didn’t fit the story arc, so I removed it.

Unfortunately, managing a few plot elements turned out to be very hard and time-consuming. There's still a possibility of getting half-stuck in the game. To partly fix that, I left one of the dev-mode features on — a camera/scene view switch. It lets players reposition the camera and re-access dialogues or comments to finish a scene. Not perfect, but it helps not to be stuck (slap browser tab).

## Adding Objects

After almost every refinement prompt, Bolt would try to either add something extra or remove something I didn’t want deleted. So I had to stay on my toes and do a quick QA after every round.

As the project grew, adding or changing even small things became harder. Sure, updating a text string in the code was easy — but moving a 3D object elsewhere? Not so much. I guess I really need to learn how to work withThree.jsmore deeply.

Still, I had a blast working with Bolt to add sound effects, camera animations, and visual glitches. It all had to be done carefully, though — too much and the game’s atmosphere would break.

## Debugging and Free Camera

At one point, I came up with the idea of a debug/free camera — a temporary mode that let me roam freely through scenes, get coordinates, and feed them back to Bolt to fix camera positions. Not without problems, but it definitely helped straighten things out (AI loved to put the camera inside other objects).

Eventually, I had to restart the Bolt chat. Even small updates were taking too long and using up too many tokens. So I duplicated the project inside Bolt and started a fresh chat. This actually helped a lot with the final touches.

Simple things, like placing lamp posts along a road, seem easy — especially in a 3D editor. But with AI, it turned into a huge and complex task.

## Learning Curve

Creating decent-looking levels that matched my initial vision was super satisfying. I added music via Suno, and Bolt helped with glitchy visual effects to spice up the atmosphere. A few things that Bolt added unexpectedly — like some pretty crazy dialogue lines or random objects in the store — turned out really cool.

In my opinion, AI is great at helping you get an initial POC/demo of your concept up and running fast. But going full-scale and handling details is still tricky. Same with control — it’s easy to handle HUD/UI, but working with 3D objects can be a nightmare if you’re new to it.

That said, AI is great with plot twists and story scenarios.

If you're running low on ideas, it can help shake things up.If you have plenty of ideas, it can help transfer them into something

## What's Next

The dreamlike and Kafkaesque story in Far Away Drive is just a small part of the full game I’ve envisioned. I’d love to eventually build this out as a full-scale project. Working with Bolt made me think it’s possible. For now, though, I’m planning to polish the current version a bit more, squash some bugs, and eventually bring it to itch.io. Hopefully, Bolt can help me package everything up for that too;)

quick video overview:https://youtu.be/wOmfDKuy9Eggame:https://tubular-treacle-ef1c30.netlify.app/

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
