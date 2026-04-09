---
title: We Induced Smells With Ultrasound
url: https://writetobrain.com/olfactory
site_name: hackernews_api
fetched_at: '2025-11-23T11:07:25.156676'
original_url: https://writetobrain.com/olfactory
author: exr0n
date: '2025-11-21'
description: We decided to try to stimulate the olfactory bulb with focused ultrasound. As far as we know, no one seems to have done this kind of stimulation before - even in animals.
tags:
- hackernews
- trending
---

We pointed an ultrasound probe at the scent-processing region of the brain to obtain different sensations. Different focal spots corresponded to different smells, which we’ve replicated first-try on two people and validated with a blind trial. The sensations we obtained are:

The sensation of fresh air, with a lot of oxygen
The smell of garbage, like few-day-old fruit peels
An ozone-like sensation, like you're next to an air ionizer
A campfire smell of burning wood

Here is a video from our blind tasting:

Your browser does not support the video tag.

## The Setup

Smells are processed in the olfactory bulb. We decided to try to stimulate it with focused ultrasound through the skull. As far as we know,no one seems to have done this kind of olfactory stimulation before- even in animals.However, after being able to induce sensations of motion the previous week, it seemed promising to try the same for olfactory.

### The Anatomy

The olfactory bulb, ourtarget, is tucked behind the top of the nose. That turns out to be a pretty inconvenient location for a couple of reasons:

1. The nose doesn’t provide a flat surface for mounting a transducer for stimulation.
2. It's mostly filled with air, which interferes with ultrasound. Ultrasound needs a continuous medium to travel through, and filling the nose with gel seemed rather unappealing.

Instead, we found that you can place the transducer on the forehead and aim the ultrasound downward towards the olfactory bulb. While this isn’t a perfect solution because the frontal sinuses can weaken the signal, careful device positioning above the sinuses still allows us to reach our general target region.

### The ultrasound

We got our first effects using just a handheld probe and some gel, but it quickly became obvious that holding a probe steady by hand makes it nearly impossible to keep the focal spot in the same place.
To improve stability, we improvised a makeshift headset, allowing for more reliable positioning. We switched from gel to a solid, jello-like pad for stability and general comfort. In the end, our headset got a bit hacky:

It ended up having a knife taped to the probe for mechanical supportAt the time, all of our headsets had a knife taped to the probe, as untaping the knife lead to software errors.. At some point we thought of using a mouthguard for fixing the probe relative to the brain. This was a great idea considering the teeth are the only exposed part of the skull, except it turns out you can’t talk about smells while wearing a mouthguard.

To guide placement, we used an MRI of Lev’s skull to roughly determine where the transducer would point and how the focal region (where ultrasound waves actually concentrate) aligned with the olfactory bulb (the target for stimulation).

We found our “sweet spot” to be low-frequency ultrasound focused right below the forehead and angled downward toward the bulbs. Specifically:

* 300 kHz frequency (low enough to penetrate the skull well)
* Focal depth of about 39 mm (where the ultrasound energy converged beneath the forehead)
* 50–55° steering angles (to point the focus down toward the bulbs)
* 5-cycle pulses at a 1200 Hz repetition rate (short, rapidly repeating bursts)

While Albert did not have an MRI available, this general configuration still worked for him with minor adjustments to the focal spot position.

### Safety

The largest chunk of the time was spent on making sure the ultrasound sequences behaved safely and in the manner we expected, split between two directions:

1. Measuring the output field. We put the transducer in a water tank and measured the pressure at the focal spot. With our parameters, it ranged from 150 to 250 kPa, which corresponded to a mechanical index of at most 0.4. That implied that the average intensity at the focal spot was by an order of magnitude lower than what's typically used in tFUS and has been proven safe. We were also far within safety limits on mechanical index and thermal dose.
2. Avoiding the optic nerve by reducing asymmetry in the system: the nerves are further from the middle of the head. The olfactory bulb also has its two components slightly off-center, so a bit of asymmetry was necessary: we focused at an angle of 2 degrees to the side in one of the presets. However, we stayed within the limit of 15 degrees, which is enough not to touch the optic nerves.

## Results

We have managed to induce four different sensations, all of them in two people:

The sensation of fresh air, with a lot of oxygen
The smell of garbage, like few-day-old fruit peels
An ozone-like sensation, like you're next to an air ionizer
A campfire smell of burning wood

We distinguish betweena smellanda sensationhere because, subjectively, they feel different. The smells are strong and localized to the noise, almost like you could sniff around and find the source. The sensations are more diffuse: a weak, slow-onset impression of a smell, often paired with other (likely placebo) feelings, such as a light tingling on the face.

Both smells and sensations are strongest on a light in-breath, so we tested by sitting there, with a probe to the forehead, mildly sniffing. Sometimes there is a slight waft of a smell that comes on over a few breaths, and sometimes it just hits you. The first time Albert smelled the garbage, he jerked his eyes open thinking a garbage truck just drove in!This was indoors.

Many of these scents correspond not to specific receptor types but rather combinations of receptors. We think this is because the focal spot is pretty large—300kHz ultrasound in tissue has a wavelength of 5mm, while the adult human olfactory bulb is roughly 6-14mm in lengthThe olfactory bulb can vary in size by up to 3x, depending on "age and olfactory experience", so perhaps (we're making this up) with more usage your olfactory bulb might actually get bigger, leading to better resolution stimulation!.

We found different scents by steering the beam over ~14 mm (20 degrees at 4 cm radius). The distance between freshness and burning was ~3.5 mm. We ensured that the effect was not placebo with an auditory mask (blasting music through airpods) so you don’t hear the probe, though you cannot distinguish the different focal spots through sound anyways. We then tested discrimination in a trial where Thomas selected the focal spots, and Lev was naming the scents. You can check out the full videohere.

It is remarkable that we could induce different scents with such little steering (40% of the diffraction-limited focal spot sizeAnd potentially even higher, because there was some dead space in between the focal spots, where you don't feel anything.). This suggests that the resolution we have access to is much higher than the spatial resolution of the ultrasound (a kind ofsuper-resolution for neurostim!) In particular, we do not need single-neuron resolution to find an independent basis of scents, upon which we can construct our latent space. To improve this system, the next steps are a more stable setup, increased frequency, more play with focal location, spot size, and stimulus waveform.

### Can you feel the meaning

The reason stimulating olfactory sensations is interesting is not just "VR for smells", as one might initially assume. The nose has400 distinct receptor types, and we can distinguishsubtle combinationsof their activations, so they could serve as a channel of writing directly into the brain, as a means of non-invasive neuromodulation.

The olfactory system potentially allows writing up to 400, if not 800 due to two nostrils, dimensions into the brain. That is comparable to the dimensionality of latent spaces of LLMs, which implies you could reasonably encode the meaning of a paragraph into a 400-dimensional vector. If you had a device which allows for this kind of writing, you could learn to associate the input patterns with their corresponding meanings. After that, you could directlysmell the latent space. A bit of ultrasound, a breath in - and you understood a paragraph.

People are able to develop synesthesia - being able to hear colors and see smells, and it might be possible to extend that to semantics. However, at this stage it is speculative.

One could try to make a similar argument for the eyes: take 400 cones on the retina, hijack them, and you've got yourself a 400-dimensional channel. But we think the nose is better. The olfactory system ismuchsimpler and more directly interfaces with core brain regions, like the hippocampus. The signal through the olfactory system is simply less filtered and processed. If you tried to write arbitrary light intensities into a patch of cones, the next step of the processing would be a convolutional neural network-like structure in the visual cortex, and the signal would get averaged out. The embeddings you'd write would never make it into the higher levels of processing in the brain. You can try to encode the information in a more easily perceptible way, such asChernoff faces, but it would reduce the bandwidth, and learning the remapping would still be very difficult.

In contrast, only a few synapses separate the olfactory receptors from thehippocampusThis is why certain smells bring up such strong memories!, which is responsible for memory, as well as from the amygdala, which does emotional regulation.

Finally, personally speaking, the authors use their eyes and ears more than their noses during office workRaphael Hotter noted that this is in fact a general statement, as the usage of eyes and ears extends beyond office work.. The nose is an underutilized channel that imposes fewer bad priors (spatial/tonal maps) than the visual, auditory, and somatosensory.

We found four scents in a couple of days. With a little more engineering, it should be possible to increase the bit rate of olfactory stimulation bya lot.

If we gain control of all 400 basis vectors, we might be able tosmell meaning.And we’ve already covered the first one percent.

## Acknowledgements

We thank Raffi Hotter, Aidan Smith, and especially Mason Wang for thoughtful feedback on this blogpost.
