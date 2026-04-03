---
title: 'BOLD: Ask Your Video Library Anything - DEV Community'
url: https://dev.to/marcelfahle/bold-ai-for-the-spoken-word-3bj8
site_name: devto
fetched_at: '2026-01-07T11:07:18.492629'
original_url: https://dev.to/marcelfahle/bold-ai-for-the-spoken-word-3bj8
author: Marcel Fahle
date: '2026-01-04'
description: This is a submission for the DEV's Worldwide Show and Tell Challenge Presented by Mux What... Tagged with devchallenge, muxchallenge, showandtell, video.
tags: '#devchallenge, #muxchallenge, #showandtell, #video'
---

DEV's Worldwide Show and Tell Challenge Submission 🎥

This is a submission for theDEV's Worldwide Show and Tell Challenge Presented by Mux

## What I Built

Bold turns your video library into something you can actually talk to. Ask a question, get the answer — not a list of search results to dig through. The actual answer, pulled from your content, with a timestamp to prove it.

Upload your training videos, and Bold figures out what's in there. Not just transcripts (those are noisy garbage). We extract what's actually being taught. Then when someone asks a question, they get the answer. Click the timestamp, land on the exact moment.It's not search. It's answers.

## My Pitch Video

BQ02ayiNgCwHkrs01wu4XpoM8QlA8uYn0101

## Demo

https://yo.bold.video(demo using the Yo! Podcast by Rob Hope)https://boldvideo.com(marketing site - in progress)

Want to poke around? Drop a comment or reach out — happy to set up a test library for you.

## The Story Behind It

I've been building video infrastructure for almost two decades. Started with a headless video platform — just encoding, hosting, delivery — and some of those original customers are still streaming with me today.

A couple years ago, LLMs got good enough that I could finally solve the problem I'd been thinking about forever: video is impossible to search. You can't skim it. You can't Ctrl+F it. Once it's in a library, it's basically dead content.

Then I got into the coaching world through SaaS Academy and kept hearing the same thing: "We have 500 hours of training content and nobody can find anything." These programs invested serious money into video, and it was just... sitting there. Collecting dust.

So I built Bold to fix that. We extract what's actually being taught in each video — the signal, not the noise — and then search intelligently. The result: answers that actually come from your library, with timestamps to prove it.

Oh, and fun Mux story: years ago when Mux was just getting started, I actually interviewed for a job there. Talked with Matt and everything. Didn't work out, but I fell in love with the platform anyway. Been building on it ever since.

## Technical Highlights

The transcription problem:Most tools use Whisper or pull YouTube auto-captions. Fine for casual stuff, but it butchers industry terminology. We integrate with AssemblyAI, Deepgram, Speechmatics, Sonix, and Rev — and pick the best one based on your domain. Plus custom dictionaries so "Kubernetes" doesn't become "Cooper Netties."

Why "just search transcripts" doesn't work:Raw transcripts are noisy. Ums, tangents, repetition, half-finished thoughts. If you dump all that into a vector database and search it, you're searching garbage. You'll get results. They just won't be the right ones.

We do it differently. We extract structured understanding first — what's being taught, what questions get answered, the actual signal. Then when someone asks a question, we figure out which videos are even relevant before we start looking for answers. That's how you actually find the right thing instead of drowning in noise.

Stack:Backend: Elixir/Phoenix, lots of ObanDatabase: Postgres with multi-tenancyVideo: Mux (encoding, delivery, playback)Search: Meilisearch + pgvectorFrontend: Next.js SDK for custom portals

### Use of Mux (Additional Prize Category Participants Only)

Like I said — I've been a Mux fan since the early days. It's core infrastructure for Bold:

* Encoding & delivery:Every video goes through Mux. Fast encoding, solid CDN, just works.
* Timestamped playback:When our AI cites a source, we deep-link directly to that moment using Mux playback IDs. Click the citation, land on the exact second.
* Audio extraction:We pull audio from Mux-encoded videos for transcription.
* Thumbnails:Mux-generated thumbnails for video navigation and citation previews.

Honestly, Mux is one of those tools where you just set it up and forget about it. Which is exactly what you want from video infrastructure.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
