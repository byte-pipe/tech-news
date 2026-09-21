---
title: i built a green blob that lives on my desktop. now it has feelings. - DEV Community
url: https://dev.to/mikachu/i-built-a-green-blob-that-lives-on-my-desktop-and-now-it-has-feelings-4pjd
site_name: devto
content_file: devto-i-built-a-green-blob-that-lives-on-my-desktop-now
fetched_at: '2026-09-21T16:50:07.799888'
original_url: https://dev.to/mikachu/i-built-a-green-blob-that-lives-on-my-desktop-and-now-it-has-feelings-4pjd
author: Mika Flowers
date: '2026-09-20'
description: 'A quick disclaimer before we dive in: when I say "feelings," I mean state machines, bond... Tagged with showdev, python, linux, opensource.'
tags: '#showdev, #python, #linux, #opensource'
---

Built natively with Python and GTK4

A quick disclaimer before we dive in: when I say "feelings," I mean state machines, bond progression, and interaction history — not an LLM. Mochi isn't running on any AI model, and there's no language model deciding how he reacts. Every "emotion" here is deterministic: state lifecycles, timers, and memory of past interactions, not inference. Just wanted to set that expectation up front. Carry on 🌱

I've been building a little green creature that lives on my Linux desktop.

His name is Mochi.version 0.01 of mochi. laughable i know, but he's so cute!

At first, the goal was honestly pretty simple: make blob move.

Then it became: make blob feel alive.

And apparently I've now reached: give blob a productivity system, emotional progression, snacks, and an alarming number of animations.

So... yeah. Mochi v0.3 happened. 🌱

## The original idea was much smaller

Mochi started as a pixel-art desktop companion for Linux.

Python. GTK4. PyGObject. Cairo.

No cloud service. No account. No giant Electron window hiding somewhere in the background. Just a little creature hanging out on your desktop.

The early versions focused mostly on making that basic illusion work. Mochi could idle, blink, walk around, sleep, react when you clicked him, notice when you were typing, and occasionally respond to what was happening on the desktop.

And honestly, getting even that working reliably taught me way more about desktop development than I expected. Because the moment your cute blob can walk, sleep, be picked up, react to input, display UI, and independently trigger animations, you've accidentally created a state-management problem.

A surprisingly adorable state-management problem.

But v0.3 made me rethink what Mochi actually was.

## I didn't want to build a Tamagotchi that makes you feel guilty

Once I started thinking about progression, the obvious direction was some kind of virtual-pet system.

Hunger. Health. Daily streaks. Meters slowly falling while you're away.

And I hated basically all of it.

I don't want opening my laptop after three difficult days to result in my desktop pet staring at me like:

mother. you have abandoned me. 😭

Software already asks enough from us. Mochi is supposed to make the desktop feel a little warmer, not become another notification demanding maintenance.

So the design rule for v0.3 became:

1. Care should create affection, not obligation.
2. Your bond with Mochi can grow. It doesn't decay because you went outside. There are no daily streaks. Mochi doesn't starve. Closing the application isn't a moral failure.
3. Progression exists mainly to unlock more personality, reactions, dialogue, animations, and tiny surprises.
That decision ended up shaping basically the entire release.

## Mochi has a bond system now

v0.3 introduces persistent bond progression.

The important word there is persistent. Mochi is slowly beginning to remember the relationship you've built with him instead of resetting emotionally every time the program starts.

Interactions can contribute to bond progress, and reaching new levels gives me somewhere to attach increasingly expressive behavior later.

Not stronger stats. Not "+5 Mochi damage."

Expression. Different reactions. Different little moments. More personality.

That feels much more appropriate for what this project is becoming.

And yes, there is a level-up animation. Because obviously there is. I have priorities.

## You can feed him

This might be one of those features that exists primarily because watching Mochi eat something made me happy. And I am completely okay with that.

Feeding is a small interaction rather than the foundation of some constantly draining hunger mechanic. That's an important distinction.

I want you to interact with Mochi because it's cute and you want to. Not because a progress bar has been weaponized against you.

That sounds like I'm dramatically overthinking feeding a green pixel blob. I probably am. But tiny design decisions like this completely change how software feels to live with.

## I built an entire emote catalogue

This has become one of my favorite parts of the project. Mochi has been accumulating reactions. A lot of reactions.

Instead of treating those animations as random disconnected GIFs, I've been working toward an actual catalogue and state system that lets Mochi use them coherently.

The hard part isn't drawing an animation. The hard part is answering questions like:

* What happens if Mochi wants to emote while he's walking?
* What if you pick him up halfway through?
* What if he's sleeping?
* What happens when the animation finishes?
* What if an old timer fires after his state has already changed?
That's where this cute desktop pet quietly turned into a real software architecture problem.

Mochi now has explicit behavior/state ownership so higher-priority interactions can interrupt lower-priority ambient behavior without a dozen timers fighting over the sprite.

Which is a very serious sentence about a creature shaped approximately like a gumdrop.

## Mochi is becoming aware of what I'm doing

This is the direction I'm probably most interested in long term. Mochi can react to broad desktop activity. If I'm spending time in a terminal, editor, browser, media app, or other recognized context, Mochi can behave differently.

But I've been deliberately strict about the privacy boundary.

Mochi does not need to know what I'm typing. He doesn't need every window title. He doesn't need filenames. He doesn't need a transcript of my desktop.

Instead, the system tries to reduce activity into tiny semantic signals. Something closer to:

terminal active
typing happening
media playing
user returned

Enter fullscreen mode

Exit fullscreen mode

instead of:

here is everything Mika is currently doing

I think that distinction is extremely important. A desktop companion should be able to feel aware without becoming desktop surveillance.

That principle is staying.

## Then I accidentally gave my desktop pet a Pomodoro timer

This is probably the feature that pushed Mochi furthest away from "desktop toy."

It's called Focus with Mochi. You can start a focus session, choose the focus and break lengths, select your rounds, enable gentle encouragement, and even use a rain soundscape.

While you work, Mochi works with you. Focus time contributes to your bond. Breaks don't. And — very intentionally — Mochi does not judge what you do during them.

I didn't want another hyper-optimized productivity system screaming about efficiency. The idea is much softer:

I'm working for a little while. Mochi is here too.

That's it. And weirdly, I like that much more.

## The difficult part wasn't adding features

The biggest lesson from v0.3 has been that adding another feature to Mochi isn't particularly difficult anymore. Making every feature coexist is.

* A focus session needs to survive interactions.
* Feeding shouldn't break the state machine.
* Dragging Mochi around shouldn't leave an invisible window behind.
* A nameplate shouldn't steal mouse input.
* Sleeping shouldn't be accidentally cancelled because a UI opened.
* An old callback shouldn't wake up three seconds later and overwrite the state you're currently in.
And because Mochi runs as an actual desktop surface on Linux, I also have to care about things like:

Wayland. XWayland. GTK lifecycle behavior. Window positioning. Multiple monitors. Negative monitor coordinates. Input grabs. GLib timers. Shutdown cleanup.

Things I absolutely did not picture myself thinking about when I originally drew a green blob.

That has probably been my favorite part of the project. Mochi keeps creating excuses for me to learn systems I wouldn't otherwise touch.

## And I still don't want Mochi to become annoying

There's a temptation with something like this to maximize activity. More reactions. More popups. More dialogue. More notifications. More stuff.

I'm trying to resist that.

A good ambient companion needs to know when to shut up. Sometimes Mochi notices something and reacts. Sometimes he doesn't. Sometimes he just sits there.

That silence is part of the personality.

The goal isn't:

LOOK HOW MANY FEATURES MY DESKTOP PET HAS.

It's:

huh. it kinda feels like this little thing lives here.

That's the bar I'm chasing.

## What's next

v0.3 has ended up being a much bigger architectural step than I originally expected.

The bond system gives Mochi memory. The interaction system gives that bond meaning. The growing emote library gives him more ways to express it. Context awareness connects him to the desktop. And Focus with Mochi is my first experiment in making the companion genuinely useful without turning him into another productivity dashboard.

There is still a lot I want to explore:

* More meaningful bond milestones
* More contextual reactions
* Tiny unlockable behaviors
* Better dialogue
* More polish
* Probably several bugs caused by GTK doing something I was absolutely positive GTK would not do
You know. Software development.

But I'm really happy with the direction.

Mochi started as: what if there was a little guy on my desktop?

v0.3 is starting to answer the much more interesting question: what would make me actually care that he's there?

🌱

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (19 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse