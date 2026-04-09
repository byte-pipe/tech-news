---
title: PixiEditor 2.0 - a FOSS Universal 2D Graphics Editor is here! | PixiEditor Blog
url: https://pixieditor.net/blog/2025/07/30/20-release/
site_name: hackernews_api
fetched_at: '2025-08-04T07:04:43.934354'
original_url: https://pixieditor.net/blog/2025/07/30/20-release/
author: ksymph
date: '2025-08-01'
description: PixiEditor 2.0 – A FOSS universal 2D graphics editor
tags:
- hackernews
- trending
---

All Articles


# PixiEditor 2.0 - a FOSS Universal 2D Graphics Editor is here!






Krzysztof Krysiński


July 30, 2025




pixieditor
v2
launch




July 30, 2025





## What is PixiEditor?

Up until today, PixiEditor was known as a pixel-art editor. Version 2.0 is much more than that. It’s a Universal 2D Editor - a brand new category.

It’s not yet another Photoshop alternative. We take the word “Universal” much more seriously. We built an extremely configurable raster/vector render pipeline, which you can adjust for any workflow you can think of.

Our goal is to build a free and open source editor that can handle all of 2D graphics

* Raster
* Vector,
* Animations,
* Procedural (VFX, effects, non-desctuctive editing)

## What can it do?

Need to create a thumbnail for your YouTube video? Done. Edit SVG files? Easy. Create a pixel-art animation spritesheet? You bet.

Or maybe you have a special workflow that requires complex setup? PixiEditor can help you with most demanding needs. In the most of the other image editors, you can only do as much as developers prepared. To extend its functionality you usually need to find appropriate plugin and hope it does what you want to or try finding a clever way to solve your problem.

PixiEditor’s Node Graph on the other hand, gives you full control over the rendering of your image. For example, with Node Graph only, we managed to build a 3D cube texturing workspace with live preview. And it’s just a .pixi file that you can send to anyone.

Q1 summary blog postvery well describes most of the features present in PixiEditor 2.0. But in short:

### Toolsets for any scenario

Switch between Painting, Pixel-art and Vector toolsets. Mix vectors and raster graphics in one file.

#### Vectors

PixiEditor natively supports editing vectors in High DPI, meaning you can edit low-res documents and combine it with vectors that will rendered crisp on the same canvas.

All vectors are non-destructive, they are preserved on separate layers and can be edited anytime.

It includes tools such as:

#### Path tool: Create Bézier Curves and Polygons

#### Line, Ellipse and Rectangle

#### Text

It’s far from end of the list, vectors and vector layers are very powerful in combination withNode Graph

### Node Graph

The Node Graph is one of PixiEditor’s most powerful features. It allows for creating effects previously only possible with specialized software such as game engines.

With classic layers + tools experience you can do very much, but with node graph, you can make almost anything. I’m not joking, it’s just a matter of time until someone runs Doom in it.

#### Basic overview

By connecting nodes you can make complex effects using simple rules. Every layer is a node and it can be connected to other nodes.

##### Procedurally Generated Islands with seasons animation

Fully procedural fire

#### Node Workspaces

To solve the issue of constant need of reattaching nodes to see their effect, we’ve implemented a special node called “Preview” which creates a custom output that can be toggled in the viewport settings

In the video above, there’s only one file that has a graph with multiple outputs. By creating 3 viewports for the same image, you can preview all the outputs at once.

This is a very powerful feature that allows you to create entire workspaces. We’ve made areusable pixel art case studyto demonstrate its use.

### Animations

One of the most requested features in PixiEditor 1.0 was frame by frame animations, and we’ve finally delivered.

But that’s not the end, except classic cels you can utilize node graph to create procedural animations.

You can render them as a video (gif, mp4) or export to spritesheet for your games.

One missing piece of the puzzle is key frame animations and vector animations, but that’s coming later after 2.0 release.

### Pixel Art Toolset

You can create pixel arts with dedicated tools, such as:

#### Brush with pixel-perfect option

#### Transform (scale, move, skew, rotate, perspective) selection and layers

#### Non-destructive, pixel-perfect text tool

## Interested?

Make sure to readQ1 summary blog postfor feature details

## Pixi Labs and Founder’s Pack

One of the big changes that happened over past few months is the birth of Pixi Labs Sp. z o.o. - we’ve established a legal entity for PixiEditor related stuff.

But don’t worry, PixiEditor is still independent, free and open-source. We are not going to change that. However there are a lot of challenges when it comes to building open-source projects. The biggest is funding.

Over 1 year ago I left my job to finally develop PixiEditor full time. I want to keep it that way. I deeply believe in open-source and its importance in the world. Unfortunately we don’t live in a utopia and
I need to start earning money, both to buy myself food, keep PixiEditor infrastructure alive and ideally, hire other PixiEditor contributors.

### How are we planning to earn money?

The deal is simple. We’ll be maintaining and developing PixiEditor for free and in the meantime we will create useful paid extensions and assets that you’ll be able to buy.

It’s a win-win.

### Founder’s Pack

A very first paid extension we’ve just released with 2.0 Release isFounder’s Pack, and is available today.

For the old timers, Founder’s Pack is a upgradedSupporter Pack, so if you’ve purchased Supporter Pack, you’ll get the update for free. We are retiring Supporter Pack as Founder’s Pack replaces it.

#### What does it offer?

Let’s start with the juciest things,workspaces.

#### Card Builder

Now no matter if you are Balatro fan, or you are building a card based game, Card Builder workspace makes it easy. It automatically creates a pattern on the back, mirrors all the suits and ranks.

Ask Mushy, he seems to like being a part of a card.

#### 3D Cube Texturing

No need to leave PixiEditor to see the result, rotate the cube and see how your texture fits!

#### Texturing

The concept is simple, you have a drawing area and PixiEditor tiles it on all sides to give you a quick glance if your texture is seamless.

#### Reusable pixel-art animation

A workspace that is set up to quickly create reusable animations based on UV indexing. Works great if you need to create a lot of variations of the same animation.

### Palettes

21 unique palettes ready to use.

### Unique badge inside the app

Get it today

## Join us on the Release Live stream

If you want to see what PixiEditor 2.0 is capable of or you want to ask us a question, join our livestream today (30 July). If you are reading this later, the recording is available, check how it went!

I hope it inspires you to make something cool. Or silly. Or tiny. Or huge. Whatever it is, just have fun.

Make sure to stay till the end as we will be giving away Founder’s Pack and a discount code.

## Some additional info

PixiEditor 2.0 has a bit higher hardware requirements than 1.0, mainly you need a Vulkan compatible GPU (or CPU with integrated graphics that support it) and 64 bit system. If for any reason, 2.0 does not work for you, click on Properties in the Steam library, then Betas and select pixieditor-1.0 beta to downgrade.
We are working hard to support more hardware configurations, but 32-bit systems will no longer be supported.

## Thank you

I would like to thank you from the bottom of my heart for your support along the way. But It’s not the end. If you use PixiEditor and find it useful, consider buying Founder’s Pack as it is the only way to ensure we can keep working on this.

flabbet




 What is PixiEditor?
 What can it do?
 Toolsets for any scenario
 Vectors
 Path tool: Create Bézier Curves and Polygons
 Line, Ellipse and Rectangle
 Text
 Node Graph
 Basic overview
 Procedurally Generated Islands with seasons animation
 Node Workspaces
 Animations
 Pixel Art Toolset
 Brush with pixel-perfect option
 Transform (scale, move, skew, rotate, perspective) selection and layers
 Non-destructive, pixel-perfect text tool
 Interested?
 Pixi Labs and Founder’s Pack
 How are we planning to earn money?
 Founder’s Pack
 What does it offer?
 Card Builder
 3D Cube Texturing
 Texturing
 Reusable pixel-art animation
 Palettes
 Unique badge inside the app
 Join us on the Release Live stream
 Some additional info
 Thank you
