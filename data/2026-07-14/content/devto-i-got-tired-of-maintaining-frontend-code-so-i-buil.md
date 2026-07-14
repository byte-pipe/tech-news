---
title: I Got Tired of Maintaining Frontend Code. So I Built a Declarative UI Runtime. - DEV Community
url: https://dev.to/thuangf45/i-got-tired-of-maintaining-frontend-code-so-i-built-a-declarative-ui-runtime-5dbl
site_name: devto
content_file: devto-i-got-tired-of-maintaining-frontend-code-so-i-buil
fetched_at: '2026-07-14T11:32:48.173812'
original_url: https://dev.to/thuangf45/i-got-tired-of-maintaining-frontend-code-so-i-built-a-declarative-ui-runtime-5dbl
author: Thuangf45
date: '2026-07-10'
description: 'Here is a question that sounds simple until you''ve actually shipped a UI: how many files does it take... Tagged with javascript, webdev, showdev, architecture.'
tags: '#showdev, #javascript, #webdev, #architecture'
---

Systems-level shift from code to data

Here is a question that sounds simple until you've actually shipped a UI: how many files does it take before nobody on the team, including you, can confidently say what happens when you click a button?

For me, the answer turned out to be somewhere around two hundred. Not because the logic was complicated. Because nothing in those two hundred files agreed with anything else about how a button should be built.

This is the story of how I got there, what it cost me, and the engine I eventually built to make sure it wouldn't happen to me again. LuciaCore is a prototype, not a finished framework, but it already does the one thing I set out to make it do: let me describe a working, interactive web page as data, instead of assembling it by hand every time.

## Where I came from

My background is systems programming: operating systems, networking, CPU scheduling, architecture, API performance. That's the layer where I'm comfortable, because the problems there tend to be well-defined. You can usually name the bottleneck, measure it, and know whether your fix actually worked.

Nothing runs in isolation forever, though. At some point, whatever gets built needs a face, a web app, a mobile client, a desktop tool, something a person actually clicks on. So I picked up frontend development, assuming it would be the easy detour before getting back to the interesting work. HTML, CSS, and JS took a day or two to understand conceptually. A few more days of tutorials and small exercises, and I felt ready.

I was wrong about the "easy" part, but not in the way I expected. The syntax was never the problem.

## What a growing frontend project actually costs you

I started with a portfolio site. Small in scope, on paper. In practice, it took an entire month, and almost none of that month went into deciding what the site should say or look like. It went into everything that sits between an idea and a working page.

CSS was the first tax I paid. Every button needed its alignment decided by hand. Every new class needed a naming convention, one I was inventing as I went, and every new page tempted me to bend that convention slightly rather than follow it. That's how a project quietly ends up with three different ways of writing what is functionally the same button, none of them wrong exactly, just uncoordinated.

The second tax was file count. I split the project into small modules for the sake of organization, dozens of files at first, then hundreds of HTML, CSS, and JS files. That solved readability at the file level and created a loading problem at the page level, since every page pulled in far more separate requests than it needed. So I bundled everything down: one JS file, one CSS file, a handful of HTML files per page. That fixed load time and quietly made the next problem worse.

Roughly, the shape of that change looked like this:

Before (hundreds of small files) After (bundled)
portfolio/ portfolio/
├── header.html ├── index.html
├── header.css ├── about.html
├── header.js ├── contact.html
├── footer.html ├── bundle.js
├── footer.css └── bundle.css
├── footer.js
├── button-primary.html
├── button-primary.css
├── button-primary.js
├── button-secondary.html
├── button-secondary.css
├── button-secondary.js
└── ... 190+ more files like this

Enter fullscreen mode

Exit fullscreen mode

Fewer requests, same underlying problem: every one of those original files still had to be found, opened, and understood by hand whenever something needed to change.

The real cost showed up during maintenance. Every UI tweak or visual bug turned into a search, going file by file, trying to find whichever one was actually responsible for what I was looking at on screen. Nothing pointed back to its source in an obvious way, because nothing had been built to a consistent shape to begin with. Each component reflected whatever I happened to think looked right that day, with no shared structure connecting one to the next. That's the part that's hard to explain to someone who hasn't lived through it: no single file was bad. The problem was that holding an entire project's accumulated inconsistency in your head at once had become its own full-time job.

Around then I looked at Tailwind, React, and TypeScript, assuming a proper framework would make the problem go away. It moved the problem instead of removing it. I still needed npm, a build pipeline, and configuration files, and I still ended up with hundreds of files, just organized under someone else's conventions instead of mine. The portfolio project sat unfinished for a long time after that. Not because I didn't know how to write the UI. Because the overhead of keeping it consistent had outpaced my patience for it.

## The realization

For a while I kept framing the problem as "which tool solves this," which meant I kept evaluating frameworks against each other and finding the same shape of overhead underneath all of them: files to organize, conventions to enforce by hand, a build step standing between the source and the running page.

The actual shift happened when I stopped asking which framework, and started asking a more uncomfortable question: what if the problem wasn't the framework at all? What if it was the fact that I was hand-assembling HTML, CSS, and JS every single time, regardless of which tool I used to do it? Frameworks were giving me better ways to organize that assembly work. None of them were removing the requirement to do it.

That's the moment LuciaCore actually started, not as a search for a better framework, but as an attempt to eliminate the manual assembly step entirely. If a browser can already run HTML, CSS, and JS natively, the real question was whether something could sit on top of that and generate the markup and behavior on my behalf, driven by nothing more than a description of what I wanted, rather than a hand-written implementation of it.

## Why JSON

HTML describes structure. CSS describes appearance. JavaScript describes behavior.

LuciaCore doesn't try to replace any of those three. It sits one level above them, describing what a developer intends the interface to be, rather than the implementation of any single layer. All three of HTML, CSS, and JS are still implementation underneath it, and implementation is exactly where the inconsistency I'd been fighting kept creeping in, because implementation has to be redone by hand every single time, and hand-done work drifts.

What I wanted instead was a way to describe intent: this is a button, it says this, it does that when clicked, place it here. Not how to construct that button node by node, but what the button is supposed to be. JSON turned out to be a good fit for that, not because it's a clever format, but because it's just data. It has no execution model of its own, so there's nowhere for implementation detail to sneak back in. The engine, not the author, is left responsible for turning that description into an actual DOM node, actual scoped styles, and an actual event listener, the same way, every time, regardless of who wrote the JSON or when.

Written out, that description looks like this:

{

 
"type"
:
 
"button"
,

 
"label"
:
 
"Get started"
,

 
"action"
:
 
"navigate::to::signup"
,

 
"style"
:
 
"background: #2563eb; color: white; padding: 12px 20px; border-radius: 8px;"

}

Enter fullscreen mode

Exit fullscreen mode

and the engine turns it into this, every time, regardless of who wrote the JSON:

<button

 
class=
"lucia-button"

 
style=
"background:#2563eb; color:#fff; padding:12px 20px; border-radius:8px;"

 
data-action=
"navigate::to::signup"
>

 Get started

</button>

Enter fullscreen mode

Exit fullscreen mode

Nothing in the JSON describes how the DOM node gets built, how the click listener gets attached, or how the style gets scoped so it doesn't leak into the next button on the page. All of that is the engine's responsibility, and it's handled the same way for every node, which is exactly the property I didn't have before.

That's the core distinction LuciaCore is built around. It isn't a component library with a different syntax. It's closer to a declarative UI runtime, something that sits in the browser and interprets a description of an interface, rather than a framework you configure and build against. JSON just happens to be the serialization format that description is written in, it isn't the interesting part on its own, it's a convenient, unambiguous way to write down intent. I'm avoiding the word "framework" deliberately here, because a framework usually still expects you to write the implementation, just inside its rules. LuciaCore is asking for the description instead, and handling the implementation itself.

## Designing the vocabulary

Once I'd committed to describing UI as data, I needed to decide what the smallest usable vocabulary looked like. I split interfaces into two categories:

* Layouts,row,column,grid,card, which control how children are arranged.
* Primitives,button,text,input,image,loading,... the actual leaf elements a user sees and touches.

In practice, a small piece of UI is just those two categories nested inside each other:

row
 └─ column
 ├─ text "Welcome back"
 └─ button "Sign in" → action: navigate::to::home

Enter fullscreen mode

Exit fullscreen mode

Nothing in that tree is a special case. Acolumndoesn't know or care whether its children are more layouts or primitives, it just arranges whatever it's given, which is what makes the two categories composable instead of a fixed set of page templates.

I chose JavaScript to build the engine itself for an unglamorous reason: the browser already runs HTML, CSS, and JS natively, so if the engine is just JS, the only thing a project needs on top of it is one JSON file. No npm install, no build step, no compiler stage between the source and the running page.

Once the layout and primitive split existed, a few more concepts fell out of it almost on their own:

* typedeclares what to render, a layout, a primitive, a component defined elsewhere in the file, or a standalone module, as long as it resolves to a valid name.
* styleis raw CSS that the engine injects and scopes automatically, so any layout or primitive can be visually overridden without touching engine internals.
* actionis a string describing a system call I defined myself, and this one deserves its own explanation.

## The action DSL

I didn't want click handlers scattered across the codebase the way I'd had them before, each one a small, differently-shaped piece of imperative logic. What I wanted was for behavior to be describable the same way structure already was: as intent, not as a sequence of steps.

That's why actions in LuciaCore are plain strings likenavigate::to::home,alert::message,api::call, orstorage::set::key::value. Each one reads roughly like a sentence: verb, then target, then argument.navigate::to::homedoesn't tell the engine how to swap pages, tear down the old DOM, or restore scroll position. It says where the user intends to go, and the engine owns the how. The same is true forapi::call, which describes that a request should happen, not the fetch boilerplate underneath it.

A button wired to one of these needs nothing else attached to it:

{

 
"type"
:
 
"button"
,

 
"label"
:
 
"Save changes"
,

 
"action"
:
 
"api::call |> alert::Saved!"

}

Enter fullscreen mode

Exit fullscreen mode

On click, the engine reads that string and does two things in order: it fires the request described by the action, then shows the confirmation, once the first step resolves. Nothing about the fetch call, the loading state, or the sequencing between the two steps was written by hand for this button. It's declared once, in the string, and interpreted the same way for every button that uses it.

The distinction that matters here is the same one as everywhere else in the engine: the action string says what should happen, not how to implement it.navigate::to::homeandapi::call |> alert::Saved!are declarations of intent, not procedures. The engine still has to write the actual imperative code somewhere, the fetch call, the DOM swap, the event binding, but that code lives in one place, inside the engine, instead of being reinvented slightly differently in every click handler across a project.

This mirrors the same trade I made with layouts and primitives. A hand-writtenonClickhandler is implementation, and implementation is where inconsistency and one-off bugs like to live. A declarative action string is intent, interpreted the same way everywhere it appears.

For anything genuinely too custom for this vocabulary, I defined a resolution contract instead of extending the DSL indefinitely. Atypelikebutton::buy::shop::item::0resolves to/button/buy/shop/item/0.js. If it's a render module, the contract is arenderfunction. If it's an action module, the contract is anexecutefunction. Same naming convention, same resolution logic, whether you're extending rendering or behavior. The engine doesn't need to know the difference until it actually opens the file.

It also became clear early on that putting every piece of UI directly into a page's JSON would just recreate the sprawl I was trying to escape, in a new format. So I introducedcomponents, reusable UI definitions referenced bytype, with data flowing into them throughprops:anditem:tokens. The rule I settled on is simple, and I think it's the right default: the node being called always has final say over its own values. The caller supplies defaults, the callee can override them. That keeps composition predictable. You can reason about a component in isolation, without tracing every possible caller that might feed it data.

Here's what that looks like end to end. The component defines its own shape once:

{

 
"type"
:
 
"custom_cta_button"
,

 
"layout"
:
 
{

 
"type"
:
 
"button"
,

 
"label"
:
 
"props:label"
,

 
"action"
:
 
"props:action"
,

 
"style"
:
 
"background:#16a34a; color:white; padding:10px 18px; border-radius:6px; props:style;"

 
}

}

Enter fullscreen mode

Exit fullscreen mode

and any page can call it, supplying only the values that differ:

{

 
"type"
:
 
"custom_cta_button"
,

 
"props"
:
 
{

 
"label"
:
 
"Start free trial"
,

 
"action"
:
 
"navigate::to::signup"
,

 
"style"
:
 
""

 
}

}

Enter fullscreen mode

Exit fullscreen mode

The component owns its structure and styling defaults. The page calling it only ever supplies data. Neither side needs to know the other's internals to work correctly together.

Looking back, this is roughly the point where the project stopped being just a JSON schema and started being something closer to a small declarative language: types, layouts, actions, tokens, and a resolution contract for extending all three. JSON is still just the syntax that language happens to be written in. I don't want to overstate this, it's a small language with a narrow purpose, not a general-purpose one, but it's more accurate to describe it that way than to call it a data format with some conventions attached.

## Two files, then one

The engine split naturally along its two responsibilities:action.jsfor parsing and dispatching behavior,render.jsfor reading JSON and generating HTML and CSS. Getting each into a shape that actually held together took an unglamorous number of iterations, implement, break, fix, repeat. Nothing about that part was clever. It was just work.

Along the way I refactored harder than I expected to. Early on, out of sheer file-splitting habit left over from the portfolio project, I'd broken every primitive into its own file,row.js,button.js, one file per concept. Once the engine's behavior stabilized, I noticed that split was pure overhead: layouts and primitives share roughly 99% of the same rendering logic, just with different tag names and default styles. I folded it all back into the engine's core instead of scattering it across files, the same instinct that had caused the original mess, now working in the opposite direction.

I addedmain.jsto wireaction.jsandrender.jstogether, and to read thesystemblock ofcontent.json, versioning, and registering a Service Worker for offline caching when one is configured. After that refactor, the whole engine was down to three lean files, which I bundled and obfuscated into a singleluciacore.engine.js, the only script a project needs to load.

## The first real feedback

After running it myself for a few days, I showed it to another engineer I know. Their reaction was direct: it was easy to pick up, specifically because there's now one standardized way to describe UI, generated consistently by the engine, instead of everyone inventing their own structure the way I had. You can still customize anything, the engine just compiles it down to the same consistent shape every time, regardless of who wrote it.

I also handed it to someone with no engineering background, and they hesitated, not because the underlying idea was wrong, but because I hadn't separated concerns cleanly enough yet. Layout and content lived in the same JSON, which meant editing a headline required understandingrow,column, andpropsfirst. That's what led me to splitcomponentsfromcontents:

* componentsdefine how something looks, built from layouts and primitives, the part that requires understanding structure.
* contentsdefine what it says, the actual text and data values, the part a non-technical collaborator should be the only thing they need to touch.

That split opened a door I hadn't planned for originally: components as shareable, drop-in pieces. Instead of asking "can I get your HTML, CSS, and JS," you ask "can I get your component," paste the JSON into your owncontent.json, and it works, no framework version to match, no build config to reconcile. It's a smaller, more contained unit to hand off than a chunk of markup or React code you'd otherwise hesitate to touch without fully understanding it first.

## What this means for working with AI tools

There's a side effect of this structure worth mentioning, but I want to be careful about how, because it's easy to overstate. It isn't that a language model becomes smarter when it reads LuciaCore's JSON. It's that a small, bounded, consistently-shaped schema is simply less for any reader, human or model, to hold in working memory at once, compared to hundreds of loosely related HTML, CSS, and JS files with no shared structure connecting them.

A model reasoning about a UI written as scattered markup has to reconstruct the relationships between files first: which class affects which element, which script wires up which button, before it can reason about the actual change being asked for. Acontent.jsonfile skips that reconstruction step, because the structure is explicit and uniform by construction. A page is a tree of typed nodes. Styles are locally scoped. Actions are declared inline, next to the node they belong to. Ten lines of that schema is a smaller, more predictable context than five hundred lines of implementation detail, not because the model got better at reading code, but because there's less ambiguity to resolve before it can start reasoning about intent.

## Making it fast: an optimization story

Getting the vocabulary right didn't make it fast, and I want to be specific about why, because the failure mode here is an ordinary one for anything doing recursive tree rendering on a single thread.

The engine renders a page by recursively walking the JSON tree and building HTML and CSS from it. JavaScript in the browser is single-threaded, so that recursive rendering work and the logic and network work, fetching data, running actions, were competing for the same thread. The practical result was contention: the UI couldn't paint until rendering finished, and rendering was sharing time with whatever network or logic work happened to be in flight at the same moment. On pages with a lot of nodes, that meant three to five seconds to open on a laptop, and ten to fifteen seconds on a phone. Slow enough to notice immediately, not a rounding error.

Roughly, the before and after looked like this:

Before — everything blocks the same thread
main thread: |--- walk JSON tree ---|--- fetch data ---|--- run actions ---|
 | |
 page load starts first paint (3–5s desktop, 10–15s mobile)

After — UI paints first, work continues in the background
main thread: |--- paint skeleton ---|
 | |
 page load starts first paint (near-immediate)
 |--- fetch data ---|--- hydrate nodes ---| (background)

Enter fullscreen mode

Exit fullscreen mode

Two changes addressed most of it, in this order.

The first was letting the main thread yield to the browser's paint cycle before doing anything else. Rather than running the render walk and the logic and network work back-to-back on the same thread, I restructured the flow so the UI could paint a skeleton immediately, yielding execution back to the browser so it could actually draw, before continuing with data fetching and action logic in the background. The scheduling change didn't make any individual piece of work faster. It just stopped forcing the user to wait for all of it to finish before seeing anything at all.

The second was caching compiled pages, keyed by a hash of the content. Recompiling the entire JSON tree into HTML and CSS on every visit is wasted work if nothing has changed since the last one. LuciaCore now hashescontent.jsonand only recompiles a page when that hash actually changes, storing the compiled result for reuse. Cache invalidation here is simple by design: the hash either matches or it doesn't, so there's no separate invalidation logic to keep correct over time. Repeat visits, laptop or mobile, became noticeably faster once recompilation stopped happening on every load.

Neither change altered what the engine renders, only when and how often it does the expensive part of the work. That's usually where the real performance win is hiding in a system shaped like this: not in a faster algorithm, but in not redoing work you already did.

## What building with LuciaCore looks like today

The whole setup is two files.

index.html, scaffolded with!and Tab in VS Code, then one script tag added:

<!DOCTYPE html>

<html
 
lang=
"en"
>

<head>

 
<meta
 
charset=
"UTF-8"
>

 
<meta
 
name=
"viewport"
 
content=
"width=device-width, initial-scale=1.0"
>

 
<title>
My App powered by Lucia
</title>

 
<script 
defer
 
src=
"https://cdn.jsdelivr.net/gh/thuangf45/luciacore.assets@master/luciacore.engine.js"
></script>

</head>

<body>

</body>

</html>

Enter fullscreen mode

Exit fullscreen mode

content.json, the actual workspace, with four sections:

{

 
"system"
:
 
{
 
"version"
:
 
"1.0.0"
,
 
"debug"
:
 
true
 
},

 
"pages"
:
 
[

 
{

 
"name"
:
 
"home"
,

 
"layout"
:
 
{

 
"type"
:
 
"column"
,

 
"style"
:
 
"padding: 40px; gap: 16px; align-items: center;"
,

 
"children"
:
 
[

 
{
 
"type"
:
 
"text"
,
 
"level"
:
 
"h1"
,
 
"label"
:
 
"Hello LuciaCore"
 
},

 
{
 
"type"
:
 
"button"
,
 
"label"
:
 
"Click me"
,
 
"action"
:
 
"alert::It works!"
 
}

 
]

 
}

 
}

 
],

 
"contents"
:
 
[],

 
"components"
:
 
[]

}

Enter fullscreen mode

Exit fullscreen mode

* system, engine configuration: debug mode, versioning, offline caching.
* pages, the routes of the app, reached withnavigate::to::pageName.
* contents, the editable text and data a non-technical collaborator should touch.
* components, reusable UI templates built from layouts and primitives, referenced bytypeand fed data throughprops:anditem:tokens.

That's the entire mental model needed to start. No package manager, no build step. The engine does that work in the browser, at the moment the page loads.

## Where it stands, and why I built it this way

I want to be direct about the current state: LuciaCore is a prototype. It hasn't been through years of production edge cases the way an established framework has, and I'm not claiming it should replace one, or that it renders faster than the tools people already reach for. What I can say is narrower, and I think more honest: it's a genuinely usable engine, today, for building real interactive, multi-page UIs, buttons that do things, pages that navigate, data loaded from an API, described entirely as data rather than code.

I wasn't trying to replace the browser. The browser already does its job well. I was trying to reduce the amount of frontend complexity I personally had to manage by hand, the naming conventions, the file sprawl, the one-off click handlers, the accumulated inconsistency that made a small portfolio site take a month to finish. Describing structure, behavior, and content as three separate, explicit things, instead of one undifferentiated pile of markup and script, is the trade LuciaCore is built around, and it's a trade I'd make again.

Every framework I've used represents a different set of trade-offs, and none of them is free. React, Vue, and Angular each trade differently between flexibility and structure, and each is better suited to some problems than others. LuciaCore isn't an attempt to beat any of them at what they do. It's an exploration of a different trade: developers describe intent, and the runtime owns the implementation, in exchange for less flexibility at the edges than a general-purpose framework would give you.

If you've run into the same wall, or if you look at this and immediately see where it would break under your own workload, I'd rather hear about it than not. The code and docs are on GitHub.

* Github:LuciaCore Engine
* Gitbook:Luciacore Docs

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (42 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse