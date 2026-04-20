---
title: LLMs can be absolutely exhausting | Tom Johnell
url: https://tomjohnell.com/llms-can-be-absolutely-exhausting/
site_name: hnrss
content_file: hnrss-llms-can-be-absolutely-exhausting-tom-johnell
fetched_at: '2026-03-16T11:23:27.680061'
original_url: https://tomjohnell.com/llms-can-be-absolutely-exhausting/
date: '2026-03-15'
description: Some days I get in bed after a tortuous 4-5 hour session working with Claude or Codex wondering what the heck happened. It's easy to blame the model - there'...
tags:
- hackernews
- hnrss
---

# LLMs can be absolutely exhausting

15 Mar, 2026

Some days I get in bed after a tortuous 4-5 hour session working with Claude or Codex wondering what the heck happened. It's easy to blame the model - there's so many options to choose from:

1. They're dumbing down the model to save money.
2. Context rot!
3. Codex/Claude Code/[insert harness] is getting bloated.

It's not uncommon for me to come back to the problem the next day, my own context window cleared from rest, and find a fast and fulfilling path forward with the help of the LLM. What's going on?

## I'm tired & experiments are too slow

### As I get more tired, the quality of my prompts degrade

This one seems pretty obvious. If I am becoming mentally fatigued, I will write worse prompts, and because of that, the AI will do a worse job. Here's an example of what happens when I'm really tired: Kick off a somewhat meaty prompt (after 30% of context was used to align with the AI on the problem), realize right after submitting that I missed some key context, interrupt the LLM, provide the context, and then have it proceed. Without a doubt, interrupting Claude Code or "steering" in Codex leads to worse outcomes.

### Feedback loop is too slow and context is bloated

Some of the work I'm doing right now requires parsing some large files. There's bugs in that parsing logic that I'm trying to work through with the LLM. The problem is, every tweak requires re-parsing and it's a slow process. I liken it to a slot machine that takes 10 minutes to spin. To add insult to injury, some of these tasks take quite a bit of context to get rolling on a new experiment, and by the end of the parsing job, the LLM is 2% away from compaction. That then leads to either a very dumb AI or an AI that is pretending to know what's going on with the recent experiment once it's complete.

## The happy path with AI

### Avoiding the doom-loop psychosis caused by bad prompting

If I reach the point where I am not getting joy out of writing a great prompt, then it's time to throw in the towel. That has to be the first signal. If I'm half-assing it, being short, interrupting, and getting frustrated, then time to take a break.

There's some metacognition that needs to take place here. Am I being less descriptive because I haven't actually thought through this problem and I'm hoping the AI will just fill the gaps? That can be a very seductive trap to fall into. AIs are getting quite good at filling in undefined requirements, something that I remember having to do as a software engineer myself, but they're not good enough yet.

There's times I write a prompt with so much clarity in my desired end-state that I'm already celebrating the end-result when I submit the prompt because I know the AI is going to CRUSH IT. That's the feeling I need to look for in every prompt. If it's more the feeling of unsureness or impatience, it's just not going to pan out.

### Recognizing slow feedback loops and making those the problem

In the case of my parsing problem I mentioned above, it was too slow and the feedback loop was painful. I want my slot machine to take seconds/minutes to spin, not 15/20/30 minutes. In these cases, I've started to spin up a new session with the LLM, lay out my problem with feedback loop speed, express my desire to get to a sub 5-minute loop, give it an example of a failure case, and ask it to reproduce that failure case as quickly as possible. This is starting to sound familiar ... TDD anyone?

I was always the scrappy engineer. Sure I wrote tests, but I was never one to stop and create elaborate test cases or integration tests for bespoke problems. That was too time consuming, and also, I was getting paid even if my feedback loop wasn't perfect.

It's been quite the journey to fight that feeling that writing elaborate tests is time-consuming when working with AI. If you give an LLM clear success criteria: "Reproduce this specific failure case and make sure the clock time is less than 5 minutes to do it. Feel free to experiment with ways to optimize the code path or omit certain pieces that are unnecessary to reproduce" - the AI will not only reproduce the problem (maybe slowly the first time), but it will create levers for a faster feedback cycle. With that fast feedback cycle, it will consume less context and be SMARTER. This can seriously save hours of debugging time.

## Conclusion

When I am exhausted from working with an LLM - it might actually be a "skill issue". I need to recognize when I'm tired and entering the doom-loop psychosis. Cognitive outsourcing of requirements is seductive, but it's a trap. If I'm not enjoying the act of writing the perfect prompt and absolutely confident I will return to a result I'm 95% happy with, I need to either take a break or ponder if I've really thought through the problem. If things are moving slow and it feels as though context is filling up too quickly - I need to make that the problem to solve. Find a path, with the help of the LLM, to iterate faster and use up less context.

### Subscribe

You can subscribe to my blog viaemailorRSS feed.
