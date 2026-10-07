---
title: Why Your TypeScript Code Still Crashes in Production - DEV Community
url: https://dev.to/smtahosin/why-your-typescript-code-still-crashes-in-production-2bf4
site_name: devto
content_file: devto-why-your-typescript-code-still-crashes-in-producti
fetched_at: '2026-10-07T17:42:36.483819'
original_url: https://dev.to/smtahosin/why-your-typescript-code-still-crashes-in-production-2bf4
author: S M Tahosin
date: '2026-10-06'
description: A practical visual guide to the TypeScript mental model. Discover why types vanish at runtime, how structural typing works, and how to write clean, type-safe code that never crashes in production. Tagged with typescript, javascript, beginners, discuss.
tags: '#discuss, #typescript, #javascript, #beginners'
---

Type assertions mask runtime risks

You spend an entire afternoon adding types to your project. Every variable has an interface, every function has explicit return types, and your editor is completely free of red squiggly lines. You feel invincible.

You deploy to production.

Twenty minutes later, your error tracker pings you with this:

TypeError: Cannot read properties of undefined (reading 'toUpperCase')

Enter fullscreen mode

Exit fullscreen mode

Wait. How? You wrote TypeScript! Wasn't TypeScript supposed to make this exact error impossible?

If this has happened to you, welcome to the club. Almost every developer goes through a phase where TypeScript feels like an aggressive back-seat driver that yells at you constantly, yet somehow lets actual bugs slip right into production.

The problem is rarely your code. The problem is almost always yourmental model.

Most beginners treat TypeScript like Java or C# bolted onto JavaScript. But TypeScript does not work like any traditional language you have used before. Today, we are going to look at how TypeScriptactuallythinks, why your types disappear before your app even boots, and how to stop fighting the compiler once and for all.

## 1. The Phantom Type System: Type Erasure

Here is the single most important truth about TypeScript:

TypeScript does not exist when your code runs.

When you runtsc(the TypeScript compiler), it does two completely separate jobs:

1. It checks your code for type errors.
2. It completely strips away every singletype,interface, and type annotation, spitting out plain JavaScript.

Look closely at what happens after compilation. Those beautiful interfaces you designed? Gone. The custom generic constraints? Vanished.

At runtime in Node.js or in Chrome's V8 engine, your computer is running raw JavaScript. The runtime has zero memory of what types you wrote.

### The Classic Beginner Trap

Because beginners think types exist at runtime, they often write code like this:

interface
 
User
 
{

 
id
:
 
number
;

 
name
:
 
string
;

}

function
 
processResponse
(
data
:
 
unknown
)
 
{

 
// ❌ RUNTIME ERROR: 'User' only refers to a type, 

 
// but is being used as a value here.

 
if 
(
data
 
instanceof
 
User
)
 
{

 
console
.
log
(
data
.
name
);

 
}

}

Enter fullscreen mode

Exit fullscreen mode

JavaScript'sinstanceofoperator checks prototypes of actual objects in memory. ButUserwas erased during compilation! It left no trace in JavaScript, soinstanceof Usermakes zero sense to the runtime.

### Why Bad Data Crashes in Production

This also explains why external data breaks your app:

interface
 
ApiResponse
 
{

 
username
:
 
string
;

}

// You tell TypeScript: "Trust me, the API returns an ApiResponse"

const
 
response
 
=
 
await
 
fetch
(
'
/api/user
'
);

const
 
user
 
=
 
(
await
 
response
.
json
())
 
as
 
ApiResponse
;

// If the backend sent { error: "User not found" }, this explodes!

console
.
log
(
user
.
username
.
toUpperCase
());
 

Enter fullscreen mode

Exit fullscreen mode

TypeScript trusted your annotation at compile time. But TypeScript cannot monitor the network pipe. If the backend returnsnullor{ error: 500 }, your code will crash at runtime.

Rule of thumb:TypeScript validates what you write, not what the outside world sends you. For external boundaries (APIs, localStorage, user input), always use runtime validators like Zod or custom type guard functions.

## 2. Shape Over Name: Structural Typing

If you come from Java, C#, or C++, this next concept will blow your mind.

In traditional languages, type systems arenominal. A type's identity is determined by its explicit name or declaration.

In TypeScript, the type system isstructural(often called compile-time duck typing). A type's identity is determined exclusively by its internal shape.

Let's look at a concrete example:

type
 
Vector2D
 
=
 
{

 
x
:
 
number
;

 
y
:
 
number
;

};

type
 
Point2D
 
=
 
{

 
x
:
 
number
;

 
y
:
 
number
;

};

const
 
point
:
 
Point2D
 
=
 
{
 
x
:
 
10
,
 
y
:
 
20
 
};

const
 
vector
:
 
Vector2D
 
=
 
point
;
 
// ✅ 100% Valid!

Enter fullscreen mode

Exit fullscreen mode

In Java or C#, assigning aPoint2Dto aVector2Dwithout an explicit cast would throw a compile-time error. They have different names, so they are different types.

In TypeScript, the compiler checks the blueprint:

* Doespointhave anxof type number? Yes.
* Doespointhave ayof type number? Yes.
* Done. They are completely interchangeable.

### The "Excess Property" Surprise

Here is a puzzle that confuses almost everyone when they start:

type
 
Options
 
=
 
{

 
timeout
:
 
number
;

};

function
 
startServer
(
opts
:
 
Options
)
 
{

 
console
.
log
(
`Starting with timeout: 
${
opts
.
timeout
}
`
);

}

// Case A: Passing an object literal directly

// ❌ ERROR: Object literal may only specify known properties, 

// and 'port' does not exist in type 'Options'.

startServer
({
 
timeout
:
 
5000
,
 
port
:
 
8080
 
});

// Case B: Passing an existing variable reference

const
 
myConfig
 
=
 
{
 
timeout
:
 
5000
,
 
port
:
 
8080
 
};

startServer
(
myConfig
);
 
// ✅ Valid! No errors!

Enter fullscreen mode

Exit fullscreen mode

Why does Case A fail while Case B succeeds when both pass the exact same properties?

Here is why: TypeScript enforcesExcess Property Checksspecifically on fresh object literals.

When you write an inline literal{ timeout: 5000, port: 8080 }, TypeScript assumes you made a typo (like typingtimeouutinstead oftimeout), so it strictly flags any extra fields.

But when you assign it to an intermediate variablemyConfig, TypeScript switches back to pure structural typing. BecausemyConfigsatisfies the contract of havingtimeout: number, TypeScript permits it.

Understanding this difference saves you hours of head-scratching.

## 3. The Type Spectrum: any vs unknown vs never

When developers struggle with a stubborn type error, the easiest temptation is reaching forany.

// The "I give up" button

const
 
user
:
 
any
 
=
 
fetchUserData
();

Enter fullscreen mode

Exit fullscreen mode

Usinganydoes not solve your type problem. It simply tells the compiler:"Stop doing your job. Turn off safety for this variable and everything it touches."

It spreads like a virus. Once one variable isany, any function calling it loses autocomplete and validation.

Instead, modern TypeScript gives you a clean spectrum of tools:

### 1.unknown: The Safe Top Type

Whenever you truly do not know what a value is (like an API response, user input, or parsed JSON), useunknowninstead ofany.

unknownaccepts any value, but refuses to let you do anything with it until you prove what it is:

function
 
parsePayload
(
input
:
 
unknown
)
 
{

 
// ❌ ERROR: 'input' is of type 'unknown'.

 
// console.log(input.trim());

 
// ✅ Safe: We prove it is a string first (Type Narrowing)

 
if 
(
typeof
 
input
 
===
 
'
string
'
)
 
{

 
console
.
log
(
input
.
trim
());
 
 
}

}

Enter fullscreen mode

Exit fullscreen mode

### 2.never: The Exhaustive Bottom Type

neverrepresents a state that should mathematically never happen. It is your secret weapon for making sure you never forget a case in complex conditional logic:

type
 
Action
 
=
 
 
|
 
{
 
type
:
 
'
LOGIN
'
;
 
username
:
 
string
 
}

 
|
 
{
 
type
:
 
'
LOGOUT
'
 
}

 
|
 
{
 
type
:
 
'
SIGNUP
'
;
 
email
:
 
string
 
};

function
 
handleAction
(
action
:
 
Action
)
 
{

 
switch 
(
action
.
type
)
 
{

 
case
 
'
LOGIN
'
:

 
return
 
`Welcome, 
${
action
.
username
}
`
;

 
case
 
'
LOGOUT
'
:

 
return
 
'
Goodbye
'
;

 
case
 
'
SIGNUP
'
:

 
return
 
`Signed up with 
${
action
.
email
}
`
;

 
default
:
 
{

 
// If someone adds a new action to Action and forgets 

 
// to add a case here, this line will NOT compile!

 
const
 
_exhaustiveCheck
:
 
never
 
=
 
action
;

 
return
 
_exhaustiveCheck
;

 
}

 
}

}

Enter fullscreen mode

Exit fullscreen mode

If tomorrow another developer adds{ type: 'RESET_PASSWORD' }toAction, the TypeScript compiler will immediately flag an error insidehandleActionbefore the code ever reaches testing.

## 4. Kill Optional Flag Hell with Discriminated Unions

Look at this common pattern for managing network request state:

// The "Everything Might Exist" anti-pattern

type
 
RequestState
 
=
 
{

 
isLoading
:
 
boolean
;

 
data
?:
 
UserData
;

 
error
?:
 
string
;

};

Enter fullscreen mode

Exit fullscreen mode

This looks innocent, but mathematically, this type allows8 different combinations:

* isLoading: true,data: user,error: "Failed"
* isLoading: false,data: undefined,error: undefined

None of these combinations make sense in real life! Yet your code has to defensively check every single property withif (state.data && !state.isLoading && !state.error).

Instead, model your domain with aDiscriminated Union:

type
 
RequestState
 
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
 
UserData
 
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
 
string
 
};

function
 
renderUI
(
state
:
 
RequestState
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
loading
'
:

 
return
 
'
<Spinner />
'
;

 
case
 
'
error
'
:

 
// TypeScript knows 'error' exists here!

 
return
 
`<ErrorMessage text="
${
state
.
error
}
" />`
;

 
case
 
'
success
'
:

 
// TypeScript guarantees 'data' exists here!

 
return
 
`<UserProfile user="
${
state
.
data
.
name
}
" />`
;

 
case
 
'
idle
'
:

 
return
 
'
<WelcomePrompt />
'
;

 
}

}

Enter fullscreen mode

Exit fullscreen mode

By adding a single literal string tag (status), impossible states become unrepresentable in your code. TypeScript narrows the object automatically inside each branch.

## 5. Stop Using "as" (Use "satisfies" Instead)

In older TypeScript codebases, you will see theaskeyword everywhere:

type
 
Theme
 
=
 
'
light
'
 
|
 
'
dark
'
;

type
 
Palette
 
=
 
Record
<
Theme
,
 
string
>
;

// The "as" type assertion (A polite lie to the compiler)

const
 
colors
 
=
 
{

 
light
:
 
'
#ffffff
'
,

 
dark
:
 
'
#121212
'
,

}
 
as
 
Palette
;

// No autocomplete for exact color strings!

colors
.
light
;
 
// Type is just 'string', not '#ffffff'

Enter fullscreen mode

Exit fullscreen mode

When you useas, you force the compiler to accept your declaration. If you mistyped a hex code or omitted a required key,aswill often mask the problem.

In modern TypeScript (v4.9 and above), use thesatisfiesoperator instead:

type
 
Theme
 
=
 
'
light
'
 
|
 
'
dark
'
;

type
 
Palette
 
=
 
Record
<
Theme
,
 
string
>
;

const
 
colors
 
=
 
{

 
light
:
 
'
#ffffff
'
,

 
dark
:
 
'
#121212
'
,

}
 
satisfies
 
Palette
;

// 1. Validates that 'colors' matches Palette shape

// 2. Retains exact literal precision!

// colors.light has type '#ffffff', not generic string!

Enter fullscreen mode

Exit fullscreen mode

satisfiesgives you the best of both worlds: it validates that your object conforms to a contract without discarding the specific literal types and properties of your data.

## The Mental Shift That Changes Everything

Once you internalize these five core concepts:

1. Types are completely erased at runtime.Validate external boundaries with tools like Zod or custom guards.
2. TypeScript checks shapes, not names.Embrace structural compatibility instead of fighting it.
3. Avoidany.Useunknownto enforce safety andneverto catch unhandled edge cases.
4. Use Discriminated Unions.Make illegal states mathematically impossible to represent.
5. Prefersatisfiesoveras.Catch real bugs while preserving literal precision.

Suddenly, you are no longer treating TypeScript like an adversary. The constant fight with the compiler stops, and it transforms into the sharpest pair programmer you have ever had.

Looking back at my own journey, the hardest transition was unlearning the habit of trusting types at runtime. It took one painful Friday night deployment outage for that lesson to truly stick.

I am curious: what was the specific TypeScript error or mental model shift that took you the longest to wrap your head around? Have you ever had a runtime bug slip through because of type erasure? Share your battle stories or favorite type patterns below. Hearing how other engineers untangled their mental models is always one of the best ways we all level up.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (25 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse