---
title: The React2Shell Story | Lachlan Davidson | Blog
url: https://lachlan.nz/blog/the-react2shell-story/
site_name: hackernews_api
content_file: hackernews_api-the-react2shell-story-lachlan-davidson-blog
fetched_at: '2026-05-10T11:50:24.815374'
original_url: https://lachlan.nz/blog/the-react2shell-story/
author: mufeedvh
date: '2026-05-08'
description: The story of CVE-2025-55182 (React2Shell)
tags:
- hackernews
- trending
---

← Posts

 

# The React2Shell Story

 

Authored by Lachlan Davidson

 
 

On November 30th 2025, I reported a critical remote code execution vulnerability ("React2Shell") to Meta. On December 3rd, Meta released a fix and public advisory (CVE-2025-55182), urging developers to immediately update.

Funnily enough, I didn't set out to find a vulnerability in React. I just wanted to understand a protocol so I could be better at hacking modern web applications. But instead, I fell down a rabbit hole to a critical vulnerability that affected millions of websites.

I also recommend reading Sylvie's blog post on React2Shell, and the shenanigans following it.

Dates in this post are displayed in NZDT (GMT +13). This contrasts to Sylvie's post (GMT -7) and Meta's (GMT -8)

## Monday - Taking Flight

As a professional hacker, Monday 24 November 2025 started as a normal work day: finishing off reports, starting new projects, etc. But that afternoon, fueled by curiosity and frustration, I felt a switch flip in my brain, and I dived head-first into a rabbit hole with no turning back.

#### Some Background

In recent years, I've pentested plenty of web apps built on Next.js - a very popular framework based on React. Next.js makes use of React Server Components (RSC) to efficiently render content on the server and send it to the user's browser, as well as React Server Functions (formerly Server Actions) to let user interactions seamlessly invoke server-side JavaScript code.

Many ridiculed Server Actions when they were introduced (you may remember this picture doing the rounds?), but it caught on as it's genuinely quite a cool feature. In one codebase, developers can write server-side code and call it from client-side code.

To facilitate these features, your browser and the server need a fancy way to send messages back and forth, which existing technologies weren't quite suitable for. So, the React team had to build something new. Anybody who has pentested a web app that uses Server Functions should be familiar with this slightly odd request format:

0
=
[
{
 
"a"
:
 
"$$undefined"
,
 
"b"
:
 
"$1:foo:bar"
 
}
]
&
1
=
...

Collectively as an industry, I think we've all thought "Meh, it just looks like JSON with some bells and whistles added", and proceeded to test this like a traditional app, despite the fact there's clearly more attack surface here. I was certainly guilty of this.

#### Where the Switch Flipped

On this Monday, I developed a relentless urge to learn about this format. Ineededto understand it. Those who know me will attest that I don't do things by halves, and will gladly go to the ends of the earth to tear a problem apart.

Most web application hacking is just throwing stuff at applications that the developers didn't anticipate. If this protocol gave me more unique things to throw at web apps, I simplyhadto know; I could perhaps even publish a methodology for it!

#### Wait, but what is it?

So I started by looking at the docume-- oh... there is no specification for the protocol, and the documentation that does exist is scant on details.

What is this protocol even called? It took me some digging to learn its name is "Flight". This is easy to findnow, but before the disclosure of React2Shell, it was surprisingly difficult to even find the name, let alone the format of the protocol.

The best information I could find was a few threads on X discussing RSC.

I was already hooked on trying to understand Flight, but seeing "no docs, only code" poured fuel on the fire of my motivation. My fate was now sealed; I would not rest until I was a Flight expert.

I hardly got a wink of sleep, but by the next morning, I had a good understanding of the protocol's fundamentals, though this was just the beginning.

#### Flight 101

Next.js allows developers to magically pass complex JavaScript objects between client-side and server-side code, but this includes objects that cannot be represented by simple JSON. Flight solves that problem, adding support for more complicated data types (such asDate,BigInt, andMap), references (including circular references), and Promises (data that arrives asynchronously), to name a few of its features.

It's still fundamentally based on JSON, but Flight messages are broken into "chunks". Each chunk is typically sent as a form element, and can arrive asynchronously, potentially out-of-order. The special$syntax denotes a Flight type. Seen below,$Dindicates a date,$xis a reference to another chunk, and$x:yallows property selection.

0
 
=
 
{

 
"email"
:
 
"
[email protected]
"
,

 
"updated"
:
 
"$D04 Dec 1995 00:12:00 GMT"
,

 
"details"
:
 
"$1"

}

&
1
 
=
 
{

 
"firstName"
:
 
"$2"
,

 
"lastName"
:
 
"$3:foo"

}

&
2
 
=
 
"John"

&
3
 
=
 
{

 
"foo"
:
 
"Doe"

}

Once parsed, the above resolves to the following in the server's memory:

{

 
"email"
:
 
"
[email protected]
"
,

 
"updated"
:
 
Date
(
Mon
 
Dec
 
04
 
1995
 
13
:
12
:
00
 
GMT
+
1300
 
(
New
 
Zealand
 
Daylight
 
Time
)
)
,

 
"details"
:
 
{

 
"firstName"
:
 
"John"
,

 
"lastName"
:
 
"Doe"

 
}

}

#### A "Glaring Omission of a Safety Check"

Crucially, Flight allows referencing an object's properties. So what happens if we try to reference a property that isn't directly on an object, but rather on its prototype?

Lo and behold, if we send the server a Flight message that references an inherited property (in this case,Number.prototype.toString), it successfully retrieves it and places it on our attacker-controllable object.

0
 
=
 
{

 
"foo"
:
 
"$1:toString"

}

&
1
 
=
 
123

0
 
=
 
{

 
"foo"
:
 
Number
.
prototype
.
toString

}

This was described by Guillermo Rauch (the original author of Next.js and founder of Vercel) as"a glaring omission of a safety check". However, at the time, I honestly didn't think too much of this. It seemed... excessively lenient, but it abided by standard JavaScript property lookup semantics. React is one of the most battle-tested frameworks out there, so it must be fine,right?

## Tuesday - Weaponising Flight

#### The Initial Goal

With my initial research, I had two key things in mind:

1. Developers frequently neglect to validate user inputs.
2. Flight can let attackers send significantly more complex objects than plain JSON.

This could be a potent combination. I wasn't looking for a vulnerability in Flight itself (yet), but rather to see if Flight could beabusedto exploit Next.js apps with insufficient validation.

Almost every Next.js application I've reviewed has contained such attack surface, including many open-source projects, so I hoped to weaponise Flight to build an exploit methodology and earn some CVEs.

(Side note: When React2Shell was fixed, it also closed off these cool attack vectors, making these initial ideas moot.)

#### Example 1 - Type Coercion

Here is a very simple React Server Function a developer might implement, but with a subtle vulnerability:

async
 
function
 
sayHello
(
name
:
 
string
)
:
 
string
 
{

 
'use server'

 
return
 
'Hello, '
 
+
 name 
+
 
'!'

}

This incorrectly assumesnameis a string - but that's just wishful thinking. It may actually be any object that a malicious client can send with Flight. So what happens if we send a custom object with a function referenced ontoString? When attempting to concatenate it with'Hello',the server will implicitly call thetoStringfunction!

It's especially easy to gloss over this mistake, as the TypeScript annotation: stringprovides an illusion of type safety; however, this is not actually enforced at runtime.

#### Example 2 - Explicit Function Calls

ThetoStringexample is simple to identify, but seemed the hardest to exploit, as it's only one function call with no controllable arguments.

On the contrary, this example has significantly more attack surface. The developer has once again assumedstris a string, but an attacker could place a malicious function onreplaceAlland control two arguments to it.

async
 
function
 
replaceStuff
(
str
:
 
string
,
 before
:
 
string
,
 after
:
 
string
)
:
 
string
 
{

 
'use server'

 
return
 str
.
replaceAll
(
before
,
 after
)

}

#### The Illusion of Type Safety

"But Lachlan, the parameters in those examples clearly have types?!", I can hear some of you exclaim.

However, TypeScript only performs build-time analysis - it can't validate or enforce the type of untrusted data at runtime. This double-edged sword can make it very convincing that the user input is a valid type, but nothing actually checks this. An attacker can still send an arbitrary object, even when the developer expects something specific.

#### Exploitation - The Rules of the Game

Flight provides the ammunition, but actually turning it into a useful weapon was difficult.

To present this like a CTF puzzle...

Assuming an application developer has written insecure code (like the prior examples):

* An attacker-specified function is called once
* The attacker controls 0 to N arguments
* Whatever function we specify, and whatever shape our arguments take, must come from Flight messages.

Skimming the React docs and Flight code indicates we can use the following data types:

1. Plain objects, arrays, strings
2. Constants that JSON can't represent (Infinity,BigInt,NaN, etc.)
3. Date
4. Set,Map, and typed arrays, such asUint8Array
5. APromisefor a chunk that will arrive in the future
6. References to Server Functions
7. Any property or method on any of the above

The final point is the most important, as this is where we can start referencing functions. For example, we can make anArray, then referenceArray.prototype.join. Or, we can make aDateto referenceDate.prototype.getYear, and so on.

With any function, we can use.constructorto get access to theFunctionconstructor, which is one of the few ways to dynamically execute arbitrary code in JavaScript. First, you call it with the code to execute, and it returns a function. When you executethatfunction, your arbitrary code executes.

If we could coerceFunction("console.log('evil')")(), we'd win. Through the rules of the game, calling a function once is easy. However, subsequently calling the result seemed near-impossible.

At this point, I asked for advice and ideas from quite a few friends. But in particular, I'd like to thankSylvie Mayerwho I've been friends with for many years. Knowing that she's highly-skilled at CTF challenges of a similar nature to this, I approached her with my research so far into Flight and the aforementioned puzzle 'rules'. She has her ownblog poston this saga, and also some great write-ups on her blog, such as Python jail challenges that have quite a similar skill set to this.

## Wednesday - The Ridiculous Cycle

I still had to fit normal work days around this, but throughout this week, I couldn't help but spend every other waking moment on this newfound obsession. On top of that, the dopamine made sleep out of the question. I already considered myself very knowledgeable about JavaScript, but I kept learning more and more about its quirks, what Flight gave us access to, and how we could make it misbehave.

Sylvie and I spent quite some time here trying to weaponise Flight, but every time we found something that looked promising, we tried and failed to make it do something useful for achieving RCE. But on every iteration, I became slightly more fluent with this strange protocol and the things it gave us access to.

Interestingly though, we both kept getting stuck in this mental loop:

It's very bizarre to look back and personally reflect on this. Clearly, I had a massive cognitive blind spot. React's near-impeccable track record in security made the notion of finding a vulnerability like this seem ridiculous. The examples I gave above of vulnerable application code (treating untrusted user input like a string) actually appeared inside React itself! This made me almost disregard such cases as potential avenues for exploitation.

The best we hoped for at this point was that React/Flight would let us construct a malicious function to execute, and the vulnerable application would then actually invoke it.

## Thursday - The First Breakthrough

At some point on Thursday evening, I found one of the most crucial ingredients that would lead me to develop React2Shell.

When the high-level framework (such as Next.js) asks React to decode an incoming Flight payload, it callsawait decodeReply(...). It looks perfectly reasonable, but hides a tricky secret...

#### Quick History Lessons - Callbacks and Promises

Server-side JavaScript code runs in a single thread, allowing I/O to be handled by the engine with native code in background threads. In JS-world, you pass a "callback" function for the engine to invoke when the background operation is complete.

doTheThing
(
123
,
 
function
(
result
)
 
{

 
doTheNextThing
(
result
.
blah
,
 
function
(
)
 
{

 
moreStuff
(
...
)

 
}
)

}
)

However, this gets very messy. If you need 10 sequential database calls to handle an incoming request, you need 10 layers of indentation, leading to "callback hell". This motivated the invention of "Promises" - a standard format that represents the promise of a future value.

With a Promise, you call.then(...callback...)instead of passing a callback function directly. If your.thenhandler returns another Promise, you can keep chaining.thencalls. You don't need layers of indentation for each call, you just chain another.then(...).

doThething
(
123
)

 
.
then
(
(
result
)
 
=>
 
doTheNextThing
(
result
.
blah
)
)

 
.
then
(
(
)
 
=>
 
moreStuff
(
)
)

 
.
then
(
(
)
 
=>
 
andEvenMoreStuff
(
)
)

This was a big improvement, but still not particularly ergonomic. But then, ECMAScript 2017 finally introducedasync/awaitto JS, allowing asynchronous code to be written like synchronous code:

let
 result 
=
 
await
 
doTheThing
(
123
)

await
 
doTheNextThing
(
result
.
blah
)

await
 
moreStuff
(
)

await
 
andEvenMoreStuff
(
)

Functions markedasyncsimply return aPromisewhen called, and allawaitdoes is call.then(...)on aPromise, makingasync/awaitfully interoperable with promises!

However... beforePromisewas standard in ECMAScript 2015, there were a whole raft of community implementations of promises, often with differing behaviour. But they all had one thing in common: the.then(...)convention. So, we call any object that follows this convention a "thenable" - quite literally, any object which can be.then()'d.

Under the hood,awaitinvokesPromise.resolve, which leniently invokes thenables.

>
 
await
 
{
 then
:
 
console
.
log
 
}

function
 
(
)
,
 
function
 
(
)
 
// logged injected resolve, reject callbacks

But there's one final detail: Do you ever have toawait await foo()? No! If a thenable resolves toanother thenable, it willalsobe called automatically.

>
 
await
 
{

 
then
:
 
resolve1
 
=>
 
resolve1
(
{

 
then
:
 
resolve2
 
=>
 
resolve2
(
123
)

 
}
)
 

}

123
 

#### Abusing Thenables

So what happens if we serialise and send the following to Flight?

{

 then
:
 
Array
.
prototype
.
push

}

Well,await decodeReply(...)will first run the Flight parser. But, it then sees it got another thenable, and calls our attacker-supplied function!

The request will hang, because our fake promise never resolves. But if we inspect it in memory, we find the runtime indeed called.then(resolve, reject)on our crafted object:

{

 then
:
 
Array
.
prototype
.
push
,

 
0
:
 
[
Function
 
(
anonymous
)
]
,

 
1
:
 
[
Function
 
(
anonymous
)
]
,

 length
:
 
2

}

This was the first piece of behaviour that didn't feel intentional in React. Up until this point, everything that Flight provided felt... excessive, but from my outside perspective, it looked like what you'd expect, given its design.

Taking it one step further, if we craft our thenable payload to resolve to another thenable, we can chain unlimited function calls. However, at the time, I didn't fully recognise the importance of this. I already had ways of implicitly calling a function on our attacker-controlled object, so this didn't feel like a new capability.

## Friday - Tantalisingly Close

In the early AM of Friday, I made the single biggest breakthrough that changed the game. Instead of "Could Flight be used to exploit applications?" things quickly turned to "Holy moly, there's a serious chance of a critical vulnerability in React Flight itself".

This is where another back-and-forth between hope and despair started. I thought I was minutes away from getting a critical vulnerability in React, but then nothing worked like I thought it would.

#### Accessing React's Internals

So far, I'd been focussing on what JavaScript builtins I could reference with Flight, but there was another gadget that had been staring me in the face. When normally referencing another chunk in Flight, you use$x. But there's another option: if you use$@x, you instead create apromiseof a chunk that will arrive later. How does React do this? It creates anew Chunk, whereChunkis a React-specific object that inherits fromPromise.

So what happens if you send the following?

0
 
=
 
{

 
"then"
:
 
"$1:then"

}

&
1
 
=
 
"$@2"

You get this:

 Error: An undefined error was thrown, see here for more info: https://nextjs.org/docs/messages/threw-undefined
at ignore-listed frames

What on earth happened??

1. "$@2"constructed anew Chunk(...)
2. $1:thenpulled outChunk.prototype.then:React's implementation of .then
3. Flight returned our attacker-controlled object
4. awaitinvoked.then(...), calling React's implementation, but againstour object, not React's

Analysing the code shows React tried to look up.statuson our chunk, didn't find a normal state, and rejected the promise (e.g. threw an error), with.reasonas the error. However,.reasonisundefinedon our attacker-controlled object.

Chunk
.
prototype
.
then
 
=
 
function
 
<
T
>
(

 
this
:
 SomeChunk
<
T
>
,

 
resolve
:
 
(
value
:
 
T
)
 
=>
 mixed
,

 
reject
:
 
(
reason
:
 mixed
)
 
=>
 mixed
,

)
 
{

 
const
 chunk
:
 SomeChunk
<
T
>
 
=
 
this
;

 
...

 
switch
 
(
chunk
.
status
)
 
{

 
// ... (normal cases) ...

 
default
:

 
reject
(
chunk
.
reason
)
;

 
break
;

 
}

}

#### First Approach - Malicious Server Manifest

I was now convinced there was RCE in React.

Chunkis the fundamental object where Flight is implemented, and it holds a lot of internal state. I could coerce Flight to runChunk.prototype.thenagainst my object, and therefore spoof any of that internal state, creating a "fake chunk".

As I was quite familiar with Flight now, the pathway to RCE seemed obvious. To use Server Functions, React needs a "server manifest". This is a strict list that maps Server Function IDs that a user can specify to which module name and function the server should run.

My idea was:

1. Make Flight runChunk.prototype.thenagainst our object
2. In our "fake chunk" override the server manifest to map an ID tochild_process'sexecfunction, granting shell execution.

I quickly constructed a payload to do exactly that; however, it didn't work and I had no clue why, despite flailing around in a debugger for an hour.

I felt miles away from making it work, so I pinged Sylvie privately at this point, and shared my latest findings with her. In my mind, I now felt like it could take another week of research before getting anywhere. But while in the process of walking her through replicating my test environment, I hooked my debugger correctly and saw React trying to read and execute./child_process.dev.js?!?!

React doesn't use Node's module system directly, but rather Webpack or Turbopack. Becausechild_processwasn't a valid module in Webpack, it fell back to trying to find thechild_processmodule as a file on-disk.

Once again...

So, my payload was doing exactly what I hoped for - tricking React into including thechild_processmodule and executing code, but just not therealchild_processmodule.

Sylvie and I then started looking for which moduleswereavailable. She zoomed in on modules that could allow file writes, and I zoomed out to exhaustively enumerate the potentially useful modules that were available by default.

Neither of us was successful that night, and as dawn broke, I unfortunately had a pile of pesky 'real' work to catch up on, and we briefly shelved it for a day.

#### RCE

Late on Friday, I had a brainwave on how to build the exploit chain, and in the early hours of Saturday morning, I finally made it all click, and React2Shell was born.

It was averycomplicated exploit chain. It involved hopping several function calls to ultimately callModule._load, which allows arbitrary JavaScript execution in Node.js, as the module namedmodulewas fortunately accessible. However, it required alotof complex operations to modify the internal state ofmoduleto overcome limitations. To be honest, I'm not even sure if I understand it, butit's on my GitHub.

I was in a state of shock and disbelief. At this point, the analytical part of my brain felt it was statistically more likely that I was currently delirious from sleep deprivation than that I had actually found RCE in React. Shortly after, not knowing what to do, I just closed my laptop and fell asleep until it was nearly Sunday.

## Sunday - Refining RCE and Submission

Spoofing the server manifest turned out to be a bad approach. The RCE worked, but it relied on Webpack's generated module IDs being correct (which is only partially consistent), running in a Node.js runtime, and many other factors.

So, I worked from first principles and found a far more elegant solution very quickly. Revisiting the idea ofFunction("evilCode();")();, I just needed to find somewhere in React'sChunkcode that called a function with an argument I could control, and then place that result somewhere it would be called. With a fresh pair of eyes, I focussed on places in theChunkcode where React calls functions that are assumed to be from its internal state, but I could now control. In one case, when creating a reference to an uploaded file blob, the$Bxcode calls_formData.get(...)with an argument we can mostly control. We can use this to construct our malicious function, and plant the result on a finalthenproperty, finally getting our RCE called.This is the PoC I submitted to Meta.

## Disclosure

When I sent the report to Meta, the reproduction steps were scarily easy. Effectively: install a fresh Next.js/React app, run the script, RCE.

Amazingly, despite being a weekend, the Meta team triaged, reproduced, and confirmed my submission in around 17 hours.

The Meta and wider React team (including Vercel) were truly a delight to work with. It was surreal to meet and chat with their very talented staff over Zoom and Slack, and see just how seriously they were all treating this.

They worked around the clock to develop and test patches, co-ordinate comms, prepare the CVE for release, while also co-ordinating with industry partners to implement defences before the exploit became public knowledge.

## Aftermath

Sylvie's blog post covershow we started scanning for vulnerable targets to immediately alert them (and hopefully earn some sweet bounty), as the potential impact could be devastating if weaponised by attackers. From big AI firms to crypto trading platforms, Next.js is very popular and public-facing.

In a future post, I will discuss how the next few days unfolded: the "race to reproduce", the double-edged sword of 0-day protections, and, of course, the involvement of AI.