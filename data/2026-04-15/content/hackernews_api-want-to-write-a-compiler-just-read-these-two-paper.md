---
title: Want to Write a Compiler? Just Read These Two Papers.
url: https://prog21.dadgum.com/30.html
site_name: hackernews_api
content_file: hackernews_api-want-to-write-a-compiler-just-read-these-two-paper
fetched_at: '2026-04-15T20:02:35.842225'
original_url: https://prog21.dadgum.com/30.html
author: downbad_
date: '2026-04-15'
description: Want to Write a Compiler? Just Read These Two Papers (2008)
tags:
- hackernews
- trending
---

programming in the
twenty-first century

It's not about technology for its own sake. It's about being able to implement your ideas.

# Want to Write a Compiler? Just Read These Two Papers.

Imagine you don't knowanythingabout programming, and you want learn how to do it. You take a look at Amazon.com, and there's a highly recommended set of books by Knute or something with a promising title,The Art of Computer Programming, so you buy them. Now imagine that it's more than just a poor choice, but thatallthe books on programming are at written at that level.

That's the situation with books about writing compilers.

It's not that they're bad books, they're just too broadly scoped, and the authors present so much information that it's hard to know where to begin. Some books are better than others, but there are still the thick chapters about converting regular expressions into executable state machines and different types of grammars and so on. After slogging through it all you will have undoubtedly expanded your knowledge, but you're no closer to actually writing a working compiler.

Not surprisingly, the opaqueness of these books has led to the myth that compilers are hard to write.

The best source for breaking this myth is Jack Crenshaw's series,Let's Build a Compiler!, which started in 1988. This is one of those gems of technical writing where what's assumed to be a complex topic ends up being suitable for a first year programming class. He focuses on compilers of the Turbo Pascal class: single pass, parsing and code generation are intermingled, and only the most basic of optimizations are applied to the resulting code. The original tutorials used Pascal as the implementation language, but there's a C version out there, too. If you're truly adventurous, Marcel Hendrix has done aForth translation(and as Forth is an interactive language, it's easier to experiment with and understand than the C or Pascal sources).

As good as it is, Crenshaw's series has one major omission: there's no internal representation of the program at all. That is, no abstract syntax tree. It is indeed possible to bypass this step if you're willing to give up flexibility, but the main reason it's not in the tutorials is because manipulating trees in Pascal is out of sync with the simplicity of the rest of the code he presents. If you're working in a higher level language--Python, Ruby, Erlang, Haskell, Lisp--then this worry goes away. It's trivially easy to create and manipulate tree-like representations of data. Indeed, this is what Lisp, Erlang, and Haskell were designed for.

That brings me toA Nanopass Framework for Compiler Education[PDF] by Sarkar, Waddell, and Dybvig. The details of this paper aren't quite as important as the general concept: a compiler is nothing more than a series of transformations of the internal representation of a program. The authors promote usingdozens or hundreds of compiler passes, each being as simple as possible. Don't combine transformations; keep them separate. The framework mentioned in the title is a way of specifying the inputs and outputs for each pass. The code is in Scheme, which is dynamically typed, so data is validated at runtime.

After writing a compiler or two, then go ahead and plunk down the cash for the infamousDragon Bookor one of the alternatives. Maybe. Or you might not need them at all.

permalinkJune 29, 2008

# previously

* A Spellchecker Used to Be a Major Feat of Software EngineeringCoding as PerformanceDon't Be Afraid of Special CasesPurely Functional Retrogames, Part 4Purely Functional Retrogames, Part 3
* Coding as PerformanceDon't Be Afraid of Special CasesPurely Functional Retrogames, Part 4Purely Functional Retrogames, Part 3
* Don't Be Afraid of Special CasesPurely Functional Retrogames, Part 4Purely Functional Retrogames, Part 3
* Purely Functional Retrogames, Part 4Purely Functional Retrogames, Part 3
* Purely Functional Retrogames, Part 3

# archives

twitter/mail

I'm James Hague, arecovering programmerwho has been designing video games since the 1980s.Programming Without Being Obsessed With ProgrammingandOrganizational Skills Beat Algorithmic Wizardryare good starting points. For the older stuff, try the2012 Retrospective.

Where arethe comments?
