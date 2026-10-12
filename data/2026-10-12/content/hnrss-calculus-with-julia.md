---
title: Calculus with Julia
url: https://jverzani.github.io/CalculusWithJuliaNotes.jl/
site_name: hnrss
content_file: hnrss-calculus-with-julia
fetched_at: '2026-10-12T20:08:26.024403'
original_url: https://jverzani.github.io/CalculusWithJuliaNotes.jl/
author: John Verzani
date: '2026-10-10'
description: Calculus with Julia
tags:
- hackernews
- hnrss
---

# Preface

Calculus with Julia

This is a set of notes for learningcalculususing theJulialanguage.Juliais an open-source programming language with an easy to learn syntax that is well suited for this task.

Read “Getting started with Julia” to learn how to install and customizeJuliafor following along with these notes. Read “Julia interfaces” to review different ways to interact with aJuliainstallation.

Since the mid 90s there has been a push to teach calculus using many different points of view. TheHarvardstyle rule of four says that as much as possible the conversation should include a graphical, numerical, algebraic, and verbal component. These notes use the programming languageJuliato illustrate the graphical, numerical, and, at times, the algebraic aspects of calculus.

There are many examples of integrating a computer algebra system (such asMathematica,Maple, orSage) into the calculus conversation. Computer algebra systems can be magical. The popularWolframAlphawebsite calls the full power ofMathematicawhile allowing an informal syntax that is flexible enough to be used as a backend for Apple’s Siri feature. (“Siri what is the graph of x squared minus 4?”) For learning purposes, computer algebra systems model very well the algebraic/symbolic treatment of the material while providing means to illustrate the numeric aspects. These notes are a bit different in thatJuliais primarily used for the numeric style of computing and the algebraic/symbolic treatment is added on. Doing the symbolic treatment by hand can be very beneficial while learning, and computer algebra systems make those exercises seem kind of redundant, as the finished product can be produced much more easily.

Our real goal is to get at the concepts using technology as much as possible without getting bogged down in the mechanics of the computer language. We feelJuliahas a very natural syntax that makes the initial start up not so much more difficult than using a calculator, but with a language that has a tremendous upside. The notes restrict themselves to a reduced set of computational concepts. This set is sufficient for working many of the problems in calculus, but do not cover thoroughly many aspects of programming. (Those who are interested can go off on their own andJuliaprovides a rich opportunity to do so.) Within this restricted set, are operators that make many of the computations of calculus reduce to a function call of the formaction(function, arguments...). With a small collection of actions that can be composed, many of the problems associated with introductory calculus can be attacked.

These notes are presented in pages covering a fairly focused concept, in a spirit similar to a section of a book. Just like a book, there are try-it-yourself questions at the end of each page. All have a limited number of self-graded answers. These notes borrow ideas from many sources, for exampleStrang (n.d.),Knill (n.d.),Schey (1997),Hass et al. (2018),Rogawski et al. (2019),Angenent (2012), several Wikipedia pages, and other sources.

These notes are accompanied by aJuliapackageCalculusWithJuliathat provides some simple functions to streamline some common tasks and loads some useful packages that will be used repeatedly.

These notes are presented as a Quarto book. To learn more about Quarto books visithttps://quarto.org/docs/books.

Compiling these notes into apdffile with Quarto is possible with some piecing together of parts. The result is less than optimal and also quite large.

Download pdf version

Tocontribute– say by suggesting additional topics, correcting a mistake, or fixing a typo – click the “Edit this page” link and join the list ofcontributors. Thanks to all contributors.

Averyspecial thanks goes out to@fangliu-tjufor their careful and most-appreciated proofreading and error spotting spread over a series of PRs.

## Running Julia

For individual usersJuliais installed quite easily with thejuliauputility or by other means. There are some brief installation notes in the overview ofJuliacommands.

Calculus with Julia version 0.27, produced on August 31, 2026.

Angenent, Sigurd. 2012. 
Wisconsin Calculus
. Https://github.com/SigurdAngenent/WisconsinCalculus/tree/master.

Hass, Joel R., Christopher E. Heil, and Maurice D. Weir. 2018. 
Thomas’ Calculus
. Pearson.

Knill, Oliver. n.d. 
Some Teaching Notes
. 
https://people.math.harvard.edu/~knill/teach/index.html
.

Rogawski, Jon, Colin Adams, and Robert Franzosa. 2019. 
Calculus
. Macmillan.

Schey, H. M. 1997. 
Div, Grad, Curl, and All That
. W.W. Norton.

Strang, Gilbert. n.d. 
Calculus
. Wellesley-Cambridge Press. 
https://ocw.mit.edu/courses/res-18-001-calculus-online-textbook-spring-2005/
.