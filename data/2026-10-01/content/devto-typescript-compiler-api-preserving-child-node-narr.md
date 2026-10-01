---
title: 'TypeScript Compiler API: Preserving Child Node Narrowing in Reusable Type Guards 🔧 - DEV Community'
url: https://dev.to/nyaomaru/typescript-compiler-api-preserving-child-node-narrowing-in-reusable-type-guards-4pgh
site_name: devto
content_file: devto-typescript-compiler-api-preserving-child-node-narr
fetched_at: '2026-10-01T17:18:16.547556'
original_url: https://dev.to/nyaomaru/typescript-compiler-api-preserving-child-node-narrowing-in-reusable-type-guards-4pgh
author: nyaomaru
date: '2026-09-30'
description: Hoi hoi! 👋 I'm @nyaomaru, a frontend engineer exploring new possibilities with Jev 😸 (I'm also... Tagged with typescript, opensource, webdev, frontend.
tags: '#typescript, #opensource, #webdev, #frontend'
---

Property refinement applies beyond AST nodes

Hoi hoi! 👋

I'm@nyaomaru, a frontend engineer exploring new possibilities withJev😸 (I'm also curious about "Decisions API" from OpenAI)

Recently, I was looking into the TypeScript Compiler API and asking a pretty specific question

Can reusable type guards preserve not only the AST node type, but also a narrowed child property?

At first, I thought this might be a Compiler API-specific problem.

Then I reproduced the same pattern with plain TypeScript objects.

That changed the way I looked at it.

The interesting problem wasn't really the AST.

It wasproperty refinement.

Let's look at it! 👀

## 🌲 A Very Common Compiler API Pattern

Suppose we have a broadts.Node.

import
 
*
 
as
 
ts
 
from
 
"
typescript
"
;

declare
 
const
 
node
:
 
ts
.
Node
;

Enter fullscreen mode

Exit fullscreen mode

We want to know two things:

* Is this aCallExpression?
* Is itsexpressionanIdentifier?

Inline, this is easy.

if 
(
ts
.
isCallExpression
(
node
)
 
&&
 
ts
.
isIdentifier
(
node
.
expression
))
 
{

 
// node: ts.CallExpression

 
// node.expression: ts.Identifier

 
node
.
expression
.
text
;

}

Enter fullscreen mode

Exit fullscreen mode

TypeScript understands the control flow perfectly.

Nothing special is needed.

And honestly, if this check appears only once, I would probably leave it exactly like this.

## 🤔 What If We Want to Reuse That Shape?

Now suppose the same AST shape appears in several places:

* a visitor
* filter
* find
* another transformation
* another lint rule

Then giving the check a name starts to make sense.

Since TypeScript v5.5, simple functions can often infer a type predicate automatically.

But this compound parent-plus-child check is different.

const
 
isCallWithIdentifierExpression
 
=
 
(
node
:
 
ts
.
Node
)
 
=>

 
ts
.
isCallExpression
(
node
)
 
&&
 
ts
.
isIdentifier
(
node
.
expression
);

// inferred:

// (node: ts.Node) => boolean

Enter fullscreen mode

Exit fullscreen mode

So if we want the extracted predicate to preserve both facts, we have to describethe refined type explicitly.

const
 
isCallWithIdentifierExpression
 
=
 
(

 
node
:
 
ts
.
Node
,

):
 
node
 
is
 
ts
.
CallExpression
 
&
 
{

 
expression
:
 
ts
.
Identifier
;

}
 
=>
 
ts
.
isCallExpression
(
node
)
 
&&
 
ts
.
isIdentifier
(
node
.
expression
);

Enter fullscreen mode

Exit fullscreen mode

This works. Then we can reuse it

declare
 
const
 
nodes
:
 
readonly
 
ts
.
Node
[];

const
 
calls
 
=
 
nodes
.
filter
(
isCallWithIdentifierExpression
);

// calls:

// Array<

//   ts.CallExpression & {

//     expression: ts.Identifier;

//   }

// >

Enter fullscreen mode

Exit fullscreen mode

So what's the problem?

There isn't really a runtime problem.

The annoying part is that we had to manually describe this 👇

ts
.
CallExpression
 
&
 
{

 
 
expression
:
 
ts
.
Identifier
;

}

Enter fullscreen mode

Exit fullscreen mode

But we already performed those exact runtime checks.

It would be nice if we could compose the checks and let the type follow them. 😸

## 🧩 Refining the Parent and Child Together

This is where I ended up usingrefineKey.

Withis-kit

import
 
*
 
as
 
ts
 
from
 
"
typescript
"
;

import
 
{
 
and
,
 
refineKey
 
}
 
from
 
"
is-kit
"
;

const
 
isCallWithIdentifierExpression
 
=
 
and
(

 
ts
.
isCallExpression
,

 
refineKey
(
"
expression
"
,
 
ts
.
isIdentifier
),

);

Enter fullscreen mode

Exit fullscreen mode

That's it.

Now

declare
 
const
 
node
:
 
ts
.
Node
;

if 
(
isCallWithIdentifierExpression
(
node
))
 
{

 
// node:

 
// ts.CallExpression & {

 
//   expression: ts.Identifier;

 
// }

 
node
.
expression
.
text
;

}

Enter fullscreen mode

Exit fullscreen mode

The interesting part is the relationship between the two checks.

ts
.
isCallExpression
;

Enter fullscreen mode

Exit fullscreen mode

narrows the parent.

Then

refineKey
(
"
expression
"
,
 
ts
.
isIdentifier
);

Enter fullscreen mode

Exit fullscreen mode

within the composed narrowing chain, checks one property on the parent already narrowed byts.isCallExpressionand preserves the checked child type.

So the idea is

Check the child once at runtime, then carry that same fact back to the parent type.

## 😸 This Turned Out Not to Be an AST Problem

This was the part that surprised me during the research.

I originally thought I was investigating a TypeScript Compiler API gap.

But the same shape appears with ordinary objects too.

Conceptually, the pattern is just

Parent

 
 
↓

check
 
property

 
 
↓

Parent
 
&
 
{

 
 
property
:
 
RefinedChild

}

Enter fullscreen mode

Exit fullscreen mode

The Compiler API is simply a really good stress test for it because AST code contains this pattern everywhere.

For example

CallExpression
  → expression
  → Identifier

Enter fullscreen mode

Exit fullscreen mode

or

VariableDeclaration
  → initializer?
  → CallExpression

Enter fullscreen mode

Exit fullscreen mode

or

CallExpression
  → arguments[0]
  → StringLiteral

Enter fullscreen mode

Exit fullscreen mode

So I don't think ofrefineKeyas a Compiler API helper.

The Compiler API is just an advanced example of a more generic composition problem.

## 🔗 Compiler API Guards Already Compose Well

Another thing I wanted to avoid was wrapping TypeScript's existing predicates unnecessarily.

The Compiler API already provides excellent guards

ts
.
isStringLiteral
;

ts
.
isIdentifier
;

ts
.
isCallExpression
;

ts
.
isClassDeclaration
;

Enter fullscreen mode

Exit fullscreen mode

We should reuse them.

For example

import
 
*
 
as
 
ts
 
from
 
"
typescript
"
;

import
 
{
 
or
 
}
 
from
 
"
is-kit
"
;

const
 
isStringLike
 
=
 
or
(
ts
.
isStringLiteral
,
　
ts
.
isNoSubstitutionTemplateLiteral
);

declare
 
const
 
nodes
:
 
readonly
 
ts
.
Node
[];

const
 
strings
 
=
 
nodes
.
filter
(
isStringLike
);

// strings:

// (

//   | ts.StringLiteral

//   | ts.NoSubstitutionTemplateLiteral

// )[]

Enter fullscreen mode

Exit fullscreen mode

There is no reason foris-kitto create its own

isTsStringLiteral
();

isTsIdentifier
();

isTsCallExpression
();

Enter fullscreen mode

Exit fullscreen mode

That would just duplicate the Compiler API.

The useful part is composition.

## ♻️ Reuse the Same Guard infindand Visitors

This becomes more useful when a refined shape appears in several contexts.

For example

import
 
*
 
as
 
ts
 
from
 
"
typescript
"
;

import
 
{
 
and
,
 
refineKey
 
}
 
from
 
"
is-kit
"
;

const
 
isIdentifierNamedJsxAttribute
 
=
 
and
(

 
ts
.
isJsxAttribute
,

 
refineKey
(
"
name
"
,
 
ts
.
isIdentifier
),

);

Enter fullscreen mode

Exit fullscreen mode

We can use it withfind:

declare
 
const
 
attributes
:
 
readonly
 
ts
.
JsxAttributeLike
[];

const
 
attribute
 
=
 
attributes
.
find
(
isIdentifierNamedJsxAttribute
);

// attribute:

// (

//   ts.JsxAttribute & {

//     name: ts.Identifier;

//   }

// ) | undefined

Enter fullscreen mode

Exit fullscreen mode

The same guard works in a visitor

function
 
visit
(
node
:
 
ts
.
Node
):
 
void
 
{

 
if 
(
isIdentifierNamedJsxAttribute
(
node
))
 
{

 
// node:

 
// ts.JsxAttribute & {

 
//   name: ts.Identifier;

 
// }

 
node
.
name
.
text
;

 
}

 
ts
.
forEachChild
(
node
,
 
visit
);

}

Enter fullscreen mode

Exit fullscreen mode

That's the point where extracting the guard starts earning its keep.

The runtime rule and the TypeScript narrowing travel together.

## 🫥 Optional Children Are a Different Contract

AST nodes contain lots of optional properties.

For example, aVariableDeclarationmay or may not have an initializer.

declaration
.
initializer
;

Enter fullscreen mode

Exit fullscreen mode

So this is slightly different from refining a required property.

We don't just want

Refineinitializer.

We want

Requireinitializerto exist, then refine it.

For that case,is-kithasrefineDefinedKey.

import
 
*
 
as
 
ts
 
from
 
"
typescript
"
;

import
 
{
 
refineDefinedKey
 
}
 
from
 
"
is-kit
"
;

const
 
hasCallInitializer
 
=
 
refineDefinedKey
(
"
initializer
"
,
 
ts
.
isCallExpression
);

Enter fullscreen mode

Exit fullscreen mode

Now

declare
 
const
 
declaration
:
 
ts
.
VariableDeclaration
;

if 
(
hasCallInitializer
(
declaration
))
 
{

 
// declaration.initializer: ts.CallExpression

 
declaration
.
initializer
.
expression
;

}

Enter fullscreen mode

Exit fullscreen mode

Inside the branch,initializeris both:

* present
* ats.CallExpression

A missing initializer returnsfalse.

An explicitlyundefinedinitializer also returnsfalse.

I like keeping this separate fromrefineKeybecause absence is runtime behavior, not just a TypeScript annotation.

## 📦 Arrays Have the Same Problem

AST arrays introduce another small issue.

Suppose we want a call whose first argument is a string literal.

This

node
.
arguments
[
0
];

Enter fullscreen mode

Exit fullscreen mode

looks simple, but at runtime the array can be empty.

So we want to prove two things:

* index0exists
* the value is aStringLiteral

We can compose that too

import
 
*
 
as
 
ts
 
from
 
"
typescript
"
;

import
 
{
 
and
,
 
refineIndex
,
 
refineKey
 
}
 
from
 
"
is-kit
"
;

const
 
isCallWithStringFirstArgument
 
=
 
and
(

 
ts
.
isCallExpression
,

 
refineKey
(
"
arguments
"
,
 
refineIndex
(
0
,
 
ts
.
isStringLiteral
)),

);

Enter fullscreen mode

Exit fullscreen mode

Then

declare
 
const
 
node
:
 
ts
.
Node
;

if 
(
isCallWithStringFirstArgument
(
node
))
 
{

 
// node: ts.CallExpression

 
// node.arguments[0]: ts.StringLiteral

 
node
.
arguments
[
0
].
text
;

}

Enter fullscreen mode

Exit fullscreen mode

Now index0is known to exist and to be ats.StringLiteral.

Again, this isn't really an AST-specific idea.

It's just

Refine one checked location and preserve that fact.

## 🪆 Nested Checks Can Stay Composable

These refinements can also be nested.

Suppose we want a function-like declaration whose:

* bodyexists
* bodyis a block
* first statement exists
* first statement is a return statement

We can build the pieces separately.

import
 
*
 
as
 
ts
 
from
 
"
typescript
"
;

import
 
{
 
and
,
 
refineDefinedKey
,
 
refineIndex
,
 
refineKey
 
}
 
from
 
"
is-kit
"
;

const
 
isBlockStartingWithReturn
 
=
 
and
(

 
ts
.
isBlock
,

 
refineKey
(
"
statements
"
,
 
refineIndex
(
0
,
 
ts
.
isReturnStatement
)),

);

const
 
hasBodyStartingWithReturn
 
=
 
refineDefinedKey
(

 
"
body
"
,

 
isBlockStartingWithReturn
,

);

Enter fullscreen mode

Exit fullscreen mode

Then

declare
 
const
 
functionLike
:
 
ts
.
FunctionLikeDeclaration
;

if 
(
hasBodyStartingWithReturn
(
functionLike
))
 
{

 
// functionLike.body: ts.Block

 
// functionLike.body.statements[0]: ts.ReturnStatement

 
functionLike
.
body
.
statements
[
0
].
expression
;

}

Enter fullscreen mode

Exit fullscreen mode

Each step proves one thing.

There is no path string like

body.statements[0]

Enter fullscreen mode

Exit fullscreen mode

and no special AST DSL.

It's just small guards composed together.

## 🔒 Why Only One Concrete Key or Index?

There is an important limitation here.

A successful lookup proves one concrete location.

If we check

refineKey
(
"
expression
"
,
 
...)

Enter fullscreen mode

Exit fullscreen mode

we proved something about

parent
.
expression
;

Enter fullscreen mode

Exit fullscreen mode

We didnotprove that every property from some wider key domain passed the same test.

That's why the refinement helpers intentionally work with one concrete key or index.

Broad key unions and similar multi-location claims would make the resulting type much easier to overstate.

I would rather make the API slightly less magical than let one runtime lookup claim more than it actually checked.

## 🧪 What About TypeScript 7?

This research became especially interesting because TypeScript v7 changed the Compiler API landscape.

The examples in this section were verified against TypeScript v7.0.2.

As of TypeScript v7.0.2, AST types and predicates are exposed through

typescript/unstable/ast

Enter fullscreen mode

Exit fullscreen mode

So the same composition style can be used there

import
 
*
 
as
 
ast
 
from
 
"
typescript/unstable/ast
"
;

import
 
{
 
and
,
 
refineKey
 
}
 
from
 
"
is-kit
"
;

const
 
isCallWithIdentifierExpression
 
=
 
and
(

 
ast
.
isCallExpression
,

 
refineKey
(
"
expression
"
,
 
ast
.
isIdentifier
),

);

Enter fullscreen mode

Exit fullscreen mode

One thing I specifically investigated was whether TypeScript v7 made theseisXchecks unnecessary throughkindnarrowing.

For a genuine discriminated union, TypeScript can absolutely narrow from a literal discriminant.

But the broad ASTNodecurrently exposed by the TypeScript v7 AST surface is not that kind of closed discriminated union.

So with a broad AST node, theisXpredicates still matter.

For example

import
 
*
 
as
 
ast
 
from
 
"
typescript/unstable/ast
"
;

declare
 
const
 
node
:
 
ast
.
Node
;

if 
(
node
.
kind
 
===
 
ast
.
SyntaxKind
.
CallExpression
)
 
{

 
// broad ast.Node does not automatically

 
// expose CallExpression properties here

}

Enter fullscreen mode

Exit fullscreen mode

This distinction matters.

A custom AST type modeled as a discriminated union can behave differently.

That doesn't mean TypeScript v7's broadNodecurrently behaves the same way.

### Why Not MakeNodea Closed Union?

After I posted about this,Jake Baileygave a wonderfully concise answer:

because it's slow 😞

because it's slow 😞

— 
Jake Bailey (@jakebailey.dev)
 
2026-09-30T01:49:50.060Z

That makes the trade-off much easier to understand.

IfNodewere one closed discriminated union containing every AST node type,kindcould potentially give us stronger narrowing and exhaustive checks.

For example, with a closed union, we can use the familiarneverpattern

switch 
(
node
.
kind
)
 
{

 
// handle every known kind...

 
default
:
 
{

 
const
 
exhaustive
:
 
never
 
=
 
node
;

 
}

}

Enter fullscreen mode

Exit fullscreen mode

When a new variant is added, thatnevercheck can fail at compile time and tell us that our handling is no longer exhaustive.

But that stronger type-level model is not free.

The cost is type-checking performance, a very large closed union gives the checker more work to do.

So the broad shape ofast.Nodeis not simply a missing narrowing feature.

There is a real trade-off here

stronger compile-time exhaustiveness vs. type-checking performance

And that also helps explain why explicit predicates likeast.isCallExpression()still have an important role.

There is one more TypeScript 7-specific detail worth keeping in mind.

Theunstablepart of

typescript/unstable/ast

Enter fullscreen mode

Exit fullscreen mode

is also important.

I wouldn't build documentation promises around a still-evolving API surface.

The composition pattern is generic.

The exact TypeScript v7 integration can evolve with TypeScript itself.

## ✋ You Probably Don't Need This for Every AST Check

This is also important.

If I have one local condition

if 
(
ts
.
isReturnStatement
(
node
)
 
&&
 
node
.
expression
)
 
{

 
// node: ts.ReturnStatement

 
// node.expression: ts.Expression

 
visit
(
node
.
expression
);

}

Enter fullscreen mode

Exit fullscreen mode

I would leave it inline.

Really.

Turning it into

const
 
isReturnWithExpression
 
=
 
...

Enter fullscreen mode

Exit fullscreen mode

just because wecandoesn't automatically make the code better.

I think the useful split is

Situation                    

Prefer                                        

One local branch              

Native 
ts.isX
 checks                        

Repeated AST shape            

Named reusable guard                          

Project already uses 
is-kit

refineKey
, 
refineDefinedKey
, 
refineIndex

The goal isn't

Replace everyts.isXcondition withis-kit.

The goal is

When a runtime fact becomes reusable vocabulary, keep the narrowing reusable too.

## 🚫 What This Does Not Try to Do

is-kitdoesn't try to become a Compiler API framework.

It does not:

* wrap individual Compiler API functions
* validate complete AST node shapes
* control AST traversal
* detect AST cycles
* add a TypeScript runtime dependency
* require TypeScript as a peer dependency
* replace clear one-off inline checks

The Compiler API is simply a demanding real-world example of generic property refinement.

That's the boundary I want to keep.

## 🎯 The Important Part

I started this research thinking

Maybe the TypeScript Compiler API needs some special handling.

What I found was more general.

The recurring problem was

narrow parent
    ↓
check child
    ↓
preserve both facts
    ↓
reuse the predicate

Enter fullscreen mode

Exit fullscreen mode

That's useful for AST nodes, but it isn't really about AST nodes.

So my current mental model is:

* use native type guards for the actual runtime knowledge
* keep one-off conditions inline
* compose a named guard when the same checked shape becomes reusable
* preserve child refinement on the parent instead of rewriting intersection types by hand

For the Compiler API, that can look like

const
 
isCallWithIdentifierExpression
 
=
 
and
(

 
ts
.
isCallExpression
,

 
refineKey
(
"
expression
"
,
 
ts
.
isIdentifier
),

);

Enter fullscreen mode

Exit fullscreen mode

Small runtime checks.Small reusable pieces.And TypeScript keeps the facts we actually checked. 😸

I also wrote a more detailed guide with examples for required children, optional children, array indices, nested AST shapes, and TypeScript 7

Advanced Property Refinement with the TypeScript Compiler API

## Advanced Property Refinement with the TypeScript Compiler API | is-kit

Use TypeScript Compiler API guards as an advanced example of reusable property refinement across broad AST node types.

 is-kit.dev
 

And if you want to exploreis-kititself

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

If it looks useful, a ⭐ on GitHub is always very welcome!

Thanks for reading! 🙌

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse