---
title: I Compared 6 TypeScript Validation Libraries. Here's What Surprised Me 🤔 - DEV Community
url: https://dev.to/nyaomaru/i-compared-6-typescript-validation-libraries-heres-what-surprised-me-325g
site_name: devto
content_file: devto-i-compared-6-typescript-validation-libraries-heres
fetched_at: '2026-10-29T20:59:59.395924'
original_url: https://dev.to/nyaomaru/i-compared-6-typescript-validation-libraries-heres-what-surprised-me-325g
author: nyaomaru
date: '2026-10-28'
description: Hoi hoi! 👋 &nbsp; I'm nyaomaru, a frontend engineer and OSS developer working mostly with... Tagged with typescript, opensource, webdev, frontend.
tags: '#typescript, #opensource, #webdev, #frontend'
---

The hidden danger of mismatched runtime contracts

Hoi hoi! 👋

I'm nyaomaru, a frontend engineer and OSS developer working mostly with TypeScript.

When we need runtime validation in TypeScript, the conversation often turns into this 👇

"Which library should I use?"

* Zod?
* Valibot?
* ArkType?
* typia?

Or maybe,just write a type guard?

I maintainis-kit, so I think about this boundary quite a lot.

And recently I started wondering

Are we comparing libraries that are actually solving the same problem?

For example, if all I want is this

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
;

}

Enter fullscreen mode

Exit fullscreen mode

do I really need a schema system?

But if I want:

* structured validation errors
* transformations
* parsing
* schema metadata
* framework integrations

then a small boolean guard is probably not enough either.

So instead of asking"Which validator is best?", I tried a different comparison.

I implemented the sameUservalidation with:

* a handwritten guard with a TypeScript predicate
* is-kit
* Runtypes
* Valibot
* Zod
* ArkType
* typia

Then I compiled, tested them against the same fixtures, measured standalone browser bundle size, and ran a small steady-state runtime benchmark.

The hardest part was not making seven validators compile.

It wasmaking seven validators mean the same thing.

Even “a string with at most 100 characters” can describe different runtime contracts.

So, let's look at what each tool is actually buying us. 😺

## 🧪 The User we will validate

Here is the shared type.

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
:
 
number
;

 
role
:
 
"
admin
"
 
|
 
"
user
"
;

 
tags
:
 
string
[];

 
profile
:
 
{

 
bio
:
 
string
;

 
active
:
 
boolean
;

 
};

};

Enter fullscreen mode

Exit fullscreen mode

And the runtime rules are:

* idmust be a string
* namemust contain 1–100 UTF-16 code units
* agemust be an integer from 18 to 120
* rolemust be exactly"admin"or"user"
* tagsmust be an array of strings
* profile.biomust be a string
* profile.activemust be a boolean
* extra keys are rejected at the root and insideprofile
* values are not coerced

For this comparison, the main input domain isordinary JSON-decoded data.

That matters because JavaScript can also give us strange things like inherited properties, sparse arrays, symbols, getters, and non-enumerable keys.

We'll come back to those later.

## 1. ✍️ Handwritten Guard — Sometimes a Guard Is Enough

Let's start with the boring option, a handwritten JavaScript guard with a TypeScript predicate.

No validation library.

const
 
isRecord
 
=
 
(
value
:
 
unknown
):
 
value
 
is
 
Record
<
string
,
 
unknown
>
 
=>

 
typeof
 
value
 
===
 
"
object
"
 
&&
 
value
 
!==
 
null
 
&&
 
!
Array
.
isArray
(
value
);

const
 
hasExactKeys
 
=
 
(

 
value
:
 
Record
<
string
,
 
unknown
>
,

 
keys
:
 
readonly
 
string
[],

):
 
boolean
 
=>

 
Object
.
keys
(
value
).
length
 
===
 
keys
.
length
 
&&

 
keys
.
every
((
key
)
 
=>
 
Object
.
hasOwn
(
value
,
 
key
));

export
 
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

 
!
isRecord
(
value
)
 
||

 
!
hasExactKeys
(
value
,
 
[
"
id
"
,
 
"
name
"
,
 
"
age
"
,
 
"
role
"
,
 
"
tags
"
,
 
"
profile
"
])

 
)
 
{

 
return
 
false
;

 
}

 
if 
(

 
!
isRecord
(
value
.
profile
)
 
||

 
!
hasExactKeys
(
value
.
profile
,
 
[
"
bio
"
,
 
"
active
"
])

 
)
 
{

 
return
 
false
;

 
}

 
return 
(

 
typeof
 
value
.
id
 
===
 
"
string
"
 
&&

 
typeof
 
value
.
name
 
===
 
"
string
"
 
&&

 
value
.
name
.
length
 
>=
 
1
 
&&

 
value
.
name
.
length
 
<=
 
100
 
&&

 
typeof
 
value
.
age
 
===
 
"
number
"
 
&&

 
Number
.
isInteger
(
value
.
age
)
 
&&

 
value
.
age
 
>=
 
18
 
&&

 
value
.
age
 
<=
 
120
 
&&

 
(
value
.
role
 
===
 
"
admin
"
 
||
 
value
.
role
 
===
 
"
user
"
)
 
&&

 
Array
.
isArray
(
value
.
tags
)
 
&&

 
value
.
tags
.
every
((
tag
)
 
=>
 
typeof
 
tag
 
===
 
"
string
"
)
 
&&

 
typeof
 
value
.
profile
.
bio
 
===
 
"
string
"
 
&&

 
typeof
 
value
.
profile
.
active
 
===
 
"
boolean
"

 
);

};

Enter fullscreen mode

Exit fullscreen mode

And then

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

}

Enter fullscreen mode

Exit fullscreen mode

This is still very good.

For one local boundary, a handwritten type guard has a huge advantage

There is no extra model to learn.

It is just JavaScript runtime checks plus a TypeScript predicate.

But the cost starts to appear when your codebase grows this

isUser
;

isProfile
;

isRole
;

isNonEmptyString
;

isAdultAge
;

isStringArray
;

isApiResponse
;

isConfig
;

isFeatureFlag
;

Enter fullscreen mode

Exit fullscreen mode

Now you are not writing "one guard" anymore.

You are maintaining your own tiny guard library.

And this is where the next option starts to make sense. 👍

## 2. 🔧 is-kit — When Small Guards Become Reusable Building Blocks

This is the problem I builtis-kitaround.

I didn't want a schema-first workflow for every narrowing problem.

I wanted small guards that stay small, but compose cleanly.

import
 
{

 
and
,

 
arrayOf
,

 
isBoolean
,

 
isNumber
,

 
isString
,

 
oneOfValues
,

 
predicateToRefine
,

 
safeParse
,

 
struct
,

}
 
from
 
"
is-kit
"
;

export
 
const
 
isName
 
=
 
and
(

 
isString
,

 
predicateToRefine
<
string
>
(

 
(
value
)
 
=>
 
value
.
length
 
>=
 
1
 
&&
 
value
.
length
 
<=
 
100
,

 
),

);

export
 
const
 
isAge
 
=
 
and
(

 
isNumber
,

 
predicateToRefine
<
number
>
(

 
(
value
)
 
=>
 
Number
.
isInteger
(
value
)
 
&&
 
value
 
>=
 
18
 
&&
 
value
 
<=
 
120
,

 
),

);

export
 
const
 
isProfile
 
=
 
struct
(

 
{

 
bio
:
 
isString
,

 
active
:
 
isBoolean
,

 
},

 
{
 
exact
:
 
true
 
},

);

export
 
const
 
isUser
 
=
 
struct
(

 
{

 
id
:
 
isString
,

 
name
:
 
isName
,

 
age
:
 
isAge
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
user
"
),

 
tags
:
 
arrayOf
(
isString
),

 
profile
:
 
isProfile
,

 
},

 
{
 
exact
:
 
true
 
},

);

export
 
const
 
parseUser
 
=
 
(
input
:
 
unknown
)
 
=>
 
safeParse
(
isUser
,
 
input
);

Enter fullscreen mode

Exit fullscreen mode

The important part is that the pieces remain normal guards

const
 
names
 
=
 
values
.
filter
(
isName
);

if 
(
isAge
(
value
))
 
{

 
// value is number

}

Enter fullscreen mode

Exit fullscreen mode

That is useful whenyour codebase already thinks in terms of predicates.

And this is also where I would draw the line.

safeParse()gives a small success/failure result around a guard.

It doesnotturnis-kitinto:

* a field-level issue system
* a transformation pipeline
* a schema metadata system
* an OpenAPI ecosystem
* a form integration layer

If those are the actual requirements, I would rather use a schema library than try to make a guard toolkit become one.

One type-level detail also showed up in the verification,struct()andarrayOf()infer readonly structures.

So the runtime shape matches ourUser, butreadonly string[]is not assignable to mutablestring[].

That difference is real, and the type tests make it explicit instead of hiding it with a cast. 🔧

## 3. 🏃 Runtypes — A Validator Object, Not Just a Predicate

Runtypesmoves one level further.

Instead of just a boolean predicate, you get a runtime validator object with several ways to consume it.

import
 
{

 
Array
 
as 
RtArray
,

 
Boolean
 
as 
RtBoolean
,

 
Literal
,

 
Number
 
as 
RtNumber
,

 
Object
 
as 
RtObject
,

 
String
 
as 
RtString
,

 
Union
,

}
 
from
 
"
runtypes
"
;

const
 
Name
 
=
 
RtString
.
withConstraint
(

 
(
value
)
 
=>

 
(
value
.
length
 
>=
 
1
 
&&
 
value
.
length
 
<=
 
100
)
 
||
 
"
name length must be 1..100
"
,

);

const
 
Age
 
=
 
RtNumber
.
withConstraint
(

 
(
value
)
 
=>

 
(
Number
.
isInteger
(
value
)
 
&&
 
value
 
>=
 
18
 
&&
 
value
 
<=
 
120
)
 
||

 
"
age must be an integer in 18..120
"
,

);

export
 
const
 
UserSchema
 
=
 
RtObject
({

 
id
:
 
RtString
,

 
name
:
 
Name
,

 
age
:
 
Age
,

 
role
:
 
Union
(
Literal
(
"
admin
"
),
 
Literal
(
"
user
"
)),

 
tags
:
 
RtArray
(
RtString
),

 
profile
:
 
RtObject
({

 
bio
:
 
RtString
,

 
active
:
 
RtBoolean
,

 
}).
exact
(),

}).
exact
();

export
 
const
 
isUser
 
=
 
(
input
:
 
unknown
)
 
=>
 
UserSchema
.
guard
(
input
);

export
 
const
 
checkUser
 
=
 
(
input
:
 
unknown
)
 
=>
 
UserSchema
.
check
(
input
);

export
 
const
 
parseUser
 
=
 
(
input
:
 
unknown
)
 
=>
 
UserSchema
.
parse
(
input
);

export
 
const
 
inspectUser
 
=
 
(
input
:
 
unknown
)
 
=>
 
UserSchema
.
inspect
(
input
);

Enter fullscreen mode

Exit fullscreen mode

This feels different from a guard toolkit.

A predicate mainly answers

Is this value aUser?

ARuntypecan also answer that question, but the same object can:

* narrow withguard
* throw withcheck
* parse withparse
* expose structured failure data

Also,check()andparse()should not be treated as synonyms.

Runtypessupports parser behavior, and object handling can differ between validation and parsing contexts.

That is exactly the kind of runtime machinery you do not have in a plain predicate. 🏃

## 4. 🤖 Valibot — Schema Validation With a Modular API

Valibotis where the comparison starts looking more "schema-like".

import
 
*
 
as 
v
 
from
 
"
valibot
"
;

export
 
const
 
UserSchema
 
=
 
v
.
strictObject
({

 
id
:
 
v
.
string
(),

 
name
:
 
v
.
pipe
(
v
.
string
(),
 
v
.
minLength
(
1
),
 
v
.
maxLength
(
100
)),

 
age
:
 
v
.
pipe
(
v
.
number
(),
 
v
.
integer
(),
 
v
.
minValue
(
18
),
 
v
.
maxValue
(
120
)),

 
role
:
 
v
.
picklist
([
"
admin
"
,
 
"
user
"
]),

 
tags
:
 
v
.
array
(
v
.
string
()),

 
profile
:
 
v
.
strictObject
({

 
bio
:
 
v
.
string
(),

 
active
:
 
v
.
boolean
(),

 
}),

});

export
 
const
 
isUser
 
=
 
(
input
:
 
unknown
)
 
=>
 
v
.
is
(
UserSchema
,
 
input
);

export
 
const
 
parseUser
 
=
 
(
input
:
 
unknown
)
 
=>
 
v
.
safeParse
(
UserSchema
,
 
input
);

Enter fullscreen mode

Exit fullscreen mode

This gives us:

* schema validation
* type inference
* structured issues
* parsing APIs
* transformation pipelines

But the API is still function-based and modular.

That is a big part ofValibot's design.

Instead of every capability living as methods on large schema objects, you compose independent functions.

That makes tree shaking a first-class part of the normal API.

And unlike a pure schema-only mental model,Valibotalso exposesv.is()as a type guard.

So schema validation and ordinary TypeScript narrowing are not mutually exclusive.

One caveat:v.is()is the guard path. It does not expose validation issues or apply transformations like parsing does. 🤖

## 5. 💎 Zod — When the Schema Is Part of a Bigger Ecosystem

NowZod.

import
 
*
 
as 
z
 
from
 
"
zod
"
;

export
 
const
 
UserSchema
 
=
 
z
.
strictObject
({

 
id
:
 
z
.
string
(),

 
name
:
 
z

 
.
string
()

 
.
refine
(

 
(
value
)
 
=>
 
value
.
length
 
>=
 
1
 
&&
 
value
.
length
 
<=
 
100
,

 
"
name must contain 1..100 UTF-16 code units
"
,

 
),

 
age
:
 
z
.
int
().
min
(
18
).
max
(
120
),

 
role
:
 
z
.
enum
([
"
admin
"
,
 
"
user
"
]),

 
tags
:
 
z
.
array
(
z
.
string
()),

 
profile
:
 
z
.
strictObject
({

 
bio
:
 
z
.
string
(),

 
active
:
 
z
.
boolean
(),

 
}),

});

export
 
type
 
User
 
=
 
z
.
output
<
typeof
 
UserSchema
>
;

export
 
const
 
parseUser
 
=
 
(
input
:
 
unknown
)
 
=>
 
UserSchema
.
safeParse
(
input
);

// This schema has no transforms, so its output type is safe for the input too.

export
 
const
 
isUser
 
=
 
(
input
:
 
unknown
):
 
input
 
is
 
User
 
=>
 
parseUser
(
input
).
success
;

Enter fullscreen mode

Exit fullscreen mode

Zoddoes not expose a built-inis()method, but this adapter can narrowinputbecause this schema has no transforms. With a transforming schema,safeParse().datais the safe typed value: the original input and output types may differ.

Zodis not interesting because it can validate aUser.

All of these libraries can do that.

The real value is everything around the schema:

* form integrations
* API tooling
* schema conversion
* metadata
* codecs
* OpenAPI-related tooling
* framework integrations

If your schema is already becoming part of application infrastructure, that ecosystem matters. 💎

There is one important detail in this sample though.

I didnotuse this

z
.
string
().
min
(
1
).
max
(
100
);

Enter fullscreen mode

Exit fullscreen mode

Why?

Because our contract says

1–100 UTF-16 code units

Zod's built-in string length checks use Unicode code points, so this sample uses.refine()with JavaScript'sstring.lengthto preserve the stated UTF-16 contract. The shared emoji fixture demonstrates why below.

### What about bundle size?

It is too easy to write

Valibotis small,Zodis large.

That is not a good 2026 comparison anymore.

Zod also hasZod Mini, which uses a more functional, tree-shakable API.

The bundle table later in this article measuresregular Zod, not Zod Mini.

So it should not be read asValibotversus the smallest possibleZodsetup.

Zodcan also compile optimized validation logic at runtime withz.compile()andnew Function.

I did not enable it here.

That makes this distinction more useful than the broad label “generated validation”

runtime schema compilation
 vs
build-time generation from TypeScript types

Enter fullscreen mode

Exit fullscreen mode

That distinction becomes important when we get totypia.

## 6. 🚢 ArkType — What If the Runtime Schema Looked Like TypeScript?

ArkTypehas a very different authoring model.

import
 
{
 
type
 
}
 
from
 
"
arktype
"
;

export
 
const
 
UserSchema
 
=
 
type
({

 
id
:
 
"
string
"
,

 
name
:
 
"
0 < string <= 100
"
,

 
age
:
 
"
18 <= number.integer <= 120
"
,

 
role
:
 
"
'admin' | 'user'
"
,

 
tags
:
 
"
string[]
"
,

 
profile
:
 
{

 
bio
:
 
"
string
"
,

 
active
:
 
"
boolean
"
,

 
},

}).
onDeepUndeclaredKey
(
"
reject
"
);

export
 
const
 
isUser
 
=
 
(
input
:
 
unknown
)
 
=>
 
UserSchema
.
allows
(
input
);

export
 
const
 
parseUser
 
=
 
(
input
:
 
unknown
)
 
=>
 
UserSchema
(
input
);

export
 
const
 
ArkErrors
 
=
 
type
.
errors
;

Enter fullscreen mode

Exit fullscreen mode

I like this comparison

z
.
int
().
min
(
18
).
max
(
120
);

Enter fullscreen mode

Exit fullscreen mode

vs

"
18 <= number.integer <= 120
"
;

Enter fullscreen mode

Exit fullscreen mode

Neither is "better".

They are different ways to express the runtime contract.

If your team already thinks naturally in TypeScript-like expressions,ArkTypeis very readable.

allows()also works as a type guard.

And calling the schema directly gives you validated output or an error collection.

Another interesting part:ArkTypecan precompile optimized traversal logic at runtime when the environment allowsnew Function.

SoArkTypeis already doing specialization. 🚢

But it is still not the same architecture astypia.

ArkTypestarts from a runtime type representation.

typiastarts from TypeScript types during the build.

## 7. 🚀 typia — Generate the Validator During the Build

typiais the outlier in this comparison.

import
 
typia
,
 
{
 
type
 
tags
 
}
 
from
 
"
typia
"
;

type
 
Utf16Name
 
=
 
tags
.
TagBase
<
{

 
kind
:
 
"
utf16Name
"
;

 
target
:
 
"
string
"
;

 
value
:
 
undefined
;

 
validate
:
 
"
$input.length >= 1 && $input.length <= 100
"
;

}
>
;

export
 
interface
 
User
 
{

 
id
:
 
string
;

 
name
:
 
string
 
&
 
Utf16Name
;

 
age
:
 
number
 
&
 
tags
.
Type
<
"
uint32
"
>
 
&
 
tags
.
Minimum
<
18
>
 
&
 
tags
.
Maximum
<
120
>
;

 
role
:
 
"
admin
"
 
|
 
"
user
"
;

 
tags
:
 
string
[];

 
profile
:
 
{

 
bio
:
 
string
;

 
active
:
 
boolean
;

 
};

}

export
 
const
 
isUser
 
=
 
typia
.
createEquals
<
User
>
();

export
 
const
 
validateUser
 
=
 
typia
.
createValidateEquals
<
User
>
();

Enter fullscreen mode

Exit fullscreen mode

This is not a runtime schema object.

The source of truth is the TypeScript type plustypia's tags.

Thentypia's build transform turns

typia
.
createEquals
<
User
>
();

Enter fullscreen mode

Exit fullscreen mode

into specialized validation code.

That means there is no general runtime schema interpreter walking aUserschema object.

But there is a trade-off

You need build integration.

The current official setup uses TypeScript 7 andttsc/ typia's transform integration.

Stocktscalone does not run the transform.

In my verification workspace, the firsttypiabuild also had to compile a Go source plugin and took several minutes.

That setup cost is not part of the runtime benchmark, but it is absolutely part of the adoption decision.

Also,typia's built-inMinLength/MaxLengthdid not match our UTF-16 contract.

So I used a custom tag forname.

Again, same-looking validation rule, different semantics. 🚀

## 😹 Wait, Even "String Length" Was Different?

This was the first test that made me stop.

"
😀
"
.
repeat
(
51
).
length
;

// 102

Enter fullscreen mode

Exit fullscreen mode

JavaScript'sstring.lengthcounts UTF-16 code units.

So with our contract

maximum = 100 UTF-16 code units

Enter fullscreen mode

Exit fullscreen mode

this should fail.

And it did fail in:

* handwritten guard
* is-kit
* Runtypes
* Valibot
* ArkType

But the originalZodandtypiasamples accepted it.

Why?

Because theirbuilt-in length constraints count Unicode code points instead.

For this string

51 emoji
= 51 code points
= 102 UTF-16 code units

Enter fullscreen mode

Exit fullscreen mode

Neither behavior is wrong.

They are just different contracts.

And neither one necessarily matches "what a human sees" either, because grapheme clusters make Unicode even more fun. 😹

So I changed theZodsample to.refine()andtypiato a custom tag.

That was probably the most useful lesson in the whole comparison 👇

Equivalent-looking schemas are not automatically equivalent runtime contracts.

## So What Are We Actually Comparing?

At this point, these no longer look like seven interchangeable libraries.

They are different runtime models.

Approach

Source of truth          

Natural success API                      

Structured failures      

Transformation model      

Compilation / build requirement                          

Handwritten guard

Type + handwritten check  

Predicate                                

Manual                    

Manual                    

None                                                      

is-kit  

Composed guards          

Predicate / 
safeParse
                  

Basic valid/invalid result

Guard-oriented            

None                                                      

Runtypes

Runtype object            

guard
 / 
check
 / 
parse
              

Yes                        

Parsers                  

None                                                      

Valibot  

Schema functions          

is
 / 
safeParse
                        

Yes                        

Schema pipelines          

None                                                      

Zod      

Schema objects            

parse
 / 
safeParse
                    

Yes                        

Transforms / codecs      

No build transform; optional runtime 
z.compile()
        

ArkType  

Runtime type expressions  

allows
 / invocation                    

Yes                        

Morphs                    

No build transform; runtime precompilation when available

typia    

TypeScript types and tags

Generated predicates / validation results

With validation APIs      

Build-generated functions

Build transform required
                              

This is why I no longer like thinking about them as a simple upgrade ladder.

A schema library is not "a better type guard".A generated validator is not "a better schema".

They solve overlapping problems at different layers.

## ✅ What Actually Passed?

The complete harness, lockfile, fixtures, probes, and generated result files live intypescript-validator-comparison. The article links to that immutable commit, rather than to a moving branch.

To reproduce the recorded snapshot:

git clone https://github.com/nyaomaru/typescript-validator-comparison.git

cd 
typescript-validator-comparison
git checkout 
--detach
 b26350d01fd18cb77d55a95e2f3b112657f0d305
corepack pnpm 
install
 
--frozen-lockfile

corepack pnpm verify

Enter fullscreen mode

Exit fullscreen mode

pnpm verifyruns lint, strict type checking, fixtures, bundle measurement, benchmarks, JavaScript-only probes, and report generation. The result tables below are that run's saved snapshot, reruns on another machine will naturally produce different timing numbers.

I pinned the versions and ran the same fixture matrix against all seven implementations.

Environment

Date:       2026-10-23
Node:       24.22.1
TypeScript: 7.0.2
pnpm:       11.22.0
ttsc:       0.31.3
tsbuild:    0.28.2

Enter fullscreen mode

Exit fullscreen mode

Packages

Package  

Version

is-kit  

1.15.3  

runtypes

7.0.5  

valibot  

1.5.0  

zod      

4.6.5  

arktype  

2.2.8  

typia    

15.1.0  

The shared matrix contains 35 JSON fixtures.

That includes:

* valid users
* age boundaries
* name boundaries
* emoji length cases
* wrong primitive types
* missing fields
* invalid roles
* invalid array elements
* extra root keys
* extra nested keys
* non-object roots

All seven matched the expected result.

35 fixtures
× 7 validators
= 245 boolean checks

Enter fullscreen mode

Exit fullscreen mode

All 245 passed.

The harness also checks input mutation, richer APIs, strict TypeScript compilation, lint, builds, narrowing, and bundled output behavior.

So the implementations agree for the JSON-shaped contract in this article—not necessarily for every JavaScript value.

## 🧩 One More Surprise: "Exact" Is Not Always Exact

I also tested values outside the normal JSON-shaped input domain. The four probes in the table mean exactly this:

const
 
sparseTags
 
=
 
{
 
...
valid
,
 
tags
:
 
new
 
Array
(
2
)
 
};

const
 
inheritedFields
 
=
 
Object
.
create
(
valid
);

const
 
extraSymbol
 
=
 
{
 
...
valid
,
 
[
Symbol
(
"
extra
"
)]:
 
true
 
};

const
 
extraUndefined
 
=
 
{
 
...
valid
,
 
extra
:
 
undefined
 
};

Enter fullscreen mode

Exit fullscreen mode

The repository runs nine more probes, including non-enumerable properties and a throwing getter. Here is what happened for these four

Probe                            

Native

is-kit

Runtypes

Valibot

Zod    

ArkType

typia  

Sparse 
tags
 array              

Accept

Reject

Accept  

Reject  

Reject

Reject  

Accept

All fields inherited            

Reject

Reject

Reject  

Accept  

Accept

Accept  

Accept

Extra symbol property            

Accept

Accept

Reject  

Accept  

Accept

Reject  

Accept

Extra key with value 
undefined

Reject

Reject

Reject  

Reject  

Reject

Reject  

Accept

All seven accepted the extra non-enumerable property I tested.

All seven threw when reading a getter that throws.

This doesnotmean one library is "correct" and the others are broken.

It means

"Exact object validation" needs a scope.

For example, my native guard uses

Object
.
keys
(
value
);

Enter fullscreen mode

Exit fullscreen mode

That only sees enumerable string keys.

And this

value
.
tags
.
every
(...)

Enter fullscreen mode

Exit fullscreen mode

skips sparse array holes.

That is perfectly reasonable for JSON data.

It is not a universal policy for every weird object JavaScript can create.

This is another reason I think validator comparisons should state the expected input domain.

## 📦 Bundle Size

Now the fun table. 😺

Each browser-targeted entry exports onlyvalidate.

All of them were bundled with the same esbuild settings:

* browser platform
* ESM
* ES2022
* minification
* tree shaking
* legal comments removed

Then I measured raw, gzip, and Brotli output.

Validator

Raw bytes

gzip bytes

Brotli bytes

handwritten guard

      588

       337

         295

is-kit    

    3,421

     1,530

       1,423

runtypes  

   16,667

     5,188

       4,657

valibot  

    5,722

     1,853

       1,675

zod      

   89,888

    26,212

      23,331

arktype  

  155,549

    47,603

      41,956

typia    

      772

       403

         339

A few important caveats.

### This is standalone cost

If your app already ships Zod, the marginal cost of one more schema is not 26 KB gzip.

This table measures isolated entry bundles.

### This is regular Zod

NotZodMini.

So this table doesnotanswer

ValibotvsZodMini?

### Generated does not mean zero bytes

typia's final guard bundle was only 772 bytes raw in this test.

But it still shipped generated code and a uint32 helper.

"Generated validator" does not mean "free validator".

Still, the architectural difference is very visible here.

## ⚡ Runtime

I almost did not include runtime numbers because validator benchmarks get misleading very quickly.But since the workspace already had the same contract and fixtures, I ran a small steady-state benchmark.

Three cases:

* valid user
* wrongid
* wrong nestedprofile.active

Each library ran in a separate Node process.

Each case used:

* 20,000 warmup calls
* 9 measured samples
* 50,000 calls per sample

Schemas and validators were created outside the measured loop.

Results are median nanoseconds per call, with min–max in parentheses.

Validator

                 Valid

             Wrong 
id

  Wrong 
profile.active

handwritten guard

     79.9 (77.3–114.1)

      73.6 (72.1–84.9)

       80.8 (79.0–96.3)

is-kit    

232.0 (225.7–257.5)

34.5 (33.1–38.9)

210.3 (203.6–218.1)

runtypes  

5804.0 (5425.5–6298.0)

9221.8 (8443.2–11063.2)

10101.2 (9287.6–10503.5)

valibot  

   951.2 (425.2–1782.7)

    200.2 (96.1–422.3)

  1112.1 (648.4–1538.1)

zod      

  612.6 (351.3–1203.5)

1491.6 (862.9–2824.6)

2208.5 (1592.4–4757.4)

arktype  

   291.5 (278.1–614.4)

          9.6 (6.6–17.7)

        12.0 (11.3–37.6)

typia    

     21.9 (20.5–46.1)

          2.0 (1.9–6.4)

        11.5 (10.8–17.2)

Please donotread this as:

typia is the fastest validator.

This is a microbenchmark.

The same small object shapes are validated repeatedly, so V8 can optimize very aggressively.

I would not interpret a2.0 nsresult as a portable "cost of validation" in a real application.

The success APIs are also different:

* handwritten guard uses a predicate
* is-kituses a predicate
* Runtypesuses.guard()
* Valibotusesis()
* ZodusessafeParse(...).success
* ArkTypeusesallows()
* typiauses a generated equals guard

Those operations do not all perform exactly the same work.

What the benchmarkdoesshow is that architecture and failure path matter.

For example:

* the handwritten guard pays for exact-key checks before rejecting the wrongid
* ArkType's invalid paths were much cheaper than its valid path
* typia's generated guard had very low steady-state overhead here
* Runtypes' richer validation machinery costs more in this particular hot loop

That is useful.

A universal speed ranking is not.

## So... Which One Would I Use? 🤔

After doing all of this, my decision tree is actually pretty simple.

### Just one local narrowing check?

Use a handwritten guard.

if 
(
isUser
(
input
))
 
{

 
// input is User

}

Enter fullscreen mode

Exit fullscreen mode

No dependency is a feature when the problem is small.

### Lots of reusable guards?

This is where I useis-kit. 🔧

values
.
filter
(
isName
);

if 
(
isAge
(
value
))
 
{

 
// ...

}

Enter fullscreen mode

Exit fullscreen mode

The problem is not "I need a schema".

The problem is "I keep rebuilding the same predicates and composition helpers".

### Want a validator object?

Runtypesis interesting when you like having one runtime object that can: 🏃

guard
check
parse
inspect
assert

Enter fullscreen mode

Exit fullscreen mode

### Want schema validation with a modular API?

Valibot. 🤖

Especially if client bundle size and tree shaking are important parts of the design.

### Want schemas tied into a bigger ecosystem?

Zod. 💎

That is probably its strongest reason to exist in many applications.

And if bundle size is a concern, evaluate Zod Mini separately.

### Want the schema syntax to feel like TypeScript?

ArkType. 🚢

"
18 <= number.integer <= 120
"
;

Enter fullscreen mode

Exit fullscreen mode

is a very different authoring experience from chained schema methods.

### Want TypeScript types transformed into validators during the build?

typia.But I would treat the build integration as part of the decision, not a footnote.

## Final Thought

These tools overlap, but they live at different layers.

The hard part is not making seven validators compile. It is making seven validators mean the same thing.

So before comparing package size or benchmark screenshots, ask what the boundary needs to return and what runtime machinery is worth carrying.

Use the smallest model that still represents your boundary well.

Then, which one will you use?

Thank you for reading! 🤲

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (22 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse