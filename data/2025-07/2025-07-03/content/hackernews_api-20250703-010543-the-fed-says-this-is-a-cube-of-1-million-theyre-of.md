---
title: The Fed says this is a cube of $1 million. They're off by half a million. - Calvin Liang
url: https://calvin.sh/blog/fed-lie/
site_name: hackernews_api
fetched_at: '2025-07-03T01:05:43.351566'
original_url: https://calvin.sh/blog/fed-lie/
author: Calvin Liang
date: '2025-07-02'
description: Trust me, I counted.
tags:
- hackernews
- trending
---

# The Fed says this is a cube of $1 million. They're off by half a million.


 Trust me, I counted.


 





At the Federal Reserve Bank of Chicago’s Money Museum, there’s a big transparent cube on display. It’s filled with tightly packed stacks of$1\$1$1bills, claiming to contain$1,000,000\$1{,}000{,}000$1,000,000.










The plaque proudly declares:

Have you ever wondered what one million dollars looks like?
You don’t have to wonder anymore because you can see it right in front of you!

But I don’t trust signs. I trust counting.

## The Big Count

I first tried counting the stacks right there in the room. The cube was tall, so I had to step back to see the whole thing, squinting at the stacks, trying to follow each row. I lost track almost immediately.

Also, people were starting to look at me funny. Apparently, staring intensely at a pile of cash while muttering numbers isn’t normal museum behavior.

Then, I tried with a photo. I zoomed all the way in on my phone, dragging my finger across the screen, mentally tallying as I went.

Still couldn’t keep count.

All I wanted was a way to click on things in a photo and have the number go up.

You’d think this would already exist, a browser based tool for counting things.

Turns out it… doesn’t. At least, not as a web app I can find on Google.

There are some clunky old Windows programs, niche scientific tools, and image analysis software that assumes you’re trying to count cells under a microscope, not people, penguins, or stacks of $1 bills in a Federal Reserve cube.

So I madeDot Counter.

It’s stupidly simple: upload an image, click to drop a dot, and it tells you how many you’ve placed. That’s it. But somehow, nothing like it existed.

I originally made it to investigate this very cube, but I figured other people might need to count stuff in pictures.

Now it’s yours too.

Go forth. Count wisely.

Count your enemies. Count your blessings. Count your stacks of cash.

Because when someone tells you it’s a million dollars, you might want to double check.

## Final Tally






Assuming each bundle contains100100100bills*, that’s

102
×
8
×
19
×
$
100
=
$
1,550,400
102 × 8 × 19 × \$ 100 = \$ 1{,}550{,}400
102
×
8
×
19
×
$100
=
$1
,
550
,
400

*The straps on them are blue which is thestandard for a stack of100100100$1\$1$1bills. Unless these are some sort of ultra-rare$64.5\$64.5$64.5bundles. In which case, I have follow-up questions.

So yeah. They’re off by50%50\%50%.

That’s$550,400\$550{,}400$550,400in extra cash.

## Hmm 🤔

Imagine the meeting.

“Hey so… we’re $550,400 over budget on the million-dollar cube project.”

### Bad at math?

If you knock222from each dimension (basically pealing away the outermost layer of money bundles), the math actually gets kinda close

100
×
6
×
17
×
$
100
=
$
1,020,000
100 \times 6 \times 17 \times \$ 100 = \$ 1{,}020{,}000
100
×
6
×
17
×
$100
=
$1
,
020
,
000

but since dollar bills are much wider than they’re tall, it wouldn’t look like a cube anymore.

### Inflation?

Maybe the Fed is playing the long game.

At the Fed’s2%2\%2%inflation target, this cube will be worth$1\$1$1million in today’s dollars in:

log
⁡
1.02
(
1,550,400
1,000,000
)
=
22
 
years
\log_{1.02}(\frac{1{,}550{,}400}{1{,}000{,}000})=22 \thinspace\text{years}
lo
g
1.02
​
(
1
,
000
,
000
1
,
550
,
400
​
)
=
22
years

Can’t wait to come back in 2047 and say: “Nice. Nailed it.”

### Technicality?

Sure, it does technically contain$1,000,000\$1{,}000{,}000$1,000,000.

And also$550,400\$550{,}400$550,400of bonus money.

Which is kind of like ordering a burger and getting three.

I mean, sure, free stuff. But it’s not what you asked for.

### Empty inside?

What if it’s hollow?

You can only see the outer stacks. For all we know, the middle is just air and crumpled-up old newspaper.

A money shell. A decorative cube. A fiscal illusion. The world’s most expensive piñata (but don’t hit it, security is watching).

And get this: just the outermost layer is already worth:

[
(
102
×
8
×
19
)
−
(
100
×
6
×
17
)
]
×
100
=
$
530,400
[(102 \times 8 \times 19) - (100 \times 6 \times 17)] \times 100 = \$ 530{,}400
[(
102
×
8
×
19
)
−
(
100
×
6
×
17
)]
×
100
=
$530
,
400

You’d only need a 3-layer-thick shell to blow past a million:

[
(
102
×
8
×
19
)
−
(
96
×
2
×
13
)
]
×
100
=
$
1,300,800
[(102 \times 8 \times 19) - (96 \times 2 \times 13)] \times 100 = \$ 1{,}300{,}800
[(
102
×
8
×
19
)
−
(
96
×
2
×
13
)]
×
100
=
$1
,
300
,
800

## Howwouldyou make a million dollar cube?

Turns out U.S. dollars are extremely non-cube-friendly. Each bill is6.14in6.14\thinspace\text{in}6.14inwide by2.61in2.61\thinspace\text{in}2.61intall, a nice and even aspect ratio of:

6.14
2.61
≈
2.3524904...
\frac{6.14}{2.61} \approx 2.3524904...
2.61
6.14
​
≈
2.3524904...

Each 100-bill bundle is0.43in0.43\thinspace\text{in}0.43ininches thick.

### Best I could do

* 909090bundles per stack
* 7×167 \times 167×16stacks
* 90×7×16×$100=$1,008,00090 \times 7 \times 16 \times \$ 100 = \$ 1{,}008{,}00090×7×16×$100=$1,008,000

Which gives you a lovely almost-cube:

* 42.97in42.97\thinspace\text{in}42.97in(3.58ft)(3.58\thinspace\text{ft})(3.58ft)wide
* 41.76in41.76\thinspace\text{in}41.76in(3.48ft)(3.48\thinspace\text{ft})(3.48ft)deep
* 38.70in38.70\thinspace\text{in}38.70in(3.225ft)(3.225\thinspace\text{ft})(3.225ft)tall

Not perfect. Not terrible. At least it’s honest, unlike that other cube.

## Conclusion

So what’s in the cube?

Maybe it’s$1\$1$1million.

Maybe it’s an empty box with a money shell.

Most likely it’s$1.55\$1.55$1.55million.

All I know is I built a tool, did the math, and triple-checked the stacks.

The sign says you don’t have to wonder.
But I did anyway.

And now… you don’t have to either.
