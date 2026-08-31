---
title: I Tried to Beat Peter Norvig and Accidentally Became Ryan Gosling - DEV Community
url: https://dev.to/highflyer910/i-tried-to-beat-peter-norvig-and-accidentally-became-ryan-gosling-45b8
site_name: devto
content_file: devto-i-tried-to-beat-peter-norvig-and-accidentally-beca
fetched_at: '2026-08-31T17:51:28.858390'
original_url: https://dev.to/highflyer910/i-tried-to-beat-peter-norvig-and-accidentally-became-ryan-gosling-45b8
author: Thea
date: '2026-08-31'
description: 'A few days ago, I posted my submission for the DEV Frontend Challenge: Khachapuri made entirely with... Tagged with algorithms, python, adventofcode, programming.'
tags: '#algorithms, #python, #adventofcode, #programming'
---

A few days ago, I posted my submission for the DEV Frontend Challenge: Khachapuri made entirely with HTML and CSS. I was expecting comments about CSS, but instead someone showed up and invited me to a mysterious "Hero's Journey": Peter Norvig needed rescuing, and his wall-clock time was going to be my opponent.

Obviously, I accepted.

I followed the challenge to my GitHub repo, and that's where I discovered that, among other things, I had somehow become Ryan Gosling.

He'd looked at my bio, decided there was something hidden in there, added a space, capitalized two letters, and turned me into Ryan Gosling. 😄

And I knew this wasn't going to be a normal coding challenge.

## TL;DR

At this point, I had also figured out thatthe person behind the challengehad no intention of giving me just a programming puzzle. He was funny, unpredictable, and clearly having far too much fun building this whole thing. There were movie characters, cryptic clues, suspicious Georgian, perfectly timed GIFs, music, and references hidden inside references.

And the more I followed it, the more obvious it became how much thought had gone into the whole thing. The clues were clever, the references were ridiculous in the best possible way, and somehow he always seemed to know exactly when to drop something new, making me question everything again.😀

It felt less like someone had handed me a coding task and more like someone had built an adventure around one.

And I was already completely in.

## The Setup

The challenge went something like this: Peter Norvig (yes,thatPeter Norvig - Google, "the" AI textbook) had taken my mysterious challenger hostage. His code was hogging all the memory, keeping the CPU busy, and refusing to give him an answer.Even ThePrimeagen's (Netflix, Youtuber) Rust solution couldn't save it.

So naturally, the person he decided to call for help was me. Or Ryan Gosling. Or Jon Snow. I wasn't quite sure anymore.😃

Then I was informed that in Georgian, we have an ancient expression: არმატურის გოგონა, or "rebar girl." It describes a girl who finds herself up against all kinds of high-tech magic, grabs a huge piece of iron because that's what happens to be nearby, andgets to work.

But there was a small problem. This expression does not exist.😂

Nobody in Georgia says this. He made it up for me on the spot. The Georgian was actually correct, which made it even funnier. So I accepted my new identity and continued.

Then he told me he'd been sharing these challenges for two years, and nobody had solved one yet. Somehow, around 100 developers had already been involved along the way. That was kind of scary.🙈

But I had already accepted the challenge, and now I was way too curious to give up. So there was only one thing left to do: grab the imaginary steel pipe and try.

And from there, the references just kept coming:Ygritte.Jon Snow.Tenet.Sicario.Road signs.Birds.Videos that might have been clues, jokes, misdirection, or all three at once.Suspicious attention to Ygritte's eyebrow movement.And somehow, there was always an April Ludgate GIF for the occasion.The problem was, I had no idea which of these were actual hints and which were just jokes. So I started paying attention to everything.

## The Actual Puzzle

Behind all this craziness was a real problem:Advent of Code 2022, Day 5 - Supply Stacks.

You get a bunch of crates stacked on numbered piles and instructions likemove 4 from 2 to 1. You follow all the moves, then print the crate that ends up on top of each stack. Simple enough.

Except my original AoC input was perfectly normal. The input he gave me was not. 😃 It had roughly86,000 lines,30,000 move instructions, with some moves asking to move tens of thousands of crates at once. Add all those moves together, and you're looking at more than half a billion crate movements.Some instructions even tried to move more crates than the stack actually had.

At first I thought the Ygritte GIF was another "You know nothing, Jon Snow" joke. Nope. I was looking at the wrong thing. He wanted me to notice a very suspicious eyebrow movement.😆

Somehow, that eyebrow clue led straight to a discussion about technical bounds: the number of stacks was limited by the input format, but the move counts could get absurdly large. And as I would later find out, instructions moving more crates than a stack had were completely intentional.

Peter Norvig's Python solution and ThePrimeagen's Rust solution couldn't handle this input in a reasonable time. My job was simple: beat their wall-clock time.

I started in JavaScript and later ported my final solution to Python because, at around 5 am I suddenly realized that the repo where this challenge started was my Python LeetCode repo. 😁

We do not talk about that part.

## Attempt 1: Correct Answer, Terrible Speed

My first solution was pretty straightforward: I used arrays for the stacks, and instead of moving crates one by one, I grabbed the whole block with splice(), reversed it, and pushed it onto the destination stack.

And it worked.

The output produced a string of letters:JUAREZ

Suddenly, another reference -the Sicario scenemade sense.😊

I was pretty happy. I had the right answer, I had found the road to Juarez, and another piece of this ridiculous puzzle was solved.

There was just one problem:~7 seconds.

Correct answer, but terrible execution time. The mercenaries were still winning.😁

## Attempt 2: Stop copying, just point at things

My next idea was: what if I stopped moving the actual crate data?

Instead of copying crates around, I represented each stack using references like{array, start, end, reversed}that pointed back to the original data. A move would then rearrange those references instead of copying all the crates.

This brought the execution time down to~2 seconds.

Better, but still nowhere near good enough.

On this massive input, those ranges kept breaking into smaller and smaller pieces, so eventually I still had to iterate through a lot of them. I had made it faster, but I was still doing too much work.

And that was the real problem.

I had JUAREZ. I knew my logic worked. Now I had to figure out why something this simple was still taking seconds, and whether I actually needed to do all that work in the first place.

By then I was far too curious to stop.

## Turns Out Tenet Was Documentation

At this point, I had found JUAREZ, but the mercenaries were still destroying my performance. 🙈

And his answer was basically: I'd already solved it. My program was just doing more than it needed to. To finish faster, I hadto do less.The first thing he told me was to go back to the problem statement and ask a very literal question:What does it actually ask me to produce?Then he told me to close the IDE, step away from the computer, grab some colored pencils, and draw the crates.And right after that, he sent me a scene fromTenet, Clémence Poésy talking about entropy, time, and things moving backwards.Because of course he did. 😄At first my brain went:cool, another movie reference.

Then:wait.

Oh. Backwards. You bastard.

But the important part wasn't simply reversing my loop.

The puzzle never asks for the complete final state.It only asks for thetopcrate of each stack. That's it.So why was I spending all this time calculating where every single crate ended up?I didn't need the whole final state. I only needed to know:Where did each final top position come from?Instead of starting with the initial stacks and moving all the crates forward, I could start with each final top position and trace it backwards through the move history.

For each move, I only had to figure out what happened to the position I was tracking and keep tracing it backwards.

No crates need to move at all.

There was one more problem with this evil input. Some instructions asked to move more crates than the source stack actually contained. So before tracing backwards, I made one cheap forward pass that tracked only the sizes of the stacks.

No crate data. Just integers:

sizes
 
=
 
[
len
(
stack
)
 
for
 
stack
 
in
 
initial_stacks
]

moves
 
=
 
[]

for
 
count
,
 
src
,
 
dst
 
in
 
raw_moves
:

 
count
 
=
 
min
(
count
,
 
sizes
[
src
])

 
sizes
[
src
]
 
-=
 
count

 
sizes
[
dst
]
 
+=
 
count

 
moves
.
append
((
count
,
 
src
,
 
dst
))

Enter fullscreen mode

Exit fullscreen mode

That gave me the number of crates each move could actually move. Then I could trace each final top position backwards:

for
 
count
,
 
src
,
 
dst
 
in
 
reversed
(
moves
):

 
if
 
count
 
==
 
0
:

 
continue

 
if
 
curr_stack
 
==
 
dst
:

 
if
 
depth_from_top
 
<
 
count
:

 
curr_stack
 
=
 
src

 
depth_from_top
 
=
 
count
 
-
 
1
 
-
 
depth_from_top

 
else
:

 
depth_from_top
 
-=
 
count

 
elif
 
curr_stack
 
==
 
src
:

 
depth_from_top
 
+=
 
count

Enter fullscreen mode

Exit fullscreen mode

curr_stacktells me which stack the position belonged to at that point.depth_from_toptells me how far it was from the top.

That's all I need to carry backwards. And this is where those ridiculous move sizes stop being scary.

Compare:

move 4 from 2 to 1

with:

move 101198 from 2 to 6

If I'm actually moving crates, the second one looks horrible.

But my backwards solution doesn't iterate through those 101198 crates. It only asks where the position I'm tracking sits relative to that moved block.So whether the command says4or101198, I'm still doing a small, constant amount of work for that tracked position. And there are only a handful of final positions I care about because I only need the top crate from each stack.

So backward tracing is:O(stacks × moves).

It depends on the number of stacks and move instructions, not on the total number of crates those instructions ask me to move.

And then I ran it.

~89msin JavaScript, down from~7 seconds.

The steel pipe had done its job. ⚔️Later I ported the same solution to Python, where it usually ran somewhere around100–200mson my machine.

And that was it.

I hadn't found a faster way to simulate half a billion crate movements.I just stopped simulating them.I had spent hours trying to figure out how to move the crates faster. The answer was to stop moving them.

## What I Actually Learned

The obvious lesson is to avoid unnecessary work. When optimizing code, it's easy to ask:How can I make this operation faster?But sometimes the better question is:Do I need to perform this operation at all?My first two attempts were fighting to move crates more efficiently. The final solution came from realizing I didn't need to move them in the first place.

But I learned something else too:

I had forgotten how much I missed a real challenge.

Especially in this AI era, when sitting there for hours fighting with your own code can almost feel like the weird way to do things, I had forgotten how much fun that struggle could actually be.

I liked not knowing where this was going. I liked getting stuck, thinking I had figured something out, finding another clue, going back again, and refusing to leave those stupid boxes alone until I understood what I was missing.

And yes, at times I really wasn't sure I could solve it. That whole "two years" and "around 100 developers" thing was still somewhere in the back of my mind. 😄

But somewhere between coding at 2 am, trying to understand what Clémence Poésy was telling me, fighting Peter Norvig's wall clock, following Ygritte's eyebrows, and somehow becoming Ryan Gosling, programming became ridiculously fun again.

I had missed that. That's probably my favorite thing I got out of this whole adventure.

I started by asking how to move the crates faster.

I finished by realizing I didn't need to move them at all.

Not bad for something that started under a CSS khachapuri.

I regret nothing. ⚔️

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse