---
title: Uncertain⟨T⟩ - NSHipster
url: https://nshipster.com/uncertainty/
site_name: lobsters
fetched_at: '2025-08-27T23:08:07.071806'
original_url: https://nshipster.com/uncertainty/
date: '2025-08-27'
published_date: '2025-07-25T00:00:00-07:00'
description: GPS coordinates aren’t exact. Sensor readings have noise. User behavior is probabilistic. Yet we write code that pretends uncertainty doesn’t exist, forcing messy real-world data through clean Boolean logic.
tags: swift
---

You know what’s wrong with people?
 They’re too sure of themselves.

Better to be wrong and own it than be right with caveats.
 Hard to build a personal brand out of nuance these days.
 People are attracted to confidence — however misplaced.

But can you blame them? (People, that is)
 Working in software,
 the most annoying part of reaching Senior level
 is having to say“it depends”all the time.
 Much more fun getting to say“let’s ship it and iterate”as Staff or“that won’t scale”as a Principal.

Yet, for all of our intellectual humility,
 why do wewritevibe code like this?

if

current
Location
.
distance
(
to
:

target
)

<

100

{


print
(
"You've arrived!"
)

// But have you, really? 🤨

}

GPS coordinates aren’t exact.
 They’re noisy. They’re approximate. They’re probabilistic.
 ThathorizontalAccuracyproperty tucked away in yourCLLocationobject
 is trying to tell you something important:
 you’reprobablywithin that radius.Probably.

ABool, meanwhile, can be onlytrueorfalse.
 Thatifstatement needs to make a choice one way or another,
 but code like this doesn’t capture the uncertainty of the situation.
 If truth is light,
 then current programming models collapse the wavefunction too early.

## Picking the Right Abstraction

In 2014, researchers at the University of Washington and Microsoft Research
 proposed a radical idea:
 What if uncertainty were encoded directly into the type system?
 Their paper,Uncertain<T>: A First-Order Type for Uncertain Dataintroduced a probabilistic programming approach that’s both
 mathematically rigorous and surprisingly practical.

As you’d expect for something from Microsoft in the 2010s,
 the paper is implemented in C#.
 But the concepts translate beautifully to Swift.

You can findmy port on GitHub:

import

Uncertain

import

Core
Location

let

uncertain
Location

=

Uncertain
<
CLLocation
>.
from
(
current
Location
)

let

nearby
Evidence

=

uncertain
Location
.
distance
(
to
:

target
)

<

100

if

nearby
Evidence
.
probability
(
exceeds
:

0.95
)

{


print
(
"You've arrived!"
)

// With 2σ confidence 🤓

}

When you compare twoUncertainvalues,
 you don’t get a definitivetrueorfalse.
 You get anUncertain<Bool>that represents theprobabilityof the comparison beingtrue.

The same is true for other operators, too:

// How fast did we run around the track?

let

distance
:

Double

=

400

// meters

let

time
:

Uncertain
<
Double
>

=

.
normal
(
mean
:

60
,

standard
Deviation
:

5.0
)

// seconds

let

running
Speed

=

distance

/

time

// Uncertain<Double>

// How much air resistance?

let

air
Density
:

Uncertain
<
Double
>

=

.
normal
(
mean
:

1.225
,

standard
Deviation
:

0.1
)

// kg/m³

let

drag
Coefficient
:

Uncertain
<
Double
>

=

.
kumaraswamy
(
alpha
:

9
,

beta
:

3
)

// slightly right-skewed distribution

let

frontal
Area
:

Uncertain
<
Double
>

=

.
normal
(
mean
:

0.45
,

standard
Deviation
:

0.05
)

// m²

let

air
Resistance

=

0.5

*

air
Density

*

frontal
Area

*

drag
Coefficient

*

(
running
Speed

*

running
Speed
)

This code builds a computation graph,
 sampling only when you ask for concrete results.
 The library usesSequential Probability Ratio Testing (SPRT)to efficiently determine how many samples are needed —
 maybe a few dozen times for simple comparisons,
 scaling up automatically for complex calculations.

// Sampling happens only when we need to evaluate

if

~
(
running
Speed

>

6.0
)

{


print
(
"Great pace for a 400m sprint!"
)

}

// SPRT might only need a dozen samples for this simple comparison

let

sustainable
For5K

=

(
running
Speed

<

6.0
)

&&

(
air
Resistance

<

50.0
)

print
(
"Can sustain for 5K:
\(
sustainable
For5K
.
probability
(
exceeds
:

0.9
)
)
"
)

// Might use 100+ samples for this compound condition

Using an abstraction likeUncertain<T>forces you to deal with uncertainty as a first-class concept
 rather than pretending it doesn’t exist.
 And in doing so, you end up with much smarter code.

To quoteAlan Kay:

Point of view is worth 80 IQ pointsAlan Kay

Before we dive deeper into probability distributions,
 let’s take a detour to Monaco and talk aboutMonte Carlo sampling.

## The Monte Carlo Method

Behold, a classic slot machine (or “fruit machine” for our UK readers 🇬🇧):

enum

Slot
Machine

{


static

func

spin
()

->

Int

{


let

symbols

=

[


"◻️"
,

"◻️"
,

"◻️"
,

// blanks


"🍒"
,

"🍋"
,

"🍊"
,

"🍇"
,

"💎"


]


// Spin three reels independently


let

reel1

=

symbols
.
random
Element
()
!


let

reel2

=

symbols
.
random
Element
()
!


let

reel3

=

symbols
.
random
Element
()
!


switch

(
reel1
,

reel2
,

reel3
)

{


case

(
"💎"
,

"💎"
,

"💎"
):

return

100

// Jackpot!


case

(
"🍒"
,

"🍒"
,

"🍒"
):

return

10


case

(
"🍇"
,

"🍇"
,

"🍇"
):

return

5


case

(
"🍊"
,

"🍊"
,

"🍊"
):

return

3


case

(
"🍋"
,

"🍋"
,

"🍋"
):

return

2


case

(
"🍒"
,

_
,

_
),

// Any cherry


(
_
,

"🍒"
,

_
),


(
_
,

_
,

"🍒"
):


return

1


default
:


return

0

// Better luck next time


}


}

}

Should we play it?

Now, wecouldwork out these probabilities analytically —
 counting combinations,
 calculating conditional probabilities,
 maybe even busting out some combinatorics.

Or we could just let the computer pull the lever a bunch and see what happens.

let

expected
Payout

=

Uncertain
<
Int
>

{


Slot
Machine
.
spin
()

}
.
expected
Value
(
sample
Count
:

10_000
)

print
(
"Expected value per spin: $
\(
expected
Payout
)
"
)

// Expected value per spin: ≈ $0.56

At least we know one thing for certain:The house always wins.

## Beyond Simple Distributions

While one-armed bandits demonstrate pure randomness,
 real-world applications often deal with more predictable uncertainty.

Uncertain<T>provides arich set of probability distributions:

// Modeling sensor noise

let

raw
Gyro
Data

=

0.85

// rad/s

let

gyro
Reading

=

Uncertain
.
normal
(


mean
:

raw
Gyro
Data
,


standard
Deviation
:

0.05

// Typical gyroscope noise in rad/s

)

// User behavior modeling

let

user
Will
Tap
Button

=

Uncertain
.
bernoulli
(
probability
:

0.3
)

// Network latency with long tail

let

api
Response
Time

=

Uncertain
.
exponential
(
rate
:

0.1
)

// Coffee shop visit times (bimodal: morning rush + afternoon break)

let

morning
Rush

=

Uncertain
.
normal
(
mean
:

8.5
,

standard
Deviation
:

0.5
)

// 8:30 AM

let

afternoon
Break

=

Uncertain
.
normal
(
mean
:

15.0
,

standard
Deviation
:

0.8
)

// 3:00 PM

let

visit
Time

=

Uncertain
.
mixture
(


of
:

[
morning
Rush
,

afternoon
Break
],


weights
:

[
0.6
,

0.4
]

// Slightly prefer morning coffee

)

Uncertain<T>also provides comprehensivestatistical operations:

// Basic statistics

let

temperature

=

Uncertain
.
normal
(
mean
:

23.0
,

standard
Deviation
:

1.0
)

let

avg
Temp

=

temperature
.
expected
Value
()

// about 23°C

let

temp
Spread

=

temperature
.
standard
Deviation
()

// about 1°C

// Confidence intervals

let

(
lower
,

upper
)

=

temperature
.
confidence
Interval
(
0.95
)

print
(
"95% of temperatures between
\(
lower
)
°C and
\(
upper
)
°C"
)

// Distribution shape analysis

let

network
Delay

=

Uncertain
.
exponential
(
rate
:

0.1
)

let

skew

=

network
Delay
.
skewness
()

// right skew

let

kurt

=

network
Delay
.
kurtosis
()

// heavy tail

// Working with discrete distributions

let

dice
Roll

=

Uncertain
.
categorical
([
1
:

1
,

2
:

1
,

3
:

1
,

4
:

1
,

5
:

1
,

6
:

1
])
!

dice
Roll
.
entropy
()

// Randomness measure (~2.57)

(
dice
Roll

+

dice
Roll
)
.
mode
()

// Most frequent outcome (7, perhaps?)

// Cumulative probability

if

temperature
.
cdf
(
at
:

25.0
)

<

0.2

{

// P(temp ≤ 25°C) < 20%


print
(
"Unlikely to be 25°C or cooler"
)

}

The statistics are computed through sampling.
 The number of samples is configurable, letting you trade computation time for accuracy.

## Putting Theory to Practice

Users don’t notice when things work correctly,
 but they definitely notice impossible behavior.
 When your running app claims they just sprinted at 45 mph,
 or your IRL meetup app shows someone 500 feet away when GPS accuracy is ±1000 meters,
 that’s a bad look 🤡

So where do we go from here?
 Let’s channel our Senior+ memes from before for guidance.

That Staff engineer saying“let’s ship it and iterate”is right about the incremental approach.
 You can migrate uncertain calculations piecemeal
 rather than rewriting everything at once:

extension

CLLocation

{


var

uncertain
:

Uncertain
<
CLLocation
>

{


Uncertain
<
CLLocation
>.
from
(
self
)


}

}

// Gradually migrate critical paths

let

is
Nearby

=

(


current
Location
.
uncertain
.
distance
(
to
:

destination
)

<

threshold

)
.
probability
(
exceeds
:

0.68
)

And we should consider the Principal engineer’s warning of“that won’t scale”.
 Sampling has a cost, and you should understand the
 computational overhead for probabilistic accuracy:

// Fast approximation for UI updates

let

quick
Estimate

=

speed
.
probability
(


exceeds
:

walking
Speed
,


max
Samples
:

100

)

// High precision for critical decisions

let

precise
Result

=

speed
.
probability
(


exceeds
:

walking
Speed
,


confidence
Level
:

0.99
,


max
Samples
:

10_000

)

Start small.
 Pick one feature where GPS glitches cause user complaints.
 Replace your distance calculations with uncertain versions.
 Measure the impact.

Remember:
 the goal isn’t to eliminate uncertainty —
 it’s to acknowledge that it exists and handle it gracefully.
 Because in the real world,
 nothing is certain except uncertainty itself.

And perhaps,
 with better tools,
 we can finally stop pretending otherwise.
