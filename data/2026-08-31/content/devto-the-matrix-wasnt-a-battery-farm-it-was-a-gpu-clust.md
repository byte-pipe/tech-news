---
title: The Matrix Wasn't A Battery Farm. It Was A GPU Cluster Made Of Human Brains. - DEV Community
url: https://dev.to/jon_at_backboardio/the-matrix-wasnt-a-battery-farm-it-was-a-gpu-cluster-made-of-human-brains-23e5
site_name: devto
content_file: devto-the-matrix-wasnt-a-battery-farm-it-was-a-gpu-clust
fetched_at: '2026-08-31T17:51:29.378089'
original_url: https://dev.to/jon_at_backboardio/the-matrix-wasnt-a-battery-farm-it-was-a-gpu-cluster-made-of-human-brains-23e5
author: Jonathan Murray
date: '2026-08-28'
description: Nvidia is worth more than most countries because we cannot figure out how to do cheap... Tagged with ai, gpu, movies, matrix.
tags: '#ai, #gpu, #movies, #matrix'
---

Nvidia is worth more than most countries because we cannot figure out how to do cheap inference.

There are eight billion units walking around that do it on 20 watts.

I rewatched The Matrix recently and got stuck on the same thing everyone gets stuck on. Batteries.

Morpheus holds up a Duracell and tells Neo the machines are farming humans for electricity. Bio-electricity, body heat, 25,000 BTUs, the whole speech. It's a great scene. It's also thermodynamic nonsense. You are feeding these people liquefied protein slurry. If you want energy out of the slurry, burn the slurry. Skip the human. The human is a lossy middleman with opinions.

So the machines built a planet-sized data center, wired up billions of pods, wrote an entire simulated 1999 with weather and taxes and dial-up internet, all to run a power plant that loses money on every unit.

No. They were not running a power plant.

They were running inference.

## The 20 watt problem

Your brain runs on about 20 watts. That is a dim light bulb. That is less than the charger for the laptop I am typing this on.

For 20 watts you get real-time vision, real-time audio, language, motor control, a continuously updated physics model of your surroundings, and a persistent world model that predicts what happens next well enough that you can catch a set of keys someone throws at you without thinking about it.

Now price that in silicon. Go look at what a rack costs to do a worse version of any one of those things. We are building gigawatt campuses and negotiating with power utilities like nation states. Meanwhile the reference implementation has been running on leftover sandwich for two hundred thousand years.

So here is what I was thinking about on my drive in, and I am not the first person to land on it, but it fixes the movie completely:

The machines were not harvesting energy. They were harvesting compute.

## Why this makes the plot better

If you want electricity, you want the human sedated. Flat. Minimal metabolic overhead. You do not need to simulate an office job for a battery.

But if you want compute, you need the opposite. You need the brain engaged. Loaded. Running a rich model of a coherent world with stakes and consequences and other agents in it.

Which is exactly what the Matrix is.

The simulation stops being a pacifier and becomes the workload. Every human in a pod is a node processing an unimaginably detailed world model, and the machines are skimming the output. The reason the first version of the Matrix failed, the one Agent Smith says was a perfect world, is not that humans need suffering to feel real. It is that a frictionless world is a trivial workload. Nobody's brain does anything interesting in paradise. They cranked the difficulty up to keep utilization high.

They were not keeping us asleep. They were keeping us busy.

The machines built the world's largest GPU cluster and the cooling solution was a lie about 1999.

## And then I looked up whether anyone was doing this

Full disclosure on how this post came to exist, because I think the process is half the story.

I did not sit down already knowing any of this. I started with a dumb question about a 27 year old movie, said it out loud to an AI, and then spent forty minutes arguing with it. I floated the compute idea. It pushed back on the parts that were wrong and handed me the parts I did not know existed. I asked follow-ups I would never have known to ask a search engine, because I did not have the vocabulary yet. Organoid intelligence. Neuromorphic. Dendritic computation. I did not walk in with those words.

We landed on the compute theory together. I cannot cleanly tell you which half was mine.

That is a genuinely new way to learn a subject and I am not sure we have all noticed. Anyway, verify everything below yourself, because I did, and you should.

This is where it stopped being a fun shower thought and got a little weird.

There is a Swiss outfit called FinalSpark that runs lab-grown human brain organoids as a cloud platform. You can rent time on them. Over the internet. Actual living neural tissue, sitting on electrodes, available as a service.

There is Cortical Labs in Melbourne, who taught a dish of neurons to play Pong and then productized it. You can buy the unit.

The pitch in both cases is the pitch I just made. Orders of magnitude less power than silicon for certain kinds of learning.

The catches are real. The organoids live weeks, maybe months. Nobody has figured out how to program them in any way you would recognize as programming. And neurons are slow, milliseconds per spike against nanoseconds for a transistor, so this was never going to be a drop-in replacement for an H100. Different machine, different job.

There is also the question everyone in the field is politely circling, which is at what point a dish of neurons doing useful work starts to matter morally. FinalSpark's own scientists have said out loud that they think about this. I do not have an answer and I am suspicious of anyone who says they do.

To be clear, I am not advocating for any of this. I want to be on record before someone quotes me in a deposition in 2041.

## The version that probably actually happens

The boring answer is neuromorphic silicon. Loihi, NorthPole, SpiNNaker. Steal the architecture from biology, spiking neurons, memory sitting next to compute instead of across a bus, absurd parallelism. Then implement it in silicon so you get nanoseconds instead of milliseconds. Copy the design, drop the latency, skip the ethics review.

We are already using AI to help design those chips, which is its own recursive little snake eating its tail.

The open question is whether the architecture is the secret or whether the secret is somewhere in the wet chemistry. The neuromodulators, the dendritic computation, all the analog mess that does not draw cleanly on a whiteboard. It is possible we are copying the blueprint and missing the trick.

Anyway. Next time someone tells you AI is a power problem, remember there is a 20 watt reference design walking around inside your skull, and it has never once needed a substation.

Sleep well, and have a nice weekend.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse