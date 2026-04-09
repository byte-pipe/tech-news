---
title: This Month in Ladybird - July 2025 - Ladybird
url: https://ladybird.org/newsletter/2025-07-31/
site_name: hackernews_api
fetched_at: '2025-08-02T23:07:31.986433'
original_url: https://ladybird.org/newsletter/2025-07-31/
author: net01
date: '2025-08-02'
tags:
- hackernews
- trending
---

# This Month inLadybirdJuly 2025







Hello friends! July is done. We merged 319 pull requests from 47 contributors.

### Welcoming new sponsors

Ladybird is entirely funded by the generous support of companies and individuals who believe in the open web. This month, we’re excited to welcome the following new sponsors:

* Scraping Fishwith $5,000
* Blacksmithwith high-performance CI infrastructure

We’re incredibly grateful for their support. If you’re interested in sponsoring the project, pleasecontact us.

### Web Platform Tests (WPT)

As usual, we’ve made some progress on the Web Platform Tests. We’ve added 13,090 passing tests for a new total of 1,831,856.

### Google reCAPTCHA passing

There was a long-standing issue with ourpostMessageimplementation: if the serialized type had not previously been used in the destination realm, we would fail to reconstruct it. The realm didn’t recognize the type and rejected the message.

This is now fixed, allowing Google reCAPTCHA to pass!

Unfortunately, this only works onhttps://www.google.com/for now, due to a separate unresolved same-origin policy issue.

### High refresh rate support

We now detect the refresh rate of the active screen to determine how often web content should be rendered. Previously, rendering was fixed at 60 frames per second.

Websites usingrequestAnimationFramenow render at up to 120Hz on supported hardware. This change also improves the smoothness of scrolling, animations, transitions, and more.

### HTTP/3 support

HTTP/3support was recently added in curl 8.14.0 for users of OpenSSL andngtcp2. Since Ladybird uses the OpenSSL backend with libcurl, this enabled us to support HTTP/3 as well.

We now negotiate HTTP/3 for servers that advertise it via theAlt-Svc header.

We also found and reported an issue in curl whereAlt-Svc: clearwas parsed incorrectly. This has since beenfixed in curl 8.15.0.

### Trusted Types

Trusted Types is a security feature that helps prevent cross-site scripting (XSS) by locking down injection sinks likeElement.innerHTML,HTMLScriptElement.text, andHTMLScriptElement.src. It allows web developers to define policies that control how sanitized content can be created and consumed.

This month, we added initial support for Trusted Types. This includes recognizing policies and enforcing type-safe DOM writes. Further work is ongoing to support more of the spec and improve compliance.

### SVGforeignObjectimprovements

The relationship between HTML and SVG is complex. While SVG content can appear in HTML, SVG can also embed arbitrary HTML using theforeignObjectelement.

This month, we made major improvements to how Ladybird handlesforeignObject. Layout, style resolution, and rendering inside embedded HTML are now much closer to spec behavior, with better integration between the two worlds.

### CSScontent: url(...)

We added support for usingcontent: url(...)in CSS pseudo-elements such as::beforeand::after. This allows authors to insert images via CSS content, matching behavior seen on modern websites.

### :state(foo)and:uncheckedpseudo-classes

We gained two new pseudo-classes:

* :state(foo)matches a custom element whose states set includes"foo". This allows custom elements to be styled based on internal state, similar to how:checkedand:emptywork.
* :uncheckedmatches elements that are checkable but currently not checked.

These additions improve our compatibility with web components and modern form styling.

### Logical property groups

Building on work fromlast month, we now generate the mappings from logical to physical properties at compile time.

Logical and physical properties form groups—for example, the variousmarginproperties—and we now take these into account when serializing styles and when modifying them from JavaScript. This improves both CSS fidelity and performance.

### Arbitrary substitution functions

This month we rewrote our implementations ofvar()andattr()to align with the formal definition ofarbitrary substitution functionsin recent CSS specs. These are functions that return a value to be substituted into the rule before parsing continues.

Our new implementation is more robust, more spec-compliant, and sets us up to support other substitution functions likeif()andenv()in the future.

### <syntax>parsing

CSS now allows authors to define the expected syntax for attribute values using the<syntax>type. This is used withinattr()to guide how the value should be parsed.

For example:

color: attr(
data-color
 type(<color
>
));

This instructs the parser to interpret thedata-colorattribute as a CSS color. Ladybird now supports<syntax>parsing and uses it to improve behavior in CSS Houdini and custom properties.

### @propertyprogress

We’ve had a stub implementation of@propertyfor a while. This month, we started fleshing it out.

We now respect the initial value defined in a@propertydeclaration and added initial support forCSS.registerProperty(). This brings us closer to full Houdini support.

### The Web is UTF-16

By definition, strings in JavaScript and the web areUTF-16 encoded. Until now, LibJS used UTF-8 internally and transcoded to UTF-16 on the fly.

This month, we introduced a native UTF-16 string type and began transitioning LibJS and LibWeb to use it internally. This simplifies the implementation and avoids subtle encoding-related bugs, especially with Unicode edge cases.

### Credits

We’d like to thank everyone who contributed code this month:

Abhinav, Ali Mohammad Pur, Aliaksandr Kalenik, Andreas Kling, Andrew Kaster, aplefull, Arran Ireland, ayeteadoe, Ben Eidson, Callum Law, Chase Knowlden, dmaivel, edvwib, Gingeh, Glenn Skrzypczak, Grant Knowlton, InvalidUsernameException, Jan Koudijs, Jelle Raaijmakers, Kemal Zebari, Kenneth Myhra, Lucien Fiorini, Luke Wilde, Manuel Zahariev, Michael Manganiello, mikiubo, norbiros, Olekoop, Philipp Dreher, Psychpsyo, rmgx, Rocco Corsi, Ryan Liptak, Sam Atkins, Shannon Booth, Tete17, Tim Ledbetter, Timothy Flynn, Trey Shaffer, Undefine, Veeti Paananen, zac
