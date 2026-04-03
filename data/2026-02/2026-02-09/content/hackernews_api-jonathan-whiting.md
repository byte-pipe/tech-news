---
title: Jonathan Whiting
url: https://jonathanwhiting.com/writing/blog/games_in_c/
site_name: hackernews_api
content_file: hackernews_api-jonathan-whiting
fetched_at: '2026-02-09T06:00:17.047520'
original_url: https://jonathanwhiting.com/writing/blog/games_in_c/
author: valyala
date: '2026-02-08'
description: I write games in C (yes, C) (2016)
tags:
- hackernews
- trending
---

# Why I Write Games in C (yes, C)

I am an unusual beast. All my solo project games I've been making recently have
been written in 'vanilla' C. Nobody does this. So I think it might be
interesting to explain why I do.

Dry programming language opinions incoming,you have been warned.

## What I need from a language

There's some things which are non-negotiable. First of, it has to be reliable.
I can't afford to spend my time dealing with bugs I didn't cause myself.

A lot of my games were written for flash, and now flash is dying. I donotwant to spend my time porting old games to new platforms, I want to make new
games. I need a platform that I am confident will be around for a while.

Similarly I want to avoid tying myself to a particular OS, andideallyI'd
like to have the option of developing for consoles. So it's important that my
programming language is portable, and that it has good portable library
support.

## What I want from a language

The strongest thing on my desired, but notrequiredlist is simplicity. I
find looking up language features, and quirky 'clever' api's incredibly tiring.
The ideal language would be one I can memorize, and then never have to look
things up.

Dealing with bugs is huge creative drain. I want to produce less bugs, so I
want strict typing, strong warning messages and static code analysis. I want
bugs to be easier to find, so I want good debuggers and dynamic analysis.

I'm not interesting in high-def realism, but I do still care a bit about
performance. Having more cycles available broadens the palette of things you
can do. It's particularly interesting to explore what is possible with modern,
powerful computers if you aren't persuing fidelity.

Even more than that I care about the speed of the compiler. I am not a zen
master of focus, and waiting 10+ seconds is wasteful, yes, but more importantly
it breaks my flow. I flick over to Twitter and suddenly 5+ minutes are gone.

I am not an OOP convert. I've spent most of my professional life working
with classes and objects, but the more time I spend, the less I understand why
you'd want to combine code and data so rigidly. I want to handle data as data
and write the code that best fits a particular situation.

## The Alternatives

C++ is still the most common language for writing games, and not without
reason. I still do almost all of my contract work in it. I dislike it
intensely.

C++ covers my needs, but fails my wants badly. It is desperately complicated.
Despite decent tooling it's easy to create insidious bugs. It is also slow to
compile compared to C. It is high performance, and it offers features that C
doesn't have; but features I don't want, and at a great complexity cost.

C# and Java have similar issues. They are verbose and complex beasts, and I am
searching for a concise, simple creature. They both do a lot to railroad a
programmer into a strongly OOP style that I am opposed to. As per most higher
level languages they have a tendency to hide away complexity in a way that
doesn't actually prevent it from biting you.

I like Go a lot. In many ways it is C revisited, taking into account what has
be learnt in the long years since it was released. I would like to use it,
but there are big roadblocks that prevent me. The stop-the-world garbage
collection is a big pain for games, stopping the world is something you
can't really afford to do. The library support for games is quite
poor, and though you can wrap C libs without much trouble, doing so adds
a lot of busy work. It is niche enough that I worry a little about long term
relevance.

It would be nice to make things for the web, but it feels like a terrifyingly
fast moving enviroment. It is particularly scary with the death of flash.
I really dislike javascript, it is so loose that I marvel that people are
able to write big chunks of software in it. I have no interest in trying.

Haxe feels much more promising than most alternatives. If I do web stuff again
I'll be diving in here. There is some good library support. I am a little
concerned by its relative youth, will it last? I don't much have else to say
about it though, I've only dabbled with the surface.

Some people just say screw it, I'll write my own language, the language I want
to use. I admire this, and sometimes I toy with the idea of doing the same. It
feels like too much to throw away all existing library support, and taking
full responsibilty for future compatibility. It is also very difficult, and
when it comes down to it I would rather be making games than programming
languages.

## Why C isstillmy best fit

C is dangerous, but it is reliable. A very sharp knife that can cut fingers as
well as veg, but so simple it's not too hard to learn to use it carefully.

It is fast, and when it comes to compilation I can't think of anything faster.

It can be made to run on just about anything. Usually this is relatively easy.
It is hard to imagine a time when this won't be the case.

The library and tooling support is strong and ongoing.

I say this with some sadness, but it is still the language for me.

I absolutely DO NOT mean to say "hey, you should use C too". I full appeciate
preferences here are pretty specific and unusual. I have also already written
more 'vanilla' C code than most, and this certainly is part of my comfort.

So yeah, that's it :-)

Back to main site
