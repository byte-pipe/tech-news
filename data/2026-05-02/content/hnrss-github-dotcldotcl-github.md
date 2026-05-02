---
title: GitHub - dotcl/dotcl · GitHub
url: https://github.com/dotcl/dotcl
site_name: hnrss
content_file: hnrss-github-dotcldotcl-github
fetched_at: '2026-05-02T19:55:26.415713'
original_url: https://github.com/dotcl/dotcl
date: '2026-04-30'
description: Contribute to dotcl/dotcl development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

dotcl

 

/

dotcl

Public

* NotificationsYou must be signed in to change notification settings
* Fork1
* Star70

 
 
 
 
master
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

4 Commits
4 Commits
.github
.github
 
 
compiler
compiler
 
 
contrib
contrib
 
 
examples/
windows
examples/
windows
 
 
runtime.docgen
runtime.docgen
 
 
runtime
runtime
 
 
samples
samples
 
 
test
test
 
 
.gitignore
.gitignore
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
DESIGN.md
DESIGN.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
RELEASES.md
RELEASES.md
 
 
View all files

## Repository files navigation

# dotcl

Common Lisp implementation on .NET. Lisp source is compiled to CIL
(Common Intermediate Language) and runs on the .NET JIT — so the same
Lisp image runs on Windows, macOS, and Linux across x86-64 and ARM64
without per-platform porting work.

Broadly conforms to the ANSI Common Lisp standard— verified
against theansi-test suite.

## What dotcl is good for

* Embedding Common Lisp in .NET applications.dotcl.runtimeis a
regular .NET library; you load it from any C# / F# / VB.NET project,
evaluate Lisp code, and call back and forth.
* Writing .NET code in Lisp.Thedotnet:package gives direct
access to .NET types:(dotnet:new "System.Text.StringBuilder"),(dotnet:invoke sb "Append" "x"),(dotnet:static "System.Math" "Sin" 1.0). You can subclass .NET types from Lisp viadotnet:define-class— the compiler emits real .NET classes, so frameworks like MAUI,
ASP.NET Core, and MonoGame just see them as ordinary subclasses.
* Cross-platform CL with NuGet ecosystem access.Any NuGet package
is reachable from Lisp; any Quicklisp library that doesn't rely on
SBCL-only internals tends to work too (asdf, alexandria, etc. are
routinely loaded).

## Quick start

#
 One-time bootstrap: cross-compile dotcl's compiler with Roswell/SBCL.

make cross-compile

#
 Install as a `dotnet tool`-style global command.

make install

#
 REPL

dotcl repl

#
 Evaluate a form

dotcl --eval 
"
(format t 
\"
hello, ~a~%
\"
 (lisp-implementation-type))
"

#
 Run a file

dotcl --load my-program.lisp

After the first cross-compile, dotcl can self-host:DOTCL_LISP=dotcl make cross-compilerebuilds the compiler using dotcl itself.

### Prerequisites

* .NET SDK 10+— see install table below
* Roswell(only for the initial
cross-compile bootstrap — once dotcl is built it can rebuild itself)

#### Installing .NET SDK 10

OS

Command

macOS (Homebrew)

brew install --cask dotnet-sdk

Ubuntu 24.04+

sudo apt install dotnet-sdk-10.0

Debian

add the Microsoft package repository, then 
apt install dotnet-sdk-10.0
 — see 
official guide

Windows (winget)

winget install Microsoft.DotNet.SDK.10

Windows (Scoop)

scoop install dotnet-sdk

Cross-platform script

dotnet-install.sh
 / 
dotnet-install.ps1

Other

https://dotnet.microsoft.com/download

## Samples

Working integrations insamples/:

* MauiLispDemo— a .NET MAUI app (Windows + Android) whereApplication/ContentPage/ view model are all defined in Lisp
viadotnet:define-class.
* AspNetLispDemo— ASP.NET Core controller written in Lisp, with
attribute routing.
* MonoGameLispDemo—Gamesubclass in Lisp; theDrawoverride
runs on the MonoGame frame loop and animates the background colour.
* McpServerDemo— Model Context Protocol server exposing a Lisp
REPL to MCP clients (Claude Desktop, etc.).

Each sample'sREADME.mdwalks through the boot pattern.

## Architecture

* Compiler(compiler/, written in Lisp): transforms S-expressions
into a flat list of CIL instructions (SIL).
* Runtime(runtime/, written in C#): object representation,
reader, CIL assembler (PersistedAssemblyBuilder-based for.fasloutput andReflection.Emitfor in-memory codegen), and the standard
library functions that aren't expressible in pure Lisp.
* Bootstrapis by cross-compile: a Roswell SBCL runscompiler/cil-compile.lispto emitcompiler/cil-out.sil, which the
.NET runtime loads to bring up the Lisp environment. From that point
dotcl can rebuild itself.

Architectural detail and design history are inDESIGN.md. Per-change rationale is recorded underdocs/decisions/.

## Platform notes

* Windows: seedocs/windows.mdfor
installation, encoding (UTF-8 stdin/stdout always), pathname
conventions, and Windows-side .NET interop (Registry / WMI / WinForms
/ MAUI / COM).

## License

MIT. SeeLICENSE.

## About

 No description, website, or topics provided.
 

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

70

 stars
 

### Watchers

2

 watching
 

### Forks

1

 fork
 

 Report repository

 

## Releases2

v0.1.1

 Latest

 

Apr 30, 2026

 

+ 1 release

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C#66.1%
* Common Lisp33.2%
* Makefile0.7%