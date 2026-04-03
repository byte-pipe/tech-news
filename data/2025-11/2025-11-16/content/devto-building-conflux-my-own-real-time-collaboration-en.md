---
title: Building Conflux - My Own Real-time Collaboration Engine in Rust - DEV Community
url: https://dev.to/kayleecodez/building-conflux-my-own-real-time-collaboration-engine-in-rust-41lm
site_name: devto
fetched_at: '2025-11-16T11:07:00.924430'
original_url: https://dev.to/kayleecodez/building-conflux-my-own-real-time-collaboration-engine-in-rust-41lm
author: mitali
date: '2025-11-13'
description: I’ve always used real-time tools without thinking too much about how they actually work. Google Docs,... Tagged with rust, showdev, websocket, backend.
tags: '#showdev, #rust, #websocket, #backend'
---

I’ve always used real-time tools without thinking too much about how they actually work. Google Docs, Figma, Replit multiplayer, VSCode Live Share… you type something, the other person sees it instantly, nothing breaks, nobody overwrites anybody else. It... just works.

And for some reason, I kept wondering what’s happening under the hood. How does one person’s change mysteriously appear everywhere? How are conflicts handled? What happens if two people change the same thing at the same time?

I didn’t want the “high-level” answer. I wanted tofeelthe system. The same way buildingVeridianhelped me understand Git, I wanted to understand these real-time sync systems by building one myself.

So I builtConflux, a small real-time collaboration engine written in Rust. Not because the world needs another backend, but becauseIneeded to understand how these real-time systems actually sync state between multiple users without blowing up.

Turns out, it’s not some mysterious technology. It’s a bunch of simple ideas stacked cleanly.

### Why I Wanted to Build This

Whenever I saw people editing the same thing at once, my brain just assumed, “Okay, some mysterious library is doing something complicated.” But then I learned aboutCRDTs, and the whole idea clicked.

ACRDT (Conflict-free Replicated Data Type)is basically a data structure thatnever conflicts. Every update is mergeable. Everyone can edit freely without locking. And eventually, everything converges to the same state.

When I realized that, I wanted to see it for myself:

* What does a CRDT-based collaboration systemactuallylook like when you implement it?

### The "Real Stuff" Behind It: What is a CRDT?

Okay, let's break this down. The "Conflict-free" part is what matters.

The "Normal" Way (The Problem):

Imagine you and I are editing a text file.

1. We both download the file. It says:"Hello".
2. I change my copy to:"Hello world".
3. You, at theexact same time, change your copy to:"Hello there".
4. I upload my version. The server now has"Hello world".
5. You upload your version. The server now has"Hello there".

My change isgone. Forever. You overwrote me. This is aconflict. This is what version control systems like Git spend all their time trying to manage with "merge conflicts."

The "CRDT" Way (The Solution):

CRDTs don't work like that. They don't send thewhole fileback and forth. They sendinstructions.

1. We both have the state:"Hello".
2. I make a change. My local CRDT doesn't say "the new file is 'Hello world'". It generates aninstruction:(At position 5, add: " world").
3. You, at the same time, make a change. Your CRDT generates aninstruction:(At position 5, add: " there").
4. I send my instruction to the server.
5. You send your instruction to the server.

The server, and eventually all clients, getbothinstructions. The "aura" of the CRDT is that it has a mathematical rule for merging these instructions so thateveryone ends up with the exact same final state.

The final text might be"Hello world there"or"Hello there world". What's important is thatno data was lost, andwe both end up seeing the same thingwithout ever getting a "MERGE CONFLICT" error.

That's it. A CRDT is just a data structure with a "merge" algorithm so good that itneverconflicts.

### What Conflux Actually Does

Now that we know what a CRDT is, the whole system makes more sense.

Strip away the extra details, and Conflux does three simple things:

1. It maintainsrooms– like “documents” or “sessions.”
2. Each room contains aCRDT document– this stores the shared state.
3. Clients sendinstructions(updates), the server merges them, and it broadcasts them to everyone else.

Here’s that same loop, but now it makes sense:

You type something → your local CRDT generates aninstruction→ you send thatinstruction(the "update") to the server → the server merges it into its own CRDT → the server broadcasts thatinstructionto all other clients → their local CRDTs merge it → everyone's UI updates.

That’s it. That’s the entire loop. No fancy algorithm, no weird transformations, no branching timelines.

Just:update → merge → broadcast.

And because CRDTs are designed to merge cleanly, nothing conflicts.

### The Architecture (Simple Version)

To make it easier to understand, I drew it out:

Every box in this diagram has one job. No box is doing five things at once. And that simplicity is what made the whole system feel approachable.

### How the Server is Designed

The Conflux server has four main pieces, and each one does exactly one job.

#### 1. Room Manager

This is the part that keeps track of all active rooms.

If a room doesn’t exist, it creates it. If a room is idle for too long, it cleans it up.

Nothing fancy - just lifecycle management.

#### 2. Room (Actor Loop)

A room is basically its own mini-server.

It runs a loop that just listens for commands like:

* ApplyUpdate(This is our CRDTinstruction!)
* SetAwareness
* Chat
* Join
* Leave

...and it applies those updates to its own YDoc.

This “actor” design means each room is isolated, which avoids the usual shared-state chaos.

#### 3. WebSocket Server

This is the entry point.

It:

* Authenticates users using JWT.
* Extracts the room ID from the URL.
* Upgrades the connection to a WebSocket.
* Forwards incoming messages to the correct room.
* Forwards outgoing messages from the room back to the client.

It accepts two types of messages:

* Plain text:This becomes a chat message.
* JSON:This becomes a structured CRDT or awareness update.

This makes debugging easy because you can literally type chat messages from a terminal.

#### 4. JWT Authentication

Every login creates a new session ID (sid) inside the token.

This fixes the “everyone logs in with the same token” problem.When a client connects, the server knows:

* Which user
* Which session
* Which room

It’s simple, but it gives a clean identity model.

### The Sync Flow (Easy Explanation)

Let’s say two people are editing a shared document.

1. Person A edits something.Their local CRDT applies the change instantly and generates aninstruction.
2. A sends the instruction (the update) to the server.This is just a small binary chunk.
3. Server applies the instruction to its own CRDT.This keeps the server's copy of the document authoritative.
4. Server broadcasts the instruction.Allotherclients in that room receive the same update.
5. Each client applies it.Their local CRDT merges the instruction into whatever they already have.
6. Everyone stays in sync.Even if many people change the same thing at the same time, the CRDT handles the merges smoothly.

It sounds complicated, but seeing it work makes it feel simple.

### Why Awareness and Chat Matter

Real-time systems aren’t just about document content.

Users need to know:

* Who else is online
* Where their cursor is
* Who is typing
* Who joined or left

So I added “awareness events.” These are just tiny JSON messages that propagate instantly to show who's who and who's where.

Chat was simple - if the client sends normal text instead of JSON, the server treats it as a chat message and broadcasts it.

It's a small feature, but it makes the system feel alive.

### The Dashboard

I also built a small dashboard endpoint:

GET /dashboard

This returns:

* Room ID
* Number of connected clients
* Number of document updates
* Number of awareness events

It’s nothing fancy, but it’s incredibly useful toseethe system working.

### What I Learned From Building This

Just like Veridian made Git click for me, Conflux made real-time collaboration click.

Here are the things that stood out:

* Real-time sync is mostly aboutmessage ordering and broadcasting.
* CRDTs removelike 90%of the “conflict” problems.
* Actor-style rooms make concurrencysurprisingly clean.
* WebSockets areway easierto work with than I expected.
* Having a properidentity systemearly saves headaches later.
* Most “complex systems” are just achain of simple steps.

Before building Conflux, these systems felt like black boxes.

After building it, they feel like something I can understand - and even improve.

### Closing Thoughts

Conflux isn’t perfect. It’s probably missing features. It'sdefinitelynot production-ready. But it does exactly what I built it for and it helped me understand how real-time collaboration works under the hood.

If you’re curious about this stuff, try building a small version yourself.

You don’t need to recreate Google Docs. Even a tiny CRDT-based shared counter will teach you a lot.

You can check out Conflux here:https://github.com/Kayleexx/conflux

I’ll keep improving it, and I’ll probably write more about the deeper parts later.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
