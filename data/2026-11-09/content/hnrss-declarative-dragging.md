---
title: Declarative Dragging
url: https://declarative-dragging.github.io/
site_name: hnrss
content_file: hnrss-declarative-dragging
fetched_at: '2026-11-09T16:00:48.948157'
original_url: https://declarative-dragging.github.io/
date: '2026-11-04'
description: 'Declarative dragging: an interface author makes an element draggable by specifying which future model states should be accessible by dragging it. Horowitz, Blinn & Heer, UIST 2026 Best Paper.'
tags:
- hackernews
- hnrss
---

# Declarative Dragging

Joshua Horowitz,Andrew Blinn,Jeffrey Heer

★ 
Best Paper Award
, UIST 2026

What if making a diagram draggable was as simple as specifying what it can become?

Drag-and-drop makes the digital graspable. But designing bespoke drag interactions involves a lot of fiddly code to
 handle geometry, feedback, and animations. As a result, many people, from educators to game designers,
 mathematicians to creative tool builders, often don't bother.

Declarative dragginginverts the problem. Rather than programming all that visual behavior directly, you
 simply say, for each element you want to make draggable, which future states of your application dragging it
 should lead to. Our system speculatively renders those states to work
 out where things can go, then combines these possible worlds into a smooth, responsive drag-and-drop
 interaction.

Our goal with this project is to let people keep working within the semantic
 worlds they inhabit, while helping them turn the rules of their worlds into rich tactile interactions in ours.

A five-minute video introducing declarative dragging.

## How it works

D2 ismodel-driven: An interface author makes an element draggable by specifying which future model
 states should be accessible by dragging it. An engine speculatively renders these states to view trees,
 extracts the position of the dragged element in each of these renderings, and uses these to synthesize a
 drag-and-drop interaction, all without detailed work required by the interface author.

 Dragology is a library implementing “declarative dragging”: a new way for interface developers to make
 higher-quality drag-and-drop interactions with less work. Dragology enables model-driven dragging.
 

To provide greater expressive range and customizability, D2 iscomposable: simple model-driven
 drag-and-drop behaviors can be combined to create more complex ones, and modifiers can layer features like
 floating, snapping, and transitions. For more details, seethe paper.

## Dragology demos

We implemented D2 in a library calledDragology, built
 for SVG interfaces on the web.

algebra

twisted trees

bézier curve

braid

card piles

face

trominoes

sprouting tree

See ourdemo galleryfor many more interactives built with
 Dragology.

## Where it came from

 Back in 2022, I had a prototype of a game aimed at making math more tangible, a long-running obsession of
 mine. It had a lot going for it, but the fundamental mechanic, based on selecting transformations from a menu,
 lacked the juicy tactility I craved. I eventually came up with a primitive version of what would become
 model-driven dragging, but implementing it seemed daunting, so it sat on my whiteboard for the next two years,
 haunting me every time I went to make a sandwich.
 
— Andrew

Andrew's whiteboard in June 2023, sketching a basic version of model-driven dragging for tree rewriting.

 On a really nice walk in Seattle back in 2023, Andrew shared his draggy ideas with me. I kept thinking about
 them over the years, but didn't do anything about it. And then last year, it all came together. My buddy Elliot
 was playing with order-preserving maps between trees. I came up with a fun way to draw these structures, but I
 realized I didn't just want to draw them – I wanted to reach in and pull them around, and feel out their
 dynamics (what became the twisted trees demo above). That felt pretty tough, until I remembered Andrew's ideas.
 I got working on a library that, with Andrew's help, grew into declarative dragging.
 
— Josh

Our walk in Seattle in 2023, and Josh's later drawings of order-preserving maps between trees.

## Since the paper

Josh has been working on a variety of new, more intricate mathematical explorables. We've found Dragology
 particularly suited to interfaces that combine parallel representations, where you see the same system from
 different perspectives. In the permutation lab below, interacting with any one representation fluidly updates
 the others, even halfway through a drag, showing their relationships in real time.

 Parallel representations for permutations, updating in tandem.
 
Permutation lab

Andrew has been working to bring declarative dragging to existing applications, including his research on user
 interfaces for programming languages, as well as restarting work on the math game concept that
 kicked it all off.

Hazel
 is an academic programming environment where every edit keeps your
 code meaningful. Using declarative dragging, refactorings become tangible and discoverable.
 

 Not long after submitting the paper, Andrew began working on his 
math game

 again, adapting declarative dragging to the gamepad and moving off the 2D canvas into a 3D world.
 

## Cite

@inproceedings{horowitz2026declarative,
 title = {Declarative Dragging},
 author = {Horowitz, Joshua and Blinn, Andrew and Heer, Jeffrey},
 booktitle = {Proceedings of the 39th Annual ACM Symposium on
 User Interface Software and Technology (UIST '26)},
 year = {2026}
}