---
title: Backtrack-free cursive
url: https://mmapped.blog/posts/52-backtrack-free-cursive
site_name: hnrss
content_file: hnrss-backtrack-free-cursive
fetched_at: '2026-07-13T19:33:02.428306'
original_url: https://mmapped.blog/posts/52-backtrack-free-cursive
author: Roman Kashitsyn
date: '2026-07-13'
description: Making English more enjoyable to write.
tags:
- hackernews
- hnrss
---

# Backtrack-free cursive

✑
2026-07-12
penmanship

* The crime
* The redemption

I love writing in cursive,
shaping each word in one long stroke.
If you grew up learning the Latin alphabet,
you likely don’t realize how much joy it sucks out of cursive writing.
I noticed only because I learned the Cyrillic alphabet first.
I think and write primarily in English,
yet Russian feels more enjoyable to write.

## The crime

I narrowed the problem to backtracking—the need to add strokes
to the letters I’ve partially written.
English wants me to dot my i’s and cross my t’s.
It has a lot of them,
and they like to cluster in a single word.
Instead of thinking about what I want to write next,
I have to maintain a mental queue of pending strokes.

Backtracking is rare in Russian.
Onlyй(short i)
andэ(pronounced like e inend)
require two strokes.
There is alsoё(pronouncedyo, like in New York),
but its umlaut is optional.
So much of Russian literature is written without ё
that native speakers infer it unconsciously.

⊕

 The word 
destination
 requires four backtracks (two t’s and two i’s) when written in English.
 Its Russian translation 
назначение
 needs none.

To quantify my discomfort,
I analyzed Dostoevsky’sCrime and Punishmentin Russian and English
and computed how much backtracking I would have to do
if I were to write it in cursive.
The English version needs backtracking for 51% of words
with 0.68 backtracks per word on average.
In Russian, only 6.4% of words need backtracks,
with 0.066 backtracks per word on average.

One way to remove backtracking is to lift the pen immediately
instead of waiting until the end of the word,
as if doing italic calligraphy.
Pen lifts alleviate the mental queue problem
and give a chance to readjust the palm,
but they break the writing flow.

Dots and crosses are even more irritating on digital notebooks
because the undo feature works on the stroke level.
Often, I want to remove the last word I’ve written.
If each word required only one stroke to write,
I could do it in a single tap.
But since every other word requires multiple strokes,
I resort to the eraser tool,
which is slower and more distracting.

## The redemption

I couldn’t find a cursive script that would address my annoyances,
so I designed one.
It’s based onSmithHand,
with occasional borrowings from the Russian script I learned at school.
SmithHand renders most lowercase letters in one stroke,
exceptx,t,i, andj.

xis the easiest letter to fix.
Instead of using two diagonal strokes,
I draw two mirroredc’s,
as my Russian penmanship teacher would suggest.

The fix fortis also straightforward.
Instead of crossing the vertical line in a separate stroke,
I add an auxiliary line that moves the pen up and left
and then crosses the stem.
It’s the same motion you’d use to draw digit 4,
but mirrored both horizontally and vertically.

This variant oftoften appears on logos.
I counted three instances just walking around Zürich main station.
For example, logos ofStocker bakery,Leonardo ice cream parlor,
and theHotelplan groupuse it.
If it reads well on Swiss logos,
it’s good enough for my scribbles.

⊕

 Single-stroke letter 
t
 often appears on logos.

If you’re feeling fancy,
you can make a loop on the upstroke,
giving the letter a little bow.
I prefer this variation in thethandteligatures
because it pairs well with its neighbors.

⊕

 Word 
theater
 written in a single stroke.

Thettligature requires planning:
draw two vertical stems first,
then add a horizontal stroke crossing them both.

⊕

 Word 
pretty
 written in a single stroke.

iandjgave me a hard time.
I tried skipping their dots entirely,
but the result was subpar.
I tried writing the dot before the stem,
trading a backtrack for a pen lift,
but I couldn’t get used to it.
It also broke the flow,
unless the word started with a dotted letter (as ininorjust).
An acceptable solution must connect the dot and the stem in a legible way.

The breakthrough came from my prior experiments with dot shapes.
I write with an extra-fine nib,
so dots can disappear in a dense grid packed with letters.
I considered using little circles instead.
The change didn’t seem worth the trouble on its own,
but the pen lift constraint gave the idea a new appeal:
dots become invisible when connected to a stem,
but circles remain distinctive.

The design that worked fuses the circle and the stem.
To write aniwithout lifting a pen,
I draw a tight loopabovethemidlinethat flows into a stem on the downstroke.

The placement and the alignment of the circle are crucial.
If the circle is below the midline,
the letter looks like a Greekε.
If the circle doesn’t align with the stem,
the letter looks like anr.

⊕

 The circle above the letter 
i

 must be above the midline
 and align with the stem;
 otherwise, the letter is easy to confuse with
 
ε
 or 
r
.

Wordjitteris perfect for practicing the script
because it containsi,j,
and a challengingtteligature.

⊕

 Word 
jitter
 written in a single stroke.

Some capitals required minor adjustments.
The horizontal bar of capitalTturned into a loop.
CapitalFacquired a little bow that connects to the next letter.
CapitalKhas two renderings:
in two top-down strokes (requires a pen lift)
or in one stroke that traverses the top arm twice
(once up and once down).

Here is the full alphabet for reference:

⊕

 Backtrack-free cursive Latin alphabet.

I’ve been using this script for several months,
both on paper and digital notebooks.
Myi’s are still inconsistent,
myt’s andx’s
aren’t as elegant as they used to be,
but writing English finally brings me as much delight as writing Russian.

⊕

 Words 
delightful
 and 
destination
,
 each written in a single stroke.