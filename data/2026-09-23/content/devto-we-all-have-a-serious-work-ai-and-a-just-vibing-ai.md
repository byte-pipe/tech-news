---
title: We All Have a "Serious Work" AI and a "Just Vibing" AI. When Did That Happen? - DEV Community
url: https://dev.to/dj29/we-all-have-a-serious-work-ai-and-a-just-vibing-ai-when-did-that-happen-5fl2
site_name: devto
content_file: devto-we-all-have-a-serious-work-ai-and-a-just-vibing-ai
fetched_at: '2026-09-23T15:19:26.768344'
original_url: https://dev.to/dj29/we-all-have-a-serious-work-ai-and-a-just-vibing-ai-when-did-that-happen-5fl2
author: Dhruv Jani
date: '2026-09-22'
description: Hi Guys!!! As you know I wasn't good for well, a week and Now..... Let's Dive In!!! I never... Tagged with discuss, ai, gemini, antigravity.
tags: '#discuss, #ai, #gemini, #antigravity'
---

Exposing the hidden costs of AI tool choices

Hi Guys!!! As you know I wasn't good for well, a week and Now.....

Let's Dive In!!!

I never consciously decided which AI gets which job. Somehow, I just ended up with a ranking in my head. It just happened — one small decision at a time, until one day you noticed you have an entire unconscious hierarchy, and you can't fully explain how it got built.

Here's mine, laid bare.

## The IDE has its own pecking order

I use Antigravity as my AI IDE now — GitHub Copilot went pay-to-use, so that door closed. Inside Antigravity, I don't use one model. I use two, and which one shows up depends on what's actually at stake.

Claude Opus gets the hard stuff: planning, and the UI bugs that don't have an obvious cause. Gemini 3.1 Pro gets everything else — the routine work, the smaller changes.

Here's the part I only admitted to myself recently: Gemini 3.1 Pro hallucinates more than Opus does in that context. I know this. I use it anyway, for most of my day-to-day work, partly because it has more usage headroom than Claude does inside Antigravity. So the model doing the bulk of my actual coding isn't the one I trust most — it's the one I trustenough, running more often because I can afford to run it more often. I hadn't said that sentence out loud until I wrote it just now.

## The chatbots are a completely separate hierarchy

Outside the IDE, on the plain chatbot websites, the routing rules are different again:

* ChatGPTis my "is this even possible" AI. Syntax checks, rubber-duck debugging, quick throwaway questions. Free tier, small model, fast answer — I'm not trying to get something profound out of it, I just want an answer in the next ten seconds.
* Claudeis my quick-draft AI — names, ideas, urgent doc edits when something needs to sound right in the next two minutes.
* Geminigets a strangely specific and non-negotiable job: PYQ (previous year question) and calculation-heavy problems. I have never once seen it give me a wrong answer there. Not "usually right" — never wrong, in that specific lane. Ask it something about code or general facts and it can absolutely be off. Ask it to trace through a calculation and I don't double check anymore.

That's not "I like Gemini." That's a very narrow, very specific trust — earned in one lane, and it doesn't transfer to any other lane.

## The moment that gave the whole system away

I only really noticed Ihada system when it broke in a small, dumb way.

I asked Antigravity's agent to look at the final draft of a post I was about to publish — just check if everything was aligned, bolds in the right place, tags correct. A one-glance job. Instead, the agent opened a browser, took a screenshot, entered the URL, took another screenshot, moved the cursor, tried to click something, took a third screenshot, and kept going — burning a chain of actions and tokens on a task that needed about two seconds of looking at a page.

I stopped the execution mid-loop. Then I did what I always do for that exact task: opened ChatGPT and asked it to just look at the draft. Done in one reply.

That's when it clicked that my routing isn't really about "which AI is smartest." It's about matching theshapeof the tool to theshapeof the task. An agent that can act in the world was simply overkill for something that needed a two-second glance. More capability didn't help. It just made the mistake more expensive.

## It's not just work, either

The hierarchy follows you into conversations that have nothing to do with code.

Cricket is huge where I'm from, and there's a test I didn't design on purpose, it just kept happening. If I open a chat and say something as lazy as "man, [team] isn't winning today" — zero context, zero setup — Gemini goes and figures out who's actually playing, pulls their current form, checks the squad, and gives me an actual case for why they can or can't pull it off. If the match is live, it grabs the live score in the same breath. ChatGPT, given the exact same one-line prompt, asks me what the score is.

Same lazy prompt, two completely different experiences. One feels like talking to someone who was already watching the match. The other feels like I have to catch it up before we can even start.

I don't think that means Gemini is smarter. It just needs less hand-holding in that particular situation, and apparently that's enough to make me reach for it more.

The funny part is I never consciously chose any of these roles. I just kept coming back to the tool that annoyed me the least for each kind of conversation.

## What this actually says, if I'm honest

I never wrote any of these rules down. I just kept using whichever tool annoyed me the least for a particular job, until those choices turned into a system.

So — genuinely asking, not rhetorically:

What's your hierarchy for different AI usecases? Which AI gets your real work, which one gets your throwaway questions, and was there a specific moment that revealed the system to you the way the screenshot loop revealed mine?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (23 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse