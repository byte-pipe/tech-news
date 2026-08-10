---
title: Swift Protocols — The Art of Making Promises 🤝 - DEV Community
url: https://dev.to/gamya_m/swift-protocols-the-art-of-making-promises-59mb
site_name: devto
content_file: devto-swift-protocols-the-art-of-making-promises-dev-com
fetched_at: '2026-08-10T19:54:34.377717'
original_url: https://dev.to/gamya_m/swift-protocols-the-art-of-making-promises-59mb
author: Gamya
date: '2026-08-05'
description: Protocols let you define what a type can do without caring about what it actually is. Once... Tagged with swift, ios, programming, developer.
tags: '#swift, #ios, #programming, #developer'
---

Uses anime fighters to solve code repetition

## Protocols let you define what a type can do without caring about what it actually is. Once that clicks, a huge chunk of Swift and SwiftUI starts making sense.

Picture this. You're building an anime battle simulator and you need a function that calculates how long it would take for a fighter to travel to the battlefield. Easy enough — you write it forNinja:

func
 
sendToMission
(
distance
:
 
Int
,
 
using
 
fighter
:
 
Ninja
)
 
{

 
// code here

}

Enter fullscreen mode

Exit fullscreen mode

Then someone asks: "What about samurai?" Fine:

func
 
sendToMission
(
distance
:
 
Int
,
 
using
 
fighter
:
 
Samurai
)
 
{

 
// code here

}

Enter fullscreen mode

Exit fullscreen mode

Then: "What about pirates? Wizards? Giant mechs?"

Suddenly you have six versions of the same function, all doing the same thing, differing only in the type they accept. And every time someone invents a new kind of fighter, you have to write another one.

There's a better way. 🍥

## What Is a Protocol?

A protocol is a promise. It says:"Any type that conforms to me must have these specific properties and methods."

It doesn't implement anything. It doesn't put any code behind those promises. It's purely a contract — a list of requirements that types can agree to fulfill.

Here's what a protocol looks like:

protocol
 
Fighter
 
{

 
var
 
name
:
 
String
 
{
 
get
 
}

 
var
 
speed
:
 
Int
 
{
 
get
 
set
 
}

 
func
 
estimateTravelTime
(
for
 
distance
:
 
Int
)
 
->
 
Int

 
func
 
travel
(
distance
:
 
Int
)

}

Enter fullscreen mode

Exit fullscreen mode

Breaking that down:

* protocol Fighter— declaring a new protocol calledFighter. Like all types in Swift, it starts with a capital letter
* var name: String { get }— everyFightermust have anameproperty that can beread. It could be a constant or a computed property, as long as it's readable
* var speed: Int { get set }— everyFightermust have aspeedproperty that can be bothread and written. This rules out constants
* func estimateTravelTime(for:)andfunc travel(distance:)— everyFightermust have these two methods. Notice: no function bodies. Just the signatures

That's it. The protocol doesn't care how any of this is implemented. It just says: if you want to call yourself aFighter, you need these things.

## Making Types Conform

Now let's create some actual fighters. The syntax for conforming to a protocol looks just like inheriting from a parent class — a colon after the type name:

struct
 
Ninja
:
 
Fighter
 
{

 
let
 
name
 
=
 
"Naruto"

 
var
 
speed
 
=
 
85

 
func
 
estimateTravelTime
(
for
 
distance
:
 
Int
)
 
->
 
Int
 
{

 
distance
 
/
 
speed

 
}

 
func
 
travel
(
distance
:
 
Int
)
 
{

 
print
(
"
\(
name
)
 uses Body Flicker Technique to travel 
\(
distance
)
km!"
)

 
}

 
func
 
shadowClone
()
 
{

 
print
(
"Shadow Clone Jutsu!"
)

 
}

}

Enter fullscreen mode

Exit fullscreen mode

struct
 
Samurai
:
 
Fighter
 
{

 
let
 
name
 
=
 
"Rurouni"

 
var
 
speed
 
=
 
60

 
func
 
estimateTravelTime
(
for
 
distance
:
 
Int
)
 
->
 
Int
 
{

 
distance
 
/
 
speed

 
}

 
func
 
travel
(
distance
:
 
Int
)
 
{

 
print
(
"
\(
name
)
 rides swiftly on horseback for 
\(
distance
)
km."
)

 
}

 
func
 
drawSword
()
 
{

 
print
(
"Battojutsu!"
)

 
}

}

Enter fullscreen mode

Exit fullscreen mode

A few things to notice:

* Both structs conform toFighterby implementing all four required members. If either one was missing even one, Swift would refuse to build
* Ninjahas an extra method (shadowClone()) andSamuraihas an extra method (drawSword()). That's completely fine — the protocol defines theminimum, not the maximum
* nameis aletconstant in both, which satisfies{ get }since constants are readable
* speedis avarin both, which satisfies{ get set }since variables are both readable and writable

## The Payoff: Using the Protocol as a Type

Here's where everything comes together. Because Swift knows thatanyFighterhasestimateTravelTime()andtravel(), we can write our function to acceptFighterinstead of a specific type:

func
 
sendToMission
(
distance
:
 
Int
,
 
using
 
fighter
:
 
Fighter
)
 
{

 
if
 
fighter
.
estimateTravelTime
(
for
:
 
distance
)
 
>
 
10
 
{

 
print
(
"That's a long journey. 
\(
fighter
.
name
)
 better prepare."
)

 
}
 
else
 
{

 
fighter
.
travel
(
distance
:
 
distance
)

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Now this single function works withanytype that conforms toFighter:

let
 
naruto
 
=
 
Ninja
()

let
 
rurouni
 
=
 
Samurai
()

sendToMission
(
distance
:
 
500
,
 
using
:
 
naruto
)

sendToMission
(
distance
:
 
500
,
 
using
:
 
rurouni
)

Enter fullscreen mode

Exit fullscreen mode

Swift knowsestimateTravelTime()andtravel()exist on both — because the protocol guarantees it. And inside the function, whentravel()is called on aNinja, it prints the ninja version. When called on aSamurai, it prints the samurai version. Same function call, different behavior, automatically.

## Arrays of Protocols

It gets even more powerful. You can put different types together in an array, as long as they all conform to the same protocol:

func
 
calculateAllTravelTimes
(
fighters
:
 
[
Fighter
],
 
distance
:
 
Int
)
 
{

 
for
 
fighter
 
in
 
fighters
 
{

 
let
 
time
 
=
 
fighter
.
estimateTravelTime
(
for
:
 
distance
)

 
print
(
"
\(
fighter
.
name
)
 would take 
\(
time
)
 hours to travel 
\(
distance
)
km"
)

 
}

}

calculateAllTravelTimes
(
fighters
:
 
[
naruto
,
 
rurouni
],
 
distance
:
 
300
)

Enter fullscreen mode

Exit fullscreen mode

An array of[Fighter]can hold aNinja, aSamurai, or any other type that conforms toFighter. Swift doesn't care what specific type is in the array — it only cares that everything in there has fulfilled the protocol's promises.

## Why Not Just Use Inheritance?

You might be wondering: couldn't we do this with a parent class? Have aFighterclass thatNinjaandSamuraiinherit from?

You could — but protocols have two big advantages:

1. Structs and enums can conform to protocols too.In Swift, only classes can inherit from other classes. But protocols work with structs, classes, and enums alike. Since most Swift types are structs, this matters a lot.

2. You can conform to multiple protocols at once.A type can only have one parent class, but it can conform to as many protocols as you need, just by listing them separated by commas:

struct
 
Ninja
:
 
Fighter
,
 
Codable
,
 
CustomStringConvertible
 
{

 
// must satisfy all three protocols

}

Enter fullscreen mode

Exit fullscreen mode

This is why Swift developers love protocols — they're flexible in a way that inheritance just can't match.

## A Quick Note on{ get }vs{ get set }

These two annotations are easy to overlook but important to get right:

* { get }— the property must bereadable. You can satisfy this with aletconstant, avarvariable, or a computed property with a getter
* { get set }— the property must bereadable and writable. You can only satisfy this with avarvariable or a computed property with both getter and setter. Aletconstant won't work here

If you try to satisfy a{ get set }requirement with alet, Swift will tell you the conformance is wrong.

## The One Thing To Hold Onto

Protocols let you write code that works withany type that makes the right promises, rather than one specific type. That makes your functions more flexible, your arrays more versatile, and your whole codebase easier to extend without breaking existing code.

And in SwiftUI? Protocols are literally everywhere.Viewitself is a protocol.Identifiableis a protocol.Codableis a protocol. You've been using them since the first SwiftUI article — now you know exactly what they are and how they work. 🌸

This article was written by me; AI was used to improve grammar and readability.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse