---
title: Why don’t more developers “use the platform”? | Read the Tea Leaves
url: https://nolanlawson.com/2026/10/03/why-dont-more-developers-use-the-platform/
site_name: hackernews_api
content_file: hackernews_api-why-dont-more-developers-use-the-platform-read-the
fetched_at: '2026-10-04T22:12:23.187531'
original_url: https://nolanlawson.com/2026/10/03/why-dont-more-developers-use-the-platform/
author: vinhnx
date: '2026-10-04'
published_date: '2026-10-03T13:49:29-07:00'
description: For years, advocates for web standards, performance, and accessibility have implored web developers to “use the platform”. I’ve often been one of those…
tags:
- hackernews
- trending
---

For years, advocates for web standards, performance, and accessibility have implored web developers to“use the platform”. I’ve often been one of those advocates.

The argument is simple: why build something yourself, in JavaScript, when the browser can do it for you? Whatever you build, it’s likely to have poorer performance and worse usability than something the browser could just give you out-of-the-box.

I think it’s worth taking the other side, though, if for no other reason than to understand where the “platform-skeptic” developers are coming from. If “use the platform” is so obvious, then why do so many people seem to need convincing?

The most obvious reason is historical: for the longest time, browsers were playing catch-up with the ecosystem on top of them. Libraries likejQueryfilled crucial gaps while browsers implemented equivalent APIs – and even then, you might have to wait for laggards like IE6 to age out before you could actually use them. Today, most browsers are evergreen (Safari is debatable, although~7 times per yearain’t bad), but up until the 2020s or so, web developers had to deal with a decidedlylumpy web. In that environment, rolling your own is a sensible choice.

Another reason is familiarity: when you’re used to looking for React components on npm, that’s what you tend to reach for, regardless of the problem at hand. If you search for “sticky positioning” on npm, there’s no package that says “just use CSSposition: sticky, you dolt.”

And often, even with a robust standard, libraries on npm would fill a useful gap between framework ergonomics and the platform underneath it. I always found it intriguing that many React developers preferred to stick to JSX and React idioms – raw DOM APIs felt “icky” – but were perfectly happy to use lower-level libraries where raw DOM manipulations are common. For example, a virtual list library might happily use raw DOM APIs for pure performance, while exposing higher-level primitives that a novice React developer could better grasp. In a sense, the ecosystem of React components led to a natural division of labor where those with more expertise packaged up unfamiliar platform APIs in a more familiar form factor.

Some of this effect was also driven by documentation. Many npm packages have lovingly detailedREADMEs or websites with examples, tutorials, and screenshots. Whereas untilMDNbecame cemented as the go-to place for web documentation (withweb.devas Google’s more future-facing arm), documentation for the web platform was scattered across blogs,StackOverflow, and sites likeCSS Tricks. And many of these sites would just tell you to use a well-known library like jQuery or GreenSock!

The 
Dragula site
 versus the 
Drag and Drop MDN page
. Arguably the former is still more compelling.

If it were just about third-party libraries versus platform APIs, though, then I don’t think it could fully explain the antipathy toward “use the platform.” Developers who are lazy (or do I repeat myself?), and who just want a ready-made solution for whatever problem they’re facing, are unlikely to care whether that solution comes from npm, the browser, or copied off of someone’s random GitHub Gist. They want to solve their problem and move on. But there’s a different source of anti-“use the platform” that I want to explore.

For a certain type of developer, building things yourself is justmore fun. And often the resulting code is easier to reason about, especially if you don’t have an encyclopedic knowledge of the web platform. And once you’ve built something, there can be a kind ofIKEA effectwhere you want to maintain and tinker with your own homemade code.

As an example, let’s imagine you’re trying to build a modal dialog. You might visually understand how these are supposed to work: content appears on the screen, but the background is still visible although partially occluded, and maybe clicking outside the dialog dismisses it. So you might grab forposition:absoluteandz-indexto position the dialog correctly – aha, but the background still scrolls, so you have to disableoverflowon the body… And then if you understand something about accessibility, you realize you need to handleEscto dismiss, and build afocus trap, and return focus to the element that launched the dialog, and…

For many developers, what I just described sounds like a nightmare (and a good way to build something that only half-works). But for many developers, this sounds like fun! Think of how much you learn as you start building this thing. And think about how you could start putting your own spin on it by adding animations, themes, an optional “close” button… Before you know it, you’ve built a library that’s ready to go on npm. That’swaymore fun than just grabbing<dialog>and calling it a day – what a downer!

And for many of us, before APIs like<dialog>existed,this was how we learned the web platform! Many of the people who now advocate for “use the platform” were once themselves authors of polyfills, shims, and libraries. I know because I’m one myself! I spent years working on tooling forIndexedDB,WebSQL, and other browser storage APIs as part of my work onPouchDB, which eventually led to me feeling confident enough to sit in W3C standards meetings and even open issues and pull requests on the IndexedDB spec itself. Without the forcing function of a gap in the platform that needed to be filled, I don’t know if I would have found the interest or motivation to get to that level of expertise.

Of course, doing it yourself is not always an unalloyed good. Sometimes it just comes from pure ignorance. On the web platform in particular, I think one of the reasons there was such a proliferation of JavaScript solutions to problems that could be better solved by CSS, for example, is that many developers just didn’t take the time to deeply understand how CSS works.

And to be fair, CSS has historically been hard to understand! There’s a reason the site is called “CSS Tricks.” Things like theclear fix,floats, and themin-width: 0trickare hardly intuitive. Rather than trying to understand CSS’s internal algorithm, it’s often much easier to just imagine the imperative logic you want and then express it in JavaScript. Plus, for years CSS didn’t have a straightforward way to express common patterns likeline clamping,textarea resizing,scrollbar hiding, etc. So of course developers built it themselves using the tools they already understood.

I don’t even think this phenomenon of “avoiding the platform” is limited to the web. It can apply to any developer working on top of a platform they don’t fully understand. For example, at my work, we useClickHousefor storing various kinds of analytics data. At one point, my coworker and I disagreed about how to store large JSON data in a column: he built a system for compressing it before storage, whereas I put the data in a separate key-value store and only inserted the key into ClickHouse. It turned out we were both wrong! ClickHouseautomatically compresses data, and as acolumnar data storeyou actually get better compression across rows if you just let ClickHouse handle it. And the separate key-value store was just a poor man’s version of what a columnarSELECTalready does.

I only realized these things after actually taking the time to thoroughly read the ClickHouse docs and then write a benchmark to prove my hypothesis. In the end I was shocked that we had built something that was slower and clunkier than what the platform itself could give us out-of-the-box. The parallels with JavaScript and the web platform were hard to ignore.

I’m sure that if you’re a developer on iOS or Android, or someone building on top of a game engine, or really any kind of developer building on top of any platform layer, you probably have similar stories. There’s a reason that thestereotypeof the grizzled senior engineer is someone who can take a junior’s baroque tangled mess of code and replace it with a single line. The more you learn, the more you’re able to wield your knowledge of how the entire system works end-to-end to create the smallest possible contribution to it (and thus reduce your maintenance burden in the long run).

I’ve been tryingreallyhard not to talk about AI this entire post (because I’ve done it to death over the past year), but of course I can’t help but wonder how AI coding will impact this phenomenon. I actually have both an optimistic and a pessimistic take:

* Optimistic:because LLMs have an encyclopedic knowledge of whatever platform you’re working with, they can chooseexactlythe right platform API to deliver the experience the prompter asks for in vague English. And since this solution is likely faster and more correct than userland code, the agent will prefer it after rigorous testing and benchmarking. Furthermore, the “IKEA effect” goes away when developers are not actually writing the code themselves.
* Pessimistic:because LLMs seem to love duplicating code – for example, ignoring helper functions that already exist in favor of writing their own for the umpteenth time – the amount of custom, non-platform-idiomatic code will skyrocket. Developers won’t instruct their agents to test enough or to try enough alternatives, and will just commit the agent’s first draft. And because it’s always possible to add moreepicycles, the agents will continue to iterate on over-engineered solutions that never should have existed in the first place.

In my own use of AI coding, I’ve seen both phenomena happen. I’d like to think that as models and coding harnesses get better we’ll start to veer more towards the optimistic outcome, but I can’t say for sure.

In any case, these are my longwinded and somewhat conflicting thoughts on “use the platform.” As a mantra I love it, because it succinctly captures a feeling I have when I’m looking at some overwrought pile of spaghetti code and thinking how much better and more elegant it would be if the author just understood the layers beneath them a bit better. At the same time, I’vebeenthat author, and I’ve felt the joy of building such beautiful, messy code (beautiful to me, anyway), so I think it’s worth understanding where such developers are coming from. For that reason, I’m sure we’ll be hearing “use the platform” for as long as there are platforms.

You can comment onthe fediverseorLobsters.