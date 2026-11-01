---
title: Let’s Build a Brain
url: https://aatishb.com/myriad/lets-build-a-brain/
site_name: hnrss
content_file: hnrss-lets-build-a-brain
fetched_at: '2026-11-01T18:53:14.805073'
original_url: https://aatishb.com/myriad/lets-build-a-brain/
date: '2026-10-27'
published_date: '2026-10-21'
description: How simple circuits can create complex behaviors
tags:
- hackernews
- hnrss
---

Myriad
 

# Let’s Build a Brain

 
 

ByAatish BhatiaandArkarup Banerjee

The world is full of surprising behavior:Beavers building dams, songbirds singing, spiders building webs, and you reading this article.

All of these behaviors are orchestrated by neurons firing in the brain. But how exactly do collections of neurons create these complex behaviors?

This is a huge question that researchers are still working on. But over the last half century, neuroscientists have solved some pieces of this puzzle.

In this article, we’ll build a tiny creature called a spark, and we’ll give it a very simple brain. As you’ll see, even this tiny brain can create rich and unexpected behaviors.

### Light eaters

Suppose this spark feeds on light. Its goal in life is to reach the light.

The light-hungry spark needs a way to sense the world. So we’ll give it a rudimentary eye — a single neuron that detects brightness and converts it into electrical pulses.

It also needs a way to move. So we’ll give it another neuron that can wiggle a flipper.

By wiring the firstsensory neuronto the secondmotor neuron, we’ve just assembled our first neural circuit:

### The anatomy of a spark

 

With this simple circuit, the spark wiggles its flipper in proportion to the amount of light.

Can it find the light?

 

If the sparks happen to face the light, they’re drawn towards it. But most of the time, they miss.

Over time, their paths look like this:

 

Only a few paths cross the light. Clearly, we can do a lot better…

### Adding an eye

Here’s the problem: While the spark can speed up, it can’t steer. With one eye and one flipper, it only moves in one direction. But we need it to turn.

What if we give it another eye and flipper?

 

With two eyes, the spark can now sense whether the light is to its left or right. Now, it moves like this:

 

Hmm… that didn’t work. Instead of steering towards the light, it steeredawayfrom it!

 

If you didn’t know how their brains work, you might think that theyfearlight.

Why do they avoid the light? Well, if the light were to the spark’s left, then its left eye would sense more brightness, which means that its left flipper would wiggle faster, and this would cause it to turn right, away from the light. Conversely, if the light were to its right, then it would veer left.

### A crossed connection

But there’s a clever way to make this spark steer towards the light instead.

All we have to do is cross its connections. That is, we wire its left eye to its right flipper, and its right eye to its left flipper.

 

Now, it moves like this:

 

With this simple wiring change, it can finally steer towards the light.

But if you watch these sparks for a while, you’ll notice that there’s a problem.

 

While they can reach the light, they don’t slow down near it. Instead, they charge towards it like comets plunging towards the sun.

If you didn’t know how their brains work, now you might think that they’reattackingthe light.

### Becoming inhibited

Why do they attack the light? The problem lies in thetypeof connection that we used.

To see why, we need to go back to our original spark. Remember how its flipper moved faster when the light got brighter? That’s because its eye and flipper were connected with anexcitatory connection— where more input leads to more output.

 

If the light were a food source, then this spark would accelerate towards it, but it wouldn’t stop to enjoy its lunch.

 

Instead, we want the spark to slow down as it approaches the light. That is, we want its motion to beinhibitedby light.

We can solve this by swapping out the excitatory connection for aninhibitory connection— one where more input leads tolessoutput.

 

With the original excitatory connection, the spark overshoots the light. With the inhibitory one, it slows down and gently comes to a stop.

 

### Finding the light

Now let’s bring back the original two-eyed spark, but this time with inhibitory connections between its eyes and flippers.

 

Now, the flipper closer to the light moves slower, while the flipper on the opposite side moves faster, and this makes the spark turn towards the light.

 
Click to move the light around.
Drag the light to move it around.

Hooray! It can finally steer to the light and come to a stop. You can move the light in the graphic above (or the one below) to watch the sparks react.

 
Click to move the light around.
Drag the light to move it around.

They move as if they’re magnetically attracted to the light. If you didn’t know how their brains work, now you might think that theylovelight.

We’ve now seen four very different behaviors, each achieved by making small changes to the neural circuitry of our virtual creatures.

Attraction
Fear
Aggression
Love
 
 
Note: We’ve added a small amount of noise to the simulation to make the paths look more organic.

If you saw creatures behaving like this in the wild, you might attribute some rudimentary intelligence to them.

But we’ve just shown you how this apparent intelligence arises from the bottom up, with just four neurons and two connections. There’s no magic here. In this view,behavior emerges from neural circuits.

And if a brain with just four neurons can do all this, imagine what your brain can achieve with nearly 100 billion neurons.

### Adding variation

We can take this one step further.

In each of the simulations so far, the sparks all had identical brains. But biology is full of variation: No two brains are the same.

If we allow the connections between neurons to vary in strength, then each spark can react differently to the light.

 

They now have different preferences: The yellower sparks seem to love light more, while the redder sparks keep a cautious distance.

 
Click to move the light around.
Drag the light to move it around.

Just as a thermostat sets a preferred temperature, their brain wiring now determines their preference for light.

If you squint very hard at this, you might be able to see the rudiments of howourbrains encode preferences, such as a love for spicy food or an aversion to smelly cheese.

Of course, biology is far more complex than these simplified sparks. We intentionally gave them very simple brains, so that we can understand how every part works.

Their brains are also frozen in time. In reality, brains can learn: They alter their wiring to gain new skills such as learning to walk, ride a bicycle, or play a piano.

In the next article, we’ll watch this learning process in action, and see how these sparks rewire their brains to find the light.

 
 

Share this article
Link copied!

## Learn more

Thanks for readingMyriad, a blog byAatish BhatiaandArkarup Banerjeeexploring how minds emerge from matter.

Arka is an associate professor of neuroscience at Cold Spring Harbor Laboratory in New York. Check outhis lab’s researchon how asinging mouse in the cloud forests of Costa Rica got its song.

Aatish is a science journalist with a Ph.D. in physics. Previously, he was a graphics editor at The New York Times.Follow Aatish’s workfor more visually-immersive interactive explanations about science.

The sparks that we assembled in this article are based on a series ofthought experimentsby the neuroscientistValentino Braitenbergdescribed in his delightfully quirky 1984 bookVehicles: Experiments in Synthetic Psychology.

While the one-eyed sparks may look peculiar, it’s possible that you and I descended from aone-eyed cyclops-like creaturethat lived 560 million years ago.

If you enjoyed reading this, consider sharing it with a friend.

Share this article
Link copied!