---
title: 20 TypeScript Tricks Every Developer Should Know - DEV Community
url: https://dev.to/shayy/20-typescript-tricks-every-developer-should-know-94c
site_name: devto
fetched_at: '2025-07-03T22:08:17.416982'
original_url: https://dev.to/shayy/20-typescript-tricks-every-developer-should-know-94c
author: Shayan
date: '2025-07-01'
description: I've been building UserJot, a feedback and roadmap platform for SaaS teams, for the past several... Tagged with webdev, typescript, programming, javascript.
tags: '#webdev, #typescript, #programming, #javascript'
---

I've been buildingUserJot, a feedback and roadmap platform for SaaS teams, for the past several months. This project has been my deep dive into TypeScript - before this, I'd used it here and there, but never at this scale. After many hours of writing production TypeScript code, debugging type errors, and refactoring for better type safety, I've picked up tricks that genuinely make development faster and catch bugs before they hit production.

These aren't theoretical patterns from a textbook. These are practical tricks I use every day, discovered through actual problems I needed to solve. Some saved me from runtime errors, others just made the code cleaner and easier to work with. Here are 20 that actually matter.

## 1. Usesatisfiesfor Better Type Inference

Thesatisfiesoperator lets you validate that an expression matches a type while preserving the literal types. This is especially useful for configuration objects where you want both type safety and precise inference.

// Without satisfies - loses specific types

const

config1
:

Record
<
string
,

string

|

number
>

=

{


port
:

3000
,


host
:

'
localhost
'

}

// config1.port is string | number

// With satisfies - keeps specific types

const

config2

=

{


port
:

3000
,


host
:

'
localhost
'

}

satisfies

Record
<
string
,

string

|

number
>

// config2.port is number, config2.host is string

Enter fullscreen mode

Exit fullscreen mode

## 2. Const Assertions for Immutable Types

Addingas constto an object makes TypeScript treat all properties as readonly and infer the most specific types possible. Great for configuration data that shouldn't change.

const

routes

=

{


home
:

'
/
'
,


dashboard
:

'
/dashboard
'
,


settings
:

'
/settings
'

}

as

const

// routes.home is '/' not string

Enter fullscreen mode

Exit fullscreen mode

## 3. Template Literal Types for String Patterns

Template literal types let you create types that match specific string patterns. Perfect for API endpoints, event names, or any structured strings.

type

EventName

=

`on
${
Capitalize
<
string
>
}
`

// 'onClick', 'onChange', 'onSubmit' ✓

// 'click', 'handleClick' ✗

type

Method

=

'
GET
'

|

'
POST
'

|

'
PUT
'

|

'
DELETE
'

type

Endpoint

=

`/api/
${
string
}
`

type

Route

=

`
${
Method
}

${
Endpoint
}
`

// 'GET /api/users' ✓

// 'GET /users' ✗

// Real world example

function

makeRequest
(
route
:

Route
)

{


// TypeScript ensures route follows pattern

}

makeRequest
(
'
GET /api/users
'
)

// ✓

makeRequest
(
'
GET /users
'
)

// ✗ Error

Enter fullscreen mode

Exit fullscreen mode

## 4. Discriminated Unions for State Management

Use a common property to discriminate between union members. TypeScript will narrow the type based on this discriminator, making your code much safer.

type

State

=


|

{

status
:

'
idle
'

}


|

{

status
:

'
loading
'

}


|

{

status
:

'
success
'
;

data
:

string

}


|

{

status
:

'
error
'
;

error
:

Error

}

function

handleState
(
state
:

State
)

{


switch
(
state
.
status
)

{


case

'
idle
'
:


// TypeScript knows state is { status: 'idle' }


break


case

'
loading
'
:


// TypeScript knows state is { status: 'loading' }


break


case

'
success
'
:


// TypeScript knows state has 'data' property


console
.
log
(
state
.
data
.
toUpperCase
())


break


case

'
error
'
:


// TypeScript knows state has 'error' property


console
.
error
(
state
.
error
.
message
)


break


}

}

Enter fullscreen mode

Exit fullscreen mode

## 5. Type Predicates for Custom Type Guards

Create functions that tell TypeScript what type something is. This is way cleaner than multiple typeof checks scattered throughout your code.

function

isString
(
value
:

unknown
):

value

is

string

{


return

typeof

value

===

'
string
'

}

Enter fullscreen mode

Exit fullscreen mode

## 6. Indexed Access Types

Extract types from other types using bracket notation. This keeps your types DRY and automatically updates when the source type changes.

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

email
:

string

}

type

UserEmail

=

User
[
'
email
'
]

// string

type

UserKeys

=

keyof

User

// 'id' | 'name' | 'email'

Enter fullscreen mode

Exit fullscreen mode

## 7. Conditional Types for Dynamic Type Logic

Use conditional types to create types that change based on conditions. Think of them as ternary operators for types.

type

IsArray
<
T
>

=

T

extends

any
[]

?

true

:

false

type

Test1

=

IsArray
<
string
[]
>

// true

type

Test2

=

IsArray
<
string
>

// false

// Extract array element type

type

Flatten
<
T
>

=

T

extends

Array
<
infer

U
>

?

U

:

T

type

Flattened1

=

Flatten
<
string
[]
>

// string

type

Flattened2

=

Flatten
<
number
>

// number

// More practical example

type

ApiResponse
<
T
>

=

T

extends

{

error
:

string

}


?

{

success
:

false
;

error
:

string

}


:

{

success
:

true
;

data
:

T

}

Enter fullscreen mode

Exit fullscreen mode

## 8. Utility Types are Your Friend

TypeScript has built-in utility types that solve common problems. Learn them instead of reinventing the wheel.

type

PartialUser

=

Partial
<
User
>

// All properties optional

type

ReadonlyUser

=

Readonly
<
User
>

// All properties readonly

type

UserWithoutEmail

=

Omit
<
User
,

'
email
'
>

type

JustEmailAndId

=

Pick
<
User
,

'
email
'

|

'
id
'
>

Enter fullscreen mode

Exit fullscreen mode

## 9. Function Overloads for Better DX

Provide multiple function signatures for different use cases. This gives users of your functions better autocomplete and type checking.

// Overload signatures

function

parse
(
value
:

string
):

object

function

parse
(
value
:

string
,

reviver
:

Function
):

object

// Implementation signature (not visible to consumers)

function

parse
(
value
:

string
,

reviver
?:

Function
)

{


return

JSON
.
parse
(
value
,

reviver
)

}

// Usage gets proper type hints

const

obj1

=

parse
(
'
{}
'
)

// return type is object

const

obj2

=

parse
(
'
{}
'
,

(
k
,

v
)

=>

v
)

// knows reviver is allowed

// Another example with different return types

function

createElement
(
tag
:

'
img
'
):

HTMLImageElement

function

createElement
(
tag
:

'
input
'
):

HTMLInputElement

function

createElement
(
tag
:

string
):

HTMLElement

function

createElement
(
tag
:

string
):

HTMLElement

{


return

document
.
createElement
(
tag
)

}

const

img

=

createElement
(
'
img
'
)

// type is HTMLImageElement

const

input

=

createElement
(
'
input
'
)

// type is HTMLInputElement

Enter fullscreen mode

Exit fullscreen mode

## 10. Generic Constraints

Limit what types can be passed to generics. This prevents errors and provides better IntelliSense.

function

getProperty
<
T
,

K

extends

keyof

T
>
(
obj
:

T
,

key
:

K
):

T
[
K
]

{


return

obj
[
key
]

}

Enter fullscreen mode

Exit fullscreen mode

## 11. Mapped Types for Transformations

Transform all properties of a type systematically. Great for creating variations of existing types.

// Make all properties nullable

type

Nullable
<
T
>

=

{

[
K

in

keyof

T
]:

T
[
K
]

|

null

}

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

}

type

NullableUser

=

Nullable
<
User
>

// { id: string | null; name: string | null; age: number | null }

// Create getter methods from properties

type

Getters
<
T
>

=

{


[
K

in

keyof

T

as

`get
${
Capitalize
<
K

&

string
>
}
`
]:

()

=>

T
[
K
]


}

type

UserGetters

=

Getters
<
User
>

// { getId: () => string; getName: () => string; getAge: () => number }

// Remove readonly modifier

type

Mutable
<
T
>

=

{

-
readonly

[
K

in

keyof

T
]:

T
[
K
]

}

Enter fullscreen mode

Exit fullscreen mode

## 12. Never Type for Exhaustive Checks

Useneverto ensure you've handled all cases in a switch statement. TypeScript will error if you miss a case.

function

handleStatus
(
status
:

State
[
'
status
'
])

{


switch
(
status
)

{


case

'
idle
'
:

return


case

'
loading
'
:

return


case

'
success
'
:

return


case

'
error
'
:

return


default
:


const

_exhaustive
:

never

=

status


throw

new

Error
(
`Unhandled status:
${
status
}
`
)


}

}

Enter fullscreen mode

Exit fullscreen mode

## 13. Module Augmentation

Extend existing module types when needed. Useful for adding properties to window or extending third-party libraries.

declare

global

{


interface

Window

{


analytics
:

AnalyticsClient


}

}

Enter fullscreen mode

Exit fullscreen mode

## 14. Type-Only Imports

Use type-only imports to ensure imports are removed at runtime. This can reduce bundle size and prevent circular dependencies.

import

type

{

User

}

from

'
./types
'

import

{

type

Config
,

validateConfig

}

from

'
./config
'

Enter fullscreen mode

Exit fullscreen mode

## 15. Assert Functions

Create functions that assert conditions and narrow types. If the assertion fails, the function throws. This is super useful for validating data at runtime while keeping TypeScript happy.

function

assertDefined
<
T
>
(
value
:

T

|

undefined
):

asserts

value

is

T

{


if
(
value

===

undefined
)

{


throw

new

Error
(
'
Value is undefined
'
)


}

}

// Usage

function

processUser
(
user
:

User

|

undefined
)

{


assertDefined
(
user
)


// TypeScript now knows user is User, not User | undefined


console
.
log
(
user
.
name
.
toUpperCase
())

}

// Multiple assertions

function

assertValidEmail
(
value
:

unknown
):

asserts

value

is

string

{


if
(
typeof

value

!==

'
string
'
)

{


throw

new

Error
(
'
Email must be string
'
)


}


if
(
!
value
.
includes
(
'
@
'
))

{


throw

new

Error
(
'
Invalid email format
'
)


}

}

Enter fullscreen mode

Exit fullscreen mode

## 16. Branded Types for Runtime Safety

Create types that are structurally identical but nominally different. Prevents mixing up similar primitive types. This pattern has saved me from so many bugs where I passed the wrong ID type.

type

UserId

=

string

&

{

__brand
:

'
UserId
'

}

type

PostId

=

string

&

{

__brand
:

'
PostId
'

}

// Helper functions to create branded types

function

userId
(
id
:

string
):

UserId

{


return

id

as

UserId

}

function

postId
(
id
:

string
):

PostId

{


return

id

as

PostId

}

// Usage

function

getUserById
(
id
:

UserId
)

{

/* ... */

}

function

getPostById
(
id
:

PostId
)

{

/* ... */

}

const

uId

=

userId
(
'
user_123
'
)

const

pId

=

postId
(
'
post_456
'
)

getUserById
(
uId
)

// ✓

getUserById
(
pId
)

// ✗ Error: Argument of type 'PostId' not assignable to 'UserId'

Enter fullscreen mode

Exit fullscreen mode

## 17. Builder Pattern with Fluent Interface

Use generics to track the state of a builder and ensure methods are called in the right order. This pattern ensures compile-time safety for method chaining.

class

QueryBuilder
<
T

=

{}
>

{


private

query
:

any

=

{}


select
<
K

extends

string
>
(
field
:

K
):

QueryBuilder
<
T

&

{

select
:

K

}
>

{


this
.
query
.
select

=

field


return

this

as

any


}


where
<
K

extends

string
>
(
field
:

K
):

QueryBuilder
<
T

&

{

where
:

K

}
>

{


this
.
query
.
where

=

field


return

this

as

any


}


// Only available when both select and where are called


build
(
this
:

QueryBuilder
<
{

select
:

string
;

where
:

string

}
>
)

{


return

this
.
query


}

}

// Usage

const

query

=

new

QueryBuilder
()


.
select
(
'
name
'
)


.
where
(
'
id
'
)


.
build
()

// ✓ Works

const

badQuery

=

new

QueryBuilder
()


.
select
(
'
name
'
)


.
build
()

// ✗ Error: build() requires where() to be called

Enter fullscreen mode

Exit fullscreen mode

## 18. Const Enums for Zero-Cost Abstractions

Const enums are completely removed during compilation and replaced with their values. No runtime overhead.

const

enum

LogLevel

{


Debug

=

0
,


Info

=

1
,


Warn

=

2
,


Error

=

3

}

// LogLevel.Debug becomes just 0 in the compiled code

Enter fullscreen mode

Exit fullscreen mode

## 19. Intersection Types for Composition

Combine multiple types into one. More flexible than extends for combining unrelated types.

type

Timestamped

=

{

createdAt
:

Date
;

updatedAt
:

Date

}

type

Authored

=

{

authorId
:

string

}

type

Post

=

{

title
:

string
;

content
:

string

}

&

Timestamped

&

Authored

Enter fullscreen mode

Exit fullscreen mode

## 20. NoInfer Utility Type

New in TypeScript 5.4,NoInferprevents type inference in specific positions. Useful for forcing explicit type parameters. This helps avoid accidentally widening types based on the wrong parameter.

// Without NoInfer - T gets inferred from both parameters

function

createState
<
T
>
(
initial
:

T
,

actions
:

T
)

{


return

{

state
:

initial
,

actions

}

}

// Problem: T becomes string | number instead of just string

const

state1

=

createState
(
'
hello
'
,

42
)

// Oops, mixed types

// With NoInfer - T only inferred from initial

function

createStateSafe
<
T
>
(
initial
:

T
,

actions
:

NoInfer
<
T
>
)

{


return

{

state
:

initial
,

actions

}

}

// Now this errors as expected

const

state2

=

createStateSafe
(
'
hello
'
,

42
)

// ✗ Error

// Must explicitly specify T to allow different types

const

state3

=

createStateSafe
<
string

|

number
>
(
'
hello
'
,

42
)

// ✓

Enter fullscreen mode

Exit fullscreen mode

## Wrapping Up

These tricks have saved me countless hours debugging and made the UserJot codebase much more maintainable. TypeScript is powerful, but you don't need to use every feature. Pick the ones that solve real problems in your code. Start with a few, get comfortable, then gradually add more to your toolkit.

If you're building a product and need a way to collect user feedback, manage your roadmap, or keep users updated with changelogs, check outUserJot. It's what I've been building with all these TypeScript tricks, and it's designed to help teams build products their users actually want. Plus, the free tier is pretty generous, so you can try it out without committing.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
