---
title: An Interactive Intro to CRDTs | jakelazaroff.com
url: https://jakelazaroff.com/words/an-interactive-intro-to-crdts/
site_name: hnrss
content_file: hnrss-an-interactive-intro-to-crdts-jakelazaroffcom
fetched_at: '2026-03-04T11:13:13.809879'
original_url: https://jakelazaroff.com/words/an-interactive-intro-to-crdts/
date: '2026-03-03'
description: CRDTs don't have to be all academic papers and math jargon. Learn what CRDTs are and how they work through interactive visualizations and code samples.
tags:
- hackernews
- hnrss
---

Have you heard about CRDTs and wondered what they are? Maybe you’ve looked into them a bit, but ran into a wall of academic papers and math jargon? That was me before I started myRecurse CenterThe Recurse CenterThe Recurse Center is a self-directed, community-driven educational retreat for programmers in New York City.www.recurse.com/batch. But I’ve spent the past month or so doing research and writing code, and it turns out that you can build a lot with just a few simple things!

In this series, we’ll learn what a CRDT is. Then we’ll write a primitive CRDT, compose it into more complex data structures, and finally use what we’ve learned to build a collaborative pixel art editor. All of this assumes no prior knowledge about CRDTs, and only a rudimentary knowledge of TypeScript.

To pique your curiosity, this is what we’ll end up with:

JavaScript is required to run this demo.

Draw by clicking and dragging with your mouse. Change the paint color by using the color input on the bottom left. You can draw on either canvas and your changes will show up on the other, as if they were collaborating on the same picture.

Clicking the network button prevents changes from reaching the other canvas (although they’ll sync up again when they come back “online”). The latency slider adds a delay before changes on one canvas show up on the other.

We’ll build that in the next post. First, we need to learn about CRDTs!

### What is a CRDT?

Okay, let’s start from the top. CRDT stands for “Conflict-free Replicated Data Type”. That’s a long acronym, but the concept isn’t too complicated. It’s a kind of data structure that can be stored on different computers (peers). Each peer can update its own state instantly, without a network request to check with other peers. Peers may have different states at different points in time, but are guaranteed to eventually converge on a single agreed-upon state. That makes CRDTs great for building rich collaborative apps, like Google Docs and Figma — without requiring a central server to sync changes.

Broadly, there are two kinds of CRDTs: state-based and operation-based.1State-based CRDTs transmit their full state between peers, and a new state is obtained by merging all the states together. Operation-based CRDTs transmit only the actions that users take, which can be used to calculate a new state.

That might make operation-based CRDTs sound way better. For example, if a user updates one item in a list, an operation-based CRDT can send a description of only that update, while a state-based CRDT has to send the whole list! The drawback is that operation-based CRDTs impose constraints on the communication channel: messages must be delivered exactly once, in causal order, to each peer.2

This post will exclusively focus on on state-based CRDTs. For brevity, I’ll just say “CRDTs” from here on out, but know that I’m referring specifically to state-based CRDTs.

I’ve been talking about what CRDTs do, but whatisa CRDT? Let’s make it concrete: a CRDT is any data structure that implements this interface:3

interface

CRDT
<
T
,

S
>

{

 value
:

T
;

 state
:

S
;


merge
(
state
:

S
)
:

void
;

}

That is to say, a CRDT contains at least three things:

* A value,T. This is the part the rest of our program cares about. The entire point of the CRDT is to reliably sync the value between peers.
* A state,S. This is the metadata needed for peers to agree on the same value. To update other peers, the whole state is serialized and sent to them.
* A merge function. This is a function that takes some state (probably received from another peer) and merges it with the local state.

The merge function must satisfy three properties to ensure that all peers arrive at the same result (I’ll use the notationA ∨ Bto indicate merging stateAinto stateB):

* Commutativity: states can be merged in any order;A ∨ B = B ∨ A. If Alice and Bob exchange states, they can each merge the other’s state into their own and arrive at the same result.
* Associativity: when merging three (or more) states, it doesn’t matter which are merged first;(A ∨ B) ∨ C = A ∨ (B ∨ C). If Alice receives states from both Bob and Carol, she can merge them into her own state in any order and the result will be the same.4
* Idempotence: merging a state with itself doesn’t change the state;A ∨ A = A. If Alice merges her own state with itself, the result will be the same state she started with.

Mathematically proving that a merge function has all these properties might sound hard. But luckily, we don’t have to do that! Instead, we can just combine CRDTs that already exist, leaning on the fact that someone has proven these things for us.

Speaking of CRDTs that already exist: let’s learn about one!

### Last Write Wins Register

A register is a CRDT that holds a single value. There are a couple kinds of registers, but the simplest is the Last Write Wins Register (or LWW Register).

LWW Registers, as the name suggests, simply overwrite their current value with the last value written. They determine which write occurred last using timestamps, represented here by integers that increment whenever the value is updated.5Here’s the algorithm:

* If the received timestamp is less than the local timestamp, the register doesn’t change its state.
* If the received timestamp is greater than the local timestamp, the register overwrites its local value with the received value. It also stores the received timestamp and some sort of identifier unique to the peer that last wrote the value (the peer ID).
* Ties are broken by comparing the local peer ID to the peer ID in the received state.

Try it out with the playground below.

JavaScript is required to run this demo.

Did you get a sense for how LWW Registers work? Here are a couple specific scenarios to try:

* Turn the network off, make a bunch of updates tobob, and then turn it back on. When you send updates fromalice, they’ll be rejected until the timestamp exceedsbob’s timestamp.
* Perform the same setup, but once you turn the network back on, send an update frombobtoalice. Notice how the timestamps are now synced up andalicecan write tobobagain!
* Increase the latency and send an update from both peers simultaneously.alicewill acceptbob’s update, butbobwill rejectalice’s. Sincebob’s peer ID is greater, it breaks the timestamp tie.

Here’s the code for the LWW Register:

class

LWWRegister
<
T
>

{


readonly
 id
:

string
;

 state
:

[
peer
:

string
,
 timestamp
:

number
,
 value
:

T
]
;


get

value
(
)

{


return

this
.
state
[
2
]
;


}


constructor
(
id
:

string
,
 state
:

[
string
,

number
,

T
]
)

{


this
.
id
=
 id
;


this
.
state
=
 state
;


}


set
(
value
:

T
)

{


// set the peer ID to the local ID, increment the local timestamp by 1 and set the value


this
.
state
=

[
this
.
id
,

this
.
state
[
1
]

+

1
,
 value
]
;


}


merge
(
state
:

[
peer
:

string
,
 timestamp
:

number
,
 value
:

T
]
)

{


const

[
remotePeer
,
 remoteTimestamp
]

=
 state
;


const

[
localPeer
,
 localTimestamp
]

=

this
.
state
;


// if the local timestamp is greater than the remote timestamp, discard the incoming value


if

(
localTimestamp
>
 remoteTimestamp
)

return
;


// if the timestamps are the same but the local peer ID is greater than the remote peer ID, discard the incoming value


if

(
localTimestamp
===
 remoteTimestamp
&&
 localPeer
>
 remotePeer
)

return
;


// otherwise, overwrite the local state with the remote state


this
.
state
=
 state
;


}

}

Let’s see how this stacks up to the CRDT interface:

* stateis a tuple of the peer ID that last wrote to the register, the timestamp of the last write and the value stored in the register.
* valueis simply the last element of thestatetuple.
* mergeis a method that implements the algorithm described above.

LWW Registers have one more method namedset, which is called locally to set the register’s value. It also updates the local metadata, recording the local peer ID as the last writer and incrementing the local timestamp by one.

That’s it! Although it appears simple, the humble LWW Register is a powerful building block with which we can create actual applications.

### Last Write Wins Map

Most programs involve more than one value,6which means we’ll need a more complex CRDT than the LWW Register. The one we’ll learn about today is called the Last Write Wins Map (or LWW Map).

Let’s start by defining a couple types. First, our value type:

type

Value
<
T
>

=

{


[
key
:

string
]
:

T
;

}
;

If each individual map value holds typeT, then the value of the entire LWW Map is a mapping of string keys toTvalues.

Here’s our state type:

type

State
<
T
>

=

{


[
key
:

string
]
:
 LWWRegister
<
T

|

null
>
[
"state"
]
;

}
;

Do you see the trick? From our application’s perspective, the LWW Map just holds normal values — butit actually holds LWW Registers. When we look at the full state, each key’s state is the state of the LWW Register at that key.7

I want to pause on that for a moment, because it’s important. Composition lets us combine primitive CRDTs into more complex ones. When it’s time to merge, all the parent does is pass slices of incoming state to the appropriate child’s merge function. We can nest this process as many times as we want; each complex CRDT passing ever-smaller slices of state down to the next level, until we finally hit a primitive CRDT that performs the actual merge.

From this perspective, the LWW Map merge function is simple: iterate through each key and hand off the incoming state at that key to the corresponding LWW Register to merge. Try it out in the playground below:

JavaScript is required to run this demo.

It’s kind of difficult to trace what’s happening here, so let’s split up the state for each key. Note, though, that this is just a visualization aid; the full state is still being transmitted as a single unit.

Try increasing the latency and then updating different keys on each peer. You’ll see that each peer accepts the updated value with a higher timestamp, while rejecting the value with a lower timestamp.

JavaScript is required to run this demo.

The full LWW Map class is kinda beefy, so let’s go through each property one by one. Here’s the start of it:

class

LWWMap
<
T
>

{


readonly
 id
=

""
;

 #data
=

new

Map
<
string
,
 LWWRegister
<
T

|

null
>>
(
)
;


constructor
(
id
:

string
,
 state
:
 State
<
T
>
)

{


this
.
id
=
 id
;


// create a new register for each key in the initial state


for

(
const

[
key
,
 register
]

of
 Object
.
entries
(
state
)
)

{


this
.
#data
.
set
(
key
,

new

LWWRegister
(
this
.
id
,
 register
)
)
;


}


}

}

#datais a private property holding a map of the keys to LWW Register instances. To instantiate a LWW Map with preexisting state, we need to iterate through the state and instantiate each LWW Register.

Remember, CRDTs need three properties:value,stateandmerge. We’ll look atvaluefirst:


get

value
(
)

{


const
 value
:
 Value
<
T
>

=

{
}
;


// build up an object where each value is set to the value of the register at the corresponding key


for

(
const

[
key
,
 register
]

of

this
.
#data
.
entries
(
)
)

{


if

(
register
.
value
!==

null
)
 value
[
key
]

=
 register
.
value
;


}


return
 value
;


}

It’s a getter that iterates through the keys and gets each register’svalue. As far as the rest of the app is concerned, it’s just normal map!

Now let’s look atstate:


get

state
(
)

{


const
 state
:
 State
<
T
>

=

{
}
;


// build up an object where each value is set to the full state of the register at the corresponding key


for

(
const

[
key
,
 register
]

of

this
.
#data
.
entries
(
)
)

{


if

(
register
)
 state
[
key
]

=
 register
.
state
;


}


return
 state
;


}

Similar tovalue, it’s a getter that builds up a map from each register’sstate.

There’s a clear trend here: iterating through the keys in#dataand handing things off to the register stored at that key. You’d thinkmergewould work the same way, but it’s a little more involved:


merge
(
state
:
 State
<
T
>
)

{


// recursively merge each key's register with the incoming state for that key


for

(
const

[
key
,
 remote
]

of
 Object
.
entries
(
state
)
)

{


const
 local
=

this
.
#data
.
get
(
key
)
;


// if the register already exists, merge it with the incoming state


if

(
local
)
 local
.
merge
(
remote
)
;


// otherwise, instantiate a new `LWWRegister` with the incoming state


else

this
.
#data
.
set
(
key
,

new

LWWRegister
(
this
.
id
,
 remote
)
)
;


}


}

First, we iterate through the incomingstateparameter rather than the local#data. That’s because if the incoming state is missing a key that#datahas, we know that we don’t need to touch that key.8

For each key in the incoming state, we get the local register at that key. If we find one, the peer isupdatingan existing key that we already know about, so we call that register’smergemethod with the incoming state at that key. Otherwise, the peer hasaddeda new key to the map, so we instantiate a new LWW Register using the incoming state at that key.

In addition to the CRDT methods, we need to implement methods more commonly found on maps:set,get,deleteandhas.

Let’s start withset:


set
(
key
:

string
,
 value
:

T
)

{


// get the register at the given key


const
 register
=

this
.
#data
.
get
(
key
)
;


// if the register already exists, set the value


if

(
register
)
 register
.
set
(
value
)
;


// otherwise, instantiate a new `LWWRegister` with the value


else

this
.
#data
.
set
(
key
,

new

LWWRegister
(
this
.
id
,

[
this
.
id
,

1
,
 value
]
)
)
;


}

Just like in the merge method, we’re either calling the register’ssetto update an existing key, or instantiating a new LWW Register to add a new key. The initial state uses the local peer ID, a timestamp of 1 and the value passed toset.

getis even simpler:


get
(
key
:

string
)

{


return

this
.
#data
.
get
(
key
)
?.
value
??

undefined
;


}

Get the register from the local map, and return its value if it has one.

Why coalesce toundefined? Because each register holdsT | null. And with thedeletemethod, we’re ready to explain why:


delete
(
key
:

string
)

{


// set the register to null, if it exists


this
.
#data
.
get
(
key
)
?.
set
(
null
)
;


}

Rather than fully removing the key from the map, we set the register value tonull. The metadata is kept around so we can disambiguate deletions from states that simply don’t have a key yet. These are calledtombstones— the ghosts of CRDTs past.

Consider what would happen if we really did delete the keys from the map, rather than leaving a tombstone. Here’s a playground where peers can add keys, but not delete them. Can you figure out how to get a peer to delete a key?

JavaScript is required to run this demo.

Turn off the network, add a key toalice’s map, then turn the network back on. Finally, make a change tobob’s map. Sincealicesees that the incoming state frombobis missing that key, she removes it from her own state — even thoughbobnever knew about that key in the first place. Whoops!

Here’s a playground with the correct behavior. You can also see what happens when a key is deleted.

JavaScript is required to run this demo.

Notice how we never remove deleted keys from the map. This is one drawback to CRDTs — we can only ever add information, not remove it. Although from the application’s perspective the key has been fully deleted, the underlying state still records that the key was once there. In technical terms, we say that CRDTs aremonotonically increasingdata structures.9

The final LWW Map method ishas, which returns a boolean indicating whether the map contains a given key.


has
(
key
:

string
)

{


// if a register doesn't exist or its value is null, the map doesn't contain the key


return

this
.
#data
.
get
(
key
)
?.
value
!==

null
;


}

There’s a special case here: if the map contains a register at the given key, but the register containsnull, the map is considered to not contain the key.

For posterity, here’s the full LWW Map code:

class

LWWMap
<
T
>

{


readonly
 id
:

string
;

 #data
=

new

Map
<
string
,
 LWWRegister
<
T

|

null
>>
(
)
;


constructor
(
id
:

string
,
 state
:
 State
<
T
>
)

{


this
.
id
=
 id
;


// create a new register for each key in the initial state


for

(
const

[
key
,
 register
]

of
 Object
.
entries
(
state
)
)

{


this
.
#data
.
set
(
key
,

new

LWWRegister
(
this
.
id
,
 register
)
)
;


}


}


get

value
(
)

{


const
 value
:
 Value
<
T
>

=

{
}
;


// build up an object where each value is set to the value of the register at the corresponding key


for

(
const

[
key
,
 register
]

of

this
.
#data
.
entries
(
)
)

{


if

(
register
.
value
!==

null
)
 value
[
key
]

=
 register
.
value
;


}


return
 value
;


}


get

state
(
)

{


const
 state
:
 State
<
T
>

=

{
}
;


// build up an object where each value is set to the full state of the register at the corresponding key


for

(
const

[
key
,
 register
]

of

this
.
#data
.
entries
(
)
)

{


if

(
register
)
 state
[
key
]

=
 register
.
state
;


}


return
 state
;


}


has
(
key
:

string
)

{


return

this
.
#data
.
get
(
key
)
?.
value
!==

null
;


}


get
(
key
:

string
)

{


return

this
.
#data
.
get
(
key
)
?.
value
;


}


set
(
key
:

string
,
 value
:

T
)

{


// get the register at the given key


const
 register
=

this
.
#data
.
get
(
key
)
;


// if the register already exists, set the value


if

(
register
)
 register
.
set
(
value
)
;


// otherwise, instantiate a new `LWWRegister` with the value


else

this
.
#data
.
set
(
key
,

new

LWWRegister
(
this
.
id
,

[
this
.
id
,

1
,
 value
]
)
)
;


}


delete
(
key
:

string
)

{


// set the register to null, if it exists


this
.
#data
.
get
(
key
)
?.
set
(
null
)
;


}


merge
(
state
:
 State
<
T
>
)

{


// recursively merge each key's register with the incoming state for that key


for

(
const

[
key
,
 remote
]

of
 Object
.
entries
(
state
)
)

{


const
 local
=

this
.
#data
.
get
(
key
)
;


// if the register already exists, merge it with the incoming state


if

(
local
)
 local
.
merge
(
remote
)
;


// otherwise, instantiate a new `LWWRegister` with the incoming state


else

this
.
#data
.
set
(
key
,

new

LWWRegister
(
this
.
id
,
 remote
)
)
;


}


}

}

### Next Steps

We now have two CRDTs in our toolbox:LWW RegisterandLWW Map. How do we actually use them? We’ll cover that in the next post:Building a Collaborative Pixel Art Editor with CRDTsBuilding a Collaborative Pixel Art Editor with CRDTs | jakelazaroff.comCRDTs sound cool, but how are they actually used? Let's learn by building a collaborative pixel art editor.jakelazaroff.com/words/building-a-collaborative-pixel-art-editor-with-crdts/.

## Footnotes

1. They’re also known as CvRDTs (“Cv” standing for “convergent”) and CmRDTs (“Cm” standing for “commutative”), respectively, although I think “state-based” and “operation-based” are the preferred terms.↩
2. There are also delta CRDTs, or hybrid CRDTs, which allow peers to negotiate the subset of the state they need to send each other. That’s one example of blending operation-based and state-based CRDTs. But the fundamental tradeoff remains: sending less data between peers means more constraints on communication.↩
3. Technically, a CRDT can be anything that follows the merging rules described below. This is a working definition; in practice, implementations in object-oriented languages will end up looking something like this.↩
4. Commutativity and associativity might sound the same, and indeed most commutative operations are also associative. But there are a few math operations that are only one or the other. Matrix multiplication, for example, isassociative but not commutativeMatrix multiplication - Wikipediaen.wikipedia.org/wiki/Matrix_multiplication#Non-commutativity. And surprisingly, floating point arithmetic — i.e. any math operator in JavaScript —is commutative but not associativeAssociative property - Wikipediaen.wikipedia.org/wiki/Associative_property#Nonassociativity_of_floating_point_calculation!↩
5. You might ask: why not use the actual time? Unfortunately, accurately syncing clocks between two computers is an extremely hard problem. Using incrementing integers like this is one simple version of alogical clockLogical clock - Wikipediaen.wikipedia.org/wiki/Logical_clock, which captures the order of events relative to each other rather than to the “wall clock”.↩
6. [citation needed]↩
7. If the value type isT, why is the state type a union ofT | null? More on that in a bit!↩
8. You might be wondering: if another peer deleted a key from their map, shouldn’t we remove it from our local map as well? It’s the same reason the state holdsT | null. We’re getting there!↩
9. There are a couple ways mitigate this drawback, both of which are outside the scope of this article. One is “garbage collection”: pruning tombstones from CRDTs, which prevents you from merging states with any changes made before the tombstones were removed. Another is creating an efficient format to encode the data. You can also combine these methods. Research suggests thatthis can result in as little as 50% overhead compared to the “plain” dataCRDTs: The Hard PartsA talk on the latest research on CRDTs, originally given at the Hydra distributed computing conference on 6 July 2020.References: https://martin.kleppmann.co...youtu.be/x7drE24geUw?t=3587. If you’d like to skip ahead and see some of this optimization in action, check out the final part in this series:Making CRDTs 98% More EfficientMaking CRDTs 98% More Efficient | jakelazaroff.comState-based CRDTs grow monotonically, but that doesn't mean they can't be efficient. We'll learn how to compress the pixel editor state by 98%.jakelazaroff.com/words/making-crdts-98-percent-more-efficient/.↩
