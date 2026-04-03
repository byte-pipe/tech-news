---
title: a grand vision for rust
url: https://blog.yoshuawuyts.com/a-grand-vision-for-rust/
site_name: hnrss
content_file: hnrss-a-grand-vision-for-rust
fetched_at: '2026-03-09T11:18:23.846260'
original_url: https://blog.yoshuawuyts.com/a-grand-vision-for-rust/
author: Yoshua Wuyts
date: '2026-03-05'
published_date: '2026-03-05'
description: My “grand vision” for Rust
tags:
- hackernews
- hnrss
---

# a grand vision for rust— 2026-03-05

1. effects
2. substructural types
3. refinement types
4. conclusion

I don’t think I’ve ever quite articulated my “grand vision” for Rust, despite
having written a fair bit about the language and its features. There is a lot I
could say here, but currently there are three directions of development which I
find particularly interesting:

1. Improving Rust’s support for effects
2. Improving Rust’s support for substructural rules
3. Adding support for refinement types in Rust

There are more things in the language to be excited about, but these three in
particular interest me. If you’ve followed my work in Rust even a little bit for
the past few years, this might provide some clarity about what exactly it is I’m
trying to work towards here.

## Effects

Rust has support forconst fnandasync fnon stable Rust. And on nightly it
also has support fortry fnandgen fn. These are often referred to as
“function colors”, but more formally they’re also known as “effect types” which
are part of a broader category of programming language research called
“type-and-effect systems”.

Dealing with only one or two effects is generallyfine. But the more effects
you add the more painful they become to work with. And from talking with people
who work on compilers, operating systems, VMs, and the like I believe that Rust
would benefit greatly from being able to provide more guarantees on functions
including:

* Functions which guarantee they do not unwind (absence of thepaniceffect)
* Functions which guarantee they terminate (absence of thediveffect)
* Functions which are guaranteed to be deterministic (absence of thendeteffect)
* Functions which are guaranteed to not call host APIs (absence of theioeffect)

That’s a lot of kinds of functions to introduce. But for the kinds of systems
that Rust wants to be used for all of these areincrediblyuseful. Which is
why I’m interested in adding the right abstractions that allow us to introduce
these kinds of functions in a way that feels good to use.

## Substructural types

Rust’s claim to fame is the introduction of the borrow checker, which statically
guarantees memory safety and without needing a garbage collector at runtime. In
formal terms, Rust’s type system is consideredaffine, which means that each
value must be usedat most once. And “use at most once” is exactly what’s
needed to guarantee the absence of bugs like “use after free”.

But there are type systems which can provide even more guarantees. One step
beyond “use at most once” is “use exactly once”. Types that provide that guarantee
are called “linear” and in addition to guaranteeing the absence of “use after
free” they can also guarantee the absence of memory leaks.

And one step even beyond linear types are “ordered types”. These types aren’t
just used exactly once, they’re used exactly once in the exact order they were
introduced. What that means in practice: these are types with a stable memory
address that will never be changed until they are dropped. Here they are, side-by-side:

Type
Usage
Guarantees

Affine types
at most once
No more “use after free”

Linear types
exactly once
No more memory leaks

Ordered types
exactly once, in-order
Stable memory locations

I won’t bore you with terms like “contraction” and “weakening” here. You should
readthe wikipedia
pageif you want to
learn more. But specifically for Rust: this is why we’ve been working on new
traits likeMoveandForget:

* !Forgetunlocks linear types
* !Moveunlocks ordered types1

1

Move unlocks ordered types in a way thatactually composeswith the rest of the language, unlikePin. To be fully ergonomic does however also depend onemplacement in the language, which I believe is best expressed as an effect.

## Refinement types

“Use after free” is more formally known as atemporal memory safety violation.
Its sibling is the “out of bounds error” which is also known as aspatial
memory safety violation(ref). In Rust
the borrow checker can entirely statically guarantee we never run into use after
free bugs. However if we want to relax those rules a little, we can opt-in to using types likeRcandArcwhich check those properties at runtime instead.

When it comes to out of bounds checks things are however a little different. The
default is typically to check bounds at runtime, which may sometimes be omitted
by the compiler - but only as an optimization. That means we’re trading away
runtime performance for memory safety.

But what if we could trade away compile time for memory safety instead? Type
systems which can attach additional guarantees to existing types are calledrefinement type systems. And for Rust we’re experimenting with an ultra-lightweight
version of this we’re callingpattern types.

Pattern types use Rust’s pattern syntax to annotate existing types. Take for
exampleNonZeroUsize: this has historically been backed by a ton of custom
compiler optimizations to enable the use of niches in layout. But with pattern
types we can get those same optimizations automatically byrefininingtheusizetype with a pattern:

type 
NonZeroUsize = 
usize
 is 
1
..;

// ^^^^^^ refinement using patterns

A closely related feature to pattern types areview types, which would enable the
compiler to consider disjoint patterns when reasoning about aliasing
(ref). These
are great because they would allow holding two mutable references to the same
type, as long as each reference doesn’t look at any of the other fields.

I see pattern types and view types as the way we can make Rust’s borrow checker storyeven better. Both by removing the fundamental tradeoff between runtime checks vs memory safety (pattern types). As well as making even more valid borrows expressible (view types).

## Conclusion

There are a lot of things in Rust to be excited about. I love the work that’s
happening in improving the formalisms in the language, improvements in the
compiler, and in the ecosystem. And there are many more language improvements in
the works which I haven’t mentioned but I’m excited for (I’m looking at you,
reflection).

But me personally? I want for Rust to become the safest darn production-grade
language in existence. Because though we’re not doing too bad, we’re no
Ada/SPARK yet. But also: working on features like these is what I find
interesting and exciting. It’s why I volunteer to work on Rust.

And while figuring out how to fundamentally improve Rust isn’t easy or quick. I
believe it is definitely possible, eventually worthwhile, and in my opinion:
a lot of fun!