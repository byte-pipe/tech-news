---
title: Rhombus v1.0
url: https://blog.racket-lang.org/2026/06/rhombus-v1.0.html
date: 2026-06-23
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-25T05:57:51.753960
---

# Rhombus v1.0

# Rhombus version 1.0 announcement

## Release information
- Date: 22 Jun 2026  
- Install: <https://rhombus-lang.org/download.html>  
- More information: <https://rhombus-lang.org/>  

## Major contributors
Mashfi Ishtiaque Ahmad, Taylor Allred, Nia Angle, Wing Hei Chan, Stephen De Gabrielle, Robert Bruce Findler, Jacqueline Firth, Matthew Flatt, Oliver Flatt, Kiran Gopinathan, Ben Greenman, Siddhartha Kasivajhula, Alex Knauth, Jay McCarthy, Lucas Myers, Alec Mills, Sam Phillips, Sorawee Porncharoenwase, Jens Axel Søgaard, Sam Tobin‑Hochstadt.

## Rhombus goals
- **Approachable syntax** – conventional, non‑parenthesized notation for everyday use.  
- **Racket‑level extensibility** – macro system as expressive as Lisp/Racket while remaining consistent and accessible.  
- **Balance size vs domain fit** – language core stays manageable; extensions tailor the language to specific domains.  
- **Modern language features** – lexical scoping, closures, objects, pattern matching, type parametricity, and a new class system.  

## Frequently asked questions (highlights)

- **What kind of language is Rhombus?**  
  General‑purpose, functional, extensible, dynamic with static constructs; good performance, extensive docs, practical libraries.

- **What makes it different?**  
  Compact repetitions using ellipses (…), default functional data structures with favorable asymptotic complexity, and deep extensibility.

- **Performance** – benchmarks are provided on the website (details omitted here).

- **Getting started** – use DrRacket, Magic Racket for VSCode, or Racket mode in Emacs.

- **Relation to Racket** – built on Racket; a module with `#lang rhombus` is a Rhombus program. It pushes Racket’s multi‑language ecosystem forward.

- **Syntax vs Racket** – new conventional syntax plus improvements: better predefined data structures, pervasive pattern matching, hierarchical namespaces, richer contracts/types.

- **Homoiconicity** – replaces S‑expressions with “shrubbery notation,” an “abicameral” syntax for macros and metaprogramming.

- **Macros and DSLs** – macros are integral but not required; the language supports DSL creation and metaprogramming tasks such as documentation and analysis.

- **Academic vs production** – originated in academia but intended for production use; inherits Racket’s stability and community support.

- **Libraries** – still growing, but benefits from the existing Racket ecosystem.

- **Relevance with AI coding agents** – agents can already generate idiomatic Rhombus code; DSL support remains valuable for both humans and autonomous agents.

## Example Rhombus programs
- Short examples displayed in a carousel on the official site.  
- **Pille** – a language built on Rhombus that uses LLVM as a back end; showcases heavy metaprogramming.  
- **Economancy** – a tabletop‑game implementation (referee, player programs, minimal GUI) written entirely in Rhombus.