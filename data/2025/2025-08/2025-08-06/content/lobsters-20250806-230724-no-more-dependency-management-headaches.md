---
title: No more dependency management headaches
url: https://gleam.run/news/no-more-dependency-management-headaches/
site_name: lobsters
fetched_at: '2025-08-06T23:07:24.765138'
original_url: https://gleam.run/news/no-more-dependency-management-headaches/
date: '2025-08-06'
description: Gleam v1.12.0 released
tags: gleam, release
---

05 August, 2025byLouis Pilfold

Share

Gleam is a type-safe and scalable language for the Erlang virtual machine and
JavaScript runtimes. Today Gleamv1.12.0has been published. Let's
take a look at the highlights.

## Understanding dependency conflicts

Gleam packages use semantic versioning, and they specify what ranges of
releases they are compatible with to ensure that all selected versions are
compatible with each other. This is very useful in ensuring that you don't end
up stuck with invalid versions that cause the project to fail to compile, or
are broken in more confusing subtle ways.

This does, however, mean that sometimes you will have conflicts when adding a
dependency, as there's no version which is compatible with the existing
versions you have locked. Historically this has been very confusing as we've
haven't able to display much useful information when this happens.

error
: Dependency resolution failed

An error occurred while determining what dependency packages and
versions should be downloaded.
The error from the version resolver library was:

Unable to find compatible versions for the version constraints in your
gleam.toml. The conflicting packages are:

- app
- wisp
- mist
- gleam_otp
- gleam_json

It's not clear at all what the problem is, or what the programmer might need to
do to resolve the problem. This is not fun for them at all.

Thanks to a lot of hard work from Jak and a new release of the underlyingpubgrubversion solving algorithm
library Gleam will now provide much clearer error messages:

error
: Dependency resolution failed

There's no compatible version of `gleam_otp`:
 - You require wisp >= 1.0.0 and < 2.0.0
 - wisp requires mist >= 1.2.0 and < 5.0.0
 - mist requires gleam_otp >= 0.9.0 and < 1.0.0
 - You require lustre >= 5.2.1 and < 6.0.0
 - lustre requires gleam_otp >= 1.0.0 and < 2.0.0

There's no compatible version of `gleam_json`:
 - You require wisp >= 1.0.0 and < 2.0.0
 - wisp requires gleam_json >= 3.0.0 and < 4.0.0
 - You require gleam_json >= 2.3.0 and < 3.0.0

Version solving is (perhaps unexpectedly) a very difficult problem! This was
not a trivial improvement to make so a huge thank you toGiacomo Cavalieriand the pubgrub library maintainers.

## Major update notifications

Another part of the dependency puzzle is knowing when there is a new major
version of any of the dependencies. Typically Gleam packages permit a range of
minor and patch versions, but not new major versions as according to semver
they have breaking changes, so they may not be compatible.

[dependencies]
lustre = ">= 5.2.0 and < 6.0.0"

When there's a new major version the programmer will need to check if the
package is compatible, and to adjust the code for the new version if
necessary.

To make it easier to understand when this needs to be done thegleam update,
andgleam deps downloadcommands will now print a message when there are new
major versions of packages available. For example:

$ gleam update
 Resolving versions

The following dependencies have new major versions available:

gleam_http 1.7.0 -> 4.0.0
gleam_json 1.0.1 -> 3.0.1
lustre 3.1.4 -> 5.1.1

Thank youAmjad Mohamedfor this!

## Future dependency management improvements

Dependency packages can be extremely useful for being productive when
programming, but great care must be taken with them, both within a single
project and across the wider ecosystem. We want the experience of using
packages to be enjoyable and beneficial, and want to avoid developers getting
stuck in "dependency hell". In the coming releases we will provide new
features that help with managing and auditing dependencies, resolving version
conflicts, and to ensure that code published to the package manager is high
quality and suitable for production use as much as possible.

## Echo messages

Gleam has a convenientechokeyword that is used for quick print-debugging.
Put it in front of an expression and it'll print the value and the source
location to the console. It returns the value it prints, so it can be
inserted anywhere in the code and not change the semantics of the code. There's
even a language server code action for removing allechos from a module once
you are done debugging.

It is now possible to add a custom message to be printed byecho, so you can
add additional information to aid with your debugging.

pub

fn

main
() {

echo

11

as

"lucky number"

}

/src/module.gleam:2 lucky number
11

I've also improved the way thatechodisplays character lists in Erlang, and
circular references and error instances in JavaScript, which should be greatly
useful for folks working with code written in these languages.

Thank youGiacomo Cavalieri!

## Code size reduction

We've made numerous improvements to Gleam's code generation pipeline which have
resulted in the final output being smaller. This is especially impactful when
compiling to JavaScript to be used in a web browser as there's an initial cost
to downloading JavaScript programs, especially on lower power devices or with
poor network connectivity.

Code generated for the record update syntax will now reuse existing variables
when possible, reducing the size of the generated code, the number of
variables, and the number of new scopes defined for both Erlang and JavaScript.
For example:

pub

fn

main
() ->
Nil
 {

let
 trainer =
Trainer
(name:
"Ash"
, badges:
0
)

battle
(
Trainer
(..trainer, badges:
1
))
}

This Gleam code compiled for the Erlang VM would previously generate code like
this:

-spec main() -> nil.
main() ->
 Trainer = {trainer, 0, <<"Ash"/utf8>>},
 battle(
 begin
 _record = Trainer,
 {trainer, 1, erlang:element(3, _record)}
 end
 ).

With v1.12's variable reuse this is generated instead:

-spec main() -> nil.
main() ->
 Trainer = {trainer, 0, <<"Ash"/utf8>>},
 battle({trainer, 1, erlang:element(3, Trainer)}).

In addition to these the code generated for acaseexpression on the
JavaScript target has been reduced in size in many cases, and the previous
release's improved dead-code detection is now use to avoid generating any code
that would go unused in the final program.

These improvements were the work of Surya and myself, thank youSurya Rose!

## More flexible list formatting

Gleam comes with an automatic code formatter, which can be run in an editor
using the Gleam language server, or from the command line withgleam format.
Having a canonical formatter means that all Gleam has the same predictable
style, making it easier to read Gleam code, and removing time consuming debates
about superficial code style.

Previously the formatter wouldn't give the programmer any control over how
lists are formatted, always putting the elements on a single line if they fit
within the column limit, or spreading them over multiple lines if it does not.
With this release the programmer is given more control! If a list would fit on
a single line they can still opt to have it spread over multiple lines.

pub

fn

my_favourite_pokemon
() ->
List
(
String
) {
 [
"natu"
,
"chimecho"
,
"milotic"
]
}

To tell the formatter that this list should be spread over multiple lines a
comma can be added before the], which will cause it to be formatted like so:

pub

fn

my_favourite_pokemon
() ->
List
(
String
) {
 [

"natu"
,

"chimecho"
,

"milotic"
,
 ]
}

By removing the trailing comma the formatter will try and fit the list on a
single line again.

The formatter will also permit the programmer to control whether to have
elements be placed one-per-line, or to try and fit multiple onto a line, and
single empty lines within lists will be preserved. This will greatly help with
large lists that would benefit from being visually segmented into different
parts.

Thank youGiacomo Cavalieri! This change
will be very popular, I'm sure.

## JSDoc support

JSDocis the most widely used format for in-code
documentation in JavaScript, and it is supported by many editors and
programming tools. Documentation comments in Gleam code will now be included in
the output using JSDoc syntax when compiling to JavaScript.

Thank youGiacomo Cavalieri!

## Unreachable import warnings

While not commonly done as it tends to make code harder to read, it is possible
to import a function from another module in an unqualified fashioned, meaning
you don't need to add themodule.prefix when using the function in the
importer module.

If a function or a constant is imported in an unqualified fashion and there is
function or constant with the same name defined in the module then the imported
value will not be accessible at all, making the import pointless. The compiler
now emits a warning in this case, so the programmer can identify and fix the
problem.

Thank youAayush Tripathi!

## Discarded variable hints

The compiler can now tell when an unknown variable might be referring to a
variable that has been discarded with a_prefix, providing an helpful error
message highlighting it. For example, this piece of code:

pub

fn

go
() {

let
 _x =
1

 x
+

1

}

Now results in the following error:

error
: Unknown variable

 ┌─
 /src/one/two.gleam:4:3

 │

3 │
 let _x = 1

 │

-- This value is discarded

4 │
 x + 1

 │

^ So it is not in scope here.

Hint: Change
`_x`
 to
`x`
 or reference another variable

This new error message also shows off the improved format for secondary labels
in warnings and errors, which provide context for the error message. They are
highlighted in a distinct fashion to show they are secondary, and in language
server clients they will be shown as additional information attached to the
diagnostic.

Thank youGiacomo Cavalierifor these!

## Avoiding extra object allocations

It is not uncommon when pattern matching to have case clauses where the pattern
and the clause match exactly. These clauses cause the value to be passed through
unchanged, as can be seen here in theErrorclause of this code.

pub

fn

find_book
() ->
Result
(
Book
,
LibraryError
) {

case

ask_for_isbn
() {

Error
(error) ->
Error
(error)

Ok
(isbn) ->
load_book
(isbn)
 }
}

Previously the generated code for this would construct a newErrorto contain
the pattern matchederrorvalue. With this release the compiler identifies
that the resulting value would be identical to the pattern matched value and
instead reuses that value. It is safe to do this because Gleam is an immutable
language.

Thank youGiacomo Cavalieri!

## Redundant comparison warnings

The compiler now emits a warning when performing a redundant comparison that
it can tell is always going to succeed or fail. For example, this piece of
code:

pub

fn

find_line
(lines) {

list
.
find
(lines,
fn
(x) { x
==
 x })
}

Would result in the following warning:

warning
: Redundant comparison

 ┌─
 /src/warning.gleam:2:17

 │

1 │
 list.find(lines, fn(x) { x == x })

 │

^^^^^^ This is always `True`

This comparison is redundant since it always succeeds.

Thank youGiacomo Cavalieri!

## Helpful import errors for Pythonistas

When learning a new language it can be common to make mistakes with the syntax,
especially with syntax that is similar but not the same as another language the
programmer is more familiar with.

Gleam's module import syntax looks similar to Python's, but it uses/instead
of.in the module name. The compiler now emits a helpful message when this
mistake is made.

error
: Syntax error

 ┌─
 /src/parse/error.gleam:1:11

 │

1 │
 import one.two.three

 │

^ I was expecting either `/` or `.{` here.

Perhaps you meant one of:

 import one/two
 import one.{two}

Thank youZij-IT!

## Helpful list errors for JavaScripters

Similarly a programmer learning a new language may attempt to use a feature
their other language has that their new language does not.

Gleam has a syntax for prepending to a list, which is similar to JavaScript's
array spread syntax, but faster as it doesn't need to allocate a whole new
array and copy the elements across. One big difference to the JavaScript
feature is that it is only for prepending, which can be unexpected for
JavaScript programmers. A helpful error message is now emitted if the
programmer tries to use it to concatenate two lists together.

pub

fn

main
() ->
Nil
 {

let
 xs = [
1
,
2
,
3
]

let
 ys = [
5
,
6
,
7
]
 [
1
, ..xs, ..ys]
}

error
: Syntax error

 ┌─
 /src/parse/error.gleam:5:13

 │

5 │
 [1, ..xs, ..ys]

 │

--
^^ I wasn't expecting a second list here

 │

│

 │

You're using a list here

Lists are immutable and singly-linked, so to join two or more lists
all the elements of the lists would need to be copied into a new list.
This would be slow, so there is no built-in syntax for it.

Thank youCarl Bordum HansenandGiacomo Cavalieri.

## Argument labels hints in errors

The error message emitted when a function is called with the wrong number
of arguments has been improved, it now show the labels for the missing
arguments.

error
: Incorrect arity

 ┌─
 /src/main.gleam:6:3

 │

6 │
 Pokemon(198, name: "murkrow")

 │

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Expected 3 arguments, got 2

This call accepts these additional labelled arguments:

 - moves

Thank youGiacomo Cavalieri!

## Bit array improvements

Gleam has an expressive literal syntax for constructing and pattern matching on
binary data, as is common for languages on the Erlang VM. This syntax is
supported when compiling to JavaScript too.

The endianness of a segment can now be specified when constructing or pattern
matching on UTF codepoints in bit arrays.

Calculations are now allowed in the size options of bit array patterns. For
example, the following code is now valid:

let

assert
 <<size, data:bytes
-
size
(size
/

8

-

1
)
>>
 = some_bit_array

Thank youSurya Rose!

## Erlang local function inlining

When compiling for the Erlang VM the Gleam build tool will use the Erlang
compiler to produce BEAM bytecode for the Gleam code, so Gleam benefits from
all the optimisations that it includes.

One option that is disabled by default is inlining of functions within the same
module. This Gleam release enables it with conservative configuration that
should result in no increase in generated code size. Some BEAM programs will
see a notable increase in performance thanks to this.

Thank youGiacomo Cavalieri!

## Monorepo code links support

Gleam generates and publishes HTML documentation for packages as they are
published to Hex, the BEAM ecosystem package manager. In the documentation
there are links to the code for types and functions, so you can see how they
are defined after you have read their documentation.

To support this Gleam expects a git tag to be added to each published release,
and will help you to do so. However, this system didn't work for monorepos that
contain multiple Gleam projects, as the tags could clash.

Therepositorysection ingleam.tomlnow allows specifying thetag-prefixproperty, which is prepended to the default tag. This prefix allows the
programmer to avoid tag clashes for the different packages in a monorepo

Thank youSakari Bergen!

## CommonJS module support

Some Gleam packages may include JavaScript or Erlang modules which are used
with Gleam's "external function" FFI functionality. With this release you can
now include JavaScript modules with the.cjsfile extension, which enables
use of the CommonJS import system.

Thank youyoshi!

## Remove block code action

The language server now offers a code action to remove blocks that wrap a
single expression. For example, in this code snippet:

case
 greeting {

User
(name:) -> {
"Hello, "

<>
 name }

// ^^^^^^^^^^^^^^^^^^^^^ Triggering the code action


// with the cursor over this block.


Anonymous
 ->
"Hello, stranger!"

}

Would be turned into:

case
 greeting {

User
(name:) ->
"Hello, "

<>
 name

Anonymous
 ->
"Hello, stranger!"

}

Thank youGiacomo Cavalieri!

## And the rest

And thank you to the bug fixers and experience polishers:Aayush Tripathi,cysabi,Giacomo Cavalieri,Louis Pilfold, andSurya Rose.

For full details of the many fixes and improvements they've implemented seethe
changelog.

## A call for support

Gleam is not owned by a corporation; instead it is entirely supported by
sponsors, most of which contribute between $5 and $20 USD per month, and Gleam
is my sole source of income.

We have made great progress towards our goal of being able to appropriately pay
the core team members, but we still have further to go. Please consider
supportingthe projector core team membersGiacomo CavalieriandSurya Roseon GitHub Sponsors.

Thank you to all our sponsors! And special thanks to our top sponsors:

* Aaron Gunderson
* Aayush
* Abel Jimenez
* ad-ops
* Adam Brodzinski
* Adam Johnston
* Adam Wyłuda
* Adi Iyengar
* Adrian Mouat
* Ajit Krishna
* Aleksei Gurianov
* Alembic
* Alex Houseago
* Alex Manning
* Alexander Koutmos
* Alexander Stensrud
* Alexandre Del Vecchio
* Aliaksiej Maroz
* Ameen Radwan
* Andho Mohamed
* Andrea Bueide
* André Mazoni
* Andy Young
* Antharuu
* Anthony Khong
* Anthony Maxwell
* Anthony Scotti
* Arthur Weagel
* Arya Irani
* Austin Beau Bodzas
* Azure Flash
* Barry Moore II
* Bartek Górny
* Ben Martin
* Ben Marx
* Ben Myles
* Benjamin Kane
* Benjamin Moss
* bgw
* Bjarte Aarmo Lund
* Bjoern Paschen
* Brad Mehder
* Brett Cannon
* Brett Kolodny
* Brian Dawn
* Brian Glusman
* Bruce Williams
* Bruno Michel
* bucsi
* Cam Ray
* Cameron Presley
* Carl Bordum Hansen
* Carlo Munguia
* Carlos Saltos
* Chad Selph
* Charlie Duong
* Charlie Govea
* Chew Choon Keat
* Chris Donnelly
* Chris King
* Chris Lloyd
* Chris Ohk
* Chris Rybicki
* Chris Vincent
* Christopher David Shirk
* Christopher De Vries
* Christopher Dieringer
* Christopher Jung
* Christopher Keele
* CJ Salem
* Clifford Anderson
* Coder
* Cole Lawrence
* Comamoca
* Comet
* Constantin (Cleo) Winkler
* Corentin J.
* cysabi
* Damir Vandic
* Dan
* Dan Dresselhaus
* Dan Gieschen Knutson
* Dan Strong
* Danielle Maywood
* Daniil Nevdah
* Danny Arnold
* Danny Martini
* Dave Lucia
* David Bernheisel
* David Coba
* David Cornu
* David Pendray
* Dennis Dang
* dennistruemper
* dependabot[bot
* Diemo Gebhardt
* Donnie Flood
* Dusty Phillips
* Dylan Anthony
* Dylan Carlson
* Ed Hinrichsen
* Ed Rosewright
* Edon Gashi
* Eileen Noonan
* eli
* elke
* Emma
* Emma
* Endo Shogo
* Eric Koslow
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
* Fede Esteban
* Felix
* Fernando Farias
* Filip Figiel
* Fleey
* Florian Kraft
* Francis Hamel
* frankwang
* G-J van Rooyen
* Gabriel Vincent
* Gavin Panella
* GearsDatapacks
* Geir Arne Hjelle
* Georg Hartmann
* Georgi Martsenkov
* ggobbe
* Giacomo Cavalieri
* Giovanni Kock Bonetti
* given
* Graham Vasquez
* Grant Everett
* graphiteisaac
* Guilherme de Maio
* Guillaume Heu
* Guillaume Hivert
* Gunnar Ahlberg
* Hammad Javed
* Hannes Nevalainen
* Hannes Schnaitter
* Hans Raaf
* Hayleigh Thompson
* Hazel Bachrach
* Henning Dahlheim
* Henrik Tudborg
* Henry Warren
* Heyang Zhou
* Hizuru3
* Hubert Małkowski
* Iain H
* Ian González
* Ian M. Jones
* Igor Montagner
* inoas
* Isaac Harris-Holt
* Isaac McQueen
* István Bozsó
* Ivar Vong
* Jacob Lamb
* Jake Cleary
* Jake Wood
* Jakob Ladegaard Møller
* James Birtles
* James MacAulay
* Jan Pieper
* Jan Skriver Sørensen
* Jean Niklas L'orange
* Jean-Adrien Ducastaing
* Jean-Luc Geering
* Jean-Marc QUERE
* Jen Stehlik
* Jerred Shepherd
* Jesse Cooke
* jiangplus
* Jimpjorps™
* Joey Kilpatrick
* Joey Trapp
* Johan Strand
* John Björk
* John Strunk
* Jojor
* Jon Charter
* Jon Lambert
* Jonas E. P
* Jonas Hedman Engström
* JonasGruenwald
* Jonatan Männchen
* jooaf
* Joseph Lozano
* Joseph T. Lyons
* Joshua Byrd
* Joshua Steele
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
* Kritsada Sunthornwutthikrai
* Kryštof Řezáč
* Krzysztof Gasienica-Bednarz
* Landon
* Leah Ulmschneider
* Leandro Ostera
* Lee Jarvis
* Lennon Day-Reynolds
* Leon Qadirie
* Leonardo Donelli
* Lexx
* lidashuang
* Lily Rose
* Lukas Bjarre
* Luke Amdor
* Luna
* Manuel Rubio
* Mario Vellandi
* Marius Kalvø
* Mark Dodwell
* Mark Holmes
* Mark Markaryan
* Martin Fojtík
* Martin Janiczek
* Martin Poelstra
* Martin Rechsteiner
* Mat Warger
* Matt Heise
* Matt Mullenweg
* Matt Savoia
* Matt Van Horn
* Matthew Jackson
* Matthew Whitworth
* Matthias Nüßler
* Max Harris
* Max McDonnell
* metame
* METATEXX GmbH
* Metin Emiroğlu
* Michael Davis
* Michael Duffy
* Michael Jones
* Michael Lynch
* Michael Maysonet
* Michael Mazurczak
* Michael McClintock
* Michal Timko
* Mikael Karlsson
* Mike Roach
* Mikey J
* MoeDev
* MzRyuKa
* n8n - Workflow Automation
* Natanael Sirqueira
* Nathaniel Knight
* NFIBrokerage
* Nick Chapman
* Nick Reynolds
* Nicklas Sindlev Andersen
* NicoVIII
* Nik Revenco
* Niket Shah
* Nikolai Steen Kjosnes
* Ninaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
* NineFX
* NNB
* nnuuvv
* Noah Betzen
* Nomio
* nunulk
* Ocean
* Olaf Sebelin
* OldhamMade
* Oliver Medhurst
* Oliver Tosky
* optizio
* Patrick Wheeler
* Paul Guse
* paul vidal
* Pedro Correa
* Pete Jodo
* Peter Rice
* Philpax
* Qdentity
* Race Williams
* Rasmus
* Raúl Chouza
* re.natillas
* Redmar Kerkhoff
* Reilly Tucker Siemens
* Renato Massaro
* Renovator
* Richard Viney
* Rico Leuthold
* Rintaro Okamura
* Ripta Pasay
* Robert Attard
* Robert Ellen
* Robert Malko
* Rodrigo Álvarez
* Ronan Harris
* Rotabull
* Rupus Reinefjord
* Ruslan Ustitc
* Russell Clarey
* Sakari Bergen
* Sam Aaron
* Sam Zanca
* sambit
* Sammy Isseyegh
* Samu
* Savva
* Saša Jurić
* Scott Trinh
* Scott Wey
* Scott Zhu Reeves
* Sean Cribbs
* Sean Jensen-Grey
* Sean Roberts
* Sebastian Bugge
* Sebastian Porto
* Seve Salazar
* Sgregory42
* Shane Poppleton
* Shawn Drape
* shunom
* Sigma
* simone
* Stefan
* Stefan Hagen
* Steinar Eliassen
* Stephen Belanger
* Strandinator
* SyntacticalAnomaly
* Sławomir Ehlert
* Theo Harris
* Thomas
* Thomas Coopman
* Thomas Crescenzi
* Thomas Ernst
* Tim Brown
* Timo Sulg
* tkanerva
* Tolek
* Tom Hughes
* Tom Schuster
* Tomasz Kowal
* Tomek
* tommaisey
* Tristan de Cacqueray
* Tristan Sloughter
* Tudor Luca
* upsidedowncake
* Valerio Viperino
* Viv Verner
* Volker Rabe
* Walton Hoops
* Weizheng Liu
* Willyboar
* Wilson Silva
* Yamen Sader
* Yasuo Higano
* yoshi~
* zenconomist
* Zij-IT
* zonghan
* Zsombor Gasparin
* ZWubs
* ~1814730
* ~1847917
* ~1867501
* Éber Freitas Dias

Try Gleam
