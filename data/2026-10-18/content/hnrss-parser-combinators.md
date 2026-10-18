---
title: Parser Combinators
url: https://t3.at/blog/2026-10-17-parser-combinators/
site_name: hnrss
content_file: hnrss-parser-combinators
fetched_at: '2026-10-18T21:14:58.850071'
original_url: https://t3.at/blog/2026-10-17-parser-combinators/
date: '2026-10-18'
description: Better than regex!
tags:
- hackernews
- hnrss
---

T3
Oct 17, 2026

# Parser Combinators

"
Hello
, 
world
!"
→
{
 greeting: 
"Hello"
,
 who: 
"world"

}
The string "Hello, world!" parses into an object with greeting "Hello", who "world".
type
 Parser<
T
> =
 
(input: string) => [
T
, 
string
]
[
"
pInteger
number
10
, 
"
string
 20 30
"
]
pInteger
The type Parser of T is a function from an input string to a pair of a T and the rest of the string. For example, pInteger cuts "10 20 30" after"10", and returns the number 10 and the rest of the string," 20 30".
pHello
[
"
Hello
"
, 
"
 100
"
]
pIgnoreWhitespace
[
"
 
null
"
, 
"
100
"
]
pInteger
[
"
100
"
, 
"
"
]
"Hello 100" parsed by pHello, then pIgnoreWhitespace, then pInteger, each taking the rest the one before left over: pHello returns "Hello" and " 100". pIgnoreWhitespace returns " " and "100". pInteger returns "100" and "".
pHello100
[
"
Hello 100
["Hello", null, 100]
"
, 
"
"
]
"Hello 100" parsed by pHello100, each taking the rest the one before left over: pHello100 returns "Hello 100" and "".
pSeq(
 
pHello
,
 
pIgnoreWhitespace
,
 
pInteger

)
⇒
Parser<[

string
,

null
,

number

]>
pSeq given pHello, pIgnoreWhitespace, pInteger is a Parser of the tuple [string, null, number].
const pHello100 = pSeq(...)
const result = pHello100("Hello 100")
pHello100
[
"
Hello 100
["Hello", null, 100]
"
, 
"
"
]
"Hello 100" parsed by pHello100, each taking the rest the one before left over: pHello100 returns "Hello 100" and "".
pGreeting
[
"
Hello 100
["Hello", null, 100]
{
 greeting: "Hello",
 who: 100
}
pMap
"
, 
"
"
]
"Hello 100" parsed by pGreeting, each taking the rest the one before left over: pGreeting returns "Hello 100" and "".
pSeq(pNumber, pSemicolon)
[
"
10;
[10, ";"]
"
, 
"
20;30;
"
]
pSeq(pNumber, pSemicolon)
[
"
20;
[20, ";"]
"
, 
"
30;
"
]
pSeq(pNumber, pSemicolon)
[
"
30;
[30, ";"]
"
, 
"
"
]
"10;20;30;" parsed by pSeq(pNumber, pSemicolon), then pSeq(pNumber, pSemicolon), then pSeq(pNumber, pSemicolon), each taking the rest the one before left over: pSeq(pNumber, pSemicolon) returns "10;" and "20;30;". pSeq(pNumber, pSemicolon) returns "20;" and "30;". pSeq(pNumber, pSemicolon) returns "30;" and "".
PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
64 bytes from 1.1.1.1: icmp_seq=1 ttl=52 time=389 ms
64 bytes from 1.1.1.1: icmp_seq=2 ttl=52 time=68.7 ms
64 bytes from 1.1.1.1: icmp_seq=3 ttl=52 time=47.1 ms
64 bytes from 1.1.1.1: icmp_seq=4 ttl=52 time=48.6 ms
64 bytes from 1.1.1.1: icmp_seq=5 ttl=52 time=85.8 ms
64 bytes from 1.1.1.1: icmp_seq=6 ttl=52 time=84.8 ms
64 bytes from 1.1.1.1: icmp_seq=7 ttl=52 time=87.4 ms
--- 1.1.1.1 ping statistics ---
8 packets transmitted, 7 received, 12.5% packet loss, time 7008ms
rtt min/avg/max/mdev = 47.129/115.880/388.750/112.515 ms
{
 header: { targetIp: "1.1.1.1", resolvedIp: "1.1.1.1", icmpPayloadSize: 56, totalPacketSize: 84 },
 packets: [
 { byteCount: 64, from: "1.1.1.1", seq: 1, ttl: 52, time: 389 },
 { byteCount: 64, from: "1.1.1.1", seq: 2, ttl: 52, time: 68.7 },
 { byteCount: 64, from: "1.1.1.1", seq: 3, ttl: 52, time: 47.1 },
 { byteCount: 64, from: "1.1.1.1", seq: 4, ttl: 52, time: 48.6 },
 { byteCount: 64, from: "1.1.1.1", seq: 5, ttl: 52, time: 85.8 },
 { byteCount: 64, from: "1.1.1.1", seq: 6, ttl: 52, time: 84.8 },
 { byteCount: 64, from: "1.1.1.1", seq: 7, ttl: 52, time: 87.4 },
 ],
 statistics: {
 packetsTransmitted: 8, packetsReceived: 7, packetLoss: 12.5, time: 7008,
 rtt: { min: 47.129, avg: 115.88, max: 388.75, mdev: 112.515 },
 },
}
Fold
const result = list.reduce((acc, n) => acc + n)
["Hello", " ", 100] 
→
 "Hello 100"
Unfold
const result = pSeq(...)("Hello 100")
"Hello 100" 
→
 ["Hello", " ", 100]
T
string

## Parser Combinators

Parsingis the act of taking less structured input like text, and turning it into more structured data, like objects.

Many of you will be familiar with using regex to parse text, and some of you might know about tree-sitter, a heavy-duty parsing library which powers the syntax highlighting in your code editor.

But regex gets messy on complex tasks, and tree-sitter often is overkill — for this middle ground,parser combinatorsare perfect. Not many people know about them, so allow me to show you!

## The partial parser

The smallest unit of parsing we’ll be looking at is thepartial parser. It gets to decide where to cut the input string, and then it returns a tuple consisting ofwhateverand the rest of the string.

It can be any old function, as long as it returns such a tuple! It can even use regex inside.

▸
Code definition
·
pInteger
const
 pInteger
: 
Parser
<
number
> 
=
 (
input
: 
string
) 
=>
 {

 const
 match
 =
 input
.
match
(
/
^
\d
+
/
);

 if
 (
match
 ==
 null
) 
throw
 new
 Error
();

 const
 digits
 =
 match
[
0
];

 return
 [
Number
(
digits
), 
input
.
substring
(
digits
.
length
)];

};

## Chaining

A single parser function won’t do much on its own; but by applying multiple parsers in sequence, we can consume the entire input step by step.

▸
Code definition
·
pHello
const
 pHello
: 
Parser
<
string
> 
=
 (
input
: 
string
) 
=>
 {

 if
 (
!
input
.
startsWith
(
"Hello"
)) 
throw
 new
 Error
();

 return
 [
"Hello"
, 
input
.
substring
(
5
)];

};
▸
Code definition
·
pIgnoreWhitespace
const
 pIgnoreWhitespace
: 
Parser
<
null
> 
=
 (
input
: 
string
) 
=>
 {

 const
 match
 =
 input
.
match
(
/
^
\s
+
/
);

 if
 (
match
 ==
 null
) 
throw
 new
 Error
();

 const
 spaces
 =
 match
[
0
];

 return
 [
null
, 
input
.
substring
(
spaces
.
length
)];

};
▸
Code definition
·
pInteger
const
 pInteger
: 
Parser
<
number
> 
=
 (
input
: 
string
) 
=>
 {

 const
 match
 =
 input
.
match
(
/
^
\d
+
/
);

 if
 (
match
 ==
 null
) 
throw
 new
 Error
();

 const
 digits
 =
 match
[
0
];

 return
 [
Number
(
digits
), 
input
.
substring
(
digits
.
length
)];

};
const
 [
token1
, 
input2
] 
=
 pHello
(
"Hello 100"
);

const
 [
token2
, 
input3
] 
=
 pIgnoreWhitespace
(
input2
);

const
 [
token3
, 
input4
] 
=
 pInteger
(
input3
);

console
.
log
(
token1
, 
token2
, 
token3
); 
// "Hello", null, 100

console
.
log
(
input4
); 
// empty!

## Chaining

Or, and this is where the real power of partial parsers comes in: we wrap the chain up as a new parser of its own.

▸
Code definition
·
pHello100
const
 pHello100
: 
Parser
<[
string
, 
null
, 
number
]> 
=
 (
input
: 
string
) 
=>
 {

 const
 [
hello
, 
rest1
] 
=
 pHello
(
input
);

 const
 [
space
, 
rest2
] 
=
 pIgnoreWhitespace
(
rest1
);

 const
 [
number
, 
rest3
] 
=
 pInteger
(
rest2
);

 return
 [[
hello
, 
space
, 
number
], 
rest3
];

};

## pSeq

Or we generalize even further and provide a function that does the chaining! “Feeding the rest of the string into the next parser” is super generic after all, and doesn’t really depend on what any single parser does.

Getting the types right is tricky, but TypeScript is perfectly capable of expressing these complex variadic types.

▸
Code definition
·
pSeq
type
 Parsers
<
T
 extends
 unknown
[]> 
=
 { [
K
 in
 keyof
 T
]: 
Parser
<
T
[
K
]> };

const
 pSeq
 =
 <
T
 extends
 unknown
[]>(...
parsers
: 
Parsers
<
T
>): 
Parser
<
T
> 
=>

 (
input
) 
=>
 {

 const
 results
 =
 [] 
as
 unknown
 as
 T
;

 let
 rest
 =
 input
;

 for
 (
const
 p
 of
 parsers
) {

 const
 [
val
, 
next
] 
=
 (
p
 as
 Parser
<
unknown
>)(
rest
);

 results
.
push
(
val
);

 rest
 =
 next
;

 }

 return
 [
results
, 
rest
];

 };

## Combinators

SincepSeqcombines many parsers into a new parser, we call it aparser combinator.

Take a moment to appreciate the functional madness going on:pSeqis a function that takes parsers, which are functions, and it returns another parser, which is also a function.

And only then do we actually start the parsing, by calling the resulting function with data.

It’s like we are building up this construct of nested functions to create a complex program. Kinda cool!

## By the way

If splitting a string into many tokens feels somehow related to.reducethen you have good instincts. What we are doing here is actually the dual, which is called anunfoldin functional circles (reduceis referred to as afold).

While a fold uses intermediate state — the accumulator — to combine
a list of things into one, an unfold uses intermediate state to split one thing into many.

Yay, maths!

## Tuples are unwieldy

If the point of parsing is to get structured, often human-readable data out of raw strings, then a tuple of values like["Hello", null, 100]can hardly be the end goal.

We could of course map over the result to transform it into a more convenient shape.

const
 pHello100
 =
 pSeq
(...);

const
 [
result
, 
rest
] 
=
 pHello100
(
"Hello 100"
);

console
.
log
(
result
); 
// ["Hello", null, 100]

const
 parsed
 =
 {

 greeting
: 
result
[
0
],

 who
: 
result
[
2
],

};

## pMap

But this is not in the spirit of parser combinators! Like before, we can also wrap the mapping into a new parser combinator itself.

pMaptakes a parser and a function; the function will be applied
to the eventual result after parsing.

▸
Code definition
·
pMap
const
 pMap
 =
 <
T
, 
R
>(
parser
: 
Parser
<
T
>, 
fn
: (
value
: 
T
) 
=>
 R
): 
Parser
<
R
> 
=>

 (
input
: 
string
) 
=>
 {

 const
 [
value
, 
rest
] 
=
 parser
(
input
);

 return
 [
fn
(
value
), 
rest
];

 };
const
 pGreeting
 =
 pMap
(

 pHello100
,

 ([
greeting
, 
_
, 
who
]) 
=>
 ({ 
greeting
, 
who
 }),

);

const
 [
parsed
, 
rest
] 
=
 pGreeting
(
"Hello 100"
);

console
.
log
(
parsed
); 
// { greeting: "Hello", who: 100 }

## pRepeat

Before we hop into a practical example, let me show the third fundamental parser combinator:pRepeat— it takes a given
parser and applies it over and over again until it can’t.

It’s the*of regex, as a combinator!

▸
Code definition
·
pRepeat
const
 pRepeat
 =
 <
T
>(
parser
: 
Parser
<
T
>): 
Parser
<
T
[]> 
=>

 (
input
: 
string
) 
=>
 {

 const
 values
: 
T
[] 
=
 [];

 let
 rest
 =
 input
;

 while
 (
true
) {

 try
 {

 const
 [
value
, 
next
] 
=
 parser
(
rest
);

 values
.
push
(
value
);

 rest
 =
 next
;

 } 
catch
 {

 return
 [
values
, 
rest
];

 }

 }

 };
▸
Code definition
·
pNumber
const
 pNumber
: 
Parser
<
number
> 
=
 (
input
: 
string
) 
=>
 {

 const
 match
 =
 input
.
match
(
/
^
\d
+
/
);

 if
 (
match
 ==
 null
) 
throw
 new
 Error
();

 const
 digits
 =
 match
[
0
];

 return
 [
Number
(
digits
), 
input
.
substring
(
digits
.
length
)];

};
▸
Code definition
·
pSemicolon
const
 pSemicolon
: 
Parser
<
string
> 
=
 (
input
: 
string
) 
=>
 {

 if
 (
!
input
.
startsWith
(
";"
)) 
throw
 new
 Error
();

 return
 [
";"
, 
input
.
substring
(
1
)];

};
const
 pNumberCsv
 =
 pRepeat
(
pSeq
(
pNumber
, 
pSemicolon
));

pNumberCsv
(
"10;20;30;"
);

// [[[10, ";"], [20, ";"], [30, ";"]], ""]

## Let’s build a parser!

We have enough tools now to start parsing actual, real-world data!

Above is a sample output of me pinging Cloudflare. There’s tons
of useful info in there, so let’s parse it into structured data —
how about this:

type
 PingResult
 =
 {

 header
: 
PingHeader
;

 packets
: 
IcmpPacket
[];

 statistics
: 
PingStatistics
;

};

type
 IcmpPacket
 =
 {

 byteCount
: 
number
; 
from
: 
string
;

 seq
: 
number
; 
ttl
: 
number
; 
time
: 
number
;

};

type
 PingHeader
 =
 {

 targetIp
: 
string
; 
// 1.1.1.1

 resolvedIp
: 
string
; 
// 1.1.1.1 but in parentheses

 icmpPayloadSize
: 
number
; 
// 56

 totalPacketSize
: 
number
; 
// 84

};

type
 PingStatistics
 =
 {

 packetsTransmitted
: 
number
; 
packetsReceived
: 
number
;

 packetLoss
: 
number
; 
time
: 
number
;

 rtt
: { 
min
: 
number
; 
avg
: 
number
; 
max
: 
number
; 
mdev
: 
number
 };

};

## Bits and Bobs

We have some recurring things in this output like decimal numbers or IP addresses. So let’s set those up first.

▸
Code definition
·
pString
// Exact text, like "PING"

const
 pString
 =
 (
text
: 
string
): 
Parser
<
string
> 
=>
 (
input
: 
string
) 
=>
 {

 if
 (
!
input
.
startsWith
(
text
)) 
throw
 new
 Error
();

 return
 [
text
, 
input
.
substring
(
text
.
length
)];

};
▸
Code definition
·
pInteger
// Whole numbers, like 64

const
 pInteger
: 
Parser
<
number
> 
=
 (
input
: 
string
) 
=>
 {

 const
 match
 =
 input
.
match
(
/
^
\d
+
/
);

 if
 (
match
 ==
 null
) 
throw
 new
 Error
();

 const
 digits
 =
 match
[
0
];

 return
 [
Number
(
digits
), 
input
.
substring
(
digits
.
length
)];

};
▸
Code definition
·
pDecimal
// Numbers with an optional fraction, like 68.7

const
 pDecimal
: 
Parser
<
number
> 
=
 (
input
: 
string
) 
=>
 {

 const
 match
 =
 input
.
match
(
/
^
\d
+
(
\.
\d
+
)
?
/
);

 if
 (
match
 ==
 null
) 
throw
 new
 Error
();

 const
 digits
 =
 match
[
0
];

 return
 [
Number
(
digits
), 
input
.
substring
(
digits
.
length
)];

};
▸
Code definition
·
pIpV4Address
// Four bytes and three dots, like 1.1.1.1

const
 pByte
 =
 pMap
(
pInteger
, (
n
) 
=>
 {

 if
 (
n
 >
 255
) 
throw
 new
 Error
();

 return
 n
;

});

const
 pDot
 =
 pString
(
"."
);

const
 pIpV4Address
 =
 pMap
(

 pSeq
(
pByte
, 
pDot
, 
pByte
, 
pDot
, 
pByte
, 
pDot
, 
pByte
),

 ([
a
, 
_1
, 
b
, 
_2
, 
c
, 
_3
, 
d
]) 
=>
 `
${
a
}
.
${
b
}
.
${
c
}
.
${
d
}
`
,

);
▸
Code definition
·
pWhitespace
// At least one space

const
 pWhitespace
: 
Parser
<
null
> 
=
 (
input
: 
string
) 
=>
 {

 const
 match
 =
 input
.
match
(
/
^
\s
+
/
);

 if
 (
match
 ==
 null
) 
throw
 new
 Error
();

 return
 [
null
, 
input
.
substring
(
match
[
0
].
length
)];

};

## The header

The first line should be easy, it’s just somepSeqof parsers and then apMapto finagle it intoPingHeadershape.

▸
Code definition
·
pPingHeaderParts
const
 pPingHeaderParts
 =
 pSeq
(

 pString
(
"PING"
), 
pWhitespace
, 
pIpV4Address
, 
pWhitespace
,

 pString
(
"("
), 
pIpV4Address
, 
pString
(
")"
), 
pWhitespace
,

 pInteger
, 
pString
(
"("
), 
pInteger
, 
pString
(
")"
),

 pString
(
" bytes of data."
),

);
▸
Code definition
·
pPingHeader
const
 pPingHeader
 =
 pMap
(

 pPingHeaderParts
,

 ([
a
, 
b
, 
c
, 
d
, 
e
, 
f
, 
g
, 
h
, 
i
, 
j
, 
k
, 
l
, 
m
]) 
=>
 ({

 targetIp
: 
c
,

 resolvedIp
: 
f
,

 icmpPayloadSize
: 
i
,

 totalPacketSize
: 
k
,

 }),

);

## A packet

Actually the packets are also apSeqof parsers, followed by apMap. This parsing stuff is really easy, hey!

▸
Code definition
·
pIcmpPacketParts
const
 pIcmpPacketParts
 =
 pSeq
(

 pInteger
, 
pString
(
" bytes from "
), 
pIpV4Address
,

 pString
(
": icmp_seq="
), 
pInteger
,

 pString
(
" ttl="
), 
pInteger
,

 pString
(
" time="
), 
pDecimal
, 
pString
(
" ms"
),

);
▸
Code definition
·
pIcmpPacket
const
 pIcmpPacket
 =
 pMap
(

 pIcmpPacketParts
,

 ([
a
, 
b
, 
c
, 
d
, 
e
, 
f
, 
g
, 
h
, 
i
, 
j
]) 
=>
 ({

 byteCount
: 
a
, 
from
: 
c
, 
seq
: 
e
, 
ttl
: 
g
, 
time
: 
i
,

 }),

);

## The statistics

Could you imagine doing this in regex by the way?

▸
Code definition
·
pUselessLine
const
 pUselessLine
 =
 pSeq
(

 pString
(
"--- "
), 
pIpV4Address
, 
pString
(
" ping statistics ---"
),

);
▸
Code definition
·
pStatsLine1
const
 pStatsLine1
 =
 pSeq
(

 pInteger
, 
pString
(
" packets transmitted, "
),

 pInteger
, 
pString
(
" received, "
),

 pDecimal
, 
pString
(
"% packet loss, time "
),

 pInteger
, 
pString
(
"ms"
),

);
▸
Code definition
·
pStatsLine2
const
 pStatsLine2
 =
 pSeq
(

 pString
(
"rtt min/avg/max/mdev = "
),

 pDecimal
, 
pString
(
"/"
), 
pDecimal
, 
pString
(
"/"
),

 pDecimal
, 
pString
(
"/"
), 
pDecimal
,

 pString
(
" ms"
),

);
▸
Code definition
·
pPingStatistics
const
 pPingStatistics
 =
 pMap
(

 pSeq
(
pUselessLine
, 
pWhitespace
, 
pStatsLine1
, 
pWhitespace
, 
pStatsLine2
),

 ([
_1
, 
_2
, [
a
, 
b
, 
c
, 
d
, 
e
, 
f
, 
g
, 
h
], 
_3
, [
i
, 
j
, 
k
, 
l
, 
m
, 
n
, 
o
, 
p
, 
q
]]) 
=>
 ({

 packetsTransmitted
: 
a
, 
packetsReceived
: 
c
,

 packetLoss
: 
e
, 
time
: 
g
,

 rtt
: { 
min
: 
j
, 
avg
: 
l
, 
max
: 
n
, 
mdev
: 
p
 },

 }),

);

## Ping packets, parsed!

And boom, that’s pretty much it! Just one morepSeqandpMapto wrap all the parts together, and we have built a complete parser for the ping command.

That was super easy, right?

▸
Code definition
·
pPingSummary
const
 pPingSummary
: 
Parser
<
PingResult
> 
=
 pMap
(

 pSeq
(

 pPingHeader
,

 pRepeat
(
pMap
(
pSeq
(
pWhitespace
, 
pIcmpPacket
), ([
_
, 
packet
]) 
=>
 packet
)),

 pWhitespace
,

 pPingStatistics
,

 ),

 ([
header
, 
packets
, 
_
, 
statistics
]) 
=>
 ({ 
header
, 
packets
, 
statistics
 }),

);

## Go give it a try

In a single post we built a fairly complicated parser from literally zero, and a hand-rolled parser combinator library along the way!

It’s much easier to create correct and maintainable parsers this way than with a regex; once you start nestingpSeqcalls, the equivalent regex would become an unreadable mess, while the combinator approach gives you something squeaky clean.

In case you are missing fancier features like backtracking or lookahead, rest assured that parser combinators can handle those scenarios as well, since at the end of the day it’s all just functions composed together.

Go give them a try next time you have to parse something — parser combinators are a really elegant solution to the parser problem, and many more people should use them!