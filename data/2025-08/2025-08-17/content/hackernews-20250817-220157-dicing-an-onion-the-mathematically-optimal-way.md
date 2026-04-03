---
title: Dicing an Onion, the Mathematically Optimal Way
url: https://pudding.cool/2025/08/onions/
site_name: hackernews
fetched_at: '2025-08-17T22:01:57.614864'
original_url: https://pudding.cool/2025/08/onions/
author: The Pudding
date: '2025-08-17'
description: There is more than one way to dice an onion…
---

This is a project about onions and math.

Why? Because tens of millions of people are curious about how to properly dice an onion,according to YouTube.

In 2021, chef and food writer J. Kenji López-Altbroke out some mathto getoptimaluniform piece sizes. But there is more than one way to dice an onion…



# Dicing anthe Mathematically Optimal Way



ByAndrew AquinowithRussell SamoraandJan Diehm



This is an onion.(Well, a simplified cross-section of one.) We’ve cut it in half lengthwise, using a sharp knife to reduce the chance of injury and onion-induced crying.





From here, what’s the best way to dice it? That is, how do we get the most uniform piece size?

For the sake of example, let’s assume our onion has 10 layers. We can represent the layers as concentric circles.

Let’s start with a common approach—vertical cuts.





The piecesnear the center lineare fairly consistent in shape and size.

Butalong the bottomthere are some noticeably larger pieces. When you dice an onion, you’re probably not imagining pieces like these.

This inconsistency can be measured by calculating thestandard deviationof our pieces’ areas.

A note on the standard deviationIn this article when we say standard deviation it refers torelative standard deviation. Relative standard deviation here is the ratio of the standard deviation compared to the average piece size. Because relative standard deviation is a percentage, we can makeunitlesscomparisons about how tightly our piece sizes cluster around the average—we don’t have to make any assumptions about the exact dimensions of our onion.

Without getting too deep in the weeds, just know thata higher standard deviation means more piece size variation.So to obtain the most consistently sized pieces, we want to make the standard deviation assmall as possible.

Adjust the slider below to see how the number of cuts affects the standard deviation. Oh, and don’t forget tocheck out the exploded view toggleto see the variation.


explode


excellent uniformity

std dev:

37.3%



Cuts (vertical)



10





Okay, let’s try a different technique—radial cuts.





The piece size still isn’t very consistent—thosenear the outsideare much larger than thosenear the center.

How does the standard deviation of pieces cut radially compare to those cut vertically?


explode


fair uniformity

std dev:

57.7%



Cuts (radial)



10


cut type


vertical

radial

target height



0%


When making 10 cuts into a 10-layer onion radially, the standard deviation (57.7%) isgreaterthan when cutting vertically (37.3%), which means that our piece size is nowlessconsistent.

But we can improve the radial cut strategy.

Kenji claims that the most uniform pieces can be produced byaiming at a point ~60% of the onion’s radius below the cutting surface.


explode


excellent uniformity

std dev:

34.5%




The pieces now look more consistent, except for a few smaller onesalong the bottom.

Does the math confirm ~60% depth as the superior technique?

Indeed, 34.5% is the smallest standard deviation we’ve seen so far. This finding is further supported by Dr. Dylan Poulsen, an associate professor of mathematics at Washington College, who calculated that the ideal “onion constant” is ~55.731% depth (source,another source). Kenji backs Dr. Poulsen’s method inthis more recent New York Times article.

But we can improve the radial cut strategy even more!

Dr. Poulsen’s analysis is based on makinginfinitely many cutsinto an onion withinfinitely many layers:

A slide from Dr. Poulsen’s breakdown on the math behind onion cutting.

However, in the physical world we’re only capable of making a finite number of cuts, and real onions have a finite number of layers. The diagrams from Kenji’s original claim show 10 cuts being made into an onion with 10 layers. How can we optimize that?

When making 10 cuts into a 10-layer onion, the smallest standard deviation (29.5%) occurs when making radial cuts aimed 96% of the onion’s radius below the cutting surface! 😮


explode


excellent uniformity

std dev:

29.5%



Cuts (radial)



10


cut type


vertical

radial

target height



−96%


Before we explain how we got that result, let’s briefly consider another popular technique: making 1-2 horizontal cuts before vertical,which Kenji recommended in 2016. What does the math say about this strategy? How does combining it with vertical/radial cuts affect our piece size?


explode


excellent uniformity

std dev:

37.3%


Layers



10

Cuts (vertical)



10

Cuts (horiz.)



0

cut type


vertical

radial

target height



0%


How do you find the size of an onion piece?Onions and onion pieces are 3D objects with volumes, but we’re analyzing areas of 2-dimensional cross-sections to simplify the math.When making vertical cuts, we can obtain the area of an onion piece in thebottomlayer by calculating the area under a circular curve in the piece’s horizontal range. When we want the area of an onion piece in anupperlayer, we take the area under its higher circular curve and subtract the area under its lower circular curve.The calculation for radially cut onion pieces is generally the same. However, cutting radially produces diagonal lines. We also add the area under the diagonal line to the left of the piece, and subtract the area under the diagonal line to the right of the piece.

### Optimal techniques

We looked at all 19,320 combinations of onion layer numbers, vertical/radial cut numbers, radial cut depth (as whole number percentages), and horizontal cut numbers that are possible with this model. We then found which technique results in the minimum standard deviation when making 1-10 vertical/radial cuts into an onion with 7-13 layers:

number of layers

7
8
9
10
11
12
13

Cuts
Method
Standard Deviation
10

radial, 96% depth

								96%


radial, 96% depth
29.5%
9

radial, 76% depth

								76%


radial, 76% depth
32.5%
6

radial, 69% depth

								69%


radial, 69% depth
33.2%
7

radial, 87% depth

								87%


radial, 87% depth
33.2%
8

radial, 53% depth

								53%


radial, 53% depth
34.2%
5

radial, 96% depth

								96%


radial, 96% depth
35.4%
4

radial, 53% depth

								53%


radial, 53% depth
41.0%
3

radial, 69% depth

								69%


radial, 69% depth
41.6%
1

vertical, 1 horizontal cut

vertical, 1 horizontal cut
43.5%
2

vertical

vertical
43.5%

### Insights

* It turns out that making horizontal cuts almost never helps with consistency.
* Radial cuts are usually more consistent than vertical cuts, but you have to aim below the center of the onion.
* The ideal radial depth varies depending on the number of layers and cuts—but it’s always ≥48%. As the layer and cut numbers increase and approach infinity, this ideal radial depth converges to the onion constant of ~55.731%, mentioned above.


## The importance of optimal




Armed with this knowledge, we can apply the optimal dicing strategy to any onion. But how big a difference does being mathematically optimal make when it comes to cooking? We got in touch with Kenji via email to find out.

Us—How much does uniformity matter?

Kenji—“It matters far more for winning internet debates and solving interesting math problems than it does for cooking. For home cooks, having onion dice that are a little off from perfect is not really an issue anyone should seriously worry about.”

Oh…

Well anyways, we hoped you enjoyed reading this deep-dive about onions and math. And even if your food still tastes the same, you can show off your optimally uniform onion pieces in your next meal. Good luck finding an infinitely thin knife and an onion made of perfect circles.
