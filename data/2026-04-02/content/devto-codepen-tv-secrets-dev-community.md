---
title: CodePen TV secrets - DEV Community
url: https://dev.to/ivorjetski/codepen-tv-secrets-fib
site_name: devto
content_file: devto-codepen-tv-secrets-dev-community
fetched_at: '2026-04-02T19:24:44.494408'
original_url: https://dev.to/ivorjetski/codepen-tv-secrets-fib
author: Ben Evans
date: '2026-03-29'
description: Those seven deadly things you always wanted to know about creating a CRT TV in CSS. A... Tagged with codepen, css, cssart, crt.
tags: '#codepen, #css, #cssart, #crt'
---

Pure CSS art using squircles and 3D lighting

## Those seven deadly things you always wanted to know about creating a CRT TV in CSS.

A behind the scenes candid deep dive.

(1) My first vanilla CSS Art project!😮Can you actually believe it? Yes. But anyway, I got so into SASS that it wasn't until... Well I explained it all in mylast postbut yeah, I guess this is my first actual pure CSS art! I did really want to add white noise and channel clicks, but that would have involved JavaScript, so you shall have to imagine that yourselves. It's also my first use ofcorner-shape: squircle. Firefox doesn't support me on this yet, but oh well! I think squircle is necessary usage for a CRT!

(2) Lighting the CodePen logo.🌅The spinny cube thing has actual three dimensional light coming from the left, which took blumming ages to do, and it's barely even noticeable. So I would just like to point that out here 😅

The lighting within the TV image is also the opposite, to the TV, as I thought this might help represent a TV broadcast. But I also think this isn't noticeable :)

(3) The volume control distorts the scanlines.🔊I thought this would kind of represent the increase in volume interfering with the tuning, as it would if you didn't have ground loop isolation.

(4) Rotating knobs.🛞Getting the knobs look like they rotate when the shine stays top right. It was a tricky one. But the dashed border works hard here.

(5) The glass reflections could not be square!😎To replicate the distortion of a cathode ray tube's shape. The window reflection is made entirely of repeated right dashed borders. These look very different depending on the browser engine. Blink's dash size is almost perfect for the real window panes. But it's a strange way to draw windows.


&,

&
:before
,

&
:after

{


width
:

31rem
;


height
:

100rem
;


border
:

solid

7rem

transparent
;


border-right
:

dashed

7rem

hsla
(

var
(
--wht-hsl
),
.05
);


background
:

transparent
;


border-radius
:

50%
;


}

Enter fullscreen mode

Exit fullscreen mode

(6) It's responsive!📱The TV changes layout depending on your screen size. I used rems and aspect ratios hard!

(7) The CodePen 2.0 logo.🖋️The rotating 2.0 makes no sense in reality. It doestransform:scaleX(-1)exactly at 90 degrees so that 2.0 reads left to right on both the front and back.

Just one more thing...🕵️The YouTube's video intro is made entirely of CSS! I adapted two of my older projects to introduce it. As well as this one. And the music was written by me and Robert Frogley especially for the video.

Keep this on the QT 🤫 but I also lost most of the screenshots for creating this video because my laptop died and the drive got wiped when trying to fix it. So annoyingly I had to undo everything I did and screenshot it, and then play it forwards! 😮

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
