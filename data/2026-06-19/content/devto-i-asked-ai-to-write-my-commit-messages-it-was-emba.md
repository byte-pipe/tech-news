---
title: I Asked AI to Write My Commit Messages It Was Embarrassing. - DEV Community
url: https://dev.to/harsh2644/i-asked-ai-to-write-my-commit-messages-it-was-embarrassing-a6i
site_name: devto
content_file: devto-i-asked-ai-to-write-my-commit-messages-it-was-emba
fetched_at: '2026-06-19T01:17:35.794927'
original_url: https://dev.to/harsh2644/i-asked-ai-to-write-my-commit-messages-it-was-embarrassing-a6i
author: Harsh
date: '2026-06-16'
description: I asked AI to write a commit message for me last week The code change was simple. A bug fix One line,... Tagged with git, programming, humor, productivity.
tags: '#git, #programming, #humor, #productivity'
---

Human context for future maintenance

I asked AI to write a commit message for me last week The code change was simple. A bug fix One line, easy to explain in a single sentence if I'd bothered to think about it for ten seconds.

The AI wrote:

Updated stuff. Fixed things. Improved performance.

That was it Four words of pure, unhelpful weapons-grade nothing I stared at it. Then I closed the tab. Then - for reasons I can't fully explain - I reopened it and stared at it again, as if it might improve on a second viewing.

I couldn't ship it. Not because it was technically wrong. Because it was soulless. It told a future reader absolutely nothing about what had happened, why it had happened, or whether it mattered.

That's when it hit me: AI can write code. It apparently cannot write a message that sounds like a human who gives even a small amount of a damn.

Here's what happened when I let AI write my commit messages for a week -and why I'm never doing it again.

## What Commit Messages Used to Mean

I used to actually spend time on commit messages.

Not hours. Not a whole production. But enough - a sentence that explained the why not just the what A brief note about a trade-off I'd considered and rejected. Sometimes a link to the ticket. Sometimes a one-line explanation of a genuinely weird edge case that future-me would otherwise stare at in confusion.

The message was never really for the code itself. The code speaks for itself, eventually, if you read it carefully enough. The message was for the next person the one who'd find this specific commit six months later, mid-debugging-session, wondering why on earth did anyone do it this way.

A good commit message is a small specific gift to your future self or to whoever inherits your code next.

I genuinely hadn't noticed I'd stopped giving that gift Not until I handed the job to AI and got back a perfect mirror-clean reflection of exactly how little effort I'd been putting in.

## The AI's Commit Messages: A Gallery of Shame

Here's what the AI produced for my last three actual commits I'm sharing these because I think you'll recognize the genre even if you haven't seen these exact words.

1 Fixed stuff.Three words. Zero context. Not the faintest clue what was fixed, why it needed fixing, or whether anyone should care.

2 Improved performance.By how much? Where in the codebase? Through what mechanism? Compared to what baseline? The message answers none of these and somehow still manages to sound confident about it.

3 Bug fixes and other improvements.This might be the most generic sentence that has ever existed in the English language It is, technically, true of almost every commit ever made by anyone.

The AI had access to the actual diff. It had seen exactly what changed, line by line. And given all that information, it chose to communicate essentially nothing.

Here's the part that actually got to me: these messages aren't even useful to another AI. If a different model reads "fixed stuff" in six months while trying to understand the history of this file, it gets exactly as much signal as a human would which is to say, none.

The commit message wasn't really the problem. It was a symptom. I had quietly stopped caring about the story of my own code, and the AI trained to be helpful and inoffensive - just mirrored that indifference straight back at me, dressed up in complete sentences.

## Why This Actually Matters

Commit messages aren't just decoration on top of Git history. They're not busywork.

They're for the teammate who finds this code in six months and needs to understand why a decision was made before they touch it They're for the person doing a code review who's trying to evaluate whether a change is reasonable. They're for you - specifically you, at 2 AM, staring at a stack trace, trying to remember what you were thinking when you wrote this.

A good commit message answers one question clearly: why did we do this?

A bad commit message answers nothing, while taking up exactly as much space as a good one would have.

The AI gave me generic, hollow commit messages because - and this is the uncomfortable part - I had already been giving generic, hollow commit messages for a while before I asked it to take over. It learned the pattern from my own recent history. It reflected my laziness back at me with perfect fidelity and zero judgment.

That's the part that actually embarrassed me. Not the AI's output. Mine.

The AI wasn't the problem. I was, and the AI just made it visible.

## The Lesson

I'm back to writing my own commit messages.

Not because I have some rule against AI assistance in general - I use it plenty for other things. But because I realized somewhere in this process that the commit message was never really meant for a computer to generate. It's meant for a human to read, and it should sound like it was written by one who was paying attention.

The AI can write the code. It can refactor, suggest, generate, autocomplete. What it apparently can't do - at least not without me actively caring first - is write the story of why a change happened. And the story is the part that actually matters, to the next reviewer, to the next maintainer, to future-me debugging something at an hour I'd rather not specify.

I don't need AI to write my commit messages.

I just need to care enough, for about fifteen seconds per commit, to write them myself.

## One Question

What's the worst commit message you've ever seen - or, if we're being honest with each other, written yourself?

I'll go first: "Fixed stuff."

I'm not proud of it. But I stand by sharing it.

Your turn. 👇

I used AI to help structure this post and organize my thoughts The experience, the Fixed stuff commit message, and the embarrassing realization are all mine.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (23 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse