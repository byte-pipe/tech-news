---
title: 'State Management in Front-end Web Development: Mutators - DEV Community'
url: https://dev.to/abbeyperini/state-management-in-front-end-web-development-mutators-24gp
site_name: devto
content_file: devto-state-management-in-front-end-web-development-muta
fetched_at: '2026-08-20T19:30:46.276003'
original_url: https://dev.to/abbeyperini/state-management-in-front-end-web-development-mutators-24gp
author: Abbey Perini
date: '2026-08-19'
description: Libraries like Valtio and Pinia for Vue use a mutator pattern instead of the actions, dispatch, and... Tagged with webdev, react, vue, javascript.
tags: '#webdev, #react, #vue, #javascript'
---

Libraries likeValtioandPiniafor Vue use a mutator pattern instead of theactions, dispatch, and reducers pattern.

You can find the Valtio example in thereact-state GitHub repoand the Pinia example in thevue-state GitHub repo. I'm usingReact19.1.0,Valtio2.3.2,Vue13.5.40 andPinia4.0.3.

1. Mutability
2. Mutators
3. Pinia Example
4. Valtio Example
5. Conclusion

## Mutability

Mutators mutate mutable state. You can change a part of your state without replacing the whole thing.

This article is a lot shorter than the last part of the series. Mutators seem much more intuitive to learn and more computationally efficient. (We don't have to replace the entire object.) So why not always use mutable state?

The mutator pattern allows you to have side effects in your state update methods. Mutable state is non-deterministic. It is easy to create transient bugs that are difficult to troubleshoot, likerace conditions. The result of your updates may vary wildly depending on the order of method calls, (especially with parallel processing.)

The actions, dispatch, and reducers pattern forces you to define and handle every possible permutation of your state in the store. Mutators allow you to handle possible permutations when and how you want, including outside of the store. This may lead to verbose code handling every possible permutation in your components.

This isn't to say that the mutator pattern inherently produces bugs. Where the actions, dispatch, and reducers pattern imposes strict rules, the mutator pattern gives you freedom. With freedom comes the opportunity to create more bugs.

## Mutators

In the first part of this series, I said that reactive state is essentially creating getters and setters. Another set of terms for the same pattern is accessors and mutators.

In other words, instead of creating theobserver patternwith actions, dispatch, and reducers, mutators just use the observer pattern.

Typically, this uses aProxyunder the hood. A Proxy is a copy of a JavaScript object (the target) and a handler. The handler defines operations to be performed on the target like accessors and mutators.

The methods for accessing state are called getters or accessors. The methods for mutating state are typically called actions.

## Pinia Example

The first thing I need to do is initialize Pinia as a plugin.

// main.ts

import
 
{
 
createApp
 
}
 
from
 
'
vue
'
;

import
 
{
 
createPinia
 
}
 
from
 
'
pinia
'
;

import
 
App
 
from
 
'
./App.vue
'
;

const
 
pinia
 
=
 
createPinia
();

const
 
app
 
=
 
createApp
(
App
);

app
.
use
(
pinia
);

app
.
mount
(
'
#app
'
);

Enter fullscreen mode

Exit fullscreen mode

I'll be using the Setup Store syntax, because I'm more familiar withComposition APIsyntax. Plus, I want the ability to usewatchersandcomposablesin my stores. The docs provide examples for theOptions Stores syntax, if you're more comfortable with that.

Next, I create my store. Everything can go inside the store, include my update methods, called actions.

// stores/shibas.ts

import
 
{
 
defineStore
 
}
 
from
 
'
pinia
'
;

import
 
{
 
ref
,
 
type
 
Ref
 
}
 
from
 
'
vue
'
;

export
 
const
 
useShibaStore
 
=
 
defineStore
(
'
shibas
'
,
 
()
 
=>
 
{

 
// state

 
const
 
count
 
=
 
ref
(
0
);

 
const
 
shibaList
:
 
Ref
<
string
[]
>
 
=
 
ref
([]);

 
const
 
pending
 
=
 
ref
(
false
);

 
const
 
errorMessage
 
=
 
ref
(
""
);

 
// action

 
async
 
function
 
increment
(
number
:
 
number
)
 
{

 
errorMessage
.
value
 
=
 
""
;

 
count
.
value
 
+=
 
number
;

 
pending
.
value
 
=
 
true
;

 
const
 
response
 
=
 
await
 
fetch
(
`https://dog.ceo/api/breed/shiba/images/random/
${
number
}
`
);

 
const
 
shibas
 
=
 
await
 
response
.
json
();

 
pending
.
value
 
=
 
false
;

 
if 
(
shibas
.
status
 
!==
 
"
success
"
)
 
{

 
errorMessage
.
value
 
=
 
shibas
.
status
!
.
toString
();

 
return
;

 
}

 
return
 
shibas
.
message
.
forEach
((
shiba
:
 
string
)
 
=>
 
shibaList
.
value
.
push
(
shiba
))

 
}

 
return
 
{
 
count
,
 
shibaList
,
 
increment
,
 
pending
,
 
errorMessage
 
}

})

Enter fullscreen mode

Exit fullscreen mode

Finally, I use my store in my component to display the shibas.

// components/shibaCounter.vue

<
script
 
setup
 
lang
=
"
ts
"
>

import
 
{
 
useShibaStore
 
}
 
from
 
'
@/stores/shibas
'
;

import
 
{
 
storeToRefs
 
}
 
from
 
'
pinia
'
;

const
 
shibas
 
=
 
useShibaStore
();

// Destructuring without storeToRefs will break reactivity

const
 
{
 
count
,
 
shibaList
,
 
pending
,
 
errorMessage
 
}
 
=
 
storeToRefs
(
shibas
)

function
 
handleIncrement
(
e
:
 
SubmitEvent
)
 
{

 
const
 
form
 
=
 
e
.
target
 
as
 
HTMLFormElement
;

 
// Actions can be used as store properties

 
shibas
.
increment
(
parseInt
(
form
.
number
.
value
));

}

<
/script
>

<
template
>

 
<
div
>

 
<
span
>
Shibas
:
 
{{
count
}}
<
/span
>

 
<
form
 
@
submit
.
prevent
=
"
handleIncrement
"
>

 
<
label
 
for
=
'
number
'
>
Number
<
/label
>

 
<
input
 
id
=
'
number
'
 
type
=
"
number
"
/>

 
<
button
 
type
=
"
submit
"
>
Add
 
Shibas
<
/button
>

 
<
/form
>

 
<
p
 
v
-
if
=
"
pending
"
>
Pending
<
/p
>

 
<
p
 
v
-
if
=
"
errorMessage.length > 0
"
>
{{
errorMessage
}}
<
/p
>

 
<
img
 
v
-
for
=
"
shiba in shibaList
"
 
:
key
=
"
shiba
"
 
:
src
=
"
shiba
"
 
alt
=
"
shiba
"
 
/>

 
<
/div
>

<
/template
>

<
style
 
lang
=
"
css
"
>

img
 
{

 
width
:
 
300
px
;

}

<
/style
>

Enter fullscreen mode

Exit fullscreen mode

## Valtio Example

I'm using a Valtio example becauseZustand is kind of a hybrid. Zustand's update syntax doesn't use actions, dispatch, and reducers. It's closer to accessors and mutators. However, it usesImmerunder the hood to keep state immutable. If your updates get too complex and Immer can't keep up, you have to handle the immutability yourself.

First, I instantiate my proxy (store).

// ShibaCounter-Valtio.js

import
 
{
 
proxy
,
 
useSnapshot
 
}
 
from
 
'
valtio
'

export
 
const
 
shibaStore
 
=
 
proxy
({

 
count
:
 
0
,

 
shibaList
:
 
[],

 
pending
:
 
false
,

 
error
:
 
false
,

});

Enter fullscreen mode

Exit fullscreen mode

Then, I create my component that accesses the proxy usinguseSnapshot. This creates a read-only subscriber that watches for changes. Note that unlike Redux, I don't have to rely onuseEffectto trigger side effects.

import
 
{
 
useSnapshot
 
}
 
from
 
'
valtio
'
;

import
 
{
 
shibaState
,
 
increment
 
}
 
from
 
'
../ShibaCounter-Valtio
'
;

export
 
function
 
ShibaCounterValtio
()
 
{

 
const
 
shibaSnap
 
=
 
useSnapshot
(
shibaState
);

 
function
 
handleIncrement
(
event
)
 
{

 
event
.
preventDefault
();

 
increment
(
parseInt
(
event
.
target
.
number
.
value
));

 
}

 
let
 
shibaImages
 
=
 
shibaSnap
.
shibaList
.
map
(
shiba
 
=>
 
{

 
return 
(

 
<
img
 
src
=
{
shiba
}
 
alt
=
"
shiba
"
 
key
=
{
shiba
}
>

 
<
/img
>

 
);

 
})

 
return 
(

 
<
div
>

 
<
span
>
Shibas
:
 
{
shibaSnap
.
count
}
<
/span
>

 
<
form
 
onSubmit
=
{(
event
)
 
=>
 
handleIncrement
(
event
)}
>

 
<
label
 
htmlFor
=
'
number
'
>
Number
<
/label
>

 
<
input
 
id
=
'
number
'
 
type
=
"
number
"
/>

 
<
button
 
type
=
"
submit
"
>
Add
 
Shibas
<
/button
>

 
<
/form
>

 
{
 
shibaSnap
.
pending
 
&&
 
<
p
>
Pending
<
/p>
}

 
{
 
shibaSnap
.
error
 
&&
 
<
p
>
{
error
}
<
/p> 
}

 
{
 
shibaImages
 
}

 
<
/div
>

 
)

}

Enter fullscreen mode

Exit fullscreen mode

Finally, I create my increment action. Valtio is purposefullyunopinionated about organizing your actions. I like keeping it all together, so I'm just going to export my actions from the same file as my state.

// ShibaCounter-Valtio.js

export
 
async
 
function
 
increment
(
number
)
 
{

 
shibaState
.
error
 
=
 
""
;

 
shibaState
.
count
 
+=
 
number
;

 
shibaState
.
pending
 
=
 
true
;

 
const
 
response
 
=
 
await
 
fetch
(
`https://dog.ceo/api/breed/shiba/images/random/
${
number
}
`
);

 
const
 
shibas
 
=
 
await
 
response
.
json
();

 
shibaState
.
pending
 
=
 
false
;

 
if 
(
shibas
.
status
 
!==
 
"
success
"
)
 
{

 
shibaState
.
error
 
=
 
shibas
.
status
.
toString
();

 
return
;

 
}

 
return
 
shibas
.
message
.
forEach
((
shiba
)
 
=>
 
shibaState
.
shibaList
.
push
(
shiba
))

 
}

Enter fullscreen mode

Exit fullscreen mode

## Conclusion

The mutator pattern is much more intuitive than the actions, dispatch, and reducers pattern, but freedom makes it easier to create hard to troubleshoot bugs. It's hard not to view the actions, dispatch, and reducers pattern as the default - these examples even call their update methods actions. However, I've just touched the surface of both of these libraries. They're more flexible and much easier to get started with.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse