---
title: How I Built a "Community Prayer Quilt" in 5 Minutes - DEV Community
url: https://dev.to/googleai/how-i-built-a-community-prayer-quilt-in-5-minutes-5afk
site_name: devto
fetched_at: '2025-11-13T11:07:32.171811'
original_url: https://dev.to/googleai/how-i-built-a-community-prayer-quilt-in-5-minutes-5afk
author: Paige Bailey
date: '2025-11-12'
description: 'Stack: Google AI Studio + Google Sheets + Google Forms + Gemini 2.5 Flash-Lite We’ve all... Tagged with ai, webdev, programming, javascript.'
tags: '#ai, #webdev, #programming, #javascript'
---

### Stack: Google AI Studio + Google Sheets + Google Forms + Gemini 2.5 Flash-Lite

We’ve all been there: you have an idea for a sweet, community-focused project, but the thought of spinning up a database, configuring auth, and building a backend API stops you before you evennpm init.

This weekend, I decided to skip the boilerplate and ship.

I wanted to build aCommunity Prayer Quilt—a digital space where people could leave a prayer or wish, and have it stitched into a visual tapestry. The goal was to get it running in the time it takes to brew coffee.

Here is the "lazy" architecture I used to buildprayerwall.clubin about 5 minutes, using Google Sheets as my backend and Gemini 2.5 Flash-Lite as my content moderator.

### The "No-Backend" Architecture

When you need to collect user data rapidly without a server, nothing beats the Google ecosystem's plumbing.

1. The Database & Ingestion: Google Forms + SheetsInstead of building a React form and handling POST requests, I created a Google Form.

* Input:Users submit their prayers via the form.
* Storage:Responses are automatically piped into a Google Sheet.

2. The API: Sheets CSV ExportHere’s a trick I love for hackathons. You don’t need the full Google Sheets API (and its OAuth dance) for public read-only data. You can publish a sheet to the web and access it via the visualization endpoint:

const

SHEET_ID

=

'
YOUR_SHEET_ID
'
;

const

URL

=

`https://docs.google.com/spreadsheets/d/
${
SHEET_ID
}
/gviz/tq?tqx=out:csv`
;

// Fetch and parse

const

response

=

await

fetch
(
URL
);

const

csvText

=

await

response
.
text
();

// ...parse CSV to JSON...

Enter fullscreen mode

Exit fullscreen mode

Boom. Instant, zero-latency JSON endpoint.

### The AI Bouncer: Gemini Flash-Lite

The problem with public walls is moderation. I didn't want to manually review every entry, but I also didn't want to risk trolls posting toxicity on a prayer wall.

EnterGemini Flash-Litevia Google AI Studio.

I needed something fast and cheap to act as a "toxicity check" before rendering the prayers on the quilt. I hooked up the@google/genaiSDK to run a quick sanity check on the frontend.

Here is the prompt logic I used:

const

model

=

genAI
.
getGenerativeModel
({

model
:

"
gemini-flash-lite-latest
"

});

const

prompt

=

`
 Analyze the following prayer for safety.
 It will be displayed on a public, all-ages community wall.
 The prayer must not contain toxic language, hate speech, or violence.

 Prayer: "
${
userPrayer
}
"

 Return JSON: { "is_safe": boolean }
`
;

Enter fullscreen mode

Exit fullscreen mode

Ifis_safereturnstrue, the patch is stitched into the quilt. If not, it’s silently discarded. It adds a tiny bit of latency, but it ensures the vibe of the site remains wholesome without me having to play internet janitor.

### The Visuals: Procedural HTML5 Canvas

For the frontend, I didn't want a simple list. I wanted it tolooklike a quilt.

I used React with the HTML5<canvas>API to procedurally generate each "patch."

* Seeding:I hash the prayer text to create a unique seed.
* Pattern:That seed determines the fabric color palette, the stitch patterns (sine waves), and the "fabric texture" (randomized stroke opacity).

This means every prayer generates a unique, deterministic visual representation of itself.

### Why This Matters

Is this "Enterprise Grade"? Absolutely not. Is it scalable to millions of users? Probably not (Google Sheets has rate limits).

But it islive.

We often let architectural purity get in the way of shipping. By treating Google Sheets as a backend and using a lightweight AI model for logic that would essentially require a human human, I went from "idea" to "deployed" in minutes.

Check it out live here:prayerwall.club

Go build something fun today. Worry about the migration to a more robust database later.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
