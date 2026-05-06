---
title: Multi-stroke text effect in CSS
url: https://yuanchuan.dev/multi-stroke-text-effect-in-css
site_name: hackernews_api
content_file: hackernews_api-multi-stroke-text-effect-in-css
fetched_at: '2026-05-06T20:20:50.455152'
original_url: https://yuanchuan.dev/multi-stroke-text-effect-in-css
author: yuanchuan
date: '2026-05-06'
description: I used to see that retro multi-stroke text effect quite often and tried to replicate it using the CSS text-stroke property, but the results never quite matched. Because text-stroke accepts a single value, stacking elements was the only workaround I could think of, though it didn't seem to work.
tags:
- hackernews
- trending
---

I used to see that retro multi-stroke text effect quite often and
 tried to replicate it using the CSStext-strokeproperty,
 but the results never quite matched.
 Becausetext-strokeaccepts a single value, stacking elements was the only workaround I could think of, though it didn't seem to work.

One evening late last year,
 I was eager to give it another shot after seeing the text effect again in the bookGraphic Japan : from woodblock and zen to manga and kawaii.

Text stroke effect from the book

I kept stacking several elements and accidentally varied thetext-stroke-widthfor each layer.
 To my suprise, the result was getting closer this time.

--c
:
 
#cc0d55
;

--n
:
 
@i
(
-1
);

@grid
:
 
36
x1
 
/
 
240px
;

@content
:
 
'✱'
;

position
:
 
absolute
;

inset
:
 
0
;

font
:
 
100
px
/
0
 
sans-serif
;

color
:
 
var
(
--c
);

z-index
:
 
@I
(
-
@
i
);

-webkit-text-stroke-color
:
 
@pn
(
--c
,
 
#f4e1e8
);

-webkit-text-stroke-width
:
 
$
em
(.
08
n
+.
02
(
1
-
(
-1
)^
n
));

## How it works

For different values of thetext-stroke-width,
 browsers will automatically draw outlines of the charater,
 The larger you set the stroke width, the thicker the outline will get,
 while still maintain its original shape.

@grid: 7x1/ 360px auto noclip;
 @content: '✱';
 font: 50px/0 sans-serif;
 color: transparent;
 -webkit-text-stroke-color: #cc0d55;
 -webkit-text-stroke-width: @i(*1.8px);

The next step is to use different colors and put them in order.

@grid: 12x1/ 100px ß #f4e1e8;
 @content: '✱';
 position: absolute;
 inset: 0;
 z-index: @I(-@i);
 font: 50px/0 sans-serif;
 color: transparent;
 -webkit-text-stroke-color: @pn(#f4e1e8, #cc0d55);
 -webkit-text-stroke-width: @i(*3px);

The interesting part is how the browsers outlining the character shapes differently.
 FireFox offers more smoother rendering than in Chrome and Safari.

Chrome/Safari

Firefox

Another interesting part is when there are more text put inline, the character shapes will be merged.

/* ... */

@content
:
 
'秋收冬藏'
;

## Trying different fonts

The final result really depends on the font you choose.
 To help experimenting with different fonts more quickly,
 I added the@google-fontfunction for faster font loading.

 --c: #cc0d55,#fff;
 @grid: 34x1 / 320px;
 @content: 'b';
 font: 150px/0 @google-font(Matemasie);
 @place: center;
 z-index: @I(-@i);
 color: @pn(--c);
 -webkit-text-stroke-color: @pn(--c);
 -webkit-text-stroke-width: @i(-1, ease, *12px);
 

font-family
:
 
@google-font
(
Matemasie
);

@content
:
 
'b'
;

 --c: #cc0d55,#fff;
 @grid: 30x1 / 320px;
 :after {
 content: 'Love';
 position: absolute;
 }
 font: 80px/0 @google-font("Pacifico");
 @place: center;
 z-index: @I(-@i);
 color: @pn(--c);

 -webkit-text-stroke-color: @pn(--c);
 -webkit-text-stroke-width: @i(ease, -1, *15px);
 

font-family
:
 
@google-font
(
Tangerine
);

@content
:
 
'Love'
;

 --c: #fff9e0,#f1c550,#ff6600,#ce2525;
 --c: #cc0d55,#fff;
 @grid: 30x1 / 320px +2 ~0 -10%;
 :after {
 content: '+';
 position: absolute;
 }
 @place: 50% 50%;
 font: 120px/0 @google-font("Cherry Bomb One");
 z-index: @I(-@i);
 color: @pn(--c);

 -webkit-text-stroke-color: @pn(--c);
 -webkit-text-stroke-width: @i(ease, -1, *12px);
 

font-family
:
 
@google-font
(
'Cherry Bomb One'
);

@content
:
 
'+'
;

Unfortunately, the performance is as bad as CSS filters, especially when the font-size is getting bigger,
 you may have noticed some flicking above.
 It's fine for experiments like this, or for generating images with css-doodle,
 but it's not well-suited for production usage.

## More examples

Here are two more examples to play around with different colors and characters, generated with css-doodle, just for fun.

CodePen link for the first one:https://codepen.io/yuanchuan/pen/ogzarGo