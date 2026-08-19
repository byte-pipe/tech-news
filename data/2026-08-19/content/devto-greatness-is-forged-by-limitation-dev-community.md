---
title: Greatness Is Forged by Limitation - DEV Community
url: https://dev.to/adamthedeveloper/greatness-is-forged-by-limitation-e20
site_name: devto
content_file: devto-greatness-is-forged-by-limitation-dev-community
fetched_at: '2026-08-19T19:23:06.162258'
original_url: https://dev.to/adamthedeveloper/greatness-is-forged-by-limitation-e20
author: Adam - The Developer ✨
date: '2026-08-19'
description: Can't believe I spent 2 weeks writing this. Last week, I gave a talk at a Cursor community event... Tagged with ai, programming, webdev, career.
tags: '#ai, #programming, #webdev, #career'
---

Can't believe I spent 2 weeks writing this.

Last week, I gave a talk at a Cursor community event about AI and how it's changing the way we build software. The event went great, and after the talk, quite a few people came up to me for 1:1 conversations.

One particular guy caught my attention. He wasn't a technical person, but he asked me something interesting:

"With so many tools and technologies available today, how do you even navigate all of this and pick the right ones?"

He thought it must be overwhelming. Then he smiled and said that with so many options available, he hopes many great things be built.

I thought about it for a second and smiled too, and before I could answer, he had to leave... but his question stuck with mi.

A few days later, sitting in a library looking for something to read, I ran into an answer:UNIX Network Programmingby W. Richard Stevens. (Great book btw, give it a read!)

90s tech, limited memory, limited processing power, limited bandwidth and limited tooling... etc.

Yet somehow, we got things like UNIX, TCP/IP, early operating systems, incredible mathematical breakthroughs, massive engineering projects, and some of the most elegant pieces of technology ever built.

It made me wonder:

What if the things that limited us were also the things that forced us to become better?What if greatness isn't always created by having more, but by being forced to do more with less?

The guy assumed more tools meant a better shot at greatness, but the book in my hands was proof of the opposite.

## The Paradox of Limitation

I believe there's a reason having less can sometimes make us better.

We usually think of limitations as something to overcome: less money, less time, fewer resources, less knowledge. All of it standing between us and what we want to achieve.

But there's another side to limitation we don't talk about enough.

A limitation doesn't just take something away. It also takes away what could have been.

And maybe that's exactly what we need. Because when everything is available, when every direction is possible, every tool is at hand, every approach is open to us, it sounds like freedom.

But freedom without boundaries can be surprisingly hard to live inside.

You give someone unlimited resources and they can spend a lifetime deciding what to do with them. Give them nothing and the question suddenly gets simple:

How much can I achieve with what I have?

That question changes how you think. You stop searching for the perfect tool, because it doesn't exist, and start building with what's in front of you. You notice details that would otherwise stay invisible, not because you're more observant by nature, but because you no longer have the luxury of not noticing.

Maybe that's the real gift of limitation. Narrowing down your options but also sharpening your attention.

Perhaps that's the paradox: the fewer doors we have, the more clearly we see the one we're standing in front of.

And btw, this isn't a new idea.

## Constraints Force Creativity

### The book

Let's take a look at Stevens' book for a moment. The book is essentially a walkthrough of the sockets API:socket(),bind(),listen(),accept(),connect(),read(),write(), andclose().

That's the whole vocabulary for making two machines on opposite sides of the planet talk to each other reliably.

But Stevens didn't invent those calls. The Berkeley sockets came out of UC Berkeley's CSRG in 4.2BSD, around 1983. Stevens wrote the book that taught a generation of programmers how they actually worked.

He wasn't designing for a world of infinite compute. He was documenting an API built in an era of expensive memory, slow CPUs, and unreliable, low-bandwidth links and there was no room for mistakes, sprawling do-everything interfaces, or generic, accept-all contracts.

Every function had to earn its place.

And with those constraints forced upon the people who designed it, the result is an API so minimal and well-composed that, four decades later, in a world where none of those original constraints exist anymore, it's still the interface nearly every programming language wraps for networking.

Take Python'ssocketmodule, Node'snetmodule, or Go'snetpackage, they all trace their shape back to those same eight or so primitives.

The paradox in miniature: by not having the luxury of building something bloated, they had no choice but to build something timeless instead. BSD built it under scarcity. Stevens documented why it was that tight.

And of course, this is also what surprisedmiwhen I decided to pick up a book from the 90s. I expected it to feel dated but instead, I ended up learning a great deal from it, much of which I can still apply to the software I'm building today.

### C

The language that started it all, laying the foundation for everything we have today.

C is a good example here, a language so elegant yet it gives you remarkably little. no GC, no elaborate standard abstractions, no safety net between you and memory. want something? you often have to understand what's happening underneath.

By today's standards, we'd call it unsafe or labeling it a weakness but that limitation also forces a certain kind of thinking, you have to pay more attention to details, you become more conscious of memory, data layout, ownership and what the machine's actually doing.

The language doesn't give you many options or answers but it makes you ask better questions and make better, timeless decisions.

### Go

Let's come back to the future, let's look at Go. Go takes a different direction, Its constraints weren't imposed by hardware, they were largely chosen by its designers.

With all the things available by its time, the language was designed with its featured kept deliberately minimal & simple. syntax wise, type system wise, fewer ways to express the same idea.

When a language gives you fewer ways to solve a problem, you spend less time debating which clever abstraction to use and more time solving the problem itself.

Go's restraint is the feature, What it leaves out is just as intentional as what it includes.

### Music

I play the piano, so this one isn't theoretical.

Today you can put a DAW, a thousand plugins, and an AI vocal fixer on a laptop and make a record anywhere. In the 70s and 80s, a lot of that work was physical. Cut the wrong stretch of tape and it was gone. Limited tracks, limited studio time, expensive gear. The band had to know the part. Screw up a take and sometimes everyone started over.

When recording time costs real money, you don't spend six hours on a snare. When you have eight tracks, you decide what deserves one. You can hear that in the records: the performances, the imperfections, the decisions.

I'm not arguing we go back to splicing tape. I'm saying the constraint did work that infinite undo doesn't.

## The Problem With Having Everything

Abundance can create complacency, endless choices... which creates the temptation to solve every problem by simply throwing more at it.

Let's come back to our topic regarding AI. Like a modern DAW, I believe AI is a wonderful partner in our work. But next to that, it is also removing a great deal of constraints faster than almost anything we've seen before.

Just a few years ago, a requested feature would take around 1-2 months. Trying a different architecture meant actually building it. Rewriting a block of code took time, and if it wasn't mine, I had to understand the context first.

Now I can ask AI to do all of that in seconds. The thing that used to stop you was effort. When that cost drops, it's easy to stop asking whether you should do it at all. You generate five versions instead of picking one. You add another library because the model already knows it. You rewrite working code because the new draft looks cleaner.

The shift isn't "can I build this?" anymore. it's"Should I?"

When you have nothing, the limits are imposed on you. When you have everything,you have to impose some on yourself.

## So What Do You Do With That

I never got to answer that guy at the event. If I could now, I wouldn't give him a list of tools.

I'd tell him more options don't guarantee better work and they just make it easier to never decide. The 90s didn't produce UNIX because people had more. They produced it because they had less, and less forced the work to get honest.

That doesn't mean throw AI away, or go back to cutting tape, or write everything in C. It means the environment won't hand you a limit for free anymore. If you want the sharpening, you have to pick one. Ship one use case. Let the model generate the boring parts and keep the core decision yours. Give yourself a deadline ugly enough that you can't keep adding.

Cap the stack this week.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse