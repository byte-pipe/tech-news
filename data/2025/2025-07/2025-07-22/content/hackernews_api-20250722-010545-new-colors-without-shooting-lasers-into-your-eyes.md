---
title: New colors without shooting lasers into your eyes
url: https://dynomight.net/colors/
site_name: hackernews_api
fetched_at: '2025-07-22T01:05:45.014928'
original_url: https://dynomight.net/colors/
author: dynomight
date: '2025-07-18'
published_date: '2025-07-17T00:00:00+00:00'
description: Can optical illusions take you outside the human color gamut?
tags:
- hackernews
- trending
---

DYNOMIGHT

ABOUT

guide to life

sub​scribe

DYNOMIGHT

ABOUT

guide to life

subscribe

# New colors without shooting lasers into your eyes

# New colors without shooting lasers into your eyes

Jul 2025

* 1.
* 2.
* 3.
* 4.

Subscribe?

ok

(Or try
RSS
 or
substack
)

Mistakes?fix plz(Just want to seewhat happens?)Comments atlemmy,substack.

## 1.

Your eyes sense color. They do this because you have three different kinds of cone cells on your retinas, which are sensitive to differentwavelengths of light.

For whatever reason, evolution decided those wavelengths should beoverlapping. For example, M cones are most sensitive to 535 nm light, while L cones are most sensitive to 560 nm light. But M cones are still stimulated quite a lot by 560 nm light—around 80% of maximum. This means you never (normally) get to experience having just one type of cone firing.

So what do you do?

If you’re a quitter, I guess you accept the limits of biology. But if you likefun, then what you do is image people’s retinas, classify individual cones, and then selectively stimulate them using laser pulses, so you aren’t limited by stupid cone cells and their stupid blurry responsivity spectra.

Fong et al. (2025)choose fun.

When they stimulated only M cells…

Subjects report that [pure M-cell activation] appears blue-green of unprecedented saturation.

If you make people see brand-new colors, you will have my full attention. It doesn’t hurt to use lasers. I will read every report from every subject. Do our brains even know how to interpret these signals, given that they can never occur?

But tragically, the paper doesn’t give any subject reports. Even though most of the subjects were, umm, authors on the paper. If you want to know what this new color is like, the above quote is all you get for now.

## 2.

Or… possibly you can see that color right now?

If you click on the above image, a little animation will open. Please do that now and stare at the tiny white dot. Weird stuff will happen, but stay focused on the dot. Blink if you must. It takes one minute and it’s probably best to experience it without extra information i.e. without reading past this sentence.

The idea for that animation is not new. It’splagiarizedbased on Skytopia’sEclipse of Titanoptical illusion (h/tSteve Alexander), which dates back to at least 2010. Later I’ll show you some variants with other colors and give you a tool to make your own.

If you refused to look at the animation, it’s just a bluish-green background with a red circle on top that slowly shrinks down to nothing. That’s all. But as it shrinks, you should hallucinate a very intense blue-green color around the rim.

Why do you hallucinate that crazy color? I think the red circle saturates the hell out of your red-sensitive L cones. Ordinarily, the green frequencies in the background would stimulate both your green-sensitive M cones and your red-sensitive L cones, due to theiroverlapping spectra. But the red circle has desensitized your red cones, so you get to experience your M cones firing without your L cones firing as much, and voilà—insane color.

## 3.

So here’s my question: Can that type of optical illusion show you all the same colors you could see by shooting lasers into your eyes?

That turns out to be a tricky question. See, here’s a triangle:

Think of thistriangleas representing all the “colors” you could conceivably experience. The lower-left corner represents only having your S cones firing, the top corner represents only your M cones firing, and so on.

So what happens if you look different wavelengths of light?

Short wavelengths near 400 nmmostlyjust stimulate the S cones, but also stimulate the others a little. Longer wavelengths stimulate the M cones more, but also stimulate the L cones, because the M and L cones haveoverlapping spectra. (That figure, and the following, are modified fromFong et al.)

When you mix different wavelengths of light, you mix the cell activations. So all the colors you cannormallyexperience fall inside this shape:

That’s the standardhuman color gamut, inLMS colorspace. Note that the exact shape of this gamut is subject to debate. For one thing, the exact sensitivity of cells is hard to measure and still a subject of research. Also, it’s not clear how far that gamut should reach into the lower-left and lower-right corners, since wavelengths outside 400-700 nm still stimulate cells a tiny bit.

And it gets worse. Most of the technology we use to represent and display images electronically is based onstandard RGB (sRGB) colorspace. This colorspace,by definition, cannot represent the full human color gamut.

The precise definition of sRGB colorspace is quite involved. But very roughly speaking, when an sRGB image is “pure blue”, your screen is supposed to show you a color that looks like 450-470 nm light, while “pure green” should look like 520-530 nm light, and “pure red” should look like 610-630 nm light. So when your screen mixes these together, you can only see colors inside this triangle.

(The corners of this triangle don’t quite touch the boundaries of the human color gamut. That’s because it’s very difficult to produce single wavelengths of light without using lasers. In reality, the sRGB specification say that pure red/blue/green should produce a mixture of colors centered around the wavelengths I listed above.)

What’s the point of all this theorizing? Simple: When you look at the optical illusions on a modern screen, you aren’tjustfighting the overlapping spectra of your cones. You’re also fighting the fact that the screen you’re looking at can’t produce single wavelengths of light.

So do the illusions actually take you outside the natural human color gamut? Unfortunately, I’m not sure. I can’t find much quantitative information about how much your cones are saturated when you stare at red circles. My best guess is no, or perhaps just a little.

## 4.

If you’d like to explore these types of illusions further, I made a page in which you can pickanycolors. You can also change the size of the circle, the countdown time, if the circle should shrink or grow, and how fast it does that.

You can try ithere. You can export the animation to an animated SVG, which will be less than 1 kb. Or you can just save the URL.

Some favorites:

* Red inside, reddish-orange outside
* Red inside, green outside
* Green inside, purple outside

If you’re colorblind, I don’tthinkthese will work, though I’m not sure. Folks with deuteranomaly have M cones, but they’re shifted to respond more like L cones. In principle, these types of illusions might help selectively activate them, but I have no idea if that will lead to stronger color perception. I’d love to hear from you if you try it.

Subscribe?

ok

(Or try
RSS
 or
substack
)

Mistakes?fix plz(Just want to seewhat happens?)Comments atlemmy,substack.

 My 9-week unprocessed food self-experiment


What I really want to know is: What benefit would I get from making my diet better?

The idea of “processed food” may simultaneously be the most and least controversial concept in nutrition. So I did a self-experiment alternating between periods of eating whatever and eating only “minimally processed” food, while tracking...

 Scribble-based forecasting and AI 2027


math or intuition?

AI 2027 forecasts that AGI could plausibly arrive as early as 2027. I recently spent some time looking at both the timelines forecast and some critiques [1, 2, 3]. Initially, I was interested in technical...

 The AI safety problem is wanting


(not knowing or succeeding)

I haven’t followed AI safety too closely. I tell myself that’s because tons of smart people are working on it and I wouldn’t move the needle. But I sometimes wonder, is that logic really unrelated...

 Thoughts on the AI 2027 discourse


what we need is more commentary on the discourse

A couple of months ago (April 2025), a group of prominent folks released AI 2027, a project that predicted that AGI could plausibly be reached in 2027 and have important consequences. This included a set...

 Optimizing tea: An N=4 experiment


what brewing temperature is best?

Tea is a little-known beverage, consumed for flavor or sometimes for conjectured effects as a stimulant. It’s made by submerging the leaves of C. Sinensis in hot water. But how hot should the water be?...

 My more-hardcore theanine self-experiment


coffee is bad

Theanine is an amino acid that occurs naturally in tea. Many people take it as a supplement for stress or anxiety. It’s mechanistically plausible, but the scientific literature hasn’t been able to find much of...

 Limits of smart


molecules and chaos

Take me. Now take someone with the combined talents of Von Neumann, Archimedes, Ramanujan, and Mozart. Now take someone smarter again by the same margin and repeat that a few times. Say this Being is...

 Rewarding ideas


Do we need new incentives for creating information?

If you were in South America 12,000 years ago and you discovered where a bunch of glyptodonts were hiding or you figured out a better glyptodont hunting method, you could tell your tribal band and...

 My 16-month theanine self-experiment


randomized and blinded, N=1

The internet loves theanine. This is an amino acid analog that’s naturally found in tea, but now sold as a nutritional supplement for anxiety or mood or memory. Many people try theanine and report wow...

 Car trouble


And how not to fix it

Some time ago—I'm not sure when exactly—my car started rattling. It would only rattle: 1. When the engine was on, sitting idle, or 2. When accelerating with just the right amount of throttle. This rattle,...

 Counterintuitive effects of minimum prices


they lower utilization

The Attorney General of Massachusetts recently announced that drivers for ride-sharing companies must be paid at least $32.50 per hour. Now, if you're a hardcore libertarian, then you probably hate with the minimum wage. You...

 OK, I can partly explain the LLM chess weirdness now


("make LLMs play better with one weird trick")

We recently talked about a mystery: All large language models (LLMs) are terrible at chess. All, that is, except for gpt-3.5-turbo-instruct, which for some reason can play at an advanced amateur level. This is despite...

 Something weird is happening with LLMs and chess


are they good or bad?

A year ago, there was a lot of talk about large language models (LLMs) playing chess. Word was that if you trained a big enough model on enough text, then you could send it a...

 The real data wall is billions of years of evolution


Careful with those human analogies

Say you have a time machine. You can only use it once, to send a single idea back to 2005. If you wanted to speed up the development of AI, what would you send back?...

 Fahren-height


(celsi-pour?)

The Internet is well into middle-age, and yet doesn’t seem to have answered humanity’s most pressing question: If you pour boiling hot water from various heights, how much does it cool in flight?

 Fancy math doesn't make simple math stop being true


on butts and instrumental variables

What are you supposed to do when someone disagrees with you using a bunch of math you can’t understand? I’ve been thinking about that recently because of the NordICC colonoscopy trial. It took 85k Europeans...

 Are language models good at making predictions?


politics more than science

To get a crude answer to this question, we took 5000 questions from Manifold markets that were resolved after GPT-4’s current knowledge cutoff of Jan 1, 2022. We gave the text of each of them...

 Grug on diet soda and autism


why bad and why so much promote

grug try to not yell about bads in science news too much because why make same yells over and over? and grug have no new learns, just feel people maybe sometimes not use old learns...

 My stupid noise journey


A tale of bad choices

Interested in how to be a big dumb idiot and over-complicate things and waste time and money and endure tons of stress and some real physical pain all by thinking that you’re cleverer than you...

 The second system problem


Building a safe AI ≠ preventing all unsafe AI

In The Vulnerable World Hypothesis, Nick Bostrom imagines we found a technological "black ball"—say a way to make a nuclear weapon with just some glass, some metal, and a battery. He concludes that society in...

 I still think it's very unlikely we're observing alien aircraft


They'd have to be messing with us.

Some suggest there might be alien aircraft on Earth now. The argument goes something like this: A priori, there’s no reason there shouldn’t be alien aircraft. Earth is 4.54 billion years old, but the universe...

 Why didn't we get GPT-2 in 2005?


We probably could have

The ancient Romans were never great at building ships and never tried to explore the Atlantic. The basic reason seems to be—why bother? The open ocean has no resources and is a vast plane of...

 First-principles on AI scaling


How likely are we to hit a barrier?

It's hard not to feel blinkered by recent AI progress. Every week there seems to be an AMAZING NEW SYSTEM with UNPRECEDENTED CAPABILITIES. It's impossible not to wonder what the future holds. Until recently, I...

 Your friend the language model


The world is running out of khakis

I originally wrote this as part of a much longer post on LLM scaling laws and possible barriers/trajectories for progress. The idea was to provide the minimal background necessary to understand all that stuff. But...

 Winner take all science


Is it helpful for things to work this way?

By the early 1950s, it was known thanks to people like Miescher, Levene, and Chargaff that genes were carried by long polymers in the cell nucleus. It was also known that those polymers had a...
