---
title: 'ty: An extremely fast Python type checker and language server'
url: https://astral.sh/blog/ty
site_name: hackernews_api
fetched_at: '2025-12-17T11:07:20.411438'
original_url: https://astral.sh/blog/ty
author: gavide
date: '2025-12-16'
description: ty is an extremely fast Python type checker and language server, written in Rust, and designed as an alternative to mypy, Pyright, and Pylance.
tags:
- hackernews
- trending
---

Back to blog

December
 16,
 2025

# ty: An extremely fast Python type checker and LSP

##### Charlie Marsh

@
charliermarsh

TL;DR:tyis anextremely fast Python type checker and
language server, written in Rust, and designed as an alternative to tools like mypy, Pyright, and
Pylance.

Today, we're announcing the Beta release ofty. We now use ty
exclusively in our own projects and are ready to recommend it to motivated users for production use.

At Astral, we build high-performance developer tools for the Python ecosystem. We're best known foruv, our Python package manager, andRuff, our linter and formatter.

Today, we're announcing the Beta release of the next tool in the Astral toolchain:ty, an
extremely fast Python type checker and language server, written in Rust.

0s
20s
40s
ty
Pyrefly
Pyright
mypy
5.32s
19.62s
45.66s
2.19s

Type checking thehome-assistantproject on the command-line, without caching (M4).

ty was designed from the ground up to power a language server. The entire ty architecture is built
around "incrementality", enabling us to selectively re-run only the necessary computations when a
user (e.g.) edits a file or modifies an individual function. This makes live updates extremely fast
in the context of an editor or long-lived process.

0s
1s
2s
ty
Pyright
Pyrefly
370.5ms
2.60s
4.5ms

Re-computing diagnostics in the language server after editing a file in thePyTorchproject (M4).

You can install ty today withuv tool install ty@latest, or via ourVS Code extension.

Like Ruff and uv, ty's implementation was grounded in some of our core product principles:

1. An obsessive focus on performance.Without caching, ty is consistently between 10x and 60x
faster than mypy and Pyright. When run in an editor, the gap is even more dramatic. As an
example, after editing a load-bearing file in the PyTorch repository, ty recomputes diagnostics
in 4.7ms: 80x faster than Pyright (386ms) and 500x faster than Pyrefly (2.38 seconds). ty is very
fast!
2. Correct, pragmatic, and ergonomic.With features likefirst-class intersection types,advanced type narrowing,
andsophisticated reachability analysis,
ty pushes forward the state of the art in Python type checking, providing more accurate feedback
andavoiding assumptionsabout user intent that often lead to false positives. Our goal with ty is not only to build a
faster type checker; we want to build a better type checker, and one that balances correctness
with a deep focus on the end-user experience.
3. Built in the open.ty was built by our core team alongside dozens of active contributors
under the MIT license, and the same goes for oureditor extensions. You can
run ty anywhere that you write Python (including in thebrowser).

Even compared to other Rust-based language servers like Pyrefly, ty can run orders of magnitude
faster when performing incremental updates on large projects.

Your browser does not support the video tag.

Editing a central file in thePyTorchrepository withty(left) andPyrefly(right). ty's incremental architecture is designed to make live updates extremely fast.

ty also includes abest-in-class diagnostic system, inspired by the
Rust compiler's own world-class error messages. A single ty diagnostic can pull in context from
multiple files at once to explain not only what's wrong, but why (and, often, how to fix it).

When assigning an invalid value to a dictionary key,tysurfaces both the type mismatch at the assignment site and the corresponding item declaration.

Diagnostic output is the primary user interface for a type checker; we prioritized our diagnostic
system from the start (with both humans and agents in mind) and view it as a first-class feature in
ty.

When importing an unresolved module,tysurfaces both the unresolved import at the import site and the corresponding Python version configuration.

If you use VS Code, Cursor, or a similar editor, we recommend installing thety VS Code extension. The ty
language server supportsall the capabilitiesthat you'd expect for a modern language server (Go to Definition, Symbol Rename, Auto-Complete,
Auto-Import, Semantic Syntax Highlighting, Inlay Hints, etc.), and runs in any editor that
implements theLanguage Server Protocol.

Following the Beta release, our immediate priority is supporting early adopters. From there, we're
working towards a Stable release next year, with the gap between theBetaandStablemilestones largely focusing on: (1) stability
and bug fixes, (2) completing the long tail of features in thePython typing specification, and (3) first-class
support for popular third-party libraries likePydanticandDjango.

On a longer time horizon, though, ty will power semantic capabilities across the Astral toolchain:
dead code elimination, unused dependency detection, SemVer-compatible upgrade enforcement, CVE
reachability analysis, type-aware linting, and more (including some that are too ambitious to say
out loud just yet).

We want to make Python the most productive programming ecosystem on Earth. Just as withRuffanduv, our commitment
from here is that ty will get significantly better every week by working closely with our users.
Thank you for building with us.

### Acknowledgements#

ty is the most sophisticated product we've built, and its design and implementation have surfaced
some of the hardest technical problems we've seen at Astral. Working on ty requires a deep
understanding of type theory, Python runtime semantics, and how the Python ecosystem actually uses
Python.

I'd like to thank all those that contributed directly to the development of ty, including:Douglas Creager,Alex Waygood,David Peter,Micha Reiser,Andrew Gallant,Aria Desires,Carl Meyer,Zanie Blue,Ibraheem Ahmed,Dhruv Manilawala,Jack O'Connor,Zsolt Dollenstein,Shunsuke Shibayama,Matthew Mckee,Brent Westbrook,UnboundVariable,Shaygan Hooshyari,Justin Chapman,InSync,Bhuminjay Soni,Abhijeet Prasad Bodas,Rasmus Nygren,lipefree,Eric Mark Martin,Tomer Bin,Luca Chiodini,Brandt Bucher,Dylan Wilson,Eric Jolibois,Felix Scherz,Leandro Braga,Renkai Ge,Sumana Harihareswara,Takayuki Maeda,Max Mynter,med1844,William Woodruff,Chandra Kiran G,DetachHead,Emil Sadek,Jo,Joren Hammudoglu,Mahmoud Saada,Manuel Mendez,Mark Z. Ding,Simon Lamon,Suneet Tipirneni,Francesco Giacometti,Adam Aaronson,Alperen Keleş,charliecloudberry,Dan Parizher,Daniel Hollas,David Sherret,Dmitry,Eric Botti,Erudit Morina,François-Guillaume Fernandez,Fabrizio Damicelli,Guillaume-Fgt,Hugo van Kemenade,Josiah Kane,Loïc Riegel,Ramil Aleskerov,Samuel Rigaud,Soof Golan,Usul-Dev,decorator-factory,omahs,wangxiaolei,cake-monotone,slyces,Chris Krycho,Mike Perlov,Raphael Gaschignard,Connor Skees,Aditya Pillai,Lexxxzy,haarisr,Joey Bar,Andrii Turov,Kalmaegi,Trevor Manz,Teodoro Freund,Hugo Polloli,Nathaniel Roman,Victor Hugo Gomes,Nuri Jung,Ivan Yakushev,Hamir Mahal,Denys Zhak,Daniel Kongsgaard,Emily B. Zhang,Ben Bar-Or,Aleksei Latyshev,Aditya Pratap Singh,wooly18,Samodya Abeysiriwardane, andPepe Navarro.

We'd also like to thank theSalsateam (especiallyNiko Matsakis,David Barsky,
andLukas Wirth) for their support and collaboration; theElixirteam (especiallyJosé Valim,Giuseppe Castagna, andGuillaume Duboc), whose work strongly influenced our approach to
gradual types and intersections; and a few members of the broader Python typing community:Eric Traut,Jelle Zijlstra,Jia Chen,Sam Goldman,Shantanu Jain, andSteven Troxler.

Finally, on a personal level, I'd like to highlight the core team
(Alex,Andrew,Aria,Carl,David,Dhruv,Doug,Ibraheem,Jack, andMicha), who created ty
from nothing and pushed it to be great from Day 1.
