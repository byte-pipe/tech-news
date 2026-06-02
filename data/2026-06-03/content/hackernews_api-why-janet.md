---
title: Why Janet?
url: https://ianthehenry.com/posts/why-janet/
site_name: hackernews_api
content_file: hackernews_api-why-janet
fetched_at: '2026-06-03T01:51:29.880300'
original_url: https://ianthehenry.com/posts/why-janet/
author: yacin
date: '2026-06-02'
description: 'I never thought it could happen to me. I mean, parentheses? In this day and age? But for the past couple years, my go-to programming language for fun side projects has been a little Lisp dialect called Janet. (print "hey janet") I like Janet so much that I wrote an entire book about it, and put it on The Internet for free, in the hopes of attracting more Janetors to the language. I think you should read it, but I know that you don’t believe me, so I’m going to try to convince you. Here’s my attempt at a sales pitch: here is why you – you of all people – should give Janet a chance.'
tags:
- hackernews
- trending
---

April 12, 2023

# Why Janet?

I never thought it could happen to me. I mean, parentheses? In this day and age? But for the past couple years, my go-to programming language for fun side projects has been a little Lisp dialect calledJanet.

(print "hey janet")

I like Janet so much thatI wrote an entire book about it, and put it on The Internet for free, in the hopes of attracting more Janetors to the language.

I think you should read it, but I know that you don’t believe me, so I’m going to try to convince you. Here’s my attempt at a sales pitch: here is why you –you of all people– should give Janet a chance.

# Janet is simple

Janet is an imperative language with first-class functions, a single namespace for identifiers, and lexical block scoping. The core of the language is very small, consisting of only eight instructions:do,def,var,set,if,while,break,fn. But thanks to macros, there are lots of high-level wrappers that give you more powerful or convenient control flow.

You can “learn” Janet in an afternoon, because the runtime semantics are extremely familiar: think JavaScript, plus value types, minus all the wats. And the rest of the language is small: the entire standard libraryfits on one page. It was this ease of getting started that got me hooked in the first place.

# Janet is distributable

It’s easy to compile Janet programs into native executables that statically link the Janet runtime. And you can share those programs with other people, without asking them to install Janet first – or your project’s dependencies, or anything else for that matter. You don’t even have to tell them it’s written in Janet!

The way that Janet pulls this off is very elegant: Janet compiles itself to bytecode, and then writes that bytecode into a.cfile that also starts up the Janet runtime. Then it compiles that C file with your system’s C compiler. Since Janet is designed to be easy to embed, this makes perfect sense: it is, essentially, embedding itself into a trivial C executable.

A simple Janet “hello world” compiled to a native binary weighs under a megabyte (784K for Janet 1.27.0 on aarch64 macOS, but your mileage may vary). This includes the full Janet runtime, garbage collector, and even the bytecode compiler – so you can write programs that evaluate Janet code at runtime,if you want to.

This makes Janet an excellent choice for writing little command-line apps. Which is especially true when you consider that…

# Janet is unrealistically good at parsing text

Instead of regular expressions, Janet’s text wrangling is based aroundparsing expression grammars. Parsing expression grammars are simpler, more powerful, and more predictable than regular expressions. They aren’t line-oriented, so they can parse multi-line text without a problem. They can also parse HTML, or JSON, or any other non-regular language. They can also parsebinaryfile formats – they have no problems with arbitrary null bytes.

They really areparsers: structured, composable, first-class parsers.And they’re pretty easy to learn!

# Janet has the best subprocess DSL of any high-level language

There is athird-party library calledshthat provides a shell scripting DSL that allows you to express pipes and redirects directly in Janet. Like this:

($ find . -name *.janet | say)

It’s pretty incredible. It’s such a nice DSL thatI dedicated a whole chapter ofJanet for Mortalsto it– and the things that you can do with it. It elevates Janet from a reasonable alternative to Perl to a reasonable alternative toBashfor a surprisingly large range of programs.

# Janet is embeddable

Lua has become the de facto “embedded language,” which is a shame, because… well, this isn’t a post about Lua. You might not care about this very much, but there’s a chance that it’s just because you haven’t tried it yet: being able to writeprogams that expose scripting interfacesis a pretty fun superpower.

Embedding Janet is very easy: the Janet runtime is a small C library, and all you have to do is link it in and then call regular C functions to manipulate Janet values. You can even embed it intowebsites, and writestatic sites with custom programmable DSLs!

# Janet has mutable and immutable collections

Janet’s collection types come in mutable and immutable flavors. Immutable collections have value semantics: the immutable vector[1 2]is indistinguishable from(take 2 [1 2 3]), despite the fact that they have different memory addresses. Mutable collections, on the other hand, have reference semantics: the hash table@{:x 1 :y 2}is only equal to itself. Another hash table with the same keys and values is a distinct object.

Not every language has immutable composite values built right into the standard library!

# Macros, macros, macros

I think this is the real reason you should learn Janet, but I didn’t want to lead with it because I didn’t want to scare you off.

You can write Janet just fine without ever learning how to write macros. But you should learn how, because writing macros isfun. It feels different than any sort of programming that I’ve done before.

Writing macros requires thinking twice at once: you’re writing code to write code, so you have to keep two threads of execution straight in your mind: the code that is running now, at compile time, manipulating values and abstract syntax trees, and the code that you are manipulating, the application code that you produce, the code that will run in the future.

Janet’s macros are not hygienic, and Janet does not have a separate namespace for functions. But by allowing you to unquote literal functions, Janet makes it possible to write macros that are completely referentially transparent. It’s an incredibly simple and elegant solution to anotherwise very delicate problem. And the fact that it is possible to do this in Janet highlights my next favorite feature…

# Janet lets you pass values from compile-time to run-time

This is the most interesting thing about Janet, in my opinion. But it might not sound very interesting at first – really all it means is that any Janet value can be serialized to disk and read back in later.

But this serialization is implicit: when you compile a Janet program, it runs all of the top-level instructions – regular statements, function declarations, whatever – and then, once it’s executed all of the top-level values, Janet writes down a snapshot of your program’s state to disk.

And it’s afullsnapshot of your program’s state: shared references are preserved, so mutable values can still be mutated after you “resume” the snapshot. Generators remember exactly what instruction they need to run the next time you resume them. Closures gonna close.

Macros are a special-case of compile-time code execution – manipulating abstract syntax trees to create new functions – but this is a superpower that you can enjoy without any macros at all. Making a game? Reticulate your splines ahead of time! Or embed assets in your final binary by reading files at compile time – you can perform arbitrary side effects!

Janet for Mortalshas an example of using this to autogenerate database bindings based on a SQL schema file– a bit of a silly example, but something that would be quite difficult to do in most languages.

# Janet feels good in the hand

This is completely subjective, but I love Janet’s syntax. It strikes a perfect balance of simplicity, uniformity, and variety.

It uses pervasive parentheses, but breaks them up with[]for lists and{}for tables.

Mutable literals are always prefixed with@:@"mutable string",{:immutable hash-table}, etc.

Anonymous functions are written(fn [x] (+ 1 x)), but there’s a shorthand notation for lifting any expression into a function with|:|(+ 1 $).

Janet supports “splats” or “spreads” with;:(+ ;args).

String literals can be written with any number of backticks, and closed with the same number of backticks. Escape sequences like\ndon’t apply in backtick-quoted strings, so you can create strings with any contents without ever thinking about how to escape them – all you have to do is wrap them in a sufficient number of backticks.

Rest parameters use&instead of.:(defn foo [first & rest] ...).

Janet doesn’t support reader macros, so the syntax itself is fixed. If you know how to read Janet, you can read all Janet programs. Which is not to say you can make sense of them…

# Janet prefers comfort to tradition

Janet does not adhere to the ancient customs.CARis calledfirst.PROGNis calleddo.LAMBDAisfn, andSETQisdef.nilis not the empty list; it is its own type, and there are first-class Booleans in the language. It eschewsEQ,EQL,EQUAL, andEQUALP. There is nary a linked list in sight.

This isn’t reallygoodorbad, but I thought it was worth calling out: if you saw the parentheses and assumedFORMATwas not far behind, maybe give Janet a second look.

comment on this post
comment via twitter
talk about me on hacker news
Next up ➜ Generalized Macros