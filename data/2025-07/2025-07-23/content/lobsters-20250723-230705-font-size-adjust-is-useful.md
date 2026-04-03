---
title: font-size-adjust Is Useful
url: https://matklad.github.io/2025/07/16/font-size-adjust.html
site_name: lobsters
fetched_at: '2025-07-23T23:07:05.218886'
original_url: https://matklad.github.io/2025/07/16/font-size-adjust.html
date: '2025-07-23'
description: In this article, I will describe a recent addition to CSS, the font-size-adjust property. I am also making a bold claim that everyone in the world misunderstands the usefulness of this property, including Google, MDN, and CSS Specification itself. (Just to clarify, no, I am not a web designer and I have no idea what I am talking about).
tags: design, web
---

# font-size-adjust Is UsefulJul 16, 2025

In this article, I will describe a recent addition to CSS, thefont-size-adjustproperty. I am also making a bold claim that
 everyone in the world misunderstands the usefulness of this property,
 includingGoogle,MDN, andCSS Specification itself. (Just to clarify, no, I am not a web
 designer and I have no idea what I am talking about).

Let’s start with oversimplified and incorrect explanation offont-size(seehttps://tonsky.me/blog/font-size/for details). Let’s say you
 specifiedfont-size: 96px. What does that mean? First,
 draw a square 96 pixels high:

Then, draw a letter “m” somewhere inside this box:

m

This doesn’t make sense? I haven’t told you how large the letter m
 should be? Tiny? Huge? Well, sorry, but that’s really how font size
 works. It’s a size of the box around the glyph, not the size of the
 glyph. And there isn’t really much consistency between the fonts as to
 how large the glyph itself should be. Here’s a small “x” in the three
 fonts used on my blog at 48px font size:

x

x

x

They are quite different! And this is wherefont-size-adjustcomes in. If I specifyfont-size-adjust: ex-height
 0.5,I ask the browser to scale the font such that the letter “x” is
 exactly half of the box. This makes the fonts comparable:

x

x

x

## Me vs. Everyone

Now, the part where I foolishly disagree with the world! The way
 this property is described inMDNand elsewhere is as if it only matters for the font fallback. That
 is, if you havefont-family: Futura,
 sans-serif,one potential problem could be that
 the fallback sans-serif font on the user’s machine will have very
 different size from Futura. So, the page could look very differently
 depending on whether fallback kicks in or not (and fallback can kick
 intemporarily, while the font is being loaded). So, the
 official guideline is, roughly,

When using font fallback, find a value offont-size-adjustthat makes no change for the first font
 of the fallback stack.

I don’t find this to be a particularly compelling use-case! Make
 sure to vendor the fonts used, specify@font-faceinline in a<style>tag inside the<head>to avoid extra round trips, addfont-display: block;and FOUC is solved for most people. Otherwise, you might want to
 stick tosystem-uifont.

A use-case forfont-size-adjustI findmuchmore compelling is that you probably are going to use several fonts
 on a web-page. And you also mightchangefonts in the
 future. And they will have different intrinsic size because that’s
 how the things are. Part of the mess is avoidable by pinning the
 meaning of font size. So, the guideline I’d use is:

Stickfont-size-adjust: ex-height
 0.53;into your CSS reset, right next tobox-sizing:
 border-box.

Why0.53? That’s the invariant ratio for Helvetica, but
 any number in that vicinity should work!
