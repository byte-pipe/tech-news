---
title: The Lobster Programming Language — Wouter van Oortmerssen
url: https://strlen.com/lobster/
site_name: hackernews_api
content_file: hackernews_api-the-lobster-programming-language-wouter-van-oortme
fetched_at: '2026-03-09T07:24:35.050448'
original_url: https://strlen.com/lobster/
author: keyle
date: '2026-03-04'
description: The Lobster Programming Language
tags:
- hackernews
- trending
---

# The Lobster Programming Language

Lobster is a programming language that tries to combine the advantages of static typing and compile-time memory management with a very lightweight, friendly and terse syntax, by doing most of the heavy lifting for you.

While it is a general purpose language, its current implementation is biased towards games and
other graphical things, with plenty of “batteries included” functionality.

Lobster is Open Source (Apache v2 license) and can be found ongithub. Online copy of the fulldocumentation.

## Features

Features have been picked for their suitability in a game programming language, and in particular to make code terse, quick to write and refactor. It is meant to not hold you back to get an idea going quickly.

* LanguageStatic typing that feels almost as easy to write as dynamic typing thanks to “Flow-Sensitive Type-Inference and Specialization”.Compile time reference counting / lifetime analysis / borrow checker.Lightweight Blocks / Anonymous Functions that make any function using them look identical to built-in control structures.Vector operations (for math and many other builtins).Unified overloading & dynamic dispatch, in & outside classes, supporting specialization.Immutable “inline” structs (zero overhead).GIL-less, race-less distributed memory model multi-threading.Python-style indentation based syntax with C-style flavoring
* Static typing that feels almost as easy to write as dynamic typing thanks to “Flow-Sensitive Type-Inference and Specialization”.
* Compile time reference counting / lifetime analysis / borrow checker.
* Lightweight Blocks / Anonymous Functions that make any function using them look identical to built-in control structures.
* Vector operations (for math and many other builtins).
* Unified overloading & dynamic dispatch, in & outside classes, supporting specialization.
* Immutable “inline” structs (zero overhead).
* GIL-less, race-less distributed memory model multi-threading.
* Python-style indentation based syntax with C-style flavoring
* ImplementationChoose between running directly using the convenient JIT, or compilation to C++ for extra speed.Reference Counting with cycle detection at exit, 95% of reference count ops removed at
compile time thanks to lifetime analysis.Fully graphical debugger (inspect stack traces, modify variables etc).Dynamic code loading.Relatively fast (order of magnitude faster than Python, significantly faster than Lua (benchmark), not yet a C competitor, but can be eventually) and economical (low overhead memory allocation)Easy to deploy (engine/JIT exe + compressed bytecode file)Modularly extendable with your own library of C++ functions
* Choose between running directly using the convenient JIT, or compilation to C++ for extra speed.
* Reference Counting with cycle detection at exit, 95% of reference count ops removed at
compile time thanks to lifetime analysis.
* Fully graphical debugger (inspect stack traces, modify variables etc).
* Dynamic code loading.
* Relatively fast (order of magnitude faster than Python, significantly faster than Lua (benchmark), not yet a C competitor, but can be eventually) and economical (low overhead memory allocation)
* Easy to deploy (engine/JIT exe + compressed bytecode file)
* Modularly extendable with your own library of C++ functions
* EnginePortable (mostly courtesy of OpenGL/SDL/Freetype), allowing your games to be run on Windows, Linux, Mac OS X, iOS, Android and WebAssembly (in that order of maturity, currently).High level interface to OpenGL functionality, very quick to get going with simple 2D geometric primitives3D primitive construction either directly from triangles, or using high level primitives made into meshes through marching cubesGLSL shaders (usable accross OpenGL & OpenGL ES 2 without changes)Accurate text rendering through FreeTypeUniform input system for mouse & touchSimple sound system supporting .wav and .sfxr synth files.ImGui support.Comes with useful libraries written in Lobster for things like A* path finding and game GUIs
* Portable (mostly courtesy of OpenGL/SDL/Freetype), allowing your games to be run on Windows, Linux, Mac OS X, iOS, Android and WebAssembly (in that order of maturity, currently).
* High level interface to OpenGL functionality, very quick to get going with simple 2D geometric primitives
* 3D primitive construction either directly from triangles, or using high level primitives made into meshes through marching cubes
* GLSL shaders (usable accross OpenGL & OpenGL ES 2 without changes)
* Accurate text rendering through FreeType
* Uniform input system for mouse & touch
* Simple sound system supporting .wav and .sfxr synth files.
* ImGui support.
* Comes with useful libraries written in Lobster for things like A* path finding and game GUIs

## Examples

let’s start with syntax and blocks:

def
 
find
(xs, fun):
 
for
(xs) x, i:
 
if
 fun(x):
 
return
 i
 
return
 
-
1

let r 
=
 
2

let i 
=
 find [ 
1
, 
2
, 
3
 ]: _ 
>
 r

We can learn a lot about the language from this tiny example:

* findis a function that takes a vector and a function as argument, and returns the index of the first element for which that function returns true, or -1 if none.
* It uses an indentation based syntax, though in this example thefor-if-returncould also have been written on a single line.
* The call tofindis in its maximum terse form which is a shorter form of writing the more verbosefind([ 1, 2, 3 ], fn(x): x > r). Blocks / anonymous function arguments are typically written directly after the call they are part of, and generally have the syntax of a (possibly empty) list of arguments (separated by commas), separated from the body by a:. The body may either follow directly, or start a new indentation block on the next line. Additionally, if you don’t feel like declaring arguments, you may use variable names starting with an_inside the body that are automatically declared.
* forandiflook like language features, but they have no special syntactical status compared tofind. Any such functions you add will work with the same syntax.
* Notice the complete lack of type declarations. The code is fully statically typed, however, type inference is smart enough to assign types to everything, and functions likefindget specialized to work on whatever arguments they are called with, in this case a list of ints, and a specific lambda. Specialization not only increases the range of code type inference can handle, it allows the compiler to optimize this particular case as if you had hard-coded the loop (much like C++ templates).
* blocks/functions may refer to “free variables”, i.e. variables declared outside of their own scope, liker. This is essential to utilize the full potential of blocks.
* iwill contain2at the end of this (the index of element3). It does not clash with the otheribecause of lexical scoping. Here=means assignment, andlet(orvarfor mutable) defines a new variable.
* returnreturns fromfind, not from the enclosing function (which would be the block passed toif). In fact, it can be made to return from any named function, which makes it powerful enough to implement exception handling in Lobster code, instead of part of the language.

Types, dynamic dispatch, immutables and vector ops:

class
 
Animal
:
 alive 
=
 true

class
 
Cat
 : Animal
 
def
 
hello
(): 
print
 
"meow"

class
 
Dog
 : Animal
 barked 
=
 
0

def
 
hello
(d::Dog):
 
print
 
"bark!"

 barked
++

let d 
=
 Dog {}
d
.
hello()

let a:Animal 
=
 d
a
.
hello()

What we learn here:

* we can declare custom datatypes, that can optionally inherit from existing datatypes.
* we can declare them with eitherstructorclass, where the former means the object is immutable and passed in-line by value. This enforces more functional style programming for objects which can be seen as unit things (like points and vectors). These structs can be used with the rich set of built-in vector operations.
* We can declare multiple version of a function, either in-line in the class, or anywhere else (both declarations ofhelloabove are equivalent). These functions can be used as overloads (statically dispatched, liked.hello()) or dynamic dispatch (likea.hello()). Unlike other languages, this distinction depends on context, and because in Lobster all types and functions are known (closed world compilation), this can use static dispatch more often.
* we can specify types for arguments with:. Besides their use in overloads, they can be used in regular functions to make compile time type errors simpler. You can even specify the type with::, which allows you direct access to all members of the type, so you can writexinstead ofp.xetc.
* (not shown here): classes, structs and functions can have generic arguments, even in addition to dynamic dispatch.

Enough of dry programming language stuff, how do we draw?

import
 
vec

import
 
color

import
 
gl

let directions 
=
 [ xy_0, xy_x, xy_y ]

def
 
sierpinski
(depth) 
->
 void:
 
if
 depth:
 gl_scale 
0.5
:
 
for
(directions) d:
 gl_translate d:
 sierpinski(depth 
-
 
1
)
 
else
:
 gl_polygon(directions)

fatal(gl_window(
"sierpinski"
, 
512
, 
512
))

while
 gl_frame():
 
if
 gl_button(
"escape"
) 
==
 
1
: 
return

 gl_clear(color_black)
 gl_scale(
float
(gl_window_size()))
 sierpinski(
7
)

which produces:

What do we see:

* if we skip togl_window, this creates the window and sets up OpenGL basics. This can theoretically fail which will return us an error string, but here for the example we’re lazy.
* rendering in Lobster centers around frames like in most game engines, so we redraw everything every time (this example has no animation or interaction, so that looks a bit silly).gl_frametakes care not only of frame swapping, but updating input etc as well
* gl_scaleallows us to scale all rendering by specifying the unit size (compared to the previous scale, which by default is pixel size). Using the current window size thus gets us a canvas with a resolution of 1.0 x 1.0 which is convenient for the algorithm we’re about to run
* The import pulls in definitions for 2d/3d/4d vectors and some useful constants (e.g.xyz_0is a vector of all zeroes).
* The recursive function then keeps subdividing and scaling in 3 directions until it gets to the bottom of the recursion where it draws the triangles

To see more about the builtin functionality of Lobster (graphics or otherwise), check out thebuiltin functions reference(this particular file may be out of date, it can be regenerated by the runninglobster -r). You can also check out draft version of the full Lobsterdocumentation,
in particular theLanguage Reference.

Most recent version of everything is onGitHub.

Come chat onDiscordorGitter.

Like it on theFacebook page.