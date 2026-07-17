---
title: 'GitHub - vercel-labs/native: Toolkit for building native desktop apps · GitHub'
url: https://github.com/vercel-labs/native
site_name: github
content_file: github-github-vercel-labsnative-toolkit-for-building-nati
fetched_at: '2026-07-17T11:31:45.294908'
original_url: https://github.com/vercel-labs/native
author: vercel-labs
description: Toolkit for building native desktop apps. Contribute to vercel-labs/native development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 vercel-labs

 

/

native

Public

* NotificationsYou must be signed in to change notification settings
* Fork262
* Star6.4k

 
 
 
 
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

274 Commits
274 Commits
.github
.github
 
 
assets
assets
 
 
build
build
 
 
changelog.d
changelog.d
 
 
docs
docs
 
 
editors/
native-markup
editors/
native-markup
 
 
evals
evals
 
 
examples
examples
 
 
packages
packages
 
 
scripts
scripts
 
 
skill-data
skill-data
 
 
skills/
native-sdk
skills/
native-sdk
 
 
src
src
 
 
tests
tests
 
 
third_party
third_party
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
RELEASING.md
RELEASING.md
 
 
app.zon
app.zon
 
 
build.zig
build.zig
 
 
build.zig.zon
build.zig.zon
 
 
View all files

## Repository files navigation

# Native SDK

Native SDK is the complete toolkit for building native desktop applications.

Native SDK exists because expressive UI and native performance should not be competing goals. Developers often choose web-based runtimes because they offer freedom, speed and control over the product experience. But that freedom often comes with a heavy runtime. Native SDK keeps the expressive authoring model and replaces the runtime with native rendering.

Views are declarative markup in.nativefiles, logic is plain TypeScript compiled to native code at build time — or Zig, first-class by choice — and Native SDK's own engine draws every pixel into real OS windows. No browser, no WebView, no JS runtime in the binary: Zig is how everything works, TypeScript and Native markup are how apps are authored.

Soundboard, Notes, and Calculator fromexamples/— every pixel drawn by the Native SDK engine, captured through its deterministic reference renderer. The images follow your color scheme.

## Quick start

Install the CLI:

npm install -g @native-sdk/cli

Create and run an app:

native init my_app

cd
 my_app
native dev

A native window opens with a working counter. The whole app is three files of truth — view, logic, manifest — and no build config. The view issrc/app.native, a markup file that binds values and dispatches messages (the counter row at its heart):

<
row
 
gap
="
8
" 
main
="
center
" 
cross
="
center
" 
grow
="
1
"
>

 
<
button
 
variant
="
secondary
" 
on-press
="
decrement
"
>
-
</
button
>

 
<
text
>
{count}
</
text
>

 
<
button
 
variant
="
primary
" 
on-press
="
increment
"
>
+
</
button
>

</
row
>

All logic lives insrc/core.ts: aModelinterface, aMsgunion, and one pureupdatefunction — the only place state changes, plain TypeScript compiled to native code at build time:

export
 
function
 
update
(
model
: 
Model
,
 
msg
: 
Msg
)
: 
Model
 
{

 
switch
 
(
msg
.
kind
)
 
{

 
case
 
"increment"
:
 
return
 
{
 ...
model
,
 
count
: 
model
.
count
 
+
 
1
 
}
;

 
case
 
"decrement"
:
 
return
 
{
 ...
model
,
 
count
: 
model
.
count
 
-
 
1
 
}
;

 
case
 
"reset"
:
 
return
 
{
 ...
model
,
 
count
: 
0
 
}
;

 
}

}

Prefer Zig for the core?native init my_app --template zig-corescaffolds the same app withsrc/main.zig— same loop, same runtime, first-class by choice.

Editsrc/app.nativewhilenative devruns and the window updates in place, keeping your state.native dev --coreruns the TypeScript core under node for instant logic checks,native checkvalidates the core and every view in milliseconds without building, andnative buildproduces an optimized release binary.

Read the full guide atnative-sdk.dev/quick-start.

## What you get

Beautiful by default— Great software should not start from a blank slate. The built-in component catalog — buttons, tabs, text fields, dialogs, charts, virtual lists, and more — ships with considered typography, spacing, and color, so the appnative initscaffolds already looks intentional the first time its window opens.

Customizable by design— Your app should have its own identity, not ours. Styling is design tokens end to end: color, radius, and typography resolve by name, re-resolve live when the theme changes, and can be replaced wholesale —examples/soundboardandexamples/deckare the same music player separated only by tokens and a chrome pass.

Native from the start— Every interface is rendered without a browser or WebView. The engine draws into real OS windows while scroll physics, menus, dialogs, the tray, and text input stay with the operating system, and markup compiles into the executable at build time, so a release build carries no parser or interpreter — the scaffolded counter app builds to a single binary a few megabytes small.

Predictable state— State changes should be explicit, inspectable and easy to reason about. Events produce messages, messages update state, and state renders the interface; markup can bind and dispatch but never mutate. The loop is so deterministic thatnative automate recordjournals a session andreplayreproduces it headlessly, verified frame by frame against state fingerprints.

Simple authoring— Interfaces should be easy to read, easy to write and easy to generate. Views are elements, flex layout,{bindings}, and expressions likeselected="{f == filter}", andnative checkvalidates every view against your app's actualModelandMsg— bindings, iterables, message tags — in milliseconds, withfile:line:columnerrors that teach.

AI is part of the workflow— Native SDK is designed for a world where humans and AI agents build software together. Every app embeds an automation server, so any agent can read accessibility snapshots, drive widgets, assert on live state, and take deterministic screenshots of the running window; accessibility findings are machine-checked innative check; and the CLI ships the agent skills that teach all of it (native skills list).

## Examples

The apps pictured above live inexamples/, most as zero-config projects —app.zonplussrc/, no build files — run straight from their directory withnative dev.

Example

What it shows

calculator

A complete small app: markup keypad, keyboard input, chrome shortcuts, theming.

notes

Persistence through the effects channel: debounced writes, restore on boot, dialogs, search.

soundboard

Album grid with decoded cover art, context menus, timers, and a custom theme.

deck

The soundboard player rebuilt as a dense hardware chassis: two windows, same widgets, different tokens.

feed

A 100,000-row list, virtualized with runtime-owned scrolling.

The full catalog inexamples/README.mdalso covers guarded OS capabilities, GPU surfaces, WebView composition, web-frontend shells, and the iOS/Android embed hosts.

## Platforms

macOS is the primary development platform and carries the deepest support: Metal presentation, OS scroll physics, native context menus, app menus, tray, and dialogs. Linux runs the full showcase through the deterministic software renderer in real windows, with pointer, keyboard, scroll, IME composition, and HiDPI; Windows runs on a Win32 host with IME composition and is exercised in CI, including real input injection. Mobile support is experimental: iOS is simulator-proven through the embed library and Android cross-compiles with the full embed ABI, but APIs and tooling on both are still evolving — desktop is the mature surface. WebView surfaces coexist on every desktop platform. Theplatform support matrixdocuments exactly what each host supports today.

## Documentation

The full documentation is atnative-sdk.dev.

* Quick Start— install to a running, tested app
* Philosophy— the six principles behind the toolkit
* App Model— the model/message/update loop, wiring, and hot reload
* TypeScript Cores— the app-core subset, effects, subscriptions, and the node dev loop
* Native UI— every element, attribute, and pattern in the markup
* Components— the component catalog
* State & Data Flow— derive-don't-store, bindings, and text editing
* Testing— full-loop UI tests, headless on any machine
* Automation— snapshots, widget driving, record/replay, screenshots
* Capabilities— guarded OS services: notifications, clipboard, dialogs, credentials
* Packaging— from binary to distributable app
* Platform Support— what each host supports today

## Contributing

Native SDK is pre-1.0: APIs still move, and the toolkit is evolving quickly. Bug reports and focused pull requests are welcome — for larger changes, open an issue first so the design can be discussed. SeeCONTRIBUTING.mdfor the development setup and local checks.

## License

Apache-2.0

## About

Toolkit for building native desktop apps

native-sdk.dev

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

6.4k

 stars
 

### Watchers

20

 watching
 

### Forks

262

 forks
 

 Report repository

 

## Releases21

v0.5.2

 Latest

 

Jul 17, 2026

 

+ 20 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Zig78.3%
* TypeScript9.7%
* Objective-C4.8%
* C2.5%
* C++2.1%
* Objective-C++1.0%
* Other1.6%