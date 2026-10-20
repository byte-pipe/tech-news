---
title: How Do You Validate `unknown` in TypeScript Without a Schema Library? 🛡️ - DEV Community
url: https://dev.to/nyaomaru/how-do-you-validate-unknown-in-typescript-without-a-schema-library-1a11
site_name: devto
content_file: devto-how-do-you-validate-unknown-in-typescript-without
fetched_at: '2026-10-20T22:05:17.537938'
original_url: https://dev.to/nyaomaru/how-do-you-validate-unknown-in-typescript-without-a-schema-library-1a11
author: nyaomaru
date: '2026-10-14'
description: Hoi hoi! 👋 I'm @nyaomaru, a frontend engineer who is obsessed with gamba. 😸🦐 Recently, I was... Tagged with typescript, opensource, webdev, programming.
tags: '#typescript, #opensource, #webdev, #programming'
---

Commenters debate skipping heavy schema libraries

Hoi hoi! 👋

I'm@nyaomaru, a frontend engineer who is obsessed with gamba. 😸🦐

Recently, I was thinking about a very common TypeScript problem.

Suppose some value comes from:

* an API response
* JSON.parse
* local storage
* a message payload
* third-party code

What type should it have before we actually verify it?

Probably this

declare
 
const
 
input
:
 
unknown
;

Enter fullscreen mode

Exit fullscreen mode

That part is easy.

The interesting question is what comes next.

How do we safely turn thatunknowninto something useful?

And do we really need a full schema library every time?

Let's look at it! 👀

## Validate unknown in TypeScript Without a Schema Library | is-kit

Validate unknown TypeScript values with small composable type guards and safeParse, without adopting a schema-first validation workflow.

 is-kit.dev
 

## 🧱unknownIs Doing Its Job

Suppose we have

declare
 
const
 
input
:
 
unknown
;

input
.
name
;

// Error

Enter fullscreen mode

Exit fullscreen mode

TypeScript refuses to let us accessname.

At first this can feel annoying.

But TypeScript is actually telling us something important

We have a value.

We do not know what it is yet.

That is exactly what an untrusted boundary value should mean.

An HTTP response does not become aUserjust because our application expects aUser.

Neither does parsed JSON.

So I like to think ofunknownlike this

unknownis not missing type information.

It is an honest description of a value we have not verified yet.

The problem is notunknown.

The problem is how we establish trust.

## 😈 The Easy Escape:as User

There is a very short way out.

type
 
User
 
=
 
{

 
id
:
 
string
;

 
name
:
 
string
;

};

declare
 
const
 
input
:
 
unknown
;

const
 
user
 
=
 
input
 
as
 
User
;

user
.
name
.
toUpperCase
();

Enter fullscreen mode

Exit fullscreen mode

TypeScript is happy.

Nice! 🎉

Except,nothing was actually checked.

This still works

const
 
input
 
=
 
{

 
id
:
 
"
user-1
"
,

 
name
:
 
123
,

}
 
as
 
unknown
;

const
 
user
 
=
 
input
 
as
 
User
;

user
.
name
.
toUpperCase
();

// 💥 Runtime error

Enter fullscreen mode

Exit fullscreen mode

as Userchanges what the compiler believes.

It does not inspect the runtime value.It does not add missing properties.It does not turn123into a string.

So if runtime trust matters, a type assertion is not validation.

We need an actual runtime check.

## 🛡️ A Type Guard Connects Runtime and TypeScript

Let's start small.

Withis-kit, we can build a guard like this

import
 
{
 
isString
,
 
oneOfValues
,
 
struct
 
}
 
from
 
"
is-kit
"
;

const
 
isUser
 
=
 
struct
({

 
id
:
 
isString
,

 
name
:
 
isString
,

 
role
:
 
oneOfValues
(
"
admin
"
,
 
"
member
"
),

});

Enter fullscreen mode

Exit fullscreen mode

Now we can passunknowndirectly to it

declare
 
const
 
input
:
 
unknown
;

if 
(
isUser
(
input
))
 
{

 
input
.
name
.
toUpperCase
();

 
// input:

 
// Readonly<{

 
// id: string;

 
// name: string;

 
// role: "admin" | "member";

 
// }>

}

Enter fullscreen mode

Exit fullscreen mode

This is the part I like.

The same check does two jobs

runtime
→ does this value actually match?

TypeScript
→ what is this value after the check succeeds?

Enter fullscreen mode

Exit fullscreen mode

There is no separate schema definition and no type assertion.

We just compose small runtime predicates.

## 🧩 The Shape Can Grow Naturally

Real payloads are usually a little more complicated.

Maybe a user has:

* an optional profile
* a nullable bio
* a list of tags

We can keep composing guards

import
 
{

 
arrayOf
,

 
isString
,

 
nullable
,

 
oneOfValues
,

 
optionalKey
,

 
struct
,

}
 
from
 
"
is-kit
"
;

const
 
isProfile
 
=
 
struct
({

 
displayName
:
 
isString
,

 
bio
:
 
optionalKey
(
nullable
(
isString
)),

});

const
 
isUser
 
=
 
struct
({

 
id
:
 
isString
,

 
role
:
 
oneOfValues
(
"
admin
"
,
 
"
member
"
),

 
profile
:
 
optionalKey
(
isProfile
),

 
tags
:
 
arrayOf
(
isString
),

});

Enter fullscreen mode

Exit fullscreen mode

Then

isUser
({

 
id
:
 
"
user-1
"
,

 
role
:
 
"
member
"
,

 
tags
:
 
[
"
typescript
"
,
 
"
guards
"
],

});

// true

Enter fullscreen mode

Exit fullscreen mode

But

isUser
({

 
id
:
 
"
user-1
"
,

 
role
:
 
"
owner
"
,

 
tags
:
 
[
"
typescript
"
],

});

// false

Enter fullscreen mode

Exit fullscreen mode

Each piece is still just a guard.

That means we can test it independently, reuse it somewhere else, or compose it into something larger.

There is also an important difference here

optionalKey
(...)

Enter fullscreen mode

Exit fullscreen mode

means

the property may be absent

Enter fullscreen mode

Exit fullscreen mode

while

nullable
(...)

Enter fullscreen mode

Exit fullscreen mode

means

the value may be null

Enter fullscreen mode

Exit fullscreen mode

Those are different runtime contracts, so I prefer keeping them separate.

## 📦 What DoessafeParseAdd?

A direct guard is often enough.

if 
(
isUser
(
input
))
 
{

 
renderUser
(
input
);

}

Enter fullscreen mode

Exit fullscreen mode

But sometimes I want the validation result itself to move through the program.

For example

const
 
result
 
=
 
safeParse
(
isUser
,
 
input
);

if 
(
!
result
.
valid
)
 
{

 
return
 
{
 
status
:
 
400
 
as
 
const
 
};

}

return
 
{

 
status
:
 
200
 
as
 
const
,

 
user
:
 
result
.
value
,

};

Enter fullscreen mode

Exit fullscreen mode

safeParsegives us a small tagged result

{

 
valid
:
 
(
true
,
 
value
);

}

Enter fullscreen mode

Exit fullscreen mode

or

{

 
valid
:
 
false
;

}

Enter fullscreen mode

Exit fullscreen mode

So TypeScript can narrow it with a normal branch.

The important part is whatsafeParsedoesnotdo.

It does not:

* clone the value
* coerce the value
* generate a new object
* transform invalid data into valid data

On success, it returns the same value after the guard has accepted it.

So I think of the difference like this

guard
→ boolean + narrowing

safeParse
→ tagged result + validated value

Enter fullscreen mode

Exit fullscreen mode

Same runtime rule.

Different control-flow shape.

## 🧃 What About JSON?

This is one of the most common boundaries.

const
 
value
 
=
 
JSON
.
parse
(
body
);

Enter fullscreen mode

Exit fullscreen mode

The awkward part is thatJSON.parsereturnsany.

So now the unsafe value can spread through the program before we validate it.

Instead, we can keep the boundary small

import
 
{
 
safeJsonParse
 
}
 
from
 
"
is-kit
"
;

declare
 
const
 
body
:
 
string
;

const
 
result
 
=
 
safeJsonParse
(
body
,
 
isUser
);

if 
(
!
result
.
valid
)
 
{

 
return
 
{
 
status
:
 
400
 
as
 
const
 
};

}

renderUser
(
result
.
value
);

Enter fullscreen mode

Exit fullscreen mode

Conceptually, the flow is

JSON text
 ↓
decode
 ↓
unknown
 ↓
guard
 ↓
validated value

Enter fullscreen mode

Exit fullscreen mode

Invalid JSON and guard failures both produce

{

 
valid
:
 
false
;

}

Enter fullscreen mode

Exit fullscreen mode

And again, nothing is coerced just to make the value pass.

I like this because the unsafe part stays right at the decode boundary.

## 🚪 Should Extra Keys Be Allowed?

There is another small design choice that appears at object boundaries.

Suppose we expect

{

 
username
:
 
string
;

 
password
:
 
string
;

}

Enter fullscreen mode

Exit fullscreen mode

Should this also be accepted?

{

 
username
:
 
"
Neko
"
,

 
password
:
 
"
secret
"
,

 
admin
:
 
true
,

}

Enter fullscreen mode

Exit fullscreen mode

Withstruct, extra keys are allowed by default.

That is often useful for API responses because a server may add a new field without breaking an older client.

But sometimes we really want a closed object shape.

Then we can use

const
 
isCredentials
 
=
 
struct
(

 
{

 
username
:
 
isString
,

 
password
:
 
isString
,

 
},

 
{
 
exact
:
 
true
 
},

);

Enter fullscreen mode

Exit fullscreen mode

Now

isCredentials
({

 
username
:
 
"
Neko
"
,

 
password
:
 
"
secret
"
,

});

// true

Enter fullscreen mode

Exit fullscreen mode

while

isCredentials
({

 
username
:
 
"
Neko
"
,

 
password
:
 
"
secret
"
,

 
admin
:
 
true
,

});

// false

Enter fullscreen mode

Exit fullscreen mode

The important part is not that one mode is always better.

It is that the boundary should express the contract we actually want.

## 🤔 So Do We Still Need Schema Libraries?

Yes.

Sometimes absolutely.

A type guard toolkit and a schema library overlap a little, but they are not trying to solve exactly the same problem.

For example, a schema library is probably the better choice when we need:

* structured validation errors with field paths
* multiple validation issues at once
* coercion
* default values
* transformations
* schema-generated types or external artifacts
* deep integration with a form or API framework

Those are larger validation workflows.

is-kitasks a narrower question

Does this value satisfy this runtime predicate?

If yes, what can TypeScript safely narrow it to?

Enter fullscreen mode

Exit fullscreen mode

That narrower model is sometimes exactly what I want.

For example

Approach

Good fit

Inline 
typeof
 checks

One small local condition

Type guards

Reusable boolean validation and narrowing

Schema library

Rich validation, transformation, and schema workflows

So I don't think the question is

Type guards or schema libraries—which one wins?

The more useful question is

What is the smallest validation model that solves this boundary?

## 🎯 The Important Part

I started with a simple value

declare
 
const
 
input
:
 
unknown
;

Enter fullscreen mode

Exit fullscreen mode

The tempting shortcut was

const
 
user
 
=
 
input
 
as
 
User
;

Enter fullscreen mode

Exit fullscreen mode

But that only changes TypeScript's belief.

It does not establish runtime trust.

A runtime guard gives us a much more useful flow

unknown
 ↓
runtime check
 ↓
narrowed value

Enter fullscreen mode

Exit fullscreen mode

And when we want a result-oriented API

unknown
 ↓
guard
 ↓
safeParse
 ↓
{ valid: true, value }
or
{ valid: false }

Enter fullscreen mode

Exit fullscreen mode

No hidden conversion.

No assertion pretending the check already happened.

Just small runtime rules that TypeScript can understand too. 😸

If you want to see the full guide, including JSON boundaries, exact objects, and custom domain refinements:

## Validate unknown in TypeScript Without a Schema Library | is-kit

Validate unknown TypeScript values with small composable type guards and safeParse, without adopting a schema-first validation workflow.

 is-kit.dev
 

And if you want to exploreis-kititself:

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

If it looks useful, a ⭐ on GitHub is always very welcome!

Thanks for reading! 🙌

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse