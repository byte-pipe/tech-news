---
title: 'GitHub - DioxusLabs/dioxus: Fullstack app framework for web, desktop, and mobile. · GitHub'
url: https://github.com/DioxusLabs/dioxus
site_name: github
content_file: github-github-dioxuslabsdioxus-fullstack-app-framework-fo
fetched_at: '2026-07-21T11:37:18.763057'
original_url: https://github.com/DioxusLabs/dioxus
author: DioxusLabs
description: Fullstack app framework for web, desktop, and mobile. - DioxusLabs/dioxus
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 DioxusLabs

 

/

dioxus

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.8k
* Star37.4k

 
 
 
 
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

7,170 Commits
7,170 Commits
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.vscode
.vscode
 
 
.zed
.zed
 
 
examples
examples
 
 
notes
notes
 
 
packages
packages
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE-APACHE
LICENSE-APACHE
 
 
LICENSE-MIT
LICENSE-MIT
 
 
README.md
README.md
 
 
_typos.toml
_typos.toml
 
 
codecov.yml
codecov.yml
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
lychee.toml
lychee.toml
 
 
View all files

## Repository files navigation

### Website|Examples|Tutorial|中文|PT-BR|日本語|Türkçe|한국어

Build for web, desktop, and mobile, and more with a single codebase. Zero-config setup, integrated hot-reloading, and signals-based state management. Add backend functionality with Server Functions and bundle with our CLI.

fn
 
app
(
)
 -> 
Element
 
{

 
let
 
mut
 count = 
use_signal
(
|| 
0
)
;

 
rsx
!
 
{

 h1 
{
 
"High-Five counter: {count}"
 
}

 button 
{
 onclick
:
 move |_| count += 
1
,
 
"Up high!"
 
}

 button 
{
 onclick
:
 move |_| count -= 
1
,
 
"Down low!"
 
}

 
}

}

## ⭐️ Unique features:

* Cross-platform apps in three lines of code (web, desktop, mobile, server, and more)
* Ergonomic state managementcombines the best of React, Solid, and Svelte
* Built-in featureful, type-safe, fullstack web framework
* Integrated bundler for deploying to the web, macOS, Linux, and Windows
* Subsecond Rust hot-patching and asset hot-reloading
* And more!Take a tour of Dioxus.

## Instant hot-reloading

With one command,dx serveand your app is running. Edit your markup, styles, and see changes in milliseconds. Use our experimentaldx serve --hotpatchto update Rust code in real time.

## Build Beautiful Apps

Dioxus apps are styled with HTML and CSS. Use the built-in TailwindCSS support or load your favorite CSS library. Easily call into native code (objective-c, JNI, Web-Sys) for a perfect native touch.

## Truly fullstack applications

Dioxus deeply integrates withaxumto provide powerful fullstack capabilities for both clients and servers. Pick from a wide array of built-in batteries like WebSockets, SSE, Streaming, File Upload/Download, Server-Side-Rendering, Forms, Middleware, and Hot-Reload, or go fully custom and integrate your existing axum backend.

## Experimental Native Renderer

Render using web-sys, webview, server-side-rendering, liveview, or even with our experimental WGPU-based renderer. Embed Dioxus in Bevy, WGPU, or even run on embedded Linux!

## First-party primitive components

Get started quickly with a complete set of primitives modeled after shadcn/ui and Radix-Primitives.

## First-class Android and iOS support

Dioxus is the fastest way to build native mobile apps with Rust. Simply rundx serve --platform androidand your app is running in an emulator or on device in seconds. Call directly into JNI and Native APIs.

## Bundle for web, desktop, and mobile

Simply rundx bundleand your app will be built and bundled with maximization optimizations. On the web, take advantage of.avifgeneration,.wasmcompression, minification, and more. Build WebApps weighingless than 50kband desktop/mobile apps less than 5mb.

## Fantastic documentation

We've put a ton of effort into building clean, readable, and comprehensive documentation. All html elements and listeners are documented with MDN docs, and our Docs runs continuous integration with Dioxus itself to ensure that the docs are always up to date. Check out theDioxus websitefor guides, references, recipes, and more. Fun fact: we use the Dioxus website as a testbed for new Dioxus features -check it out!

## Community

Dioxus is a community-driven project, with a very activeDiscordandGitHubcommunity. We're always looking for help, and we're happy to answer questions and help you get started.Our SDKis community-run and we even have aGitHub organizationfor the best Dioxus crates that receive free upgrades and support.

## Full-time core team

Dioxus has grown from a side project to a small team of fulltime engineers. Thanks to the generous support of FutureWei, Satellite.im, the GitHub Accelerator program, we're able to work on Dioxus full-time. Our long term goal is for Dioxus to become self-sustaining by providing paid high-quality enterprise tools. If your company is interested in adopting Dioxus and would like to work with us, please reach out!

## Supported Platforms

Web

* Render directly to the DOM using WebAssembly
* Pre-render with SSR and rehydrate on the client
* Simple "hello world" at about 50kb, comparable to React
* Built-in dev server and hot reloading for quick iteration

Desktop

* Render using Webview or - experimentally - with WGPU orFreya(Skia)
* Zero-config setup. Simply `cargo run` or `dx serve` to build your app
* Full support for native system access without IPC
* Supports macOS, Linux, and Windows. Portable <3mb binaries

Mobile

* Render using Webview or - experimentally - with WGPU or Skia
* Build .ipa and .apk files for iOS and Android
* Call directly into Java and Objective-C with minimal overhead
* From "hello world" to running on device in seconds

Server-side Rendering

* Suspense, hydration, and server-side rendering
* Quickly drop in backend functionality with server functions
* Extractors, middleware, and routing integrations
* Static-site generation and incremental regeneration

## Running the examples

The examples in the main branch of this repository target the git version of dioxus and the CLI. If you are looking for examples that work with the latest stable release of dioxus, check out the0.6 branch.

The examples in the top level of this repository can be run with:

cargo run --example 
<
example
>

However, we encourage you to download the dioxus-cli to test out features like hot-reloading. To install the most recent binary CLI, you can use cargo binstall.

curl -fsSL https://dioxuslabs.com/install.sh 
|
 bash

If this CLI is out-of-date, you can install it directly from git or cargo-binstall

cargo install --git https://github.com/DioxusLabs/dioxus dioxus-cli --locked

With the CLI, you can also run examples with the web platform. You will need to disable the default desktop feature and enable the web feature with this command:

dx serve --example 
<
example
>
 --platform web -- --no-default-features

## Contributing

* Check out the websitesection on contributing.
* Report issues on ourissue tracker.
* Jointhe discord and ask questions!

## License

This project is licensed under either theMIT licenseor theApache-2 License.

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in Dioxus by you, shall be licensed as MIT or Apache-2, without any additional
terms or conditions.

## About

Fullstack app framework for web, desktop, and mobile.

dioxuslabs.com

### Topics

 react

 css

 android

 html

 rust

 ios

 ui

 web

 native

 ssr

 wasm

 desktop

 virtualdom

### Resources

 Readme

 

### License

 Apache-2.0, MIT licenses found
 

### Licenses found

Apache-2.0

LICENSE-APACHE

 

MIT

LICENSE-MIT

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

37.4k

 stars
 

### Watchers

188

 watching
 

### Forks

1.8k

 forks
 

 Report repository

 

## Releases40

v0.7.9

 Latest

 

May 8, 2026

 

+ 39 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* opencollective.com/dioxus-labs

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust93.1%
* HTML2.1%
* R1.9%
* JavaScript1.2%
* TypeScript1.1%
* Makefile0.2%
* Other0.4%