---
title: PhobosLab
url: https://phoboslab.org/log/2026/05/n64-additive-blending
site_name: hackernews_api
content_file: hackernews_api-phoboslab
fetched_at: '2026-05-17T06:00:41.616953'
original_url: https://phoboslab.org/log/2026/05/n64-additive-blending
author: ibobev
date: '2026-05-16'
description: Additive Blending on the Nintendo 64
tags:
- hackernews
- trending
---

Dominic Szablewski, 
@phoboslab

— Monday, May 4th 2026

# Additive Blending on the Nintendo 64

Did you ever wonder why explosions and other effects looked so much cooler on
the original PlayStation than they did on the Nintendo 64?

“Silent Bomber“ for the PSX

“Star Fox 64“ for the N64

The reason is additive blending! Or rather, in the N64 case, the lack thereof. While
the N64 actually did support additive blending, it was practically unusable.

### PSX

The PSX supports 4 different blend modes (in addition to just overwriting
pixels) to control how sprites and geometry are mixed into the existing
frame buffer:

0: (src + dst) / 2
1: src + dst
2: dst - src
3: dst + src/4

The one you see here in Silent Bomber is conceptually the simplest one:src + dst. 
That is, colors are just added to the existing ones in the frame buffer.

 | R | G | B |
| src (sprite) | 171 | 42 | 226 | 
| + dst (framebuffer) | 63 | 141 | 170 | 
| = result | 234 | 183 | 255 | 

Drawing a sprite over a scene can only ever make itbrighter, never darker.
Perfect for explosions, plasma beams and magic spells. Importantly, note how 
theBvalue in this example adds up to396, but the PSX GPU helpfully clamps
it to the maximum range of255.

(Aside: the PSX GPU actually only works in 16bit precision with 5bit color 
components, so values range from0 .. 31; the math is the same.)

### N64

The N64's “Reality Display Processor” (the fixed-function rasterizer, short RDP)
has a much more flexible way to control blending: a configurable “Color Combiner”. 
This is somewhat similar to OpenGL'sglBlendFunc().

Libdragonexposes this functionality with theRDPQ_BLENDER((P, A, Q, B))macro that instructs the RDP to execute(P * A) + (Q * B), where eachslotcan be one of several inputs.

Setting up additive blending with this is trivial:

RDPQ_BLENDER
((
 
IN_RGB
,
 
IN_ALPHA
,
 
MEMORY_RGB
,
 
ONE
 
))

The problem is, the RDP doesn't clamp the result.

 | R | G | B |
| src (sprite) | 171 | 42 | 226 | 
| + dst (framebuffer) | 63 | 141 | 170 | 
| = result | 234 | 183 | 140 | 
 ^
 wraps around!

The resulting output is less than desirable:

Now, you could of course fall back to draw such effects on the “Reality Signal 
Processor” (RSP), the vector co-processor of the N64. But that gets complicated 
quickly if you want to do rotation, scaling or any actual 3D stuff. The RDP
is much better suited for this. Displaying is its job!

While the RDPcandraw into a 32bit buffer, it was very uncommon for games
to do so. Almost all N64 games used a 16bit framebuffer for the final output.
But with this in mind, I came up with a different plan:

Let the RDP draw onto a 32bitRGBA 8888(8 bits per component) buffer, but have 
all our sprites in the 16bitRGBA 5551(5 bits per color component, 1 bit alpha) 
range. I could just pre-process assets by dividing RGB by8(or right shifting
by3bits). This will essentially draw everything way too dark, but in turn
gives us lots of headroom for additive blending.

No wrap around when all additive blended sprites result in less than 255

Better yet, we don't have to do this image pre-processing offline. We can just
instruct the color combiner to do it for us when drawing. For free!

// Abuse the fog alpha value to draw all colors at 1/8th intensity

rdpq_set_fog_color
(
RGBA32
(
0
,
 
0
,
 
0
,
 
256
/
8
));

rdpq_mode_blender
(
RDPQ_BLENDER
((
 
IN_RGB
,
 
FOG_ALPHA
,
 
MEMORY_RGB
,
 
ONE
 
)));
 

So how do we get this back to normal brightness? Simple: use a 16bit frame buffer
for displaying and “copy” all the 32bit colors into it. We just have to be careful
to clamp all 8bit color components into the 5bit range.

void
 cpu_rgba_8888_to_5551
(
uint32_t 
*
rgba32_in
,
 uint16_t 
*
rgba16_out
)
 
{

 
for
 
(
int
 i 
=
 
0
;
 i 
<
 
320
 
*
 
240
;
 i
++)
 
{

 color_t c 
=
 color_from_packed32
(
rgba32_in
[
i
]);

 
if
 
(
c
.
r 
>
 
31
)
 
{
 c
.
r 
=
 
31
;
 
}

 
if
 
(
c
.
g 
>
 
31
)
 
{
 c
.
g 
=
 
31
;
 
}

 
if
 
(
c
.
b 
>
 
31
)
 
{
 c
.
b 
=
 
31
;
 
}

 rgba16_out
[
i
]
 
=
 
(
c
.
r 
<<
 
11
)
 
|
 
(
c
.
g 
<<
 
6
)
 
|
 
(
c
.
b 
<<
 
1
)
 
|
 
0x1
;

 
}

}

Doing this on the CPU is of course prohibitively expensive. It takes about 70ms 
for a 320×240 frame. But this is where the RSP co-processor shines. The problem
now became simple enough.

The RSP's 128bit vector instructions can process 8 pixels at a time. With
some help from HailToDodongo on the #N64Brew discord optimizing the GPU microcode, 
this now runs in about 3.1ms for the whole frame!

(Trivia: I'd like to interject for a moment. What is commonly referred to as 
“GPU microcode” in the context of the N64 is in fact, MIPS/assembly that runs 
on the RSP, or as I've recently taken to calling it, MIPS plus assembly.)

Modern tooling for N64 development is phenomenal. While it helps to have 
some understanding of assembly, you don't have to write MIPS assembly by hand
anymore. HailToDodongo invented a C-like language calledRSPLthat directly compiles to it.

So the whole setup looks like this:

// Init the display with a 16bit frame buffer

display_init
(
RESOLUTION_320x240
,
 
DEPTH_16_BPP
,
 
3
,
 
GAMMA_NONE
,
 
FILTERS_DISABLED
);

// Create a secondary 32bit render buffer and set it as render target

surface_t render32 
=
 surface_alloc
(
FMT_RGBA32
,
 
320
,
 
240
);

rdpq_set_color_image
(
render32
);

// Configure the color combiner to draw at 1/8th intensity

rdpq_set_fog_color
(
RGBA32
(
0
,
 
0
,
 
0
,
 
256
/
8
));

rdpq_mode_blender
(
RDPQ_BLENDER
((
IN_RGB
,
 
FOG_ALPHA
,
 
MEMORY_RGB
,
 
ONE
)));

// Draw your scene with lots of additive blended sprites

render_scene
();

// Kick of the conversion from the 32bit render buffer to the 

// 16bit frame buffer on the RSP

rsp_rgba_8888_to_5551
(
render32
->
buffer
,
 screen
->
buffer
);

// Present the 16bit framebuffer

display_show
(
screen
);

Resulting in lots of gloriously additive blended sprites without any wrap around 
artifacts.

There was of course a reason that most games used a 16bit frame buffer to 
begin with: the atrocious memory throughput of the N64. Drawing onto a 32bit
buffer takes almost twice the time compared to a 16bit buffer, because the RDP
has to shuffle twice the amount of bytes from and back to the frame buffer
stored in RDRAM.

Still, this technique worked out better than I expected. It's certainly good
enough for some applications.

I can also see further optimization potential by only drawing those sprites 
that need additive blending to the 32bit buffer – maybe even at a lower 
resolution — and then combine it with the rest of scene's 16bit buffer on the RSP…

A simple demo project for the above video can be found on github:github.com/phoboslab/n64_addblend