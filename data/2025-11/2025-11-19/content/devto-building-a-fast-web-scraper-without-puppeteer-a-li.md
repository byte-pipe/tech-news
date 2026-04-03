---
title: 'Building a Fast Web Scraper Without Puppeteer: A Live Coding Challenge - DEV Community'
url: https://dev.to/dilutedev/building-a-fast-web-scraper-without-puppeteer-a-live-coding-challenge-2apg
site_name: devto
fetched_at: '2025-11-19T11:07:13.544779'
original_url: https://dev.to/dilutedev/building-a-fast-web-scraper-without-puppeteer-a-live-coding-challenge-2apg
author: Isaac Sunday
date: '2025-11-17'
description: How I built a production-grade scraper for NC public notices using Cheerio and TLS fingerprinting... Tagged with typescript, webscraping, node, performance.
tags: '#typescript, #webscraping, #node, #performance'
---

How I built a production-grade scraper for NC public notices using Cheerio and TLS fingerprinting instead of headless browsers

## The Challenge

During a live coding interview, I was tasked with building a scraper forncnotices.com, a North Carolina public notices database. The catch? I had limited time and needed to handle a complex ASP.NET application with state management, pagination, and CAPTCHA protection.

The interviewer mentioned their team used Puppeteer for their existing scraper. I chose a different path.

## Why Not Puppeteer?

Don't get me wrong - Puppeteer is fantastic for many use cases. But for this task, it felt like bringing a tank to a knife fight:

* Resource overhead: Running a headless Chrome instance uses 100-200MB of RAM per instance
* Slower execution: Browser startup alone takes 1-2 seconds
* Complexity: Managing browser lifecycles, waiting for selectors, handling browser crashes

Since ncnotices.com renders server-side (classic ASP.NET), I didn't need JavaScript execution. I just needed to:

1. Parse HTML efficiently
2. Manage cookies and sessions
3. Bypass basic bot detection

## The Tech Stack

{


"
dependencies
"
:

{


"
cheerio
"
:

"
^1.1.2
"
,

// Fast HTML parsing


"
impit
"
:

"
^0.7.0
"
,

// TLS fingerprinting


"
tough-cookie
"
:

"
^6.0.0
"

// Cookie management


}

}

Enter fullscreen mode

Exit fullscreen mode

### Key Libraries

Cheerio: jQuery-like HTML parsing that's blazing fast. Perfect for server-rendered content.

Impit: The secret sauce. This library mimics real browser TLS fingerprints, making requests indistinguishable from actual Chrome/Firefox browsers. Much lighter than Puppeteer.

tough-cookie: Proper cookie jar implementation for session management.

## The Technical Challenges

### 1. ASP.NET ViewState Management

ASP.NET uses__VIEWSTATEand__VIEWSTATEGENERATORtokens for state management. These need to be extracted and sent with each request:

private

getStateTokens
(
$
:

CheerioAPI
):

{


view_state
:

string
;


view_state_generator
:

string
;

}

{


const

configText

=

$
.
text
().
split
(
"
0|hiddenField
"
).
at
(
-
1
)?.
split
(
"
|
"
)

||

[];


let

view_state

=

$
(
"
#__VIEWSTATE
"
).
attr
(
"
value
"
)

||

""
;


let

view_state_generator

=

$
(
"
#__VIEWSTATEGENERATOR
"
).
attr
(
"
value
"
)

||

""
;


if
(
!
view_state
)

{


view_state

=

configText
[
configText
.
findIndex
((
x
)

=>

x
.
trim
()

==

"
__VIEWSTATE
"
)

+

1
];


}


if
(
!
view_state_generator
)

{


view_state_generator

=

configText
[
configText
.
findIndex
((
x
)

=>

x
.
trim
()

==

"
__VIEWSTATEGENERATOR
"
)

+

1
];


}


return

{

view_state
,

view_state_generator

};

}

Enter fullscreen mode

Exit fullscreen mode

The tokens can be in hidden fields OR embedded in the response text. I handle both cases.

### 2. Pagination Hell

Classic ASP.NET pagination requires simulating user interactions through POST requests with specific event targets:

const

queryParams
:

Record
<
string
,

string
>

=

{


ctl00
$ToolkitScriptManager1
:


params
.
page

>

1


?

"
ctl00$ContentPlaceHolder1$WSExtendedGridNP1$updateWSGrid|ctl00$ContentPlaceHolder1$WSExtendedGridNP1$GridView1$ctl01$btnNext
"


:

"
ctl00$ContentPlaceHolder1$as1$upSearch|ctl00$ContentPlaceHolder1$as1$btnGo
"
,


__VIEWSTATE
:

params
.
config
.
view_state
,


__VIEWSTATEGENERATOR
:

params
.
config
.
view_state_generator
,


__ASYNCPOST
:

"
true
"
,


// ... more params

};

Enter fullscreen mode

Exit fullscreen mode

Each page requires the previous page's state tokens, creating a chain of requests.

### 3. CAPTCHA Support

The site occasionally shows reCAPTCHA. I built an extensible solver interface:

export

interface

ICaptchaSolver

{


solveCaptcha
(
siteKey
:

string
,

pageUrl
?:

string
):

Promise
<
string
>
;

}

Enter fullscreen mode

Exit fullscreen mode

This allows plugging in any CAPTCHA solving service (2captcha, Anti-Captcha, etc.) without modifying the scraper logic.

### 4. Session Management

The scraper maintains cookies across requests using tough-cookie:

this
.
client

=

new

Impit
({


browser
:

"
chrome
"
,


proxyUrl
:

proxyUrl
,


ignoreTlsErrors
:

true
,


cookieJar
:

new

CookieJar
(),

});

Enter fullscreen mode

Exit fullscreen mode

## The Complete Flow

async

searchKeyword
(
query
:

string
):

Promise
<
NCSearchItem
[]
>

{


let

hasNext

=

true
;


let

setPreset

=

true
;

// Simulate form fill on first request


let

page

=

1
;


const

config

=

await

this
.
getSearchConfig
();


const

items
:

NCSearchItem
[]

=

[];


do

{


const

{

items
:

currentItems
,

view_state_generator
,

view_state
,

has_next

}


=

await

this
.
executeSearch
(
query
,

{

page
,

date
:

config
.
date
,

config

},

setPreset
);


items
.
push
(...
currentItems
);


page
++
;


hasNext

=

has_next
;


config
.
view_state

=

view_state
;


config
.
view_state_generator

=

view_state_generator
;


setPreset

=

false
;


}

while
(
hasNext
);


return

items
;

}

Enter fullscreen mode

Exit fullscreen mode

1. Get initial config and state tokens
2. Execute search with form simulation
3. Extract results and pagination state
4. Continue until no more pages
5. Return all items

## Performance Comparison

Let's crunch the numbers for a realistic scenario: scraping 100 public notices across 10 paginated search result pages.

### Puppeteer Approach

Browser startup: 1,500ms (one-time cost)
10 search page loads: 10 × 300ms = 3,000ms
100 detail page loads: 100 × 300ms = 30,000ms
───────────────────────────────────────────
Total time: ~34.5 seconds
Memory usage: ~150MB per instance

Enter fullscreen mode

Exit fullscreen mode

### This Approach (Cheerio + Impit)

HTTP client init: 50ms (one-time cost)
10 search requests: 10 × 100ms = 1,000ms
100 detail requests: 100 × 100ms = 10,000ms
───────────────────────────────────────────
Total time: ~11 seconds
Memory usage: ~10MB per instance

Enter fullscreen mode

Exit fullscreen mode

Result: 3.1x faster execution time, 15x lower memory footprint

### Scalability on 8GB RAM

Approach

Concurrent Instances

Theoretical Throughput

Puppeteer

~50 instances

~145 notices/sec

Cheerio + Impit

~800 instances

~7,270 notices/sec

50x better concurrency- though realistically limited by network bandwidth and rate limiting rather than memory.

## What I Learned

1. Choose the right tool: Puppeteer is amazing, but not always necessary
2. Understand the target: Server-side rendering = no JavaScript needed
3. TLS fingerprinting matters: Impit makes requests look legitimate
4. State management is crucial: ASP.NET apps require careful token handling
5. Build for extensibility: The CAPTCHA solver interface allows easy integration

## The Outcome

I completed this scraper 2 hours after the interview ended and sent it to the interviewer. While I didn't get the job (they chose another candidate), the interviewer specifically mentioned:

"You are clearly very smart and have a lot of expertise. I will put you at the top of my list for the future."

Sometimes the best outcome isn't getting the job - it's building something you're proud of and demonstrating genuine problem-solving skills.

## Try It Yourself

The full source code demonstrates:

* Clean TypeScript architecture
* Comprehensive type definitions
* Testable design with dependency injection
* Production-ready error handling

const

scraper

=

new

NCNotices
(
"
http://your-proxy:8888
"
);

const

results

=

await

scraper
.
searchKeyword
(
"
foreclosure
"
);

for
(
const

searchItem

of

results
)

{


const

detail

=

await

scraper
.
getItem
(
searchItem
);


console
.
log
(
detail
);

}

Enter fullscreen mode

Exit fullscreen mode

## Final Thoughts

Web scraping isn't about using the most popular tools - it's about understanding your target, choosing the right approach, and building maintainable solutions. Sometimes a lightweight HTTP client with good HTML parsing beats a full browser automation framework.

What's your experience with web scraping? Have you faced similar challenges with state management or bot detection? Drop a comment below!

## P.S. - The Plot Twist

So... did I get the job?

Spoiler alert: Nope! But hey, I had fun building this and learned a ton in the process. Sometimes the best outcome isn't getting hired - it's the skills you sharpen and the code you're proud to share.

Plus, I got one of the nicest rejection messages I've ever received:

Not bad for a live coding challenge I completed 2 hours after the interview ended. 😄

Interested in more deep dives on web scraping, TypeScript, and performance optimization? Follow me for more technical breakdowns!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
