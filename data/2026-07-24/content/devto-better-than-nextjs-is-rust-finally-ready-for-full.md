---
title: Better than Next.js? Is Rust Finally Ready for Full-Stack Web Development? Introducing Topcoat - DEV Community
url: https://dev.to/francescoxx/better-than-nextjs-is-rust-finally-ready-for-full-stack-web-development-introducing-topcoat-2h09
site_name: devto
content_file: devto-better-than-nextjs-is-rust-finally-ready-for-full
fetched_at: '2026-07-24T11:34:58.177322'
original_url: https://dev.to/francescoxx/better-than-nextjs-is-rust-finally-ready-for-full-stack-web-development-introducing-topcoat-2h09
author: Francesco Ciulla
date: '2026-07-23'
description: There is a super-new Rust Web Framework in town, and it's name is Topcoat Rust is already a solid... Tagged with webdev, programming, rust, javascript.
tags: '#webdev, #programming, #rust, #javascript'
---

Creators discuss co-located auth and SSR caching

There is a super-new Rust Web Framework in town, and it's name is Topcoat

Rust is already a solid choice for backend development, especially with frameworks like Axum. But building a complete web application in Rust still means connecting many different libraries yourself. That is the problem Topcoat wants to solve.

Topcoat is a new batteries-included framework created by Carl Lerche and Julien Scholz for building full-stack, reactive web applications entirely in Rust.

Announcement:https://tokio.rs/blog/2026-07-22-announcing-topcoatGitHub:https://github.com/tokio-rs/topcoat

Prefer a video version? I discussed Topcoat directly with Carl Lerche, the creator of Tokio, and Julien Scholz, the creator of Topcoat.

### What is Topcoat?

Topcoat is fully server-rendered.

Your components can be asynchronous, access the database, load application state, and check user permissions directly on the server.

A minimal application looks like this:

#[tokio::main]

async
 
fn
 
main
()
 
{

 
topcoat
::
start
(
Router
::
builder
()
.discover
()
.build
())

 
.await

 
.unwrap
();

}

#[page(
"/"
)]

async
 
fn
 
home
()
 
->
 
Result
 
{

 
view!
 
{

 
<!
DOCTYPE
 
html
>

 
<
html
>

 
<
head
>

 
<
title
>
"Hello world"
</
title
>

 
topcoat
::
dev
::
script
()

 
</
head
>

 
<
body
>

 
<
h1
>
"Hello from Topcoat!"
</
h1
>

 
</
body
>

 
</
html
>

 
}

}

Enter fullscreen mode

Exit fullscreen mode

### Reactivity without WebAssembly

Frameworks like Leptos and Dioxus can run Rust in the browser through WebAssembly.

Topcoat takes a different route.

It renders the application on the server and adds client-side reactivity through small reactive instructions. It can also re-render parts of the UI on the server and replace only the section that changed.

The approach is closer to HTMX or Hotwire than to a traditional React-style SPA.

This makes Topcoat especially interesting for:

* Admin panels
* Internal tools
* Blogs and content platforms
* Online stores
* Data-heavy applications

For highly interactive browser applications, a client-heavy framework may still be a better fit.

### Is it replacing Axum?

No. Axum is still a great choice for APIs and lower-level HTTP endpoints.

Topcoat works at a higher level and tries to remove the boilerplate between routing, components, HTML rendering, assets, and reactive updates.

A project could easily use both.

### Why Topcoat matters

Rust already has many excellent libraries, but it has been missing a more opinionated, integrated experience similar to Rails, Laravel, or Next.js.

Topcoat is moving in that direction with:

* Server-rendered components
* An asset pipeline
* Tailwind-based UI components
* Fonts and icon integrations
* Request-level memoization
* Authentication close to the protected component
* Planned integration with the Toasty ORM

It is still early, and the team is open about the current limitations of its reactivity system.

Still, this feels like an important step for Rust web development.

Topcoat is not here to replace every existing framework. It is trying to make it much easier to build complete, server-rendered applications without leaving Rust.

Would you try it for your next internal tool or dashboard?

Watch the full discussion with Carl Lerche and Julien Scholz:

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse