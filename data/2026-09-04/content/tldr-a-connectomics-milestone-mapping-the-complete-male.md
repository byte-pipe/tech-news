---
title: 'A connectomics milestone: Mapping the complete male fruit fly brain'
url: https://research.google/blog/a-connectomics-milestone-mapping-the-complete-male-fruit-fly-brain/
site_name: tldr
content_file: tldr-a-connectomics-milestone-mapping-the-complete-male
fetched_at: '2026-09-04T14:48:01.749162'
original_url: https://research.google/blog/a-connectomics-milestone-mapping-the-complete-male-fruit-fly-brain/
date: '2026-09-04'
description: AI agent traffic grew 7,851% in 2025. Security and marketing teams are both flying blind, and the fix runs through visibility, identity, and governance, in that order.
tags:
- tldr
---

# A connectomics milestone: Mapping the complete male fruit fly brain

September 3, 2026

Michał Januszewski and Viren Jain, Research Scientists, Google Research

We partnered with HHMI Janelia and collaborators to publish a complete map of the male fruit fly’s brain and central nervous system, creating the largest brain map to date. Together with ongoing research on other species, such as fish and mice, these wiring maps begin to reveal the mechanics of how all brains work.

## Quick links

* Paper
* Dataset
* Connectomics website
* Video
* News from Google post
* ShareCopy link×
* Copy link×

The common fruit fly,Drosophila melanogaster, has been central toscientific researchleading tomultiple Nobel Prizes. Fruit flies have been a fundamentalmodel organism in genetics, thanks to their stereotypical behavior and short life cycle, and promise to do the same for neuroscience. While the thoughts of this fruit-loving insect might seem far removed from human cognition, the brains of vastly different species share many similarities. Because mapping the 86 billion neurons in a human brain is not yet possible, scientists are using AI to map the brains of smaller organisms, like fruit flies. This will help us decipher how animal nervous systems perceive the world, react to stimuli, and how damaged neural pathways might one day be repaired.

Now, in a project led byHoward Hughes Medical Institute (HHMI) Janelia Research Campus, our team and collaborators have released acomplete wiring diagram of the male fruit fly’s brain and central nervous system. Published inCell, “Sexual dimorphism in the complete connectome of the Drosophila male central nervous system”, is the result of a decade-long partnership that advances the field of connectomics using computing and AI to build cellular-scale maps of entire brains. With over 166,000 neurons and 125 million synaptic connections, this is the largest brain map by number of neurons to date, providing a fundamental resource for scientists to use fruit flies as a model organism for studying how the brain works.

A small subset of cells in the male fruit fly’s brain and central nervous system, as viewed from in front at an angle (left) and from above (right).

Themale fruit fly connectomealso includes theventral nerve cord, analogous to the spinal cord, and so begins to expand from just the brain into how the brain controls the body. The male fly connectome has been annotated and verified, or proofread, by a team of human experts at HHMI Janelia. It can be viewed, explored and downloaded viaNeuroglancer, theopen-source toolwe created to enable researchers tovisualizehuge multidimensional datasets.

The new connectome contains neurons from the central brain (green), optic lobes (purple) and ventral (i.e., central) nerve cord (blue). The new connectome enables linking auditory, visual and olfactory inputs to motor outputs for this key model organism.

This new brain map complements thefemale fruit fly brain mapand recently releasedcomplete female fruit fly brain and nerve cordmap. Having both male and female brains and central nervous systems mapped allows the two to becomparedin places where neurons differ, and used to study the biological mechanisms for fruit flycourtshipand aggression. In parts of the brain that are similar in both sexes, having two complete fruit fly connectomes will allow researchers to begin to see the variability between individuals.

An example of a neuron that is different between the male (green) and previously mapped female (magenta) fruit fly brains. The male neuron has two additional projections. AI enables accurate 3D reconstructions to pinpoint these structural differences.

## Steps toward mapping a full fruit fly brain

Brain mapping, orconnectomics, begins with sectioning a brain into millions of thin slices, taking an image of each section, and using computers and AI to stitch the images together. Our researchers build systems that leverage AI to turn flat electron microscope images into 3D reconstructions, using an evolving suite of techniques to generate accurate neural shapes.

OurAI connectomics toolsincludeflood-filling networks, which use convolutional neural networks to start at a single pixel and identify all other pixels that are part of the same object. In 2019, our Connectomics team released aninitial, fully-automated reconstructionof a female fruit fly brain. By 2020, our team and collaborators released a human-verified map ofhalf a female fruit fly brainwith 25,000 neurons and 21 million connections, a record at the time. Meanwhile, the team was already working on the full, verified brain map for a male fruit fly, which is now complete.

These methods continue to improve. A recent effort incorporatedsynthetic neurons into the training data, successfully improving the speed and accuracy of our state-of-the-art reconstruction system,PATHFINDER. We are also helping to develop new techniques for labeling andannotatingspecific types of neurons. Currently, mapping the fruit fly brain requires years of human effort just to verify and annotate the neural shapes. By reducing this need for manual error correction, research groups can tackle even larger brain mapping projects within reasonable budgets and timelines.

## Looking ahead: Mapping entire fish brains

The field of connectomics is already advancing into vertebrates: organisms with a spinal cord. These are anatomically, evolutionarily and functionally more similar to humans. In a study led byColumbia Universityand published this week inNature, our team helped map a portion of theelephantnose fish’shindbrain that is used in signal processing. This paper, “Connectome analysis of a cerebellum-like circuit for sensory prediction”, shows for the first time how the connectome, a static resource, can be combined with other information to studyneural plasticity and learning, producing the most complete mechanistic model of learning in a vertebrate brain to date.

Larval zebrafish are one of the few vertebrates whose brains are small enough to be mapped from end to end using current techniques. Zebrafish also have the advantage of being transparent in their larval stage, allowing measurements of neural activity during experiments, as captured in theZAPBench dataset. Our upcoming paper with Harvard, “A connectomic resource for neural cataloguing and circuit dissection of the larval zebrafish brain”, is the first whole-brain dataset for a vertebrate that includes the neural structure and molecular type spanning an entire vertebrate brain. Our team also released a preliminary version of a dataset thatcombines neural activity and structurein the same larval zebrafish brain, as an open resource to the research community.

An image from the Fish Fire&Wire dataset, which combines whole-brain electrical activity and neural structure for the same larval zebrafish specimen.

## Conclusion

The male fruit fly connectome is a foundational resource that will support a new era for experimental neuroscience, with future applications in biology, pharmacy and medicine. Three companion papers released today show how the male fruit fly connectome has already been used for research on the neuroscience ofvisual systems,tasteandsocial behavior. Methods developed here will also help advance other projects, such as the upcoming fully proofread map of the zebrafish brain, and mapping a portion of themouse brain. While modeling the 86 billion neurons in the human brain remains out of reach, we are moving toward revealing how brains function and understanding the processes underlying mental ailments, such as Alzheimer’s, depression or schizophrenia. Someday, we hope these efforts lead to new ways to treat cognitive ailments, improve brain health, and support brain repair.

## Acknowledgments

We thank our academic collaborators at HHMI Janelia and elsewhere, and acknowledge core contributions from the Connectomics Team at Google. We are grateful to Hannah Hickey and Elise Kleeman for their help. Thanks to Lizzie Dorfman, Michael Brenner, John Platt, and Yossi Matias for their support, coordination and leadership.

* Labels:
* General Science
* Health & Bioscience
* Machine Intelligence
* Open Source Models & Datasets

## Quick links

* Paper
* Dataset
* Connectomics website
* Video
* News from Google post
* ShareCopy link×
* Copy link×

×

❮

❯

 Two detailed 3D color-coded visualizations of a fruit fly's neural pathways and nerve cord.
 

 Diagram of a male fruit fly nervous system mapping the central brain, optic lobes, and VNC.
 

 Comparison of the dimorphic AOTU008 neural pathway, showing differences between male and female fruit flies.
 

 Multi-colored 3D map of interconnected neurons inside a translucent gray outline of a fruit fly head.