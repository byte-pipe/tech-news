---
title: Why I Built My Own Humanizer (And Why You Should Too) - DEV Community
url: https://dev.to/dannwaneri/why-i-built-my-own-humanizer-and-why-you-should-too-2a9e
site_name: devto
content_file: devto-why-i-built-my-own-humanizer-and-why-you-should-to
fetched_at: '2026-02-27T11:15:44.110583'
original_url: https://dev.to/dannwaneri/why-i-built-my-own-humanizer-and-why-you-should-too-2a9e
author: Daniel Nwaneri
date: '2026-02-24'
description: There's a tool called humanizer — a Claude Code skill built by blader, inspired by Wikipedia's guide... Tagged with ai, writing, tooling, webdev.
tags: '#ai, #writing, #tooling, #webdev'
---

There's a tool called humanizer — a Claude Code skill built by blader, inspired by Wikipedia's guide to detecting AI writing. It's good. 6,600 stars, hundreds of forks, an active community adding patterns and language support. If you want to strip AI tells from any text, it does that well.

I used it. Then I built something different.

The problem isn't that humanizer is wrong. It's that it's solving a slightly different problem than the one I actually have.

Humanizer checks your writing against a generic human baseline. It knows what AI writing looks like and flags the patterns — significance inflation, copula avoidance, the rule of three, em dash overuse. Twenty-four patterns derived from Wikipedia's AI cleanup guide. Run your draft through it, find the tells, rewrite.

That works if your goal is writing that doesn't look AI-generated.

My goal is writing that sounds like me.

Those are related but not the same thing. I can write a draft that passes every humanizer check and still sounds nothing like my published work. No AI tells, no voice. Sterile, voiceless prose is as detectable as slop — it just gets detected by different readers.

The thing I needed wasn't a list of patterns to avoid. It was a calibration against my own writing at its best.

So I built voice-humanizer. Same foundation as blader's tool — same 24 patterns, now 27 with three new ones from a community PR. But with one addition that changes what it does: a CORPUS.md file containing your own published writing, from which the skill extracts your voice fingerprint before it checks anything else.

Voice check first. AI pattern check second.

The fingerprint tracks what you reach for and — just as important — what you don't. Rhythm, specificity, the patterns absent from your corpus that signal drift.

Here's what that looks like in practice. I ran voice-humanizer on a draft of this post before publishing. It caught this:

Before (draft):

The fingerprint tracks rhythm patterns, paragraph opening style, specificity signals, what you reach for when you need a concrete detail, and — just as important — what you don't do.

Flag:

Voice drift — list of five items where your corpus shows you compress to two. Em dash doing emotional emphasis work your corpus handles structurally.

After:

The fingerprint tracks what you reach for and — just as important — what you don't. Rhythm, specificity, the patterns absent from your corpus that signal drift.

No AI pattern was triggered. A generic humanizer would have passed this. Voice-humanizer caught it because the corpus knew this author compresses lists. That's the difference.

When it flags something now, it doesn't just say "this pattern looks like AI." It says "this reads as Claude because it uses three parallel items where your corpus shows you compress to two. Here's what you'd likely do instead."

That's a different kind of feedback.

The corpus approach also solves a problem humanizer can't: false positives.

My writing uses em dashes. Not excessively, but deliberately — once per piece, structurally. A generic humanizer would flag that. Voice-humanizer won't, because it appears in the corpus. It's my pattern, not AI bleeding through.

Same for any other stylistic choice that looks like an AI tell in isolation but is actually part of your voice. The corpus is the ground truth.

You can use voice-humanizer with your own writing. The repo is public:github.com/dannwaneri/voice-humanizer

CORPUS.md is gitignored — your writing stays private. CORPUS.example.md shows you what to put there. Five questions in SETUP.md help you extract your own voice fingerprint before you start.

It won't work without a corpus. That's intentional. A humanizer calibrated to nobody's voice in particular isn't calibrated to yours.

Credit to blader for the foundation — the pattern list and skill format this is built on. Voice-humanizer solves a narrower problem for a specific kind of writer: someone who's been writing long enough to know what their best work sounds like — and doesn't want AI assistance to flatten it.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)


For further actions, you may consider blocking this person and/orreporting abuse
