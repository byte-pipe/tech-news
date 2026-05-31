---
title: Racket v9.2
url: https://blog.racket-lang.org/2026/05/racket-v9-2.html
site_name: hackernews_api
content_file: hackernews_api-racket-v92
fetched_at: '2026-05-31T19:32:42.115775'
original_url: https://blog.racket-lang.org/2026/05/racket-v9-2.html
author: The Unknown Author
date: '2026-05-28'
description: '_posted by Stephen De Gabrielle and John Clements_ We are pleased to announce Racket v9.2 is now available from https://download.racket-lang.org/. As of this release:: The `match` form checks that when non-linear patterns (patterns where the same vari...'
tags:
- hackernews
- trending
---

27 May 2026

posted by Stephen De Gabrielle and John Clements

We are pleased to announce Racket v9.2 is now available fromhttps://download.racket-lang.org/.

## As of this release:

* Thematchform checks that when non-linear patterns (patterns where the same variable is used multiple times) are used with..., the two parts of the matched value actually are equal. Additionally, match rejects non-linear patterns where one use of the variable is used with...and another is not.This repair could cause existing code to fail.
* Typed Racket’s types for theasinandacosprocedures correctly handle situations where the function produces a complex number, avoiding unsound results that were previously possible.This repair could cause existing code to fail at compile time.
* The#%foreign-inlinecore syntactic form provides unsafe access to facilities provided at the linklet layer by a Racket implementation. This means that any code that handles all core forms by enumeration will need to be updated.
* Unicode 17.0 is used for character and string operations.
* This release includes internal support for a more static “ffi2” foreign interface (to be used in a future package).
* Theterminal-file-positionfunction counts bytes written to ports connected to a terminal, such asstdinandstderr.
* Cross-phase persistent modules allow more types ofquoted data.
* The implementations ofmember,memw,when,unless,let/ec, andcondare rewritten to use onlyracket/kernelsyntax
* Theimpersonator-property-predicate-procedure?function identifies procedures created bymake-impersonator-property.
* In Typed Racket, polymorphic struct types are printed using type arguments (e.g.,(Array Byte)) rather than exposing an internal representation.
* The stepper’s display of numbers better matches the language settings.
* Scribble documents that do not use the Racket-manual style get aninitial-scaleof 1.0, instead of the manual style’s 0.8, but this can be configured using theinitial-scaleproperty.
* By default, margin notes appear inline for narrow displays in all styles, not just in the Racket-manual style.
* Big-bang programs distributed as .dmg files correctly handle theclose-on-stopfeature.
* There are many other repairs and documentation improvements!

## Thank you

The following people contributed to this release:

Alexander Shopov, Alexis King, Asilo, Bert De Ketelaere, Bob Burger, Bogdan Popa, Chung-chieh Shan, François-René Rideau, Gustavo Massaccesi, Ilya Klyuchnikov, Jade Sailor, Jamie Taylor, John Clements, Jonathan Simpson, LS_Hower, Matthew Flatt, Matthias Felleisen, Mike Sperber, Pavel Panchekha, Philippe Meunier, RMOlive, Robby Findler, Roman Klochkov, Sam Tobin-Hochstadt, Shu-Hung You, Stephen de Gabrielle, Tejas Sanap, Vincent Lee, and Wing Hei Chan.

Racketis a community developed open source project and we welcome new contributors. Seeracket/README.mdto learn how you can be a part of this amazing project.

## Feedback Welcome

Questions and discussion welcome at the Racket community onDiscourseorDiscord.

## Please share

If you can - please help get the word out to users and platform specific repo packagers

Racket - the Language-Oriented Programming Language - version 9.2 is now available from https://download.racket-lang.org

See https://blog.racket-lang.org/2026/05/racket-v9-2.html for the release announcement and highlights.