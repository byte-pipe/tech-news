---
title: The key to understanding “Dynamic Programming” is that it’s not referring to “computer programming” – Vidar's Blog
url: https://www.vidarholen.net/contents/blog/?p=1172
site_name: hackernews_api
fetched_at: '2025-07-22T04:06:49.634414'
original_url: https://www.vidarholen.net/contents/blog/?p=1172
author: r4um
date: '2025-07-18'
description: “Dynamic programming” is not referring to “computer programming”
tags:
- hackernews
- trending
---

When seeing the phrase “dynamic programming” in an algorithms class
or leetcode study guide, the first question people ask is “what does
‘dynamic’ mean in this context?”.

The key question is instead “what does ‘programming’ mean in this
context?”, because it does not mean “computer programming”.

Instead it refers to, as the Oxford English Dictionary puts it,

programming. n.

4. Planning carried out for purposes of control, management,
or administration.

So really, it’s closer to “TV programming” (as in creating a
schedule), than “computer programming” (as in writing software).

The term was coined in the 1950s at a time when civil engineers would
say they’re “programming a new office building” to mean they’re
“planning the order and timeline for each sub-step required to construct
a new office building”.

Ignoring a million details, the resulting plan (the “program”) would
be something like

1. Site preparation
2. Excavation
3. Foundation
4. Structural framework
5. Exterior
6. Roofing
7. Interior
8. Hvac/electrical/plumbing
9. Fixtures/furnishing
10. Final inspection

(Real engineers can rip this example to shreds in the comments of
whichever site they came from.)

The steps of the plan must necessarily be in dependency order,
because each step likely relies on previous steps be done. Electricians
will fail to complete their work if they arrive at the worksite while
the loggers are still clearing trees.

It shouldn’t need stating, but you wouldn’t pour three separate
concrete foundations if you have three steps that need a foundation.
You’d do it once so that it’s ready for anything that needs it. That’s
the point of ordering the steps.

Dynamic Programming in Computer Science similarly means “planning the
order of each sub-step required to solve the complete problem”.

When “programming”fibonacci(10), the “program” would be
something like (given that we already havefib(0)andfib(1)by definition):

1. fib(2)
2. fib(3)
3. fib(4)
4. fib(5)
5. fib(6)
6. fib(7)
7. fib(8)
8. fib(9)
9. fib(10)

The steps of the plan must necessarily be in dependency order,
because each step likely relies on previous steps to be done.fib(7)will not be able to get its work done iffib(5)orfib(6)are not ready.

It shouldn’t need stating, but you wouldn’t computefib(8)three separate times if you have three steps that
need it. You’d do it once so that it’s ready for anything that needs it.
That’s the point of ordering the steps.

This “program” could be planned top down, i.e. starting withfib(10)and determining that you first need to solvefib(9)andfib(8), and repeating the process
recursively.

It could also be planned bottom up, by noticing the pattern that
every fibonacci number will have to be computed in order anyways, so you
might as well start from0and work your way up.

Either way, the final plan is the same, and both are considered
Dynamic Programming.

So next time you see someone struggling to understand what could
possibly make Dynamic Programming “dynamic”, suggest they instead look
into what makes it “programming”.

The term “Dynamic Programming” was coined by Richard Bellman in the
1950s, long before anyone knew how confusing it would become. In his
autobiography, he describes how he ended up with this name:

The 1950s were not good years for mathematical research.

We had a very interesting gentleman in Washington named Wilson. He
was Secretary of Defense, and he actually had a pathological fear and
hatred of the word, research.

I’m not using the term lightly; I’m using it precisely. His face
would suffuse, he would turn red, and he would get violent if people
used the term, research, in his presence.

You can imagine how he felt, then, about the term, mathematical.

The RAND Corporation was employed by the Air Force, and the Air Force
had Wilson as its boss, essentially. Hence, I felt I had to do something
to shield Wilson and the Air Force from the fact that I was really doing
mathematics inside the RAND Corporation.

What title, what name, could I choose?

In the first place I was interested in planning, in decision making,
in thinking. But planning, is not a good word for various reasons. I
decided therefore to use the word, “programming”.

I wanted to get across the idea that this was dynamic, this was
multistage, this was time-varying I thought, lets kill two birds with
one stone. Lets take a word that has an absolutely precise meaning,
namely dynamic, in the classical physical sense. It also has a very
interesting property as an adjective, and that is its impossible to use
the word, dynamic, in a pejorative sense. Try thinking of some
combination that will possibly give it a pejorative meaning. It’s
impossible*.

Thus, I thought dynamic programming was a good name. It was something
not even a Congressman could object to. So I used it as an umbrella for
my activities.

*This Haskell fan’s contender is “dynamic typing” :P
