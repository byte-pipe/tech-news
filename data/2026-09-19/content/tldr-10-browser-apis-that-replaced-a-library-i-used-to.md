---
title: 10 browser APIs that replaced a library I used to install
url: https://flaviocopes.com/browser-apis-replacing-libraries
site_name: tldr
content_file: tldr-10-browser-apis-that-replaced-a-library-i-used-to
fetched_at: '2026-09-19T14:10:49.216562'
original_url: https://flaviocopes.com/browser-apis-replacing-libraries
date: '2026-09-19'
published_date: '2026-09-19T10:00:00.000Z'
description: 'Ten browser APIs that replace npm packages and jQuery plugins: dialog, popover, view transitions, structuredClone, groupBy, Temporal, with 2026 support notes.'
tags:
- tldr
---

~~~

Here are ten things browsers do on their own today that used to cost us an npm package or a jQuery plugin. For each one I name the library it replaced, show the shortest example that works, and tell you where browser support stands as of September 2026, checked against MDN’s compatibility data and the Baseline status.

Some of those libraries were mine. In 2013 I wrote thatjQuery was everywhere and I used it. In 2018 I wrotea Moment.js tutorial. Both posts are still on this site, and both describe problems the browser now solves without a dependency.

I ordered the list by how much it saves you. Temporal closes it because it’s the biggest win and also the one not shipping everywhere yet, and I say exactly which browsers have it.

## 1. Intersection Observer

For years, lazy loading images meant installinglazysizesorlozad.lazysizeslistened to scroll events, measured elements withgetBoundingClientRect()on every scroll, and swapped adata-srcattribute intosrcwhen the image got close to the viewport. It worked, and it ran your code on every scroll frame.lozadcame later and was already a thin wrapper around the API in this section.

Intersection Observermoves that work into the browser. You describe which elements you care about, and the browser calls you when they enter or leave the viewport. No scroll listener, no layout measurement in your code.

The lazy loading pattern becomes this:

const
 observer
 =
 new
 IntersectionObserver
((
entries
) 
=>
 {

 for
 (
const
 entry
 of
 entries) {

 if
 (
!
entry.isIntersecting) 
continue

 entry.target.src 
=
 entry.target.dataset.src

 observer.
unobserve
(entry.target)

 }

})

document.
querySelectorAll
(
'img[data-src]'
).
forEach
((
img
) 
=>
 {

 observer.
observe
(img)

})

For plain images you don’t even need this much. When I moved my ebooks to very long pages and the hosting bill went up, I fixed it with theloading="lazy"attribute andone Hugo template. The observer is for everything the attribute can’t do: infinite scroll, “start the animation when the section is visible”, analytics for which parts of a page people reach. The demo page of mytte.jslibrary uses it to restart each text animation when its section scrolls into view.

Its siblingsResizeObserver and MutationObserverreplaced the element-resize and DOM-watching plugins the same way.

The gotcha: the callback runs once right afterobserve(), with the current state of the element. If an image is off screen, you get an entry withisIntersecting: falsebefore the user ever scrolls, which is what thecontinuein the example handles.

Support: every browser you target has had it since Safari 12.1, and it has been Baseline widely available since 2021.lozadhad its last release in 2020 andlazysizesin 2021.

## 2. The dialog element

A modal used to be adiv, some CSS to dim the page, and a library likemicromodalor the jQuery UI dialog widget to handle the parts nobody wants to write: trapping focus inside the box, closing on Escape, blocking clicks on the page behind it, and putting the box above everything else.

The<dialog>elementdoes all of that:

<
dialog
 id
=
"newsletter"
>

 <
form
 method
=
"dialog"
>

 <
p
>Get the JavaScript Handbook by email.</
p
>

 <
button
>Close</
button
>

 </
form
>

</
dialog
>

<
button
 id
=
"open"
>Subscribe</
button
>

<
script
>

 const
 dialog
 =
 document.
querySelector
(
'#newsletter'
)

 document.
querySelector
(
'#open'
).
addEventListener
(
'click'
, () 
=>
 {

 dialog.
showModal
()

 })

</
script
>

showModal()opens it in the top layer, adds a backdrop you can style withdialog::backdrop, traps focus, and makes the rest of the page inert. Escape closes it. A form withmethod="dialog"closes it on submit, so the close button needs no JavaScript.

The gotcha is the difference betweenshow()andshowModal(). OnlyshowModal()gives you the backdrop and the focus trap. And clicking outside the box does not close it by default. Theclosedby="any"attribute adds that, but it’s in Chrome 134 and Firefox 141 only, not in a stable Safari as of September 2026. If you need click-outside-to-close everywhere, keep a small click handler on the dialog.

Support: Chrome 37, Firefox 98, Safari 15.4. Baseline widely available since September 2024.

## 3. The Popover API

Tooltips and dropdown menus were the reason many of us installedtippy.js, which sat on top ofpopper.js, which later became Floating UI. The libraries did two jobs: show and hide the element with the right dismissal rules, and position it next to its trigger.

ThePopover APItakes the first job. Two attributes and no JavaScript:

<
button
 popovertarget
=
"share-menu"
>Share</
button
>

<
div
 id
=
"share-menu"
 popover
>

 <
a
 href
=
"https://x.com/intent/post?url=https://flaviocopes.com"
>Post on X</
a
>

 <
a
 href
=
"https://news.ycombinator.com/submitlink?u=https://flaviocopes.com"
>Submit to HN</
a
>

</
div
>

Clicking the button toggles the menu. Clicking anywhere else, or pressing Escape, closes it. That’s the light dismiss behavior every menu library implemented by hand with a document-level click listener. The popover also renders in the top layer, so it never loses az-indexfight with a sticky header. From code you haveshowPopover(),hidePopover()andtogglePopover(), and atoggleevent fires on every change.

The gotcha is the second job, because the Popover API does not position anything. By default a popover appears in the center of the viewport (the browser styles it withinset: 0andmargin: auto), not next to the button. Placing it beside its trigger is the job of CSS anchor positioning, which is not Baseline yet as of September 2026, so you either write the positioning CSS yourself or keep Floating UI for the math and let the browser handle showing and hiding. Thepopover="hint"value for tooltips that don’t close other popovers is also new, Chrome 151 and Firefox 153 only.

Support: Chrome 114, Firefox 125, Safari 17. Baseline newly available since January 2025.tippy.jshad its last release in November 2021.

## 4. The View Transitions API

Animating between pages on a server-rendered site meantbarba.jsorswup. They intercept every link click, fetch the next page overfetch(), swap the content into the current document, and animate the swap. You get smooth transitions and a router you didn’t ask for, with its own rules for scripts, scroll position and analytics.

TheView Transitions APIdoes the animation part in the browser. For changes inside one page you wrap the DOM update in a call:

document.
startViewTransition
(() 
=>
 {

 list.
prepend
(newItem)

})

The browser takes a snapshot before the update, runs your callback, takes another snapshot, and cross-fades between the two. You customize the animation with CSS on::view-transition-old(root)and::view-transition-new(root), and elements with aview-transition-nameget their own morphing animation.

For real page-to-page navigation, the part barba.js existed for, you opt in with one CSS rule on both pages:

@view-transition
 {

 navigation: auto;

}

There is no router and no intercepted click here. The browser does a normal navigation and animates between the old and the new document. Astro wraps the same API in its<ClientRouter />component if you want to control it from a framework.

The gotcha is support, and it splits in two. Same-document transitions (startViewTransition()) are in Chrome 111, Safari 18 and Firefox 144, and became Baseline newly available in October 2025. Cross-document transitions (the@view-transitionrule) are in Chrome 126 and Safari 18.2, and Firefox does not ship them as of September 2026. Firefox users get a plain navigation, which is a fine fallback, but if the transition is central to your design you still need a library there.

## 5. AbortController, and fetch with it

fetch()itself replaced$.ajax()and most of whataxioswas installed for.I use fetch directly in most of my projects. For its first years it had no way to cancel a request, and that alone kept axios installed in a lot of codebases.

AbortControllerclosed that gap:

const
 controller
 =
 new
 AbortController
()

fetch
(
'https://api.github.com/repos/flaviocopes/tte-js'
, {

 signal: controller.signal,

})

controller.
abort
()

The promise rejects with an error whosenameisAbortError. For the most common case, a hard time limit, you don’t even need a controller:

const
 response
 =
 await
 fetch
(
'https://flaviocopes.com/rss.xml'
, {

 signal: AbortSignal.
timeout
(
5000
),

})

I used exactly that inPort Pilot, a tool that probes local ports on my Mac. Some ports accept a connection and never answer with HTTP, so every probe gets 450 milliseconds and then moves on. Without the abort, one stuck service slowed the whole scan.

The same signal works withaddEventListener(), so oneabort()removes every listener you registered with it, andAbortSignal.any()combines a user cancel and a timeout into one signal. Axios itself now documents its cancel tokens as deprecated and accepts anAbortSignalinstead.

The gotcha: a timeout rejects withTimeoutError, notAbortError, so checkerror.nameif you treat them differently. And aborting stops your code from waiting. If the request already reached the server, the server still processes it.

Support: AbortController has been Baseline widely available since 2021 (Chrome 66, Firefox 57, Safari 12.1).AbortSignal.timeout()is newer, Chrome 124, Firefox 100, Safari 16, Baseline newly available since April 2024.

## 6. structuredClone()

Deep copying an object was the number one reason to install lodash, forcloneDeep, orrfdcif you cared about speed. Many of us installed nothing and wroteJSON.parse(JSON.stringify(obj)), hoping the object had no dates in it.

structuredClone()is built in:

const
 order
 =
 {

 id: 
1
,

 items: [{ sku: 
'javascript-handbook'
, qty: 
1
 }],

 created: 
new
 Date
(),

}

const
 copy
 =
 structuredClone
(order)

copy.items[
0
].qty 
=
 2

order.items[
0
].qty 
//1

copy.created 
instanceof
 Date
 //true

It uses the same algorithm the browser uses to pass data to a Web Worker or store it in IndexedDB. Nested arrays and objects are copied, and unlike the JSON trick it keepsDate,Map,Set,RegExp, typed arrays andundefinedvalues intact, and it handles circular references.

TheTailwind theme generatoron this site clones a default state object every time you reset or pick a preset, so editing the current theme never touches the defaults.

The gotcha: it throws aDataCloneErrorif the object contains a function or a symbol, and class instances come back as plain objects. Methods are gone andcopy instanceof Cartisfalse. If your data has behavior attached, you still need a copy method of your own.lodash.cloneDeepcopied functions by reference and kept prototypes, so code that relied on that breaks when you swap it.

Support: Chrome 98, Firefox 94, Safari 15.4, Node.js 17. Baseline widely available since September 2024.

## 7. Object.groupBy()

Grouping an array by a key was the second reason many of us installed lodash._.groupBy(posts, 'tag')was one line, and writing thereduce()by hand every time was tedious enough to justify the dependency.

Object.groupBy()is the built-in version:

const
 posts
 =
 [

 { title: 
'The Fetch API'
, tag: 
'js'
 },

 { title: 
'CSS Grid'
, tag: 
'css'
 },

 { title: 
'Arrow functions'
, tag: 
'js'
 },

]

const
 byTag
 =
 Object.
groupBy
(posts, (
post
) 
=>
 post.tag)

byTag.js.
length
 //2

Object.
keys
(byTag) 
//['js', 'css']

The callback returns the group key for each item, and you get one property per group.Map.groupBy()does the same and returns aMap, which is what you want when the key is an object or when you need to preserve key types.

The gotcha comes from the return value. It’s a null-prototype object, sobyTag.hasOwnProperty('js')throws aTypeError, because there is nohasOwnPropertyto call. UseObject.hasOwn(byTag, 'js')or'js' in byTag. The keys are also coerced to strings, like every property key, so grouping by a numeric year gives you'2018', and a group that doesn’t exist isundefined, which makesbyTag.php.lengththrow. Lodash had the same shape, minus the prototype detail.

Support: Chrome 117, Firefox 119, Safari 17.4. It became Baseline widely available on September 5, 2026.

## 8. toSorted(), toReversed(), toSpliced() and with()

sort()andreverse()mutate the array in place, and that bit everyone at least once, usually inside a React component where the sorted list was also the state. The workarounds were[...items].sort(), or lodash’ssortBy()which returns a new array, or a helper library likeimmutability-helper.

Thefour copying methodsreturn a new array and leave the original alone:

const
 prices
 =
 [
29
, 
9
, 
49
]

const
 sorted
 =
 prices.
toSorted
((
a
, 
b
) 
=>
 a 
-
 b)

prices 
//[29, 9, 49]

sorted 
//[9, 29, 49]

toReversed()is the copying version ofreverse(),toSpliced()ofsplice(), andwith(index, value)replaces one item and returns the new array:

prices.
with
(
1
, 
10
) 
//[29, 10, 49]

The gotcha is inherited fromsort().toSorted()without a comparator sorts as strings, so[29, 9, 49].toSorted()gives[29, 49, 9]. Always pass a comparator for numbers. Andwith()is stricter than assignment:prices.with(5, 1)throws aRangeError, whereprices[5] = 1would have grown the array with empty slots. There is notoPushed()ortoShifted()either, so for those you still spread into a new array.

Support: Chrome 110, Firefox 115, Safari 16. Baseline widely available since January 2026.

## 9. Web Crypto

Hashing a string or signing a token in the browser used to meancrypto-js. Its own README now opens with a “Discontinued” section and points you to the nativeCryptomodule, and its last release was 4.2.0 in October 2023. On the server,jsonwebtokenwraps Node’scryptofor the same HMAC step.

crypto.subtledoes the work in every modern browser and in Node.js. Signing an HS256 JWT, the partjsonwebtokendoes for you, is a key import and onesign()call:

const
 encoder
 =
 new
 TextEncoder
()

const
 key
 =
 await
 crypto.subtle.
importKey
(

 'raw'
,

 encoder.
encode
(
'a-long-random-secret-from-your-env'
),

 { name: 
'HMAC'
, hash: 
'SHA-256'
 },

 false
,

 [
'sign'
]

)

const
 signature
 =
 await
 crypto.subtle.
sign
(

 'HMAC'
,

 key,

 encoder.
encode
(
`${
header
}.${
payload
}`
)

)

signatureis anArrayBufferof 32 bytes. Base64url-encode it, append it toheader.payload, and you have the token. The whole flow, including why verifying must never trust thealgin the header, is inhow JWT signing actually works, and theJWT signer toolon this site runs this code in your browser.

Hashing is shorter:

const
 digest
 =
 await
 crypto.subtle.
digest
(
'SHA-256'
, encoder.
encode
(
'hello'
))

const
 hex
 =
 [
...new
 Uint8Array
(digest)]

 .
map
((
b
) 
=>
 b.
toString
(
16
).
padStart
(
2
, 
'0'
))

 .
join
(
''
)

Because the same API exists on Cloudflare Workers, the webhook that handles course purchases on this site verifies Paddle’s RSA signature withcrypto.subtle.verify(), and the form endpoints hash visitor IPs withdigest()before using them as rate-limit keys.

The gotcha:crypto.subtleis only available in a secure context, so HTTPS orlocalhost. On a plainhttp://page it’sundefined. Everything is async and returnsArrayBuffer, so you write the hex and base64url helpers yourself. And there is no MD5, asking for it throwsNotSupportedError.

Support: Chrome 37, Firefox 34, Safari 11. Baseline widely available since 2020.

## 10. Temporal

Dates are why Moment.js got installed everywhere, and why so many projects still carrymoment,dayjsordate-fns.Dateonly knows the system time zone and UTC, mutates in place, counts months from zero, and parses non-ISO strings differently across engines.

Temporalis the replacement built into the language. Every value is immutable, calendar dates and exact instants are different types, and time zones are first class:

const
 launch
 =
 Temporal.PlainDate.
from
(
'2026-09-19'
)

launch.
add
({ weeks: 
1
 }).
toString
() 
//'2026-09-26'

const
 rome
 =
 Temporal.Now.
zonedDateTimeISO
(
'Europe/Rome'
)

rome.timeZoneId 
//'Europe/Rome'

Differences come out as aDurationyou can ask for in the unit you need:

const
 start
 =
 Temporal.PlainDate.
from
(
'2026-08-10'
)

const
 end
 =
 Temporal.PlainDate.
from
(
'2026-09-17'
)

end.
since
(start).days 
//38

start.
until
(end, { largestUnit: 
'months'
 }).
toString
() 
//'P1M7D'

Moment’s other big feature, “3 days ago”, was already replaced byIntl.RelativeTimeFormat, which has been in every browser since Safari 14 in 2020. I cover it in theJavaScript internationalizationpost.

Support is where Temporal differs from everything above. As of September 2026 it ships in Firefox since version 139 (May 2025) and in Chrome since version 144 (January 2026), while Safari has it in Safari Technology Preview only, with no stable release. That means Temporal is not Baseline, and a public web app still needs@js-temporal/polyfill, which is at version 0.5.x and not small, because it carries the calendar and time zone logic. Outside the browser, Node.js 26 enables Temporal by default and Deno has it since 2.7, so a script that only runs there needs no polyfill. One caveat from my own machine: the Homebrew build of Node 26 I have installed was compiled without it, so checktypeof Temporalbefore you rely on it.

Moment’s own documentation calls it a legacy project in maintenance mode. Day.js and date-fns are still maintained and still fine. Temporal puts the same model in the language itself, and the polyfill goes away the day Safari ships it.

One more gotcha:Temporal.PlainDate.from()accepts a properties object or an RFC 9557 string, which is the ISO 8601 format with optional annotations. Moment’s forgiving parser that accepted almost anything is gone on purpose. Validate user input first, then build the Temporal value.

## Before you install the next one

Check Baseline before reaching for npm. MDN shows the status at the top of every API page, and theweb-featurespackage on npm has the same data in JSON if you want it in a script. That’s the data I used for every support line in this post.

Widely available means every engine has shipped it for at least 30 months, and you can drop the library. Newly available means all three engines have it but older versions are still around, so look at your own traffic before deciding. With limited availability, like Temporal today, the library or the polyfill stays, and you write the code against the standard API so that removing it later means deleting an import.

If you want the fundamentals behind these examples, arrays, objects, promises and the DOM, the freeJavaScript coursecovers them in order.

Tagged: 
JavaScript
 · 
All topics
Follow @flaviocopes

Want me to talk about your product? You cansponsor this site.

~~~

Related posts about js:

* What happens when Bun runs a TypeScript file
* How to group array items with Object.groupBy()
* JavaScript immutable array methods: toSorted(), toReversed(), toSpliced(), with()
* AbortController: how to cancel a fetch request in JavaScript
* WebAssembly tutorial
* A deep dive into Hono
* Hono: middleware, cookies, headers, redirects
* Hono: a modern web framework for JavaScript