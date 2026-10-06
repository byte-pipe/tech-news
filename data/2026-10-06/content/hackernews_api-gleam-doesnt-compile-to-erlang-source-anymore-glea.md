---
title: Gleam doesn't compile to Erlang source anymore | Gleam programming language
url: https://gleam.run/news/gleam-doesnt-compile-to-erlang-source-anymore/
site_name: hackernews_api
content_file: hackernews_api-gleam-doesnt-compile-to-erlang-source-anymore-glea
fetched_at: '2026-10-06T22:54:09.068454'
original_url: https://gleam.run/news/gleam-doesnt-compile-to-erlang-source-anymore/
author: ingve
date: '2026-10-06'
description: 'News post: Gleam v1.19.0 released!'
tags:
- hackernews
- trending
---

05 October, 2026byLouis Pilfold

Share
Copied the post URL!

Gleam is a type-safe and scalable language for the Erlang virtual machine and
JavaScript runtimes. Today Gleamv1.19.0has been published, so
let's go over what's new.

## A new compilation target

Over the last few monthsGiacomo Cavalierihas entirely rewritten Gleam's Erlang code generator that has an entirely
different design, and most notably, outputs a different format. Previously Gleam
generated Erlang source code, now it generatesErlang abstract forms.

"Erlang abstract forms" is an intermediate representation used by the Erlang
compiler. It is a metadata-annotated tree that represents Erlang syntax, and it
is normally produced by running Erlang's tokeniser and parser. It has a binary
encoding using Erlang'sexternal term format,
and with this binary format we can load our generated code directly, skipping
the front-half of the Erlang compiler.

This new Erlang code generator brings several benefits:

* The performance of the compiler has been improved, significantly reducing the
build times for Gleam projects running on Erlang.
* The location metadata available to the runtime is now accurate to original
Gleam source code, rather than to the Erlang source code the compiler would
generate. This means, for example, the line numbers in BEAM crash reports and
stacktraces are perfectly accurate, while previously they could be
inaccurate, only pointing to the nearest function. This metadata could also
enable full support for Gleam in debuggers such asedb,
though we have not done any work on this ourselves.
* The code-quality of the Gleam compiler has been improved. The Erlang code
generator was one of the oldest and most stable parts of the Gleam codebase,
so while it wasn't causing us any problems it wasn't conforming to the
standards and conventions we have today. This new replacement is excellent,
and arguably raising the bar for the compiler as whole.
* We never have to hear someone use the word "transpiler" as a pejorative ever
again.1

## Ok, so how fast is it?

I'm going to show you some numbers in a moment, but please remember that
benchmarks are always contrived and never tell the full story. This data could
be a good introduction or jumping-off point, but a good understanding requires
the person to do further research and experience.

Thebenchmarkis based on José
Valim'slangcompilebenchproject. Thank you José! It is a measure of the time
taken to compile 100 modules that each contain 100 functions that return a
"hello world" string. This is practical as this shape of test project can be
easily replicated across different languages to produce the most like-for-like
test projects, but it is limited in what it can tell us as only a small subset
of the features of each language get compiled. In real projects code will be
greatly more varied, and different features will have different compilation
costs in different languages.

The first stage of the code generator rewrite was released in v1.18.0, the
previous release, so let's compare v1.17.0 to the newly released v1.19.0.
This chart shows the time taken to compile the benchmark project, lower is
better.

0ms
100ms
200ms
300ms
400ms
500ms
Gleam v1.19
Gleam v1.17

As you can see, a considerable improvement! This is a full build from scratch,
without any caching. Gleam's compilation is incremental, so during typical
development it would be much faster as it will not be compiling the entire
project.

The originallangcompilebenchincludes only Erlang, Elixir, and Gleam, but I
have extended it an assortment of other popular programming languages, to help
folks get a rough feel for how fast Gleam compiles compared to a language they
are familiar with. I've also included Gleam when compiling to JavaScript.
Here's the results:

0ms
200ms
400ms
600ms
800ms
1000ms
Gleam (JavaScript)
Go
Gleam (Erlang)
Erlang
Java
Elixir
Elm
Rust
C#
TypeScript 7

Remember: This is a contrived benchmark and is this alone is insufficient to
draw any hard conclusions about these languages. That said, these results
do suggest that Gleam's compilation is nice and fast, and as a Gleam programmer
I can say that Gleam development is very enjoyable, with little time spent
waiting for the computer.

## Why not target BEAM bytecode directly?

We have moved from from compiling from source code that is fed to the Erlang
compiler to an intermediate-representation that is fed into the Erlang
compiler, but why not bypass the Erlang compiler altogether? Couldn't we make a
BEAM bytecode generator that outperforms the Erlang compiler? Perhaps we could
also use Gleam's type information to generate more optimised code too.

While it is possible to achieve these benefits, it's unlikely we would be
able to. Unlike Erlang source and Erlang abstract forms, BEAM bytecode is not
fixed and unchanging. Each new release of the virtual machine can evolve and
improve the bytecode, adding new functionality and sometimes removing
functionality that has been made redundant. We would need to commit to forever
keeping up-to-date with this evolution, working closely with the Erlang
maintainers to be ready for up-coming changes, and to have new versions of
Gleam ready for new releases of the virtual machine. It would also be a
significant effort to reproduce all the existing optimisations that have been
implemented in the Erlang compiler over the decades, even with the help we
might have from Gleam's more capable static analysis.

Gleam is a community project supported bysponsorship.
We have only a fraction of the finances of languages that are
backed by corporations or academic institutions, so we need to think carefully
about the most efficient and sustainable ways to use our resources.
Gleam is a reliable foundation for software development, every decision we make
has to work for years and decades to come. Compiling to Erlang abstract forms
is the cost-benefit sweet-spot for Gleam today.

We're also in great company with this decision. Our much-loved older-sibling
language Elixir also compiles to Erlang via abstract forms. If it's good enough
for Elixir, then it's good enough for Gleam!

Alright, enough about that. There's plenty more in Gleam v1.19.0 to go-over.

## JavaScript decision tree assignment optimisation

It's not just the Erlang code generation that has seen some love, there's some
good improvements for JavaScript too.

In Gleam flow control is done with pattern matching using acaseexpression,
and it gets compiled to nestedifstatements. Because pattern matching is
declarative the compiler is able to reorder and optimise the runtime logic,
using a divide-and-conquer approach to find the right branch as quickly as
possible.

John Downeyhas improved this process to
generate flatter code, with nestedifstatements collapsed into a single
condition and fewer intermediate variables. For example, take this Gleam code:

pub
 
fn
 
go
(x) {
 
case
 x {
 
Wibble
(
1
, 
2
) -> 
1

 _ -> 
2

 }
}

Previously this small bit of Gleam would compile to this surprisingly large bit
of JavaScript2:

export
 
function
 
go
(
x
)
 
{

 
if
 
(
isWibble
(
x
)
)
 
{

 
let
 
$
 
=
 
x
[
0
]
;

 
if
 
(
$
 
===
 
1
)
 
{

 
let
 
$1
 
=
 
x
[
1
]
;

 
if
 
(
$1
 
===
 
2
)
 
{

 
return
 
1
;

 
}
 
else
 
{

 
return
 
2
;

 
}

 
}
 
else
 
{

 
return
 
2
;

 
}

 
}
 
else
 
{

 
return
 
2
;

 
}

}

But now it generates this:

export
 
function
 
go
(
x
)
 
{

 
if
 
(
isWibble
(
x
)
 
&&
 
x
[
0
]
 
===
 
1
 
&&
 
x
[
1
]
 
===
 
2
)
 
{

 
return
 
1
;

 
}
 
else
 
{

 
return
 
2
;

 
}

}

A nice improvement, I'm sure you'll agree! Surprisingly this makes little-to-no
change to the size of code bundles once minified and compressed (gzip really is
magic), but the resulting code has fewer branches for JavaScript engines to
optimise.

Thank you John!

## List literal optimisation

While they share a syntax in their respective languages, Gleam's immutable
persistent list type is not the same as the JavaScript mutable contiguous array
type. When Gleam code is compiled to JavaScript any list literal has to be
compiled to JavaScript code that constructs the runtime data structures. For
example, take this Gleam code:

let
 numbers = [
1
, 
2
, 
3
]

This would compile to JavaScript code2like this, where a JavaScript array is
constructed and passed to a function to convert it to a Gleam list.

const
 
numbers
 
=
 
arrayToList
(
[
1
,
 
2
,
 
3
]
)

With this release the compile will now generate different code for short list
literals, generating more direct code that does not convert from an array.

const
 
numbers
 
=
 
prepend
(
1
,
 
prepend
(
2
,
 
prepend
(
3
,
 
empty
)
)
)

With modern JavaScript engines this results in a nice performance improvement,
and it is especially impactful for projects that use lots of short lists, like
those using theLustrelibrary. We recorded no
improvement for longer lists, so the array-to-list approach is still used for
those.

Thank youGiacomo Cavalierifor this!

## TypeScript API overloads

When compiling to JavaScript the Gleam compiler will also generatefunctionsfor working with the programmer-defined data structures from JavaScript.
Alongside this the compiler can also provide TypeScript declaration files,
enabling full integration between TypeScript and Gleam in a single project.

One of the functions provided for each custom type is a function to check
whether a value is a particular variant or not. For example, given the
following type:

pub
 
type
 
Box
(value) {
 
Full
(value)
 
Empty

}

The generated function would have this TypeScript declaration:

export
 
function
 
Box$isFull
(
value
:
 
any
)
:
 
value
 
is
 
Full
<
unknown
>
;

The keen-eyed TypeScript programmer readers may notice a problem here. If the
value is already known to be of typeBox<number>, then this function can be
used to refine the container type toFull, but the type parameter ofnumberis generalised tounknown, causing type information loss. This is very
cumbersome.

Giacomo Cavalierihas added an overload
to the definition, so the type is preserved whenever possible.

export
 
function
 
Box$isFull
<
I
>
(
value
:
 
Box$
<
I
>
)
:
 
value
 
is
 
Full
<
I
>
;

export
 
function
 
Box$isFull
(
value
:
 
any
)
:
 
value
 
is
 
Full
<
unknown
>
;

Thank you Giacomo!!

## Improvements for other build tools

Gleam users will typically use the official build tool that is part of thegleamexecutable, but sometimes folks will want to compile and use Gleam code
in other contexts. For example, an Elixir or Erlang programmer may want to use
a dependency package that is written in Gleam. This works fantastically at runtime
as these three BEAM languages have excellent zero-cost interop, but getting to
this point can be tricky, as Elixir and Erlang's main build tools do not have
built-in support for Gleam.

Thegleamexecutable offers several commands that expose compiler
functionality, for use by other build tools. This release includes several
improvements to these commands, with the intent of getting Gleam support in
Elixir's Mix and Erlang's rebar3.

The Erlang virtual machine requires all packages too have a.appresource
file along with the compiler bytecode. Previously these Gleam-supporting build
tools would be expected to provide these, but nowgleamwill generate the
files for them when compiling to BEAM.

Thecompile-packagecommand gains a--no-devflag, which will have the
compiler only load code from thesrcdirectory and to skip packages listed asdev_dependencies.

Theexport package-informationandexport package-interfacecommands can
now print their information to stdout, while previously they would have to
write to a file. Alongside that, theexport javascript-preludeandexport typescript-preludecommands can now write to a file.

Thank youRodrigo Álvarezfor these additions!
Hopefully we will see Gleam support in Elixir's Mix build tool soon.

## Language server label support

Gleam has an excellent language server built-in, providing IDE functionality to
all editors that support the language server protocol. Possibly the last piece
of major functionality was full support for labels of fields and arguments.Alistair Smithhas fixed this, adding support for
go-to-definition, find-references and renaming of labels! Thank you Alistair, I
know many people will be absolutely delighted by this time-saving feature.

## Formatting Gleam code in the browser

There is a WebAssembly build of the compiler, used bythe language
tourandthe
playgroundto compile Gleam in the web browser.John Downeyhas added a newformat_sourcefunction, enabling people to run the Gleam code formatter inside the browser.
We will add this functionality to the playground in the near future. Thank you
John!

## As always, better error messages

Making error messages as clear and as helpful as possible is very important to
us. It's all very well for a tool to be nice to use when things are going well,
it is when things are going badly that the experience can really help or hurt
the programmer's stress levels.

Small accidental syntax errors can be a pain, especially if you're not sure
what and where the mistake is.

0xda157has added a special error for when a git
merge conflict marker is found in the code, and another for when theUser(..lucy, score: 10)record update syntax is written with the original
record in the wrong position likeUser(score: 10, ..lucy). She has also added
an errors for procedural operators that do not exist in Gleam, such as+=and*=.

n0kk23has added a custom helpful error message
for when|is used in pattern matching in a way that is not valid syntax in
Gleam, but is valid in other languages, such as Java.

Giacomo Cavalierihas added a helpful
error message for binary operators that are not permitted in constant
expressions, and at the same time he has improved the fault
tolerance3of the compiler in the presence of these mistakes.

Andrey Kozhevhas added extra context to the
error message for when a module tries to use a private type or value from
another module within the same package, letting them know that while it does
exist, it is private. We do not offer this for modules from dependency
packages, to avoid leaking information about code the programmer does not
maintain.

And lastly,James Dolanhas improved the
type checker such that an invalid type alias definition can no longer cause a
cascade of further errors through all usages of the alias.

Thank you all for making Gleam debugging easier and easier.

## And the rest

And thank you to the bug fixers and experience polishers:

0xda157,Amr Kadry,Andrey Kozhev,Giacomo Cavalieri,Hari Mohan,Ian Chamberlain,Jack Programs,John Downey,Lillian Rose,Mar Bloeiman,mmustafasenoglu,Naomi Roberts,Rodrigo Álvarez,Senthilnathan,Surya Rose, andVivid.

For full details of the many fixes and improvements they've implemented seethe
changelog.

## A call for support

Gleam is not owned by a corporation; instead it is entirely supported by
sponsors, most of which contribute between $5 and $20 USD per month, and Gleam
is my sole source of income.

We have made great progress towards our goal of being able to appropriately pay
the core team members, but we still have further to go. Please consider
supportingthe project or core team members.

Thank you to all our sponsors! And special thanks to our top sponsor:

* # <h1>NinaLovesToPutLongTextIntoNameFields.GitHubNamesArePrettyFun(IThinkThereAreOnlyAFewAnnoyingBugsAndOneFormThatStoppedWorkingCompletely).AnywayCheckOutGleam!ItIsAReallyCoolLanguageWithALovelyCommunity.BLM!CovidIsNotOver!TransRightsAreHumanRights!</h1>
* 0xda157
* Aaron Zuspan
* Abel Jimenez
* Aboio
* Adam Brodzinski
* Adam Daniels
* Adam Johnston
* Adi Iyengar
* Adrian Mouat
* Ajit Krishna
* albertchae
* Aleksei Gurianov
* Alex Houseago
* Alex Kelley
* Alex Manning
* Alexander Stensrud
* Alexandre Del Vecchio
* Aliaksiej Homza
* Alistair Smith
* Andrey
* André Mazoni
* Andy Young
* Anthony Scotti
* Antonio Farinetti
* ArcOnyx
* Arthur Weagel
* Arto Bendiken
* Arya Irani
* Atuin
* Barry Moore II
* Ben Martin
* Benjamin Kane
* Benjamin Moss
* bgw
* Billuc
* blurrcat
* Brad Mehder
* Brett Cannon
* Brett Kolodny
* Brian Glusman
* Bruce Williams
* Bruno Konrad
* bucsi
* Caleb Falcione
* Cameron Presley
* Carlo Munguia
* Carlos Saltos
* Chad Selph
* Chew Choon Keat
* Chris Lloyd
* Chris Ohk
* Chris Vincent
* Christian Visintin
* Christopher De Vries
* Christopher Keele
* Clifford Anderson
* Coder
* Cole Lawrence
* Comamoca
* Constantin (Cleo) Winkler
* Corentin J.
* Cyphernil
* dagi3d
* Dan
* Dan Dresselhaus
* Dan Gieschen Knutson
* Dan Piths
* Dan Strong
* Daniele
* daniellionel01
* Daniil Nevdah
* Danny Arnold
* Danny Martini
* Darshak Parikh
* David Bernheisel
* David Cornu
* David Pendray
* Diemo Gebhardt
* Djordje Djukic
* Dylan Anthony
* Dylan Carlson
* Ed Rosewright
* Edgar Gomes
* Edon Gashi
* Eileen Noonan
* Eleina Mironia
* Eric Koslow
* Erik Ohlsson
* Erik Terpstra
* erikareads
* ErikML
* erlend-axelsson
* Ernesto Malave
* Ethan Olpin
* Evaldo Bratti
* Evan Johnson
* evanasse
* Fabrizio Damicelli
* Falk Pauser
* Fede Esteban
* FeiShengWu
* Felix
* Felix Dumbeck
* Filip Figiel
* Florian Kraft
* Francis Hamel
* frankwang
* G-J van Rooyen
* Gabriela Sartori
* Gears
* Geir Arne Hjelle
* Giacomo Cavalieri
* ginkogruen
* Giovanni Kock Bonetti
* Grant Everett
* graphiteisaac
* Greg Burri
* Guflly
* Guilherme de Maio
* Guillaume Heu
* Hannes Nevalainen
* Hans Raaf
* Hari Mohan
* Harry Bairstow
* Hazel Bachrach
* Henning Dahlheim
* Henrik Tudborg
* Henry Warren
* Heyang Zhou
* Hizuru3
* Hubert Małkowski
* Iain H
* Ian Chamberlain
* Ian González
* Igor Montagner
* ImmConCon
* inoas
* Isaac McQueen
* iskrisis
* Ivar Vong
* Jachin Rupe
* Jack Valinsky
* JackProgramsJP
* Jake Cleary
* Jake Wood
* James
* James Birtles
* James MacAulay
* Jan Fooken
* Jan Pieper
* Jan Skriver Sørensen
* Jean Niklas L'orange
* Jean-Adrien Ducastaing
* Jean-Luc Geering
* Jen Stehlik
* Jerred Shepherd
* Joey Kilpatrick
* Joey Trapp
* Johan Strand
* Johanna Larsson
* John Björk
* John Downey
* John Strunk
* Jojor
* Jon Charter
* Jon Lambert
* Jonas E. P
* Jonas Hedman Engström
* jooaf
* Joshua Steele
* jstcz
* Julian Hirn
* Julian Lukwata
* Julian Schurhammer
* Justin Lubin
* Jérôme Schaeffer
* Jørgen Andersen
* KamilaP
* Kemp Brinson
* Kero van Gelder
* Kevin Schweikert
* khalidbelk
* Kile Deal
* Kirill Morozov
* Kramer Hampton
* Kristoffer Grönlund
* Kristoffer Grönlund
* Krzysztof Gasienica-Bednarz
* Kuma Taro
* Landon
* Leah Ulmschneider
* Lennon Day-Reynolds
* Leon Qadirie
* Leonardo Donelli
* Lexx
* lidashuang
* Lillian Rose
* Lukas Bjarre
* Luke Amdor
* Manuel Rubio
* Marius Kalvø
* Mark Holmes
* Mark Markaryan
* Markus Wesslén
* Martin Fojtík
* Martin Janiczek
* Martin Poelstra
* Martin Rechsteiner
* matiascr
* Matt Heise
* Matt Mullenweg
* Matt Savoia
* Matt Van Horn
* Matthew Jackson
* Max Duval
* Max McDonnell
* METATEXX GmbH
* Michael G
* Michael Jones
* Michael Mazurczak
* Michal Timko
* Mikael Karlsson
* Mike Roach
* Mikey J
* Mikko Ahlroth
* MLC Bloeiman
* MoeDev
* Moin
* Mustafa Senoglu
* N. G. Scheurich
* n0kk23
* n8n - Workflow Automation
* Naomi Roberts
* Natalie Rose
* Nessa Jane Marin
* Nick Leslie
* Nick Papadakis
* Nicklas Sindlev Andersen
* NicoVIII
* Nigel Baillie
* Niket Shah
* Nikolai Steen Kjosnes
* Nikolas
* NineFX
* Nomio
* nunulk
* Olaf Sebelin
* OldhamMade
* Oliver Medhurst
* Oliver Tosky
* ollie
* Optizio
* P.
* Patrick Wheeler
* Paul Guse
* Pedro Correa
* Pete Jodo
* Peter Rice
* Philpax
* Qdentity
* R.Kawamura
* Race
* Radmacher
* Rasmus
* Raúl Chouza
* rebecca
* Redmar Kerkhoff
* Reilly Tucker Siemens
* Renato Massaro
* Renovator
* Rico Leuthold
* Rintaro Okamura
* Ripta Pasay
* Rob Durst
* Robert Attard
* Robert Ellen
* Robert Malko
* Rocka Nutrition GmbH
* Rodrigo Álvarez
* Rohan
* Rotabull
* Rupus Reinefjord
* Ruslan Ustitc
* Russell Clarey
* Sakari Bergen
* Sam Aaron
* Sammy Isseyegh
* Savva
* Saša Jurić
* Scott Trinh
* Scott Wey
* Sean Cribbs
* Sean van den Eijnden
* Sebastian Porto
* Senthilnathan
* Seve Salazar
* Sgregory42
* Shane Poppleton
* Shawn Drape
* Shunji Lin
* shxdow
* Sigma
* simone
* Stefan
* Steinar Eliassen
* Stephane Rangaya
* Strandinator
* Sławomir Ehlert
* Thomas
* Thomas Coopman
* Thomas Crescenzi
* Tim Brown
* Timo Sulg
* Tobias Ammann
* Tomas Vemola
* Tomasz Kowal
* tommaisey
* Tristan Sloughter
* Tudor Luca
* upsidedowncake
* Vassiliy Kuzenkov
* Viv Verner
* Vivid
* Volker Rabe
* vshakitskiy
* Will Ramirez
* Willow (GHOST)
* Xucong Zhan
* Yamen Sader
* Yasuo Higano
* ZWubs
* ~1814730
* ~1847917
* ~1867501
* Éber Freitas Dias

Try Gleam

1. "Transpiler" means a compiler that outputs a human-readable
format, such as source code. It's a cool sounding word, but most the time
people use it to imply that a given compiler is in some way inferior. This
is very silly, as there is nothing about compiling to a human-readable format
that makes a compiler easier to implement. If you care about that output
being nicely formatted it might even be harder than using a binary format.↩︎
2. The code has been slightly edited for clarity, but the parts
related to this improvement are unchanged.↩︎
3. Gleam's compiler is the heart of the Gleam language server,
so unlike traditional compilers it needs to be able to provide information
about code even when it is in invalid state. If only valid code could be
fully analysed then the language server would provide a degraded experience
to the programmer when they are half-way-through a refactoring or other large
edit.↩︎