---
title: What Happens When You Run `npm run dev` - DEV Community
url: https://dev.to/lovestaco/what-happens-when-you-run-npm-run-dev-ae9
site_name: devto
content_file: devto-what-happens-when-you-run-npm-run-dev-dev-communit
fetched_at: '2026-05-21T12:05:49.554104'
original_url: https://dev.to/lovestaco/what-happens-when-you-run-npm-run-dev-ae9
author: Athreya aka Maneshwar
date: '2026-05-19'
description: Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is... Tagged with webdev, programming, javascript, beginners.
tags: '#webdev, #programming, #javascript, #beginners'
---

Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is free and source-available on Github.Star git-lrcto help devs discover the project. Do give it a try and share your feedback for improving the project.

You've runnpm run devapproximately 1,000 times in your life.

You've watched the terminal blink.

You've switched to the browser.

Magic happened.

But do you actually know what's going on? Like,reallyknow?

Today we go all the way down the hole understanding shell, process spawning, module graphs, Hot Module Replacement, React Fast Refresh.

## Step 0: You press Enter

npm run dev

Enter fullscreen mode

Exit fullscreen mode

Your shell looks upnpmin yourPATHand finds it — often inside whatever directorynvminstalled Node into, or at a system path like/usr/local/bin/npm. It hands control to the npm CLI, which is itself just a Node.js script.

npm then does one thing: reads yourpackage.json.

{

 
"scripts"
:
 
{

 
"dev"
:
 
"vite"

 
}

}

Enter fullscreen mode

Exit fullscreen mode

It finds"dev": "vite"and prepares to run it.

## Step 1: npm spawns a child process

npm temporarily adds./node_modules/.binto yourPATH, then spawns a child process running thedevcommand.

So"vite"resolves to./node_modules/.bin/vite, which is a symlink to the actual Vite binary insidenode_modules/vite/bin/vite.js.

No magic.It's just Node running a JS file.

## Step 2: Vite boots up

Vitereads yourvite.config.js(or.ts), registers plugins, and does something really clever before anything is served.

### The esbuild pre-bundling trick

Vite usesesbuildwritten in Go, absurdly fast to pre-process yournode_modulesdependencies.

It does two things:

1. Converts CommonJS to ESM.Browsers can't natively loadrequire(). esbuild rewrites it.
2. Collapses packages with many internal files into one.lodashhas 600+ tiny files. esbuild merges them so the browser makes one request, not 600.

The result is cached in.vite/deps/. Touchnode_modules? Cache busts.Otherwise it skips this step entirely on restart.

## Step 3: The dev server is just... an HTTP server

Vite starts a plain Node.js HTTP server onlocalhost:5173.

No webpack dev server magic, no complex middleware chains.

When the browser requests a file, Vite:

1. Reads it from disk
2. Transforms it on-the-fly (JSX → JS, TypeScript → JS,.css→ injected<style>)
3. Serves it as a nativeES Module

The browser itself handles module resolution using<script type="module">.

The key insight:Vite doesn't bundle your source code in dev mode at all.

The browser fetches each file individually as an ES module.

This is why Vite's dev startup is near-instant regardless of your project size it only processes what the browser actually asks for.

Each arrow is a real HTTP request. The browser is doing the graph traversal for you.

## Step 4: The module graph

As files are requested, Vite builds an internalmodule dependency grapha map of who imports what.

This graph is lazy, only nodes that get requested exist in it.

If you never navigate to a route, those components are never fetched, never in the graph.

This is the structure that makes HMR fast.

When a file changes, Vite doesn't scan all your code.

It just walks this graph.

## Step 5: You save a file — here's where it gets interesting

### 5a. OS notifies Vite immediately

Vite useschokidarwhich wraps OS-native file system events:

OS

API

Mechanism

Linux

inotify

Kernel watches inodes directly

macOS

FSEvents

Core Services file-system event API

Windows

ReadDirectoryChangesW

Win32 API

Zero polling. The OS taps Vite on the shoulder the moment your editor flushes to disk.

### 5b. Walk the graph, find the HMR boundary

Vite walksupthe module graph from the changed file, looking for the first ancestor that has registered an HMR handler viaimport.meta.hot.accept().

With React, you never writeimport.meta.hot.accept()yourself.

The@vitejs/plugin-reactplugin (which usesReact Fast Refresh)automatically injectsthis into every component file at transform time. It's invisible to you.

If no boundary is found all the way up tomain.jsxfull page reload.

You'll see this happen when you editvite.config.jsor a non-component JS utility that isn't HMR-aware.

### 5c. Server re-transforms only the changed file

Vite re-runs justButton.jsxthrough its plugin pipeline JSX transform, any Babel plugins, etc.

The result is a fresh ES module in memory.

### 5d. Browser fetches the new module via dynamic import

The HMR client (a small script Vite injects into your page) is told an update is available and calls:

import
(
'
/components/Button.jsx?t=1718023456789
'
)

Enter fullscreen mode

Exit fullscreen mode

The?t=timestampquery param is the cache-buster. The browser sees a URL it hasn't fetched before, makes a real HTTP request, gets the new module.

### 5e. The module swap —hot.disposeandhot.accept

Vite's HMR runtime is built around two functions you (or, with React, the plugin) register onimport.meta.hot:

// In a module that wants to handle its own updates:

// Clean up before this module is replaced —

// cancel timers, unsubscribe, remove listeners.

import
.
meta
.
hot
.
dispose
((
data
)
 
=>
 
{

 
clearInterval
(
timer
)

})

// Receive the freshly imported module and re-wire things.

import
.
meta
.
hot
.
accept
((
newModule
)
 
=>
 
{

 
// newModule is the updated exports

})

Enter fullscreen mode

Exit fullscreen mode

A subtle but important detail: Vite's HMR doesn't literally swap theoriginalimported module object for everyone up the chain.

The accepting module i.e the HMR boundary is responsible for taking the new exports and applying them.

That simplified model is what lets Vite skip the expensive work of rewriting every importer, and it's enough for almost every real dev scenario.

disposeis where you cancel asetInterval, unsubscribe from a store, or remove an event listener, anything that would leak if the old module just got abandoned.

Note on CSS:stylesheets take a slightly different path. When a.cssfile changes, Vite doesn't dynamically re-import a JS module, it swaps the<link>(or<style>) tag for the updated stylesheet, which avoids a flash of unstyled content.

## Step 6: React Fast Refresh does the actual re-render

React Fast Refresh is a separate system built by the React team. When the new component module lands, it:

1. Compares hook signatures.IfButtonhaduseState, useEffectbefore and still hasuseState, useEffectafter, state is preserved. Add or remove a hook? State resets for that component only.
2. Finds all live instancesin the React fiber tree.
3. Surgically re-rendersonly the affected subtree. Parent components don't re-render. Siblings don't re-render. Just the changed component and its children.

This is why you can edit a component's styling while a form is mid-fill and the form doesn't reset. The form state lives in a parent or sibling — Fast Refresh never touched it.

## The full picture

## Why does this matter?

If you're on webpack's dev server, a file save triggers a rebuild of the bundle, even with HMR. On a mid-size project that can mean noticeable latency between save and browser update.

With Vite's native-ESM approach, the server does almost nothing (one file transform), the browser fetches one URL, and Fast Refresh touches one subtree.

The entire round trip is typically very fast and stays fast as your project grows.

That's not a marginal improvement.

It fundamentally changes how you work — edit → see result becomes nearly instantaneous.

AI agents write code fast. They also silently remove logic, change behavior, and introduce bugs -- without telling you. You often find out in production.

git-lrc fixes this. It hooks into git commit and reviews every diff before it lands. 60-second setup. Completely free.*

Any feedback or contributors are welcome! It's online, source-available, and ready for anyone to use.

⭐ Star it on GitHub:

## HexmosTech/git-lrc

### Free, Micro AI Code Reviews That Run on Commit

|🇩🇰 Dansk|🇪🇸 Español|🇮🇷 Farsi|🇫🇮 Suomi|🇯🇵 日本語|🇳🇴 Norsk|🇵🇹 Português|🇷🇺 Русский|🇦🇱 Shqip|🇨🇳 中文|

# git-lrc

## Free, Micro AI Code Reviews That Run on Commit

 

 
 
 
 
 
 

AI agents write code fast. They alsosilently remove logic, change behavior, and introduce bugs -- without telling you. You often find out in production.

git-lrcfixes this.It hooks intogit commitand reviews every diffbeforeit lands. 60-second setup. Completely free.

## See It In Action

See git-lrc catch serious security issues such as leaked credentials, expensive cloud
operations, and sensitive material in log statements

git-lrc-intro-60s.mp4

## Why

* 🤖AI agents silently break things.Code removed. Logic changed. Edge cases gone. You won't notice until production.
* 🔍Catch it before it ships.AI-powered inline comments show youexactlywhat changed and what looks wrong.
* 🔁Build a…

View on GitHub

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse