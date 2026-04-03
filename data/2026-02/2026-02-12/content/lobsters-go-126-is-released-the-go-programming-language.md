---
title: Go 1.26 is released - The Go Programming Language
url: https://go.dev/blog/go1.26
site_name: lobsters
content_file: lobsters-go-126-is-released-the-go-programming-language
fetched_at: '2026-02-12T06:00:24.309810'
original_url: https://go.dev/blog/go1.26
date: '2026-02-12'
description: Go 1.26 adds a new garbage collector, cgo overhead reduction, experimental simd/archsimd package, experimental runtime/secret package, and more.
tags: go
---

# The Go Blog

# Go 1.26 is released

Carlos Amedee, on behalf of the Go team10 February 2026

Today the Go team is pleased to release Go 1.26.
You can find its binary archives and installers on thedownload page.

## Language changes

Go 1.26 introduces two significant refinements to the languagesyntax and type system.

First, the built-innewfunction, which creates a new variable, now allows its operand to be an
expression, specifying the initial value of the variable.

A simple example of this change means that code such as this:

x := int64(300)
ptr := &x

Can be simplified to:

ptr := new(int64(300))

Second, generic types may now refer to themselves in their own type parameter list. This change
simplifies the implementation of complex data structures and interfaces.

## Performance improvements

The previously experimentalGreen Tea garbage collectoris now enabled by default.

The baselinecgo overhead has been reducedby approximately 30%.

The compiler can nowallocate the backing storefor
slices on the stack in more situations, which improves performance.

## Tool improvements

Thego fixcommand has been completely rewritten to use theGo analysis framework, and now includes a
couple dozen “modernizers”, analyzers
that suggest safe fixes to help your code take advantage of newer features of the language
and standard library. It also includes theinlineanalyzer, which
attempts to inline all calls to each function annotated with a//go:fix inlinedirective.
Two upcoming blog posts will address these features in more detail.

## More improvements and changes

Go 1.26 introduces many improvements over Go 1.25 across
itstools, theruntime,compiler,linker,
and thestandard library.
This includes the addition of three new packages:crypto/hpke,crypto/mlkem/mlkemtest, andtesting/cryptotest.
There areport-specificchanges
andGODEBUGsettingsupdates.

Some of the additions in Go 1.26 are in an experimental stage
and become exposed only when you explicitly opt in. Notably:

* Anexperimentalsimd/archsimdpackageprovides access to “single instruction,
multiple data” (SIMD) operations.
* Anexperimentalruntime/secretpackageprovides
a facility for securely erasing temporaries used in code that manipulates secret
information, typically cryptographic in nature.
* Anexperimentalgoroutineleakprofilein theruntime/pprofpackage that reports leaked goroutines.

These experiments are all expected to be generally available in a
future version of Go. We encourage you to try them out ahead of time.
We really value your feedback!

Please refer to theGo 1.26 Release Notesfor the complete list
of additions, changes, and improvements in Go 1.26.

Over the next few weeks, follow-up blog posts will cover some of the topics
relevant to Go 1.26 in more detail. Check back later to read those posts.

Thanks to everyone who contributed to this release by writing code, filing bugs,
trying out experimental additions, sharing feedback, and testing the release candidates.
Your efforts helped make Go 1.26 as stable as possible.
As always, if you notice any problems, pleasefile an issue.

We hope you enjoy using the new release!

Previous article:Results from the 2025 Go Developer SurveyBlog Index
