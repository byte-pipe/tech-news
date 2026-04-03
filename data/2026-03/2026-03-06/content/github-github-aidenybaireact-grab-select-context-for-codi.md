---
title: 'GitHub - aidenybai/react-grab: Select context for coding agents directly from your website · GitHub'
url: https://github.com/aidenybai/react-grab
site_name: github
content_file: github-github-aidenybaireact-grab-select-context-for-codi
fetched_at: '2026-03-06T11:12:23.909010'
original_url: https://github.com/aidenybai/react-grab
author: aidenybai
description: Select context for coding agents directly from your website - aidenybai/react-grab
---

aidenybai

 

/

react-grab

Public

* NotificationsYou must be signed in to change notification settings
* Fork262
* Star5.7k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

1,135 Commits
1,135 Commits
.changeset
.changeset
 
 
.github
.github
 
 
packages
packages
 
 
scripts
scripts
 
 
.cursorignore
.cursorignore
 
 
.gitignore
.gitignore
 
 
.oxfmtrc.json
.oxfmtrc.json
 
 
AGENTS.md
AGENTS.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
turbo.json
turbo.json
 
 
vercel.json
vercel.json
 
 
View all files

## Repository files navigation

# React Grab

Select context for coding agents directly from your website

How? Point at any element and press⌘C(Mac) orCtrl+C(Windows/Linux) to copy the file name, React component, and HTML source code.

It makes tools like Cursor, Claude Code, Copilot run up to3× fasterand more accurate.

### Try out a demo! →

## Install

Run this command at your project root (wherenext.config.tsorvite.config.tsis located):

npx -y grab@latest init

## Connect to MCP

npx -y grab@latest add mcp

## Usage

Once installed, hover over any UI element in your browser and press:

* ⌘C(Cmd+C) on Mac
* Ctrl+Con Windows/Linux

This copies the element's context (file name, React component, and HTML source code) to your clipboard ready to paste into your coding agent. For example:

<
a
 
class
=
"ml-auto inline-block text-sm"
 
href
=
"#"
>

 Forgot your password?

</
a
>

in
 
LoginForm
 
at
 
components
/
login
-
form
.
tsx
:
46
:
19

## Manual Installation

If you're using a React framework or build tool, view instructions below:

#### Next.js (App router)

Add this inside of yourapp/layout.tsx:

import
 
Script
 
from
 
"next/script"
;

export
 
default
 
function
 
RootLayout
(
{
 children 
}
)
 
{

 
return
 
(

 
<
html
>

 
<
head
>

 
{
process
.
env
.
NODE_ENV
 
===
 
"development"
 
&&
 
(

 
<
Script

 
src
=
"//unpkg.com/react-grab/dist/index.global.js"

 
crossOrigin
=
"anonymous"

 
strategy
=
"beforeInteractive"

 
/>

 
)
}

 
</
head
>

 
<
body
>
{
children
}
</
body
>

 
</
html
>

 
)
;

}

#### Next.js (Pages router)

Add this into yourpages/_document.tsx:

import
 
{
 
Html
,
 
Head
,
 
Main
,
 
NextScript
 
}
 
from
 
"next/document"
;

export
 
default
 
function
 
Document
(
)
 
{

 
return
 
(

 
<
Html
 
lang
=
"en"
>

 
<
Head
>

 
{
process
.
env
.
NODE_ENV
 
===
 
"development"
 
&&
 
(

 
<
Script

 
src
=
"//unpkg.com/react-grab/dist/index.global.js"

 
crossOrigin
=
"anonymous"

 
strategy
=
"beforeInteractive"

 
/>

 
)
}

 
</
Head
>

 
<
body
>

 
<
Main
 
/>

 
<
NextScript
 
/>

 
</
body
>

 
</
Html
>

 
)
;

}

#### Vite

Add this to yourindex.html:

<!doctype html
>

<
html
 
lang
="
en
"
>

 
<
head
>

 
<
script
 
type
="
module
"
>

 
if
 
(
import
.
meta
.
env
.
DEV
)
 
{

 
import
(
"react-grab"
)
;

 
}

 
</
script
>

 
</
head
>

 
<
body
>

 
<
div
 
id
="
root
"
>
</
div
>

 
<
script
 
type
="
module
" 
src
="
/src/main.tsx
"
>
</
script
>

 
</
body
>

</
html
>

#### Webpack

First, install React Grab:

npm install react-grab

Then add this at the top of your main entry file (e.g.,src/index.tsxorsrc/main.tsx):

if
 
(
process
.
env
.
NODE_ENV
 
===
 
"development"
)
 
{

 
import
(
"react-grab"
)
;

}

## Plugins

React Grab can be extended with plugins. A plugin can add context menu actions, toolbar menu items, lifecycle hooks, and theme overrides.

Register a plugin viawindow.__REACT_GRAB__:

window
.
__REACT_GRAB__
.
registerPlugin
(
{

 
name
: 
"my-plugin"
,

 
hooks
: 
{

 
onElementSelect
: 
(
element
)
 
=>
 
{

 
console
.
log
(
"Selected:"
,
 
element
.
tagName
)
;

 
}
,

 
}
,

}
)
;

In React, register inside auseEffectafter React Grab loads:

useEffect
(
(
)
 
=>
 
{

 
const
 
api
 
=
 
window
.
__REACT_GRAB__
;

 
if
 
(
!
api
)
 
return
;

 
api
.
registerPlugin
(
{

 
name
: 
"my-plugin"
,

 
actions
: 
[

 
{

 
id
: 
"my-action"
,

 
label
: 
"My Action"
,

 
shortcut
: 
"M"
,

 
onAction
: 
(
context
)
 
=>
 
{

 
console
.
log
(
"Action on:"
,
 
context
.
element
)
;

 
context
.
hideContextMenu
(
)
;

 
}
,

 
}
,

 
]
,

 
}
)
;

 
return
 
(
)
 
=>
 
api
.
unregisterPlugin
(
"my-plugin"
)
;

}
,
 
[
]
)
;

Actions use atargetfield to control where they appear. Omittarget(or set"context-menu") for the right-click menu, or set"toolbar"for the toolbar dropdown:

actions: 
[

 
{

 
id
: 
"inspect"
,

 
label
: 
"Inspect"
,

 
shortcut
: 
"I"
,

 
onAction
: 
(
ctx
)
 
=>
 
console
.
dir
(
ctx
.
element
)
,

 
}
,

 
{

 
id
: 
"toggle-freeze"
,

 
label
: 
"Freeze"
,

 
target
: 
"toolbar"
,

 
isActive
: 
(
)
 
=>
 
isFrozen
,

 
onAction
: 
(
)
 
=>
 
toggleFreeze
(
)
,

 
}
,

]
;

Seepackages/react-grab/src/types.tsfor the fullPlugin,PluginHooks, andPluginConfiginterfaces.

## Primitives

React Grab provides a set of primitives for building your own mini React Grab.

Here's a simple example of how to build your own element selector with hover highlight and one-click inspection:

npm install react-grab@latest

Then, put this in your React app:

import
 
{
 
useState
 
}
 
from
 
"react"
;

import
 
{
 
getElementContext
,
 
freeze
,
 
unfreeze
,
 
openFile
,
 
type
 
ReactGrabElementContext
 
}
 
from
 
"react-grab/primitives"
;

const
 
useElementSelector
 
=
 
(
onSelect
: 
(
context
: 
ReactGrabElementContext
)
 
=>
 
void
)
 
=>
 
{

 
const
 
[
isActive
,
 
setIsActive
]
 
=
 
useState
(
false
)
;

 
const
 
startSelecting
 
=
 
(
)
 
=>
 
{

 
setIsActive
(
true
)
;

 
const
 
highlightOverlay
 
=
 
document
.
createElement
(
"div"
)
;

 
Object
.
assign
(
highlightOverlay
.
style
,
 
{

 
position
: 
"fixed"
,

 
pointerEvents
: 
"none"
,

 
zIndex
: 
"999999"
,

 
border
: 
"2px solid #3b82f6"
,

 
transition
: 
"all 75ms ease-out"
,

 
display
: 
"none"
,

 
}
)
;

 
document
.
body
.
appendChild
(
highlightOverlay
)
;

 
const
 
handleMouseMove
 
=
 
(
{
 clientX
,
 clientY 
}
: 
MouseEvent
)
 
=>
 
{

 
highlightOverlay
.
style
.
display
 
=
 
"none"
;

 
const
 
target
 
=
 
document
.
elementFromPoint
(
clientX
,
 
clientY
)
;

 
if
 
(
!
target
)
 
return
;

 
const
 
{
 top
,
 left
,
 width
,
 height 
}
 
=
 
target
.
getBoundingClientRect
(
)
;

 
Object
.
assign
(
highlightOverlay
.
style
,
 
{

 
top
: 
`
${
top
}
px`
,

 
left
: 
`
${
left
}
px`
,

 
width
: 
`
${
width
}
px`
,

 
height
: 
`
${
height
}
px`
,

 
display
: 
"block"
,

 
}
)
;

 
}
;

 
const
 
handleClick
 
=
 
async
 
(
{
 clientX
,
 clientY 
}
: 
MouseEvent
)
 
=>
 
{

 
highlightOverlay
.
style
.
display
 
=
 
"none"
;

 
const
 
target
 
=
 
document
.
elementFromPoint
(
clientX
,
 
clientY
)
;

 
teardown
(
)
;

 
if
 
(
!
target
)
 
return
;

 
freeze
(
)
;

 
onSelect
(
await
 
getElementContext
(
target
)
)
;

 
unfreeze
(
)
;

 
}
;

 
const
 
teardown
 
=
 
(
)
 
=>
 
{

 
document
.
removeEventListener
(
"mousemove"
,
 
handleMouseMove
)
;

 
document
.
removeEventListener
(
"click"
,
 
handleClick
,
 
true
)
;

 
highlightOverlay
.
remove
(
)
;

 
setIsActive
(
false
)
;

 
}
;

 
document
.
addEventListener
(
"mousemove"
,
 
handleMouseMove
)
;

 
document
.
addEventListener
(
"click"
,
 
handleClick
,
 
true
)
;

 
}
;

 
return
 
{
 isActive
,
 startSelecting 
}
;

}
;

const
 
ElementSelector
 
=
 
(
)
 
=>
 
{

 
const
 
[
context
,
 
setContext
]
 
=
 
useState
<
ReactGrabElementContext
 
|
 
null
>
(
null
)
;

 
const
 
selector
 
=
 
useElementSelector
(
setContext
)
;

 
return
 
(

 
<
div
>

 
<
button
 
onClick
=
{
selector
.
startSelecting
}
 
disabled
=
{
selector
.
isActive
}
>

 
{
selector
.
isActive
 ? 
"Selecting…"
 : 
"Select Element"
}

 
</
button
>

 
{
context
 
&&
 
(

 
<
div
>

 
<
p
>
Component: 
{
context
.
componentName
}
</
p
>

 
<
p
>
Selector: 
{
context
.
selector
}
</
p
>

 
<
pre
>
{
context
.
stackString
}
</
pre
>

 
<
button

 
onClick
=
{
(
)
 
=>
 
{

 
const
 
frame
 
=
 
context
.
stack
[
0
]
;

 
if
 
(
frame
?.
fileName
)
 
openFile
(
frame
.
fileName
,
 
frame
.
lineNumber
)
;

 
}
}

 
>

 Open in Editor
 
</
button
>

 
</
div
>

 
)
}

 
</
div
>

 
)
;

}
;

Seepackages/react-grab/src/primitives.tsfor the fullReactGrabElementContext,getElementContext,freeze,unfreeze, andopenFileprimitives.

## Resources & Contributing Back

Want to try it out? Check outour demo.

Looking to contribute back? Check out theContributing Guide.

Want to talk to the community? Hop in ourDiscordand share your ideas and what you've built with React Grab.

Find a bug? Head over to ourissue trackerand we'll do our best to help. We love pull requests, too!

We expect all contributors to abide by the terms of ourCode of Conduct.

→ Start contributing on GitHub

### License

React Grab is MIT-licensed open-source software.

Thank you toAndrew Luetgersfor donating thegrabnpm package name.

## About

Select context for coding agents directly from your website

react-grab.com

### Topics

 react

 ai

 coding

 react-grab

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

5.7k

 stars
 

### Watchers

12

 watching
 

### Forks

262

 forks
 

 Report repository

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript97.6%
* CSS1.1%
* Other1.3%