---
title: Single-file HTML apps | Hyperclay
url: https://hyperclay.com/
site_name: hackernews_api
fetched_at: '2025-08-19T10:02:32.408073'
original_url: https://hyperclay.com/
author: pil0u
date: '2025-08-18'
description: A single HTML file is all you need to build a web app. Hyperclay hosts these HTML files so you can create personal, malleable software easily.
tags:
- hackernews
- trending
---

docs

get started

start

login

# Experience the Zen of making, hosting, and sharing great software in a single, portable, self-updating, vanilla HTML file

Build web apps like you're sculpting clay, not managing infrastructure.

Modern web development forces you through layers of abstraction: config files, build steps, magic frameworks, deployment pipelines.

Hyperclay returns to a simpler model: your app is a single HTML file you (and your clients) manipulate directly. Edit the file through its visual UI and it persists its own state.

What if web apps were as simple to edit as documents? Hyperclay makes it possible: UI, logic, and data live in one self-modifying HTML file. Edit it live. Share it instantly. Download and use it locally.

It's Google Docs for interactive code.Shareable, portable, malleable apps, but you fully control the document, what it looks like, and how it's edited.

* Direct Manipulation:Edit your app while it's running. No compile step, no refresh needed. Changes happen instantly, like editing a document. Share a URL and users see your updated page.
* What you see is what you build:The UI is the app itself. When you modify the interface or edit the source in DevTools, you're directly changing the application. There's no abstraction layer.
* True Portability:Export your app as an HTML file that runs anywhere: offline, on any server, forever. Version control tracks every save, protecting you from irreversible mistakes.

The coolest part? It's just an HTML file. Nothing special. Change it, it serializes its DOM, and sends it to a/saveendpoint. Nothing magic about it.

The tech: Hyperclay is a NodeJS server and frontend JS library that allows HTML pages to update their DOM and then replace their own .html source with the updated version.

Imagine clicking a checkbox, which adds the `checked` attribute to its element, then using Hyperclay to globally persist this version of `document.body.outerHTML`, so that it's there next time someone visits the page. There's automatic versioning and read/write permissioning.

I build several dozen websites a year

When I’m in flow, coding a website feels like writing a story

But it’s better than a story, because I can interact with it as I’m coding

Most of the things I build transform some data into a more useful format

For example,

Static websites are the obvious place to host these simple tools

But static websites fall short in one annoying way: changes to them are ephemeral

This is frustrating because the problems I want to help solve are not ephemeral

With physical objects, ephemerality is shocking — changes are supposed to persist

But there's no obvious digital counterpart to physical objects

Static websites are great, but changes users make to them reset

To get digital objects to act more intuitively, we need to build a whole persistence layer around them

In practice, this means a server with a database, API, templates, and user accounts

That’s a lot of effort to mimic what we take for granted with physical objects

This is frustrating because I want to focus on making the actual thing, not the persistence layer

I'm like a writer who wants to create experiences for readers, but I have to keep fixing typewriters

It would be a great to ignore all the noise of modern web dev and just build the experience I want

What I need is a primitive concept that's so obvious it feels like a single, shapeable object

Let’s take an example: a personal dev log I can update over time

There’s a surprising amount of work in getting this simple digital object online

Updating it can be a cumbersome process too, when it should be natural and instant

The best workflow I can imagine is the ease-of-use of a local desktop app you open and edit, but its changes are persisted online

If only my UI had the power to permanently update itself

When I’m done updating it, people can view it

It would be a better digital object: malleable, shareable, cloneable, persistent

Think about how many digital objects are designed specifically for this workflow:

This is the lifecycle of:

1. Website builders
2. Docs, spreadsheets, presentations
3. Multimedia editors
4. Business dashboards
5. Blogging platforms
6. Work management tools
7. Survey, poll, quiz builders
8. Knowledge base builders
9. Mind mapping tools
10. Invoice generators
11. Data visualization tools
12. Financial modeling apps
13. Creative asset generators
14. Interactive course builders
15. Project brief generators
16. Resume builders
17. Wireframing tools
18. Product roadmap makers
19. Etc etc etc

What kind of thing could encapsulate this workflow in a single, small package?

Of course! Most web apps already use HTML, with a few extra steps in the middle

What if we cut out the middle steps?

We’d be left with a simple, easy-to-think-about stack:

HTML becomes the all-in-one database / API / UI, flattening all levels of the stack into one layer






































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































It's a lot less to worry about:

We’d get a full web app with the same amount of code that a static website requires

It’s easy to think about!

It's a new primitive: a single, shapeable object

IntroducingHyperclay, a place to host self-modifying HTML files(e.g. HTML apps)

Hyperclay gobbles up ordinary HTML pages and makes it so changes made to them persist

Here’s how simple your online, editable, shareable journaling app could be:

<
div
 contenteditable
>
My new blog!
</
div
>

Or you could build a way to track the extra hours you worked this week:

<
h1
>
Extra Hours
</
h1
>

<
input
 type
=
"checkbox"
 persist
>

<
input
 type
=
"checkbox"
 persist
>

<
input
 type
=
"checkbox"
 persist
>

(
persist
 writes the
checked
 attribute to the DOM)

For something more complex, see my personal dev log:

(To persist changes,request accessto Hyperclay)

HTML apps unify UI, state, and behavior into one concept

But best of all, shaping these HTML documents feels like shaping something real, like a physical object

Not in the mood to go down endless rabbit holes just to build a simple idea?

Hi, I’m David, I’d love to introduce you to a lightweight way to web app.

Introducing Hyperclay:

HTML APPS

hyperclay newsletter

subscribe

© 2025 Hyperspace Systems LLC

Terms

Privacy

Pricing

Changelog

Docs

@panphora on X
