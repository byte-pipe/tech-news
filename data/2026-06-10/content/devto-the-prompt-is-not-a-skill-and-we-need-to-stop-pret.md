---
title: The 'Prompt' Is Not a Skill — And We Need to Stop Pretending - DEV Community
url: https://dev.to/harsh2644/the-prompt-is-not-a-skill-and-we-need-to-stop-pretending-3m18
site_name: devto
content_file: devto-the-prompt-is-not-a-skill-and-we-need-to-stop-pret
fetched_at: '2026-06-10T12:07:40.510893'
original_url: https://dev.to/harsh2644/the-prompt-is-not-a-skill-and-we-need-to-stop-pretending-3m18
author: Harsh
date: '2026-06-09'
description: Writing a prompt isn't engineering. It's typing. You type what you want. The AI figures out the rest... Tagged with ai, career, programming, discuss.
tags: '#discuss, #ai, #career, #programming'
---

Judgment over conversational inputs

Writing a prompt isn't engineering. It's typing.

You type what you want. The AI figures out the rest That's not a skill. that's having a conversation with a very fast very confident intern who never admits uncertainty.

And yet. We've started calling ourselves prompt engineers We've started listing it on LinkedIn We've started acting like knowing how to ask is the same as knowing how to build. It's not.

The real skill - the one that actually matters the one that was always there never - changed. It's knowing what to ask for. It's knowing whether the answer is right It's knowing what the AI assumed what it missed and what it quietly broke without flagging.

Prompting isn't the skill Judgment is.

Let me explain why - and why pretending otherwise is actively hurting us.

## What We're Actually Doing

Let's be honest about what prompting looks like in practice.

You open a chat window. You type a description of what you want. The AI writes code If it's wrong or incomplete, you type another sentence. refining it The AI tries again You repeat until it works or until you give up and write it yourself.

That's not engineering. That's talking.

Engineering requires understanding trade-offs It requires knowing why one solution is better than another for a specific context It requires anticipating failure modes designing for change making decisions that will hold up when requirements shift six months from now and someone else is maintaining the code.

Prompting requires none of that.

The AI handles the trade-offs - or rather it makes choices without surfacing them to you The AI anticipates failure modes - poorly silently in ways you won't discover until production The AI makes the architectural decisions You review approve and ship.

We've outsourced the thinking and called it a skill.

We've confused using a tool with knowing the craft.

## The Lie We're Telling Ourselves

Here's the lie, stated plainly: I'm a prompt engineer I've developed a new professional skill.

You haven't. You've learned to talk to a machine that was specifically designed, at enormous expense to understand natural language from anyone The entire point of these models is that you don't need special knowledge to use them.

The AI doesn't need your prompt engineering skills It needs your judgment It needs you to know whether the code it wrote is actually correct - not just syntactically valid but correct for your use case your constraints your edge cases It needs you to catch the assumptions it made without telling you It needs you to ask "what happens when this list is empty?" because the AI won't ask that question It'll just assume a list will always have items write code based on that assumption and return output that looks completely reasonable until a user with an empty list hits the endpoint.

And here's the part that bothers me most: prompting is accessible to everyone My non-technical friends prompt My parents have started prompting My neighbor who describes "coding" as the thing where you make computers do things prompts They get useful results.

The thing that separates a developer from a person who has never written a line of code isn't the prompt It's knowing what to do with the answer It's knowing when the answer is wrong It's knowing which parts of the AI's output to trust and which parts to verify independently.

That's not a prompt skill. That's a development skill And we've had it all along.

## The Moment I Couldn't Unsee It

A non-technical friend pulled me aside at a gathering last month They'd been using AI tools for a few weeks and were clearly excited about it So you just type what you want and the AI writes the code for you? I said yes.

Then I felt something I didn't expect: embarrassment.

Because that's what I do I type what I want I review the answer I copy the relevant parts I ship it. And in that moment I realized my friend - who doesn't know what a stack trace is who has never debugged anything who thinks "deploying" means emailing a file - could do the same sequence of steps with the same tools.

So I asked myself the uncomfortable question: if a person without my background can follow the same workflow what's actually valuable about me?

The answer when I sat with it honestly: I know when the AI is wrong I know the questions to ask next I know what the AI assumed and whether those assumptions hold I know which of its solutions will cause problems under load or fail on edge cases or be a nightmare to maintain.

Those aren't prompt skills Those are engineering skills They took years of frustration and failure to develop And they're completely invisible in the prompt itself.

## What the Real Skill Actually Is

Prompting is the input method. The skill is everything that surrounds it.

Knowing what to actually ask for.Not "write a function that does X" That's easy anyone can do that "Write a function that handles empty inputs null values and malformed data and tell me what assumptions you're making - that requires knowing what could go wrong Which requires experience.

Knowing if the answer is right.The AI is always confident Confidence doesn't correlate with correctness You need the background to know when confidence is lying - when the code looks right but has a subtle flaw when the explanation is plausible but wrong when the solution works for the example but fails in the general case.

Knowing what the AI assumed.This is the one that bites most often. The AI doesn't tell you its assumptions - it just makes them and moves on The empty list The non-null pointer The timezone that's always UTC The user that always has a name Catching those assumptions before they reach production is an engineering skill full stop.

Knowing when to ignore the AI entirely.Sometimes the AI gives you a solution that technically works but is wrong for your context - wrong architecture wrong abstraction level wrong trade-off for your specific constraints Recognizing that requires understanding your system deeply enough to evaluate proposals not just accept them.

These are not prompt skills They are the same skills developers have always needed The input method changed The judgment required did not.

Prompting is easy Judgment is hard We need to stop conflating them.

## Why This Isn't Just Semantics

Calling prompting a skill isn't a harmless rebranding It has real consequences.

Junior developers are being told to learn prompt engineering as if it's a foundation - as if it substitutes for understanding data structures debugging system design how things fail It doesn't It can't A junior who can prompt but can't reason about their code is a junior who can produce output quickly and catch problems slowly.

Companies are hiring prompt engineers - roles that optimize for the input method rather than the judgment behind it They're building teams organized around the tool rather than the craft.

And developers are updating their LinkedIn profiles with skills that sound impressive but describe something any person with internet access can do.

The result: a layer of the industry that can generate but not evaluate That can ship fast but can't debug when it breaks That has strong opinions about which prompting techniques work best and fragile intuitions about why the code is actually wrong.

When the empty list assumption crashes production at 2 AM, the prompt won't save you The debugging skills will. The architectural intuition will. The experience of having been burned before will.

We're not prompt engineers We're developers who use AI as a tool. And the distance between those two descriptions matters more than it might seem.

## What I'm Doing Instead

I'm not quitting AI I'm not going back to writing everything from scratch That would be a different kind of self-deception.

But I've stopped calling prompting a skill in any meaningful sense of the word I treat it as an input method - the way I treat typing or using a terminal It's how I talk to a tool not a capability I've developed.

I focus on the things that require actual judgment: architecture edge cases failure modes trade-offs the assumptions hidden in outputs that look correct. I ask what did the AI assume? before I ship I treat confident AI output with the same skepticism I'd give a confident junior who hasn't worked in production yet.

I remind myself regularly: typing isn't engineering Thinking is And I don't put prompt engineering on my resume.

## One Question

Are you a prompt engineer?

Or are you a developer - with real skills, real judgment, real experience who happens to use AI as a tool?

I've made my choice about how I answer that.

What's yours? 👇

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (45 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse