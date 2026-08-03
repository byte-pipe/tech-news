---
title: rust-project-goals/src/2026/move-trait.md at main · rust-lang/rust-project-goals · GitHub
url: https://github.com/rust-lang/rust-project-goals/blob/main/src/2026/move-trait.md
site_name: hackernews_api
content_file: hackernews_api-rust-project-goalssrc2026move-traitmd-at-main-rust
fetched_at: '2026-08-04T06:00:19.760798'
original_url: https://github.com/rust-lang/rust-project-goals/blob/main/src/2026/move-trait.md
author: paavohtl
date: '2026-08-03'
description: Rust Project Goals tracker. Contribute to rust-lang/rust-project-goals development by creating an account on GitHub.
tags:
- hackernews
- trending
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 rust-lang

 

/

rust-project-goals

Public

* NotificationsYou must be signed in to change notification settings
* Fork114
* Star159

 
 
 
 
 

## FilesExpand file tree

main
/

# move-trait.md

Copy path
Blame
More file actions
Blame
More file actions
 

## Latest commit

 

## History

History
History
134 lines (90 loc) · 11.4 KB
main
/

# move-trait.md

Copy path
Top

## File metadata and controls

* Preview
* Code
* Blame
134 lines (90 loc) · 11.4 KB
Raw
Copy raw file
Download raw file
Outline
Edit and raw actions

# Immobile types and guaranteed destructors

Metadata

Point of contact

@lcnr

Status

Accepted

What and why

Let types opt out of being moved or forgotten, enabling scoped spawn, async drop, and pin-by-default

Timespan

2026-2027

Roadmap

Just add async

Roadmap

Rust for Linux

Tracking issue

[
#635
]

Other tracking issues

[
rust-lang/rust#149607
]

Zulip channel

#t-lang/move-trait

[types] champion

@lcnr

[lang] champion

@jackh726

## Summary

We propose to introduce new traits that describe what operations are possible on a type. Today Rust assumes all types can be moved (relocated in memory) and forgotten (viamem::forget). We will introduce traits likeMoveandForgetthat make these capabilities explicit, allowing types to opt out. This follows the precedent set by theSized hierarchy work, which relaxes the assumption that all types have a compile-time-known size. We will implement MVPs in the compiler, write RFCs, and validate viability through real-world testing in the Linux Kernel.

## Motivation

### The status quo

Rust has historically assumed that all values can be moved (relocated in memory) and forgotten (viamem::forget, without running destructors). These assumptions are baked into the language: assignment moves values, andmem::forgetis safe. But some types need to opt out of these capabilities:

Immobile types:A lot of async futures want to be self-referential, but self-referential types can't be safely moved. The current solution isPin, which encodes immovability as a property ofplacesrather thantypes. This leads to significant complexity. AsThe Safe Pinned Initialization Problemdescribes,Pinstruggles to safely encode self-referential types in systems like the Linux kernel.

Guaranteed destructors:Some types need their destructors to run. ATransactiontype might requirecommit()orrollback()before cleanup. A scoped task handle must join before the scope exits. Butmem::forgetis safe, so Rust can't guarantee destructors run. This blocks patterns like safe scoped spawn for async, where the spawned task borrows from the parent scope.

### What we propose to do about it

We propose to generalize Rust's type system with new auto-traits that describe what operations are possible on a type. The framing is positive: traits represent capabilities. At the base layer, types may have no special capabilities. We then layer on the things we need:

* Move: The type can be relocated in memory.
* Destruct: The type can be implicitly dropped (destructor runs when it goes out of scope).
* Forget: The type can be forgotten viamem::forgetwithout running its destructor.

This follows the precedent set by theSized hierarchywork. Just as that work relaxes "all types have compile-time-known size" to support scalable vectors, this work relaxes "all types can be moved" and "all types can be forgotten."

TheMovetraitencodes movability as a property of types rather than places:

#
[
lang = 
"move"
]

unsafe
 auto 
trait
 
Move
 
{
}

Types implementing!Movecannot be moved and must keep a stable address for their entire existence. This is simpler thanPinbecause immovability is a type property, not a place property. Construction of!Movetypes will rely on work from#t-lang/in-place-init.

TheForgettraitlets types opt out of being forgettable:

// Types implementing !Forget must have their destructors run

unsafe
 
impl
 !
Forget
 
for
 
ScopedTaskHandle
 
{
}

With!Forget, we could build safe scoped spawn: the handle's destructor joins the task, and because the handle can't be forgotten, the join is guaranteed. This unblocks patterns that are currently impossible in safe Rust.

### Work items over the next year

#### Movetrait

Let types opt out of being relocated in memory, encoding immovability as a type property rather than a place property.

Task

Owner(s)

Notes

Compiler implementation for 
Move

@lcnr and @nia-e

Write the 
Move
 RFC

@yoshuawuyts

Test in Linux kernel

@BennoLossin

RfL is an important Rust user which uses a lot of self-referential data structures.

Test interactions between 
Iterator
 and 
!Move

@yoshuawuyts

It's important to prove that generator-based effects can be desugared to 
impl Trait + !Move
 so they can support self-references.

#### Guaranteed destructors

Explore letting types opt out ofmem::forget, enabling patterns like safe scoped spawn for async.

Task

Owner(s)

Notes

Design exploration for guaranteed destructors

@nikomatsakis

Explore trait hierarchy options and interaction with existing features

What is concretely out of scope for this year is anything related to changing or
updating theFuturetrait. This is the only stable trait in Rust which depends
onPin, and would need a migration story to be able to useMove. However depending onPinis not the only shortcomingFuturehas (1+2+ 10 more issues), and so fixing theFuturetrait is best treated as a standalone project.

## Team asks

Team

Support level

Notes

[lang]

Large

Design session needed to work through design

[types]

Large

Involved in implementation + review

## Frequently asked questions

### How does this relate to the Sized hierarchy work?

TheSized hierarchywork establishes the pattern: Rust can relax assumptions that were previously universal by introducing trait hierarchies that let types opt out. That work relaxes "all types have compile-time-known size" to support scalable vectors and extern types. This goal applies the same pattern to "all types can be moved" and "all types can be forgotten."

### How does this relate to the "pin ergonomics" initiative?

This work is an alternative toProject Goal 2025H2: Continue Experimentation with Pin Ergonomics, which includes the following extensions:

* A new item familypinin lvalues, e.g.&pin x,&pin mut x,&pin const x.
* A one-off overload of Rust'sDroptrait, e.g.fn drop(&pin mut self).
* A new item kindpinin patterns, e.g.&pin <pat>.

Notably this work does not solvepin's duplicate definition
problem, meaning that even with these extentions we still end up withTraitandPinnedTraitvariants of existing
traits. TheDroptrait being the exception to this, since the initiative is proposing to special-case it using a one-off overload.

Rather than trying to change the language to makePinwork, we believe the
problem is withPinand we should improve the way immovable types are encoded
in Rust instead. With the eventual goal to deprecatePinin Rust entirely.

Because Rust promises to stay backwards-compatible forever, makingpina
language-item on par with&andmutis something we'll forever need to keep
supporting. Given our eventual goal is to deprecatePin, we do not believe
that we should makepina part of the language. Which is whyMoveis not just a complimentary proposal, but intended as an alternative.

### What enables safe scoped spawn?

Safe scoped spawn requires guaranteed destructors. The pattern: spawn returns a handle whose destructor joins the task. If you couldmem::forgetthe handle, the task could outlive the scope and access dangling references. With!Forget, the handle's destructor is guaranteed to run, making the pattern safe. This is one of the key motivations for the guaranteed destructors portion of this goal.

### Where can I read more about this design space?

Several blog posts explore this area:

* Move, Destruct, Leakexplores the trait hierarchy for destructors and forgetting. Note that unlike this post, we don't believeMoveshould be a supertrait ofDestruct. It's useful to have types that can be destructed/dropped but not moved (e.g., self-referential types that need cleanup).
* Must move typesintroduces the concept of types that force callers to take specific actions.
* Ergonomic Self-Referential Types for Rustandits follow-upexplore theMovetrait design.
* Why Pin is a part of trait signaturesexplains the problems withPinthat motivate this work.
* Placing functionsproposes syntax for constructing!Movetypes in place.