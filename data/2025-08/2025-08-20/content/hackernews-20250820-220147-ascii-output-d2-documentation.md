---
title: ASCII output | D2 Documentation
url: https://d2lang.com/blog/ascii/
site_name: hackernews
fetched_at: '2025-08-20T22:01:47.815001'
original_url: https://d2lang.com/blog/ascii/
author: Terrastruct
date: '2025-08-20'
published_date: '2025-08-02T00:00:00.000Z'
description: In the latest release of D2 (0.7.1), we introduce ASCII outputs.
---

In the latest release of D2 (0.7.1), we introduce ASCII outputs.

Any output file with extensiontxtwill use the ASCII renderer to write to it.

Here is an example of their rendering from theD2 Vim extension. The user opens a.d2file and opens a preview window, which updates upon every save.

## Code documentation​

Perhaps the most useful place for ASCII diagrams is in the source code comments. Small
simple diagrams next to functions or classes can serve to be much clearer than describing
a flow.

Here again the Vim extension demonstrates a functionality to write some d2 code and
replace the selection with the ASCII render.

## Unicode and standard ASCII​

The default character set of ASCII renders is unicode, which has nicer box-drawing
characters. If you'd like true ASCII for maximum portability, you can specify this with
the flag--ascii-mode=standard.

## Limitations​

Alpha

Note that the ASCII renderer should be considered in alpha stage. There will be many
corner cases, areas of improvements, and outright bugs. If you enjoy using it, we'd
appreciate you taking the time to file any issues you run into:https://github.com/terrastruct/d2/issues.

The ASCII renderer is a downscale of the layout determined by the ELK layout engine with
some post-processing to further compact it.

* No styles are supportedSome will never be, e.g.animatedandfontdon't make sense in ASCII.Some may in the future with limited scope, e.g. colors when rendered to terminal.By extension, themes are mootSome should be considered TODOs, e.g.double-borderandmultiple
* Some will never be, e.g.animatedandfontdon't make sense in ASCII.
* Some may in the future with limited scope, e.g. colors when rendered to terminal.By extension, themes are moot
* By extension, themes are moot
* Some should be considered TODOs, e.g.double-borderandmultiple
* Uneven spacingSometimes the downscaling results in a box with uneven spacing, e.g. a rectangle with
width 5 and the label is 2 chars. Due to discrete coordinate space in ASCII renders, some
outputs may look less even than their SVG counterparts.
* Sometimes the downscaling results in a box with uneven spacing, e.g. a rectangle with
width 5 and the label is 2 chars. Due to discrete coordinate space in ASCII renders, some
outputs may look less even than their SVG counterparts.
* Certain things just can't renderSpecial text, e.g. Markdown, Latex, CodeImages and iconsUML classes and SQL tablesRight now these aren't special-handled -- whether removing them from the diagram or
using some placeholder is the right choice is tbd.
* Special text, e.g. Markdown, Latex, Code
* Images and icons
* UML classes and SQL tables
* Right now these aren't special-handled -- whether removing them from the diagram or
using some placeholder is the right choice is tbd.
* Not all shapes are supportedHere's what all the shapes render as in ASCII. Some of these, like cloud and circle,
have curves that don't translate well to ASCII. We render these as a rectangle and add
a little icon for what it's supposed to represent in the top-left. These are subject to
change. For now we recommend rendering without custom shapes.
* Here's what all the shapes render as in ASCII. Some of these, like cloud and circle,
have curves that don't translate well to ASCII. We render these as a rectangle and add
a little icon for what it's supposed to represent in the top-left. These are subject to
change. For now we recommend rendering without custom shapes.

## Try it yourself​

This is live now in the D2 Playground. Try opening the below code block (click top right
of it).
