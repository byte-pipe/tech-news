---
title: I Built a Graveyard for My Dead Side Projects - With AI Eulogies & a 3D Cemetery - DEV Community
url: https://dev.to/varshithvhegde/i-built-a-graveyard-for-my-dead-side-projects-with-ai-eulogies-a-3d-cemetery-5g0e
site_name: devto
content_file: devto-i-built-a-graveyard-for-my-dead-side-projects-with
fetched_at: '2026-07-15T11:33:04.312715'
original_url: https://dev.to/varshithvhegde/i-built-a-graveyard-for-my-dead-side-projects-with-ai-eulogies-a-3d-cemetery-5g0e
author: Varshith V Hegde
date: '2026-07-12'
description: 'This is a submission for Weekend Challenge: Passion Edition What I Built Every developer... Tagged with devchallenge, weekendchallenge.'
tags: '#devchallenge, #weekendchallenge'
---

DEV Weekend Challenge: Passion Edition Submission

This is a submission forWeekend Challenge: Passion Edition

## What I Built

Every developer has a graveyard of side projects — started with fire, abandoned quietly on a Tuesday. They deserved better than an empty GitHub repo gathering digital dust.

DevGraveyardis a gothic memorial platform where developers give their abandoned passion projects a proper burial. Connect your GitHub, pick a dead repo, carve its epitaph — and watch Gemini AI write a dramatic breakup letter from you to the project.

Here's what it does:

* ⚰️Bury a project— 3-step burial wizard: pick a repo → choose cause of death ("Never Made it Past Localhost","Ran Out of Weekend","It Was Complicated"...) → write an epitaph
* 🪦Real tombstone data— pulls your actual commit history: peak obsession streak, most commits in a single day, last commit message (your final words)
* 🤖AI Eulogy— Google Gemini writes a dramatic breakup letter from you to the project, referencing your real commit data
* 🕯️Community mourning— light candles, leave RIP messages, vote to resurrect projects
* 🌐3D Graveyard— a full Three.js interactive cemetery: bare trees, fireflies, flickering candles, soul wisps, resurrection pulse rings. Click any tombstone to interact

My ownARweaverepo had 56 commits, a 2-day peak streak, 30 commits on its best day. Cause of death:"Never Made it Past Localhost."Last words:"feat: overlay plane in 3D builder — drag/scale image on marker, position saved to DB and restored in AR viewer."

It worked until it worked.

## Demo

🔗Live →devgraveyard.varshithvhegde.in

## Code

## Varshithvhegde/devgraveyard

### Give your abandoned passion projects a proper burial. A gothic graveyard for dead side projects.

# ⚰️ DevGraveyard

A memorial for your abandoned side projects. They deserved better than an empty GitHub repo gathering digital dust.

Live →devgraveyard.varshithvhegde.in

## What is this?

Every developer has a graveyard of passion projects — started with fire, abandoned quietly on a Tuesday. DevGraveyard gives them a proper burial.

* Bury a project— connect GitHub, pick a dead repo, choose a cause of death ("Never Made it Past Localhost","Ran Out of Weekend","It Was Complicated"...), write an epitaph
* Real tombstone data— pulls your actual commit history: peak streak, most commits in a day, last commit message as "final words"
* AI Eulogy— Google Gemini writes a dramatic breakup letter from you to the project, referencing your real commit data
* Community mourning— light candles, leave RIP messages, vote to resurrect projects
* 3D Graveyard— a full Three.js interactive cemetery at/graveyard-3d. Click tombstones…

View on GitHub

## How I Built It

### The Stack

Layer

Tech

Frontend

Next.js 14 (App Router), TypeScript, Tailwind CSS, shadcn/ui

Auth + Database

Supabase (GitHub OAuth, Postgres, Row Level Security)

AI

Google Gemini 
gemini-2.5-flash

3D

Three.js + React Three Fiber + @react-three/drei

Animations

Motion (Framer Motion successor)

Deployment

Vercel

### Step 1 — Burying a Project

When you click"Bury a Project", a 3-step wizard walks you through:

1. Choose Victim— your GitHub repos load via the API. Already-buried repos show an"already buried"badge and are disabled so you can't bury the same project twice.
2. Write the Epitaph— pick a cause of death from a curated list or write your own. Add an optional epitaph (100 chars max). In the background we fetch your full commit history.
3. Confirm Burial— a live tombstone preview renders with your real data before you commit.

### Step 2 — Commit History as Emotional Data

This is the technical heart of the project. When you bury a repo, we paginate through the entire commit history via the GitHub API and compute what I call"obsession data":

// From src/lib/github/analyze.ts

export
 
function
 
computePeakObsession
(
commits
:
 
GitHubCommit
[])
 
{

 
// commits per day → longest consecutive streak

 
// latest commit between midnight–5am → "latest night session"

 
// max commits in a single day → "best day"

 
// ...

}

Enter fullscreen mode

Exit fullscreen mode

These numbers feed directly into the tombstone — and into the Gemini prompt. A project that died after 30 commits on its best day tells a different story than one with 3 total commits.

### Step 3 — The AI Eulogy

The eulogy prompt is carefully engineered to produce something specific, not generic:

Write exactly 3 paragraphs. Format as a letter FROM the developer
TO the project. Tone: dramatic, darkly funny, genuinely melancholic.
Opening: "Dear {repo_name},"
Reference at least 2 of these real data points:
 - Peak obsession: 30 commits in a single day
 - Latest night session: 2:34 AM 
 - Cause of death: "Never Made it Past Localhost"
 - Last commit message: "feat: overlay plane in 3D builder..."
Close with: "Yours, but not anymore, — A Tired Developer"
Max 250 words. No markdown.

Enter fullscreen mode

Exit fullscreen mode

The results are genuinely surprising. Gemini knows you committed at 2 AM. It writes about that specific obsession. Here's what it produced for myARweaveproject:

"I remember the fervor, the peak obsession when I clocked 30 commits in a single day, mapping out every PLpgSQL schema and every front-end interaction. We built features that felt so robust within the confines of our little local development environment. You were a vibrant, if demanding, companion, demanding all my CPU cycles and mental bandwidth..."

The eulogy reveals with a typewriter animation when first generated, then persists in Supabase forever.

### Step 4 — The 3D Graveyard

The 3D view at/graveyard-3dis a full Three.js scene built with React Three Fiber.

The tombstone shapeis a singleExtrudeGeometryfrom aTHREE.Shape— a rectangle withabsarcfor the semicircular arch. Much cleaner than a box + half-cylinder:

function
 
makeTombShape
()
 
{

 
const
 
w
 
=
 
0.34
,
 
h
 
=
 
0.95
;

 
const
 
shape
 
=
 
new
 
THREE
.
Shape
();

 
shape
.
moveTo
(
-
w
,
 
0
);

 
shape
.
lineTo
(
-
w
,
 
h
);

 
shape
.
absarc
(
0
,
 
h
,
 
w
,
 
Math
.
PI
,
 
0
,
 
false
);
 
// perfect semicircle

 
shape
.
lineTo
(
w
,
 
0
);

 
return
 
shape
;

}

Enter fullscreen mode

Exit fullscreen mode

Animations in the scene:

* Tombstonesrise from undergroundon load, staggered by index (ease-out cubic)
* FlickerCandle— cone flame with per-frame scale noise + matchingPointLightintensity flicker
* SoulWisps— glowing orbs float upward from tombstones with candles lit
* ResurrectPulse— an expandingringGeometryon the ground below voted tombstones
* 55 firefly particles with sine-wave drift
* Fog, stars, bare winter trees, directional moonlight

You can light candles and vote to resurrect directly from the 3D panel— it calls the real API and the stone reacts in real time.

### The Public Graveyard Wall

Every buried project joins the public memorial wall at/graveyard, sortable by newest, most mourned, or most resurrection votes.

### Design Philosophy

The entire aesthetic is built around one idea:this should feel like a real memorial, not a joke. Developers genuinely grieve abandoned projects. The tombstones use engraved text, chiseled dividers, moss at the base. The AI eulogy takes commit data seriously. The community features are real interactions — your candle is stored in a database, your RIP message has an author and a timestamp.

The passion isn't just the theme. It's the subject matter.

## Prize Categories

🏆 Best Use of Google AI

DevGraveyard usesGoogle Gemini(gemini-2.5-flash) as the emotional core of the product. The eulogy generation prompt is engineered to reference specific real data points from the user's commit history — producing output that feels genuinely personal rather than generic AI text.

The key insight: the AI isn't just generatingcontent, it's transforming raw GitHub telemetry (commit counts, timestamps, last message) into something that makes youfeelthe loss of a project you actually cared about.

The eulogy is generated once per tombstone (owner only), stored permanently in Supabase, and revealed with a typewriter animation. It costs one API call and lasts forever — the project's eulogy becomes part of its memorial.

Built in a weekend. MyARweaverepo will never see production. But now it has a tombstone. That's something.

⚰️devgraveyard.varshithvhegde.in

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (30 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse