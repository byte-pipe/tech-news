---
title: is-kit Reached 100 Stars ⭐🎉 Here’s What Changed Since 50 - DEV Community
url: https://dev.to/nyaomaru/is-kit-reached-100-stars-heres-what-changed-since-50-49pf
site_name: devto
content_file: devto-is-kit-reached-100-stars-heres-what-changed-since
fetched_at: '2026-10-21T22:06:22.090446'
original_url: https://dev.to/nyaomaru/is-kit-reached-100-stars-heres-what-changed-since-50-49pf
author: nyaomaru
date: '2026-10-21'
description: Hoi hoi! YAY! is-kit just reached 100 GitHub stars⭐ 🎉🎉🎉 When it reached 50 stars, I wrote about how... Tagged with typescript, opensource, webdev, frontend.
tags: '#typescript, #opensource, #webdev, #frontend'
---

Covers new APIs, Effect edge cases, and OSS usage

Hoi hoi!

YAY!is-kitjust reached100 GitHub stars⭐🎉🎉🎉

When it reached 50 stars, I wrote about how we use it in a production TypeScript application serving more than 100,000 users. 👇

Real-world scale for type safety

 nyaomaru
 

 nyaomaru
 
 
 

nyaomaru

 Follow
 

Aug 12

## is-kit Reached 50 Stars ⭐ Here’s How We Use It in Production

#
typescript

#
opensource

#
webdev

#
frontend

97
 reactions

Comments

 21
 comments

 7 min read
 

I could write the same story again. But that would be boring. 😹

A lot has happened since then.

The library gainednew APIs, some existing APIsbecame stricter, I startedusing it in more of my own OSS projects, andone real-world use case even exposed a type inference edge case inEffect.

So this time, instead of explaining the production adoption again, I want to look at:

* What changed between 50 and 100 stars
* Some of the most important APIs added since then
* How I am actually usingis-kitoutside the original production application
* A real bug report involvingEffect.catchIf
* What 100 stars means to me now

Let's dive in! 🔧

## ⭐ First, What Did 50 Stars Mean?

At 50 stars, the biggest thing I wanted to show was thatis-kitwas not only a toy project.

It was already being used in a real production application. 🚀

The application had repeated runtime checks like

typeof
 
value
 
===
 
"
string
"
;

typeof
 
value
 
===
 
"
number
"
;

value
 
===
 
null
 
||
 
value
 
===
 
undefined
;

Enter fullscreen mode

Exit fullscreen mode

and several larger user-defined type guards for things like HTTP errors, literal unions, arrays, API values, and plain objects.

The interesting part wasnotthatis-kitmade those checks shorter.The interesting part was that it gave them onereusable shape.

Small guards could be composed.

Application-owned helpers could sit between the library and feature code. And the result could still participate in normal TypeScript control flow.

That part has not changed.

But since 50 stars, the library itself has moved quite a bit. 👀

## 🔑 Property Refinement Became a First-Class Use Case

One thing I kept running into was this.

I already have a good type guard.I just want to apply it to one property.

For example

declare
 
const
 
input
:
 
unknown
;

Enter fullscreen mode

Exit fullscreen mode

Maybe I already know how to validate a string

import
 
{
 
isString
 
}
 
from
 
"
is-kit
"
;

Enter fullscreen mode

Exit fullscreen mode

But now I want to express

"This object has anameproperty, and that property is a string."

That sounds simple, but there are actually a few different cases.

A required property isnot the same as an optional property.An array index isnot the same as an object property.

And an optional property that becomes known to be defined shouldnarrow differently from one that is still optional.

Sois-kitadded three property refinement helpers:

* refineKey
* refineDefinedKey
* refineIndex

The idea is simple

Take a type guard you already trust and lift it onto a property or array element.

For example

import
 
{
 
isString
,
 
refineKey
 
}
 
from
 
"
is-kit
"
;

const
 
hasStringName
 
=
 
refineKey
(
"
name
"
,
 
isString
);

Enter fullscreen mode

Exit fullscreen mode

Now the string guard is reusable at a deeper level instead of being rewritten inside another custom predicate.

This is a small API, but I like it because it follows the same design goal as the rest ofis-kit.

Do not build one giant validator.

Build small checks that can be reused in normal TypeScript code.

## 🔍 ThendiscriminatedUnionGot Much More Serious

The biggest addition since the 50-star article is probably the exhaustive discriminated union API introduced inv1.15.0.

Consider a common TypeScript type

type
 
Result
 
=
 
{
 
ok
:
 
true
;
 
value
:
 
string
 
}
 
|
 
{
 
ok
:
 
false
;
 
error
:
 
string
 
};

Enter fullscreen mode

Exit fullscreen mode

At runtime, validating this is not difficult.

You can checkok, then validate the corresponding fields.

But there is another question

Can TypeScript verify that the validator itself covers the whole union?

That is wherediscriminatedUnioncomes in.

import
 
{
 
discriminatedUnion
,
 
isString
,
 
oneOfValues
,
 
typedStruct
 
}
 
from
 
"
is-kit
"
;

type
 
Result
 
=
 
{
 
ok
:
 
true
;
 
value
:
 
string
 
}
 
|
 
{
 
ok
:
 
false
;
 
error
:
 
string
 
};

const
 
resultUnion
 
=
 
discriminatedUnion
<
Result
>
();

export
 
const
 
isResult
 
=
 
resultUnion
(
"
ok
"
,
 
[
true
,
 
false
],
 
{

 
true
:
 
typedStruct
<
Extract
<
Result
,
 
{
 
ok
:
 
true
 
}
>>
()({

 
ok
:
 
oneOfValues
(
true
),

 
value
:
 
isString
,

 
}),

 
false
:
 
typedStruct
<
Extract
<
Result
,
 
{
 
ok
:
 
false
 
}
>>
()({

 
ok
:
 
oneOfValues
(
false
),

 
error
:
 
isString
,

 
}),

});

Enter fullscreen mode

Exit fullscreen mode

The runtime behavior is useful.

But the more interesting part is the compile-time contract.

The builder checks things like:

* Missing discriminant branches
* Extra branches
* Incompatible branch guards
* Incomplete discriminant tuples

So if the union changes, the guard cannot silently stay incomplete.

That matters because one of the easiest ways for a hand-written type guard to become dangerous is drift.

The TypeScript type evolves.The runtime guard does not.And the compiler cannot normally tell you that the two are no longer aligned.

discriminatedUnionis one attempt to make that class of mistake harder.

## 💪 The Library Also Became Stricter

Not every improvement between 50 and 100 stars was a new feature.

A lot of work was about making existing behavior more precise.

For example, recent releases included fixes around:

* recordOfliteral-key narrowing
* nativeErrorbrand checks
* array guards with overridden iterators
* exactstructvalidation
* symbol-keyed struct schemas
* cross-realm struct schemas

There was also more package-level testing.

is-kitnow checks published-package behavior from both ESM and CommonJS TypeScript consumers, and also hasDeno/JSRsmoke coverage.

This part is less exciting to show in a code snippet.

But for a small library, I think it is important.

Making sure they behave correctly in weird JavaScript and TypeScript environments is where things become real.

## 🤖 I Started Usingis-kitin Other OSS Too

Since reaching 50 stars, I've also started usingis-kitmore naturally in other OSS projects I maintain.

For example, in my changelog tooling ofchangelog-bot, I usedefineto keep small predicates reusable and composable instead of turning every runtime check into an isolated helper.

A simplified example looks like this 👇

import
 
{
 
define
,
 
oneOfValues
 
}
 
from
 
"
is-kit
"
;

const
 
CHANGELOG_SECTIONS
 
=
 
[
"
Added
"
,
 
"
Changed
"
,
 
"
Fixed
"
,
 
"
Removed
"
]
 
as
 
const
;

const
 
isChangelogSection
 
=
 
define
<
(
typeof
 
CHANGELOG_SECTIONS
)[
number
]
>
(

 
oneOfValues
(
CHANGELOG_SECTIONS
),

);

Enter fullscreen mode

Exit fullscreen mode

The exact code is not the important part.

What changed for me is that I no longer think

"I should use my library here."

I just reach for the guard I need.

A library starts becoming useful to its maintainer when it stops feeling like a demo of itself.

## 🚀 Then anis-kitGuard Ran Into an Effect Type Bug

This was one of the most interesting things that happened recently.

Anis-kituser was using a type guard with Effect'scatchIf.

Conceptually, the refinement looked like this 👇

(
error
:
 
unknown
):
 
error
 
is
 
SomeError
 
=>
 
...

Enter fullscreen mode

Exit fullscreen mode

That is completely normal foris-kit.

In fact,unknownis exactly where the library is designed to start.

But withEffect.catchIf, that refinement could affect generic inference in an unexpected way.

The error channel could become widened tounknown.

The reported case resulted in this Effect PR 👏 And merged 🚀

# fix(effect): Made catchIf NoInfer Refinement's first arg with generic Err param#9252

nikelborm

 posted on 
Oct 15, 2026

## Type

* [ ] Refactor
* [ ] Feature
* [x] Bug Fix
* [ ] Optimization
* [ ] Documentation Update

## Description

When passing(arg: unknown) => arg is SomeErrorto somecatchIfs, it turned the error channel intounknown. This PR makes onlyself's Error slot influence the types, regardless of the type taken by refinement.

Validation: the Channel, Effect, and Stream type-test files pass on TypeScript 5.9.3 and 6.0.3, andpnpm checkpasses. Temporarily reverting the implementation reproduces unknown error-channel widening in Channel data-last usage and in unrelated-refinement cases across all three APIs. The matching data-first refinement cases also pass without the fix. No tests were changed during maintainer validation.

Closes EFF-2233

View on GitHub

The relevant type originally looked roughly like this

refinement
:
 
Predicate
.
Refinement
<
E
,
 
EB
>
;

Enter fullscreen mode

Exit fullscreen mode

and the fix changed it to

refinement
:
 
Predicate
.
Refinement
<
NoInfer
<
E
>
,
 
EB
>
;

Enter fullscreen mode

Exit fullscreen mode

The important idea is that therefinement's input type should not be allowed to redefine the error type already established by theEffect.

The PR also adds type tests for cases like

const
 
result
 
=
 
Effect
.
catchIf
(

 
mixedEffect
,

 
(
e
:
 
unknown
):
 
e
 
is
 
AiError
 
=>
 
e
 
instanceof
 
AiError
,

 
()
 
=>
 
Effect
.
succeed
(
"
ok
"
),

);

Enter fullscreen mode

Exit fullscreen mode

Without the fix, the refinement input could participate in inference and widen the error channel.

WithNoInfer, the original error type remains the source of truth.

The same pattern was fixed forChannelandStreamtoo.

There was also aBlueskypost about the issue

Not like the lib itself caught it, but when I created a reusable operator:

export const isNotFoundError = and(
 isObject,
 refineDefinedKey('reason', equalsKey('_tag', 'NotFound')),
)

I noticed my streams having unknown in the error channel

github.com/Effect-TS/ef...

— 
Evangeline Rome 🌵🦎🌱🐢🐍🐸 🥦 (@evadeva.bsky.social)
 
2026-10-15T16:38:16.787Z

I really liked this bug becauseit came from an interaction I would probably never have discovered by testingis-kitalone.

is-kitdid not "break Effect". AndEffectwas not doing something absurd either.

It was a subtle TypeScript inference interaction between a generic API and a refinement whose input was intentionally broad.

That is exactly the kind of edge case that appears when libraries start meeting each other in real code.

## 👍 This Is the Kind of Feedback I Wanted

Whenis-kitreached 50 stars, I wrote

"Someone found this idea useful."

That was already enough to make me happy.

100 stars still does not mean the library is huge.

A star is still not a benchmark.It is still not proof of correctness.And it definitely does not mean every TypeScript project should installis-kit.

But something has changed.

People are not only starring the repository anymore.

They are

* Using the library
* Asking questions
* Finding edge cases
* Reporting bugs
* Comparing it with other validation approaches
* Using its guards with other TypeScript libraries
* Making me reconsider APIs I thought were already finished

That is much more valuable than the number itself. 💖

## 💬 The Project Is Also Becoming Easier to Explain

Another thing changed between 50 and 100 stars.

I became much clearer about whatis-kitisnot.

It isnottrying to replace every schema library.It isnottrying to turn every runtime value into a schema-first workflow.And it isnottrying to hide normal TypeScript control flow.

The core question is still very small

"Can thisunknownvalue safely enter this branch?"

Sometimes a schema library is the right answer.

For example, if I need:

* Rich validation errors
* Transformations
* Form validation
* A contract shared across systems

I may wantZod,Valibot,ArkType, or something else.

But sometimes I already have normal TypeScript code and I only need a reusable narrowing function.

That is where I wantis-kitto be useful.

if 
(
isUser
(
value
))
 
{

 
value
.
id
;

}

if 
(
isHttpClientError
(
error
))
 
{

 
// Handle HTTP client errors

}

items
.
filter
(
isString
);

result
.
catch
(
isHttpClientError
);

const
 
isMaybeNumber
 
=
 
nullish
(
isNumber
);

Enter fullscreen mode

Exit fullscreen mode

Small runtime decisions.Normal functions.Normal TypeScript.

## 🐱 What 100 Stars Means to Me

100 stars is still small compared with the largest TypeScript OSS projects.

No problem.

What matters to me is that the project is becoming more real in ways that have nothing to do with the star counter.

Since the 50-star milestone:

* New APIs were added
* Existing APIs became stricter
* Runtime edge cases were fixed
* Package compatibility testing improved
* I started usingis-kitnaturally in other OSS
* External usage produced feedback I could not generate alone
* Anunknown-based refinement even helped expose an inference edge case in Effect

That last part is probably my favorite.

Because the goal was never to build a library that only looks nice in its ownREADME!!!

The goal isto make reusable runtime narrowing work naturally inside real TypeScript code.

And now I am starting to see that happen outside my own repository too.

Thank you to everyone who starred the project, tried it, reported something, asked a question, opened an issue, or simply read the code. 🙏

There is still a lot I want to improve.

But 100 feels pretty nice. 😸⭐

If small composable type guards fit your TypeScript style, give it a try!

## nyaomaru/is-kit

### Build small guards. Compose them. A lightweight, zero-dependency toolkit for building reusable TypeScript type guards that compose, refine, and preserve natural narrowing. Runtime-safe 🛡️, composable 🧩, and ergonomic ✨.

# is-kit

## Build small guards. Compose them.

is-kitis a lightweight, zero-dependency toolkit for building reusable TypeScripttype guards.

is-kitis not just a collection ofisXhelpers. Its main focus is composing
small runtime checks into reusable guards while preserving useful TypeScript
narrowing.

It helps you write smallisFoofunctions, compose them intoricher runtime
checks, refine properties on values you already know about, and keepTypeScript narrowingnatural inside regular control flow. Use it at runtime
boundaries when needed, without requiring a schema-first workflow.

Runtime-safe🛡️,composable🧩, andergonomic✨ without asking you to adopt a heavy schema workflow.

* Build and reusetyped guards
* Compose guardswithand,or,not,oneOf
* UserefineKeyto narrow achild propertywhile preserving its parent type
* Validate objectshapes and collections when that is useful
* Parse or assertunknownvalues without a large schema framework

Best…

View on GitHub

Thank you for reading! 🤲

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse