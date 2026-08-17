---
title: Functional languages are heavily imperative. - DEV Community
url: https://dev.to/playfulprogramming/functional-languages-are-heavily-imperative-4c1
site_name: devto
content_file: devto-functional-languages-are-heavily-imperative-dev-co
fetched_at: '2026-08-17T19:25:57.128338'
original_url: https://dev.to/playfulprogramming/functional-languages-are-heavily-imperative-4c1
author: Mike Pearson
date: '2026-08-17'
description: Functional and declarative are not the same thing. Haskell creators knew it, and we can clearly see the difference between purity and program structure with certain Haskell, FRP, RxJS, HTML, and JavaScript examples. Tagged with imperative, declarative, haskell.
tags: '#imperative, #declarative, #haskell'
---

This article will seem full of contradictions.

Even writing it feels like a contradiction: Why am I digging through academic Haskell papers from the '90s right in the middle of my AI psychosis moment? Literally, as I write this, I am running my first experiment with an agent delegating tasks to another agent. So why am I spending time on esoteric academic nonsense instead of giving in to the vibes and building my loopy graphy software factory?

I am writing this because AI is a nuclear amplifier on the patterns we establish in our codebases, and we literally do not have the right terminology to establish scalable patterns. Nobody has the answers we need because nobody even has the right terminology to talk about it.

## Two Dimensions, Not One

Industry dogma says that functional and declarative are synonyms—that code is either side-effectfulandimperative, or pureanddeclarative:

But functional and declarative are independent dimensions:

Code that is both functional and imperative debunks this, and so does code that is both side-effectful and declarative.

Both exist!

## "Imperative Functional Programming"

Simon L Peyton Jones and Philip Wadler helped create Haskell, which is a beautiful, pure functional programming language.

In 1993 they wrote a paper called"Imperative Functional Programming."The title may sound like an oxymoron, but it isn't.

The functional programming community had been struggling with how to manage side-effects like I/O, and these co-creators of Haskell proposed a way to decouple theexpressionof I/O commands from theirexecution.

But they noticed something:

It will not have escaped the reader’s notice that programs written in the monadic style look rather similar to imperative programs. For example, the echo program in C:

echo
()
 
{

loop:
 
a
 
=
 
getchar
(
a
);

 
if
 
(
a
 
==
 
eof
)

 
return
;

 
else
 
{
 
putchar
 
(
a
);

 
goto
 
loop
;
 
}

}

Enter fullscreen mode

Exit fullscreen mode

In Haskell:

echo
 
::
 
IO
 
()

 
echo
 
=
 
getcIO
 
'bindI0'
 
\
a
 
->

 
if
 
(
a
 
==
 
eof
)
 
then

 
doneIO

 
else
 
putcI0
 
a
 
'seqI0'

Enter fullscreen mode

Exit fullscreen mode

Does the monadic style force one, in effect, to write a functional facsimile of an imperative program, thereby losing any advantages of writing in x functional language?

Nope! Jones and Wadler list two advantages that remain:

1. List operations (likemapandappend) can still operate on monadic commands
2. Effects can be expressed without immediately executing them. "It's a bit like being able to define your own control structures in an imperative language."

Recognizing the imperative structure of the Haskell monadic pattern does not mean we have to abandon the advantages that areinherentin pure functional programming.

But itisstill imperative structure.

### "Lazy Imperative Programming"

John Launchbury, another creator of Haskell, wrote a paper the following year calledLazy Imperative Programming.

In it he says,

Imperative features were introduced to Glasgow Haskell for expressing input and output.

Could this be plainer? Haskell has imperative features.

And the Haskell code that uses them is imperative. Also from his paper, an "Imperative Scan Left":

writeVaris an imperative statement, which is why this is an example of imperative code—written entirely with pure functions!!!

The paperhas many other references to imperative stuff, including this:

In a strict imperative framework such as the IO monad (and most imperative languages), no value could be returned until the whole of the list was traversed. Using lazy sequences, however, this is not the case. If only the head of the list is required then very little of the computation is performed: the variable is allocated and initialised, it is read, and the list returned with that value in the head. If even less is required, merely whether the final list is empty for example, then the variable is not even allocated as only xs needs to be examined in order to give the structure of ys.

🤯This is insanely cool.

Again, not everything in Haskellhasto be declarative for it to still allow for incredibleexecutionproperties!

### The "Imperative Feel" of Concurrent Haskell

Paul Hudak (another creator of Haskell) and Conal Elliot wrotea paperin 1997 where they weren't happy with the "strongly imperative feel" of Concurrent Haskell—even though it was 100% purely functional.

(Side note: I owe my passion for programming to this paper. More on that later.)

Here's an example of what that pure functional approach with an "strongly imperative feel" looked like:

box
 
<-
 
newEmptyMVar

forkIO
 
$
 
do

 
threadDelay
 
1000000

 
putMVar
 
box
 
42

result
 
<-
 
takeMVar
 
box

Enter fullscreen mode

Exit fullscreen mode

puTMVar box 42expresses a command to setbox's value to 42.

In the authors' own words,

While this system is purely functional in the technical sense, its semantics has a strongly imperative feel. That is, expressions are evaluated without side-effects to yield concurrent, imperative computations, which are executed to perform theimplied side effects. In contrast, modeling entire behaviors as implicitly concurrent functions of continuous time yields what we considera more declarative feel.

It is not a coincidence that the definition of "imperative" in English is "expresses a command" and that a line of code that literally "expresses a command" had an "strongly imperative feel"—even in Haskell.

But the authors were dissatisfied with that "imperative feel"—so they invented functional reactive programming (FRP):

box
 
t0
 
=

 
0
 
`
untilB
`

 
predicate
 
(
time
 
>=*
 
t0
 
+
 
1
)
 
t0

 
-=>
 
42

Enter fullscreen mode

Exit fullscreen mode

Just a single declaration. Nothing here expresses a command at all.putMVaris 100% imperative, while this is 100% declarative and 0% imperative.

Note on "more declarative" and monoparadigmatic dogma#### Note on "more declarative" and monoparadigmatic dogmaSince the industry dogma in the 1990s was "functional = declarative", they had to call FRPmore declarative. Concurrent Haskell was already declarative, supposedly, by virtue of being in Haskell—so this had to beextradeclarative 🤷And I say that with great admiration for these authors, because I owe my passion for programming to this paper. This was the origin of both RxJS and signals, which I love... very much. Too much for many people.The "Lazy Imperative Programming" paper was more contradictory. The author often contrasted Haskell with "imperative languages," while dozens of times referring to featureswithinHaskell as imperative.On the one hand, functional languages are commonly more expressive and easier to reason about than imperative languages,After reading 20 or so papers from the 1990s talking about programming paradigms, you will understand that the terminology was extremely entrenched. Academics classified programming languages into rigid categories to help explain the programming patterns of the time.Functional programmers were especially guilty of reinforcing this reductionism, since they were a minority of programmers and had to fight against the grain with every rhetorical tool they could. Branding functional programming languages as automatically 100% declarative was an enticing selling point—even though we have many Haskell creators very plainly referring to featureswithinHaskell as imperative.Also, in the 1990s very few "imperative languages" had added much functional features, having not had to deal with much concurrent processing yet, which meant languages really did mostly fall into neat categories; multi-paradigmatic languages were not the norm like they are now. The concept of entire languages as "imperative" or "declarative" somewhat applied back then, but today is a nothing but a leftover from decades of synchronous code that all matched the same 2-3 structural patterns.We have to make a mental note of this history, but if we do not push to correct the terminology, it will continue to confuse developers and AI. Many developers think that stuffing imperative features between< >characters magically makes them declarative because it's part of HTML, a "declarative language." Some are attempting this and creating masses of spaghetti code that only cosmetically looks different from the imperative JavaScript spaghetti they were writing last year.There are no "declarative languages" and "imperative languages", as much as it would simplify selling them. There are commands expressed in code, which areimperativeby the purest definition; and there are features and behaviorsdeclaredwithout scattered commands controlling them from elsewhere.

### Conclusion (Imperative Functional Programming)

The literal precise English definition of "imperative" is something that expresses a command. That is what these pure functions are doing in Haskell and other functional languages. This should already rest the argument.

But even the less precise definitions of imperative programming focus onstructural descriptions written in coderather than execution details:

* "Imperative programming involveswriting programs as sequences of explicit commandsthat are executed in order from top to bottom."https://builtin.com/articles/imperative-programming
* "logicencodedas a sequence of ordered operations"https://en.wikipedia.org/wiki/Programming_language
* "Imperative programmingfocuses on describinghow a program operates step by step, rather than on high-leveldescriptionsof its expected results"https://en.wikipedia.org/w/index.php?title=Imperative_programming
* "With an imperative approach, a developerwrites code that specifies the stepsthat the computer must take to accomplish the goal."https://learn.microsoft.com/en-us/dotnet/standard/linq/functional-vs-imperative-programming
* "Im­per­a­tive pro­gram­ming languages arecomposed of step-by-step in­struc­tions (how)... By contrast, in de­clar­a­tive pro­gram­ming, the desired result (what) isdescribeddirectly."https://www.ionos.com/digitalguide/websites/web-development/imperative-programming/
* Imperative programming is a paradigm where youexplicitly statehow the program should achieve the desired result.https://octopus.com/devops/infrastructure-as-code/declarative-vs-imperative-programming/

It's very clear that Haskell and functional programming languages are extremely cool with the flexibility they afford for all kinds of things, including the execution of side effects.

But Haskell has features that enable writing literal imperative commands even with pure functions. This results in code that is structured imperatively: Explicit commands incrementally adding to behavior described elsewhere. The instant a single command appears, it completely takes away the declarative quality of describing the final result of something up-front. The imperative features of Haskell are not justlessdeclarative; they are completely anti-declarative.

Functional programmingcanbe imperative.

## Declarative Side-Effects

### RxJS

RxJS enables fully declarative code, despite latent side-effects.

RxJS actually came from that Fran paper we looked at earlier, which proposed a way to turn this kind of Concurrent Haskell:

box
 
<-
 
newEmptyMVar

forkIO
 
$
 
do

 
threadDelay
 
1000000

 
putMVar
 
box
 
42

result
 
<-
 
takeMVar
 
box

Enter fullscreen mode

Exit fullscreen mode

into this:

box
 
t0
 
=

 
0
 
`
untilB
`

 
predicate
 
(
time
 
>=*
 
t0
 
+
 
1
)
 
t0

 
-=>
 
42

Enter fullscreen mode

Exit fullscreen mode

Neither of these trigger side-effects, but the declarative version structures the code as a single description of a complete, final logical result (a behavior over time). The thing that made the first imperative and the second declarative is thestructureof the code, not the side-effect execution model.

The same structural move can be made in side-effectful code:

const
 
box
 
=
 
Promise
.
withResolvers
();

setTimeout
(()
 
=>
 
{

 
box
.
resolve
(
42
);

},
 
1000
);

const
 
result
 
=
 
await
 
box
.
promise
;

Enter fullscreen mode

Exit fullscreen mode

const
 
box
 
=
 
await
 
lastValueFrom
(

 
timer
(
1000
).
pipe
(
map
(()
 
=>
 
42
)),

);

Enter fullscreen mode

Exit fullscreen mode

Both of these trigger side-effects when executed, but the declarative version structures the code as a single description of a complete, final logical result. The thing that made the first imperative and the second declarative is thestructureof the code, not the side-effect execution model.

These four code snippets alone are enough to complete our four quadrants:

But let's look at some more common declarative side-effects.

### HTML

"HTML is declarative" is often said. And it's mostly true (see above callout "Note on "more declarative" and monoparadigmatic dogma").

Yet the entire point of HTML is a side-effect: You being able to look at beautiful interfaces like this:

It's not just the DOM that's a side effect though. The HTML rendered in the page can itself trigger other kinds of side effects, like network calls:

<link
 
rel=
"stylesheet"
 
href=
"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
 
/>

<script 
src=
"https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"
></script>

<!-- ... -->

<img
 
src=
"https://storage.googleapis.com/blog-images-backup/1*tY3o3UFtBaMQ103en48qxA.png"
 
/>

<iframe
 
src=
"https://www.youtube.com/embed/dQw4w9WgXcQ"
 
/>

Enter fullscreen mode

Exit fullscreen mode

### Nondeterministic Declarations

#### Math.random

Math.random()technically produces a side effect because it relies on and mutates a hidden global internal state (the seed or PRNG algorithm pointer) inside the runtime environment to generate its next value.

But this is still totally declarative:

const
 
x
 
=
 
Math
.
random
();

Enter fullscreen mode

Exit fullscreen mode

#### Date.now(),crypto.randomUUID(),process.memoryUsage(), etc...

const
 
now
 
=
 
Date
.
now
();

const
 
date
 
=
 
new
 
Date
();

const
 
perfNow
 
=
 
performance
.
now
();

const
 
randomBytes
 
=
 
crypto
.
getRandomValues
(
new
 
Uint32Array
(
1
));

const
 
uuid
 
=
 
crypto
.
randomUUID
();

const
 
hrtime
 
=
 
process
.
hrtime
();

const
 
uptime
 
=
 
process
.
uptime
();

const
 
memoryUsage
 
=
 
process
.
memoryUsage
();

