---
title: madhadron - The seven programming ur-languages
url: https://madhadron.com/programming/seven_ur_languages.html
site_name: hnrss
content_file: hnrss-madhadron-the-seven-programming-ur-languages
fetched_at: '2026-04-19T19:41:07.004654'
original_url: https://madhadron.com/programming/seven_ur_languages.html
date: '2026-04-19'
description: The seven programming ur-languages (2022)
tags:
- hackernews
- hnrss
---

# The seven programming ur-languages

I regularly hear people asking which programming language to learn,
and then reeling off a list of very similar languages (“Should I learn
Java, C#, C++, Python, or Ruby?”). In response I usually tell them that
it doesn’t really matter, as long as they get started. There are
fundamentals behind them.

What do I mean when I say fundamentals? If you have an array or list
of items and you’re going to loop over it, that is the same in any
imperative language. There is straightforward iteration

int
[
10
]
 arr
;

for
 
(
int
 i 
=
 
0
;
 i 
<
 
10
;
 i
++)
 
{

 
// do something with arr[i]

}

and there is iterating over all unordered combinations

int
[
10
]
 arr
;

for
 
(
int
 i 
=
 
0
;
 i 
<
 
10
;
 i
++)
 
{

 
for
 
(
int
 j 
=
 i
+
1
;
 j 
<
 
10
;
 j
++)
 
{

 
// do something with arr[i] and arr[j]

 
}

}

and a few other patterns, but those patterns are basically the same
in C, Java, Python, or Fortran. Having neural pathways that fluently
express intention in these patterns, the same way you express thoughts
in sentence structures in English, are fundamentals.

But not all languages have the same set of patterns. The patterns for
looping in C or Python are very different from the patterns of recursion
in Standard ML or Prolog. The way you organize a program in Lisp, where
you name new language constructs, is very different from how you
organize it in APL, where fragments of symbol sequences are both the
definitions of behavior and become the label for that behavior in your
mind.

These distinct collections of fundamentals form variousur-languages. Learning a new language that traces to the sameur-language is an easy shift. Learning one that traces to an
unfamiliarur-language requires significant time and effort and
new neural pathways.

I am aware of sevenur-languages in software today. I’ll
name them for atype specimen, the way a species in
paleontology is named for a particular fossil that defines it and then
other fossils are compared to the type specimen to determine their
identity. Theur-languages are:

* ALGOL
* Lisp
* ML
* Self
* Forth
* APL
* Prolog

## ALGOL

Characteristics. Programs consist of sequences of
assignments, conditionals, and loops, organized into functions. Many
languages add module systems, ways of defining new data types,
polymorphism, or alternate control flow constructs like exceptions or
coroutines.

Examples. Most common programming languages trace to
thisur-language. ALGOL itself included ALGOL 58, ALGOL 60,
ALGOL W, and ALGOL 68. Assembly languages for mainstream processors,
Fortran, C, C++, Python, Java, C#, Ruby, Pascal, JavaScript and Ada all
trace to thisur-language.

History. This is the oldestur-language,
going back to Ada Lovelace formulating programs for Babbage’s analytical
engine. The machine and assembly languages for all Eckert-Mauchly
architecture computers, going back to EDVAC and the first Univacs were
of this form, as were all early attempts at higher level languages,
starting with Grace Hopper’s A-0 and going through Fortran and COBOL. In
the 1960’s the academic computer science community developed structured
programming to make programming in these languages more manageable,
which led to ALGOL 60, which basically all members of the class derive
from.

Over time, members of this family accrete features taken from otherur-languages. In the 1980’s, notions from the Selfur-language were grafted onto many of these language in the
form of classes as a way to define data types and do polymorphism. Since
2010, ideas from the MLur-language have been appearing.

## Lisp

Characteristics. Lisp consists of prefix expressions
enclosed in parentheses, for example

(
+
 
2
 
3
)

(
defun
 square 
(x)

 (
*
 x x))

(
*
 (square 
3
) 
3
)

This syntax seems bizarre, but the language also has a built-in
representation of lists as a data structure as parentheses around the
space separated items (e.g.,(1 2 3 4)). Thus the code is
in the form of a list, and Lisp systems let you define macros that take
a list, modify it, and pass that modified code to the compiler.

Lisps tend to behave like some otherur-language when
writing most code (usually ALGOL or ML), but are distinguished by the
macro system that lets the programmer redefine the semantics of the
language. Common Lisp, for example, has aloopsyntax, but
it is defined as a macro, not built into the language.

Examples. There were many early Lisps, but the
community achieved a consensus in Common Lisp. Meanwhile, Sussman and
Steele explored how much could be done with functions and produced
Scheme. Several other special purpose Lisps such as Lush (for numerical
computing), AutoLISP (the scripting language for AutoCAD), and Emacs
Lisp (the language used to implement editing behavior in the Emacs
editor) have been used. In recent years Clojure has emerged as a third
major branch of the Lisp family.

History. Lisp is about a year younger than Fortran,
which makes it the second oldest language still in use today. Its
origins were in a purely mathematical question: how do you write down a
mathematical structure you can define that can evaluate its own
expressions? John McCarthy provided an answer in 1958, which then got
implemented on a computer. That mathematical background made early Lisps
awkward fits for the machines they were on. Questions about memory and
CPU cycles were irrelevant to the mathematics, and things like garbage
collection had to be invented to make it work.

There was a period in the late 1970’s and early 1980’s when machines
were specially built to run Lisp from the ground up. Much of today’s
integrated development environments was invented on those machines. Lisp
itself was the vehicle of choice for most artificial intelligence
research in that period, and when artifical intelligence’s hype in the
1980’s failed to deliver, the field, and Lisp with it, crashed into what
is called the “AI Winter.” Lisps remain stubbornly alive to this day,
especially as computers gained power and other languages adopted many of
the features that originally made them awkward to implement.

## ML (functional languages)

Characteristics. ML languages are defined by
functions being first class values and a type system in the
Hindley-Milner family that is adequate to represent different kinds of
functions and tagged unions. All iteration is done by recursion, as
in

sum : 
list
 
of
 
int
 -> 
int

sum [] = 
0

sum (x:xs) = x + sum xs

or by defining functions that encapsulate the iteration pattern and
take another function to implement the behavior.

map : ('a -> 'a) -> 
list
 
of
 'a -> 
list
 
of
 'a

map _ [] = []

map f (x:xs) = (f x) : (map f xs)

Some languages in the family (Miranda and Haskell) are lazy by
default, that is, they do not evaluate anything until it is actually
needed. Others explore extensions of the type system in various
directions. OCaml attempts to merge notions from the Selfur-language. Agda and Idris mix values and types (what is
called dependent type systems) and 1ML mixes modules and types.

Examples. ML spawned CaML (Cambridge ML), Standard
ML, OCaml, and a whole related family such as Miranda, Haskell, and
today the dependently typed languages like Agda and Idris.

History. ML was the metalanguage (thus the name) for
a theorem proving program developed in Cambridge, England. The language
escaped from that context and was popular in Europe, particularly in
England and France.

## Self (object oriented
languages)

Characteristics. A program consists of a set of
objects that can receive and send messages to each other. All behavior
is implemented in this way. You create a new object by sending a message
to an existing object. You do conditionals by having a variable which
refers to either the true object or the false object. Both take a
message with two parameters, a function to run on true, and a function
to run on false. The true object runs the first function. The false
object runs the second. The calling code does not know which it is
sending to, only that it is sending a message. Loops are the same.
Indeed, by creating and inserting appropriate objects into the right
places you can entirely redefine the semantics of the language.

These languages usually have their source stored in a live
environment rather than text files. The programmer modifies the live
system and saves its new state rather than compile files to produce a
system.

Examples. The two important examples are Smalltalk
and Self. A whole range of languages implement message passing to
objects in some subset of the language. This kind of partial import is
usually referred to as “object oriented programming.” Most of these are
modeled on Smalltalk. JavaScript is the exception, and derives from
Self’s classless object system.

The ideas were taken in two other important directions.

First, Common Lisp’s object system generalized the idea of choosing
what code is run based on what object receives a message. It disconnects
behavior from the objects and instead the runtime chooses which behavior
to run based on all the parameters involved, not just one.

Second, Erlang switched the notion of a thread of execution jumping
from object to object to run various code and instead had parallel
threads of execution that explicitly listen for and send messages.

History. Smalltalk was the original language,
developed at Xerox Parc in the late 1970’s and 1980’s. There were a
variety of commercial Smalltalk systems in the 1980’s, and IBM used
Smalltalk to develop its programming tools for other languages (the
collection of tools known as VisualAge). Today Smalltalk largely
survives as the open source Pharo Smalltalk.

A lot of work was done on how to make Smalltalk run fast and
efficiently, culminating in the Strongtalk project. Strongtalk is
historically important because its discoveries became the basis of the
HotSpot just-in-time compiler for Java.

Smalltalk inherited the notion of a value and its type from earlier
languages, and implemented the idea of a class. All objects had a class
that gave their type, and the class was used to construct objects of
that type. Self disposed of the notion of class and worked solely with
objects. As this is a purer form, I have chosen Self as the type
specimen for thisur-language.

## Forth (stack languages)

Characteristics. Stack languages are an inverse of
Lisp, and share the grammar of Hewlett Packard reverse Polish notation
calculators. They have a data stack. When you write a literal like the
number42, it is pushed to the stack. When you write the
name of a function, it takes no explicit parameters. Instead it operates
on the stack. Simple arithmetic looks quite backwards

2 3 + 5 *

and function definitions are equally terse. In most Forth variants,:defines a new word, in this casesquare.
Whensquareis called it is the same as callingdup, which duplicates the top element of the stack,
followed by*, which multiplies the top two elements.

: square dup * ;

3 square

Forth allows programmers to intercept the parser and replace it with
their own code, so the grammar is entirely replaceable. It is common to
see Forth programs that define small languages, such as a Fortran subset
or a way to directly ASCII parse diagrams giving packet layouts or the
transitions of state machines.

Examples. Forth in all its many variants,
PostScript, Factor, Joy (a purely functional language that uses a
mathematical formulation of composition in place of the stack).

History. Forth was originally written in 1970 to
control radio telescopes, but then spread broadly in embedded systems.
It is sufficiently easy to bootstrap a Forth system that there are
dozens of variations created by different programmers for thir own
purposes.

PostScript emerged in the 1980’s as a flexible means to describe
documents to printers. It is much more limited in many ways than Forth,
but defines primitives related to graphical layouts in the language.

## APL (array languages)

Characteristics. Everything in the language is an (n
dimensional) array. Operators are one or two symbols long, and implement
high level operations over these arrays. The result is so terse that the
sequences of symbols become the label for an operation rather than
giving it another name. For example, to calculate the average of an
array in variablex, you would write

(
+
⌿÷≢
)
 
x

Examples. APL, J, K. The higher order operations
over arrays have been partially exported into many environments, such as
MATLAB, NumPy, and R.

History. APL began as a mathematical notation
created by Kenneth Iverson in the 1960’s. He then implemented it on a
computer. It has enjoyed a niche following ever since among people doing
heavy calculations. Its descendant, K, was very popular in financial
settings.

## Prolog (logic languages)

Characteristics. Programs consist of facts, either
“ground” facts such as Bob is Ed and Jane’s father,

father(bob
,
 ed)
.

father(bob
,
 jane)
.

or non-ground facts which define how to derive a fact from other
facts by putting in variables (which are capitalized)

grandfather(
X
,
 
Y
) 
:-
 father(
X
,
 
Z
)
,
 father(
Z
,
 
Y
)
.

Prolog runtimes take these facts and a query on them and searches for
a result for the query. And it turns out that if you choose the right
structure for defining facts, this is Turing complete.

The terms that form facts in Prolog are a native data type in their
own right that can be created and then fed to the runtime, the same way
that Lisp’s macros or Forth’s parser replacement work.

Because Prolog programs are basically searches, they are tuned rather
the way database queries are, adjusting the order in which things are
searched and cutting off paths that will not yield anything as early as
possible.

Examples. Prolog, Mercury, Kanren. The vast majority
of programming around thisur-language takes place in Prolog
itself — the community is impressively unified.

History. In the 1970’s, logicians in France realized
that they could express programs in terms of first order logic, and
began trying to implement this. In the 1980’s the Japanese fifth
generation computer project bet heavily on Prolog, and when that project
failed, Prolog went down in reputation with it.

Meanwhile, decades of research continued into how to make Prolog
runtimes smart enough to be efficient in most cases and how to add new
capabilities, such as numerical constraints (yielding constraint logic
programming).

Prolog tends to show up in niches. Type checking for Java was for
many years implemented in Prolog, as was Facebook’s original source code
search tool.

## What to do with this

For most programmers some or all of these will seem very exotic. It
is worth spending some time with each of them for the neural pathways
they will make you grow and the possibilities they introduce. Very often
two things that seems completely different when viewed through an ALGOL
lens turn into a trivial comparison seen through a different lens.

First, every programmer needs to know a language in
the ALGOL family well.

Second, learn a language in the Prolog family: SQL.
This is after the ALGOL family, SQL will give you the most mileage in
your career. I’ve collected the most common stumbling blocks people hit
when learning SQL into afree
course.

Then, once you’ve got these two, it’s worth
branching out. Learning a new language that traces to an unfamiliarur-language each year will pay dividends. The languages I would
suggest today in each of these families, and maybe in this order,
are:

* Lisp: PLT Racket
* ML: Haskell
* Self: Self
* Prolog: Prolog1
* Forth: gForth2
* APL: K (viaok)

If you do a lot of numerical work, learn K earlier. If you do lots of
embedded programming, learn gForth earlier. But the order is not
important, nor is the exact language. You could learn Standard ML or
OCaml instead of Haskell, Common Lisp instead of PLT Racket, and Factor
instead of gForth with absolute impunity. These are not-wrong
suggestions as opposed to perfect answers.

Mentioned inWriting programs

1. Yes, you should still learn Prolog even after you learn
SQL. They’re quite different in practice.↩︎
2. A reader pointed out to me that getting Forth in a deep
way usually involves building Forths, since they’re small enough for a
single person to build one from the ground up fairly quickly. gForth is
a good implementation of ANS Forth to learn to use the language. The
same reader pointed to McCabe’s bookFORTH Fundamentals, Volume
1as their preferred resource for learning to build them. Other
good Forths to study are PygmyForth, eForth, and of course Chuck Moore’s
colorForth.↩︎

« Back toProgramming|Home