---
title: Your Type Guard Can Silently Drift from Your TypeScript Type 🔧 - DEV Community
url: https://dev.to/nyaomaru/your-type-guard-can-silently-drift-from-your-typescript-type-o57
site_name: devto
content_file: devto-your-type-guard-can-silently-drift-from-your-types
fetched_at: '2026-09-29T16:48:43.581103'
original_url: https://dev.to/nyaomaru/your-type-guard-can-silently-drift-from-your-typescript-type-o57
author: nyaomaru
date: '2026-09-23'
description: Hoi hoi! 👋 I'm @nyaomaru, a frontend engineer just back from a short vacation on Texel, a small... Tagged with typescript, javascript, webdev, opensource.
tags: '#typescript, #javascript, #webdev, #opensource'
---

Forgotten guard updates risk silent runtime bugs

Hoi hoi! 👋

I'm@nyaomaru, a frontend engineer just back from a short vacation on Texel, a small island in the Netherlands. 😸🏝️

Today, let's talk about a type guard that looks completely safe.

const
 
isUser
 
=
 
(
value
:
 
unknown
):
 
value
 
is
 
User
 
=>
 
{

 
// runtime checks...

};

Enter fullscreen mode

Exit fullscreen mode

Looks good, right?

TypeScript knows that whenisUser(value)returnstrue, the value is aUser.

But there's a small problem

TypeScript trusts that promise.

It doesn't prove that your runtime checks actually validate every field inUser.

And that's where type guards can slowly drift away from the types they claim to protect.

Let's take a look! 👀

## 🕳️ A Type Guard Can Become Outdated Without an Error

Imagine we start with this type

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

Enter fullscreen mode

Exit fullscreen mode

And a hand-written type guard

const
 
isUser
 
=
 
(
value
:
 
unknown
):
 
value
 
is
 
User
 
=>
 
{

 
if 
(
typeof
 
value
 
!==
 
"
object
"
 
||
 
value
 
===
 
null
)
 
{

 
return
 
false
;

 
}

 
const
 
candidate
 
=
 
value
 
as
 
Record
<
string
,
 
unknown
>
;

 
return
 
typeof
 
candidate
.
id
 
===
 
"
string
"
 
&&
 
typeof
 
candidate
.
name
 
===
 
"
string
"
;

};

Enter fullscreen mode

Exit fullscreen mode

So far, everything matches.

Later, we updateUser

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

 
role
:
 
"
admin
"
 
|
 
"
member
"
;

};

Enter fullscreen mode

Exit fullscreen mode

But we forget to update the guard.

const
 
isUser
 
=
 
(
value
:
 
unknown
):
 
value
 
is
 
User
 
=>
 
{

 
if 
(
typeof
 
value
 
!==
 
"
object
"
 
||
 
value
 
===
 
null
)
 
{

 
return
 
false
;

 
}

 
const
 
candidate
 
=
 
value
 
as
 
Record
<
string
,
 
unknown
>
;

 
return
 
typeof
 
candidate
.
id
 
===
 
"
string
"
 
&&
 
typeof
 
candidate
.
name
 
===
 
"
string
"
;

};

Enter fullscreen mode

Exit fullscreen mode

There is norolecheck.

But this still compiles. 😿

## 🧠 Why Doesn't TypeScript Catch This?

Because this

(
value
:
 
unknown
):
 
value
 
is
 
User

Enter fullscreen mode

Exit fullscreen mode

is a user-defined type predicate.

You are telling TypeScript

Trust me. If this function returnstrue, the value is aUser.

TypeScript can check whether the declared predicate type itself makes sense.

But it cannot generally prove that arbitrary runtime logic actually validates every part of that type.

So this is possible

const
 
isUser
 
=
 
(
_value
:
 
unknown
):
 
_value
 
is
 
User
 
=>
 
true
;

Enter fullscreen mode

Exit fullscreen mode

Terrible guard.

Perfectly valid TypeScript. 😹

The return type is a contract written by us, not a proof generated from the function body.

## 🔄 This Becomes a Maintenance Problem

The annoying part isn't writing the guard once.

It's keeping these two things synchronized over time

TypeScript type
 ↕
Runtime validation

Enter fullscreen mode

Exit fullscreen mode

Types change.

Properties get

* added
* removed
* renamed
* made optional
* changed to another type

And every time that happens, we need to remember that some runtime guard somewhere may also need an update.

If we forget, the compiler may not tell us.

That's the kind of bug I really don't want to rely on memory to prevent.

## ✅ What If the Type Could Be the Contract?

This is one of the reasons I addedtypedStructtois-kit.

Suppose the application type already exists:

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

 
age
?:
 
number
;

};

Enter fullscreen mode

Exit fullscreen mode

We can build the guard against that existing type

import
 
{
 
isNumber
,
 
isString
,
 
optionalKey
,
 
typedStruct
 
}
 
from
 
"
is-kit
"
;

const
 
isUser
 
=
 
typedStruct
<
User
>
()({

 
id
:
 
isString
,

 
name
:
 
isString
,

 
age
:
 
optionalKey
(
isNumber
),

});

Enter fullscreen mode

Exit fullscreen mode

Now the field map has a type-level relationship withUser.

At runtime, it still performs ordinary object validation.

But at compile time, TypeScript can check whether the guards we declared match the object type they're supposed to follow.

## 💥 Now Drift Becomes Visible

Let's add a field again

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

 
role
:
 
"
admin
"
 
|
 
"
member
"
;

 
age
?:
 
number
;

};

Enter fullscreen mode

Exit fullscreen mode

But forget to update the guard

typedStruct
<
User
>
()({

 
id
:
 
isString
,

 
name
:
 
isString
,

 
age
:
 
optionalKey
(
isNumber
),

 
// TypeScript error:

 
// role is missing

});

Enter fullscreen mode

Exit fullscreen mode

Nice.

The runtime bug became a compile-time problem.

The same thing happens if the guard uses an incompatible field type

import
 
{

 
isNumber
,

 
isString
,

 
oneOfValues
,

 
optionalKey
,

 
typedStruct
,

}
 
from
 
"
is-kit
"
;

typedStruct
<
User
>
()({

 
id
:
 
isString
,

 
name
:
 
isNumber
,

 
// TypeScript error:

 
// User["name"] is string

 
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

 
age
:
 
optionalKey
(
isNumber
),

});

Enter fullscreen mode

Exit fullscreen mode

This is the part I care about most.

typedStructdoesn't eliminate maintenance.

It makes forgotten maintenance visible.

## 🧩 Optional and Nullable Are Different

Another place where object guards can get confusing is optional properties.

Consider:

type
 
User
 
=
 
{

 
id
:
 
string
;

 
nickname
?:
 
string
 
|
 
null
;

};

Enter fullscreen mode

Exit fullscreen mode

There are two separate ideas here

nickname may be absent

Enter fullscreen mode

Exit fullscreen mode

and

nickname may exist with the value null

Enter fullscreen mode

Exit fullscreen mode

Those are different runtime contracts.

WithtypedStruct

import
 
{
 
isString
,
 
nullable
,
 
optionalKey
,
 
typedStruct
 
}
 
from
 
"
is-kit
"
;

const
 
isUser
 
=
 
typedStruct
<
User
>
()({

 
id
:
 
isString
,

 
nickname
:
 
optionalKey
(
nullable
(
isString
)),

});

Enter fullscreen mode

Exit fullscreen mode

Now

isUser
({
 
id
:
 
"
user-1
"
 
});

// true

isUser
({

 
id
:
 
"
user-1
"
,

 
nickname
:
 
null
,

});

// true

isUser
({

 
id
:
 
"
user-1
"
,

 
nickname
:
 
"
Neko
"
,

});

// true

isUser
({

 
id
:
 
"
user-1
"
,

 
nickname
:
 
42
,

});

// false

Enter fullscreen mode

Exit fullscreen mode

I like keeping these two decisions explicit:

* optionalKey(...)→ the property may be absent
* nullable(...)→ the value may benull

They look similar at first, but they describe different things.

## 🌳 Nested Types Don't Need to Be Duplicated Either

Now imagine a larger type:

type
 
Account
 
=
 
{

 
readonly
 
id
:
 
string
;

 
readonly
 
profile
:
 
{

 
readonly
 
displayName
:
 
string
;

 
readonly
 
bio
:
 
string
 
|
 
null
;

 
}
 
|
 
null
;

 
readonly
 
tags
:
 
readonly
 
string
[];

};

Enter fullscreen mode

Exit fullscreen mode

We could manually copy the profile shape into another type.

But that creates another thing that can drift.

Instead, we can reference the type we already have

import
 
{
 
arrayOf
,
 
isString
,
 
nullable
,
 
typedStruct
 
}
 
from
 
"
is-kit
"
;

const
 
isProfile
 
=
 
typedStruct
<
NonNullable
<
Account
[
"
profile
"
]
>>
()({

 
displayName
:
 
isString
,

 
bio
:
 
nullable
(
isString
),

});

const
 
isAccount
 
=
 
typedStruct
<
Account
>
()({

 
id
:
 
isString
,

 
profile
:
 
nullable
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

This is the model I like:

Reuse the existing type at compile time. Compose small guards at runtime.

The application type remains the source we want the guard to follow.

## 🔒 What About Extra Runtime Properties?

There is another distinction worth making.

These are two different questions:

1. Does myguard definitionmatch the TypeScript type?
2. Should aruntime objectbe allowed to contain additional properties?

By default, an object can still have additional keys.

If you want the runtime object shape to be closed as well, you can enable exact mode:

import
 
{
 
isString
,
 
typedStruct
 
}
 
from
 
"
is-kit
"
;

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

const
 
isExactUser
 
=
 
typedStruct
<
User
>
()(

 
{

 
id
:
 
isString
,

 
name
:
 
isString
,

 
},

 
{

 
exact
:
 
true
,

 
},

);

Enter fullscreen mode

Exit fullscreen mode

Then:

isExactUser
({

 
id
:
 
"
user-1
"
,

 
name
:
 
"
Ada
"
,

});

// true

isExactUser
({

 
id
:
 
"
user-1
"
,

 
name
:
 
"
Ada
"
,

 
debug
:
 
true
,

});

// false

Enter fullscreen mode

Exit fullscreen mode

Whether extra properties should be rejected is a runtime policy decision.

It shouldn't be confused with keeping the guard definition synchronized with the TypeScript type.

## ⚖️ Which Should Be the Source of Truth?

I don't think there is one correct validation style for every project.

The important question is

What already owns the shape of this data?

### Manual predicate

const
 
isSomething
 
=
 
(
value
:
 
unknown
):
 
value
 
is
 
Something
 
=>
 
{

 
// custom logic

};

Enter fullscreen mode

Exit fullscreen mode

Great when the validation is unusual or not primarily structural.

### Guard-first

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

});

Enter fullscreen mode

Exit fullscreen mode

Useful when the guard itself should define the resulting type.

### Type-first

const
 
isUser
 
=
 
typedStruct
<
User
>
()({

 
id
:
 
isString
,

 
name
:
 
isString
,

});

Enter fullscreen mode

Exit fullscreen mode

Useful whenUseralready exists and the runtime guard needs to stay aligned with it.

### Schema-first

A schema library or code generation may be the better source of truth when you need things like:

* structured validation errors
* coercion
* transforms
* defaults
* generated artifacts

These solve different problems.

I don't think every boolean validation check needs to become a schema. 😸

## 🚫 WhattypedStructDoes Not Do

There are some important boundaries.

typedStructdoesnotgenerate runtime validation from a TypeScript type.

Types are erased at runtime, so you still need to declare the guards you want to execute.

It also doesn't:

* prove that every custom predicate is honest
* coerce values
* return rich structured validation errors
* replace schema-first workflows
* validate numeric or symbol properties as part of its string-keyed object contract

It's intentionally smaller than that.

The goal is simply to create a typed bridge between

the object type you already have

and

the runtime guards you choose to run

## 🎯 The Important Part

The main point isn't reallytypedStruct.

It's this

A type predicate is a promise, not a proof.

This

(
value
):
 
value
 
is
 
User

Enter fullscreen mode

Exit fullscreen mode

doesn't mean TypeScript inspected your implementation and proved that everyUserfield was validated.

We made that promise.

So when a TypeScript type is the source of truth, I think it's useful to make the runtime guard structurally depend on that type instead of relying on us to remember every future change.

That's what I wantedtypedStructto help with. 😸

If your guard defines the type, use a guard-first approach.

If an existing TypeScript type should define the contract, connect the guard to that type.

And if you need rich parsing, transforms, coercion, or detailed errors, that's where a schema starts to earn its weight.

I wrote a more complete guide about this on the is-kit documentation site:

## Keep Type Guards in Sync with TypeScript Types | is-kit

Keep hand-written runtime guards aligned with existing string-keyed TypeScript object types using typedStruct and field-level checks.

 is-kit.dev
 

If you like small reusable TypeScript type guards,is-kitis open source too!

## nyaomaru/is-kit

### Build small guards. Compose them. Lightweight, zero-dependency TypeScript type guards for runtime validation and natural narrowing. Runtime-safe 🛡️, composable 🧩, and ergonomic ✨.

# is-kit

## Build small guards. Compose them.

is-kitis a lightweight, zero-dependency toolkit for building reusable TypeScripttype guards.

It helps you write smallisFoofunctions, compose them intoricher runtime checks, and keepTypeScript narrowingnatural inside regular control flow.

Runtime-safe🛡️,composable🧩, andergonomic✨ without asking you to adopt a heavy schema workflow.

* Build and reusetyped guards
* Compose guardswithand,or,not,oneOf
* Validate objectshapes and collections
* Parse or assertunknownvalues without a large schema framework

📚 Documentation Site·🧭 Practical Guides

Best forapp-internal narrowing, filtering, and reusable guards.

## 🤔 Why useis-kit?

Tired of rewriting the sameisFoochecks again and again?

is-kitis a good fit when you want to:

* write reusableisXfunctions instead of one-off inline checks
* keep runtime validationlightweight and dependency-free
* narrow values directlyinif,filter…

View on GitHub

Thanks for reading! 🙌

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (28 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse