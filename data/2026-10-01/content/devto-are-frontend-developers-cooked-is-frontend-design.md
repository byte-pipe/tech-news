---
title: Are Frontend Developers Cooked? Is Frontend design safe? - DEV Community
url: https://dev.to/erikch/are-frontend-developers-cooked-is-frontend-design-safe-nn8
site_name: devto
content_file: devto-are-frontend-developers-cooked-is-frontend-design
fetched_at: '2026-10-01T17:18:15.643601'
original_url: https://dev.to/erikch/are-frontend-developers-cooked-is-frontend-design-safe-nn8
author: Erik Hanchett
date: '2026-09-30'
description: I recently put out a video arguing that frontend development is changing. I don't think the work is... Tagged with webdev, frontend, ai, career.
tags: '#webdev, #frontend, #ai, #career'
---

A 62-year-old vet's AI workflow advice

I recently put out a video arguing that frontend development is changing. I don't think the work is going away. The frontend developer title is what's changing, and a lot of us are turning into full stack developers.

The comments had opinions, so I recorded a follow-up.

## Pick a stack and get really good at it

One comment that I found really interesting was from a 62 year old developer with almost 30 years in the field. In the comment he described how Claude handles about half his workload now. His advice was to pick a couple of good frontend frameworks like Vue or Angular, pair them with a solid backend like C#, and become an absolute master at them.

I agree with him, and this was something I've always said. It's always good to be at least a specialist in one category. I use Kiro as my agent harness for most of my apps now, and I still want deep knowledge of the stack underneath. That way I can really understand what's happening and help steer the agent when things go wrong. The agents are good. They aren't good enough that I'd stop checking their work.

## Is frontend design the safer part of web dev?

This comment is where the title comes from. CRUD apps are the easy wins for LLMs, the argument goes, and attractive, non-generic UI with great UX is where they still struggle.

I sort of agree. With the older Anthropic models you could tell someone one-shotted a design at a glance. It had that very generic Tailwind template look. However, with every new model it's becoming harder and harder to tell. People who aren't looking at this stuff every day mostly think the designs look fine.

I didn't talk much about taste in my last video, but it is important. Looking at a screen and knowing whether the UX works, catching an accessibility problem, noticing that a flow is going to bog users down. That judgment still comes from people with experience. Still, LLMs are getting closer all the time.

## I rebuilt Winamp with an AI agent

To test this I picked something with a lot of small UI pieces. I hadKiro Crewrecreate the old Winamp MP3 player, and it came back as ErikAmp.

I was really impressed with everything it did with the UI. An equalizer with a row of sliders, a scrolling playlist, play, pause, stop, next and previous, shuffle, repeat, balance, volume. Getting every one of those working by hand would take me a couple of days, maybe less if I did nothing else. The agent basically one-shot it last Saturday. I had it fix a few bugs afterward, and it wrote a whole test suite along the way.

The source code is really simple. I never asked for Vue or React, so it skipped frameworks entirely. It's anindex.html, some CSS, a handful of JavaScript files, and a bit of Python.

You could argue that this design was already made, but still. I had it create three brand new themes, and it looks great.

## Where it starts to look like AI

The second app I showed is a 5K coach I built to get myself in shape for a race. It tells me what to do each day.

This is about as close as I get to the default Anthropic look. Dark cards, rounded corners, pill badges. It isn't flashy and I wouldn't call it amazing. For my own training plan it's fine, and it took a few minutes with my agent. Building it by hand would have eaten a lot more of my time.

## So are we cooked?

I don't think so. Building a frontend is the easiest it has ever been, and I got two working apps out of an agent with very little effort. Deciding whether those apps are any good is still the developer's job, and that takes knowing your stack and having some taste.

I'm also figuring out what to cover next. Do you want more AI workflow content, or more classic Vue and fundamentals tutorials? Tell me in the comments, and tell me where you think frontend is headed.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse