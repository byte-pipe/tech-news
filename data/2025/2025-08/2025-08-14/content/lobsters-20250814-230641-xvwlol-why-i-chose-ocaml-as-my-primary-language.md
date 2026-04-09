---
title: xvw.lol - Why I chose OCaml as my primary language
url: https://xvw.lol/en/articles/why-ocaml.html
site_name: lobsters
fetched_at: '2025-08-14T23:06:41.166726'
original_url: https://xvw.lol/en/articles/why-ocaml.html
author: xvw, Xavier Van de Woestyne
date: '2025-08-14'
description: A detailed explanation of why I chose OCaml as the ‘default’ programming language for every project.
tags: ml, plt, programming
---

# Why I chose OCaml as my primary language

 2025-08-13


 This article is a translation, the
original version is
 available here
.

I started using theOCamllanguage regularly around 2012, and since then, my interest and enthusiasm for this language have only grown. It has become my preferred choice for almost all my personal projects, and it has also influenced my professional choices.
Since 2014, I have been actively participating in public conferences dedicated to programming and software development, where I often express my enthusiasm for OCaml in ways that may be a bit over the top (but always passionate). This has earned me, in a friendly way, the nicknameOCaml evangelist— a title that, I admit, I find very flattering.
Moreover, I’m not alone in thinking this. Despite the common misconception that OCaml wouldn’t be a pragmatic choice for industry, major companies such asMeta,Microsoft,Ahref,Tarides,OCamlPro,Bloomberg,Docker,Janestreet,Citrix,Tezos, andmany othersactively use it.

* ForewordOther resources
* Other resources
* OCaml as a languageOn static type checkingFeatures of the languageA multi-paradigm languageSyntax à la MLClosely related to researchAlgebraic typesModular programming and module languageDependency injection and inversionThrough modulesThrough user-defined effectsRegarding the futureWeaknessesTo conclude on language
* On static type checking
* Features of the languageA multi-paradigm languageSyntax à la MLClosely related to researchAlgebraic typesModular programming and module languageDependency injection and inversionThrough modulesThrough user-defined effects
* A multi-paradigm languageSyntax à la MLClosely related to research
* Syntax à la ML
* Closely related to research
* Algebraic types
* Modular programming and module language
* Dependency injection and inversionThrough modulesThrough user-defined effects
* Through modules
* Through user-defined effects
* Regarding the future
* Weaknesses
* To conclude on language
* OCaml as an ecosystemCompilation, runtimes, and additional targetsA quick detour via MirageOSThe OCaml platformOPAM, the package managerDune, the build-systemOn the choice of S-expressionsContribution to the state of the art: Selective Applicative FunctorAlternativesLSP and Merlin for editorsThe advent of VSCode, LSP as standardOdoc, the documentation generatorAvailable librariesSide note on the standard libraryEcosystem Conclusion
* Compilation, runtimes, and additional targetsA quick detour via MirageOS
* A quick detour via MirageOS
* The OCaml platformOPAM, the package managerDune, the build-systemOn the choice of S-expressionsContribution to the state of the art: Selective Applicative FunctorAlternativesLSP and Merlin for editorsThe advent of VSCode, LSP as standardOdoc, the documentation generator
* OPAM, the package manager
* Dune, the build-systemOn the choice of S-expressionsContribution to the state of the art: Selective Applicative FunctorAlternatives
* On the choice of S-expressions
* Contribution to the state of the art: Selective Applicative Functor
* Alternatives
* LSP and Merlin for editorsThe advent of VSCode, LSP as standard
* The advent of VSCode, LSP as standard
* Odoc, the documentation generator
* Available librariesSide note on the standard library
* Side note on the standard library
* Ecosystem Conclusion
* On the community
* Some myths about OCamlOCaml and F#Doubled operators for floatsOn the separation between ml and mliEncapsulation without mliExpressing the interface from mlTo conclude on separation
* OCaml and F#
* Doubled operators for floats
* On the separation between ml and mliEncapsulation without mliExpressing the interface from mlTo conclude on separation
* Encapsulation without mli
* Expressing the interface from ml
* To conclude on separation
* Conclusion

In thisopinion piece, I will try to briefly share my encounter with
the language and list its advantages — organized into several sections
coveringthe language itself, its ecosystem, and its community. I
will also attempt todebunksome popular myths (or misconceptions)
found on the Internet. For the sake of transparency, it is important
to note that, at the time of writing, myprofessional
workinvolves working for and on the OCaml
ecosystem. However, readers who have followed me for several years
can attest that I was promoting the language long before I was paid to
work on the OCaml ecosystem,sometimes rather immoderately.

## Foreword

First, this article will explain why Ipersonallybelieve that
OCaml is a relevant choice in many contexts. My goal is not
specifically to convince you—although that would be a very welcomeside effect— and it’s quite likely that many of the arguments I
present will also apply to other languages!

Also, very often, when I suggest OCaml to people who want to explore
new languages or try out solutions written in OCaml, I’m kindly told
thatI’m always promoting OCaml. It’s amusing to notice that when
the suggestions involve languages adoptedby default, like
JavaScript, or more recent ones likeRustorGo, they tend
to trigger fewer reactions. This is probably because peopleimplicitlyassume that proposing alesser-knownlanguage leans
toward irrationality and personal preference. From my point of view,suggesting OCaml is, in many cases where fine-grained memory control
is not needed, just as relevant as suggesting Rust(and probably
more so).

To wrap up this preface, many people first encountered OCaml (orCaml
Light) during their
undergraduate studies or in preparatory classes, often using it in
contexts far removed from industry. As for me, I started getting
interested in OCaml much earlier, thanks to theSite du
Zéro, where a small community of functional
programming enthusiasts promoted lessmainstreamlanguages likeOCaml,Erlang, andHaskell. My interaction with OCaml at
university wasjust a bonus.

### Other resources

I’m not the first to document the reasons for choosing OCaml. There
are many other resources that, in my opinion, are also worth checking
out, and they show that OCaml users are generally very satisfied — so
much so that they’re motivated to sharehow and whywe chose the
language as our main technology:

* "Why
OCaml?",
the prologue of the bookReal World
OCaml, which presents
factual advantages of using OCaml (and whose introduction includes a
timeline). While the book is excellent in many respects, I’ve gotten
into the habit of not recommending it because I find its usage
approach quite biased, suggesting libraries by default that aren’t
necessarily widely accepted in the community.
* "Better Programming Through
OCaml",
the prologue of the book (accompanied by videos)OCaml Programming:
Correct + Efficient +
Beautiful, which
mainly explains how learning OCaml can improve a developer’s skills
in other, more popular technologies. The book is fairly recent, and
it’s the one Inow recommend as the go-to resourcefor getting
started with OCaml.
* Talk: "Why
OCaml?", a
presentation byYaron Minsky, CTO ofJane Street—an industrial user of
OCaml and one of the global leaders in finance. Yaron is also one of
the authors ofReal World OCamland the originator of the widely
quoted phrase in the statically typed programming languages world,
"Make illegal states unrepresentable". The talk offers plenty of
insights into Jane Street’s motivations for choosing OCaml.
* "OCaml for Fun & Profit: An Experience
Report", presented
byTim McGilchristatYow
2023. After a rich introduction
to the language, it covers some very concrete use cases of OCaml in
production —with fun and profit.
* "Replacing Python for
0Install"byThomas Leonard. This series of
articles is, in my view,incredibly interesting. The author of0Install, a decentralized, cross-platform
software installation system (a slightly older alternative toNix), was looking for a language other thanPythonfor a new version’s implementation
(the reasons for replacing Python are alsodocumented
here)
and carried out a thorough, methodical comparison of several
candidates:ATS,C#,Haskell,Go,Rust, andOCaml,
alongside Python. Years later, I’m still impressed by the rigor and
nuance of this series, which Ihighly recommend.

There are probably other resources and testimonials, notably on theofficial website, which features bothindustrialandacademiccase studies. There are
also articles expressing the frustration OCaml can cause. I’m aware
that OCaml is not perfect—nor do I believe any technology is
perfect. I’ll likely refer to some of these articles (implicitly or
explicitly) in the section onmythsand in the conclusion, where
I’ll try to explain in which contexts I don’t find OCaml to be a
relevant choice.

## OCaml as a language

Before diving into thefeaturesoffered by the language, I’d like
to start with a point that I believe is essential. OCaml is a
programming language that originated fromresearchand is used byindustrial
users. This duality is important
because it provides the language with two key advantages:

* Guidance ondesirablefeatures as interesting language concepts,
supported by advanced research. For example, to my knowledge, OCaml
is the firstmainstreamlanguage to offer native support foruser-defined effects,
which is the result of cutting-edge research, illustrated by
numerouspublications.
* Guidance ondesirablefeatures as tools for industrialization,
also backed by research and motivated by practical use cases. For
instance, recently,Jane Street, a
major industrial OCaml user, proposed the integration ofaffine
sessions, enablinglinear resource
management(somewhatRust-like).

This intertwining of industrial and academic motivations allows OCaml
to offer a collection of solid, useful, and well-defined features. In
other words, OCaml is alivinglanguage, and since I’ve been using
it, I’ve witnessed many developments and additions that I consider
highly desirable and thatdebunka common assertion against OCaml:the language is only useful for theory or for implementingCoq/Rocq.

Although this was historically true, the motivations provided by
industrial users justify the label "An industrial-strength functional
programming language with an emphasis on expressiveness and safety."
The opening keynote of theOCaml Workshop
2021byXavier
Leroy, titled "25 Years Of
OCaml," presents
an exhaustive timeline of OCaml’s continuous design, showing the
various phases of evolution the language has undergone.

In broad terms, OCaml is a programming language from theML
family,high-level(here, meaning it featuresgarbage
collection),statically typed(types are checked at compile time with no
implicit conversions), withtype
inference(also
calledtype synthesis), allowing the compiler to deduce the type of
an expression in most cases. This enables programming in bothfunctionalandimperativestyles.

OCaml also provides anobject-oriented programming modeland a
very richmodule system. The language has two compilation schemes:ocamlc, which compiles to abytecodeexecutable by avirtual
machine(portable and efficient), andocamlopt, which compiles tonative machine code(runnable on a widevariety of
architectures).

Moreover, OCaml allowsconversion of its bytecode to JavaScriptusingJs_of_ocaml,
enablingvery fastinteroperability within the OCaml ecosystem
(which I useextensivelyon this website). Thesame approach is
used to produce
WebAssembly. For deeper
interoperability with the JavaScript ecosystem,Melangetakes a somewhat different approach
than Js_of_ocaml to generate robust JavaScript.

OCaml is ahighly versatilelanguage, and I will now try to
present the features and strengths that make it —for me— an ideal
tool for building both personal and professional projects, starting
with a brief detour into static typing.

### On static type checking

When I was preparing, withBruno, the
episode ofIf This Then Devdedicated to OCaml — which, in the end, wasrecordedwithDidier— he asked me a question
that I found surprising:

“Is it really worth bothering with types when working on apersonal
projectquickly? Even though I can perfectly see the value forproductioncode, for apersonal projectit seems like a waste of
time to me.”

I think there are two main angles to answer this. The first, and most
obvious, is that,in principle, I don’t see why a personal project
should be any less disciplined than a professional one. When I write
softwarefor myself, I could indeed get away with ignoring thecorner casesof my implementation. Sure, that’s possible. But that’s
probably not what I actually want to do. So, if a language and its
compiler let me set up safety nets that force me to account for all
the cases in my software,I take them— just like writingunit
testsmakes development easier, and I don’t see them as a
constraint.

But beyond considerations of hygiene in a personal project, I think
the negative reputation of static type checking usually stems from a
bad experience. Indeed, in languages like C or Java, types aremostly a constraintthat can be easily circumvented. In languages
that place a strong emphasis on typing — likeOCaml,Haskell,F#,Scala, orRust—types act as safeguards. More
importantly, in my view,types also serve as a tool for expressivedesign. Using them provides safety while also offering an
incredibly rich, versatile, and concise way to describe data.

From my experience, even though it’s common to move from apoorly-typed(sorry, the temptation is too strong) to adynamically
typedlanguage — I, for instance, happily transitioned from Java to
Ruby — moving from a language with a rich type system, like OCaml or
Haskell, makes switching to adynamically typedlanguage much
harder. At present,I don’t know anyone who has seriously used
languages like OCaml or Haskell and was happy to return to languages
with less sophisticated type systems(though an interesting project
can sometimes justify such a technological regression).

This isnot just a personal observation; static type checking is
central to the broader debate about the evolution of programming
languages. Historical languages evolve (or attempt to evolve) to
integrate more type checking. For instance,Erlang, as early as the 1980s (before its
compiler source was released), experimented withintegrating a type
system. Java,
version by version, enhances features aimed at improving static type
verification, such as incorporatingsealed
families.

Many languages are experimenting with type systems:Ruby with
RBS,Crystal(a statically typed language
heavily inspired by Ruby),Python with Mypy,Elixir(which revisits Erlang’s past experiments, offering a viable gradual
typing approach), and, of course,TypeScript, which has becomewidely adoptedin the JavaScript community.

While all these initiatives are encouraging and clearly move in the
right direction, for now, they primarilyadd safeguardsbut do not
yet serve as expressivedesign tools.

When it comes to increasingly rich type systems,the White Houserecently published areportemphasizing the importance ofmemory safetyin software design and…endorsingthe use of theRustlanguage
(historicallywritten in
OCamlbefore becomingself-hosted) over C++, clearly showing that even
official bodies (often considered outdated) highlight the value of
rich type systems. Moreover, theresponse from
Tarides,
the company I work for at the time of writing this article, also
presents compelling arguments in favor of using OCaml for building
critical systems.

In conclusion, static type checking is really valuable and highly
recommended, and it’s worth exploring languages with sophisticated
type systems (like OCaml) and, why not, going even further by
increasingly delving into formal methods.

### Features of thelanguage

Even though it’s very tempting to create a massive OCaml tutorial, the
goal of this section is to present what makesOCaml,for me, ahighly relevantchoice for both learning and production. The
advantages will therefore be presented (anddefended), butthis is
not a tutorial.

#### Amulti-paradigmlanguage

Nowadays, talking aboutmulti-paradigmlanguages might seem
unnecessary, since a large majority of programming languagesfavored
by industryare already multi-paradigm. However, OCaml is afunctional programminglanguage that also supportsimperative
programming,modular programming,object-oriented
programming, and, since version5.0.0,multi-core programming.

Just asHaskellis widely recognized in
the functional programming world, it’s often assumed that adding
imperative mechanisms to a language is a bad idea — especially if one
is convinced of the benefits of the functional style. From my
perspective, there are several perfectly legitimate reasons to use
imperative programming when the language allows it:

* Readability of an implementation.Sometimes, avoiding mutability
requires adding extra plumbing (for example, aState
Monad), which can make
reading and understanding a program more cumbersome.
* Performance.Adding such plumbing can introduce overhead, making
the execution of implementations more costly.
* Ease of use.A few years ago,Arthur
Guillonceremoniously told me that
"OCaml is a lambda calculus that trivially allows effects," which
makes it very effective for tasks like debugging, where printing
messages to standard output is simple. While I acknowledge that this
is probably not thebest wayto implement logging, it undeniably
provides a comfortable user experience and enables rapid
prototyping.

In general, OCaml's dual nature — both imperative and functional —
allows you to leverage the advantages of both paradigms in different
situations and, of course, to combine them. For example, hidding a
module's imperative nature behind a functional API.

##### Syntaxà la ML

Although syntax is often considered a minor detail, languages in theML
familyhave a concise, expressive, and readable syntax. Even thoughthis
family of syntaxcan be confusing when coming from more conventional,
C-inspired syntax, one gets used to it fairly quickly and can soon
realize that it is very consistent and relatively
unambiguous. However, if OCaml’s syntax is problematic for you, don’t
hesitate to look intoReasonML, an
alternative syntax that uses braces.

##### Closely related to research

OCaml is a language that originates from French research, as shown by
thehistory of Caml,
primarily designed to implement the proof assistantCoq/Rocq. This origin — and the initial
motivations, implementing Coq while also serving as a programming
language taught in preparatory classes—creates a certain duality:

* The core features were not initially designed with industry in
mind. However, this assertion is no longer true, primarily because
OCamlhasbecome a language used in industrial contexts. While
in the language’s genesis, there were more tools for building a
language itself (facilitating the teaching of compiler mechanisms)
than tools for building "enterprise" applications, projects from the
community motivated by industrial use have enriched the language and
its ecosystem, making it a versatile tool suitable for industry. For
example, creating abindingwith theTklibrary led to
the integration in the language ofnamed
arguments,optional
arguments,
andpolymorphic
variants.
* The set of paradigms and language features arecarefully thought
out and well-theorized. Generally, the integration of a feature
(or collection of features) results from meticulous research, based
on solid theoretical foundations and reviewed by numerous experts in
the field (oftenrecognizedby the scientific community). This rigor can sometimes slow the
introduction of new features but generally ensures their proper
functioning and theoretical stability.

This theoretical rigor, stemming from OCaml’s undeniable closeness to
the research world, means that its various aspects are well
documented, illustrated bya large number of
publications,
and exhibitpredictable behavior. From my point of view, this
makes OCaml a very wise choice for understanding these different
featuresin depth. For example, I believe OCaml has allowed me tomuch better understandcertain traits or paradigms of programming
languages.

Moreover, a great example of how meticulous and rigorous research can
support the integration of a language feature is OCaml’s
implementation of anobject
model. Indeed, the
thesis ofJérôme Vouillon,Design
and Implementation of an Extension of the ML Language with
Objects, proposes
an innovative object model that integrates very well with type
inference byseparating the notions of inheritance and
subtyping— inheritance being asyntactic notionand subtyping asemantic
notion— usingrow
polymorphismto
describestructural subtyping
relationships,
as opposed tonominal
subtyping, used by
Java, C#, and most popular OOP languages. OCaml’s object model fully
adheres to theSOLID principleswithout anyadditional
ceremony.

#### Algebraic types

I’ve been quite expansive about the reasons why I value a language
with static type checking. However, in my experience, for a statically
typed language to be truly usable, the presence ofalgebraic
typesis necessary:

* Product types: These allow grouping values of heterogeneous
types (thus creating aconjunctionof heterogeneous types). They
are generally present in allmainstreamlanguages (for example,objects, which introduce additional concepts, or tuples and
records).
* Sum types: These allow constructing adisjunctionof
heterogeneous value types, with differentcasesindexed by
constructors. While somespecial casesof sums exist in mainstream
languages—likebooleans(which are a disjunction of two cases:trueandfalse, i.e., two parameterless constructors) — support
for full sum types is often cumbersome in popular languages. For
example, Kotlin and Java (andde factoC#) use a construct
associated with inheritance relations calledsealing. The
integration ofdedicated sum type
syntaxalso took some time in Scala, which, prior to recent versions,
relied on sealed families, making the expression of sums verbose
and, in my view, harder to reason about.
* Exponential types: These allow describing functions that express
types for higher-order functions (functions that can be passed as
arguments or returned as results).

Coupled withpattern
matchingandparametric
polymorphism(orgenerics), an algebraic type system is an incredibly expressive
tool for describing data structures, the state machine of a program,
or modeling abusiness
domainwith an appropriate cardinality. Even in the 21st century, where
products and exponentials are common, when I usevery popularlanguages, I am often frustrated by the lack of sum types, which
forces me to use verbose encodings (increasing the domain’s
cardinality). This is particularly noticeable when working withGoandTypeScript.

The appeal of this triad is, in fact, probably one of the reasons
(combined with a very ergonomic ecosystem and toolchain) behind the
success ofRust. In short, if you intend
to build a new programming language with static type checking,please, do not hesitate to include algebraic types!

Finally, there are aspects of OCaml's type system that I haven’t
covered, but which probably deserve dedicated articles. For example,generalized algebraic data types
(GADTs), which allow
expressing even more invariants.

#### Modular programming and module language

OCaml, through its ancestorCaml
Light, was among
the first languages to offer a module system, similar toStandard
ML, providingencapsulation and
abstractionwhile supportingseparate compilation, in the style
ofModula-2. OCaml’s module
system is afundamental aspectof the language, although its
complexity can be intimidating. Indeed, in OCaml, it is possible to
clearly distinguish the interface (thesignature) from the
implementation (thestructure), thus facilitating encapsulation and
documentation, while also allowingfunction application within the
module language.

I find it particularly difficult to address the topic of modules
briefly (it’s a subject I’ve wanted to explore on my blog foryears). However, here is a list of advantages I see in OCaml’shighly modularapproach:

* Separate compilation: A key feature that allows efficient
compilation of large programs by identifying junction points to
optimize parallel and incremental compilation. This approach is
leveraged bydune, the recommended build
system for OCaml.
* Systematic separation of implementation and interface: Offers
several significant advantages, including encapsulation and placing
documentation in the interface. In my programming workflow, I find
this very convenient because I can implement mystructure(the
module’s implementation) whilebeing guided by type inferenceand
specify its API in thesignature(the module’s interface),
deciding on the display order and providing clear documentation that
doesn’t pollute the implementation space. Additionally,
encapsulation allows me to freely define intermediate types inside
the structure, for example, to represent a program’s state machine,without letting it
escape.
* A powerful tool for describing data structures: By abstracting
types (hiding their implementation) and combining this with
encapsulation, it is possible to describe data structures thatmaintain invariants. This is why it is common to have a
structure/signature pair for each data structure, hiding
implementation details through abstraction and encapsulation.
* Reusability and sharing: Just as it is possible to describe
types in the value language (as seen with algebraic types), it is
also possible to describe types in the module language, calledtranslucent signatures, which allow defining the type of a
signature without associating it with a structure. These signatures
are structurally typed, and coupled withfunctors(functions in the module
language), it is possible toshare behaviorbetween modules.
* Advanced forms of polymorphism: IncludingHigher Kinded
Polymorphism,
available in the module language. In broad terms, you can describe
"generics parameterized by generics". This limitation in languages
like F# or Java often motivates the use ofheavy
encodingsto work around the lack.

The theory behind module languages in ML-family languages is a vast
subject,still evolving, and
very difficult to summarize in a single paragraph. However, the
introduction ofDerek Dreyer’s
thesis,Understanding and Evolving the ML Module System, provides an
excellent explanation of the purpose and use of modules, illustrated
with many examples. I hope to take the time in the coming weeks or
months to write more extensively about the module language than I havealready attempted, because it could
be very educational and, in my view, the topic is extremely
interesting!

#### Dependency injection and inversion

Briefly touching on object-oriented programming in OCaml, I mentioned
that OCaml allows, through its language features, a straightforward
way to meet the prerequisites for writingSOLIDcode. The final
point I’d like to emphasize is the ease of dependency inversion,
achievable throughlanguage-provided features. In broad terms, the
principle of dependency inversion involves describing dependency
lattices usingabstractionsrather thanimplementations. This
way, dependencies can beinjected afterward— making context
changes, for example in unit testing, trivially implementable.

OCaml provides (at least) two tools that facilitate this inversion,
each useful in different contexts. We will draw inspiration from the
very popular teletype example to show how to invert dependencies:

let

program

()

=


let

()

=

print_endline

"
Hello World
"

in


let

()

=

print_endline

"
What is your name?
"

in


let

name

=

read_line

()

in


print_endline

(
"
Hello
"

^

name
)

Even if it might not seem obvious, this program depends onconcrete
implementations— namely, interactions with standard input and
output.

##### Through modules

The most straightforward approach is to use modules, either asfirst-class valuesor by construction, usingfunctors. The duality between
signatures and structures makes dependency inversion obvious. For
example, to revisit our example, here’s how, usingfirst-class
modules, it becomesvery easyto depend on an abstract set of interactions. We start
by describing the abstract representation of possible interactions:

module

type

IO

=

sig


val

print_endline
 : string -> unit


val

read_line
 : unit -> string

end

We can now expect ourprogramfunction to take a module of typeIOas an argument (we’ll call thisa handler) and use the functions
exported by the module, which in our example is namedHandler:

let

program

(
module

Handler
:

IO
)

=


let

()

=

Handler
.
print_endline

"
Hello World
"

in


let

()

=

Handler
.
print_endline

"
What is your name?
"

in


let

name

=

Handler
.
read_line

()

in


Handler
.
print_endline

(
"
Hello
"

^

name
)

For example, in the context of unit testing, it’s possible to provide
an implementation that logs all the operations called (andmockstheread_linecall to fix the returned result). This makes expressing
unit tests thatverify business logicvery easy to implement.

Passing a concrete implementation as an argument to our function
amounts tointerpreting the program.

##### Throughuser-defined effects

OCaml version 5 arrived with a host of new features. However, the
biggest advancement is the complete redesign of the OCamlruntimeto support multi-core execution. There are several ways to describe
concurrent algorithms — for example, usingactorsorchannels. OCaml has chosen
to rely oneffects,
which simplify the management of the program'scontrol flow. In
fact, OCaml allows users to define their own effects, logically calleduser-defined effects. While
they are a powerful tool for describing concurrent programs, they also
make it easier to inject dependencies when you want to maintain
control,at the handler level, over the execution flow of a program.

Note: In my example, I am using an experimental syntax,just
mergedinto the OCaml
main branch, which will likely be available in version5.3.0of
the language.

As with our previous improvement, we first need to describe the set of
operations that can be performed. We use theeffectconstruct:

effect

Print_endline

:

string

->

unit

effect

Read_line

:

unit

->

string

Next, we can write our program in a direct style, byproducing
effects:

let

program

()

=


let

()

=

Effect
.
perform

(
Print_endline

"
Hello World
"
)

in


let

()

=

Effect
.
perform

(
Print_endline

"
What is your name?
"
)

in


let

name

=

Effect
.
perform

(
Read_line

()
)

in


Effect
.
perform

(
Print_endline

(
"
Hello
"

^

name
)
)

It is then possible tointerpret our program afterward, using a
construction similar to pattern matching, to give a specific meaning
to each effect.

Currently, it should be noted thateffect propagation is not tracked
by the type system. However, this is an experimental feature, which
is used extensively in thenew version of
YOCaml. I am aware that resources
are being devoted to developing anefficient type system to track
effect propagation!

In general, when I don’t care about controlling the program’s flow, or
I don’t need to add effectsafter the fact, I use modules. But in
the case of YOCaml, the new effect system was leveraged tointroduce
effects dedicated to unit
testing,
allowing, for example, themocking of time passing.

Once again, it’s really difficult not to go on at length aboutuser-defined effects, which are a brand-new and very exciting
feature of the language. I’ll conclude by simply sharing two articles
written byArthur Wendlingthat explain
the use of effects in a very pedagogical way, along with a
comprehensive bibliography on the literature related to effect
abstraction in functional programming:

* Scopes and effect
handlers
* Roguelike with effect
handlers
* Effect bibliography

It’s worth noting that this inversion/injection could also be done
usingrecordsorobjects. However, my experience with OCaml
suggests that approaches using modules or effects (when you want to
manipulate the program’s control flow) are often more straightforward
and easier to reason about.

### Regarding the future

OCaml is aconstantly evolvinglanguage that changes with each
version. In the section on dependency inversion, I briefly mentioned
the recent inclusion of effects in the language to describe amulti-core runtime, reflecting the ongoing evolution of OCaml over
the years. One can also note the integration ofbinding
operators, which make the
use of the triadFunctors,Applicative
Functors, andMonadsmore convenient — similar tocomputation
expressionsin F#.

Currently, many very exciting projects are underway to further improve
the language:

* A deep work on the expression of effects, with a newly added syntax,
and a collection of research on the separation betweenoperations
and effectsand, of
course, on thepropagation of effects in the type
system.
* Jane Streetproposeda
non-intrusive resource management
model, inspired by
Rust, introducingmodalitiesanda bit of linearity.
* A genuinefoundational
workhas been initiated on the module language, making the implementation
ofModular
Implicitsmore smoothly achievable.

We can also note the development of ahygienic macro
system, the gradual
integration of astaged metaprogramming
system, and the
implementation of anoptimization
back-end, reflecting
OCaml’s strong activity in the innovation sector and making its
development in the coming years very motivating and exciting!

### Weaknesses

Even though I’m convinced that OCaml is anexcellent language,
claiming it is perfect would probably bedisingenuous— after all,nothing is perfect. Here are, in my opinion, a few points that cast
a shadow on OCaml as a language:

* Lack ofad-hoc
polymorphism.Although it is possible to work around it, for example using local
module openings, the absence ofad-hoc polymorphism(viatype
classes—
as in Haskell, ortraits/implicit
objects— as in Rust and Scala, orcanonical
structures— as in Coq) can sometimes make certain situations tricky. Even
though I tend to prefer explicit relationships, over the years I’ve
found several cases where this absence can be problematic:The inability to describe type parameter constraints on
polymorphic functions, leading to polymorphic equality and
comparison functions in the standard library, which has causedmuch
debateand, for example, required specialized versions of arithmetic
operators for different numeric representations (int,int64,float).Risk of combinatorial explosion when describing many relationships
between modules. This is why thePrefacelibrary proposes a
somewhatcomplex modular
decomposition.However, even though the arrival ofimplicit
modulesis probably not in the short-term roadmap, recent work on the module
language, as discussed in the “future of OCaml” section, is
promising.
* The inability to describe type parameter constraints on
polymorphic functions, leading to polymorphic equality and
comparison functions in the standard library, which has causedmuch
debateand, for example, required specialized versions of arithmetic
operators for different numeric representations (int,int64,float).
* Risk of combinatorial explosion when describing many relationships
between modules. This is why thePrefacelibrary proposes a
somewhatcomplex modular
decomposition.
* Cumbersome interaction between the module language and the value
language.The module language isa different languagewith
its own type system. Whether this counts as a weakness is debatable,
but this distinction can be intimidating. It comes from the fact
that OCaml’s module system was a pioneer in module theory and
predates more recent innovations (e.g.,1ML).
In practice, besides beingcomplex to grasp, certain parts of the
language are hard to specify correctly, for examplerecursive
modules.
* A language comfortable for functional programming, but impure.While I consider impuritya feature, importing idioms from
purely functional languages (e.g., Haskell) can cause difficulties
related to type inference, such as thevalue
restriction.
Even though OCaml hasrelaxedthis restriction, its implications on polymorphic function inference
can still be intimidating — for very good reasons.

* Syntax.Personally, I really like OCaml’s syntax and believe
syntax should rarely be a major issue, but some choices can be
confusing. For instance, type parameters prefix the type name: a
list ofais written'a list. Many of these choices aim toreduce syntactic ambiguity, and you get used to them
quickly. However, coming from another language, some of these
conventions may seem surprising.

I think these weaknesses are generally debatable (because they are
often justified), but I completely understand that they can be
unsettling. However, I believe they are not enough to make OCaml
unusable andshould not be a major barrier to getting started with
OCaml! The benefit of having animprovablelanguage is that it
constantly offers a range of potential improvements, motivating work
that can also benefit other languages. And, to be entirely honest,
being aware of theserough edges, I’ve more often found myself
frustrated by the absence of language featuresthat exist in OCamlin other languages, rather than complaining about these rough edges
while writing OCaml itself. For these rough edges, there are usually
workarounds (sometimes only partially satisfying, I admit) that allow
one to work calmly and effectively.

### To conclude on language

I have, in very broad strokes, outlinedreasonswhy, in my
opinion, learning OCaml is avery relevantchoice. This language
allows one tofundamentally understandcertainverypopular
programming idioms (often poorly defined). Moreover, some aspects of
the language perfectly serve industrial purposes, making good
practices sometimes trivial to express! Much of this appeal can be
experimented with in other languages, but OCaml'sstrongly
multi-paradigmnature allows one to centralize this learning in a
single language. To my knowledge, in the jungle ofpartially popularlanguages, only Scala seems to cover as many topics, although, from my
point of view, its object model is, essentially for interoperability
with other JVM languages, far less interesting.

Since the goal of this article is not to be a tutorial, I deliberately
skimmed over certain concepts,modulesandeffects. I hardly mentionedobjects,polymorphic
variants, orgeneralized
algebraic types. If
these topics interest you, I encourage you to read in detail the
excellentUsing, Understanding, and Unraveling The OCaml
LanguagebyDidier Rémy, along with the books I
presented in the introduction, which is a goldmine for anyone wishing
to deepen their knowledge of OCaml.

In conclusion, OCaml offers a diverse and rich set of language-level
tools for learning programming, building industrial-grade programs
that follow standards, as well as implementingcomplex data
structuresandcategory-theory-based
abstractionssuch as a functional
core, imperative traits, a rich and expressive inferred type system
(allowing the expression of algebraic types and facilitating clear
domain modeling), a module system for abstraction, reusability, and
defining compilation units, an object model, the ability to express
effects that can be propagated and interpreteda posteriori, and
other advanced features. Even just tograsp advanced programming
concepts, OCaml is anexcellent candidate— which is why OCaml
has been an obvious inspiration for many more recent languages,with
Rust being a notable
example.

## OCaml as an ecosystem

Having an expressive language is very beneficial forbuilding things(the phrasing is deliberately naive). However, in different contexts,
both professional and personal, this is not enough:

* In a professional context, it is obvious that if I want my team and
I to be productive, it is probably not very relevant to have to
build a whole tool stack before being able to start addressing the
problem we are tasked with.
* In a personal context, even though one couldarguethat building
your technology stack isvery educational, it changes the set of
skills you actually want todevelop. If, to build a small web
application to get started with OCaml as a web language, I have to
build my entire HTTP stack, it is very likely that OCaml is not the
right choice. Rest assured, however, that OCaml hasa rich tooling
ecosystemfor building web
applications!

That’s why the features offered by the language are not a sufficient
metric to describe its viability for building and maintaining
projects. The ecosystem is also a very important factor. It is for
these reasons that.NETand theJVM, through
relatively less expressive (but improving) languages like Java and C#,
are also so popular. To assess the relevance of an ecosystem, I think
it is important to consider several criteria:

* The relevance of theruntime(or compilation targets) for the
project. It’s likely that I wouldn’t recommend OCaml for embedding
in a tiny, exotichardware— though, knowing nothing about
low-level programming (because it’s not my field at all), I could be
wrong.
* Itsplatform. Is its entiretoolchaincomplete and ergonomic?
From my point of view, this includes a package manager, abuild
system, goodeditor support(agnostic as possible), a solid
documentation generator, and a collection of additional tools, such
as aformatter(and many others).
* The relevance of theavailable libraries(and their level of
maintenance and discoverability, which generally implies having a
package manager) with particular consideration for their
ergonomics. For example, if I don’t have any cryptography
primitives, I probably wouldn’t choose this technology to build ablockchain. There is a whole class of problems that arevery
difficulttosolve in isolationor in a professional context.

In this section, we will try to overview these different points to see
if the OCaml ecosystem lives up to the language. I want to clarify
thatI am somewhat biasedbecause I have been convinced of OCaml’s
relevance since 2012, back when the ecosystem wasdrastically
poorer. At that time, I tried to build projects by patching the
gaps, which probably created asurvivorship
bias. Nowadays,
thanks in part to industrial users, the OCaml ecosystem is much richer
and more extensive, making it much easier to defend, although when
some gaps still exist, the bad faithof the old usercan resurface.

### Compilation,runtimes, and additional targets

Since its inception, OCaml has had two compilation targets:

* Native compilation, which produces highly efficient executables
compiled for a specific architecture (and supports alarge number
of
architectures). Moreover,
whereas Windows was historically largely neglected,a special
efforthas been made to support it (also note theDkMl
project, an
independent initiative).
* Compilation tobytecode(for a virtual machine), producing
portable executables.

The presence of a virtual machine enabled the development of the
venerableJs_of_OCaml,
which allowstransforming OCaml bytecode into
JavaScript,
making OCaml perfectly viable for developing applications in the
browser as well as in theNoderuntime, and
it is extensively used for this website. Using a similar approach,WebAssemblysupport was made possible very
recently through theWasm_of_OCamlproject. Supporting compilation toWASMfor a language with agarbage
collectorwas aserious challenge, but with the recent specification of
interaction betweenWASMandgarbage
collectors,OCaml now has
perfectly decent WebAssembly compilation(and many ambitious web
projects, likeOcsigen, are beginning to
supportWASMnatively).

Moreover, theMelangeproject (historicallyBuckleScript)
offers a way totranspile— mapping the OCamlASTto the
JavaScriptAST— as an alternative for producing JavaScript. If I
were to compareJs_of_OCamlandMelange, beyond the different underlying
methods used to produce JavaScript (compiling tobytecodeand then
transforming thatbytecodeinto JavaScript versus syntactic
transformation from OCaml to JavaScript), I would say thatJs_of_OCamlintegrates better with the OCaml ecosystem and is
therefore likelyintended for OCaml developerswho want to make
their projects accessible from a browser — indeed, interaction with
the existing JavaScript ecosystem can be more cumbersome.Melangefits better with the JavaScript ecosystem (npmand co) and is
therefore likelyintended for JavaScript developersseeking to
bring more safety to their JS projects (or an existing codebase).

Nowadays, it is common to findmulti-backendlanguages likeIdrisorNim. However,at the time, I was very
impressed that OCaml could,from the moment I started using it, also
compile to JavaScript. Back then, the only language I knew that
offered multiple compilation targets wasHaxe,
which were so different (incidentally, Haxe iswritten in
OCaml).

Indeed, in 2024, producing JavaScript has become standard, but thefirst traces of Js_of_OCaml date back to
2006,
making OCaml a pioneer in the field!

#### A quick detour via MirageOS

In thelattice formed by the different OCaml execution and
compilation contexts, having libraries that work well inthe
majority of contextsis a challenging task. Fortunately, theMirageOSproject — a set of libraries designed
to build anoperating system dedicated to running only a single
applicationvia virtualization (aunikernel) — introduced a
true discipline for producing multi-context libraries.

In thenear future, I would like to spend more time writing about
Mirage, a fascinating project that we are trying to integrate into our
projects, for example inYOCaml,
our static site generator. Moreover, in addition to providing a sound
approach to distributingintelligently compartmentalizedlibraries,
Mirage offers a solid foundation of libraries for building OCaml
projects, which I will discuss moreextensivelyin the section
dedicated to libraries.

### The OCaml platform

TheOCaml platformis a set of tools,
maintained within an explicit lifecycle (active,incubating,maintained, anddeprecated), designed to support the compiler with
a coherent toolchain for OCaml code production. It includes many tools
serving different purposes; however, in this section, I will focus
only on certain aspects of the platform, leaving you free to consult
itspageandroadmapfor more detailed
information. In this section, we will look at,in broad strokes, 4
main specific points:

* The package manager
* The build system (build-system)
* Editor support (including code formatting)
* The documentation generator

When using OCaml for some time, this is probably the most exciting
part of the article, because, in my opinion, it is the one that has
benefited the most from progress. And theroadmapis, in my view,
promising!

#### OPAM, the package manager

Even thoughlanguage-specific package managershave become very
popular (if not essential) in reducing adoption friction for a
language, at the time OCaml was designed, they were rare. Indeed,
apart fromCTAN, for
distributingTeXpackages,CPAN, inspired by CTAN, for
distributingPerlpackages, andPEARforPHP, it would take untilGemsfor development
technologies to consider adopting a package manager as axiomatic for a
programming language.

OPAM, forOCamlPackageManager,
is aproposalfrom 2012 (theofficial siteAboutpagepresents a small
timeline). In addition to installing packages, OPAM allows you to
install different versions of OCaml and createpotentially sandboxed
environments, calledswitches. You can
use the public resource repository,hosted on
GitHub, but it is also
perfectly possible to create your own package index.

Having already published several packages on OPAM, I must admit that
theCIfor package addition
validation is incredibly efficient and user-friendly (each error
provides a Dockerfile to reproduce the issue locally), and that the
team of people who moderate and manage package additions/changes are
extraordinarily responsive and kind.

Even though, in the light of modern standards, one could point out several criticisms of OPAM, for example:

* terminology that can be cumbersome to grasp (switch,invariant,
etc.)
* duplication of all packages and compilers across multipleswitches(this is a known issue for whichwork has already been
done)
* and probably some ergonomic issues (notably the interaction withdunecould be smoother, for whichwork is also currently
underway)
* some complications when managing packages in development,
referencing them from a source repository rather than from OPAM

I must admit that coming from an era when OPAM did not exist, I have
learned to live with some of these minor pitfalls, and on a daily
basis, I have little reason to complain about the tool, which has
never really let me down in my everyday use. However, if you have
encountered usage issues, I encourage you to discuss them onone of
the communication spacesso that the
development team can take your feedback into account and guide you.

There is alsoesyas an alternative package
manager, which draws inspiration fromNixto
build a reusablestore, in the same way it is possible to use Nix
with OCaml. However, being somewhat conventional, I am not really
familiar with these practices, and being satisfied with myworkflowwith OPAM, I have, unfortunately, never taken the time to seriously
experiment withesy.

#### Dune, thebuild-system

As with package management, historically, OCaml hadseveralbuild-systems: the venerableocamlbuild,oasis,ocp-build,Jenga, and other variations aroundMake. However, since 2018, the
community has strongly adoptedDune, abuild-systeminitially developed atJanestreet.

In many aspects, Dune can be intimidating. Indeed, itsdocumentationisvery
dense— but it has greatly improved in terms of structure over the
past few months. And, while many tools choose rule description
languages likeYAML,TOML, or evenJSON, Dune has opted forS-expressions. It is
also regrettable that Dune,by default, treatsall
warningsas
fatal.

Before explaining some of its choices (such asS-expressions), it
is very important to highlight the points that have made Dune a
standard:

* Dune isvery fastand offers ahighly efficientexecution
model
* it builds the necessary artifacts for configurationautomatically
* it generates some redundant files (such as OPAM description files)
* it trivializes thevendoringof
libraries
* it allows invokingread–eval–print
loopscorrectly provisioned by the context
* one becomes familiar very quickly withS-expressions, which
allow rules to be described schematically and rapidly
* it is relatively agnostic and can execute arbitrary tasks (similar
tomake)
* it is constantly evolving and improving from version to version
* paired withdune-release,
it makes publishing packages on OPAM incredibly simple

Perhaps I’m biased, but in my opinion, Dune is one of the most generic
and pleasantbuild-systemsI’ve ever used — even if, at first
glance, it can seem intimidating and some choices may be hard to
justify.

##### On the choice of S-expressions

At first glance, using aLisp-likesyntax to describe binaries,
libraries, and projects may seem surprising. However, this decision
has several advantages:

* The AST ofS-expressionsbeingdrastically simple, parsing
is very straightforward and can be made highly efficient, which does
not penalize compilation speed.
* The language hastermination, making it easier to inspect in case
of errors (anyone who has tried to handle errors in large YAML files
will have faced this kind of problem).
* The language is very easy to learn and to describe.
* It allows describingreal programs, making Dune relatively
generic and enabling additional tasks.

So, from my point of view, the choice ofS-expressionsis
relevant: it allows describing complex, readable programs without
being too verbose, does not significantly slow down compilation, and
enables very concise descriptions of highly complex build rules. And
to be completely honest, you get used to it very quickly!

##### Contribution to the state of the art: Selective Applicative Functor

In addition to being a very pleasantbuild-system, Dune has
contributed to the state of the art in research by highlighting a new
constructioninspired by category theory. Indeed, in 2018,Andrey
Mokhov,Neil
MitchellandSimon Peyton
Jonesproposed, in the excellent
paper"Build Systems à la
Carte", a collection of
abstractions to re-implement — modularly — variousbuild-systems. However, for reasons related tostatic dependency
analysis, these models were not compatible with Dune. After several
investigations and experiments, a new construction, similar to anApplicative,
aSelective Applicative
Functor, capturing Dune's
prerequisites was proposed. This information may seem anecdotal, but,
in my view, it reinforces the value (and importance) of being atthe
intersection of research and industry.

##### Alternatives

Although widely adopted by the community, OCaml offers alternative
systems (sometimes using Duneunder the hood), for example,Obazlwhich provides OCaml
rules forBazel,Onixwhich allows building projects
withNix,Buck2which is
an ambitious and generic project competing with Bazel, andDromwhich offers an experience
similar toCargo, unifying
package management and project building.

#### LSP and Merlin for editors

In the previous sections, we saw how much OCaml has progressed in
areas necessary for industrialization. On the other hand, in terms of
editor support, OCaml has had excellent support forVimandEmacsfor over 10 years through
theMerlinproject, which provides
editor services enablingcompletion,diagnostics,code
navigationfeatures, tools related tovalue deconstruction,value construction, management (and navigation) oftyped
holes,polarity-based search, precise information (with
verbosity control) onvalue types,jump-to-definition, etc.

In my opinion, IDE support via Merlin has been excellent in OCaml for
a very long time. Coupled withocp-indent, which calculates
the cursor position after an action in the editor, andOCamlformat, which allows
on-the-fly (configurable) formatting of OCaml files, writing code in
Emacs or Vim is an absolute joy!

##### The advent of VSCode, LSP as standard

In 2015,Visual Studio
Codearrived,
introducing theLanguage Server
Protocol,
which abstracts how editors interact with a language through a server,
following a uniform protocol. OCaml has avery good LSP
serverthat itself relies on
well-established libraries in the OCaml ecosystem, notably
Merlin. Since LSP has becomerelatively standardin the editor world
(Vim, Emacs, and, in fact, almost all free editors I know can interact
with an LSP server), the plan is to deprecate the Merlin server,
moving entirely to LSP, making Merlin a low-level library that
provides tooling used by LSP. This is one of the projects theEditorteam atTarides(which I’m part of) is working
on: makingocaml-lspfeature-compatible with Merlin’s historic
server to reduce maintenance for alternative clients (Emacs and Vim),
only worrying about OCaml-specific requests and actions (which,
logically, are not part of the protocol).

Currently, theOCaml platform for Visual Studio
CodeandOCaml-eglotare the two
canonical implementations (which extend the LSP protocol for OCaml),
respectively for VSCode and Emacs. We are currently considering the
implementation of a NeoVim plugin.

A bit like with Dune, in my opinion, the tooling state is excellent,
and the roadmap is motivating! However, since this ismy work, I’m
probably biased.

#### Odoc, the documentation generator

OCaml is distributed with a documentation generator, the venerableOCamldoc; however, it is
no longer recommended by/for the community. Indeed, the tool being
promoted isOdoc, a new tool that
exists outside the compiler and offers several very interesting
features:

* arich markuplanguage, supporting cross-references
* the ability to write "manual" pages, ephemeral, while still
benefiting from cross-references
* very good integration with Dune
* a type-based search bar (implemented viaSherlodoc)
* inclusion of source code (written in the documentation or documented
modules)
* implementation ofdriversallowing the generation of large sets of
documentation (used to implementthe documentation of all packages
on OPAM)
* support fordoctestviamdx

Even though thelook'n feelof documentation generated by Odoc is,
in my view,far superiorto that produced by OCamldoc, there is
still (once again, in my view) a bit of work needed on the UI for the
tool to be trulyperfect!

I clearly have a certain fondness for the documentation of theElixirlanguage,HexDoc(in terms ofdesignand features), and
personally, I would like OCaml to move toward that example. However,
it must be acknowledged that the documentation generated by Odoc is
superior to that of many other languages. Moreover, due to the highly
modular nature of the language, a good documentation generator that
effectively supportscross-referencesis quite an achievement!

### Available libraries

We have seen that the language iscool, and that it has tooling
which, although still evolving, is effective and pleasant to
use. Could its lack of popularity be due to a too limited set of
libraries? To be completely honest,I don’t know. What I do know
is that whenever I have had to write OCaml projects, both professional
and personal, I have often found everything I needed in thepackage
list. I think the reasons why OCaml is
mature enough for many typical projects can be summarized in several
points:

* Companies likeLexifiandJanestreethave strongly contributed
to the ecosystem by releasing many libraries necessary for their
daily use.
* Ambitious research projects, such as, in the case of the Web,Ocsigen, used industrially in
theBeSportproject, have generated a
collection of useful libraries.
* As mentioned earlier,MirageOS, with itsClean
Slateapproach, naturally produced many robust libraries.
* Like in popular languages such as JavaScript or Rust, motivated
contributors have provided excellent libraries.
* The language is old and has been used industrially for a long time.

For my part, I have sometimesre-createdlibraries for thepleasure of reinventing the wheel, but also, at times, to offer an
alternative interface. Moreover, OCaml allows interfacing with, among
other languages, C, enabling the creation ofbindingsfor a large
number of libraries and tools. However, if there is a library that you
findobjectivelymissing, I encourage you to jointhe
community.

It is important to note that my use of OCaml has focused primarily on
three areas:

* Web development(heavily driven by Mirage, Ocsigen, and
independent projects likeDream,YOCaml, and manyothers)
* Blockchain developmentand, by extension, the use of
cryptography libraries, provided once again by Mirage, as well as by
theHACL*project, a
formally verified library written inF*and extracted to OCaml
* Development ofMerlinandOCaml-LSP

All these areas still require good testing tooling, and OCaml offers
several complementary libraries to implement robust test
suites. Indeed, within the OCaml ecosystem, you can find tools to
writedoctests, classicunit
tests,property-based
tests,fuzzing, as well asoutput
observation
tests,inline
tests(which allow testing, among other things, private components), andcram
tests.

I continue to find everything I need among the available packages, and
I’m still very impressed to see the number of packages and
alternatives growyear after year. Of course, there are some gaps,
but they have not invalidated my choice of OCaml.

#### Side note on the standard library

A recurring criticism of OCaml is themodestyof its standard
library. Historically, it was designed only to implement the language
itself, so it didn’t include certain features useful for end
users. This situation has led to the emergence of alternative standard
libraries, the most popular of which are:

* Batteries,
an alternative to the standard library that is somewhatdated. Historically, it was aforkofExtlib.
* Base, an alternative
developed byJanestreet, usedquite
extensivelyin the bookReal World
OCaml. The library enforces strong
conventions, such aslabelinghigher-order functions (typically
with the namef).
* Coreis an extension of
Base.
* Containersis an
extension of the standard library (in the sense thatopen Containersat the beginning of a module does not break code written
with the standard library).

In addition to these alternative standard libraries, there are
specialized libraries that address general problems, such asBos, which provides tools to
interact with an operating system, andPreface—shameless plug— which
allows you torealize abstractions from category theory.

The stance of the maintainers on the standard library has evolved over
the years, and it is now possible to consider extending it. However,
additions to the standard library are often subject to debate, and
adding new modules can sometimes take a long time. Personally, I would
have preferred that the standard librarycontinue to serve only the
development of the languageand that a library under the OCaml
community umbrella be published. This separation allows the releases
of the language and its standard library to be desynchronized and also
likely simplifies compatibility between the library and the language.

### Ecosystem Conclusion

Unfortunately, I don’t have the opportunity to cover all the tools of
the platform, nor the fundamental building blocks that make OCaml
enjoyable to use for personal projects as well as for industrial
projects (for example, the various existingdebuggers). However, I
hope I’ve been able to give an overview of some tools that form a
solid foundation for using OCaml.

In my use of the language, I’ve sometimes had to build my own library;
however, it’s not an exercise I regret. I think, unfortunately, that
if one decides never to use a language just because 100% of the
necessary libraries aren’t available, it feels—perhaps awkwardly—to me
likeleveling down, trapping us behind languages backed bywealthy companies, like Java or C#, andthat’s a bit sad.

## On the community

Even though I’ve used many different programming languages, I think
OCaml is the only one with which I’ve had strong community
interaction. So, I’m not fully aware of how things work in other
communities, which makes my feedbacksomewhat irrelevant. But from
my experience, I find that the OCaml community, besides being very
productive, is:

* Very accessible: Like many other languages, OCaml has astrong
online presence. On these platforms,
you can find highly experienced contributors to the language and its
ecosystem and benefit from expert (or sometimes less technical)
advice. I’d like to give a special mention toGabriel
SchererandFlorian
Angeletti, whose
answers are always thoughtful and interesting.
* Very kind: I often need to ask for help, and I’ve always
received clear and precise answers, whether in private or in public.
* Very brilliant: OCaml is the product of work bybrilliant
researchers, and having the chance to interact with them is
incredible (and potentially a bit intimidating). Being able to ask
questions directly to people behind some of the major discoveries in
language design is a fantastic opportunity.

To conclude on the community aspect, even though I’m not fully aware
of how other communities interact, I find it a pleasure to be part of
the OCaml developer community. It’s a welcoming space, conducive to
sharing and learning.

## Some myths about OCaml

I’m finally reaching the most fun part of this overly long article: I
get todebunksome persistent myths about OCaml. I still can’t
promise complete objectivity, but know that my intentions are good. On
the internet, you often see various criticisms or remarks about OCaml,
and I often find it tiresome to respond. However, what better way than
an article meant to share my enthusiasm for the language to take the
time to address some of these critiques and try to provide a response?

I’ve selected a few, but it’s likely that in the future I’ll write
somewhat longer articles—similar to the members ofHeyPlzLookAtMe
(fr)— about articles I find unfair.

### OCaml and F#

F#is a programming languagehistorically very
inspiredby
OCaml that runs on the.NETplatform
(and, de facto, integrates very well with C#). I find the language —
which I have professionally used atDernierCriandD-Edge— very pleasant. Historically, since
.NET was exclusively for Windows environments, OCaml didn’t suffer
much by comparison. However, since the arrival of.NET
Core, a cross-platform implementation
of .NET, I increasingly see statements on the internet like:

"Why continue using OCaml when you can have the same language, F#,
with the entire .NET ecosystem, more features, and a syntax that’s
more pleasant to use?"

First, I do think that having the .NET (Core) ecosystem is a huge
advantage. Regarding the syntax, I’m more reserved. Indeed, I find
that indentation-based syntax sometimes makes moving code around more
cumbersome, and even though there are criticisms of OCaml’s syntax, I
must admit it hasn’t let me down. The last point seems a bit more
insidious. Indeed, F# has been equipped with features not present in
OCaml, for example:

* Computation
expressions(which are syntactically a more general form thanbinding
operators)
* Type
providers(which can, unfortunately, sometimes cause issues with .NET Core in
certain name/path resolution cases)
* Active
patterns
* Statically resolved type
parameters
* The ability to assign methods to sums and products, which makes
sense for interoperability reasons but significantly breaks type
inference
* And probably other features that I don’t know well (or are linked to
interoperability with the .NET platform, notablyreflection)

These evolutions arrived gradually in the language. It would be naive
to think that OCaml hasn’t evolved as well. Indeed, although
historically the two languages seemed very similar, from the very
beginning of F#’s proposal, certain features were missing:

* The absence of amodule language. Indeed, themodulekeyword
exists in F#, but it is only used to describe static classes (and it
integrates rather awkwardly with namespaces).
* Adrastically different object model(for interoperability with
C#, of course).

These two reasons alone would be enough to consider OCaml and F# ascousinlanguages butvery different, and in my opinion, strongly
justify preferring one over the other. In my case, OCaml over F# makes
the introductory sentence of this section moot. However, like F#,
OCaml has also evolved, and in addition to these two fundamental
differences, OCaml offers many features that are absent in F#:

* Local and generalizedopens: In OCaml, you can open a module
locally within a scope, whereas in F# you can only open a module at
thetop-level, which can be quite frustrating in some cases.
* Row polymorphism: OCaml supports row polymorphism on products
(via objects) and sums (viapolymorphic
variants).
* Generalized Algebraic Data Types (GADTs): One of the most missed
features (after the module system) for expressing precise type
constraints.
* User-defined effects: OCaml allows defining custom effect
handlers, which can simplify complex control flow and concurrency
patterns.
* Open sums: Extensible variants allow for sum types that can be
extended, though similar behavior can sometimes be simulated using
objects and inheritance.

To conclude, even though F# is a really nice language and using it
brings many advantages (notably the .NET platform), it isnot just a
better version of OCaml. The two languages are very different, and
from my point of view, OCaml has a more sophisticated type system,
which makes me prefer it over F#. In my opinion, saying that F# is
just a prettier OCaml is as reasonable as saying thatKotlinis nothing more thanScalawith a lighter syntax.

### Doubled operators for floats

The standard library contains the following arithmetic operators on
integers:

val

(

+

)

:

int

->

int

->

int

val

(

-

)

:

int

->

int

->

int

val

(

*

)

:

int

->

int

->

int

But also arithmetic operators for floating point numbers:

val

(

+.

)

:

float

->

float

->

float

val

(

-.

)

:

float

->

float

->

float

val

(

*.

)

:

float

->

float

->

float

At first glance, this may seem confusing. However, it makes perfect
sense. If we wanted to have generic operators, we would needad-hoc
polymorphism, like
in Haskell, for example, where arithmetic operators reside in theNumtype class:

class

Num

a

where


--
 more code

 (+), (-), (*) :: a -> a -> a


--
 more code

Without some form of ad-hoc polymorphism (via classes, traits, or
implicits) to describe a constraint on our operators, e.g.,op :: Num a => a -> a -> a, what can we do? A suggestion I’ve often seen online
is to usethe same trickas with the=operator, whose type isval (=) : 'a -> 'a -> bool. That doesn’t work, because while
we can hope thateverything is comparable(at worst, we can returnfalse), how can we generalize something like addition?

Support for arithmetic operators is a tricky problem, which is
actually the original motivation behindtype
classes(and the reason forstatically resolved type
parametersin F#). From my perspective,while waiting formodular
implicits,
duplicating operators to work with integers and floats seems like areasonableapproach. And if, for some strange reason, suffixing
operators with dots when using floats gives you hives, you can avoid
it using local opens by providing, for example, this module:

module

Arithmetic

(
P

:

sig


type

t


val

add
 : t -> t -> t


val

sub
 : t -> t -> t


val

mul
 : t -> t -> t


val

div
 : t -> t -> t

end
)

=

struct


let

(

+

)
,

(

-

)
,

(

*

)
,

(

/

)

=

P
.
(
add
,

sub
,

mul
,

div
)

end

Which allows extending theIntandFloatmodules (which already
provide the functionsadd,sub,mul, anddiv) by giving them
arithmetic operators:

module

Int

=

struct


include

Int


include

Arithmetic

(
Int
)

end

In broad terms, we create anIntmodule, include the previousIntmodule so that our newIntmodule retains the entire API of the
originalIntmodule, and then we define (and include) our arithmetic
operators. We can now repeat the same process withFloat:

module

Float

=

struct


include

Float


include

Arithmetic

(
Float
)

end

And now we can use a localopenso that we don’t have to suffix our
operators with dots:

let

x

=

Int
.
(
1

+

2

+

3

+

(
4

*

6

/

7
)
)

let

y

=

Float
.
(
1.3

+

2.5

+

3.1

+

(
4.6

*

6.8

/

7.9
)
)

From my point of view, even if this can be confusing for those coming
from languages where this isn’t an issue, it’s a minor problem. The
lack of operator overloading seems like a rather weak argument for not
giving a language a chance —but that’s just my humble opinion.

### On the separation betweenmlandmli

Another point that generates a lot of discussion (evenrecently)
concerns theseparation betweenmlandmlifiles. Personally,
I find it great. Even if it can introduce a bit of repetition, it
allows me to focus on the API via module encapsulation in themlifile while also adding documentation. I can organize the functions I
expose in any order I like, and naturally, I can abstract the types I
share as much as possible. Moreover, when I look at an implementation,
themlcode is rarely cluttered with documentation, making it easy
to navigate the different elements of the module. On top of that, it
enables separate compilation and prevents recompiling modules that
depend on other modules whose implementation alone was changed during
development (this is Dune’s default behavior in thedevprofile).

However, tastes vary, and when exposing complex types or module types,
this repetition can be annoying. Fortunately, there is atrick,
presented in 2020 byCraig Ferguson, that
helps mitigate this repetition:The_intf_trick.

Additionally, there are small tricks based on the ability to pass
arbitrary module expressions to theopenandincludeprimitives,
which sometimes allow you to do withoutmli. I had already mentioned
this in the articleOCaml, modules and import
schemes.

#### Encapsulation withoutmli

You can simply useopen struct (* private code *) endto avoid
exporting parts of your code without needing interfaces. For example:

open

struct


(*
 Private API
*)


let

f

x

=

x


let

g

=

_some_private_stuff

end

(*
 Public API
*)

let

a

=

f

10

let

b

=

g

+

11

#### Expressing the interface fromml

Another similar technique is to useinclude (struct ... end : sig (* public API *) end)to describe both the structure and the interface
in the same file. For example:

include

(
struct


type

t

=

int


let

f

x

=

x


let

g

=

_some_private_stuff

end

:

sig


type

t


val

f
 : int -> t

end
)

This way, the signature and the structure live in the same file, while
still allowing precise control over encapsulation. Another approach
would be to put the signature in a dedicatedmodule type, like this:

module

type

S

=

sig


type

t


val

f
 : int -> t

end

include

(
struct


type

t

=

int


let

f

x

=

x


let

g

=

_some_private_stuff

end

:

S
)

This is very similar to the first approach, except that the module
also exposes the module typeS. A useful side effect of thisleakis that you can easily reference the module's signature usingMy_mod.Sinstead of having to writemodule type of My_mod.

#### To conclude on separation

I find this separationvery desirable. However, since OCaml’s
module system is highly expressive, it is possible — through some
clever encoding — to work around this separation. From my point of
view, these approaches mainly serve to demonstrate thisexpressiveness, because the downside of merging everything in one
file is the loss of separate compilation, which I considerquite
unfortunate.

## Conclusion

I think I havebrieflycovered the points I wanted to discuss. From
my perspective,OCaml is an amazing language! It offers an
excellent balance between safety and expressiveness, thanks in
particular to its advanced type system, a rich module language,
objects, support forrow polymorphismvia objects and polymorphic
variants, and user-defined effects! Its intersection of research and
industry makes it, in my view, a language evolving in the right
direction, carefully integrating new features to stay modern without
suffering the pitfalls of too-rapid or untested adoption.

Even though for several years OCaml’s tooling might have seemed a bit…dusty, recently, thanks in part to commercial support from certain
companies, the tooling has been drastically modernized and continues
to improve, as shown bythe platform
roadmap. Additionally, the
growing ecosystem of libraries makes it possible to use OCaml in a
wide range of contexts, notably thanks to its different compilation
targets (for example, the browser viajs_of_ocamlandwasm_of_ocaml).

By combining an expressive language with a versatile ecosystem and a
supportive, responsive community, OCaml becomes a very compelling
choice for both personal and professional projects. Clearly, migrating
an entire codebase to OCaml is probably not a pragmatic move, but if
you have small personal projects in mind and are curious and
entertained by programming languages,I seriously encourage you to
consider OCaml!

I hope I’ve managed to convey my enthusiasm for this language (and its
ecosystem). If you’d like to discuss it, find projects, or explore
contribution opportunities, I’d be happy to talk with you — or you can
reach out to the community throughthe
forum, which is active, responsive, and
welcoming!