const
 
freeMemory
 
=
 
os
.
freemem
();

const
 
battery
 
=
 
await
 
navigator
.
getBattery
();

const
 
windowWidth
 
=
 
window
.
innerWidth
;

const
 
visibility
 
=
 
document
.
visibilityState
;

const
 
online
 
=
 
navigator
.
onLine
;

Enter fullscreen mode

Exit fullscreen mode

All of these are completely declarative. They are declarations of final results, and no subsequent step-by-step (or any) imperative code is involved.

But they are not pure functions. They don't have side effects, but they have side causes, so they still are not functional. So while they aren't examples of declarative code that causes side effects, they are examples of declarative code that break rules of functional programming, showing that these are independent dimensions.

### Declarative "Pure" Functions with Side-Effects

#### CPU

const
 
fib
 
=
 
(
n
:
 
number
)
 
=>
 
n
 
<
 
2
 
?
 
n
 
:
 
fib
(
n
 
-
 
1
)
 
+
 
fib
(
n
 
-
 
2
);

const
 
result
 
=
 
fib
(
50
);

Enter fullscreen mode

Exit fullscreen mode

Everything here looks pure as the driven snow, and it's definitely declarative.

No side effects at all, right?

In fact, it triggers 40,730,022,147 calls, which means that its side effects are so severe that I really don't recommend pasting that into dev tools and running it. You think jQuery has interesting side effects by reaching into the DOM and changing the behavior of random things, but this will change the behavior of everything on the page. Namely, it eliminates it because it locks up the CPU.

#### Memory

new
 
Array
(
2
 
**
 
30
).
fill
(
0
);

Enter fullscreen mode

Exit fullscreen mode

No side effects here, right? It's declarative, at least.

However, this might get compiled into assembly code that looks like this:

mov rdi, 8589934592
call malloc

mov rcx, 1073741824
mov rdi, rax
xor eax, eax
rep stosq

Enter fullscreen mode

Exit fullscreen mode

There is a huge side-effect in this code:call mallocrequests8589934592= (2 ** 30) × 8 bytes = 1,073,741,824 × 8 bytes ≈8 GiBof memory.

There may be guardrails against creating arrays this big. I didn't feel like testing it. But there is a variation that may not be prevented:

Array
.
from
({
 
length
:
 
1000
 
},
 
()
 
=>
 
new
 
Array
(
1
_000_000
).
fill
(
0
));

Enter fullscreen mode

Exit fullscreen mode

This time each inner array has only 1 million elements, but there are 1000 of them, so 1,000,000,000 total elements.

Here are some possible side-effects:

* The page or Node.js process becomes unresponsive while the runtime tries to allocate and initialize the array
* In a severe case, the browser tab crashes because it exceeds its memory limit.

And yet, it's still declarative.

### Conclusion (Declarative Side-Effects)

Declarative and functional are not synonyms. Declarative code is abouthow a computation is structured: describing a result rather than spelling out a sequence of commands to get there.

Functional purity is aboutwhat that computation depends on and affects. A declaration can trigger network requests, consume CPU and memory, observe clocks and runtime state, or depend on hidden mutable state without becoming imperative.

These are separate dimensions.

## Conclusion

The point of separating these dimensions is not to win a pointless terminology argument. It is to make better engineering decisions while AI is applying incredible pressure on our architectural patterns.

If we collapsefunctionalintodeclarative, we lose the ability to talk precisely about what code is doing. Pure code can still be structured imperatively. Declarative code can still observe mutable state, trigger I/O, allocate absurd amounts of memory, or otherwise affect the world.

Structure and purity are independent properties of code that sometimes align, butDO NOT HAVE TO!

If the problem is hidden state, surprising effects, or difficulty reasoning about dependencies, functional programming can help with its explicit inputs, immutable values, pure transformations, effect isolation. And although I love functional programming, in my experience, most apps genuinely will never see significant consequences for not being purely functional.

However, most apps I have seen have suffered severely from being imperative: It always scatters control, with commands reaching across a system (spaghetti code), or behavior that can only be understood by mentally executing twenty steps across multiple contexts. Declarative code fixes this. Functional programming does not.

I am sick of saying I like declarative code and being told to juST UsE ELm or HASkElL.

People can't even understand the problem because they don't have the words to discuss it properly.

Now throw AI into this cross-talking mix of contradictions, and this is what we can expect:

This looks delicious, but can we please try to avoid it anyway?

Let's fix our vocabulary so we can learn real things about imperative code andsteer humans and AI away from it.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse