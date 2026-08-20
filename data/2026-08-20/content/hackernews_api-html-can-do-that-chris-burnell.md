---
title: HTML Can Do That · Chris Burnell
url: https://chrisburnell.com/html-can-do-that/
site_name: hackernews_api
content_file: hackernews_api-html-can-do-that-chris-burnell
fetched_at: '2026-08-20T19:30:42.896279'
original_url: https://chrisburnell.com/html-can-do-that/
author: Chris Burnell
date: '2026-08-19'
published_date: '2026-08-08T06:00:00-03:00'
description: HTML has been gobbling up swathes of what used to be JavaScript’s remit. This page lists a bunch of dynamic functionality that we can now achieve with just HTML.
tags:
- hackernews
- trending
---

# HTML Can Do That

HTML has been gobbling up swathes of what used to be JavaScript’s remit. This page lists a bunch of dynamic functionality that we can now achieve with just HTML.

Update2026-08-20: I originally built this page in one hour duringHTML Day 2026to write and celebrate HTML, but I’ve since made some edits to better express and highlight where the browser implementation of some of this stuff is severely lacking and/or completely fails to meet accessibility needs. So, by all means, try it out, butmake it as accessible as you can!

## popover

Browser Support:popover →

Light dismiss,Escto close, no managingz-indexto wrangle it onto a top later. All managed withpopoverandpopovertarget(andpopovertargetaction) attributes in HTML. (MDN)

Toggle popover

No JavaScript, just modern browser magic, thanks to the wonderful folks speccing for the web and building our browsers!

Close

<button popovertarget="example-popover">Toggle popover</button>
<div id="example-popover" popover>
	<p>No JavaScript, just modern browser magic, thanks to the wonderful folks speccing for the web and building our browsers!</p>
	<button popovertarget="example-popover" popovertargetaction="hide">Close</button>
</div>

## <dialog>

Browser Support:dialog →

Similar thing going on aspopoverhere, except this time with a dedicated element for modal dialog boxes. (MDN)

Seecommand/commandForbelow for another, more recently-landing feature that allows us to open and close dialog elements (and will be useful for lots of other non-JS functionality, one day!).

Toggle <dialog> popover

Once again thepopoverattribute is doing some heavy-lifting here!

Close

<button popovertarget="example-dialog">Toggle &lt;dialog&gt; popover</button>
<dialog id="example-dialog" popover>
	<p>Closed with just HTML via <code>&lt;form method="dialog"&gt;</code>, opened with the <code>popover</code> attribute.</p>
	<button popovertarget="example-dialog" popovertargetaction="hide">Close</button>
</dialog>

Even though it’s sort of against the spirit of this page, I want to include this short snippet of how to interact with dialog elements in JavaScript:

Open dialog

This one is opened with.showModal()and closed with.close(), both called from JavaScript.

Close

Show JS-powered dialog code

<button id="example-dialog-js-open">Open dialog</button>
<dialog id="example-dialog-js">
	<p>This one is opened with <code>.showModal()</code> and closed with <code>.close()</code>, both called from JavaScript.</p>
	<button id="example-dialog-js-close">Close</button>
</dialog>

document.getElementById("example-dialog-js-open").addEventListener("click", () => {
	document.getElementById("example-dialog-js").showModal()
})
document.getElementById("example-dialog-js-close").addEventListener("click", () => {
	document.getElementById("example-dialog-js").close()
})

## Grouped<details>

Browser Support:details name →

A sharednameattribute turns a group of<details>into an exclusive accordion. Open one and the others close automatically. Magic! (MDN)

First

Open the second one and watch this close on its own.

Second

First one’s hidden now.

<details name="example-group">
	<summary>First</summary>
	<p>Open the second one and watch this close on its own.</p>
</details>
<details name="example-group">
	<summary>Second</summary>
	<p>First one’s hidden now.</p>
</details>

## command&commandfor

Browser Support:invoker commands →

Separate HTML buttons controllingonepopover. No scripting. (MDN)

Note:So far onlyshow-modal,close,request-close,toggle-popover,show-popover, andhide-popoverhave landed stable in browsers. We can look forward to invokers supported in the future to increment/decrement values, interact with media elements, copy text, etc.

Open

Close

show-popoveropens this andhide-popovercloses it!

Close

<button command="show-popover" commandfor="example-command-popover">Open</button>
<button command="hide-popover" commandfor="example-command-popover">Close</button>
<dialog id="example-command-popover" popover>
	<p><code>show-popover</code> opens this and <code>hide-popover</code> closes it!</p>
	<button command="hide-popover" commandfor="example-command-popover">Close</button>
</dialog>

## loading="lazy"

Browser Support:loading-lazy-attr →

This image defers loading until it’s near the viewport. Not anIntersectionObserverin sight. (MDN)

<img src="/images/avatar@2x.jpeg" loading="lazy" width="200" height="200" alt="a photo portait of Chris Burnell’s face">

## hidden until-found

Browser Support:hidden until-found →

Navigating to the fragment link below reveals the hidden section. The browser automatically removeshidden="until-found". (MDN)

Note:This one’s still pretty new and only really plays nicely with browser default search, and not so well with screen reader search implementations, for example. Still, one to keep in the back pocket for another day down the road!

Jump to hidden content

Yahaha! You found me!

<a href="#example-until-found">Jump to hidden content</a>
<div id="example-until-found" hidden="until-found">
	<p>Yahaha! You found me!</p>
</div>

## Colour, Date & Time, Range Inputs

Browser Support:input-color →,input-range →,input-datetime →

Colour, range, and date pickers, built right into the browser. (MDN: Color Input,MDN: Range Input,MDN: Color Input)

Warning!Some of these elements feel a little unfinished. I’m hoping that we can expect form elements to receive some more love over the coming years, but at this point in time, the implementations shipping in browsers are still lacking. I would tread very carefully with using some of these. You can expect things like the default browser styles of these elements to vary pretty wildly between browsers and for the accessibility experienecs to be very poor. Be wary of the many pitfalls!

Colour

Range

Date

<label>Colour <input type="color" value="#5f8aa6" autocomplete="off"></label>
<label>Range <input type="range" min="0" max="100" value="50" autocomplete="off"></label>
<label>Date <input type="date" autocomplete="off"></label>

## <datalist>

Browser Support:datalist →

Native autocomplete suggestions, no dropdown library required. (MDN)

Warning!Support for this across input types is still pretty spotty, and there are also a number of issues in its implementation in browsers. See Adrian Roselli’sUnder-Engineered Comboboxenfor more info. You might even want to skip using this for now, and keep an eye on it to see if it improves over the new few years.

Favourite HTML element 

<label>Favourite HTML element <input type="text" id="example-datalist-input" list="example-datalist" autocomplete="off"></label>
<datalist id="example-datalist">
	<option value="a">
	<option value="abbr">
	<option value="address">
	<!-- ... -->
</datalist>

Written and built byChris BurnellforHTML Day 2026during theOnline Eventrun byZachary KaionSaturday, 8thAugust 2026.

I welcome corrections or amends to this page!I am not an expert, but I’ve attempted to represent things honestly. Do not use this page to justify decisions to your boss.Or yourself.Don’t forget that not everyone browses the web like you do. And have fun with these new-ish features of HTML!