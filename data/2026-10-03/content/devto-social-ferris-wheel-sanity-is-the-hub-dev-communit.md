---
title: '🎡 Social Ferris Wheel: Sanity is the Hub - DEV Community'
url: https://dev.to/annavi11arrea1/social-ferris-wheel-sanity-is-the-hub-2m7j
site_name: devto
content_file: devto-social-ferris-wheel-sanity-is-the-hub-dev-communit
fetched_at: '2026-10-03T15:04:15.421231'
original_url: https://dev.to/annavi11arrea1/social-ferris-wheel-sanity-is-the-hub-2m7j
author: Anna Villarreal
date: '2026-09-30'
description: 'This is a submission for the Sanity Challenge, Path Two: Vibe-Code Something Strange What... Tagged with devchallenge, sanitychallenge, sanity, ai.'
tags: '#devchallenge, #sanitychallenge, #sanity, #ai'
---

Sanity Challenge Path Two Submission

This is a submission for theSanity Challenge, Path Two: Vibe-Code Something Strange

## What I Built

TLDR: Entrepreneur artist vibe codes her way to workflow optimization by consolidating all business social media posts through a single sanity content lake.

Why: Social media management is a huge task. It needs to be simplified. If you are a party of one like myself, you need all the optimization you can get.

I always thought it would be cool to have a single place to draft and send posts to all my social media platforms at once for my business. But I wanted to hold onto my final approval, to make sure a bot doesn't do something insane. We want to keep some sanity here. 😅

### The Build:

* A customized Sanity Studio
* A Claude agent that drafts seasonal social posts by reading the shop and a Knowledge Base over Sanity Context MCP
* A Node publisher that serves a human review queue

All of it is built around my existing Rails storefront at everfluorescent.com. Nothing posts to a platform yet, and that is deliberate. The first half is the story of getting here, including the parts that cost me days; the second half is how the system works.

## Demo

## Code

### New Additions:

## AnnaVi11arrea1/everfluorescent-desk

# Review desk — a Sanity App SDK app

A triage queue for social posts that an agent drafted and a person has to decide
on. Built with theSanity App SDK, it runs
in the Sanity Dashboard beside the Studio for project70komvgl.

It approves. It does not post.Approving setsvariant.statustoapprovedwhich is the state the publish worker reads. Nothing here talks to Instagram.

## Why an app and not another Studio pane

The Studio edits one document at a time, and a review queue is the opposite
shape. The thing that needs a decision isone platform variant, and a post
holds several — a Halloween post has an Instagram variant and a Facebook variant
with different captions, different assets, and independent verdicts.

So this lists variants across every post, each with the gate's verdict under it
and the buttons that move it…

View on GitHub

## AnnaVi11arrea1/everfluorescent-cms

# Ever Fluorescent — Content Desk

A Sanity Studio where one post is written once and rendered per platform, with
a preview pane that draws from the same rules that guard the publish button —
and a nightly job that pulls the store catalog in on its own.

Architecture write-up:https://claude.ai/artifact/NXcVq3ZiwfBxrF4zRBBP1j

## What is here

schemaTypes/ the nine document types, plus the variant object
lib/platformSpec.ts what each platform accepts — the single source of truth
lib/preflight.ts the checks that stand between a variant and the queue
components/ the preview pane, the four platform mock-ups, and the
 live sync console
actions/ the publish button (it approves; it does not post)
tools/obsidian-sync/ one-way sync from one vault folder into knowledge notes
functions/ code Sanity runs on its own — the catalog sync and its
 nightly trigger
sanity.blueprint.ts what to run and when

The rule that holds it together:lib/platformSpec.tsis the only place a…

View on GitHub

### Pre-existing Store:

## AnnaVi11arrea1/neoncart

# Neoncart — self-hosted store for Ever Fluorescent

Rails 7.1 ecommerce app: Stripe Checkout (card / Google Pay / Apple Pay)
dropshipper integrations (Printify wired end-to-end; ThisNew, ArtsAdd
Yoycol via configurable adapters + manual queue), branded shipping
emails with free tracking links, support ticket desk, and a partner
REST API + signed webhooks for FestConnect / goVend.

No paid add-on services: jobs run on GoodJob (Postgres — your Neon DB),
images on local disk via Active Storage, tracking via free carrier links,
email over plain SMTP.

## Stack

Rails 7.1 · PostgreSQL (Neon) · Puma · Hotwire (importmap, no Node) ·
Devise · Stripe · GoodJob · Faraday

## First-time setup

sudo apt install libvips 
#
 image variants

bundle install
cp .env.example .env 
#
 then fill it in

bin/setup 
#
 installs GoodJob tables, migrates, seeds

bin/rails s

Enter fullscreen mode

Exit fullscreen mode

Seeds create the admin user fromADMIN_EMAIL/ADMIN_PASSWORD, four
suppliers (Printify auto, the other…

View on GitHub

## My Build Process

I built this project from a terminal using Claude CLI. When Claude started to irritate me, Github Copilot CLI came to the rescue once. Ok, maybe I opened Vim, like 10 times. I prefer to not pass my api keys around if possible. Rather do that myself.

I kept notes as I worked, I could tell this was an undertaking.

### Here is a brief timeline:

* Up to 9/23: the store side.The Phase 0 Studio was in place: schema, per-platform previews, preflight checks, a publish gate, Obsidian sync and catalog sync. On the neoncart side, four PRs merged: a product id and gallery endpoint, the Retro post search archive, the admin approve queue, and follow-up fixes. I also built a publisher tool into my admin dashboard, so I can preview business posts and publish them from inside my own store; it pulls from Sanity and saves published posts for reuse or modification later. I ran the migration, restarted the Jetson services, and both new admin tabs loaded.

* 9/24: reconnected the shop to Sanity through Vercel.

* 9/26: the agent.With the shop connected and posts populating in the approval area, it was time to hand the heavy lifting to an agent. generate.mjs already drafted campaign posts at needs_review from a template (captionFor). The agent replaces that template and the rest of the pipeline stays as it was. Its drafts now reach the admin queue, and the review card shows where sources disagreed and what each caption was based on.

* 9/27: refinement.I collected upcoming events near my customers, plus holidays and seasons, into one file so posts could be scoped to the time of year. I wrote a longer prompt that also records timings, which is where the caching numbers below come from. That was also the day I found stale data coming out of Sanity and finally traced it to the sync (details in the next section). The re-run wrote five clean Halloween drafts.

* Last: the review desk.An App SDK app (everfluorescent-desk) lists variants across every post with the gate's verdict, and Approve / Back-to-draft write variant.status directly. It type-checks and builds, but I have not yet rendered it against my live data. I expect two things when I do: every card will say no knowledge notes were cited, and if no platformAccount document exists everything will show Blocked. Both would be real findings, not app bugs.

### Time-Costing Traps 🥅

1. Turn the MCP feature on before creating the endpoint. You cannot see the dashboard page that creates it until the feature is enabled. If you give your project a token before that, you have to delete it and create a new one with Context Viewer access.
2. Build the Knowledge Base entries after adding them. I built mine from the website and uploaded files once an Anthropic API key was in place. Entries that are added but not built are invisible to the agent, and this step is easy to miss.
3. The sync has to run from my local computer. Changes to the knowledge base only reached my server after I ran the sync locally. What gave it away was a last-sync date five days old. Files also had to be added to the sync list or they were never pulled in, so the agent kept getting old or incomplete data. After fixing that I had to rebuild the knowledge base again and redeploy Sanity. Files that are missing can also be archived.
4. The agent cannot see posts. The Context endpoint does not expose them, so my first--writerun proposed two products that already had template drafts from the Fall campaign. Both were correctly skipped, but that run's $0.49 was wasted. The agent is now told up front which products already have posts.
5. Claude caught its own bug in the review desk. The projection selects only some fields of each variant, so writing that array back would have silently destroyed the assets. It found the fix (useEditDocumentwith no path and a functional update) in the SDK docs rather than guessing.

Claude Catches Itself:

Claude CLI confirms neatly stored data

### Bad Data Exposed

My sources were disagreeing with themselves. Sanity can be used for quality control.

### Early design questions

Challenge

How it was overcome

Where does content live: Sanity, Obsidian or the store?

Obsidian stays my writing surface, with one-way sync into Sanity. Paintings mirror from the store instead of moving into Sanity.

Where does publishing actually run?

The publish worker runs on Vercel, not inside the neoncart store app.

Where does post approval happen?

Moved out of the Studio into my own store admin, with published posts archived in neoncart's database (the Retro post search tab).

Products with missing data (no price, no image)

Saved but flagged and blocked from posting, not silently skipped. Title, price and image are hard blocks; description and category only warn.

Lost catalog schema design doc

One salvaged copy survives (docs/catalog-schema-design.SALVAGE.md). Still open whether to rewrite it properly.

Per-platform post length and media limits (platformSpec.ts)

Found to be partly wrong against the real docs, so I am correcting them against the Instagram, Facebook, TikTok and LinkedIn developer documentation. Facebook's rate-limit documentation in particular is not good.

neoncart has no CI or tests, and deploy is manual on my Jetson

Every merged PR needs a git pull, rails db:migrate and a service restart by hand. Nothing auto-deploys.

New admin tabs not appearing after a merge

A stale running server: the migration alone does not restart Puma or the worker. Fixed with systemctl restart.

### Major Side Tangent

#### Prompt caching is a money saver. 💰

I stumbled into prompt caching along the way, and it could arguably be a post of its own.

Two cache points:

* one on the instructions and tool definitions, which do not change during a run.
* One that moves to the end of the conversation each turn so every turn reuses everything before it. 
The run summary line prints cache reads and writes with a dollar estimate, so I can see what each run costs.

#### Cost

The same three-draft run went from about $1.50 to about $0.39. Across six runs I spent $4.34, against $5.89 without caching. Priced again with identical tokens and no caching, each cached run saved between 47% and 62%, and the saving grew with the number of turns.

Request

Time

Cache write

Cache read

Uncached input

Output

1

3.1s

10,149

0

2

72

2

6.9s

4,223

10,149

2

608

3

6.8s

2,904

14,372

2

620

4

5.9s

8,034

17,276

2

473

5

20.0s

13,687

25,310

2

1,638

6

95.5s

11,125

38,997

2

8,863

Total

50,122

106,104

12

12,274

Input and output are in tokens. After the first request, everything before it was read from the cache, and only 12 input tokens in the whole run were billed at the full rate. Without caching that run would have cost about $1.09, so caching saved about $0.41, or 38%.

### Drafts that admit where sources disagree 🎭

Disclaimer: I can not correct all my data sources in a timely manner, so I've chosen to highlight this as a feature. Definitely not user error at all. 😅

The 9/27 re-run looked eight weeks ahead, excluded the four products that already had a post, and wrote five Halloween drafts with none skipped: six turns, about $0.58. Where two sources contradicted each other, the agent left the disputed claim out of the caption and recorded the conflict instead:• UV-reactivity. The Knowledge Base lists the hoodies, joggers and sweatpants as UV-reactive. The product listings never mention it, and my own dataset note limits it to the cat tapestry, original paintings and handmade items. No caption makes a glow claim.• Care instructions. The joggers listing says do not bleach or tumble dry; the Knowledge Base says tumble dry is safe. The caption says nothing about care.• Sizes. The Psychedelia Sweatpants description and the Knowledge Base both say XS to 4XL, but the variants a customer can actually add to cart stop at XXL. The same mismatch shows on Drippy Kitty and Mechanical Fantasy. The caption states no size range.

Those conflicts are now visible in the dashboard for me to see. Each review card has a cyan "Sources disagreed" box, and a "Drafted from N sources" list. The box does not block approval, because the caption already avoids the disputed claim. The sources come from the agent's run log.So I can use Sanity inside my own store to review generated posts that acknowledge conflicts and drop information that could mislead a customer.Added bonus with Sanity: editing an app inside Sanity turns out to be ordinary code. It was easy to set up the App SDK version of this.

### High Level View of System

Claude created a diagram for me, and I had Gemini make it a bit nicer looking.

The processes connect to 1 content lake in Sanity. The store never holds a CMS credential: a Sanity token cannot be narrowed below the project without an Enterprise plan, so one kept in the Rails app would also read the private knowledge notes.

✨ The publisher holds it instead, runs the agent's tool loop locally, and serves the store a queue over loopback. Magnificent. ✨

### Summary of Features

Feature

Where

What it does

Custom structure

sanity.config.ts

Needs review / Queued / Published as GROQ-filtered lists, a brandVoice singleton, syncs ordered by date

Custom document action

actions/queueForPublish.ts

runs the gate on every draft variant and approves what passes

defaultDocumentNode

sanity.config.ts

a Preview pane beside the form, with four hand-built platform mock-ups

Custom tool

components/SyncConsole.tsx

a live catalog-sync terminal in the top nav, over client.listen()

Filtered templates

sanity.config.ts

brandVoice and syncRun cannot be created by hand

Sanity Functions

functions/sync-catalog

document-triggered, 900s, its own robot token scoped to Editor

Blueprints

sanity.blueprint.ts

a nightly sibling on 15 3 * * *, read in America/Chicago

App SDK

the review desk

useDocuments, useDocumentProjection, useEditDocument, useQuery

Context MCP

publisher/context.mjs

JSON-RPC over HTTP, both JSON and SSE framing, session ids

#### Another Interesting Part

The catalog sync kicks off an external API call, and its shape is the interesting part. The Studio button does not call the store. It creates asyncRundocument; the function wakes on that document appearing, calls the store's API, and streams its log back into the same document while it runs. The Studio never needs the store's API key.

SyncConsole.tsx:241 — the entire action:

 
const
 
created
 
=
 
await
 
client
.
create
({

 
_type
:
 
'
syncRun
'
,
 
trigger
:
 
'
manual
'
,
 
outcome
:
 
'
running
'
,

 
startedAt
:
 
new
 
Date
().
toISOString
(),
 
dryRun
,

 
})

Enter fullscreen mode

Exit fullscreen mode

No fetch to the store, no API key in the browser. The Studio's onlycapability is creating a row.

The function wakes on that row appearing.

From sanity.blueprint.ts:

 
event:
 
{

 
on:
 
[
'create'
],

 
filter:
 
'_type
 
==
 
"syncRun"
 
&&
 
outcome
 
==
 
"running"
'
,

 
projection:
 
'
{
_id
,
 
trigger
,
 
outcome
,
 
dryRun
}
'
,

 
}

Enter fullscreen mode

Exit fullscreen mode

### The Drafting Agent: Claude

npm run draftasks Claude to find the season ahead and propose posts for the products that suit it, reading the shop and the Knowledge Base through two Sanity Context MCP endpoints. Each proposal carries its sources and any place two sources disagreed.

Claude proposes,planAgentDraftsdecides. Every proposal is checked against the dataset before anything is written.The product must:

* Exist
* Be active
* Have an image
* The hook must be five words or less
* Captions must pass preflight's caption rules.

Products that already have a post are left out of the prompt.

#### Importance of Structured Content Here 🚩

* A dropship supplier writes "glow in the dark" into copy for a print that is actually UV-reactive. That claim is false, and it costs a refund when the customer finds out it needs a blacklight. My own glossary note says what is true. The agent surfaces both sources instead of silently picking one, whereas a keyword search for "glow" would return the supplier's claim with equal weight.

### The workflow is data 🎢

A post is one idea with a variant per platform, so the status lives on the variant, not the post: an Instagram caption can be approved while the TikTok one goes back for a rewrite.The agent leaves its drafts at needs_review and a person moves them on. There is no separate agent status and human status to fall out of step, and no state the agent can reach that a person cannot see.The gate itself is written once. lib/platformSpec.ts in the CMS repo is the only place a platform limit is recorded — caption ceilings, hashtag caps, aspect ratios, asset counts, which of them are verified against the platform's own documentation and which are still carried from general knowledge. The Studio's preview pane reads it, the Studio's publish button reads it through lib/preflight.ts, the publisher reads a compiled copy, and the App SDK app reads the source copied verbatim. All four agree by construction.publishAttempt documents record what each send tried and what came back, request and response, so a failure is a document rather than a log line on one machine.

### The review desk, an App SDK app 🖥️

The review desk lists variants for each post with the gate's verdict and the buttons that move it. It updates live, because the SDK subscribes rather than polls. A draft the agent writes appears without a reload.

🎡 The layout is a wheel, (Ferris wheel!) with the post at the hub and its platforms orbiting on an ellipse. Angles divide evenly from twelve o'clock, and the vertical radius is solved as the smallest value at which no card overlaps another, so it adapts to any number of platforms automatically.

### The Storefront is Rails 🚂

This storefront is Rails 7.1 with Hotwire, running on a Jetson at home behind a Cloudflare tunnel, and it predates the challenge by a long way. It sells things, takes payments through Stripe, and pushes orders to dropshippers. I wasn't going to rewrite it for a contest.The custom app built on the content is React. The App SDK app, in TSX, live on top of Sanity. Rails is the business the content pipeline serves, not the deliverable. And it is the reason several things here are real rather than demonstrations:• the catalog sync pulls a genuine product feed from a genuine store, over a tunnel, with a documented failure mode about Authorization headers being dropped across a hostname redirect• the store's admin consumes the publisher's API over loopback, which answers "a workflow that kicks off an external API call" twice over•a wrong claim about a product matters because it costs a refund, not a style point

### What is not done 🫣

1. Nothing posts to any platform. Approval is only a status, so the pipeline stops one step short of its purpose. That is deliberate.
2. Platform limits need to be revisited.
3. TikTok and LinkedIn variants are seeded, not generated. A script copied the Instagram caption into them so the review wheel would have four spokes. The TikTok length warning is real, but the content under it is scaffolding.
4. Video duration is never checked. Sanity stores no duration, so the publisher and the App SDK app only warn.

## Sanity Project Details

Project ID: 70komvgl

Review Desk Link for those who can see it:

sanity.io

## Agent Sessions

Multiple days, multiple devices and terminals. A lot of sessions.

Desktop:

Microserver:

😅 And my terrible vibe coding in all its glory:

Sep 26 - Dead Sanity Token

claude.ai

Sep 26 - Publisher Crash Looping

claude.ai

Sep 27 - New Data not Appearing

claude.ai

This is alot, thank you for reading! <3

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse