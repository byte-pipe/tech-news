---
title: 'Temporal: The 9-Year Journey to Fix Time in JavaScript | Bloomberg JS Blog'
url: https://bloomberg.github.io/js-blog/post/temporal/
site_name: hackernews_api
content_file: hackernews_api-temporal-the-9-year-journey-to-fix-time-in-javascr
fetched_at: '2026-03-11T19:21:28.895721'
original_url: https://bloomberg.github.io/js-blog/post/temporal/
author: robpalmer
date: '2026-03-11'
published_date: '2026-03-11'
description: JavaScript&#39;s Date object has been a source of bugs for three decades. Temporal, which just reached Stage 4, is a modern replacement with immutable types, first-class time zone and calendar support, and nanosecond precision. This is the story of how Bloomberg, Igalia, and the TC39 community spent nine years turning an idea into a shipping standard.
tags:
- hackernews
- trending
---

# Temporal: The 9-Year Journey to Fix Time in JavaScript

	Published on
11 March 2026

Welcome to our blog! I'm Jason Williams, a senior software engineer on Bloomberg's JavaScript Infrastructure and Terminal Experience team. Today the Bloomberg Terminal runsa lot of JavaScript. Our team providesa JavaScript environmentto engineers across the company.

Bloomberg may not be the first company you think of when discussing JavaScript. It certainly wasn't for me in 2018 before I worked here. Back then, I attended my firstTC39meeting in London, only to meet some Bloomberg engineers who were there discussing Realms, WebAssembly, Class Fields, andother topics. The company has now been involved with JavaScript standardization for numerous years, including partnering with Igalia. Some of the proposals we have assisted includeArrow Functions, Async Await, BigInt, Class Fields, Promise.allSettled, Promise.withResolvers, WeakRefs,standardizing Source Maps, and more!

The first proposal I worked on wasPromise.allSettled, which was fulfilling. After that finished, I decided to help out on a proposal around dates and times, called Temporal.

## How Does JavaScript Change?#

JavaScript is unique in that it runs in all browsers. There is no single "owner," so you can't just make a change in isolation and expect it to apply everywhere. You need buy-in from all parties. Evolution happens throughTC39, the Technical Committee responsible for ECMAScript.

Proposals move through a series ofmaturity stages:

* Stage 0 - Idea
* Stage 1 - Problem space accepted
* Stage 2 - Draft design chosen, but work to continue
* Stage 2.7 - Proposal approved in principle; awaiting testing and feedback
* Stage 3 - Implementation and feedback
* Stage 4 - Standardized

In 2018, when I first looked at Temporal, it was at Stage 1. The TC39 Committee was convinced the problem was real. It was a radical proposal to bring a whole new library for Dates and Times into JavaScript. It was:

* A replacement for Date
* Providing different DateTime Types (instead of a single API)
* Immutable
* Adding first-class time zone and calendar support

But how did we get here? Why was Date such a pain point? For that, we need to take a step back.

## A Product of Its Time#

In 1995, Brendan Eich was tasked with a 10-day sprint to create Mocha (which would later become JavaScript). Under intense time pressure, many design decisions were pragmatic. One of them was to port Java's Date implementation directly. As Brendan later explained:

It was a straight port by Ken Smith (the only code in "Mocha" I didn't write) of Java's Date code from Java to C.

At the time, this made sense. Java was ascendant and JavaScript was being framed as its lightweight companion. Internally, the philosophy was even referred to asMILLJ: Make It Look Like Java.

Brendanalso notedthat changing the API would have been politically difficult:

Changing it when everyone expected Java to be the "big brother" language would make confusion and bugs; Sun would have objected too.

In that moment, consistency with Java was more important than fundamentally rethinking the time model. It was a pragmatic trade-off. The Web was young, and most applications making use of JavaScript would be simple, at least, to begin with.

## The Web Grew Up, Date Didn't#

By the 2010s, JavaScript was powering banking systems, trading terminals, collaboration tools, and other complex systems running in every time zone on earth. Date was becoming more of a pain point for developers.

### Mutability#

Developers would often write helper functions that accidently mutated the original Date object in place when they intended to return a new one:

const
 date
=

new

Date
(
"2026-02-25T00:00:00Z"
)
;

console
.
log
(
date
.
toISOString
(
)
)
;

// "2026-02-25T00:00:00.000Z"

function

addOneDay
(
d
)

{


// oops! This is mutating the date

 d
.
setDate
(
d
.
getDate
(
)

+

1
)
;


return
 d
;

}

addOneDay
(
date
)
;

console
.
log
(
date
.
toISOString
(
)
)
;

// "2026-02-26T00:00:00.000Z"

### Inconsistent Month Arithmetic#

const
 billingDate
=

new

Date
(
"Sat Jan 31 2026"
)
;

billingDate
.
setMonth
(
billingDate
.
getMonth
(
)

+

1
)
;

// Expected: Feb 28

// Actual: Mar 02

Sometimes people want to get the last day of the month and fall into traps like this one, where they bump the month by one, but the days remain the same. Date does not constrain invalid calendar results back into a valid date. Instead, it silently rolls overflow into the next month.

### Ambiguous Parsing#

new

Date
(
"2026-06-25 15:15:00"
)
.
toISOString
(
)
;

// Potential Return Values:

// - local TimeZone

// - Invalid Date RangeError

// - UTC

In this example, the string is similar, but not identical, to ISO 8601. Historically, browser behavior for "almost ISO" strings wasundefined by the specification. Some would treat it as local time, others as UTC, and one would throw entirely as invalid input.

There's more,much more, but the point is that Date has been a pain point for JavaScript developers for the past three decades.

## The Library Era#

The Web ecosystem had no choice but to patch Date's shortcomings with libraries. You can see the sheer rise of datetime libraries below. Today, they add up to more than 100 million downloads a week.

Leading the charge wasMoment.js, which boasts an expressive API, powerful parsing capabilities, and much-needed immutability. Created in 2011, it quickly became the de facto standard for handling date and time manipulations in JavaScript. So surely the problem is solved? Everyone should just grab a copy of this and call it a day.

The widespread adoption of moment.js (plus other similar libraries) came with its own set of problems. Adding the library meant increasing bundle size, due to the fact that it needed to be shipped with its own set of locale information plus time zone data from the time zone database.

Despite the use of minifiers, compilers, and static analysis tools, all of this extra data couldn't be tree-shaken away, because most developers don't know ahead of time which locales or time zones they'll need. In order to play it safe, the majority of users took all of the data wholesale and shipped it to their users.

Maggie Johnson-Pint, who had been a maintainer of Moment.js for quite a few years (alongside others), was no stranger to requests to deal with the package size.

We were at the point with moment that it was more maintenance to keep up with modules, webpack, people wanting everything immutable because React, etc than any net new functionality

And people never stop talking about the size of course.

In 2017, Maggie decided it was time to standardise dates and times with a "Temporal Proposal" for the TC39 plenary that year. It was met with great enthusiasm, leading it to be advanced to Stage 1.

## The Champions Assemble#

Stage 1was a big milestone, but it was still far from the finish line. After the initial burst of energy, progress naturally slowed. Maggie and Matt Johnson-Pint were leading the effort alongsideBrian Terlson, while simultaneously balancing other responsibilities inside Microsoft. Temporal was still early enough that much of the immediate work was unglamorous: requirements gathering, clarifying semantics, and translating "the ecosystem's pain" into a design that could actually ship.

At Bloomberg, that pain wasn't theoretical.

We run JavaScript at scale across the Terminal, using underlying runtimes and engines such asChromium, Node.jsandSpiderMonkey. Our users, and the financial markets in which they invest, span every time zone on earth. We pass timestamps constantly: between services, into storage, into the UI, and across systems that all have to agree on what "now" means, evenwhen governments change DST rules with very little notice.

On top of that, we had requirements that the built-in Date model simply wasn't designed for:

* A user-configured time zonethat is not the machine's time zone (and can change per request).
* Correct historical time zone behaviordriven by IANA Time Zone Database (tzdata) updates.
* Higher-precision timestamps(nanoseconds, at a minimum), without duct-taping extra fields onto ad-hoc wrappers forever.

In parallel with Maggie bringing Temporal to TC39, Bloomberg engineerAndrew Paprockiwas talking with Igalia about making time zones configurable in V8. Specifically, they discussed introducing a supported indirection layer so an embedder could control the "perceived" time zone instead of relying on the OS default. In that conversation,Daniel Ehrenberg(then working at Igalia) pointed Andrew at the early Temporal work because it looked strikingly similar to Bloomberg's existing value-semantic datetime types.

That exchange became an early bridge between Bloomberg's production needs, Igalia's browser-and-standards expertise, and the emerging direction of Temporal. Over the years that followed, Bloomberg partnered with Igalia (including via sustained funding support) and contributed engineering time directly into moving Temporal forward, until it eventually became something the whole ecosystem could ship. Andrew was looking for some volunteers within Bloomberg who could help push Temporal forward andPhilipp Dunkelvolunteered to be a spec champion. Alongside Andrew, he helped persuade Bloomberg to invest in making Temporal real, including a deeper partnership with Igalia. That support brought inPhilip ChimentoandUjjwal Sharmaas full time Temporal champions, adding the day-to-day focus the proposal needed to keep moving ahead.

Shane Carr joined the Champions team, representing Google's Internationalization team. He provided the focus we needed on internationalization topics such as calendars, and also served as the glue between the standardization process and the voice of users who experienced pain points with tools related to JavaScript's internationalization API (Intl), such as formatting, time zones, and calendars.

Finally, we had Justin Grant, an invited expert who had experience with iCalender and various other projects that required the use of dates and times. Other honorable mentions not on this list include Daniel Ehrenberg, Adam Shaw, and Kevin Ness.

### The Current & Past Champions of Temporal#

* Maggie Johnson-Pint (Microsoft)
* Matt Johnson-Pint (Microsoft)
* Brian Terlson (Microsoft)
* Richard Gibson (Agoric)
* Philipp Dunkel (Bloomberg)
* Ujjwal Sharma (Igalia)
* Philip Chimento (Igalia)
* Jason Williams (Bloomberg)
* Shane Carr (Google)
* Justin Grant (Invited Expert)

## How Temporal Looks Today#

Temporal is a top-level namespace object (similar to Math or Intl) that exists in the global scope. Underneath it are "types" that exist in the form of constructors. It's expected that developers will reach for the type they need when using the API, such asTemporal.PlainDateTime, for example.

Here are the types Temporal comes packed with:

### Temporal.ZonedDateTime#

If you don't know which Temporal type you need, start withTemporal.ZonedDateTime.
It is the closest conceptual replacement forDate, but without the "footguns."

Date represents:

* An exact moment in time (internally, milliseconds since epoch)
* Interpreted through the machine's current time zone
* With implicit, mutable behavior

Temporal.ZonedDateTime represents:

* An exact moment in time
* With an explicit time zone
* With an explicit calendar
* And full daylight-saving correctness
* All as an immutable value

If you're currently writing:

const
 now
=

new

Date
(
)
;

The Temporal equivalent is:

const
 now
=
 Temporal
.
Now
.
zonedDateTimeISO
(
)
;

The above example uses the Now namespace, which gives you the type already set to your current local time and time zone.

This type is optimized for DateTimes that may require some datetime arithmetic in which the daylight saving transition could potentially cause problems.ZonedDateTimecan take those transitions into account when doing any addition or subtraction of time (see example below).

// London DST starts: 2026-03-29 01:00 -> 02:00

const
 zdt
=
 Temporal
.
ZonedDateTime
.
from
(


"2026-03-29T00:30:00+00:00[Europe/London]"
,

)
;

console
.
log
(
zdt
.
toString
(
)
)
;

// → "2026-03-29T00:30:00+00:00[Europe/London]"

const
 plus1h
=
 zdt
.
add
(
{

hours
:

1

}
)
;

console
.
log
(
plus1h
.
toString
(
)
)
;

// "2026-03-29T02:30:00+01:00[Europe/London]" (01:30 doesn't exist)

In this example, we don't land at01:30but02:30instead, because01:30doesn't exist at that specific point in time.

### Temporal.Instant#

Temporal.Instantis an exact moment in time, it has no time zone, no daylight saving, no calendar. It represents elapsed time since midnight on January 1, 1970 (theUnix epoch). UnlikeDate, which has a very similar data model,Instantis measured in nanoseconds rather than milliseconds. This decision was taken by the champions because even though the browser has some coarsening forsecurity purposes, developers still need to deal with nanosecond-based timestamps that could have been generated from elsewhere.

A typical example ofTemporal.Instantusage looks like this:

// One exact moment in time

const
 instant
=
 Temporal
.
Instant
.
from
(
"2026-02-25T15:15:00Z"
)
;

instant
.
toString
(
)
;

// "2026-02-25T15:15:00Z"

instant
.
toZonedDateTimeISO
(
"Europe/London"
)
.
toString
(
)
;

// "2026-02-25T15:15:00+00:00[Europe/London]"

instant
.
toZonedDateTimeISO
(
"America/New_York"
)
.
toString
(
)
;

// "2026-02-25T10:15:00-05:00[America/New_York]"

TheInstantcan be created and then converted to different "zoned" DateTimes (more on that later). You would most likely store theInstant(in your backing storage of choice) and then use the different TimeZone conversions to display the same time to users within their time zones.

### Temporal.[PlainDate, PlainTime, PlainDateTime, PlainYearMonth, PlainMonthDay]#

We also have a family of plain types. These are what we would call "wall time," because if you imagine an analogue clock on the wall, it doesn't check for daylight saving or time zones. It's just a plain time (moving the clock forward by an hour would advance it an hour on the wall, even if you did this during a Daylight Saving transition).

We have several types with progressively less information. This is useful, as you can choose the type you want to represent and don't need to worry about running calculations on any other un-needed data (such as calculating the time if you're only interested in displaying the date).

These types are also useful if you only plan to display the value to the user and do not need to perform any date/time arithmetic, such as moving forwards or backwards by weeks (you will need a calendar) or hours (you could end up crossing a daylight saving boundary). The limitations of some of these types are also what make them so useful. It's hard for you to trip up and encounter unexpected bugs.

const
 date
=
 Temporal
.
PlainDate
.
from
(
{

year
:

2026
,

month
:

3
,

day
:

11

}
)
;

// => 2026-03-11

date
.
year
;

// => 2026

date
.
inLeapYear
;

// => false

date
.
toString
(
)
;

// => '2026-03-11'

### Calendars#

Temporal supports calendars. Browsers and runtimes ship with a set ofbuilt-in calendars, which lets you represent, display, and do arithmetic in a user's preferred calendar system, not just format a Gregorian date differently.

Because Temporal objects are calendar-aware, operations like "add one month" are performedin the rules of that calendar, so you land on the expected result. In the example below, we add one Hebrew month to a Hebrew calendar date:

const
 today
=
 Temporal
.
PlainDate
.
from
(
"2026-03-11[u-ca=hebrew]"
)
;

today
.
toLocaleString
(
"en"
,

{

calendar
:

"hebrew"

}
)
;

// '22 Adar 5786'

const
 nextMonth
=
 today
.
add
(
{

months
:

1

}
)
;

nextMonth
.
toLocaleString
(
"en"
,

{

calendar
:

"hebrew"

}
)
;

// '22 Nisan 5786'

With legacyDate, there's no way to express "add one Hebrew month" as a first-class operation. You canformatusing a different calendar, but any arithmetic you do is still Gregorian month arithmetic under the hood.

If you tried to approximate this withDate, it might look like:

const
 legacyDate
=

new

Date
(
2026
,

2
,

11
)
;

legacyDate
.
toLocaleDateString
(
"en"
,

{

calendar
:

"hebrew"

}
)
;

// '22 Adar 5786'

legacyDate
.
setMonth
(
legacyDate
.
getMonth
(
)

+

1
)
;

legacyDate
.
toLocaleDateString
(
"en"
,

{

calendar
:

"hebrew"

}
)
;

// '24 Nisan 5786'

This adds oneGregorianmonth (March → April). When you thendisplaythe result in the Hebrew calendar, you land on a different day,24 Nisanrather than22 Nisan, because the calendars don't have the same month structure or month lengths.

### Temporal.Duration#

Our final type isTemporal.Duration.Durationis straightforward and can be used with any of the other types when adding and subtracting. Another useful feature ofDurationis showing it in different units, like the example below:

const
 duration
=
 Temporal
.
Duration
.
from
(
{


hours
:

130
,


minutes
:

20
,

}
)
;

duration
.
total
(
{

unit
:

"second"

}
)
;

// => 469200

Most datetime libraries already have a duration type, so it made sense to include one. It also complements the other types by allowing the developer to compare Times or DateTimes and getting back aDurationtype.

## Implementation#

Implementing Temporal was a challenge. It is a very large proposal that brings more changes to JavaScript than any other proposal in the programming language's history. Some specific challenges include:

* This GIANT spec is bigger than all of ECMA-402 (The Internationalization spec); this made it hard (but not impossible) for a single person to implement
* The volatility of the spec created a moving target. There have been changes to the spec over the years, which meant implementations have struggled to keep up.
* Browsers demand that nearly all aspects are efficient and performant.

Temporal is the biggest addition to ECMAScript since ES2015

Whilst Firefox was able to implement Temporal as it was being specced - thanks to the great work of André Bargull (known online as Anba) - not all browsers or engines were able to work on Temporal during its earlier stages. This means that a lot of catch-up was needed by the later parts of Stage 3.

Temporal, by the number of tests added to the official test suite for ECMAScript (Test262), is the biggest addition to the ECMAScript spec. Temporal today has ~4,500 tests, a high number compared to some of the other built-ins, including its predecessor, Date.

In the June 2024 plenary, the Google Internationalization team and Boa decided to collaborate on the implementation of Temporal and to work on a Rust library that could serve both engines. The library is calledtemporal_rs. Over the course of 2024 and 2025, it ramped up the implementation of Temporal thanks to the work of Kevin Ness, Manish Goregaokar, Jose Espina and students from the University of Bergen. Todaytemporal_rspasses 100% of all tests and now serves other engines outside of V8 and Boa!

temporal_rsis pretty unconventional. It's rare, if not unprecedented, for multiple engines to collaborate on a shared library to implement a TC39 proposal. Not only did this work, but also it was a huge success.temporal_rsmeant that there was:

* Reduced barrier to entry: The students and other collaborators didn't need to understand the V8 or Boa codebase to contribute to the library.
* Improved long-term maintenance:temporal_rshas a team of maintainers who will continue to work on the library even after Temporal has reached Stage 4. This provides developers with a stable location to raise issues, report bugs, or even contribute improvements themselves with engines as stakeholders.
* Higher quality code to review:Becausetemporal_rsis scoped as a library, it means that reviewing it was easier because you didn't need the context of a whole engine. Also the library uses modern Rust features, such as the built-in linting (Clippy), formatting (Rustfmt), and CI tests against engines.

## Shipped & Standardized#

Earlier today, Temporal reached Stage 4 in the TC39 staging process, which means it will be part of the next annual ECMAScript specification (ES2026). However, you don't need to wait until then - you can use it today!

Temporal is already supported across:

* Firefox v139 (since May 2025)
* Chrome v144 (since January 2026)
* Edge v144 (since January 2026)
* TypeScript 6.0 Beta (since February 2026)
* Safari (Partial Support in Technology Preview)
* Node.js v26 (TBC)

## What's Next?#

There's still plenty of work to do for Temporal, such as figuring outhow it integrates with the rest of the Web ecosystem. We've had years of Web APIs working with or around the Date object, and those same APIs must be compatible with Temporal objects too. Here are some examples:

### Integration With Date Pickers#

Developers will want to use Temporal with date pickers. Right now, that isn't possible (it may be possible to patch via a polyfill but there is nothing in the standard today). As we improve the ergonomics of using Temporal, we will need to add support in areas where Date is used today. One example is input types that are datetime related. See below:

<
input

type
=
"
date
"

/>

<!-- element.valueAsPlainDate -->

<
input

type
=
"
time
"

/>

<!-- element.valueAsPlainTime -->

<
input

type
=
"
week
"

/>

<!-- element.valueAsPlainDate -->

<
input

type
=
"
month
"

/>

<!-- element.valueAsPlainYearMonth -->

### Supplementing DOMHighResTimeStamp#

Due to Temporal Instants supporting time down to nanoseconds, they could be used anywhere aDOMHighResTimeStampis used. In the following example, we can use an Instant to set a cookie expiry, where normally we would have previously used aDOMHighResTimeStamp.

cookieStore
.
set
(
{


name
:

"foo"
,


value
:

"bar"
,


expires
:
 Temporal
.
Now
.
instant
(
)
.
add
(
{

hours
:

24

}
)
.
epochMilliseconds
,

}
)
;

And there's certainly more. What is certain is that the JavaScript community will continue working hard to bring Temporal not only to the Web platform, but also any other libraries that make use of Date today.

## A Better Time for JavaScript#

Temporal is the result of nearly a decade of work across companies, engines, and individuals. It represents:

* Years of consensus-building inside TC39 that was informed directly by the ecosystem's prior art
* Implementation work across multiple JavaScript engines
* Collaboration between Microsoft, Google, Mozilla, Bloomberg, Igalia, Boa, and many independent contributors
* And a rare example of shared infrastructure in the form of thetemporal_rslibrary

We are proud to have funded and supported Igalia's work on Temporal for many years. That investment, combined with open collaboration, successfully helped move the proposal from idea to specification to shipping reality.

The success oftemporal_rsdemonstrates something important: new language features don't have to mean duplicated effort across engines. Shared, high-quality open source infrastructure can reduce costs, increase consistency, and accelerate innovation across the Web ecosystem.

Temporal is not just a better API. It's proof that the JavaScript community can solve long-standing problems together.

After nearly 30 years, JavaScript finally has a modern datetime API.

And this time, we got it right.

Jason Williams

Jason Williams is a senior software engineer in the JavaScript Infrastructure & Terminal Experience organisation at Bloomberg, where he focuses on software performance across the Bloomberg Terminal and the Web. He is a TC39 delegate and has had previous experience with standardizing features, implementing the language and contributing to large open source projects. Jason is also the creator of the Boa JavaScript engine.

* Previous:Source Maps: Shipping Features Through Standards
