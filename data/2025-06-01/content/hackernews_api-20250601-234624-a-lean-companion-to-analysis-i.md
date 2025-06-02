---
title: A Lean companion to “Analysis I”
url: |
  https://terrytao.wordpress.com/2025/05/31/a-lean-companion-to-analysis-i/
site_name: hackernews_api
fetched_at: |
  2025-06-01T23:46:24.523609
original_url: |
  https://terrytao.wordpress.com/2025/05/31/a-lean-companion-to-analysis-i/
author: jeremyscanvic
date: 2025-06-01
description: Almost 20 years ago, I wrote a textbook in real analysis called “Analysis I”. It was intended to complement the many good available analysis textbooks out there by focusing more on foun…
tags:
  - hackernews
  - trending
---



Almost 20 years ago, I wrote a textbook in real analysis called “Analysis I“. It was intended to complement the many good available analysis textbooks out there by focusing more on foundational issues, such as the construction of the natural numbers, integers, rational numbers, and reals, as well as providing enough set theory and logic to allow students to develop proofs at high levels of rigor.

While some proof assistants such as Coq or Agda were well established when the book was written, formal verification was not on my radar at the time. However, now that I have had some experience with this subject, I realize that the content of this book is in fact very compatible with such proof assistants; in particular, the ‘naive type theory’ that I was implicitly using to do things like construct the standard number systems, dovetails well with the dependent type theory of Lean (which, among other things, has excellent support for quotient types).

I have therefore decided to launch aLean companion to “Analysis I”, which is a “translation” of many of the definitions, theorems, and exercises of the text into Lean. In particular, this gives an alternate way to perform the exercises in the book, by instead filling in the corresponding “sorries” in the Lean code. (I do not however plan on hosting “official” solutions to the exercises in this companion; instead, feel free to create forks of the repository in which these sorries are filled in.)

Currently, the following sections of the text have been translated into Lean:Section 2.1: The natural numbersSection 2.2: AdditionSection 2.3: MultiplicationChapter 2 epilogue: Isomorphism with the Mathlib natural numbersSection 3.1: Basic set theorySection 4.1: The integers

The formalization has been deliberately designed to be separate from the standard Lean math libraryMathlibat some places, but reliant on it at others. For instance, Mathlib already has a standard notion of the natural numbers. In the Lean formalization, I first develop “by hand” an alternate constructionChapter2.Natof the natural numbers (or justNat, if one is working in theChapter2namespace), setting up many of the basic results about these alternate natural numbers which parallel similar lemmas aboutthat are already in Mathlib (but with many of these lemmas set as exercises to the reader, with the proofs currently replaced with “sorries”). Then, in an epilogue section, isomorphisms between these alternate natural numbers and the Mathlib natural numbers are established (or more precisely, set as exercises). From that point on, the Chapter 2 natural numbers are deprecated, and the Mathlib natural numbers are used instead. I intend to continue this general pattern throughout the book, so that as one advances into later chapters, one increasingly relies on Mathlib’s definitions and functions, rather than directly referring to any counterparts from earlier chapters. As such, this companion could also be used as an introduction to Lean and Mathlib as well as to real analysis (somewhat in the spirit of the “Natural number game“, which in fact has significant thematic overlap with Chapter 2 of my text).

The code in this repository compiles in Lean, but I have not tested whether all of the (numerous) “sorries” in the code can actually be filled (i.e., if all the exercises can actually be solved in Lean). I would be interested in having volunteers “playtest” the companion to see if this can actually be done (and if the helper lemmas or “API” provided in the Lean files are sufficient to fill in the sorries in a conceptually straightforward manner without having to rely on more esoteric Lean programming techniques). Any other feedback will of course also be welcome.

[UPDATE, May 31: moved the companion to a standalone repository.]

### Share this:

Like

Loading...
