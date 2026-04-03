---
title: The ear does not do a Fourier transform - by galen
url: https://www.dissonances.blog/p/the-ear-does-not-do-a-fourier-transform
site_name: hackernews
fetched_at: '2025-10-31T11:10:12.885017'
original_url: https://www.dissonances.blog/p/the-ear-does-not-do-a-fourier-transform
author: galen
date: '2025-10-31'
description: 'Sensory coding 2: electric boogaloo'
---

# The ear does not do a Fourier transform

### Sensory coding 2: electric boogaloo

galen
Sep 20, 2024
23
2
4
Share

Let’s talk about how the cochlea computes!

The tympanic membrane (eardrum) is vibrated by changes in air pressure (sound waves). Bones in the middle ear amplify and send these vibrations to the fluid-filled, snail-shaped cochlea. Vibrations travel through the fluid to the basilar membrane, which remarkably performsfrequency separation1: the stiffer, lighter base resonates with high frequency components of the signal, and the more flexible, heavier apex resonates with lower frequencies. Between the two ends, the resonant frequencies decrease logarithmically in space2.

Resonant frequencies of the basilar membrane. Outer, larger numbers are frequencies (Hz). Inner, smaller numbers are distance along the unrolled basilar membrane (mm). From
lecture slides
.

The hair cells on different parts of the basilar membrane wiggle back and forth at the frequency corresponding to their position on the membrane. But how do wiggling hair cells translate to electrical signals? This mechanoelectrical transduction process feels like it could be from a Dr. Seuss world: springs connected to the ends of hair cells open and close ion channels at the frequency of the vibration, which then cause neurotransmitter release. Bruno calls them “trapdoors”. Here’s a visualization:

It’s clear that the hardware of the ear is well-equipped for frequency analysis. Nerve fibers serve asfiltersto extract temporal and frequency information about a signal. Below are examples of filters (not necessarily of the ear) shown in the time domain. On the left are filters that are more localized in time, i.e. when a filter is applied to a signal, it is clear when in the signal the corresponding frequency occurred. On the right are filters that have less temporal specificity, but are more uniformly distributed across frequencies compared to the left one.

Filters as a function of time. Left: mostly high temporal precision (short duration), but less uniform tiling of frequencies. Right: mostly low temporal precision (long duration), but more uniform tiling of frequencies.
Lewicki 2002
.

Wouldn’t it be convenient if the cochlea were doing a Fourier transform, which would fit cleanly into how we often analyze signals in engineering? But no 🙅🏻‍♀️! A Fourier transform has no explicit temporal precision, and resembles something closer to the waveforms on the right; this is not what the filters in the cochlea look like.

We can visualize different filtering schemes, or tiling of the time-frequency domain, in the following figure. In the leftmost box, where each rectangle represents a filter, a signal could be represented at a high temporal resolution (similar to left filters above), but without information about its constituent frequencies. On the other end of the spectrum, the Fourier transform performs precise frequency decomposition, but we cannot tell when in the signal that frequency occurred (similar to right filters)3. What the cochlea is actually doing is somewhere between a wavelet and Gabor. At high frequencies, frequency resolution is sacrificed for temporal resolution, and vice versa at low frequencies.

In each large box, each rectangle represents a filter. The human ear does not perform a Fourier transform, but rather employs filters that are somewhere between a wavelet and Gabor. From
Olshausen & O’Connor 2002
.

Why would this type of frequency-temporal precision tradeoff be a good representation? One theory, explored inLewicki 2002, is that these filters are a strategy toreduce the redundancyin the representation of natural sounds. Lewicki performed independent component analysis (ICA) to produce filters maximizing statistical independence, comparing environmental sounds, animal vocalizations, and human speech. The tradeoffs look different for each one, and you can kind of map them to somewhere in the above cartoon.

ICA on environmental sounds (rustling brush, rain, etc.) and human speech (various American English dialects) result in wavelets, while animal vocalizations (rainforest mammals) result in something closer to a Fourier transform. From
Lewicki 2002
.
Examples of filters shown above.

It appears that human speech occupies a distinct time-frequency space. Some speculate that speech evolved to fill a time-frequency space that wasn’t yet occupied by other existing sounds.

+: animal vocalizations, x: environmental sounds, o: human speech.
Lewicki 2002
.

To drive the theory home, one that we have been hinting at since the outset: forming ecologically-relevant representations makes sense, as behavior is dependent on the environment. It appears that for audition, as well as other sensory modalities, we are doing this. This is a bit of a teaser for efficient coding, which we will get to soon.

We’ve talked about some incredible mechanisms that occur at the beginning of the sensory coding process, but it’s truly just the tiny tip of the ice burg. We also glossed overhowthese computations occur. The next lecture will zoom into the biophysics of computation in neurons.

1

We call thistonotopic organization, which is a mapping from frequency to space. This type of organization also exists in the cortex for other senses in addition to audition, such asretinotopyfor vision andsomatotopyfor touch.

2

The relationship between human pitch perception and frequency is logarithmic. Coincidence? 😮

3

One could argue we should be comparing to a short-time Fourier transform, but this hasresolution issues, and is still not what the cochlea appears to be doing.

23
2
4
Share
Previous
Next
