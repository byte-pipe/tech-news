---
title: 'Two Weeks In: A 15-Year QA Veteran, Back to Being the New Guy - DEV Community'
url: https://dev.to/xulingfeng/two-weeks-in-a-15-year-qa-veteran-back-to-being-the-new-guy-39g3
site_name: devto
content_file: devto-two-weeks-in-a-15-year-qa-veteran-back-to-being-th
fetched_at: '2026-09-22T15:25:58.369508'
original_url: https://dev.to/xulingfeng/two-weeks-in-a-15-year-qa-veteran-back-to-being-the-new-guy-39g3
author: xulingfeng
date: '2026-09-22'
description: I started last Monday. Today it's been exactly two weeks. Here's the funny part. I've spent 15... Tagged with discuss, career, testing, ai.
tags: '#discuss, #career, #testing, #ai'
---

Relatable impostor syndrome at an AI startup

I started last Monday. Today it's been exactly two weeks.

Here's the funny part. I've spent 15 years in QA — manual testing, then automation, then test development, then test management. I've held just about every title this field has. And on day one, at a new desk, the feeling was as basic as it gets: I have no idea what I'm doing.

## Why here

The way it happened was mostly luck. After my last company laid me off, I didn't really look for work. I spent the time on dev.to, writing my 36 Stratagems series — 30 down, 6 to go. That stretch was honestly pretty good.

Then an old colleague called. He was hiring testers and asked if I knew anyone. I thought about it and said: how about me.

One conversation with the CTO, one HR interview, and then it was Monday.

Why I said yes is simple. It's an AI agent startup, a year or two old, sitting right on the hottest thing in the industry — and in a vertical, not another general-purpose wrapper. That was enough on its own. Poking at agents and models is what I do for fun anyway.

## Two things I noticed in two weeks

The first is process. The product → requirements → dev → test → ship pipeline here is genuinely different from what I'm used to. I'll be honest: the first week I thought it was a mess, and I'm still adjusting. When you're used to one kind of order, a different kind just looks wrong. Usually it isn't wrong. It's different.

The second is pace, and this one's good. My last company ran on instant replies. Requirements changed, and the PM was expected to answer on the spot. Here it feels slower, in the best way. Testers get more time and more room to make their own calls. You're allowed to think something through instead of getting dragged along by it. Two weeks in, this is my favorite thing about the place.

Do QA long enough and you learn something: slow is fast, and fast is slow. Time you steal up front gets paid back with interest, in rework and firefighting. Half a day spent on the edge cases, the weird inputs, the what-ifs — that half day usually buys back a week. So when I say this place feels slow, I don't mean nobody's in a hurry. I mean the pace goes where it counts.

## Understand first, judge second

Fifteen years buys you fast pattern recognition. You look at something and the problem jumps out at you. It also buys you a bad habit: when something doesn't match how you'd do it, the first instinct is to doubt it instead of figuring out why it's that way.

So my rule for these two weeks: understand first, judge second. A beginner's mind sounds easy. In practice it's an argument with yourself.

## The coincidence that makes me laugh a little less

I wrote a character in the 36 Stratagems series. His name is Mark.

Mark was the reliable one — years of experience, all of it in his head. His company slowly extracted that experience into a skill. Then they laid him off.

I wrote that one from the outside, as the author, feeling pretty pleased with myself.

In that story, the Skill scored 96.8% diagnostic accuracy across 312 historical failure scenarios. Then number 313 showed up. The 450ms retry window was a compatibility shim I'd written five years earlier for RabbitMQ, and it got applied to a system that had been running Kafka for years. I'd even left a note in the migration docs:450ms matches RabbitMQ GC window. Do not reuse outside this context.At the time, nobody understood it. They thought it was a stale config comment. Not until 4 AM, when the CTO went looking for it.

Here's the line I closed that post with:

The AI didn't fail because it was wrong. It failed because it was right about yesterday — and yesterday wasn't running anymore.

Then I joined this company. And on the walls and along the corridors, there are two signs:

Your experience is waiting to be forged into an Agent.

Great employees get the work done. Great Agents keep getting it done.

(In Chinese, since that's what they actually say: 你的经验，正在等待被炼成 Agent。／优秀员工完成工作，优秀 Agent 持续完成工作！)

Me: 15 years in QA, most of the titles in this field checked off at least once. By the standard of those two sentences, I'm not an employee. I'm raw material, still in the wrapper.

And look at that second one again. Great employees get the work done. Great Agents keep getting it done. So I do the doing, and it does the keeping. I raise it, it replaces me. Structurally speaking, the logic holds up.

Back when I was writing Mark's story, readers laughed. These days I walk under those signs and I laugh a little quieter. Part of me wants to read that closing line out loud, right there in the hallway: it wasn't wrong, it was just right about yesterday.

Though honestly, being forged into an Agent doesn't bother me much. Tinkering with agents and models is what I do for fun. I'm genuinely curious what 15 years of me would come out looking like.

One request, though: take your time. I'd like to finish those last 6 first.

## Fresh eyes

One more detail. After that Mark post went up, a reader left a comment pointing out that my timeline didn't add up — the same parameter described as a one-year-old thing in one place and a five-year-old thing in another. I'd gone through that story more than 30 times. Never caught it.

I replied in the comments: you read it more carefully than I wrote it.

That's the job, honestly. AI can run 312 cases. Case 313 still needs a human. And humans miss things too, which is exactly why you always want a pair of fresh eyes on it. Fifteen years in, that's still what I get paid for.

## What's actually worth extracting

Writing that Mark story is what made it click. The valuable part of experience was never the number 450ms. It was the context for why it's 450 and not 300 — context that came out of a 3 AM postmortem and never made it into a single doc.

So if these 15 years do get forged into something, I'd want more than the conclusions in there. I'd want the judgment behind them, the part that's hard to trace back to a source. Which is also why I wanted to work at an AI agent company. Not because I'm worried about being replaced. Because I want to find out, hands on, how this is supposed to be done.

## An apology I owe

30 of the 36 Stratagems are done. 6 are left. They're on hold while I get up to speed at the new job. So to my friends on dev.to: sorry. I'm not quitting the series. I just want to learn this business properly first, and then sit down and finish the last 6 the way they deserve. I haven't forgotten what I owe you.

## What's next

The story I wrote ended on something nobody ever asked: validation only works when the person who wrote it is still around to re-run it.

That question is part of why I'm here. The AI agent space doesn't lack smart models. What it lacks is people watching to see whether the thing still works. I've done that job for 15 years. Different track, same job.

I also just like this company's agent platform. It's the kind of thing I'd dig into on my own time. So the plan is boring and simple: learn the business, ship what I'm supposed to ship, then write the last 6.

Long road. Slow and steady. It'll go fast.

P.S. English isn't my first language. I use AI to polish the writing and smooth out the rough edges. Thanks for reading.☕ Buy me a coffeeP.S.S. The old series paperback is now available. Buy it here:Amazon - AI, Ego & Regret

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (50 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse