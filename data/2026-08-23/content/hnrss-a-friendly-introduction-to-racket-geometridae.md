---
title: A Friendly Introduction to Racket – geometridae
url: https://geometridae.bearblog.dev/a-friendly-introduction-to-racket/
site_name: hnrss
content_file: hnrss-a-friendly-introduction-to-racket-geometridae
fetched_at: '2026-08-23T06:00:49.920254'
original_url: https://geometridae.bearblog.dev/a-friendly-introduction-to-racket/
date: '2026-08-22'
description: '<p style="text-align: center;"><img src="https://bear-images.sfo2.cdn.digitaloceanspaces.com/mothcodes/steal-your-face-plt.svg" alt="steal-your-face-plt" wid...'
tags:
- hackernews
- hnrss
---

# A Friendly Introduction to Racket

11 Aug, 2026

"Lisp is worth learning for the profound enlightenment experience you will have when you finally get it." — Eric S. Raymond

Welcome. Today you'll learn a language from one of programming's oldest and most unusual families. A language where code is data, where parentheses are pure structure, and where programs can write programs. By the end of this tutorial, you'll have written your own syntax.

## A bit of history

Lisp was born in1958, invented by John McCarthy at MIT. For context: it's thesecond-oldest high-level language still in use(only Fortran, from 1957, beats it by a year). Python arrived in 1991. JavaScript in 1995. Lisp predates them by more than 30 years and several ideas we now consider "modern" were born there:

* Garbage collection— inventedforLisp.
* First-class functions— passing functions as arguments, now standard everywhere.
* The REPL— the interactive read-eval-print loop that Python, Node, and Julia all have today started in Lisp.
* Conditionals as expressions— theifthat returns a value.
* Homoiconicity— codeisa data structure of the language itself. This is the big one. We'll come back to it at the end.

For decades, Lisp wasthelanguage of artificial intelligence. In the 70s and 80s there were physical computers designed to run Lisp directly: theLisp Machinesbuilt by Symbolics and LMI. Then came the "AI winter," funding dried up, and Lisp went from star to cult language.

But interesting ideas don't die they mutate, that's part of the beauty of the lisps.

### From Lisp to Scheme to Racket

In 1975, Gerald Sussman and Guy Steele createdScheme: a minimalist, elegant, almost mathematical Lisp. Scheme became academia's favorite language forteachingprogramming (the legendary bookSICPStructure and Interpretation of Computer Programs is written in Scheme).

In 1995, Matthias Felleisen's group createdPLT Scheme, a Scheme designed for education and programming language research. In 2010 it was renamedRacket, and today it's much more than a Scheme: it's alanguage for building languages. Its unofficial motto islanguage-oriented programming: if your problem needs its own language, Racket lets you build one in an afternoon.

Year

Event

1958

McCarthy invents Lisp at MIT

1975

Sussman and Steele create Scheme

1984

Common Lisp is standardized

1995

PLT Scheme (now Racket) is born

2007

Clojure is born (Lisp on the JVM)

2010

PLT Scheme is renamed Racket

Today

You, reading this, about to write parentheses UwU

## Who uses Lisptoday?

More people than you might think:

* Clojureruns in production at banks, airlines, and startups (Nubank, the largest digital bank in Latin America, runs on Clojure).
* Common Lisp(with the SBCL compiler) is still alive in expert systems, flight planning (ITA Software, acquired by Google, powered Google Flights), and scientific computing.
* Emacs Lisp— millions of people run Lisp every day without knowing it, because their editorisa Lisp interpreter.
* Guile/Guix— an entire Linux distribution configured 100% in Scheme.
* Rackethas its own annual conference (RacketCon), an active academic and artistic community, and is used for language research, formal verification (Rosette), typography and publishing (Pollen), and education around the world.
* And new Lisps keep appearing:Fennel(a Lisp that compiles to Lua, popular for games),Janet,Hy(a Lisp on top of Python)...

## Easter egg for TADC fans:

InThe Amazing Digital Circus(episode 8, "hjsakldfhl"), when Kinger opens the terminal to try to reset Caine, you can see that Caine (a creative AI built in 1996) is programmed in Lisp. The file is literally namedCaine-core.lisp.

## Installation (5 minutes)

1. Go tohttps://racket-lang.org
2. Download the installer for your system (Linux, macOS, Windows).
3. OpenDrRacket, the environment that comes included.

DrRacket has two areas: at the top you write yourdefinitions(your program), and at the bottom you have theREPLfor live experimentation. On the first line of the definitions area, write:

#lang 
racket

That line tells Racket which language you're using (remember: Racket is a language factory, so you have to pick one).

If you prefer the terminal: theracketcommand gives you a REPL, andracois the package manager and tooling command.

## First contact: everything is an expression

In the REPL, try:

>
 
(
+
 
1
 
2
)

3

>
 
(
*
 
3
 
(
+
 
2
 
2
))

12

>
 
(
string-append
 
"hello "
 
"world"
)

"hello world"

The rule of Lisp fits in one line:

Everything is(operator argument1 argument2 ...). Always. No exceptions.

There's no operator precedence to memorize, no special syntax for anything.(+ 1 2)adds.(if ...)decides.(define ...)names. The parentheses that look intimidating at first are actually the complete absence of arbitrary rules. After a week, you stop seeing them.

## Definitions and functions

#lang 
racket

(
define
 
pi-approx
 
3.14159
)

(
define
 
(
circle-area
 
r
)

 
(
*
 
pi-approx
 
r
 
r
))

(
circle-area
 
2
)
 
; => 12.56636

* definewith a name creates a constant.
* definewith(name arguments...)creates a function.
* Comments start with;.

Anonymous functions uselambda(yes,thatlambda Church's lambda calculus from the 1930s is the theoretical grandparent of all this):

(
lambda
 
(
x
)
 
(
*
 
x
 
x
))
 
; a function with no name

((
lambda
 
(
x
)
 
(
*
 
x
 
x
))
 
5
)
 
; => 25, applied directly

## Lists: the heart of Lisp

Lisp stands forLIStProcessing. Lists are the fundamental structure:

(
list
 
1
 
2
 
3
)
 
; => '(1 2 3)

'
(
1
 
2
 
3
)
 
; the same thing, "quoted"

(
first
 
'
(
1
 
2
 
3
))
 
; => 1

(
rest
 
'
(
1
 
2
 
3
))
 
; => '(2 3)

(
cons
 
0
 
'
(
1
 
2
 
3
))
 
; => '(0 1 2 3)

(
length
 
'
(
a
 
b
 
c
))
 
; => 3

Notice the quote mark'. It tells Racket:don't evaluate this, it's data. Hold onto that detail it's the door to the final trick.

### Higher-order functions

This is where Racket shines. Passing functions to other functions is the most natural thing in the world:

(
map
 
(
lambda
 
(
x
)
 
(
*
 
x
 
x
))
 
'
(
1
 
2
 
3
 
4
 
5
))

; => '(1 4 9 16 25)

(
filter
 
even?
 
'
(
1
 
2
 
3
 
4
 
5
 
6
))

; => '(2 4 6)

(
foldl
 
+
 
0
 
'
(
1
 
2
 
3
 
4
 
5
))

; => 15

maptransforms,filterselects,foldlaccumulates. With those three functions you can solve most list problems without writing a singleforloop.

## Recursion: thinking in spirals

In Lisp you don't think "repeat N times" you think "what's the base case, and how do I move toward it?":

(
define
 
(
factorial
 
n
)

 
(
if
 
(
=
 
n
 
0
)

 
1

 
(
*
 
n
 
(
factorial
 
(
-
 
n
 
1
)))))

(
factorial
 
5
)
 
; => 120

And to make things visual, let's draw something. Racket ships with graphics libraries included:

#lang 
racket

(
require
 
2htdp/image
)

(
define
 
(
sierpinski
 
level
)

 
(
if
 
(
=
 
level
 
0
)

 
(
triangle
 
8
 
"solid"
 
"purple"
)

 
(
let
 
([
t
 
(
sierpinski
 
(
-
 
level
 
1
))])

 
(
above
 
t
 
(
beside
 
t
 
t
)))))

(
sierpinski
 
6
)

Paste it into DrRacket, press Run, and watch the Sierpinski triangle appear on your screen.

## The grand finale: code that writes code

Remember the quote mark': it turns code into data. Watch:

'
(
+
 
1
 
2
)
 
; => the LIST (+ 1 2), not the number 3

(
first
 
'
(
+
 
1
 
2
))
 
; => the symbol +

(
eval
 
'
(
+
 
1
 
2
))
 
; => 3. You just evaluated data as code.

Your program is a list. You can build lists. Therefore:you can build programs with programs. This ishomoiconicity, and it's why Lisp has realmacrosnot text macros like in C, but functions that receive code and return code, before anything runs.

Racket doesn't have awhileloop? Let's invent one:

(
define-syntax-rule
 
(
while
 
condition
 
body
 
...
)

 
(
let
 
loop
 
()

 
(
when
 
condition

 
body
 
...

 
(
loop
))))

(
define
 
counter
 
0
)

(
while
 
(
<
 
counter
 
5
)

 
(
displayln
 
counter
)

 
(
set!
 
counter
 
(
+
 
counter
 
1
)))

You justextended the language !in Lisp, the syntax is yours.

Alan Kay called Lisp"the Maxwell's equations of software": a tiny core from which everything else can be derived.

## What next?

* How to Design Programs— the book Racket was designed around, free online.
* The Racket Guide— official documentation, among the best out there.
* Beautiful Racket— learn to build your own languages.
* SICP— the classic of classics, if you want the full enlightenment.