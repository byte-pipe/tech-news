---
title: AI Didn't Remove the Engineering Work. It Just Made It Easier to Pretend You Did. - DEV Community
url: https://dev.to/dj29/ai-didnt-remove-the-engineering-work-it-just-made-it-easier-to-pretend-you-did-42m9
site_name: devto
content_file: devto-ai-didnt-remove-the-engineering-work-it-just-made
fetched_at: '2026-09-17T03:38:31.829669'
original_url: https://dev.to/dj29/ai-didnt-remove-the-engineering-work-it-just-made-it-easier-to-pretend-you-did-42m9
author: Dhruv Jani
date: '2026-09-15'
description: On September 15, India — along with Sri Lanka and Tanzania — celebrates Engineer's Day, marking the... Tagged with ai, discuss, career, webdev.
tags: '#discuss, #ai, #career, #webdev'
---

Comments debate where true engineering begins

On September 15, India — along with Sri Lanka and Tanzania — celebrates Engineer's Day, marking the birth anniversary of Sir M. Visvesvaraya. He was responsible for major irrigation and water-management projects, including the Krishna Raja Sagara Dam, and pioneered an automatic water-floodgate system first installed at the Khadakvasla Reservoir. He never called himself a founder. He was too busy building things that had to actually hold water.

I bring him up because somewhere between AI coding tools and the "building in public" era, a lot of people have quietly lowered the bar for what counts as engineering — and it's starting to show.

## The New Delusion

You've seen the pattern. Someone drops a single prompt into an AI tool, gets a working landing page, deploys it on a free-tier host, and by evening they're introducing themselves as a "founder." No architecture decisions made. No idea what happens when the free tier's rate limit gets hit. No review of what the model actually wrote. Just a URL and a post about "building in public."

The problem isn't that they used AI.

The problem is thathaving something that workshas quietly become synonymous withunderstanding why it works.

That's asking a vending machine for a soda and calling yourself a bartender.

The scary part isn't that AI can generate a working app in minutes — that part's genuinely great. It's that generating something and understanding something have quietly become interchangeable in a lot of people's heads. Ship fast, sure. Just don't confuse it with the part that makes you an engineer.

## What The Difference Actually Looks Like

I got a concrete lesson in this earlier this year, solo.

### The Rebuild

ShelfTalk started as a college assignment — a full MERN book-club app I built alone in a semester, shipped just well enough to pass, then left untouched on GitHub for months. GitHub's Finish-Up-A-Thon — a challenge built specifically around finishing AI-assisted work properly instead of leaving it half-done — gave me the deadline to go back in and rebuild it for production: real Socket.io chat instead of REST polling, a live synchronized reading room, a migration to MongoDB Atlas with GridFS, and a move off Create React App onto Vite that cut HMR times by roughly 80%.

I placed top 10 out of 500+ entries.

GitHub “Finish-Up-A-Thon” Challenge Submission

 Dhruv Jani
 

 Dhruv Jani
 

Dhruv Jani

 Follow
 

Jun 7

## ShelfTalk — Books Don't Talk. We Do. (A College Project, Revived)

#
showdev

#
devchallenge

#
githubchallenge

#
webdev

13
 reactions

Comments

 9
 comments

 4 min read
 

### The Bug That Made the Point For Me

None of that taught me as much as a bug that showed up weeks later, in production. I'd added what I thought was a clever optimization to push notifications — suppress the desktop ping if the tab was visible, since nobody likes getting notified about a message they're already reading. Clean UX, I figured. Then users started missing direct messages, and my own testing couldn't reproduce it: the code was working exactly as I'd designed it.

The bug turned out to live in an assumption, not a line of code.

My code had quietly conflated "the OS can render this pixel" with "a person is paying attention" — and anyone running ShelfTalk on a second monitor was silently losing every notification, because a tab in full view is technically "visible" even if nobody's looked at it in twenty minutes. The fix was to delete the optimization I was proud of. A slightly redundant ping is mildly annoying. A silently dropped message is a broken product.

Summer Bug Smash: Smash Stories 🐛🛹

 Dhruv Jani
 

 Dhruv Jani
 

Dhruv Jani

 Follow
 

Aug 22

## The Optimization That Was Too Good: Why Our Push Notifications Only Worked When You Weren't Looking

#
devchallenge

#
bugsmash

#
javascript

#
webdev

52
 reactions

Comments

 33
 comments

 3 min read
 

Nothing about that bug shows up in a demo, and you don't discover bugs like that by simply prompting your way through a project — noticing it required a user complaint and me sitting with "it's working exactly as designed" long enough to realize the design's core assumption was wrong.

Copilot wrote a lot of the ShelfTalk rebuild with me — it scaffolded the socket event handlers, caught import errors during the Vite migration, autocompleted UI patterns I'd have looked up manually anyway. But I wouldn't call any of it "vibe coded," because the version of vibe coding I'm criticizing skips the part where you find out your own project is broken and have to fix it under pressure.

That part — the reviewing, the debugging, the actually-knowing-what-you-built part — was the entire job. Solo, with no one else to catch what I missed. It was true for Visvesvaraya with concrete and steel. It's still true now with Copilot doing some of the typing, and it was just as true for one dumb boolean on a second monitor.

## So — Where's the Line?

I don't think AI is the problem. I think the problem is how easy it's become to skip the part that makes you an engineer while keeping the part that makes you sound like one.

AI didn't remove the engineering work. It just made it easier to pretend you did it.

So I'll ask directly: where do you draw the line between using AI to build something and just watching AI build it for you?

Have you ever caught yourself on the wrong side of it?👇

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (59 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse