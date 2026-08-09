---
title: 7.8 MB of Keys I Allocated Just to Throw Away - DEV Community
url: https://dev.to/ssukhpinder/78-mb-of-keys-i-allocated-just-to-throw-away-50mn
site_name: devto
content_file: devto-78-mb-of-keys-i-allocated-just-to-throw-away-dev-c
fetched_at: '2026-08-09T11:26:28.870722'
original_url: https://dev.to/ssukhpinder/78-mb-of-keys-i-allocated-just-to-throw-away-50mn
author: Sukhpinder Singh
date: '2026-08-04'
description: 'A profiler trace put me on a code path I''d never once suspected: a request handler that reads a blob... Tagged with csharp, dotnet, programming, webdev.'
tags: '#csharp, #dotnet, #programming, #webdev'
---

A profiler trace put me on a code path I'd never once suspected: a request handler that reads a blob of space-separated tokens and sums a weight for each one it recognizes. The logic is boring and correct. What caught my eye was 7.8 MB ofstringallocations sitting in the hot loop of something that only everreadsthose tokens. I wasn't keeping any of them. I was allocating a key, doing one dictionary lookup, and dropping it on the floor.

The keys were substrings. Every token I sliced out of the blob became its own littlestringobject just so I could hand it toDictionary.TryGetValue. So I measured what that habit actually costs, and what the span-based alternate lookup buys back.

## The setup

The input is one string of 200,000 space-separated tokens, about 1.5 MB. Roughly 70% of them are real keys that live in a 5,000-entryDictionary<string, long>; the rest are misses. The job walks the blob, pulls out each token, looks it up, and adds the weight. Timings are the median of 9 rounds after a warmup, allocations come fromGC.GetAllocatedBytesForCurrentThread, .NET 10, Release build, small Linux container. Not a lab. I care about the ratios.

Here's the version I'd been writing forever:

int
 
start
 
=
 
0
;

for
 
(
int
 
i
 
=
 
0
;
 
i
 
<=
 
input
.
Length
;
 
i
++)

{

 
if
 
(
i
 
==
 
input
.
Length
 
||
 
input
[
i
]
 
==
 
' '
)

 
{

 
string
 
token
 
=
 
input
.
Substring
(
start
,
 
i
 
-
 
start
);
 
// allocates

 
if
 
(
table
.
TryGetValue
(
token
,
 
out
 
long
 
w
))
 
sum
 
+=
 
w
;

 
start
 
=
 
i
 
+
 
1
;

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Substringis the tell. It reads like exactly what I mean, which is why it never gets flagged in review. And for a handful of tokens it's genuinely fine. Here's the bill for 200,000:

[A: Substring + lookup] sum=6,963,210 median=23.4 ms allocated=7,812 KB

Enter fullscreen mode

Exit fullscreen mode

Seven and a half megabytes of keys, none of which outlived a singleif. On a busy endpoint that's 7.5 MB of garbage per call for the collector to sweep up later, and the collector's bill lands on someotherrequest's latency, which is what makes this kind of thing so annoying to track down.

## The alternate lookup

Since .NET 9,Dictionary<TKey, TValue>can hand you analternate lookupkeyed by a different, comparer-compatible type. For a string-keyed dictionary the useful one isReadOnlySpan<char>. You ask for it once, then look up spans directly — no substring, no allocation:

var
 
lookup
 
=
 
table
.
GetAlternateLookup
<
ReadOnlySpan
<
char
>>();

ReadOnlySpan
<
char
>
 
span
 
=
 
input
;

int
 
start
 
=
 
0
;

for
 
(
int
 
i
 
=
 
0
;
 
i
 
<=
 
span
.
Length
;
 
i
++)

{

 
if
 
(
i
 
==
 
span
.
Length
 
||
 
span
[
i
]
 
==
 
' '
)

 
{

 
ReadOnlySpan
<
char
>
 
token
 
=
 
span
.
Slice
(
start
,
 
i
 
-
 
start
);
 
// no alloc

 
if
 
(
lookup
.
TryGetValue
(
token
,
 
out
 
long
 
w
))
 
sum
 
+=
 
w
;

 
start
 
=
 
i
 
+
 
1
;

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Slicedoesn't copy anything — it's a window over the original string's characters. The comparer hashes and compares the span against the stored keys without ever building a temporary string. Same dictionary, same entries, just a second door into it. And the numbers:

[B: span alternate lookup] sum=6,963,210 median=14.9 ms allocated=0 KB
same result: True
allocation ratio A/B: ~200,000x
time ratio A/B: 1.57x

Enter fullscreen mode

Exit fullscreen mode

Identical sum, so I didn't quietly change behavior. Zero bytes allocated for the keys. And it came out about 1.57x faster too, which I honestly didn't expect to be that pronounced. I went in for the allocations and the wall-clock win was a bonus, mostly from skipping 140,000 string constructions and the memory traffic they drag along.

## The catch nobody mentions

GetAlternateLookupisn't free to reach for. It only works when the dictionary's comparer implementsIAlternateEqualityComparer<ReadOnlySpan<char>, string>. The good news is that the comparers you'd actually pick for machine keys already do:StringComparer.Ordinal,StringComparer.OrdinalIgnoreCase, and the default comparer you get fromnew Dictionary<string, long>()all qualify. A customIEqualityComparer<string>you wrote yourself will not, and you find out with an exception thrown at theGetAlternateLookupcall, not a compile error. So it's a runtime contract, and that's worth a test.

My honest opinion: this is a hot-path tool, not a default. If you're looking up a handful of keys, or the strings already exist asstringobjects, reach for it and you've added ceremony for nothing. Where it earns its keep is exactly the shape above, where you're carving keysout ofa larger buffer (a parser, a tokenizer, a CSV or header scanner, a log processor) and the substring is pure waste because it dies the instant the lookup returns. That's when 7.8 MB quietly turns into zero.

I've started grepping my own parsers forSubstring(followed by aTryGetValueon the next line. It's a small pattern, but it shows up more than you'd think once you know its silhouette.

Full runnable sample:https://github.com/ssukhpinder/dev-to-code-samples/tree/main/023-dictionary-alternate-lookup

Have you found a spot in your code where the key was already sitting in a buffer you owned? I'd like to hear where it turned up for you.

— still benchmarking things nobody asked me to

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse