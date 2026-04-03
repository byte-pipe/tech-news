---
title: 'A Silly Idea: A Star Wars Lightsaber Duel in the Terminal with GitHub Copilot CLI - DEV Community'
url: https://dev.to/gramli/a-silly-idea-a-star-wars-lightsaber-duel-in-the-terminal-with-github-copilot-cli-1ki7
site_name: devto
content_file: devto-a-silly-idea-a-star-wars-lightsaber-duel-in-the-te
fetched_at: '2026-02-12T19:27:48.021723'
original_url: https://dev.to/gramli/a-silly-idea-a-star-wars-lightsaber-duel-in-the-terminal-with-github-copilot-cli-1ki7
author: Daniel Balcarek
date: '2026-02-09'
description: This is a submission for the GitHub Copilot CLI Challenge 🎬 What I Built In a previous... Tagged with devchallenge, githubchallenge, cli, githubcopilot.
tags: '#devchallenge, #githubchallenge, #cli, #githubcopilot'
---

GitHub Copilot CLI Challenge Submission

This is a submission for theGitHub Copilot CLI Challenge

## 🎬 What I Built

In a previous submission for aproductivity tool, I sneaked in a small Easter egg inspired byThe Matrix. That led to a slightly silly thought, what if I built an actual movie scene usingGitHub Copilot CLI, renderedentirely in a terminalwith Unicode characters?

That idea stuck with me.It sounded unnecessary, impractical…and kind ofawesome🙂

So I decided to create aStar Wars inspired lightsaber duel in pure CLI.My very first idea was the Lord of the Rings “Ride of the Rohirrim” scene 🐎🐎, but I quickly realized I should keep the scope smaller — after all, it’s still just a terminal and Unicode characters. 😆

## 📽️ Teaser

The full animation is a bit too long for this post, so I prepared a short “teaser” instead.

#### View the complete version (~65 seconds) on GitHub

#### 🏃‍♂️ Run it locally

git clone https://github.com/Gramli/star-wars-animation.git

cd
star-wars-animation
dotnet run

Enter fullscreen mode

Exit fullscreen mode

Note:

* You’ll need.NET 10 SDKinstalled.
* Use a font with good Unicode support (e.g.,Cascadia Code).
* TheVisual Studio ConsoleorVS Code terminalrender the block characters best -> they’re true Jedi-level terminals 😄

⚠️ Running in classiccmd.exeor other limited terminals may break the animation. Consider it atraining exercise for Padawans, only the worthy (and properly equipped) terminals will experience the duel in all its glory.

## 🎥 My Experience with GitHub Copilot CLI

I brought the idea and created severaldetailed prompts. Copilot handled most of the code generation and quickly produced a nice draft version. However, something was missing — it lacked soul.

At that point,Copilot stopped being just a code generatorand became aCreative Director.I kept refining prompts, pushing for stronger visuals, better animation flow, and more cinematic moments.

Here’s a real example of how our “conversation” looked:

* Me:The animation works and we already have some nice effects, but we need to take it to the next level an Oscar-movie level. We need a real wow effect that makes this animation stunning. Can you suggest 3–5 ideas?
* Copilot:

Here are a few ways to push the animation toward a more cinematic feel, even within CLI constraints:

1. Lightsaber motion trails to make fast swings feel fluid and powerful
2. Gradient-based lighting to simulate glow and light falloff
3. Impact shockwaves that briefly distort the screen on heavy clashes
4. Molten damage on walls and floors that cool over time
5. Cinematic letterboxing during key moments to focus attention

I’d start with motion trails and molten damage for the biggest visual impact.
Which one would you like me to implement first?

Enter fullscreen mode

Exit fullscreen mode

Copilot responded with ideas like motion trails for lightsabers, gradient lighting, shockwave effects, molten damage on walls, and even cinematic letterboxing. Some of them made it into the final version, others stayed on the cutting-room floor, but theprocess itself was surprisingly fun.

I was genuinely impressed. Copilot helped transform a simple ASCII-style drawing into a small but entertaining show. Sure, it’s not an Oscar-winning movie, but for a playful, slightly ridiculous idea, I think it turned out pretty cool.

### 💥 When We Failed (And Pivoted)

Things went smoothly… until I had avery bad idea:

“What if we add a camera rotation illusion?”😅

Yeah. That was ambitious.

This turned out to be a real challenge, even for Copilot. After many new sessions and repeatedly reworking prompts, we eventually had to pivot. A full Y-axis camera rotation just wasn’t readable with simple ASCII silhouettes, so we ended up experimenting with X-axis rotation and a top-down view instead.

At that point, the silhouettes are so minimal that the viewer has to mentally accept the perspective shift, but that’s part of the charm (and limitation) of doing cinematic nonsense in a CLI.

And honestly? That experimentation, even when it didn’t fully work was one of the most fun parts of the project.

## 💭 Final Thoughts

I really enjoyed this ride. UsingGitHub Copilot CLIfor something completelynon-practical, visual, and slightly absurdturned out to be agreat experience. It pushed me to think differently about prompts, iteration, and collaboration with an AI, not just as a tool, but as acreative partner.

May the Source be with you!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (17 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
