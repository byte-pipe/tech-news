---
title: CSS Iceberg - DEV Community
url: https://dev.to/alvaromontoro/css-iceberg-506c
site_name: devto
fetched_at: '2025-12-08T11:09:15.306838'
original_url: https://dev.to/alvaromontoro/css-iceberg-506c
author: Alvaro Montoro
date: '2025-12-02'
description: Cartoon of an iceberg floating coded in CSS, with zero HTML. Tagged with css, webdev, showdev, codepen.
tags: '#showdev, #css, #webdev, #codepen'
---

CodePen runs weekly coding challenges, and this week's theme isWinter, focusing onIce and Snow. I decided to participate by drawing an iceberg floating in the ocean.

I found aniceberg image onlinethat I liked and thought it would be fun to recreate it in CSS. At first, I considered using multiple elements, then switched to a single element, and eventually settled on drawing the entire piece with pure CSS and zero HTML elements.

Whenever I share a zero-element drawing on CodePen, I add a small disclaimer: while the HTML panel may look empty, there is still some HTML. Specifically, I rely on the<body>element, along with its::beforeand::afterpseudo-elements, to create the artwork.

There are also ways to achieve a true zero-HTML setup by applying the styles directly to:rootand forcing the browser to render the CSS (this only works with Apache and Firefox, though.) So technically, this drawing could be achieved with pure CSS and absolutely no HTML elements.

The drawing itself is fairly straightforward:

* body: the sky (a linear gradient) and twoconic-gradientshadows
* body::before: the iceberg, shaped with aclip-pathand shaded with conic gradients
* body::after: the water and waves, created using a repeating horizontal radial gradient plus a linear gradient for depth

You can find thelive demo and the source code on CodePen:

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
