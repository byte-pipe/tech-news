---
title: A missing exchange rate is not an exchange rate of 1 - DEV Community
url: https://dev.to/hammad4june1999/a-missing-exchange-rate-is-not-an-exchange-rate-of-1-4474
site_name: devto
content_file: devto-a-missing-exchange-rate-is-not-an-exchange-rate-of
fetched_at: '2026-08-26T21:39:32.115629'
original_url: https://dev.to/hammad4june1999/a-missing-exchange-rate-is-not-an-exchange-rate-of-1-4474
author: Hammad Shams Uddin
date: '2026-08-20'
description: 'This is a submission for DEV''s Summer Bug Smash: Smash Stories powered by Sentry. var fx =... Tagged with devchallenge, bugsmash, javascript, api.'
tags: '#devchallenge, #bugsmash, #javascript, #api'
---

Summer Bug Smash: Smash Stories 🐛🛹

This is a submission forDEV's Summer Bug Smash: Smash Storiespowered bySentry.

var
 
fx
 
=
 
(
rates
.
rates
 
&&
 
rates
.
rates
[
v
.
currency
])
 
||
 
1
;

Enter fullscreen mode

Exit fullscreen mode

That line converts a crypto price into whatever currency the visitor picked. It has been on my site for months. It is one line, it reads like defensive programming, and it is capable of being wrong by a factor of 280.

## What|| 1means here

The rate table comes from a currency API. When that API fails, my server-side cache falls back to the only rate it can be sure of:

return
 
$c
[
'data'
]
 
??
 
[
'USD'
 
=>
 
1.0
];

Enter fullscreen mode

Exit fullscreen mode

Which is honest.USD => 1.0is true, and the fallback contains nothing it cannot vouch for.

Then the browser asks that table forPKR, getsundefined, and|| 1turns "I don't have that" into "the rate is 1".

So the page renders:

1 BTC = 95,000.00 PKR

Enter fullscreen mode

Exit fullscreen mode

The real figure is about 26,600,000. And there is no asterisk, no greyed-out state, no "approximate" — it looks exactly like the correct answer, because it is produced by exactly the same code path as the correct answer.

## The second one, in the same function

Three lines down:

var
 
ago
 
=
 
rates
.
cached_age_sec
 
!=
 
null
 
?
 
Math
.
round
(
rates
.
cached_age_sec
 
/
 
60
)
 
:
 
0
;

...

note
:
 
'
Live spot price, updated about 
'
 
+
 
(
ago
 
<=
 
0
 
?
 
'
just now
'
 
:
 
ago
 
+
 
'
 min ago
'
)

Enter fullscreen mode

Exit fullscreen mode

cached_age_secis null when the cache layer cannot say how old the figure is. The ternary is careful — it checks for null — and then maps that null onto0. One line later,0is read as"updated just now".

The one case where the freshness is genuinely unknown is the case that produces the most reassuring sentence on the page.

## The shape

Both are the same mistake wearing different clothes:

A value that was absent, replaced by a plausible default, and then rendered with the same confidence as a measured one.

The defaults are not stupid. A rate of 1 is the identity. An age of 0 is the neutral element. In isolation each choice looks like the sensible thing to reach for when something is missing. The damage is done at the point of display, where the substitute and the real thing become indistinguishable.

And it is worse than crashing. A crash is a bad experience that tells the truth. This tells a confident lie in the visitor's own currency.

## The part that makes it embarrassing

The correct handling was already in the file. Twenty lines above, the plain currency converter has always done this:

var
 
fr
 
=
 
rates
.
rates
[
v
.
from
],
 
to
 
=
 
rates
.
rates
[
v
.
to
];

if 
(
!
(
fr
 
>
 
0
)
 
||
 
!
(
to
 
>
 
0
))
 
{

 
return
 
{
 
error
:
 
'
That currency is not in the live feed.
'
 
};

}

Enter fullscreen mode

Exit fullscreen mode

Same file. Same rate table. Same author. One engine refuses; the two next to it substitute. Nothing distinguishes them except which one I happened to write while thinking about failure.

That is the real lesson and it is not about currencies:defensive habits do not generalise on their own.Getting it right once in a file is not evidence the file is right. It is one data point about one function.

## The fixes

Refuse, and name what is missing:

var
 
fx
 
=
 
(
rates
.
rates
 
&&
 
rates
.
rates
[
v
.
currency
]
 
>
 
0
)
 
?
 
rates
.
rates
[
v
.
currency
]
 
:
 
null
;

if 
(
fx
 
===
 
null
)
 
{

 
return
 
{
 
error
:
 
'
Live rates for 
'
 
+
 
(
v
.
currency
 
||
 
'
that currency
'
)

 
+
 
'
 are unavailable right now — try USD, or refresh in a moment.
'
 
};

}

Enter fullscreen mode

Exit fullscreen mode

Note> 0rather than a truthiness check. A rate of0is as unusable as a missing one, andundefined > 0isfalse, so the two collapse into the same branch without a separate test.

And let unknown stay unknown:

function
 
freshness
(
age
,
 
unit
)
 
{

 
if 
(
age
 
===
 
null
 
||
 
age
 
===
 
undefined
)
 
{
 
return
 
'
age unknown
'
;
 
}

 
if 
(
age
 
<=
 
0
)
 
{
 
return
 
'
updated just now
'
;
 
}

 
return
 
'
updated about 
'
 
+
 
age
 
+
 
'
 
'
 
+
 
unit
 
+
 
'
 ago
'
;

}

Enter fullscreen mode

Exit fullscreen mode

Three sentences for three states, instead of two sentences for three states. The bug was entirely in that missing third branch.

## Testing a feed that has failed

Neither bug is reachable by using the page. The upstream API has to bepartiallydown — up enough to return a table, broken enough that your currency is not in it. I have never once seen that state in a browser, and I never will on purpose.

So the engines had to become reachable from a test. They live in a browser IIFE, so they got the same export guard the widgets file already used:

if 
(
typeof
 
module
 
!==
 
'
undefined
'
 
&&
 
module
.
exports
)
 
{

 
module
.
exports
 
=
 
{
 
ENGINES
,
 
freshness
,
 
trueCost
 
};

}

Enter fullscreen mode

Exit fullscreen mode

Then the fixture is the whole point — a feed that is deliberately, plausibly incomplete:

const
 
feed
 
=
 
{

 
coins
:
 
{
 
bitcoin
:
 
95000
 
},
 
// but not dogecoin

 
rates
:
 
{
 
USD
:
 
1
,
 
EUR
:
 
0.92
 
},
 
// but not PKR

 
cached_age_sec
:
 
120
,

};

Enter fullscreen mode

Exit fullscreen mode

That is not a made-up shape. It is precisely what the server returns when the currency provider is down and the crypto provider is not:['USD' => 1.0]and nothing else.

One of the nineteen assertions is about a function I did not change:

const
 
bad
 
=
 
ENGINES
.
currencyConvert
({
 
amount
:
 
'
100
'
,
 
from
:
 
'
USD
'
,
 
to
:
 
'
PKR
'
 
},
 
fx
);

check
(
'
and a missing one was always refused
'
,
 
typeof
 
bad
.
error
 
===
 
'
string
'
,
 
true
);

Enter fullscreen mode

Exit fullscreen mode

It cannot fail today. It is there so the three engines that read the same table cannot quietly drift apart again — which is how they got out of step in the first place.

I buildUtilorax, a set of free browser-based tools. This came out of thecrypto price converterand thegold & silver price calculator, both of which now tell you when they don't know rather than guessing on your behalf.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (11 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse