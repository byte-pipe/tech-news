---
title: 'Ask HN: We just had an actual UUID v4 collision... | Hacker News'
url: https://news.ycombinator.com/item?id=48060054
site_name: hnrss
content_file: hnrss-ask-hn-we-just-had-an-actual-uuid-v4-collision-hac
fetched_at: '2026-05-09T07:54:27.896376'
original_url: https://news.ycombinator.com/item?id=48060054
date: '2026-05-08'
description: 'Ask HN: We just had an actual UUID v4 collision...'
tags:
- hackernews
- hnrss
---

Hacker News
new
 | 
past
 | 
comments
 | 
ask
 | 
show
 | 
jobs
 | 
submit
login
Ask HN: We just had an actual UUID v4 collision...
249 points
 by 
mittermayr
 
12 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
221 comments
I know what you're thinking... and I still can't believe it, but...

This morning, our database flagged a duplicate UUID (v4). I checked, thinking it may have been a double-insert bug or something, but no.The original UUID was from a record added in 2025 (about a year ago), and today the system inserted a new document with a fresh UUIDv4 and it came up with the exact same one:b6133fd6-70fe-4fe3-bed6-8ca8fc9386cdWe're using this:
https://www.npmjs.com/package/uuidI thought this is technically impossible, and it will never happen, and since we're not modifying the UUIDs in any way, I really wonder how that.... is possible!? We're literally only calling:import { v4 as uuidv4 } from "uuid";const document_id = uuidv4();... and then insert into the database, that's it.Additionally, the database only has about 15.000 records, and now one collision. Statistically... impossible.Has that ever happened to anyone?! What in the...

 
help

jandrewrogers
 
5 hours ago
 
 | 
next
 
[–]

This is surprisingly common.

The security of UUIDv4 is based on the assumption of a high-quality entropy source. This assumption is invalidated by hardware defects, normal software bugs, and developers not understanding what "high-quality entropy" actually means and that it is required for UUIDv4 to work as advertised.It is relatively expensive to detect when an entropy source is broken, so almost no one ever does. They find out when a collision happens, like you just did.UUIDv4 is explicitly forbidden for a lot of high-assurance and high-reliability software systems for this reason.

reply

LocalH
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

This is why CloudFlare has done what they did with the lava lamp wall. Not that the wall is such a great source of entropy on its own - I'm sure it's not their 
only
 source, but you can never have too many sources of entropy - but it makes it 
visible
 in a way that can grab those who don't fully understand the concepts of RNGs and how entropy plays into that.

The more sources of entropy, the more closely you approach "perfect" randomization. And a large chunk of those entropy sources need to be non-deterministic. Even on the small level, local applications running on local systems, like games, can use things like the mouse coordinates, the timings between button presses, the exact frame count since game start before the player presses Start to greatly enhance randomness while still using PRNGs under the hoodYes, for the latter, that'stechnicallydeterministic (and the older the game considered, the more deterministic it is, see TAS runs of old games obliterating the "RNG"). But when you have fifty different parameters feeding into the initial seed, that's fifty things an attack would have to perfectly predict or replay (and there are other ways to avoid replay attacks that can be layered on top)If CloudFlare had less than 100 different sources of entropy, I'd be disappointed. And that's assuming their algorithm for blending those entropy sources into a single seed value is good

reply

greiskul
 
14 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> you can never have too many sources of entropy

This is so true. And the beauty is that with algorithms, we don't even need to know much about the entropy to be able to extract it.There is the Von Neumann method of generating an unbiased coin from a biased coin. Of throwing it twice, and checking if you got HT or TH. And completely discarding all HH or TT results. It doesn't matter if the coin you are using is 20% or 80%, the result will be a true 50/50.There are more modern algorithms that can be even better (in that they need less coin tosses if you have a very unbalanced coin).And then there is modern cryptographic hashing. Feed it all the bits you can. Collisions end up only happening in the real world if every single one of those bits is identical. So if you have actual entropy being fed, that cannot be controlled, predicted, or replicated, modern cryptography tells you that the end result is unique.

reply

victorbjorklund
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If I understand it the Lava lamps are 90% PR/fun. They have a lot of other sources for entropy that scales better.

reply

pverheggen
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, they also have wave machines, pendulums, and mobiles :)

https://blog.cloudflare.com/harnessing-office-chaos/https://blog.cloudflare.com/chaos-in-cloudflare-lisbon-offic...

reply

euroderf
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Ant farm ? Hamster wheels ? Anything critter-driven should provide some entropy.

reply

throw-the-towel
 
55 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Speaking of ants, Fourmilab (i.e. John Walker, of Autodesk fame) used to provide a random number generator powered by background radiation: 
https://www.fourmilab.ch/hotbits/

reply

BSVogler
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I once read that noise of camera in total darkness is apparently a good source.

reply

amelius
 
26 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You can already have a good entropy source from a single resistor.

https://en.wikipedia.org/wiki/Johnson%E2%80%93Nyquist_noise

reply

unilynx
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The noise probably makes the lava lamp wall just as effective as pointing the camera at the Mona Lisa - the lamps themselves are not that unpredictable frame-to-frame.

reply

LocalH
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

For the record, the lamps and camera are present in their lobby afaik, so you can actually go there, stand in front of them, and slightly affect the entropy.

A cool parlor trick, certainly.

reply

conception
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

https://www.random.org/
 Uses atmospheric noise. These dudes use dice?
 
https://youtube.com/shorts/ncoDq5EcPFg?si=lI6f9cw8dWcaDZ4Y

reply

FuriouslyAdrift
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

https://www.idquantique.com/random-number-generation/product...

reply

__s
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Old games are RTA viable to RNG manip: 
https://m.youtube.com/watch?v=Bgh30BiWG58

reply

dheera
 
58 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The lava lamps are just for show.

You can get entropy just by plugging an oscilloscope into a pile of dirt and cranking the gain up.

reply

adrian_b
 
40 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Any high-gain amplifier can be used, with its input connected to a resistor or a diode.

For instance you can use the microphone input of a PC, together with an additional external amplifier made with an audio amplifier integrated circuit or an operational amplifier integrated circuit and with a diode or a resistor at its input. The microphone input of PCs provides a 5 V voltage that can be sufficient as a power supply for a noise source plugged in it.Such a true RNG can be made on a small PCB with an audio jack, so you can plug it into any PC with microphone input and have a true RNG that you can trust better than the RNG included in modern Intel and AMD CPUs. In the past, many AMD CPUs had defective internal RNGs. Moreover, both for Intel and for AMD it is impossible to verify whether the internal RNG does what it claims to do or it generates predictable pseudo-random numbers.

reply

thecloud
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Thanks for the insight! Mind expanding on what alternatives are being used in high reliability systems instead of UUIDv4?

reply

jandrewrogers
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

In high-reliability systems a criterion for identifier design is easy detection of defective identifiers. This includes buggy systems and adversarial manipulation.

The problem with UUIDs that rely on entropy sources is that it is computationally expensive to detect if the statistical distribution of identifiers is diverging from what you would expect from a random oracle. I've written systems that can detect entropy source anomalies but you'll want to turn it off in production.It is pretty cheap to sanity check most non-probabilistic identifier schemes. UUIDs that use broken hash algorithms (e.g. UUIDv3/5) or leak state (e.g. UUIDv7) are exposed to adversarial exploitation.The identifier scheme is dependent on the use case. Does the uniqueness constraint apply to the instance of the object or the contents of the object? Is the generation of identifiers federated across untrusted nodes? How large is the potential universe of identifiers?The basic scheme I've seen is a 128-bit structured value that has no probabilistic component. These identifiers can be encrypted with AES-128 when exported to the public, guaranteeing uniqueness while leaking no internal state. The benefit of this scheme is that it is usually drop-in compatible with standard UUID even though it is technically not a UUID and the internal structure can carry useful metadata about the identifier if you can decrypt it.Federated generation across untrusted nodes requires a more complex scheme, particularly if the universe of identifiers is extremely large. These intrinsically have a collision risk regardless of how the identifiers are generated.All of the standardized UUID really weren't designed with the requirements of scalable high-reliability systems in mind. They were optimized for convenience and expedience which is a perfectly reasonable objective. Most people don't need an identifier system engineered for extreme reliability, even though there is relatively little cost to having one.

reply

eaf7e281
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> leak state (e.g. UUIDv7)

But according to PostgreSQL, UUIDv7 provides better performance in the database, so is this essentially a trade off between security and speed?

reply

jubilanti
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, because UUIDv7 gives up some random bits in order to include the timestamp, which is done in a way that makes UUIDv7s quick to sort by timestamp.

reply

filcuk
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The latest UUID (7?) Uses half random gen, half timestamp. This not only makes it sortable by creation, but would also make a collision like this impossible.

reply

stanmancan
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's still possible in most implementations of UUIDv7.

UUIDv7 assigns the first 48 bits for the timestamp in milliseconds. You can generate a lot of UUID's in a millisecond though!Then you have another 12 bits that you can use as you wish; "rand_a". The spec has a few methods they suggest on how to use these bits including 12 bits of random data, using it for sub-millisecond timestamps, or creating a monotonic counter, but each have their downsides:- Purely random data means you can still run into collisions and anything within the same millisecond is unordered- Sub millisecond you can run into collisions; there's nothing stopping you from generating two UUID's with the same 62 bits of rand_b data in the same sub-millisecond timestamp.- Monotonic counters can overflow before the next tick, then what? Rollover? Once you roll over it's no longer monotonic and you can generate the same random data within the same monotonic cycle. Also; it's only monotonic to the system that's generating the UUID. If you have a distributed system and they each have their own monotonic cycles then you'll be generating UUID's with the same timestamp + monotonic counter, and again, are relying on not generating the same random data.You can steal some of the 62 bits in rand_b if you want as well; you can use rand_a for sub-millisecond accuracy, and then use a few bits of rand_b for a monotonic counter. There's still a chance of collision here, but it's exceedingly low at the expense of less truly random data at the end.If you want truly collision free, you'd also need to assign a couple of bits to identify the subsystem generating the UUID so that the monotonic counter is unique to that subsystem. You lose the ordering part of the monotonic counter this way though, but I guess you could argue that in nearly 100% of cases the accuracy of sub-millisecond order in a distributed system is a lie anyways.

reply

naniwaduni
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think by the time you're building a system that needs to generate (and persist!) billions of identifiers per millisecond, you're solidly past the point where 
all
 your design decisions need to be vetted for whether they make sense on your extremely exotic setup.

reply

rootlocus
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

We have a dedicated snowflake id generator service that returns batch ids. It's also distributed, each service adds its own instance number to the id. When it overflows it just blocks for the next ms. For our traffic, it's never a bottleneck.

reply

ralferoo
 
1 minute ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Something I use on my own distributed system (where I wanted 64-bit IDs), is use 32 bits for the time in seconds (with an epoch from 2020, so good until 2088), 8 bits for the device ID and 24 bits for a serial number (resets to 0 every time the seconds increments).

That's generally enough IDs per second for most of my edge nodes, but the central worker nodes need more, so I give them a different split and use 4 bits for the device ID and 28 bits for serial number instead.If a node overflows its serial number that second, I kind of cheat and increment the seconds field early. Every time this happens, I persist the seconds field to the database, and when the app restarts, it starts its seconds count at the last persisted seconds plus one. If the current time in seconds is greater than the last used seconds, I also update it and reset the serial number. Works remarkably well for smoothing out very occasional spikes in ID generation while still approximately remaining globally sortable.

ffsm8
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Considering the context I think it's worth pointing out that it's technically not 
impossible
 - it's just even less likely.

Everything in crypto is always a probability - never a certainty

reply

nitsky
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

True, but it makes the specific collision the post observed completely impossible.

reply

stanmancan
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I left a more detailed comment on the parent, but it's definitely not impossible!

reply

ryanmonroe
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The scenario in this post is that the first uuid was created one year before the duplicate uuid. That isn’t possible with v7

reply

stanmancan
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The scenario being the collision itself, the time period isn’t particularly relevant aside from it occurring much quicker than expected.

reply

ffsm8
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You're heavily leaning on "collision like this" to relate to the exact time stamps for your statement to be true.

It's equality possible to interpret the "like this" to the collision itself, without a focus on the 1 year distance between the creation dates.So I guess both views are valid.

reply

JamesSwift
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Surely the scenario where he generates the same number of items as he did between 2025 and now, but did it in 1 tick of v7 UUIDs also runs into it?

reply

matt-p
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

UUIDv7 is arguably better, because it is entropy plus time.

reply

otherme123
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It is what I usually use for its sorting, but some people don't want to leak time info.

reply

lazide
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Sequences, generally.

reply

Groxx
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Yep - I've seen legitimate-looking dups on bad hardware, and "there are a ton of trailing zeros" is also an incredibly common duplicate mode for some UUID libraries (like earlier Go ones that didn't validate the "requested N bytes, returned 3, you must re-request to get N-3 more" return values. it doesn't happen on most hardware or OSes, so people never check it, so it just comes up in production some day with tens of thousands of collisions).

reply

perching_aix
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

How is UUIDv4 to blame for a broken source of entropy? Or am I misinterpreting your words?

reply

hmry
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I wouldn't say it's "to blame", but it is more susceptible to bad RNG.

If the RNG is bad, you'll get more benefit from adding non-random bits than you would from additional badly RNG'd bits.The probability of future collisions also rises the more IDs you generate. If you incorporate non-random bits, you can alleviate that:- timestamps make the collision probability not grow over time as you accumulate more existing UUIDs that could collide- known-distinct machine IDs make the collision probability not grow as you add more machines

reply

jandrewrogers
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I never blamed UUIDv4 for broken entropy sources. A broken entropy source breaks UUIDv4 even if you are using it correctly.

There is a long history of broken entropy sources showing up in real systems. No matter how hard people try to prevent this it keeps happening. Consequently, a requirement for high-quality entropy sources is correctly viewed as an unnecessary and avoidable foot-gun in high-reliability software systems.

reply

hombre_fatal
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Presumably they mean using randomness as unique IDs.

reply

Hizonner
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> UUIDv4 is explicitly forbidden for a lot of high-assurance and high-reliability software systems for this reason.

Hmm. What do those systems do for cryptography? Just assume it won't work and not rely on it at all?

reply

jandrewrogers
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

In these kinds of systems the cryptographic components often aren't even accessible from the software. It isn't a thing you need to worry about.

This makes it easier to audit for use of entropy sources in the software since there really isn't a valid use case for it.

reply

erikerikson
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Super simple to detect and try again.

reply

jandrewrogers
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

A collision is simple to detect but it requires you to actually check, which is expensive at scale. The entire point of UUIDv4 is that you don't have to check for collisions because it should never happen. But if you don't check and it does happen you are in UB territory which is generally very bad.

Ariskof collision before it happens is non-trivial to detect but this is really what you'd want.

reply

throwaway_19sz
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Funny story no one will believe, but it’s true. A good friend of mine joined a startup as CTO 10 years ago, high growth phase, maybe 200 devs… In his first week he discovered the company had a microservice for generating new UUIDs. One endpoint with its own dedicated team of 3 engineers …including a database guy (the plot thickens). Other teams were instructed to call this service every time they needed a new ‘safe’ UUID. My pal asked wtf. It turned out this service had its own DB to store every previously issued UUID. Requests were handled as follows: it would generate a UUID, then ‘validate’ it by checking its own database to ensure the newly generated UUID didn’t match any previously generated UUIDs, then insert it, then return it to the client. Peace of mind I guess. The team had its own kanban board and sprints.

reply

Aurornis
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

> One endpoint with its own dedicated team of 3 engineers

> The team had its own kanban board and sprints.My early jobs were at startups startups with limited resources. Every decision to build something or hire someone was carefully made after much consideration. This story would have looked like fiction to me at the time.Later in my career I joined a startup like this where every new concern someone could think up turned into a new microservice with new hires to form a new team. It didn't matter how small it was, everything was a reason to hire new people and form a new team. I sat in meetings where the express goal of the quarter was communicated as growing the engineering team.It was as weird time. We had this same situation where there were 3-4 person teams who had their own sprints and planning sessions where they would come up with more ways to make work for themselves. Some of them moved so slow that they could spend entire sprints doing tiny changes. Others were working on the most over-engineered solutions you'd ever seen for trivial problems.There was one meeting where I suggested we re-assign some people on a stable project to work on something that we needed urgently, but I got shut down. That would have removed another excuse to hire more people, which would have conflicted with someone's KPIs to grow the engineering team to a specific number

reply

kypro
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> My early jobs were at startups startups with limited resources. Every decision to build something or hire someone was carefully made after much consideration. This story would have looked like fiction to me at the time.

This was pre-2015> Later in my career I joined a startup like this where every new concern someone could think up turned into a new microservice with new hires to form a new team. It didn't matter how small it was, everything was a reason to hire new people and form a new team. I sat in meetings where the express goal of the quarter was communicated as growing the engineering team.This was post-2015---Am I right?You're describing exactly what I've tried to express in various comments. There was a point in the latter half of the 2010s when it became genuinely hard to find tech work where you were building useful stuff. Startups become increasingly absurd and the focuses of their engineering teams even more so.In 2019 I was working for a company who were so desperate to hire new engineers at one point they decided to just start offering jobs to candidates which failed interviews. It was absolutely insane.

reply

swiftcoder
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ah, the heady days when we shipped a new AWS service with a team of 40, and when I came into work the next day we had 120 people and 80 of them were just inventing work out of whole cloth…

reply

mihaaly
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> someone's KPIs to grow the engineering team to a specific number

Sigh!Specific numbers!I believe a more common specific number is the yearly EBITDA or ARR (or some other acronyms in this alley I care zero about to memorize) nowadays, for investor's sake. Like in our company. Since we were acquired - and some time before - the only talk in company meetings are EBITDA, ARR, compared to a number dreamed up by someone and to be reached in 5 years time. Specific financial results in specific timeframe. Our goals are specific numbers being above today's numbers by a chosen margin. The company talk are marketing campaigns and reach, campaign efficiency measurements, pricing strategies, subscription centric licensing, sales strategies, churn, and other slang around customer bullying I also do not care about, also organizational streamlining - what a loaded word! -, bla bla bla, all for the specific sacred number put up on the pedestal.What we have zero talk about? Functionality, engineering.I seriously do not understand these people. Why are they fiddling around with selling software in a niche sensitive to global economic fluctuations insted of selling ... I don't know. Shoes? Or better yet sugary water ... no, better is vitamin water ... no, the trendiest is protein water. That is something that needs no balanced functionality and engineering that is laborous so it is resource intensive to achieve. And is in the way of reaching the sacred number put up there. Engineers are in the way towards our goals. We are pulling back the cart! We are cost center now!!I do not stay long.

reply

wongarsu
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

At some point someone optimizes the system to a global company-wide incrementing 128 bit counter. Instead of needing a costly database lookup against a growing database the microservice just fetches the current counter, increments it by one and hands out the new value. Easy, fast O(1) operation.

This even allows you to shard the service to provide high availability and distribute the service globally to reduce latency. Just give each instance a dedicated id range it can hand out. I'd suggest reserving some of the high bits to indicate data center id, and a couple more bits for id-generator instance within that dc.Wait a second, this starts to look familiar ... does Twitter still do that, or did they eventually switch?

reply

kuratkull
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Define a random 128 bit key that you will never change. Use that key to encrypt 128 bit integers in sequence using AES-128, each one comes out as a, for all practical purposes, unique unpredictable ID.

reply

throw0101c
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> 
At some point someone optimizes the system to a global company-wide incrementing 128 bit counter.

Some UUID versions include time, so there's a bit of a counter in that.

reply

sheept
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Twitter snowflakes haven't changed. Most of the bits go to the timestamp, which I guess is a global incrementing counter as you described

reply

roryirvine
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I've seen similar, buried deep within a major SV tech co.

Their process was a bit more complex because the master list of in-use UUIDs was stored in an external CMDB service run by a different department. They got a daily dump of that db, so were able to check that when generating a "provisional" id. Only once it had been properly submitted to the CMDB did it became "confirmed".They had guardrails in place to prevent "provisional" ids being used in production, and a process for recycling unused "confirmed" ids. Oh, and they did regular audits which were taken very seriously by management.Last I heard, they were 18 months into a 6 month project to move their local database cache to Zookeeper...

reply

DonHopkins
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They should upgrade to Zookeeper II: Zookeepier.

https://www.youtube.com/watch?v=_F-RyuDLR4o

reply

giancarlostoro
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I can believe it, and I often wondered "can I win the UUID misfortune lottery" I wonder if this is equally common with Microsoft's flavor aka GUIDs.

reply

tracker1
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

GUIDs are UUIDs are effectively the same thing... the issues often come down the the means of generation and storage... where UUID have versions with specific implementation details that aren't always followed, MS has internal implementations that also aren't always followed. Also worth being aware of are COMB, SequencialIDs (MS-SQL) and other serialization approaches as well as how they affect indexes in practice.

Alternatives include sequencial number generator services, or sequence services that may be entirely sequencial, etc, but may lead to out of order inserts in practice.Also, generally worth considering UUIDv7 assuming your sotrage and indexing use the time portion at the front of the index process.

reply

mrbonner
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

We have had a service to add two numbers. What make you think this is not realistic? :-)

reply

morkalork
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I too have witnessed a "add two numbers" service! Turns out you can be too extreme with rules for isolating out business logic..

reply

Schiendelman
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Same! It had validation on each number before adding them. Poor design, but that's how it worked.

reply

CodeWriter23
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I get the microservice to ensure this. But 3 people dedicated to it? I guarantee you they spent their days trudging dungeons, playing CoD and ping pong.

reply

LocalH
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'd believe it.

What I'd find harder to believe is that it wasn't really a table with more information than just "list of assigned UUIDs". I'd be really surprised (pleasantly!) if it was only that. I'd figure most startups would make sure that table links to customer info so that they knowwhichcustomer has a specific UUID, for easy searching and crossreferencing with the main db

reply

tomjakubowski
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That sort of table can be quite handy when every entity in the business's data stew is identified with a UUID, and there is no way of telling just from looking at an identifier what kind of entity it is. Particularly when the business has disparate databases and/or microservices with their own sets of UUIDs.

In such businesses, inevitably, someone will ask you to run process X for widget 8dbcd950-14c1-4877-a8b0-90c081ce033c, and that particular identifier will actually be an ID of some associated data, not the widget. You can push back and say, "That isn't a widget identifier, can you please look up the widget identifier?" It's better to be able to look that ID up in your ID ⮕ entity type lookup table, and say "the ID you provided is a widget production run ID, which produced a copy of widget a84969be-137a-41ca-97c4-515497184df9. Can you confirm this is the widget you need process X done for?", with a link to the product-facing widget page.(Also handy for the case where some code was intended to log an ID for one entity, but actually logs the ID for an associated entity with the wrong entity type indicated.)

reply

ssalka
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

At one of my previous jobs, there was a function `createEntityWithRandomUUID` which would basically do the same thing as a light wrapper around database inserts. If a conflict occurred, it would generate a new ID and try again, up to 5 times I think. No logging to indicate whether any conflict actually ever happened.

reply

franktankbank
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Who has the balls to form that team? Were they disbanded?

reply

giancarlostoro
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I will gladly assume that this team was formed after several collisions with UUID's my assumption is that they had tremendous amount of data and enough revenue to justify all of this at least financially. I would have re-evaluated the UUID version used or if adopting Snowflakes would be better at some point.

reply

rekabis
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

You would think they could automate the entire process by “creating-ahead” a certain number of UUID values in the DB, storing them in memory to reduce DB latency, and then recording the assignment to the DB once it had been assigned.

And the microservice could easily be crafted to only accept assignment requests from other known endpoints.

reply

ryandvm
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Pffft - they didn't need to store the whole UUID, just a hash. Dummies.

reply

dd8601fn
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They thought of that, but they were still working on hiring a team to maintain the hashing microservice.

reply

mstaoru
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Hashing microservice deployment was blocked by random generator microservice stuck in Pending because it needed an UUID from UUID microservice which was blocked by hashing.

reply

alserio
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

"Learned a lot today, love Galactus"

reply

mrsvanwinkle
 
6 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

already laughing from parent comment this is well done

reply

_3u10
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

one hash is insufficent, they need k-hashes.

i get the joke, but seriously a bloomfilter would be a good idea.

reply

dboreham
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is the software industry version of "The Onion".

reply

CodesInChaos
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

This is usually caused by an insufficently seeded PRNG.

Are you generating the UUID in the backend, or the frontend? Frontend is fundamentally unreliable for many reasons, including deliberate collisions. So if that case you'll need to handle collisions somehow. Though you can still engineer around common sources of collisions, the specifics depend on the environment.On the other hand making a backend reliable is feasible. What kind of environment is your code running in? Historically VMs sometimes suffered from this problem, though this should be solved nowadays. Heavily sandboxed processes might still run into this, if the RNG library uses an unsafe fallback. Forking processes or VMs can cause state duplication and thus collisions.

reply

_kst_
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

This reminds me of a passage from the book "Pro Git".

<https://git-scm.com/book/en/v2>"Here’s an example to give you an idea of what it would take to get a SHA-1 collision. If all 6.5 billion humans on Earth were programming, and every second, each one was producing code that was the equivalent of the entire Linux kernel history (6.5 million Git objects) and pushing it into one enormous Git repository, it would take roughly 2 years until that repository contained enough objects to have a 50% probability of a single SHA-1 object collision. Thus, an organic SHA-1 collision is less likely than every member of your programming team being attacked and killed by wolves in unrelated incidents on the same night."Deliberate collisions are addressed in the following paragraph.SHA-1 hashes are not random, so the issue of poor pseudo-random number generation doesn't apply as it does to uuidv4. And SHA-1 hashes are 160 bits, vs. 128 for uuidv4.But I love the idea of unrelated wolf attacks.

reply

swiftcoder
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

On the other hand, it turns out that pre-image attacks are quite feasible, and as several people who have thoughtlessly committed the pre-image attack test case files to git can attest… quite problematic

reply

TacticalCoder
 
37 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Hasn't the Git team been hard at work to optionally offer other hashes, like SHA256, in addition to SHA-1?

reply

Lammy
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

> I thought this is technically impossible, and it will never happen

I always hated this meme/mindset, because if you dig in to the history of them you'll see that their original purposewasto collide. They were labels to identify messages in Apollo's distributed computing architecture. UID and later UUIDs were a reversible way to mark an intersection point between two dimensions.Any two nodes in a distributed system would generate the same UID/UUID for the same two inputs, and a recipient of an identified message could reverse the identifier back into the original components. They were designed as labels forephemeralmessages so the two dimensions were time and hardware ID (originally Apollo serial number, later 802.3 hwaddress etc).I think a lot of the confusion can be traced to the very earliest AEGIS implementation where the Apollo engineers started using “canned” (their term, i.e. static or well-known) UIDs to identify filesystems. Over time the popular usage of UUID fully shifted from ephemeral identifiers where duplicates were intentional toward canned identifiers where duplicates were unwanted and the two dimensions were random-and-also-random.

reply

e12e
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Some discussion here:

https://github.com/uuidjs/uuid/issues/546Eg:> FWIW, I just tested crypto.getRandomValues() behavior on googlebot and it is also deterministic(!)

reply

juancn
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Something off on how the RNG is initialized? 
Lack of entropy?

If the rng is not customized it will use:const rnds8 = new Uint8Array(16);
 export default function rng() {
 return crypto.getRandomValues(rnds8);
 }getRandomValues doesn't specify a minimum amount of entropy.

reply

Hizonner
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

It's a near certainty that something is badly wrong with the RNG, and, yes, probably in how it's seeded.

It's probably messing up the cryptography, too.

reply

Onavo
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But defaults should be sane and safe. RNG isn't the sort of thing you want to be messing up. Every JS dev was taught that Math.random is not safe by default, but the crypto package is.

reply

adyavanapalli
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

What you're talking about is so extremely rare that it's much more likely that the entire Earth is destroyed by an asteroid right this inst...

reply

thomasmg
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

It is not quite as rare. I calculated it to be less common than being hit by a meteorite, and added a section about that and the Birthday Paradox to Wikipedia, to the article about UUIDs. It got removed / replaced a few years ago however. (If my source was correct, there was actually a woman hit by a meteorite, but she survived, with a leg injury.)

If you do have a UUID collision, chances are extremely high that it's either a software bug, or glitch in the computer. It could be a cosmic ray. Cosmic rays messing with the computer memory or CPU are actually relatively common.

reply

delichon
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

About as rare as an asteroid typing an ellipsis and clicking the add comment button.

reply

throw0101c
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Well, this joke dates back to (at least) the dial-up days where {#`%${%&`+'${`%& NO CARRIER

reply

xerox13ster
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

That’s just a result of jounce from localized gravity effects and atmospheric pressure disturbances in the moments before impact.

Think the ultrasonic typing hacking scene in Pantheon combined with the keyboard bouncing due to rumbling.

reply

spindump8930
 
2 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It's very common if you improperly seed, as others in the thread brought up! Or in your framing, as rare as earth getting hit if it were surrounded by a sci-fi density asteroid field.

reply

sebazzz
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Well it would be statistically even rarer for that UUID collision to happen and the earth to be destroyed by an asteroid.

reply

crazylogger
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

For a single database using UUIDs, yes, it's astronomically rare. But it's quite a different thing to say that no computer system on Earth has ever experienced a UUID collision. The number of systems out there is also astronomical.

reply

nathanmills
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

>The number of systems out there is also astronomical.

Not even close

reply

moi2388
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Sure it does. Planets are astronomical, and we only have 8 of those in our solar system.

reply

beejiu
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Are your UUIDs generated client side or server side? If it's client side, it could be due to a crawling bot. Googlebot for example executes Javascript using deterministic "randomness".

reply

adzm
 
34 minutes ago
 
 | 
parent
 | 
next
 
[–]

Googlebot's lack of randomness was the conclusion of a previous incident for that package 
https://github.com/uuidjs/uuid/issues/546

reply

dweez
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Good moment to revisit this fun article: 
https://jasonfantl.com/posts/Universal-Unique-IDs/

If the entire universe were turned into a giant computer and did nothing but generate uuids until its heat death, how many bits would you need for the ID space?

reply

ipaddr
 
58 minutes ago
 
 | 
parent
 | 
next
 
[–]

"But are you worried that every human on Earth will be hit by a meteorite right now? That probability is also non-zero, yet it is so infinitesimally small that we treat it as an impossibility."

This might be a bad example because one meteorite could take out the world and given enough time is likely to.

reply

CodeWriter23
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

If you're gonna go there, this is obligatory 
https://www.decisionproblem.com/paperclips/

reply

smokel
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Multiple times have I blamed compilers, cosmic rays, quantum effects, or at the very least an obscure kernel bug, before realizing that I was the source of a bug.

A collision at 15,000 records is so unlikely that I would first suspect something else. Duplicate processing, replayed requests, reused objects, misleading logs, or another code path reusing the identifier.Could you share a bit more of the surrounding code so we can check?

reply

mittermayr
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I fully agree. It makes no sense. Yet...

The only guesses I'm having is that we originally generated UUIDv4s on a user's phone before sending it to the database, and the UUID generated this morning that collided was created on an Ubuntu server.I don't fully know how UUIDv4s are generated and what (if anything) about the machine it's being generated on is part of the algorithm, but that's really the only change I can think of, that it used to generated on-device by users, and for many months now, has moved to being generated on server.

reply

AntiUSAbah
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

You let users generate a UUID?

To be honest, the chance that you are doing something weird is probably higher than you experiencing a real UUID conflict.How did your database 'flag' that conflict?

reply

tracker1
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Likely a unique index... duplicate insert on a primary or 1:! foreign key. I am currently shimming out a process that will add a trackingid for a job service, and just had my method stub retorn Guid.Empty... second time I ran my local test it blew up on the duplicate key... then I switched it to null, then it blew up again... I neglected to exclude null from the unique index on the foreign key.

In any case, it's easy enough to do. I mostly use UUDv7, COMB or NEWSEQUENTIALID ids myself though.

reply

wongarsu
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If it's UUIDv4 and you validate that the UUID is valid and not conflicting I don't really see the issue with user-generated UUIDs. Being able to generate unique keys in an uncoordinated manner is the main selling point of UUIDs

Sure, it's something I'd flag in any design to spend two minutes to talk about potential security implications. But usually there aren't any

reply

JambalayaJimbo
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The whole point of UUIDv4 is that you don't need to check if it's conflicting and can just use them right away. This falls apart if you let untrusted sources of UUIDv4's enter your system IMO

reply

AntiUSAbah
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Validation etc. every thing which should not be controlled by a user, will not be controlled by a user.

reply

mittermayr
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

user-generated (as in: on the user's phone) was only at the very early stages of this product, and we've since moved to on-server. It's a cash-register type of app, where the same invoice must not be stored twice. So we used to generate a fresh invoice_id (uuidv4) on the user's device for each new invoice, and a double-send of that would automatically be flagged server-side (same id twice). This has since moved on to a server-only mechanism.

The database flagged it simply by having a UNIQUE key on the invoice_id column. First entry was from 2025, second entry from today.

reply

tracker1
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Assuming the phone is using the default JS engine, it's whatever is being shimmed for node:crypto package's random bytes method... which is likely weaker.

I wrote a different implementation that cheats by using browser's methods of getting a uuid.https://github.com/tracker1/node-uuid4/blob/master/browser.m...

reply

bitsandbits
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If the server or the user's phone had the wrong time and if the date is used in generating the ID...

reply

whatevaa
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

uuidv4 is random. uuidv7 includes time.

reply

wongarsu
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

If it was two on-device generated UUIDs I could see a collision happening. There have been instances of cheap end devices not properly seeding their random number generators, leading to colliding "random" values. And cases of libraries using cheap RNGs instead of a proper cryptographic RNG, making it even worse

But on a server that shouldn't happen, especially not in 2026 (in the past, seeding the rngs of VMs used to be a bit of an issue). Even if one UUID was badly generated, a truly random UUID statistically shouldn't collide with it. You'd need an issue in both generators

reply

tracker1
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The library is using node:crypto, but with a phone target, that's likely shimmed with a JS implementation...

reply

stubish
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

The UUIDv4 collision is statistically extremely unlikely. What is more likely is both systems used the same seed. This might be just a handful of bytes, increasing the chance of collision to one in billions or even millions.

reply

tracker1
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The shim for node:crypto in the browser is likely a weaker implementation in JS than the node implementation... you can cheat and use the browser itself to get a UUIDv4...

function uuid4() {
 var temp_url = URL.createObjectURL(new Blob());
 var uuid = temp_url.toString();
 URL.revokeObjectURL(temp_url);
 return uuid.split(/[:\/]/g).pop().toLowerCase(); // remove prefixes
 }

reply

lazyjones
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Better check what crypto.js is actually doing in your exact setup. Weak polyfills exist...

reply

zie
 
29 minutes ago
 
 | 
prev
 | 
next
 
[–]

You forgot to use 
https://www.random.org/
 as your source of randomness :)

reply

Geee
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

According to the many-worlds interpretation of quantum mechanics, there's bound to be one branch of universe where every UUID is the same. Can you imagine what those guys are thinking?

reply

BobaFloutist
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Not only that, there's vastly more where every UUID 
except one
 is the same, but they never got to that one because they didn't ever use them.

Or where the first two are unique, but every following one is one of the first two.

reply

nyantaro1
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is why I am not a fan of the Everett approach

reply

zeeveener
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

"Huh, this is just an identity function. Cool. Let's move on."

reply

8organicbits
 
58 minutes ago
 
 | 
prev
 | 
next
 
[–]

I wrote about real world collisions, including that particular library last year (
https://alexsci.com/blog/uuid-oops/
).

There are a bunch of constraints that must be strictly held for UUIDs to be collision resistant, I'd guess there is a problem with your random number generator.

reply

jbverschoor
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Most plausible cause: uuid package depends on some random number generator package, which has recently been compromised in order to make “random” numbers predictable. As a result, many crypto (ssl + currency) projects are compromised due to a supplychain attack.

reply

jbverschoor
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

Changed 3 weeks ago:

uuid/src/rng.ts : the random array is const. Every call will share the same random number. Subsequent call will update your old random code, so if you generated something important... good luckThe old code used to do a slice() which creates a new copy.Might be unintentional. Although I have no idea how this would pass any tests, as you would think to test generating 2 randomnumbers and hope they are not the same.

reply

jbverschoor
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[3 more]

Didn't actually want to write a test myself.. but I miss Claudia confirmed it. Pretty concearning.

Synchronous / serial calls:import rng from './rng';
 
 const a = rng();
 console.log('a after first call: ', Array.from(a));
 
 const b = rng();
 console.log('a after second call:', Array.from(a));
 console.log('b after second call:', Array.from(b));
 
 console.log('a === b (same reference)? ', a === b);
 console.log('a equals b (same contents)? ', a.every((v, i) => v === b[i]));output:a after first call: [
 101, 193, 125, 19, 142,
 136, 181, 140, 209, 224,
 176, 153, 179, 248, 246,
 166
 ]
 a after second call: [
 4, 29, 48, 215, 162, 60,
 64, 23, 78, 137, 2, 186,
 230, 249, 70, 224
 ]
 b after second call: [
 4, 29, 48, 215, 162, 60,
 64, 23, 78, 137, 2, 186,
 230, 249, 70, 224
 ]
 a === b (same reference)? true
 a equals b (same contents)? trueand aynchronous calls:import rng from './rng';
 
 async function getId() {
 const bytes = rng();
 await new Promise(r => setTimeout(r, 0)); // yield to the event loop
 return Array.from(bytes);
 }
 
 const [id1, id2] = await Promise.all([getId(), getId()]);
 console.log('id1:', id1);
 console.log('id2:', id2);
 console.log('identical?', id1.every((v, i) => v === id2[i]));output:id1 captured: [
 61, 116, 151, 35, 153,
 75, 105, 15, 59, 235,
 162, 215, 224, 115, 31,
 122
 ]
 id2 captured: [
 13, 3, 84, 28, 22, 176,
 160, 70, 67, 246, 1, 37,
 38, 61, 171, 23
 ]
 id1 after await: [
 13, 3, 84, 28, 22, 176,
 160, 70, 67, 246, 1, 37,
 38, 61, 171, 23
 ]
 id2 after await: [
 13, 3, 84, 28, 22, 176,
 160, 70, 67, 246, 1, 37,
 38, 61, 171, 23
 ]
 ---
 final id1: [
 13, 3, 84, 28, 22, 176,
 160, 70, 67, 246, 1, 37,
 38, 61, 171, 23
 ]
 final id2: [
 13, 3, 84, 28, 22, 176,
 160, 70, 67, 246, 1, 37,
 38, 61, 171, 23
 ]
 identical? true

reply

toraway
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Shouldn't your test follow the pattern of how rng() is actually being used in the uuid.ts code internally?

Your test is more-or-less contrived to fail given the tradeoff to avoid repeated memory allocations but that doesn't say much about the actual usage in uuid generation since it's not exported for general purpose use.Presumably they had some hot path somewhere where rng() is called in a loop and this optimization made sense with awareness that it could be misused as in your example breaking the contract ensuring randomness, which (hopefully) they're not actually doing anywhere.Unless I'm missing something replacing the package over this with a less vetted implementation seems excessive and possibly even counterproductive.

reply

jbverschoor
 
56 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I don't believe so. Sure it's not an issue after some checks, but it's very easy to shoot yourself in the foot like that. I get the micro-optimization for the allocation.. But it's not clear / documented. At the minimum, the function should be renamed to reflect the inner workings.

The function is a module, and it doesn't do what you'd expect.

reply

jbverschoor
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

https://github.com/uuidjs/uuid/blob/e1f42a354593093ba0479f0b...

becamehttps://github.com/uuidjs/uuid/blob/f2c235f93059325fa43e1106...Welp.. time to patch and update everything again. Another day, another npm-package headache. Very odd()Attack vector: call the rng(), and send the result somewhere. You now have now overwritten someone elses "random number" and know about it. The fun things you can do with those numbers!

reply

jbverschoor
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Seems to be "safe" because of it's not exported, and the results get used in a different way. Still is a bug in my book.

reply

merlindru
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Gotta be a seeding issue. If it's not, and you can prove it, you're about to be a little famous probably :P

reply

tumdum_
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Poorly seeded prng.

reply

jdthedisciple
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

most likely the culprit indeed

reply

nswango
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But I used nonstandard nonces!

reply

leni536
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

It's not happening by chance, there is a bug somewhere.

From what I skimmed the package should just call to the js runtime's crypto.randomUUID(). I think it should always be properly seeded.I think it is extremely unlikely that the runtime has a bug here, but who knows? What js runtime do you use?

reply

serf
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

1 in 4.72 × 10²⁸

1 in 47.3 octillion.i'd be suspecting a race condition or some other naive mistake, otherwise id be stocking up on lottery tickets.(lol at the other user posting at the same time about the lottery ticket.. great minds and all that.)

reply

petee
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

I've always looked at it the the other way - being that lucky would mean you have even less chance of something else lucky happening, good time to save your money

reply

k4rli
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

The lottery ticket part makes no sense. Statistically if such an improbable event just happened to him, then chance of it happening again should be even more improbable.

reply

sowbug
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is probably (ha) a troll thread, but in case anyone here is among today's lucky (ha) 10,000, 
https://en.wikipedia.org/wiki/Independence_(probability_theo...

reply

jaccola
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The chance of him winning the lottery is identical to before, however the reward if he wins is slightly greater.

He would win the lottery money + he gets to tell people who don’t understand independence this incredible story!

reply

angoragoats
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

No, the events are independent. If you have a UUID collide, your chance of winning the lottery if you enter it is exactly the same as it was before the UUID collision.

reply

georgemcbay
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> If you have a UUID collide, your chance of winning the lottery is exactly the same as it was before the UUID collision.

True, but only if you were already going to play the lottery anyway.If you don't normally play the lottery and the UUID collision combined with superstition is what enticed you to play, then the UUID collision will have raised your chances of winning the lottery from 0% to slightly higher than 0%.

reply

angoragoats
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Colloquially, when I say "your chance of winning the lottery" what I mean is "your chance of winning the lottery given that you enter." And I think you probably know this. But I've updated my post to be clear.

reply

jordiburgos
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Please, do not use b6133fd6-70fe-4fe3-bed6-8ca8fc9386cd, I checked my database and I was using it already.

reply

rich_sasha
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

I always thought generating UUIDs at random was insane. I now only use LLMs. The prompt is: "generate a UUID. Make sure no one ever used it anywhere in their code or database. Check your work and think hard about each step. Do not output any reasoning or plain English, only th UUID itself".

You're welcome.

reply

mh2753
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Actually asking ChatGPT this query led it giving me this UUID "550e8400-e29b-41d4-a716-446655440000" which happens to be a very common example UUID

reply

smokel
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Actually, asking this multiple times to ChatGPT gives me different UUIDs every time, and it checked with a web search that they are not found in public data.

reply

wolttam
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The LLM is mechanistically unable to pick something actually random and outside of its training distribution, so... yep.

reply

antonvs
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If you ask it to construct a UUID character by character you should get a somewhat random one, just because of temperature.

reply

recursive
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But all LLM output is token by token, which isn't too far from character by character in the case of a UUID. Why is this different? I do not know.

reply

mittermayr
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I knew it, we're all getting the same cheap UUIDs and the good ones are reserved for the big dogs.

reply

Galanwe
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

uuid.uuidv4() recently switched to "adaptive entropy" instead of "xmax entropy" in an effort to save costs on non-premium users.

reply

antonvs
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You mean you’re not already entropymaxxing? n00b

reply

robshep
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm using 16b55183-1697-496e-bc8a-854eb9aae0f3 and probably some more too. 
I suppose if we all post our list here, then we can all check for duplicates?

reply

jsnell
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You can check 
https://everyuuid.com/
 for collisions.

reply

mittermayr
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

We should all send our already-generated UUIDs to a shared database, we could just put it on Supabase with a shared username/password posted on HN, so we can all ensure that after generating a UUIDv4 locally, it's not used by anyone else. If it's in the database, we know it's taken.

It's a super simple mechanism, check in common worldwide UUID database, if not in there, you can use it. Perhaps if we use a START TRANSACTION, we could ensure it's not taken as we insert. But that's all easy, I'll ask Claude to wire it up, no problem.

reply

broken-kebab
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But then I will claim I have already used all the UUIDs in my spreadsheets, and my lawyer will send cease&desist letters to every database.

reply

volemo
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

A site previously posted here could be useful: 
https://everyuuid.com/

reply

classified
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That UUID should have my name sticker on it. Don't your UUIDs have name stickers?

reply

nu11ptr
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Ultimately it comes down to your entropy source. I always generate and insert in a loop for this reason, if there is a collision, I therefore handle that gracefully.

reply

baq
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

the vm you're running on virtualized all the entropy away.

reply

Imustaskforhelp
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

This seems very likely to be the case.

Something tangentially cool which is related:https://eu.mouser.com/new/leetronics/leetronics-infinite-noi...

reply

rglover
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

A check inside the generator function is the best way I've found to avoid this. Wrap uuid or whatever random generator with a check against an ID cache. If it already exists, just run the generator recursively.

reply

mdavid626
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Or there is some other explanation, eg. somebody messed with the request manually, or with the db.

reply

coldtea
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Were the chances than an npm package is crap factored in?

reply

sudb
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

This is first time I have experienced some vindication that choosing CUID2[1] for one of my projects was actually a good idea.

1.https://github.com/paralleldrive/cuid2

reply

nozzlegear
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

> 
I thought this is technically impossible, and it will never happen,

In an eternal universe, even the most unlikely of events will happen an infinite number of times.

reply

sqquima
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Meta, but if I had a question like this, I'd likely have asked on Twitter or Reddit first. I'll keep in mind using HN as an alternative Q&A site.

reply

glaslong
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Buy some lava lamps

reply

sbuttgereit
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

> I thought this is technically impossible

No, very technically possible... though, with good randomness, very, very unlikely.But nothing technically prevents a UUIDv4 from generating a duplicate value.

reply

danfritz
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Always let your db generate uuids. On postgres this is easy since v18 it supports uuid v7!

There is no need to set uuids through javascript or node imo

reply

hx8
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

There's plenty of reasons to set a unique identifier before database save, or to want a unique identifier that doesn't have a 1-to-1 relationship with your object.

For example, in the idempotent kafka consumer pattern we set a unique ID in the header of every kafka message at the time of message publishing. We then have our consumers do a quick check of the ID against their data store to see if they have processed the message before or not. This way there is no impact if a consumer sees the same message twice. This allows us more flexibility during rebalancing events or replaying old offsets.

reply

NKosmatos
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

> I thought this is technically impossible

Actually it's not impossible, but very very improbable.P.S. You should play a lottery/powerball ticketP.P.S. Whenever I use the word improbable, thehttps://hitchhikers.fandom.com/wiki/Infinite_Improbability_D...comes in mind

reply

sebazzz
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

> P.S. You should play a lottery/powerball ticket

Actually, they should not. That collision and winning the lottery would be even rarer.

reply

lgeorget
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Assuming they are independent events, OP is not more nor less likely to win the lottery now that before running in the collision. I actually have more question if you claim the events in question are NOT independent!

reply

rithdmc
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Inconceivable!

reply

beardyw
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Just a stupid question, but why not append the date, even in seconds as hex. It's just a few bytes and would guarantee that everything OK now will be OK in the future?

reply

flohofwoe
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

You can just use a different UUID variant which includes timestamp data instead (e.g. v1 or v7), there are also variants which include the MAC address.

reply

itsyonas
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Might as well just use uuidv7

reply

ASalazarMX
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But since the randomness is obviously borked, it was much better to use v4 and find out about it after just 15K records instead of X million records later.

reply

mittermayr
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

yeah, any sort of additional semi-random data could've helped prevent this, I'm sure. That, however, is also kind of the idea of UUIDv4, it has lots of randomness and time built in already.

reply

flohofwoe
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

UUID v4 consists of only random bits, no timestamp info.

reply

mittermayr
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

oh, interesting, I didn't know that and this could possibly be part of the problem perhaps depending on what's used as the seed.

reply

beardyw
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

But surely hashing the date still allows for a future collision. Leaving the date as is means it will never collide after that one second has passed.

reply

toraway
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You could do that, but now you're like 90% of the way to maintaining a monotonically increasing number you that could just use as a unique ID instead without any randomness required (and without the additional 128 bits for collision protection via the appended UUID).

So your ID would take like 64 bits for the time unique to the nanosecond plus 128 bits for the UUIDv4 = 192 bits which is a pretty beefy sized ID.(I know you said just append a second count but you will want a predictable/fixed size for your data structure in pretty much any use case so need to decide the upper bound and precision ahead of time)Especially when the alternative is a 128 bit UUIDv4 that's guaranteed unique with proper usage of high quality RNG or a 128 bit UUIDv7 if you have a clock (that's needed for your method anyway) that will be much more forgiving of a flaky source of randomness and more sortable than your monotonic-ish ID for 1/3 fewer bits.Basically, stapling anything onto a UUID is a waste of space if you don't trust it, so might as well drop it completely and use a significantly smaller source of randomness at that point.

reply

kayodelycaon
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

UUID 7 does not hash the date. It uses 48 bits to store a millisecond resolution timestamp. This allows you to sort uuids by time.

reply

pan69
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> but why not append the date

And use uuid v5 to hash it :)

reply

wg0
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Would the UUID v7 be more collision proof? Hard to say because it takes time into account but then the number of entropy bits are reduced hence the UUID generated exactly at the same time have more chance of a collusion because number of entropy bits are a much smaller space hence could result in collusions more easily.

Thoughts?

reply

_kst_
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

UUID v7 relies on knowing what time it is.

Speculation: The most likely scenario for a UUID v7 collision is if UUIDs are generated during a system boot sequence, before the system clock is set to the current time. It's always 1970 somewhere. There are still 62 random bits, and optionally another 12 random bits, but those too could be problematic if the system hasn't generated enough entropy yet.

reply

AntiUSAbah
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

You open up every millisecond a new block. Should be even more unlikely

reply

shortercode
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Fun thing about random is that these things happen. UUIDv7 is less prone to this as it includes both a time component and random. I’ve been using ULID in a few project which has similar attributes to uuidv7 but more space efficient.

reply

not_math
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Reminds me of some code I saw running in production. Every time we added a new entry, we were pulling all the UUIDs from this table, generating a new UUID, and checking for collisions up to 10 times.

reply

dist-epoch
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

It's much more likely that you hit an "impossible bug" due to a bit flip somewhere.

Imagine the database having the old UUID in a memory buffer due to a recent index scan, and a bit flip happened somewhere in the logic which basically copied the old UUID into the memory location of the new UUID, or some buffer addresses got swapped, or the operation which allocated the new UUID received a memory buffer containing the old one, and due to a bit flip the memcpy operation was skipped, or something along that line.Facebook wrote extensively about this, stuff like "if (false) {do_x(); )" and do_x being called. For example their critical RocksDB kv store has extensive redundant protections to defend against such "impossible bugs".

reply

lyfeninja
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Although incredibly rare, it's not impossible so probably best to just plan for collisions. A simply retry should suffice. But I agree I feel like something is going on somewhere else ...

reply

nhumrich
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

> technically impossible

Not at all! Just very unlikely. It's about odds and statistics. Not physics.

reply

ASalazarMX
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

This undersells the word unlikely. It is very, very, very, very unlikely.

reply

AndreyK1984
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Why not to have timestamp-uuid instead ?

reply

dgellow
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

How confident are you that your machines clocks are in perfect sync? What about the risk of clock drift + correction, or hardware issues?

reply

kdps
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I get why sync of mutiple machines matters for ordering and causality, but why is it a problem for uniqueness?

reply

croon
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Not GP, but: not confident. How confident would I be to avoid a (slightly lower entropy) UUID collision while 
also
 avoiding a clock desync landing on the exact same logged millisecond? Very, which is how confident I was about not encountering an UUID collision before this thread, so very++ I guess.

reply

zuzululu
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

just uuidv5

reply

OutOfHere
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

This is why I prefer to use a random base32 string over UUID. At least you get a proper 128 bit entropy instead of just a 122 bit entropy as with UUIDv4. That's a 64x difference in collision probability. I always thought UUIDs were a toy, not for serious use. If you control the strings, you can even make a longer ID.

Also, numerous applications that use a unique ID per record frequently need to check for ID collisions. I know I do for a short URL generator.

reply

ares623
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Buy a lottery ticket

reply

naikrovek
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

The chance of a UUIDv4 collision is very low, but it is never zero.

If everything is done properly, then this is very likely the one and only time anyone involved in the telling or reading of this account will ever experience this.

reply

dalmo3
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

Classic gamblers fallacy!

reply

jaccola
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ironically one of the few comments in this thread that isn’t necessarily the gamblers fallacy!

The chance anyone involved saw or heard about the first one was near zero, now they’ve seen this one the chance they see another is still near zero (I.e unchanged).

reply

kittikitti
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Almost all pseudo-random number generators are absolute garbage. They need you believe they work because the NSA needs backdoors and to foolproof ransomware attacks. This isn't surprising at all to me.

reply

samdhar
 
13 hours ago
 
 | 
prev
 | 
next
 
[15 more]

[flagged]
uncircle
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

Statistically speaking, does extremely unlikely mean impossible? If it were replicable I'd raise my eyebrow, otherwise it's fair game, no?

As someone that enjoys the unterminable complaints about RNG in the video game scene, I would never trust any human's rationalization of random outcomes.

reply

mschild
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Statistically speaking, does extremely unlikely mean impossible?

No, it means extremely unlikely. Collisions can occur, as op just found out, but the chances are so abysmally small that most people don't care.Any application I have worked on, I always had a pre-save check to see if the UUID was already present and generate a new one if it was. Don't think it ever triggered unless a bug was introduced somewhere but good practice anyway.

reply

nubg
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You are replying to an AI bot

reply

harperlee
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Would be cool to have a plugin that shows % of bot per user, based on their history of comments.

reply

ashleyn
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

There could be a problem with the way the system generates entropy for randomness.

reply

nubg
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Question to fellow HNers, do you recognize that this comment was written by AI?

reply

prakka
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No, to be honest. However, as soon as it was pointed out, I checked again and it made sense.

In my opinion, these kind of intuitions have to grow over time. And every time it’s pointed out, you learn. So please, keep pointing it out :).

reply

tirutiru
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I did not. Post-conditioning by your comment and the other one,I can see some signs such attempting to be unusually comprehensive. The 'atoms in your liver' could be an awkward human trying to be poetic about scales.

I still don't see idiomatic markers of AI so that's scary if your claim is correct.

reply

uncircle
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I guess not, and I feel dirty now. I'm logging off for the day.

reply

nottorp
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Interesting enough, I skipped it when scrolling through the comments the first time. I 
think
 I instinctually do that to most karma whoring comments, no matter if manual or LLM generated.

Only noticed it because I did another pass and saw the replies talking about "AI".

reply

piva00
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes but as a feeling (hunch?) not as something my brain analysed and reached a conclusion.

Weird how I'm already somewhat conditioned to spot it on a intuitive level.

reply

mschild
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Kind of. It reads a bit too much like tech support you'd get when asking one for help.

reply

ssenssei
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

when it started going on about all the different cases in the second bullet point... yeah

reply

speedgoose
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes, stupid comparison with atoms in the liver and a bullet list below? I stopped reading.

reply

sublinear
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

> We're using this: 
https://www.npmjs.com/package/uuid

Why? There's a built-in for this.https://nodejs.org/api/crypto.html#cryptorandomuuidoptions

reply

OptionOfT
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

That's what the package uses. And if `crypto.randomUUID()` doesn't exist, it falls back to `crypto.getRandomValues()`, which per the documentation isn't AS strong:

https://developer.mozilla.org/en-US/docs/Web/API/Crypto/getR...So by using the package you actually lose visibility of cases where `crypto.randomUUID()` would fail.

reply

MagicMoonlight
 
3 hours ago
 
 | 
prev
 
[–]

This is why it’s stupid to assume a randomly generated ID is unique just because it is random.

reply

Guidelines
 | 
FAQ
 | 
Lists
 | 
API
 | 
Security
 | 
Legal
 | 
Apply to YC
 | 
Contact

Search: