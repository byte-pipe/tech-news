---
title: Mullvad exit IPs as a fingerprinting vector | tmctmt
url: https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/
site_name: hackernews_api
content_file: hackernews_api-mullvad-exit-ips-as-a-fingerprinting-vector-tmctmt
fetched_at: '2026-05-15T11:42:15.568321'
original_url: https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/
date: '2026-05-15'
published_date: '2026-05-14T00:00:00+00:00'
description: Mullvad is one of the few VPN providers that offers multiple exit IPs for its servers. If two people connect to the same server, they will usually end up with different public IPs. With only 578 servers (compared to Proton VPN’s 20,000), this kind of vertical scaling makes sense to avoid cramming too many users onto one IP, which would be a problem on sites with overzealous IP blocks and ratelimits.
tags:
- hackernews
- trending
---

# Mullvad exit IPs as a fingerprinting vector

2026-05-14

Mullvad is one of the few VPN providers that offers multiple exit IPs for its servers. If two people connect to the same server, they will usually end up with different public IPs.

With only 578 servers (compared toProton VPN’s 20,000), this kind of vertical scaling makes sense to avoid cramming too many users onto one IP, which would be a problem on sites with overzealous IP blocks and ratelimits.

Surprisingly, the exit IP you are given is not randomized each time you connect to the server, but deterministically pickedbased on your WireGuard key, whichrotates every 1 to 30 days(unless you use a third-party client, in which case it never rotates).

But wait.. if each server assigns you an independently picked static exit IP, wouldn’t just a few of those be enough to uniquely identify you among every other Mullvad user?

## Putting it to the test

I wrote a script that repeatedly changes my pubkey and fetches exit IPs for a set of 9 servers. Leaving it running for a night produced data points for 3650 pubkeys, which is enough to map out the exit IP range for each server:

Hostname

Start IP

End IP

# IPs

au-syd-wg-101

103.136.147.5

103.136.147.64

60

cl-scl-wg-001

149.88.104.4

149.88.104.14

11

de-ber-wg-007

193.32.248.245

193.32.248.252

8

dk-cph-wg-002

45.129.56.196

45.129.56.226

31

fi-hel-wg-201

185.65.133.10

185.65.133.75

66

us-lax-wg-001

23.234.72.36

23.234.72.126

91

us-nyc-wg-602

146.70.168.132

146.70.168.190

59

us-sjc-wg-302

142.147.89.212

142.147.89.224

13

za-jnb-wg-002

154.47.30.145

154.47.30.155

11

The pool sizes add up to over 8.2 trillion exit IP combinations for these servers, so you’d think each pubkey would be assigned a unique combination of IPs since the odds of a collision are so astronomicaly low. And yet, somehow all the pubkeys I tested were assigned just one of284 combinations.

What’s going on here?

## Different IPs, same proportion

You can calculate a numerical position for an exit IP by counting its distance from the pool’s starting IP.

For example, the IP103.136.147.53assigned byau-syd-wg-101would have a 1-based index of 49 (X.X.X.53 - X.X.X.5 + 1).

Now, if you take the IP positions for any of the 284 combinations linked above, and you divide them by pool size, a common ratio emerges:

Server

IP

Position

Pool size

Ratio

au-syd-wg-101

103.136.147.53

49

60

0.816

cl-scl-wg-001

149.88.104.12

9

11

0.818

de-ber-wg-007

193.32.248.251

7

8

0.875

dk-cph-wg-002

45.129.56.220

25

31

0.806

fi-hel-wg-201

185.65.133.63

54

66

0.818

us-lax-wg-001

23.234.72.109

74

91

0.813

us-nyc-wg-602

146.70.168.179

48

59

0.813

us-sjc-wg-302

142.147.89.222

11

13

0.846

za-jnb-wg-002

154.47.30.153

9

11

0.818

Each IP lands within the same percentile of its pool, in this case, the 81st.

This explains the limited number of combinations, Mullvad will only assign neighboring exit IPs across all its servers. But why?

## Feature or bug?

Curiously, the serverscl-scl-wg-001andza-jnb-wg-002consistently share IP indexes with each other across all 284 observed IP combinations.

The thing they have in common is a pool size of 11, and this gives us a clue about what’s happening.

In any language, if you initiate an RNG with a static seed, a rand-between call with the same bounds will always produce the same result:

use
 rand::{Rng, SeedableRng};

use
 rand::rngs::StdRng;

fn
 
main
() {

 
let
 seed 
=
 
1234
;

 
for
 _ 
in
 
1
..
100
 {

 
let
 
mut
 rng 
=
 StdRng::seed_from_u64(seed);

 
let
 number 
=
 rng.random_range(
0
..
1000
);

 
println!
(
"
{}
"
, number) 
// will always print 56

 }

}

So, the shared indexes between these two servers indicate that Mullvad is probably using some sort of seed-based RNG to pick exit IP indexes, where the seed is the pubkey (or possibly the tunnel address) and the upper bound parameter is the pool size.

This is fairly straightforward, but what happens when the bounds are changed?

use
 rand::{Rng, SeedableRng};

use
 rand::rngs::StdRng;

fn
 
main
() {

 
let
 seed 
=
 
12345
;

 
for
 bound 
in
 
10
..
100
 {

 
let
 
mut
 rng 
=
 StdRng::seed_from_u64(seed);

 
let
 number 
=
 rng.random_range(
0
..
bound);

 
let
 ratio 
=
 number 
as
 
f64
 
/
 bound 
as
 
f64
;

 
println!
(
"
{}
 
{:.3}
 "
, number, ratio)

 }

}

5 0.500 
5 0.455 
6 0.500 
6 0.462 
7 0.500 
7 0.467 
8 0.500 
9 0.529 
9 0.500 
10 0.526 
10 0.500 
11 0.524 
11 0.500 
12 0.522 
12 0.500 
13 0.520 
13 0.500 
14 0.519 
14 0.500 
15 0.517
...

As it turns out, the entropy pool of the RNG is unaffected by the bounds you provide, and at least in Rust, the same float is generated on each first call and used as a multiplier scale for the bounds, like so:min + round((max - min) * float)(this may be a giant oversimplification)

This lines up with the behavior we’ve seen in Mullvad’s exit IP picking algorithm, so it’s safe to say that this is the cause of it.

Rust as the backend language makes sense too, considering thatthe clientis also written in it.

The thing is, almost none of my programmer friends were able to accurately describe whatrandom_rangewould produce in the second code snippet, and the actual behavior took me by surprise too. It’s reasonable to think that each increment to the bounds would skew with the entropy and result in a different number, even though that’s not what happens.

Is it possible that the Mullvad devs shared this common misconception, while actually intending for there to be an unbounded number of exit IP combinations? I don’t know, but it’s a funny thought.

## Correlating identities

I made a tool that can deduce the minimum and maximum float value for a given combination of IPs, available athttps://tmctmt.github.io/mullvad-seed-estimator/.

This particular set of IPs in the screenshot resolves to a float value between 0.2909 and 0.2943 for a difference of 0.0034, which means that 0.34% of Mullvad users share these IPs. At a ball park estimate of a 100,000 active Mullvad users, this equates to 340 users.

This is definitely not as unique as I originally thought, but at the same time, >99% accuracy is really not that bad?

As an example, imagine that you are a moderator on a forum and you suspect that a new face is actually a sockpuppet of a user you banned the day prior. You check the IP logs, and despite using different Mullvad servers, both accounts resolve to the overlapping float ranges0.4334 - 0.4428and0.4358 - 0.4423. This gives you a >99% chance that they are the same person.

Now apply this to IP logs obtained through data breaches and legal channels and you can see how you could get deanonymized behind a VPN through similar correlation attacks.

## Protecting yourself

* Avoid switching servers more than once per pubkey
* Force rotate your pubkey by logging out of the Mullvad app

#privacy