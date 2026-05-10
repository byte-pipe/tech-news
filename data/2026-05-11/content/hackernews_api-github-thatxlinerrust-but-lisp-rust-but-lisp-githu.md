---
title: 'GitHub - ThatXliner/rust-but-lisp: Rust but LISP · GitHub'
url: https://github.com/ThatXliner/rust-but-lisp
site_name: hackernews_api
content_file: hackernews_api-github-thatxlinerrust-but-lisp-rust-but-lisp-githu
fetched_at: '2026-05-11T06:03:39.784316'
original_url: https://github.com/ThatXliner/rust-but-lisp
author: thatxliner
date: '2026-05-10'
description: Rust but LISP. Contribute to ThatXliner/rust-but-lisp development by creating an account on GitHub.
tags:
- hackernews
- trending
---

ThatXliner

 

/

rust-but-lisp

Public

* NotificationsYou must be signed in to change notification settings
* Fork0
* Star95

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

34 Commits
34 Commits
.github/
workflows
.github/
workflows
 
 
assets
assets
 
 
examples
examples
 
 
src
src
 
 
tapes
tapes
 
 
.gitignore
.gitignore
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
README.md
README.md
 
 
SYNTAX.md
SYNTAX.md
 
 
View all files

## Repository files navigation

# rlisp

Hello, Hacker News.You're not wrong. This is a weekend project, not a production compiler — some Rust syntax is missing (turbofish is fixed now, lifetime bounds are on the list). The point isn't completeness; it's exploring what happens when you bolt Lisp macros onto Rust semantics. If that sounds interesting, read on. If you're looking for something to be mad about,the issue tracker is open.

Rust semantics in LISP syntax. Write s-expressions, output Rust source:(s-expr → .rs → binary).

(struct Point
 (x f64)
 (y f64))

(impl Point
 (fn distance ((
&self
) (other 
&Point
)) f64
 (
let
 dx (
-
 (
.
 self x) (
.
 other x)))
 (
let
 dy (
-
 (
.
 self y) (
.
 other y)))
 (
.
 (
+
 (
.
 dx powf 
2.0
) (
.
 dy powf 
2.0
)) 
sqrt
)))

(fn main () ()
 (
let
 p1 (new Point (x 
0.0
) (y 
0.0
)))
 (
let
 p2 (new Point (x 
3.0
) (y 
4.0
)))
 (println! 
"
Distance: {}
"
 (
.
 p1 distance (& p2))))

Ownership, borrowing, lifetimes, generics, traits, pattern matching — all expressed as s-expressions.rustcstill does type checking, borrow checking, and optimization. rlisp just handles the syntax.

Pretty diagnostics withAriadne:

## Install

git clone https://github.com/ThatXliner/rlisp.git

cd
 rlisp
cargo install --path 
.

## Usage

rlisp compile file.lisp 
#
 transpile to file.rs

rlisp build file.lisp 
#
 transpile and compile with rustc

rlisp run file.lisp 
#
 transpile, compile, and run

## Quick reference

LISP

Rust

(fn add ((x i32) (y i32)) i32 (+ x y))

fn add(x: i32, y: i32) -> i32 { (x + y) }

(let x i32 42)

let x: i32 = 42;

(struct Point (x f64) (y f64))

struct Point { x: f64, y: f64 }

(enum Option (< T) (Some T) None)

enum Option<T> { Some(T), None }

(match val ((Some x) (handle x)) (None ()))

match val { Some(x) => { handle(x) }, None => { } }

(if (> x 0) (println! "yes") (println! "no"))

if (x > 0) { println!("yes") } else { println!("no") }

(impl Point (fn new (...) ...))

impl Point { fn new(...) ... }

(trait Display (fn fmt (...) Result))

trait Display { fn fmt(...) -> Result; }

(. obj field)
 / 
(. obj method arg)

obj.field
 / 
obj.method(arg)

(new Point (x 1.0) (y 2.0))

Point { x: 1.0, y: 2.0 }

(loop (body))
 / 
(while cond (body))
 / 
(for x in iter (body))

loop { body }
 / 
while cond { body }
 / 
for x in iter { body }

(lambda (x y) (+ x y))

|x, y| { x + y }

(foo! args)
 / 
(println! "{}" x)

foo!(args)
 / 
println!("{}", x)

(pub fn foo () i32 42)

pub fn foo() -> i32 { 42 }

(rust "let x: i32 = 42; x")

let x: i32 = 42; x

Full reference:SYNTAX.mdcovers everything — generics, lifetimes, visibility, modules, turbofish, inline Rust, if-let, control flow, unsafe blocks, and the complete syntax map.

Binary operators (+,-,*,/,==, etc.) emit infix:(+ a b)→(a + b).

Kebab-case identifiers with hyphens are automatically converted to Rust names using__(double underscore):page-header→page__header. Collisions (e.g.foo-barandfoo__barboth →foo__bar) emit a compile warning.

## Macros

rlisp macros are compile-time s-expression transformers — noproc_macrocrate, no token streaming, no syn/quote. A macro is just a function from s-expressions to s-expressions.

Macro bodies use three special forms borrowed from LISP:

Form

Meaning

(quasiquote template)

"Quote this template, but allow unquotes inside" — like a tagged template literal

(unquote name)

"Insert the value of 
name
 here" — a hole in the template

(unquote-splicing name)

"Splice the list 
name
 into the surrounding list" — for inserting multiple forms

Think ofquasiquoteas "return this exact s-expression, except for theunquoteholes." Without it, you'd have to manually construct every parenthesis withlistandcons.

;
; Define a when macro: (when condition body...)

(
defmacro
 
when
 (
condition
 
&rest
 body)
 (quasiquote (
if
 (unquote 
condition
) (
do
 (unquote-splicing body)))))

;
; Macro expansion:

;
; (when (> x 10) (print "big") (print "huge"))

;
; → (if (> x 10) (do (print "big") (print "huge")))

;
; → if x > 10 { print("big"); print("huge") }

(
defmacro
 
double
 (x)
 (quasiquote (
+
 (unquote x) (unquote x))))

;
; (double 21) → (+ 21 21) → 21 + 21

(fn main () ()
 (
let
 x 
21
)
 (println! 
"
Double: {}
"
 (double x))
 (
when
 (
>
 x 
10
)
 (println! 
"
x is greater than 10
"
)
 (println! 
"
this too
"
)))

&restcaptures all remaining arguments into a list, andunquote-splicingflattens that list into the surrounding form. This is how variadic macros work.

## Loops

(while (
>
 x 
0
)
 (println! 
"
{}
"
 x)
 (-= x 
1
))

(
loop
 (println! 
"
tick
"
))

(for x in 0..10
 (println! 
"
{}
"
 x))

;
; for with destructuring

(for (i val) in (
.
 v iter) enumerate
 (println! 
"
{}: {}
"
 i val))

## Closures

;
; untyped

(
let
 add (
lambda
 (x y) (
+
 x y)))

;
; typed with return type

(
let
 mul (
lambda
 ((x i32) (y i32)) i32 (
*
 x y)))

;
; move closure

(
let
 s 
"
hello
"
)
(
let
 greet (
lambda
 move () (println! 
"
{}
"
 s)))

## Modules, visibility, and imports

(pub fn public_api () i32 
42
)
(pub (crate) fn internal () i32 
0
) 
;
; pub(crate)

(pub (super) fn parent_visible () i32 
1
) 
;
; pub(super)

(pub struct Config
 (pub host 
String
) 
;
; public field

 (port u16)) 
;
; private field

(pub 
mod
 utils 
;
; inline module

 (pub fn helper () i32 
1
)
 (fn private () i32 
0
))

(
mod
 external_lib) 
;
; external module decl

(use 
std
::collections::HashMap)
(use 
std
::io::{self,Write,Read})
(use 
std
::fmt::Display as Fmt)

## Inline Rust

Drop into raw Rust with(rust "...")for anything rlisp doesn't express natively.
The string is emitted verbatim into the generated.rsfile (with LISP escape sequences unescaped):

(fn raw_example () i32
 (rust 
"
let x: i32 = 42; x * 2
"
))

(fn main () ()
 (rust 
"
let message: &str = 
\"
from raw Rust
\"
;
"
)
 (println! 
"
{}
"
 (rust 
"
message
"
)))

## Lifetimes, turbofish, and control flow

;
; Lifetime annotations on function definitions

(fn longest (
<
 
'
a) ((x &'a str) (y &'a str)) (&'a str)
 (
if
 (
>
 (
.
 x len) (
.
 y len)) x y))

;
; Turbofish via :: special form

(
let
 nums ((
::
 (
.
 (0..10) collect) Vec<i32>)))

;
; Break, continue, return

(for x in 0..10
 (
if
 (== x 
5
) (
break
))
 (
if
 (== x 
3
) (
continue
))
 (println! 
"
{}
"
 x))

;
; Type casts

(
let
 
pi
 
3.14159
)
(
let
 approx (as 
pi
 u32))

;
; if-let and while-let

(if-let (
Some
 v) (
.
 
map
 
get
 key)
 (println! 
"
found: {}
"
 v)
 (println! 
"
missing
"
))

(while-let (
Some
 v) ((
.
 iter next))
 (println! 
"
{}
"
 v))

;
; Unsafe blocks

(unsafe
 (rust 
"
let ptr: *const i32 = &42;
"
)
 (rust 
"
*ptr
"
))

## Why

Mostly for fun. I wanted to see what Rust feels like with the syntax stripped away but the type system and borrow checker still there.

Macrosare the obvious practical win: in LISP they're just functions that return s-expressions, running at compile time. No proc_macro, no token streaming. You writedefmacro, you get quasiquote, you're done.

Structural editingis another thing you don't appreciate until you try it. S-expressions are trivially balanced. You can't accidentally leave a brace dangling.

Andthe uniformitygrows on you. Expressions, types, patterns, statements — they all look the same. A function signature uses the same syntax as a match arm. It's less to keep in your head.

## License

MIT

## About

Rust but LISP

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

95

 stars
 

### Watchers

1

 watching
 

### Forks

0

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust100.0%