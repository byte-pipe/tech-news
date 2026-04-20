---
title: ArrowJS — The first UI framework for the agentic era
url: https://arrow-js.com/
site_name: tldr
content_file: tldr-arrowjs-the-first-ui-framework-for-the-agentic-era
fetched_at: '2026-03-25T01:02:07.598012'
original_url: https://arrow-js.com/
date: '2026-03-25'
description: A tiny, blazing-fast, zero-dependency, type-safe framework. No build step required. Isolate agent-generated UI inside WebAssembly sandboxes while rendering full inline DOM directly in your app — no iframes, no pre-defined components.
tags:
- tldr
---

# The first UI framework for theagentic era

A tiny, blazing-fast, zero dependency, type-safe framework with no
 build step required.ArrowJS ships with the ability to isolate component logic inside Web
 Assemblysandboxeswhile rendering full inline DOM directly in your app — no iframes,
 no pre-defined UI components.Use it to build fast, maintainable applications — or to ship safe,
 flexible, on-demand UIs for your users without having to plan
 components in advance.

$

pnpm

create

arrow-js@latest

arrow-app

 Comparing Quotes


Live

 Here are the 3 HVAC quotes. Which one’s the best deal?


 I’ve broken down the key details from each quote. Here’s a side-by-side:


Sort by

 Price


 Efficiency


 Warranty


 Lowest Price


ClimateCraft

 $7,400


SEER

15

Warranty

5 yr

CoolAir Pro

 $8,200


SEER

16

Warranty

10 yr

AirFlow Plus

 $9,100


SEER

18

Warranty

12 yr

 Generated with ArrowJS Sandbox


## Why Arrow

Arrow is a reactive UI framework built around JavaScript primitives:
 Modules, functions, and template literals. Arrow is just TypeScript, so your coding agent already knows how to use it really well.

You only need 3 functions:

* reactive
* html
* component

Unlike other major frameworks, there is no "idomatic" way to use Arrow since it's just TypeScript functions and template literals. The entire documentation fits in less than 5% of a 200k context window.

Arrow requires no build step, no JSX compilation, no React compiler, no Vite plugin (there is one if you need SSR), no Vue template complier, and yet it runs incredibly fast at less than 5kb over the wire. When coupled with theArrow sandbox, it's perfect for interfaces produced by chat agents too.

## Quickstart

Scaffold a complete Vite 8 Arrow app with SSR, hydration, route-based
 metadata, and the full framework stack in one command:

$

pnpm

create

arrow-js@latest

arrow-app

### Coding agent skill

Install the Arrow coding agent skill wrapper if you want the same
 project-specific guidance in tools like Codex and Claude Code.

$

npx

@arrow-js/skill@latest

### Other ways to install

Arrow still works fine without a build tool. If you only need the core
 runtime, a simple module import is enough.

#### From npm:

npm
 install
 @arrow-js/core

#### From a CDN:

<
script
 type
=
"module"
>

 import
 {
reactive
,
html
 }
from
 'https://esm.sh/@arrow-js/core'

</
script
>

### Editor support

Install the officialArrowJS Syntaxextension for VSCode to get syntax highlighting and
 autocomplete insidehtmltemplate literals.
 Arrow also ships TypeScript definitions for full editor support.

## Community

Join theArrow Discordto ask questions, share what you're building, and connect with
 other developers using Arrow.

Follow the authorJustin Schroederon X for updates, releases, and behind-the-scenes development.

Browse the source, report issues, and contribute onGitHub.

## Reactive Data

reactive()turns plain objects, arrays, or expressions
 into live state that Arrow (or anyone else) can track and update from.

reactive(value)orreactive(() => value)

* Wrap objects or arrays to create observable state.
* Pass an expression to create a computed value.
* Use it for local component state, shared stores, and mutable props.
* Read properties normally. Arrow tracks those reads inside watchers
 and template expressions.
* Use$onand$offwhen you want manual
 subscriptions.

import
 {
function
 reactive
<
T
 extends
 ReactiveTarget
>(
data
:
 T
)
:
 Reactive
<
T
> (+
1
 overload
)
reactive
 }
from
 '@arrow-js/core'

const

const
 data
:
 Reactive
<{

 price
:
 number
;

 quantity
:
 number
;

}>
data
 =

reactive
<{

 price
:
 number
;

 quantity
:
 number
;

}>(
data
:
 {

 price
:
 number
;

 quantity
:
 number
;

})
:
 Reactive
<{

 price
:
 number
;

 quantity
:
 number
;

}> (+
1
 overload
)
reactive
({


price
:
number
price
:
 25
,


quantity
:
number
quantity
:
 10

})

var
 console
:
 Console
console
.
Console
.
log
(
...
data
:
any
[]):
void
The **`console.log()`** static method outputs a message to the console.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/console/log_static)
log
(
const
 data
:
 Reactive
<{

 price
:
 number
;

 quantity
:
 number
;

}>
data
.
price
:
number
price
)
// 25

### Computed values

reactive(() => value)reruns when its tracked reads
 change.

import
 {
function
 reactive
<
T
 extends
 ReactiveTarget
>(
data
:
 T
)
:
 Reactive
<
T
> (+
1
 overload
)
reactive
 }
from
 '@arrow-js/core'

const

const
 props
:
 Reactive
<{

 count
:
 number
;

 multiplier
:
 number
;

}>
props
 =

reactive
<{

 count
:
 number
;

 multiplier
:
 number
;

}>(
data
:
 {

 count
:
 number
;

 multiplier
:
 number
;

})
:
 Reactive
<{

 count
:
 number
;

 multiplier
:
 number
;

}> (+
1
 overload
)
reactive
({
count
:
number
count
:
 2
,
multiplier
:
number
multiplier
:
 10
 })

const

const
 data
:
 Reactive
<{

 total
:
 Computed
<
number
>;

}>
data
 =

reactive
<{

 total
:
 Computed
<
number
>;

}>(
data
:
 {

 total
:
 Computed
<
number
>;

})
:
 Reactive
<{

 total
:
 Computed
<
number
>;

}> (+
1
 overload
)
reactive
({


total
:
Computed
<
number
>
total
:

reactive
<
number
>(
effect
: ()
=>
 number
):
Computed
<
number
> (
+
1
 overload
)
reactive
(()
=>

const
 props
:
 Reactive
<{

 count
:
 number
;

 multiplier
:
 number
;

}>
props
.
count
:
number
count
 *

const
 props
:
 Reactive
<{

 count
:
 number
;

 multiplier
:
 number
;

}>
props
.
multiplier
:
number
multiplier
)

})

var
 console
:
 Console
console
.
Console
.
log
(
...
data
:
any
[]):
void
The **`console.log()`** static method outputs a message to the console.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/console/log_static)
log
(
const
 data
:
 Reactive
<{

 total
:
 Computed
<
number
>;

}>
data
.
total
:
number
total
)
// 20

const
 props
:
 Reactive
<{

 count
:
 number
;

 multiplier
:
 number
;

}>
props
.
count
:
number
count
 =
 3

var
 console
:
 Console
console
.
Console
.
log
(
...
data
:
any
[]):
void
The **`console.log()`** static method outputs a message to the console.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/console/log_static)
log
(
const
 data
:
 Reactive
<{

 total
:
 Computed
<
number
>;

}>
data
.
total
:
number
total
)
// 30

Tip

data.totalreads like a normal value even though it is
 backed by a tracked expression.

## Templates

To render DOM elements with Arrow you use thehtmltagged template literal.

html`...`— create a mountable template

* Templates can be mounted directly, passed around, or returned from
 components.
* Expression slots are static by default, but if callable functions
 are provided they will update when their respective reactive data is
 changed. In other words${data.foo}is static but${() => data.foo}is reactive.
* Templates can render text, attributes, properties, lists, nested
 templates, and events.

Plain values render once. If you pass a function like() => data.count, Arrow tracks the reactive reads inside
 that function and updates only that part of the template when they
 change.

### Attributes

Use a function expression to keep an attribute in sync.

import
 {
function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
,
function
 reactive
<
T
 extends
 ReactiveTarget
>(
data
:
 T
)
:
 Reactive
<
T
> (+
1
 overload
)
reactive
 }
from
 '@arrow-js/core'

const

const
 data
:
 Reactive
<{

 disabled
:
 boolean
;

}>
data
 =

reactive
<{

 disabled
:
 boolean
;

}>(
data
:
 {

 disabled
:
 boolean
;

})
:
 Reactive
<{

 disabled
:
 boolean
;

}> (+
1
 overload
)
reactive
({
disabled
:
boolean
disabled
:
 false
 })

function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
`
<
button
 disabled
=
"
${
()
 =>

const
 data
:
 Reactive
<{

 disabled
:
 boolean
;

}>
data
.
disabled
:
boolean
disabled
}
"
>

 Save

</
button
>
`

Tip

Returningfalsefrom an attribute expression will
 remove the attribute. This makes it easy to toggle attributes.

import
 {
function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
,
function
 reactive
<
T
 extends
 ReactiveTarget
>(
data
:
 T
)
:
 Reactive
<
T
> (+
1
 overload
)
reactive
 }
from
 '@arrow-js/core'

const

const
 data
:
 Reactive
<{

 disabled
:
 boolean
;

}>
data
 =

reactive
<{

 disabled
:
 boolean
;

}>(
data
:
 {

 disabled
:
 boolean
;

})
:
 Reactive
<{

 disabled
:
 boolean
;

}> (+
1
 overload
)
reactive
({
disabled
:
boolean
disabled
:
 false
 })

function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
`
<
button
 disabled
=
"
${
()
 =>

const
 data
:
 Reactive
<{

 disabled
:
 boolean
;

}>
data
.
disabled
:
boolean
disabled
 ?
 true
 :
 false
}
"
>

 Save

</
button
>
`

### Lists

Return an array of templates to render a list. Add.key(...)when identity must survive reorders.

import
 {
function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
,
function
 reactive
<
T
 extends
 ReactiveTarget
>(
data
:
 T
)
:
 Reactive
<
T
> (+
1
 overload
)
reactive
 }
from
 '@arrow-js/core'

const

const
 data
:
 Reactive
<{

 todos
:
 {

 id
:
 number
;

 text
:
 string
;

 }[];

}>
data
 =

reactive
<{

 todos
:
 {

 id
:
 number
;

 text
:
 string
;

 }[];

}>(
data
:
 {

 todos
:
 {

 id
:
 number
;

 text
:
 string
;

 }[];

})
:
 Reactive
<{

 todos
:
 {

 id
:
 number
;

 text
:
 string
;

 }[];

}> (+
1
 overload
)
reactive
({


todos
: {

 id
:
number
;

 text
:
string
;

}[]
todos
:
 [

 {
id
:
number
id
:
 1
,
text
:
string
text
:
 'Write docs'
 },

 {
id
:
number
id
:
 2
,
text
:
string
text
:
 'Ship app'
 },

 ],

})

function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
`
<
ul
>

 ${
()
 =>

const
 data
:
 Reactive
<{

 todos
:
 {

 id
:
 number
;

 text
:
 string
;

 }[];

}>
data
.
todos
: {

 id
:
number
;

 text
:
string
;

}[]
|
 Reactive
<{

 id
:
 number
;

 text
:
 string
;

}[]>
todos
.
Array
<
T
>
.
map
<
ArrowTemplate
>(
callbackfn
: ((
value
:
 {

 id
:
 number
;

 text
:
 string
;

},
index
:
 number
,
array
:
 {

 id
:
 number
;

 text
:
 string
;

}[])
=>
 ArrowTemplate
)
&
 ((
value
:
 {

 id
:
 number
;

 text
:
 string
;

}
|
 Reactive
<{

 id
:
 number
;

 text
:
 string
;

}>,
index
:
 number
,
array
:
 ({

 id
:
 number
;

 text
:
 string
;

}
|
 Reactive
<{

 id
:
 number
;

 text
:
 string
;

}>)[])
=>
 ArrowTemplate
),
thisArg
?:
 any
):
ArrowTemplate
[]
Calls a defined callback function on each element of an array, and returns an array that contains the results.
@param
callbackfn A function that accepts up to three arguments. The map method calls the callbackfn function one time for each element in the array.
@param
thisArg An object to which the this keyword can refer in the callbackfn function. If thisArg is omitted, undefined is used as the this value.
map
((
todo
:
any
todo
)
 =>


function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
`
<
li
>
${
todo
:
any
todo
.
text
}
</
li
>
`
.
ArrowTemplate
.
key
: (
key
:
 string
 |
 number
 |
 undefined
)
=>
 ArrowTemplate
key
(
todo
:
any
todo
.
id
)

 )
}

</
ul
>
`

Tip

Keys are only necessary if you want to preserve the DOM nodes and
 their state. Avoid using the index as a key.

import
 {
function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
,
function
 reactive
<
T
 extends
 ReactiveTarget
>(
data
:
 T
)
:
 Reactive
<
T
> (+
1
 overload
)
reactive
 }
from
 '@arrow-js/core'

const

const
 data
:
 Reactive
<{

 tags
:
 string
[];

}>
data
 =

reactive
<{

 tags
:
 string
[];

}>(
data
:
 {

 tags
:
 string
[];

})
:
 Reactive
<{

 tags
:
 string
[];

}> (+
1
 overload
)
reactive
({
tags
:
string
[]
tags
:
 [
'alpha'
,
'beta'
,
'gamma'
] })

function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
`
<
ul
>

 ${
()
 =>

const
 data
:
 Reactive
<{

 tags
:
 string
[];

}>
data
.
tags
:
string
[]
|
 Reactive
<
string
[]
>
tags
.
Array
<
T
>
.
map
<
ArrowTemplate
>(
callbackfn
: (
value
:
 string
,
index
:
 number
,
array
:
 string
[])
=>
 ArrowTemplate
,
thisArg
?:
 any
):
ArrowTemplate
[]
Calls a defined callback function on each element of an array, and returns an array that contains the results.
@param
callbackfn A function that accepts up to three arguments. The map method calls the callbackfn function one time for each element in the array.
@param
thisArg An object to which the this keyword can refer in the callbackfn function. If thisArg is omitted, undefined is used as the this value.
map
((
tag
:
string
tag
)
 =>

function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
`
<
li
>
${
tag
:
string
tag
}
</
li
>
`
)
}

</
ul
>
`

### Events

@eventNameattaches an event listener.

import
 {
function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
 }
from
 '@arrow-js/core'

function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
`
<
button
 @click
=
"
${
(
e
:
any
e
)
 =>

var
 console
:
 Console
console
.
Console
.
log
(
...
data
:
any
[]):
void
The **`console.log()`** static method outputs a message to the console.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/console/log_static)
log
(
e
:
any
e
)
}
"
>
Click
</
button
>
`

## Components

Arrow components are plain functions wrapped withcomponent(). A component mounts once per render slot and
 keeps local state while that slot survives parent rerenders.

* Pass a reactive object as props.
* Read props lazily inside expressions like() => props.count.
* Keep local component state withreactive()inside the
 component.
* Use.key(...)when rendering components in keyed lists.

import
 {
component
,
html
,
onCleanup
,
reactive
 }
from
 '@arrow-js/core'

import
 type
 {
Props
 }
from
 '@arrow-js/core'

const
 parentState
 =
 reactive
({
count
:
 1
 })

const
 Counter
 =
 component
((
props
:
 Props
<{
count
:
 number
 }>)
=>
 {

 const
 local
 =
 reactive
({
clicks
:
 0
 })

 const
 onResize
 =
 ()
=>
 console
.
log
(
window
.
innerWidth
)

 window
.
addEventListener
(
'resize'
,
onResize
)

 onCleanup
(()
=>
 window
.
removeEventListener
(
'resize'
,
onResize
))

 return
 html
`
<
button
 @click
=
"
${
()
 =>
 local
.
clicks
++
}
"
>

 Root count
${
()
 =>
 props
.
count
}
 | Local clicks
${
()
 =>
 local
.
clicks
}

 </
button
>
`

})

html
`
<
section
>

 <
h3
>
Dashboard
</
h3
>

 ${
Counter
(
parentState
)
}

</
section
>
`

Key concept

The component function itself is not rerun on every parent update.
 Arrow keeps the instance for that slot and retargets its props when
 needed. That makes local state stable across higher-order rerenders.

In the common case, just pass a reactive object directly as the
 component props.

import
 {
component
,
html
,
reactive
 }
from
 '@arrow-js/core'

const
 state
 =
 reactive
({
count
:
 1
,
theme
:
 'dark'
 })

const
 Counter
 =
 component
((
props
)
=>

 html
`
<
strong
>
${
()
 =>
 props
.
count
}
</
strong
>
`

)

html
`
<
p
>

 Current count:

 ${
Counter
(
state
)
}

</
p
>
`

Tip

Props stay live when you read them lazily. Avoid destructuring them
 once at component creation time if you expect updates.

UseonCleanup()inside a component when you set up
 manual listeners, timers, or sockets that need teardown when the
 component slot unmounts.

### Async components

The same corecomponent()also accepts async factories
 when the Arrow async runtime is present:

import
 {
component
,
html
 }
from
 '@arrow-js/core'

import
 type
 {
Props
 }
from
 '@arrow-js/core'

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
 }

const
 UserName
 =
 component
(

 async
 ({
id
 }
:
 Props
<{
id
:
 string
 }>)
=>
 {

 const
 user
 =
 await
 fetch
(
`/api/users/
${
id
}
`
)

 .
then
((
r
)
=>
 r
.
json
()
as
 Promise
<
User
>)

 return
 user
.
name

 },

 {
fallback
:
 html
`
<
span
>
Loading user…
</
span
>
`
 }

)

const
 UserCard
 =
 component
((
props
:
 Props
<{
id
:
 string
 }>)
=>

 html
`
<
article
>
${
UserName
(
props
)
}
</
article
>
`

)

The async body resolves data, and the surrounding template stays
 reactive in the usual Arrow way. SSR waits for async components to
 settle, and hydration resumes JSON-safe results from serialized
 payload data automatically.

Tip

Most async components need no extra options. Arrow assigns ids,
 snapshots JSON-safe results, and renders resolved values directly by
 default. Reach forfallback,render,serialize,deserialize, oridPrefixonly when the default behavior is not enough.

## Watching Data

watch(effect)orwatch(getter, afterEffect)

* Use it for derived side effects outside templates.
* Dependencies are discovered automatically from reactive reads.
* Arrow also drops dependencies that are no longer touched on later
 runs.
* Watchers created inside a component are stopped automatically when
 that component unmounts.

Single-effect form:

import
 {
function
 reactive
<
T
 extends
 ReactiveTarget
>(
data
:
 T
)
:
 Reactive
<
T
> (+
1
 overload
)
reactive
,
function
 watch
<
F
 extends
 (
...
args
:
 unknown
[])
=>
 unknown
>(
effect
:
 F
)
:
 [
returnValue
:
ReturnType
<
F
>,
stop
: ()
=>
 void
] (+
1
 overload
)
watch
 }
from
 '@arrow-js/core'

const

const
 data
:
 Reactive
<{

 price
:
 number
;

 quantity
:
 number
;

 logTotal
:
 boolean
;

}>
data
 =

reactive
<{

 price
:
 number
;

 quantity
:
 number
;

 logTotal
:
 boolean
;

}>(
data
:
 {

 price
:
 number
;

 quantity
:
 number
;

 logTotal
:
 boolean
;

})
:
 Reactive
<{

 price
:
 number
;

 quantity
:
 number
;

 logTotal
:
 boolean
;

}> (+
1
 overload
)
reactive
({
price
:
number
price
:
 25
,
quantity
:
number
quantity
:
 10
,
logTotal
:
boolean
logTotal
:
 true
 })

watch
<()
=>
 void
>(
effect
: ()
=>
 void
): [
returnValue
:
void
,
stop
: ()
=>
 void
] (
+
1
 overload
)
watch
(()
=>
 {

 if
 (
const
 data
:
 Reactive
<{

 price
:
 number
;

 quantity
:
 number
;

 logTotal
:
 boolean
;

}>
data
.
logTotal
:
boolean
logTotal
) {


var
 console
:
 Console
console
.
Console
.
log
(
...
data
:
any
[]):
void
The **`console.log()`** static method outputs a message to the console.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/console/log_static)
log
(
`Total:
${
const
 data
:
 Reactive
<{

 price
:
 number
;

 quantity
:
 number
;

 logTotal
:
 boolean
;

}>
data
.
price
:
number
price
 *

const
 data
:
 Reactive
<{

 price
:
 number
;

 quantity
:
 number
;

 logTotal
:
 boolean
;

}>
data
.
quantity
:
number
quantity
}
`
)

 }

})

Getter plus effect form:

import
 {
function
 reactive
<
T
 extends
 ReactiveTarget
>(
data
:
 T
)
:
 Reactive
<
T
> (+
1
 overload
)
reactive
,
function
 watch
<
F
 extends
 (
...
args
:
 unknown
[])
=>
 unknown
>(
effect
:
 F
)
:
 [
returnValue
:
ReturnType
<
F
>,
stop
: ()
=>
 void
] (+
1
 overload
)
watch
 }
from
 '@arrow-js/core'

const

const
 data
:
 Reactive
<{

 price
:
 number
;

 quantity
:
 number
;

 logTotal
:
 boolean
;

}>
data
 =

reactive
<{

 price
:
 number
;

 quantity
:
 number
;

 logTotal
:
 boolean
;

}>(
data
:
 {

 price
:
 number
;

 quantity
:
 number
;

 logTotal
:
 boolean
;

})
:
 Reactive
<{

 price
:
 number
;

 quantity
:
 number
;

 logTotal
:
 boolean
;

}> (+
1
 overload
)
reactive
({
price
:
number
price
:
 25
,
quantity
:
number
quantity
:
 10
,
logTotal
:
boolean
logTotal
:
 true
 })

watch
<()
=>
 number
, (
total
:
 number
)
=>
 void
>(
effect
: ()
=>
 number
,
afterEffect
: (
total
:
 number
)
=>
 void
): [
returnValue
:
void
,
stop
: ()
=>
 void
] (
+
1
 overload
)
watch
(

 ()
=>

const
 data
:
 Reactive
<{

 price
:
 number
;

 quantity
:
 number
;

 logTotal
:
 boolean
;

}>
data
.
logTotal
:
boolean
logTotal
 ?

const
 data
:
 Reactive
<{

 price
:
 number
;

 quantity
:
 number
;

 logTotal
:
 boolean
;

}>
data
.
price
:
number
price
 *

const
 data
:
 Reactive
<{

 price
:
 number
;

 quantity
:
 number
;

 logTotal
:
 boolean
;

}>
data
.
quantity
:
number
quantity
 :
 null
,

 (
total
:
number
total
)
=>

total
:
number
total
 !==
 null
 &&

var
 console
:
 Console
console
.
Console
.
log
(
...
data
:
any
[]):
void
The **`console.log()`** static method outputs a message to the console.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/console/log_static)
log
(
`Total:
${
total
:
number
total
}
`
)

)

## Sandbox

@arrow-js/sandboxlets you run JS/TS/Arrow inside
 a WASM virtual machine while the host page keeps ownership of the real DOM rendered byhtml(). These two environments only communicate through serialized messages, which allows safe execution of AI-generated code and makes the sandbox a good fit for inline UI produced by chat agents.

* sourcemust include exactly onemain.tsormain.jsentry file.
* main.cssis optional and is injected into the sandbox
 host root.
* The sandbox renders through a stable<arrow-sandbox>custom element.
* Calloutput(payload)inside sandboxed code to send data
 back through the optionalevents.outputhandler.

import
 {
function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
 }
from
 '@arrow-js/core'

import
 {
function
 sandbox
<
T
 extends
 {

 source
:
 object
;

 shadowDOM
?
:
 boolean
;

 onError
?
:
 (
error
:
 Error
 |
 string
)
=>
 void
;

 debug
?
:
 boolean
;

}>(
props
:
 T
,
events
?
:
 SandboxEvents
)
:
 ArrowTemplate
sandbox
 }
from
 '@arrow-js/sandbox'

const

const
 root
:
 HTMLElement
root
 =

var
 document
:
 Document
**`window.document`** returns a reference to the document contained in the window.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Window/document)
document
.
Document
.
getElementById
(
elementId
:
string
):
HTMLElement
 |
 null
Returns the first element within node's descendants whose ID is elementId.

[MDN Reference](https://developer.mozilla.org/docs/Web/API/Document/getElementById)
getElementById
(
'app'
)

if
 (
!
const
 root
:
 HTMLElement
root
)
throw
 new

var
 Error
:
 ErrorConstructor

new
 (
message
?
:
 string
,
options
?
:
 ErrorOptions
)
=>
 Error
 (
+
1
 overload
)
Error
(
'Missing #app root'
)

const

const
 source
:
 {

 'main.ts'
:
 string
;

 'main.css'
:
 string
;

}
source
 =
 {

 'main.ts'
:
 [

 "import { html, reactive } from '@arrow-js/core'"
,

 ''
,

 'const state = reactive({ count: 0 })'
,

 ''
,

 'export default html`<button @click="${() => state.count++}">'
,

 ' Count ${() => state.count}'
,

 '</button>`'
,

 ].
Array
<
string
>
.
join
(
separator
?:
 string
):
string
Adds all the elements of an array into a string, separated by the specified separator string.
@param
separator A string used to separate one element of the array from the next in the resulting string. If omitted, the array elements are separated with a comma.
join
(
'
\n
'
),

 'main.css'
:
 [

 'button {'
,

 ' font: inherit;'
,

 ' padding: 0.75rem 1rem;'
,

 '}'
,

 ].
Array
<
string
>
.
join
(
separator
?:
 string
):
string
Adds all the elements of an array into a string, separated by the specified separator string.
@param
separator A string used to separate one element of the array from the next in the resulting string. If omitted, the array elements are separated with a comma.
join
(
'
\n
'
),

}

function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
`
<
section
>
${
sandbox
<{

 source
:
 {

 'main.ts'
:
 string
;

 'main.css'
:
 string
;

 };

}>(
props
:
 {

 source
:
 {

 'main.ts'
:
 string
;

 'main.css'
:
 string
;

 };

},
events
?
:
 SandboxEvents
)
:
 ArrowTemplate
sandbox
({

source
: {

 'main.ts'
:
string
;

 'main.css'
:
string
;

}
source
 })
}
</
section
>
`
(
const
 root
:
 HTMLElement
root
)

Live Demo

See sandbox isolation in action

A full interactive example showing reactivity inside the VM,
 blocked browser globals, and the restricted fetch bridge.

Open in Playground
 →

### Prompt for agents

If you want an agent to generate a sandbox payload directly, this
 prompt keeps the output narrow and aligned with Arrow.

Agent Prompt

Build this UI as an Arrow sandbox payload. Return an object for sandbox({ source, ... }) with exactly one entry file named main.ts or main.js, plus main.css only if styles are needed. Use @arrow-js/core primitives directly: reactive(...) for state, html
`
...
`
 for DOM, and component(...) only when reusable local state or composition is actually needed. Arrow expression slots are static by default, so any live value must be wrapped in a callable function like ${() => state.count}. Use event bindings like @click="${() => state.count++}", do not use JSX, React hooks, Vue directives, direct DOM mutation, or framework-specific render APIs.

Export a default Arrow template or component result from main.ts. Keep the example self-contained, prefer a single clear root view, and communicate back to the host with output(payload) when needed. Put CSS in main.css, keep payloads JSON-serializable, and only return the files that are necessary for the requested interface. If you create multiple files, make sure imports match the virtual filenames you place in source.

### JSON schema tool

If your agent supports tool calling, this schema produces the exact
 argument object expected bysandbox().

create_arrow_sandbox

{

 "name"
:
"create_arrow_sandbox"
,

 "description"
:
"Produce arguments for @arrow-js/sandbox."
,

 "inputSchema"
: {

 "type"
:
"object"
,

 "additionalProperties"
:
false
,

 "properties"
: {

 "source"
: {

 "type"
:
"object"
,

 "description"
:
"Virtual files passed to sandbox({ source }). Must include main.ts or main.js. main.css is optional."
,

 "additionalProperties"
:
false
,

 "properties"
: {

 "main.ts"
: {

 "type"
:
"string"
,

 "description"
:
"Main Arrow TypeScript entry file."

 },

 "main.js"
: {

 "type"
:
"string"
,

 "description"
:
"Main Arrow JavaScript entry file."

 },

 "main.css"
: {

 "type"
:
"string"
,

 "description"
:
"Optional stylesheet for the sandbox root."

 }

 },

 "anyOf"
: [

 {
"required"
: [
"main.ts"
] },

 {
"required"
: [
"main.js"
] }

 ]

 },

 "shadowDOM"
: {

 "type"
:
"boolean"
,

 "description"
:
"Whether the sandbox should render inside shadow DOM."

 },

 "debug"
: {

 "type"
:
"boolean"
,

 "description"
:
"Whether sandbox debug logging should be enabled."

 }

 },

 "required"
: [
"source"
]

 }

}

Early Access

From the team behindFormKit,Tempo,AutoAnimate,
 andDrag and Drop— Standard Agents is an open standard for creating
 domain-specific agents you can distribute and compose together to form
 safe, efficient, and effective agents. Join the early access list.

Request Early Access

You're on the list! We'll be in touch.

## Routing

The Vite scaffold uses a simplerouteToPage(url)entry so
 the server and browser both resolve the same route tree.

* Choose a route from the incoming URL.
* Return the page status, metadata, and Arrow view together.
* Reuse the same routing function for SSR and hydration so both sides
 render the same page shape.

import
 {
function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
 }
from
 '@arrow-js/core'

export
 function

function
 routeToPage
(
url
:
 string
)
:
 {

 status
:
 number
;

 title
:
 string
;

 view
:
 ArrowTemplate
;

}
routeToPage
(
url
:
string
url
:
 string
) {

 if
 (
url
:
string
url
 ===
 '/'
) {

 return
 {


status
:
number
status
:
 200
,


title
:
string
title
:
 'Home'
,


view
:
ArrowTemplate
view
:

function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
`
<
main
>
Home
</
main
>
`
,

 }

 }

 return
 {


status
:
number
status
:
 404
,


title
:
string
title
:
 'Not Found'
,


view
:
ArrowTemplate
view
:

function
 html
(
strings
:
 TemplateStringsArray
 |
 string
[],
...
expressions
:
 unknown
[])
:
 ArrowTemplate
html
`
<
main
>
Not found
</
main
>
`
,

 }

}

## Examples

Each example runs in the playground with full source you can edit
 live.

### ✅Todo List

A task tracker with reactive arrays, keyed lists, and computed filtering.

Open in Playground →

### 🍅Pomodoro Timer

A focus timer with SVG progress ring, intervals, and computed formatting.

Open in Playground →

### 🎨Color Palette

A Coolors-style harmony palette generator with reactive style binding and computed colors.

Open in Playground →

### 🔐Password Generator

A configurable password tool with reactive toggles and a strength meter.

Open in Playground →

### 🪗Accordion

Expandable FAQ sections where each component instance keeps its own state.

Open in Playground →

### 📡Live Feed

An auto-updating event feed with reactive array mutations and timed entries.

Open in Playground →

### 📊Data Table

A sortable data table with reactive column sorting, keyed rows, and computed ordering.

Open in Playground →

### 📁Tabs

A tabbed interface with ARIA roles, animated panel transitions, and per-tab content.

Open in Playground →

### 🖼️Photo Gallery

A responsive image grid with a lightbox carousel, keyboard navigation, and lazy loading.

Open in Playground →

### 🎮Flappy Arrow

Navigate ()=> through ASCII pipes in this flappy-bird tribute with reactive state and a RAF game loop.

Open in Playground →

### 🛡️Sandbox

Run untrusted Arrow code in a WASM VM with isolated DOM, restricted fetch, and one-way output.

Open in Playground →

Playground

Build something with Arrow

Open a live editor with a starter template, hot reloading, and
 every Arrow package ready to import.

Open Playground
 →
