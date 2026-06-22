---
title: Desktop apps | Deno Docs
url: https://docs.deno.com/runtime/desktop/
site_name: hackernews_api
content_file: hackernews_api-desktop-apps-deno-docs
fetched_at: '2026-06-22T13:05:24.072261'
original_url: https://docs.deno.com/runtime/desktop/
author: GeneralMaximus
date: '2026-06-22'
description: Build self-contained desktop applications from a Deno project, with framework auto-detection, hot reload, native windowing, auto-update, and cross-platform distribution.
tags:
- hackernews
- trending
---

On this page
* Why deno desktop
* Hello, desktop
* What's in this section

deno desktopturns a Deno project (anything from a single TypeScript file to a
Next.js app) into a self-contained desktop application. The output is a
redistributable binary that bundles your code, the Deno runtime, and a web
rendering engine into one bundle per platform.

Coming in Deno 2.9

deno desktopships in Deno v2.9.0 and is not in a stable release yet. To try
it now, rundeno upgrade canaryto install thecanarybuild. The command, configuration
keys, and TypeScript APIs may still change before the feature is stable.

## Whydeno desktopJump to heading#

Web technology is the most widely-known UI toolkit in the world. Desktop apps
built on web stacks (Electron, Tauri, Electrobun) take advantage of that, but
each has tradeoffs you have to live with: huge binaries, missing platform
support, no JavaScript ecosystem, no built-in update story, no framework
integration.

deno desktopis opinionated about those tradeoffs:

* Small by default, full Node compatibility.The default WebView backend
uses the operating system's own webview for small binaries, and you still have
the entire npm ecosystem available through Deno's Node compat layer. Opt into
the bundled Chromium (CEF) backend when you need identical rendering across
macOS, Windows, and Linux.
* Framework auto-detection.Pointdeno desktopat a Next.js, Astro, Fresh,
Remix, Nuxt, SvelteKit, SolidStart, TanStack Start, or Vite SSR project and it
runs: the production server in release mode, the dev server with hot reload
under--hmr. No code changes are required to take an existing web project to
the desktop.
* In-process bindings instead of IPC.Backend and UI communication goes
through in-process channels, not socket-based IPC. Values are still encoded as
they cross the call boundary, but there is no cross-process round-trip between
your Deno code and the webview.
* Cross-compile from one machine.The same machine can build for macOS,
Windows, and Linux. Backends are downloaded as needed, not built locally.
* Built-in binary-diff auto-update.Ship a singlelatest.jsonmanifest and
bsdiff patches; the runtime polls, applies, and rolls back automatically on
failed launches.

## Hello, desktopJump to heading#

Create a one-file desktop app:

main.ts
Deno
.
serve
(
(
)
 
=>

 
new
 
Response
(
"<h1>Hello, desktop</h1>"
,
 
{

 headers
:
 
{
 
"content-type"
:
 
"text/html"
 
}
,

 
}
)

)
;

>_
deno desktop main.ts

The compiled binary opens a window pointed at a local HTTP server bound to yourDeno.serve()handler. Run it directly:

>_
./main 
# macOS / Linux

.
\
main.exe 
# Windows

Deno.serve()automatically binds to the address the
webview navigates to, so you do not need to pass a port or hostname. SeeHTTP servingfor details.

## What's in this sectionJump to heading#

* Configuration: thedesktopblock indeno.json.
* Backends: CEF, webview, raw; how to choose.
* HTTP serving:Deno.serve()integration and the serving model.
* Frameworks: Next.js, Astro, Fresh, Remix,
Nuxt, SvelteKit, and others.
* Windows:Deno.BrowserWindowlifecycle, multiple
windows, events.
* Bindings: calling Deno code from the webview viabindings.<name>().
* Menus: application and context menus.
* Tray and dock: system status icons and the
macOS dock.
* Dialogs:prompt(),alert(),confirm()as
native popups.
* Notifications: native OS notifications via
the WebNotificationAPI.
* Hot module replacement:--hmrfor framework and
non-framework apps.
* DevTools: unified DevTools attached to both the
Deno runtime and the webview.
* Auto-update:Deno.autoUpdate(), manifests, bsdiff,
rollback.
* Error reporting: capturing uncaught
exceptions and panics.
* Distribution: cross-compilation, output
formats, installers.
* Comparison: howdeno desktoprelates to
Electron, Tauri, Electrobun, Dioxus.
* deno desktopCLI reference: the command,
its flags, and thedeno.jsondesktopschema.

Last updated onJune 17, 2026

## Did you find what you needed?

Yes
No
Edit this page

What can we do to improve this page?

0 / 2000

GitHub username (
optional
)

If provided, you'll be @mentioned in the created GitHub issue

Send us feedback
Privacy policy