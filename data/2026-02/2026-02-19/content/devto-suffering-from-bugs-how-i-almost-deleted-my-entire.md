---
title: 'Suffering from BUGS: How I Almost Deleted My Entire Project - DEV Community'
url: https://dev.to/maame-codes/suffering-from-bugs-how-i-almost-deleted-my-entire-project-1eef
site_name: devto
content_file: devto-suffering-from-bugs-how-i-almost-deleted-my-entire
fetched_at: '2026-02-19T11:19:46.517679'
original_url: https://dev.to/maame-codes/suffering-from-bugs-how-i-almost-deleted-my-entire-project-1eef
author: Maame Afua A. P. Fordjour
date: '2026-02-19'
description: You know that iconic DJ Khaled album, "Suffering from Success"? The one where he looks overwhelmed by... Tagged with showdev, devops, python, typescript.
tags: '#showdev, #devops, #python, #typescript'
---

You know that iconic DJ Khaled album, "Suffering from Success"? The one where he looks overwhelmed by how much he's winning?

Yeah... IWISHthat was me.

For the last 48 hours, I wasn't suffering from success. I was Suffering from Bugs. Specifically, the kind that make you question if you should drop out of Computer Science and just become a farmer instead.

I spent two days staring at a screen that screamed 500 Internal Server Error and ModuleNotFoundError. I was winning on localhost:3000 (it worked perfectly!), but the moment I tried to deploy? Disaster.

Here is the story of how I almost deleted my entire project out of frustration, and how I turned a 45-second nightmare into a win

## 1. The "Works on My Machine" Trap

I think everyone who codes in general has faced this trap maybe one too many times in their life. The reason I decided to build this project in the first place was because I have an upcoming quiz worth 30 marks of my final grade in a couple of weeks, and looking at 80+ slide per every week's lecture would be a nightmare for my revision. I do write notes (in my own words for better understanding) but when it gets to the last minute, I still cannot go through all my notes to refresh my memory of 200+ slides or even more for half of my semester. Then I decided to build 'SlideSift': Very simple tool that basically summarizes your lecture notes, just for revision.

Some of us including myself, are slow learners, and I struggle to just read or study something once, for it to stick forever. People with those kind of abilities are so lucky! But if you are like me, this would actually help you in your uni studies.

I built it using Google Gemini Pro. On my laptop, it was beautiful. It felt like magic.

But then I tried to deploy it to Render.

The Reality Check:

Cloud servers are not your laptop. They don't care that "it works for me."

Myrequirements.txtwas a mess. The server installed an ancient version of the AI library that didn't even know what "Gemini" was.

Lesson Learned:If you don't lock your dependencies (e.g.,google-generativeai>=0.8.3), the cloud will humble you very quickly.

## 2. The 45-Second Awkward Silence

The perfect scenario of how I was feeling whiles waiting for the web app to summarize the notes I uploaded, is very similar to those times when DVD's were a thing, you insert the disc into your DVD player, and sometimes if its corrupt, it shows 'disc error'. Or for my gamers, if any of you ever used the Nintendo GameCube, sometimes when you insert the tiny disc, it takes like 2 mins to load and gives you an error, then while it loads, you pretend to look into the sky so it loads faster... 😂only to receive an error and all you feel is disappointment.

Anyway, back to the story:

Once I finally fixed the crash (after what felt like 50 deploys), I hit the next wall: Latency.

Gemini Pro is smart, but it is slow.

I would upload a PDF, click "Summarize," and then... wait.And wait.And wait.

It took 45 to 60 seconds to get a response (Honestly speaking I think at a point it took like a solid 3 mins to even end up giving me an error).

Gemini pro took 45 to 60 seconds to summarize a single PDF. Then I tried to change it to Gemini Flash 1.5, for some weird reason I crashed the app when I used the Flash version, it didn't work at all.

Imagine showing this to a recruiter:

Recruiter clicks "Summarize"... spinner spins ...... awkward silence ...... "So, how's the weather?" ...... still spinning ...

Or people even using this, with modern technology in 2026, no one would wait 3 mins for a web app to work, let's be honest here. Even me the creator, didn't want to wait that long!

I hated it. It felt broken. I seriously considered hard-coding a loading message that said: "Go make a coffee, this will take a while."

This is when the Imposter Syndrome kicked in hard. I thought, "Real engineers build fast apps. I built a loading screen simulator."

3. The Pivot: Choosing Speed (Groq)

I realized I didn't have aCodeproblem; I had anArchitectureproblem.

I didn't need the "smartest" model in the world (Gemini Pro) to summarize a PDF. I needed the fastest one.

I scrapped the Google integration and switched to Groq (running Llama-3).

Groq is an inference engine designed purely for speed.

The result?

Before: > 50 seconds.

After: < 30 seconds.

It was instant. I clicked the button, blinked, and the notes were there. I literally screamed. I had been sitting behind my PC for hours, just surviving on zero sleep, dried mango slices (love them) and iced americano just to stay awake to make it work.

4. Why I Didn't Quit (The DevOps Mindset)

Well I did almost delete the entire repo and the project itself, because I kept on having so many deployment issues and Render kept on sending these error messages to my mail:

I got almost 20 of these messages and that was the time I almost gave up on this. But when I was staring at those error logs, wanting to delete the repo, I realized something: This IS the job.

As a CS student, I love writing code. But as an aspiring DevOps engineer, my job isn't just to write code, it's to ship it.

* Fixing the requirements.txt? That'sEnvironment Management.
* Switching from Gemini to Groq? That'sSystem Design.
* Handling the "Cold Start" on the free tier? That'sCost Optimization.

Honestly, that's why I am always heavy on building as you learn, because truly, that is the only way to make it stick. If I am to work on another project and face these issues, I would immediately know what to do. Tech is so fascinating, you will lose your mind sometimes but its truly remarkable.

## The Result

Slide Sift is now live. It turns chaotic lecture slides into pristine study guides instantly.

Try it here (Live Demo)(Note: It’s on the free tier, so give it at most 50s to wake up the first time!)

Check the code onGitHub

To anyone stuck in "Deployment Hell" right now:

Don't delete the repo.Take a walk. Drink some water/ coffee for my coffee lovers 😉. CRY IF YOU HAVE TO

The error is probably just a missing environment variable. You got this. 💙

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
