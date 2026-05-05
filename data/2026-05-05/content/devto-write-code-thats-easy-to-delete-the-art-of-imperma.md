---
title: 'Write Code That''s Easy to Delete: The Art of Impermanent Software - DEV Community'
url: https://dev.to/adamthedeveloper/write-code-thats-easy-to-delete-the-art-of-impermanent-software-19l1
site_name: devto
content_file: devto-write-code-thats-easy-to-delete-the-art-of-imperma
fetched_at: '2026-05-05T11:59:37.720719'
original_url: https://dev.to/adamthedeveloper/write-code-thats-easy-to-delete-the-art-of-impermanent-software-19l1
author: Adam - The Developer
date: '2026-05-02'
description: We obsess over making code last. Maybe we should obsess over making it leave gracefully. There's... Tagged with programming, webdev, productivity, architecture.
tags: '#programming, #webdev, #productivity, #architecture'
---

Designing for reversibility via modularity

We obsess over making code last. Maybe we should obsess over making it leave gracefully.

There's a quote that's been living rent-free in my head for years:

"Write code that is easy to delete, not easy to extend."— Tef,programming is terrible

The first time I read it, I pushed back. Isn't the whole point to write code thatsurvives? That scales? That you can build on top of?

Then I spent a weekend trying to rip out a logging library from a three-year-old codebase. It had quietly spread into 40 files. Removing it felt like surgery on a patient who had grown bones around a sponge.

## The Lie We Tell Ourselves

When we write code, we tell ourselves a flattering story:this will be here in five years, so I should make it robust, reusable, and extensible.

But the data doesn't support this story. Most features get changed within months. Many get cut entirely. The average production codebase has entire directories that haven't been touched in years — not because they're perfect, but because everyone is too afraid to delete them.

We write code as if it's load-bearing. Usually, it isn't.

The irony is that the more we try to make code "permanent" — wrapping it in abstractions, coupling it into shared utilities, weaving it through the system, theharderit becomes to change. We've traded adaptability for the illusion of durability.

## What "Easy to Delete" Actually Means

It doesn't mean write throwaway code. It doesn't mean skip tests or ignore structure.

It means:design for reversibility.

When you write a feature, ask yourself:if this needed to go away tomorrow, what would that look like?

If the answer is "a 400-line PR touching 20 files," something went wrong at the design stage — not the deletion stage.

Easy-to-delete code tends to share a few traits:

### 1. It lives in one place

Duplication gets a bad reputation. The DRY principle is good advice, but taken to its extreme, it creates code that's deeply entangled. When the same function is reused in eight different contexts, you can't change it for one context without worrying about all the others.

Sometimes, a little duplication is the price of independence. Two modules that both have aformatDatefunction can each evolve or disappear without consequences.

### 2. It has a clear boundary

The hardest code to delete is the code that has leaked everywhere. The database client that got imported into UI components. The config object that got passed twelve layers deep. The utility function that became load-bearing infrastructure.

Boundaries are what make deletion safe. An isolated module, a clean interface, a service behind a well-defined API... these are things you can remove, replace, or rewrite without holding or thinking through your breath.

### 3. It doesn't know too much

Code that's easy to delete tends to be ignorant but in the best way. It doesn't know about the rest of the system. It takes inputs, does its job, returns outputs. It doesn't reach out and grab global state. It doesn't mutate things it didn't create.

Ignorant code is also testable code, which is no coincidence ( I actually didn't wanna add this part for some personal reasons )

### 4. It's hidden behind a seam

Feature flags. Adapter layers. Interface abstractions. These aren't just engineering formalism — they're deletion handles. A feature behind a flag can be switched off in seconds. Code behind an interface can be swapped without the callers noticing.

The strangler fig pattern exists precisely for this reason: wrap the old thing, build the new thing alongside it, then delete the old thing once it's isolated. The seam is what makes that possible.

## A Different Way to Think About Abstraction

We often reach for abstraction to avoid repetition. But the best reason to abstract something is toisolateit or to give it a name and a box so that you can change or remove it without touching everything else.

Think about logging. You could scatterconsole.logcalls everywhere. That's easy to write and immediately painful to change. Or you could route all logging through a singleloggermodule. Now if you want to swap logging libraries, or add context, or silence it entirely — you only touch one file. ONE.

The abstraction isn't there because logging is complex. It's there because logging is a thing that mightchange or disappear, and you want that to be painless.

Abstract at the seams, not in the middle.

## Deletability as a Code Review Lens

Here's something I've started doing in code review: asking not just "does this work?" but "what would it take to remove this?"

It reframes things in a useful way.

A PR that adds a new feature and touches 15 files is a warning sign — not necessarily because it's wrong, but because it's announcing a high cost of future change. A PR that adds the same feature through a single, well-bounded module is leaving a cleaner footprint.

You can extend this to architecture decisions. Before adding a new dependency, ask: "what does removing this look like in two years?" Some dependencies are fine because they're small, stable, or isolated. Others are like introducing an invasive species. They grow into everything and become impossible to root out.

## Impermanence Is Not Defeatism

There's a Zen concept sometimes translated asimpermanence— the idea that things arise, exist for a time, and pass away. This isn't pessimism. It's just an accurate description of how things work.

Software is the same. Features come and go. Products pivot. Requirements change. The code you're writing today will be partially or wholly replaced. That's not failure — that's how living software works.

Writing for impermanence means accepting this, and designing accordingly. It means your goal isn't to write code that can never be removed. It's to write code whose removal ischeap.

The engineers who built systems that are still running 30 years later didn't achieve that by making the code impossible to touch. They achieved it by writing code that was easy to reason about, easy to isolate, and when the time came, it's easy to replace piece by piece.

## In Practice: A Checklist

Before you commit something, it's worth a quick gut-check:

* Could I delete this feature with a single PR?If not, why not?
* How many files does this touch?More isn't always worse, but it should feel intentional.
* Is this module aware of things it shouldn't be?Imports, globals, side effects.
* If this dependency disappeared tomorrow, how bad would it be?Could you swap it in an afternoon?
* Is this abstraction making things easier to change, or just avoiding repetition?

None of this means paralysis. You don't need to design every microservice like it might vanish. But developing an instinct for deletion cost with the same way you develop an instinct for performance or readability, it'll quietly make your codebases healthier.

## The Code You Don't Have to Write

There's a final point worth making: the easiest code to delete is the code you never write.

Every feature is a liability. Every abstraction is a maintenance surface. Every dependency is a relationship you're now in. The code that doesn't exist has no bugs, no coupling, no deletion cost.

This doesn't mean build nothing. It means be deliberate. When you feel the urge to add a new layer of abstraction, to generalize something that's only been used once, to build for a use case that might never arrive... pause.

Maybe the right move is to wait. To write the minimal thing. To leave room for deletion.

Because software that can change easily is software that can survive. And the secret to changeability isn't clever architecture or brilliant abstractions.

It's knowing that what you built today can be gracefully taken apart tomorrow.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (46 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse