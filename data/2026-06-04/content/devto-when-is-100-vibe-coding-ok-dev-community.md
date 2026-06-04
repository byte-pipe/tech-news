---
title: When Is 100% Vibe Coding OK ? - DEV Community
url: https://dev.to/realvorl/when-is-100-vibe-coding-ok--38p
site_name: devto
content_file: devto-when-is-100-vibe-coding-ok-dev-community
fetched_at: '2026-06-04T12:02:23.538326'
original_url: https://dev.to/realvorl/when-is-100-vibe-coding-ok--38p
author: Viorel PETCU
date: '2026-05-31'
description: Recently, I lost a lot of time reviewing and would have lost even more implementing, what I can only... Tagged with ai, go, cschallenge, productivity.
tags: '#ai, #go, #cschallenge, #productivity'
---

Brute-forcing a wooden puzzle via AI

Recently, I lost a lot of time reviewing and would have lost even more implementing, what I can only describe asvibe-writtenspecs.

Requirements thatfeltcoherent while saying almost nothing concrete. The kind of document where every paragraph sounds reasonable until you scratch the surface a bit and realize the thing is not applicable in the existing ecosystem.

To be clear: I am not againstvibe coding.

I use it myself all the time.

If I need:

* a one-off script,
* a throwaway visualization,
* a temporary parser,
* a document nobody else will maintain,

then speed matters more than rigor.

But maintenance changes the equation completely.

This weekend accidentally gave me a good example of wherevibe codingactually shines. During my usual Saturday clean-up, I knocked over one of those wooden cube puzzles:

25 identical pentacubes that are supposed to fill a perfect5×5×5cube.

Specifically this one:

I tried reconstructing it manually for a while and failed (blaming the fact that I was tired and there washeat domeover EUROPE messing with the comfort index🥵 )

Needless to say this really bugged the engineer in me and on Sunday morning I was ready to throw AI at this. I realized that:

* the rules are precise,
* the state space is finite,
* the problem is absolutely solvable,
* and computers are very good at brute force.

So I opened Go and startedvibe coding.

The single piece shape is simple:

A planar pentacube of which there are 25 instances.

At first the challenge was not the algorithm. It was the representation or the domain specific language (DSL).

Even explaining the puzzle toChatGPTtook multiple iterations. We had to establish:

* coordinate conventions,
* slice notation,
* legal piece states,
* rotation semantics,
* and eventually a labeling system for pieces.

Once the model stabilized, the rest followed naturally:

* generate transformations,
* normalize orientations,
* recursively place pieces,
* backtrack on collision.

Classic brute force.

I fully expected to need serious optimization eventually:

* pruning,
* bitboards,
* placement precomputation,
* maybe even Algorithm X.

But modern hardware is absurdly efficient.

Thenaive recursive solverfound solutions fast enough that optimization stopped being necessary and became optional engineering curiosity instead.

Somewhere in the middle of this, the project accidentally became a generic mono-pentacube solver.

computing unique orientations 
for 
default piece...
unique orientations: 24
solution found

z 
=
 0
1 1 1 1 2 
3 1 4 2 2 
3 3 5 6 2 
3 7 8 9 2 
3 8 8 8 8 

z 
=
 1
A B C D E 
A 4 4 4 4 
A A 5 6 6 
A 7 F 9 9 
G H H H H 

z 
=
 2
I B C D E 
I I C D J 
I 5 5 6 J 
I 7 F 9 J 
G 7 F H J 

z 
=
 3
B B C D E 
K K K K E 
L M 5 6 J 
G 7 F 9 N 
G O O O O 

z 
=
 4
L B C D E 
L M K P N 
L M P P N 
L M F P N 
G M O P N 

Enter fullscreen mode

Exit fullscreen mode

Then I wantedvisual output.

So we addedOBJ/MTLexport and grouped the generated geometry by piece so the solutions could be inspected directly in Blender.

At that point I left the chat entirely, opened Codex, cleaned the implementation up, packaged it properly, and turned it into something reusable for solving this entire family of problems.

Solution

Exploded View

Not bad for roughly two hours ofvibe coding.

But I think the important part is this:

My attempt only worked becauseI already knewthe problem itself wassolvable.

That certainty let me push through:

* incorrect assumptions,
* hallucinated constraints,
* broken code generation,
* malformed OBJ output,
* and multiple rounds ofChatGPTconfidently misunderstandingthe puzzle.

That is where I thinkvibe codinggenuinely works well:

When the human already owns the invariants.

If you know:

* the problem is solvable,
* the constraints are real,
* and the output is verifiable,

then AI becomes an accelerator andvibe codingis100% OKin my book.

But if the requirements themselves are "vibes", then the system has nothing solid to converge toward.

You do not get speed.

You get, well, nonsense.

PS:

should you knock over your puzzle, or ever need to fill a 5x5x5 cube with a planar pentacube, while also needing to visualise the solution...I got you:vibe codedgoimplementation

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse