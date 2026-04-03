---
title: The time is right for a DOM templating API
url: https://justinfagnani.com/2025/06/26/the-time-is-right-for-a-dom-templating-api/
site_name: hackernews
fetched_at: '2025-06-28T07:04:47.473259'
original_url: https://justinfagnani.com/2025/06/26/the-time-is-right-for-a-dom-templating-api/
author: mdhb
date: '2025-06-28'
---

TL;DR: I want to propose addinga declarative templating APIto the web platform. Here's why...

The web platform is the most successful application runtime of all time. While the largest reason for this is the web's reach, it wouldn't be possible without the DOM API, which turns a mostly static document viewer into a highly dynamic and expressive runtime.

For as much hate as the DOM sometimes receives (some of that deserved, but some really not!) the DOM is undeniably a very powerful API. This is easily shown by all the amazing and highly dynamic web applications out there - even an app as complex as Photoshop is available as a web app, and its entire UI is built with web components!

Yet the DOM is missing one of the most important and popular features in modern web development: templating. Currently there is no ergonomic way in the standard DOM APIs to create a chunk of DOM nodes, from data, event listeners added, properties set on elements, safe against XSS attacks; and then to efficiently update that chunk with new data.

This kind of templating is the cornerstone of all modern web frameworks and rendering libraries these days, all of which let you declaratively combine markup with data. This includes React, Vue, Angular, Preact, Lit, Svelte, SolidJS, Stencil, Quik, Ember, FAST, Polymer, Marko, and just about every other framework out there.

The reasons that declarative templating are so popular and foundational may be obvious, but let's recount them anyway:

* The ergonomics are far superior to imperative DOM APIs. Declarative interpolation - plus features that go beyond plain HTML, like event listeners and property setting - help preserve the locality of behavior, making templates much easier to write and read than imperative code.
* It's easier to be secure against XSS attacks, since templates can automatically escape interpolations.
* Performance can be faster than all but the best hand-written code. Good template systems take great care to update only the DOM that needs to change.
* Static analysis is easier. Most template systems support some kind of type-checking and intellisense. Many similar static analysis passes are much more difficult to do with imperative APIs.
* Efficient server-side rendering becomes possible, due to the ability to interpret declarative template definitions outside of the full browser environment.

It's rare to see a technique that wins so completely on so many axes; that's good for DXandUX, for security, and portability, and is so extremely popular as to be ubiquitous.

So templating is great, but what's the problem with the current situation?

The biggest thing to me is that there's an extremely core need of nearly all web applications that's just not being met by the platform. The web platform should adapt to meet such clearly demonstrated developer needs, and in the case of templating it hasn't yet. And it's such an obvious thing to add, similar to howinternationalizationand agreat datetime APIare now part of the platform, or howschedulerandsanitizerAPIs are hopefully coming soon too.

But we also have real consequences of the lack of templating, it's bad for everyone:

Users suffer from longer app download times, rendering overhead, and/or insecure apps. They often need to wait for library code to download before their application is usable. For templating, this can range from only a few kB in the best cases, to upwards of 100kB or more in the worst. A few kB might not seem that bad, but it can be a pretty large portion of an ideal budget for initial interactive rendering of an app.

Developers need to reach for a library, and thus tools like npm or a CDN, to do many basic things. This adds to the overhead of getting started. It makes simple static files and devtools less useful than they could be. There's no fundamental templating knowledge that's portable between stacks, and native DOM creation APIs like innerHTML are unsafe by default.

Frameworks are harder to build because they have to implement templating. Templating libraries are challenging to build and maintain because they're under massive constraints: they must be ergonomic, fast to render, fast to update, secure, and as small as possible. Libraries very often have to make hard trade-offs between features, performance, and code size.

And the platform suffers from this friction as it competes with native platforms that are far less sensitive to a few kB here and there. Competing platforms like Flutter, SwiftUI, Jetpack Compose, etc. not only all have templating-like systems built-in, but they work on app installs, use compiled languages, and also don't have to worry as much about things like a few kB in app bundle size.

## Why right now is a great time to add templating

There have been proposals to add things close to templating to the platform before.E4Xwas a big one that actually shipped in Firefox and Flash. E4H was a simplification of that idea by Ian Hixie that I can't find any references for anymore. At some point around 2012 there were even prototypes of a built-in `html` template-literal tag. Those failed, and for the better I think, because they might have helped with creating DOM, but not with updating it.

But now I think we can revisit this feature. In fact, I think that right now is aparticularlygood time to address this situation and add a templating API to the DOM.

A big reason why I think we can do this now is that frameworks have worn great cowpaths to pave. And while it's true that there's a lot of variety in userland template solutions, they're actually very similar in a lot of ways, and they seem to be getting more similar over time. We understand ergonomic template syntaxes and reactivity models a lot better than 13 years ago.

But also, not everyone uses frameworks and there's a lot of pent-up developer demand for ergonomic DOM manipulation and reactivity APIs from so-called "vanilla" developers and the web components communities.

There are in-flight proposals for very low-level DOM update primitives, likeDOM Parts, which target framework implementations, but I think higher-level APIs like full declarative templating can take even more load off, help prove out and complete the lower-level API proposals, and be really impactful for developers and users.

### We know what good syntax for templating looks like

The popular client-side template systems out there all share fundamentally similar syntax of markup with bindings. While there are small differences in expression delimiters, control flow constructs, binding type designators; the similarities are far greater than the differences. Even across the HTML-based (Vue, Angular, Svelte) and JavaScript-based (React, Lit, Solid) spectrum.

Things get even more similar when you look at JavaScript-based APIs (which any new DOM API would be): templates are usually expressions, composition is done via nesting template expressions or references to them, and control flow is just JavaScript.

There's also a lot of similarity in semantics. The most popular JavaScript-API-based systems return a description of the DOM from a template expression, then apply that description with a separate render function call. Most of those also update the DOM with the same render function call (though some eschew that altogether for fine-grained reactivity).

Previous platform proposals didn't match these semantics. Both E4X and E4H added new syntax to JavaScript to embed markup in JavaScript similar to JSX, but they critically didn't return a description of DOM, but a fragment of DOM itself. This made them good for initial DOM creation, but bad for updates, which were still imperative.

### We can build an API for today's JavaScript

It's been here for a while, but it's worth reminding readers: we have a built-in JavaScript feature for embedded DLS like HTML:tagged template literals.

So we can describe templates in a DOM API without having to add new features to JavaScript. And we have popular libraries that prove this approach works well. That's a big deal for realistically being able to move a proposal forward.

### We can also plan for tomorrow's JavaScript

Tagged template literals are great - they're an often unsung hero feature of ES2015 - but they have a bit more syntactic overhead than JSX, especially with userland component systems. And, people love JSX.

So some people might ask: why don't we just add JSX to JavaScript too?

Well, the problem with JSX is that it's all syntax and no semantics. This means that in order to standardize it we can't just add new syntax to JavaScript, we have to define the semantics. Treating JSX as a call to an ambiently-defined createElement() call is out of the question. Creating a tree of objects is possible, but that's one of the least efficient ways to use JSX as it irretrievably mixes static unchangeable parts of the tree with dynamic parts of the tree, precluding more efficient update patterns. If the Records and Tuples proposal were progressing, JSX could maybe create Records with boxes, but that proposal has been stalled, especially on the record identity and box parts that would make it suitable for a JSX semantics.

Nailing down the semantics is already probably the hardest part of a hypothetical JSX proposal, but there's also a chicken-and-egg problem when it comes to templating. In order to ensure that a JSX-like syntax and semantics is suitable for full-expressive DOM templating, we need a target templating system to verify it against. It might seem like React already provides this, but in some ways React's templating is less powerful and expressive than other systems. For instance, React doesn't provide a way to explicitly bind to properties and events of DOM elements, or provide directives that apply to an element.

But again, people love JSX, and JSX has absolutely proven the popularity of embedding markup in JavaScript. So I do believe that the platform should eventually take a look at adding something like it. I'm just a realist about how much work that is and think that we can do templating with today's JavaScript much sooner.

Luckily, the good thing about today's non-standard JSX is that it's pure syntax with no runtime semantics. This means that we can build JSX-to-tagged-template-literal compilers, as many have done for things like JSX-to-Lit. A transform for JSX to a native template API would make the template API a compile target, where developers could choose a syntax they prefer, with little-to-no runtime overhead charged against users.

Then, if work to standardize JSX is picked up by someone, it'll have a concrete system to target. The template system may have to adapt to accept the data type that a JSX expression evaluates to, but this is eminently possible, and a better direction to adapt in that having a native JSX syntax and semantics that we later realize are insufficient for native templating.

### We can lay the groundwork for HTML-based templating

Many web developers have been asking for a full-features HTML-based templating system. This is across communities like web components users, framework users, and "vanilla" developers. Many developers expected this kind of templating from the `<template>` element, or from declarative shadow DOM, or web components in general, and are disappointed that it's not the case. And a very large fraction of frameworks use HTML-based templates instead of JavaScript-based templates: Vue, Angular, Polymer, Svelte…

So they might ask why we don't pursue an HTML-based API first instead of a JavaScript-based API?

My answer would be that an HTML-based system is just a much, much larger undertaking. The beauty of React and JSX is that it leaves so many things to plain JavaScript while the JSX part only concerns itself with markup and bindings. Control flow and expressions are just script. An HTML-based template system would need to invent binding syntax, an expression language, control flow constructs, plus all of the template update mechanisms that a JavaScript-API has to.

We also don't have a native way to load HTML-based template definitions. The HTML Imports feature of the web components v0 spec is gone, and HTML Modules aren't here yet. This means that we'd have to embed HTML templates inside JavaScript modules, and at that point it's nicer to have your expressions just be JavaScript in the same lexical scope as your data. In fact, this is exactly the reason that Polymer 3, (which moved the HTML templates of Polymer 2 into JavaScrip) led directly to Lit. It was less code and a better experience to just let JavaScript handle all the script-like things.

So a JavaScript API is a subset of an HTML-based API, and will be a huge stepping stone towards an HTML-based API. Once the JavaScript API is in and proven, the HTML API only takes defining bindings, expressions, control flow, and a module system (ok, yes, that's still a massive amount of work).

### We've explored the reactivity landscape

While early DOM templating proposals didn't include updating, userland systems have thoroughlyexplored the landscape by now, and discovered good mental models and better and worse implementation approaches. I think we can now zero-in on a system that combines the best features from the different approaches.

The most popular reactivity approaches can be grouped into a few main categories:

* VDOM and diffing as used in React
* Template identity as used in Lit
* Signals and similar fine-grained reactivity as used in Solid (and an increasing number of frameworks like Svelte, Vue, Angular)

Diffing is great because on the surface it's a very comprehensible model, and it works with any data. Unfortunately, it's slow compared to other approaches, and variations in diffing algorithms could be observable. I think it'd be difficult to standardize one diffing algorithm, and difficult to convince platform engineers to accept an approach with that much overhead.

Template identity - which updates the DOM if it was rendered with the current template, replaces it otherwise - is fast and gives very similar results to diffing in a majority of use cases, and it's easy to understand. It fits very well with tagged-template literals, alternate JSX transforms, and HTML-based templates, and has a nice simple semantics. It would be straightforward to specify.

Signals… are great, IMO. I strongly supportthe proposal to add them to JavaScript, and think that they should be a part of any new reactive DOM APIs including a template API.

Signals aren't a native part of the platform yet, and not guaranteed to be in. Signals-based systems also require all your data to be wrapped in signals - they work best when you're all in on them. But there's a lot of data that's not in signal form, and a lot of platform APIs that don't produce signals. Re-rendering is an easy way to pick up changes to non-signal data.

It's pretty easy to have a system that supports both template updating and fine-grained signals updating as co-existing modes of reactivity. A signal-pure template - one that only passes signals to bindings - would never need to be "re-rendered" - it could always only update via signals. A template that possibly references non-signal data needs to be re-rendered. Typically re-rendering is done automatically by the component or framework layer which will have reactivity, like reactive component properties.

I think this makes template identity with signals a winning combination that's fast, comprehensible, flexible, and possible to to specify.

## A path to a proposal

I brought up the topic of a native declarative JS templating API inthis GitHub issue, and I think what's vaguely outlined there is a logical and valuable next step for DOM creation APIs; for vanilla web developers, web components developers, and future framework evolution.

* It's immediately useful to vanilla web developers as an ergonomics and secure DOM creation primitive.
* It's immediately useful to many existing web component libraries, such as Lit, FAST, HyperElement, etc.
* It's immediately useful to raw web component API users, and a stepping stone to a more complete ergonomic reactive component definition API.
* New frameworks can be built around it.
* Existing frameworks could use it as a compile target, runtime backend, or possibly support the templating API directly.
* It's useful for reactivity - both for "re-rendering" techniques and for use with Signals
* It's a good stepping stone to declarative HTML templating and declarative custom elements.It's a much smaller API to agree on and specifyIt helps define the semantics for templates
* It's a much smaller API to agree on and specify
* It helps define the semantics for templates
* It will require the completion of the DOM Parts proposal, and help define it and prove its usefulness.

This is no small undertaking though. The surface API and syntax aren't huge, but the behavior space and the underlying DOM Parts API are large. Fine-grained reactivity also requires some kind of DOM scheduler. So there are a large number of things to enumerate, agree on, specify, and add tests for.

It's going to have to be a collaborative effort, but I think it can be done and deliver huge value for web developers and users. I'll be working on a proposal as much as I have time for, and hopefully I can get other developers, especially some platform engineers interested too.

Please comment onwebcomponents#1069, or reach out to me onBlueskyif you're interested!

### likes on Bluesky
