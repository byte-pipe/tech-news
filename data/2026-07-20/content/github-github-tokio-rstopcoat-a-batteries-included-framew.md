---
title: 'GitHub - tokio-rs/topcoat: A batteries-included framework for building web apps · GitHub'
url: https://github.com/tokio-rs/topcoat
site_name: github
content_file: github-github-tokio-rstopcoat-a-batteries-included-framew
fetched_at: '2026-07-20T11:58:00.121607'
original_url: https://github.com/tokio-rs/topcoat
author: tokio-rs
description: A batteries-included framework for building web apps - tokio-rs/topcoat
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 tokio-rs

 

/

topcoat

Public

* NotificationsYou must be signed in to change notification settings
* Fork34
* Star1.3k

 
 
 
 
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

771 Commits
771 Commits
.cargo
.cargo
 
 
.github/
workflows
.github/
workflows
 
 
benchmarks
benchmarks
 
 
crates
crates
 
 
examples
examples
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
STYLE.md
STYLE.md
 
 
Topcoat.toml
Topcoat.toml
 
 
release-plz.toml
release-plz.toml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
View all files

## Repository files navigation

# Topcoat

### The full full-stack framework for Rust

Topcoat is a modular, batteries-included Rust framework for building fullstack apps. It prioritizes simplicity and productivity. SeeLearn Topcoatto get started, or theRoadmapfor what's coming next.

Early-stage and experimental. Expect breaking changes.

use
 topcoat
::
{

 
Result
,

 router
::
{
Router
,
 
RouterBuilderDiscoverExt
,
 page
}
,

 view
::
{
component
,
 view
}
,

}
;

#
[
tokio
::
main
]

async
 
fn
 
main
(
)
 
{

 topcoat
::
start
(
Router
::
builder
(
)
.
discover
(
)
.
build
(
)
)
.
await
.
unwrap
(
)
;

}

#
[
page
(
"/"
)
]

async
 
fn
 
home
(
)
 -> 
Result
 
{

 
view
!
 
{

 <!
DOCTYPE
 html>
 <html>
 <body>
 hello
(
name
:
 
"World"
)

 </body>
 </html>
 
}

}

#
[
component
]

async
 
fn
 
hello
(
name
:
 
&
str
)
 -> 
Result
 
{

 
view
!
 
{
 <h1>
"Hello, "
 
(
name
)
 
"!"
</h1> 
}

}

## What makes Topcoat different

### Client reactivity without the boilerplate

Topcoat renders all markup on the server: components can be async and query the database directly, eliminating all the traditional boilerplate needed for a separate API layer. Interactivity does not have to cost a round-trip, though. A$(...)expression is ordinary type-checked Rust that Topcoat evaluates on the server for the initial render and also translates to JavaScript, so it re-runs instantly in the browser. No wasm bundle, no client build step:

view
!
 
{

 signal open = 
false
;

 
// Runs entirely in the browser; no server round-trip.

 <button @click=$
(
|_e| open
.
set
(
!open
.
get
(
)
)
)
>
"What is Topcoat?"
</button>
 <p 
:
hidden=$
(
!open
.
get
(
)
)
>
"A fullstack Rust framework."
</p>

}

When an update does need the server, like fresh search results, mark the component as a#[shard]. Topcoat re-renders it on the server whenever one of its$(...)arguments changes and swaps the new HTML in place:

#
[
component
]

async
 
fn
 
search
(
)
 -> 
Result
 
{

 
view
!
 
{

 signal query = 
String
::
new
(
)
;

 <input @input=$
(
|e
:
 
Event
| query
.
set
(
e
.
target
.
value
)
)
>

 
// Updates as the user types.

 search_results
(
query
:
 $
(
query
.
get
(
)
)
)

 
}

}

#
[
shard
]

async
 
fn
 
search_results
(
cx
:
 
&
Cx
,
 
query
:
 
String
)
 -> 
Result
 
{

 
view
!
 
{

 <ul>
 
// Your own server-side code, like a database query:

 
for
 product in search_products
(
cx
,
 
&
query
)
.
await
? 
{

 <li>
(
product
.
name
)
</li>
 
}

 </ul>
 
}

}

### Powerful, unsurprising HTML templates

Theview!macro stays true to HTML and Rust. Use familiar Rust control flow as part of your templates:

view
!
 
{

 <nav>
 
for
 item in nav_items 
{

 <a
 href=
(
item
.
url
)

 
if
 item
.
url == current_path 
{

 aria-current=
"page"

 class=
"active"

 
}

 >
 
(
item
.
label
)

 </a>
 
}

 </nav>

}

Use thetopcoat fmtCLI command to automatically formatview!snippets (and other macros) across your codebase.

### Module-based routing

Topcoat can optionally infer your route tree from your app's module structure (without a build step):

src/
|-- app.rs -> / (and the root <html> layout)
`-- app/
 |-- about.rs -> /about
 |-- _marketing.rs (layout, no URL segment)
 |-- _marketing/
 | `-- pricing.rs -> /pricing
 |-- posts.rs -> /posts
 |-- posts/
 | `-- id.rs -> /posts/{post_id}
 `-- api/
 `-- health.rs -> GET /api/health

### Premade components you can edit

Topcoat UI is a component library based onTailwindinspired byshadcn/ui. Components are copied into your project via thetopcoat uiCLI command, meaning you can freely change their design and functionality to fit your use case:

#
[
component
]

async
 
fn
 
delete_card
(
)
 -> 
Result
 
{

 
view
!
 
{

 card
(

 card_header
(

 card_title
(
"Delete workspace"
)

 card_description
(

 
"This permanently removes the workspace and all of its data."

 
)

 
)

 card_footer
(

 attrs
:
 attributes! 
{
 class=
"justify-end"
 
}
,

 button
(
variant
:
 
ButtonVariant
::
Ghost
,
 
"Cancel"
)

 button
(
variant
:
 
ButtonVariant
::
Destructive
,
 
"Delete workspace"
)

 
)

 
)

 
}

}

### Asset bundling

The bundler scans your compiled binary forasset!calls, copies (or even downloads) every file into a local asset directory, and allows Topcoat to serve them efficiently with aggressive browser caching.

const
 
FERRIS
:
 
Asset
 = 
asset
!
(
"./ferris.png"
)
;

view
!
 
{
 <img src=
(
FERRIS
)
> 
}

Topcoat also ships with utilities for web fonts and icons, as well as easy integrations forFontsource(Google Fonts) andIconify.

### Built-in Tailwind support

Enabled thetailwindfeature to integrateTailwindinto your project effortlessly:

view
!
 
{
 <link rel=
"stylesheet"
 href=
(
topcoat
::
tailwind
::
stylesheet!
(
)
)
> 
}

## Learn Topcoat

Start here

* Getting started: create a new project, install the CLI, run the dev server.
* Source code formatting:topcoat fmtfor macro bodies.

Rendering

* Theview!macro: templating syntax, control flow, conditional attributes.
* The#[component]macro: async functions as components, with child content.
* Theattributes!macro: reusable runtime attribute fragments.
* Theclass!macro: space-separated class lists from static and conditional entries.

Routing

* Router: pages, layouts, and API routes; manual and auto-discovered.
* Module-based routing: derive the route table from your module tree.

Working with requests

* Request context (Cx): the value pages, layouts, and components read from.
* App context: share long-lived values across requests, keyed by type.
* Memoization:#[memoize]for per-request caching and fan-out dedup.
* Functions, not middlewares: the recommended way to model auth and other request-scoped concerns.
* Cookies: read and write the request cookie jar, with signed, encrypted, and prefixed cookies.
* Sessions: bring-your-own-storage session authentication: login/logout lifecycle, sliding expiration, and token rotation.

Asset system

* Assets: declare assets in Rust, serve them with content-hashed URLs.
* Fonts: bundle and serve web fonts.
* Icons: download Iconify icon sets or declare your own.

Client reactivity

* The runtime: signals,$(...)expressions,@event handlers, and:bind attributes.
* Expressions: the dual Rust/JavaScript expression language and its vocabulary.
* Procedures: async server functions callable from the browser.
* Shards: components that re-render on the server when their arguments change.

UI components

* Topcoat UI: premade components vendored into your project for you to edit.

Third-party integrations

* Tailwind: Tailwind CSS without Node, wired into the asset pipeline.
* htmx: drive partial HTML swaps from the server with request/response header helpers.

## Roadmap

Planned features we'd like to bring to Topcoat. Have an idea?Open an issue.

* topcoat newCLI command to bootstrap pre-configured projects
* Static export
* (More) reactivity (topcoat-runtime)
* More Topcoat UI components, full "blocks" e.g. sign-in form
* Emailing
* BetterToastyintegration (safely create/update records from forms without listing out all the fields)
* Validations
* OpenAPIendpoints
* Docs for how to deploy Topcoat
* Pre-rendering for static pages
* Streaming SSR / Suspense
* Client-side navigation + prefetching
* WebSockets
* Server-sent events
* Image optimization / resizing
* Easier-to-use middlewares like rate-limiting, compression, etc.
* Authentication
* Background jobs
* Islands

## About

A batteries-included framework for building web apps

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.3k

 stars
 

### Watchers

9

 watching
 

### Forks

34

 forks
 

 Report repository

 

## Releases

292

tags

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust94.9%
* TypeScript3.0%
* JavaScript1.1%
* Other1.0%