---
title: I put a real-time 3D shader on the Game Boy Color | Danny's Blog
url: https://blog.otterstack.com/posts/202512-gbshader/
site_name: hackernews_api
content_file: hackernews_api-i-put-a-real-time-3d-shader-on-the-game-boy-color
fetched_at: '2026-02-09T11:22:38.497870'
original_url: https://blog.otterstack.com/posts/202512-gbshader/
author: adunk
date: '2026-02-08'
published_date: '2025-12-05'
description: I put a real-time 3D shader on the Game Boy Color
tags:
- hackernews
- trending
---

# I put a real-time 3D shader on the Game Boy Color

Written by:
 Danny Spencer

December 5, 2025

Updated February 8, 2026

## Demonstration

I made a Game Boy Color game that renders images in real time. The player controls an orbiting light and spins an object.

### Play it here

### Check out the code, download the ROMs

https://github.com/nukep/gbshader

## 3D Workflow

### Early lookdev

Before really diving into this project, I experimented with the look in Blender to see if it would even look good. IMO it did, so I went ahead with it!

I experimented with a "pseudo-dither" on the Blender monkey by adding a small random vector to each normal.



### Blender to normal map workflow

tl;dr: Cryptomattes and custom shaders to adjust normal maps

It doesn't really matter what software I used to produce the normal maps. Blender was the path of least resistance for me, so I chose that.

For the teapot, I simply put in a teapot, rotated a camera around it, and exported the normal AOV as a PNG sequence. Pretty straight-forward.

For the spinning Game Boy Color, I wanted to ensure that certain colors were solid, so I used cryptomattes in the compositor to identify specific geometry and output hard-coded values in the output.

The geometry in the screen was done by rendering a separate scene, then compositing it in the final render using a cryptomatte for the screen.

## The Math

### Normal Maps



The above animations are normal map frames that are used to solve the value of each pixel

Normal maps are a core concept of this project. They're already used everywhere in 3D graphics.

And indeed, normal map images are secretly a vector field. The reason normal maps tend to have a blue-ish baseline color, is because everyone likes to associate XYZ with RGB, and +Z is the forward vector by convention.

In a typical 3D workflow, a normal map is used to encode the normal vector at any given point on a textured mesh.

### Calculating a Lambert shader using dot products

The simplest way to shade a 3D object is using the dot product:

v
=
N
⋅
L
v = \mathbf{N} \cdot \mathbf{L}
v
=
N
⋅
L

whereNNNis the normal vector, andLLLis the light position when it points towards the origin (or equivalently: the negative light direction).

Expanded out component-wise, this is:

v
=
N
x
L
x
+
N
y
L
y
+
N
z
L
z
v = \mathbf{N}_x\mathbf{L}_x + \mathbf{N}_y \mathbf{L}_y + \mathbf{N}_z\mathbf{L}_z
v
=
N
x
​
L
x
​
+
N
y
​
L
y
​
+
N
z
​
L
z
​

When the light vector is constant for all pixels, it models what most 3D graphics software calls a "distant light", or a "sun light".

### Spherical Coordinates

To speed up computation on the Game Boy, I use an alternate version of the dot product, using spherical coordinates.

Aspherical coordinateis a point represented by a radiusrrr, a primary angleθ\thetaθ"theta", and a secondary angleφ\varphiφ"phi". This is represented as a tuple:(r,θ,φ)(r, \theta, \varphi)(r,θ,φ)

The dot product of two spherical coordinates:

(
r
1
,
θ
1
,
φ
1
)
⋅
(
r
2
,
θ
2
,
φ
2
)
=
r
1
r
2
(
sin
⁡
θ
1
sin
⁡
θ
2
cos
⁡
(
φ
1
−
φ
2
)
+
cos
⁡
θ
1
cos
⁡
θ
2
)
(r_1, \theta_1, \varphi_1) \cdot (r_2, \theta_2, \varphi_2) = r_1r_2 (\sin \theta_1 \sin \theta_2 \cos(\varphi_1 - \varphi_2) + \cos \theta_1 \cos \theta_2)
(
r
1
​
,
θ
1
​
,
φ
1
​
)
⋅
(
r
2
​
,
θ
2
​
,
φ
2
​
)
=
r
1
​
r
2
​
(
sin
θ
1
​
sin
θ
2
​
cos
(
φ
1
​
−
φ
2
​
)
+
cos
θ
1
​
cos
θ
2
​
)

Because all normal vectors are unit length, and the light vector is unit length, we can just assume the radiusrrris equal to 1. This simplifies to:

v
=
sin
⁡
θ
1
sin
⁡
θ
2
cos
⁡
(
φ
1
−
φ
2
)
+
cos
⁡
θ
1
cos
⁡
θ
2
v = \sin \theta_1 \sin \theta_2 \cos(\varphi_1 - \varphi_2) + \cos \theta_1 \cos \theta_2
v
=
sin
θ
1
​
sin
θ
2
​
cos
(
φ
1
​
−
φ
2
​
)
+
cos
θ
1
​
cos
θ
2
​

And using the previous variable names, we get the formula:

v
=
sin
⁡
N
θ
sin
⁡
L
θ
cos
⁡
(
N
φ
−
L
φ
)
+
cos
⁡
N
θ
cos
⁡
L
θ
v = \sin N_\theta \sin L_\theta \cos(N_\varphi - L_\varphi) + \cos N_\theta \cos L_\theta
v
=
sin
N
θ
​
sin
L
θ
​
cos
(
N
φ
​
−
L
φ
​
)
+
cos
N
θ
​
cos
L
θ
​

## Making it work on the Game Boy

### Encoding normal maps in the Game Boy ROM

In the ROM, I decided to fixLθL_\thetaLθ​"L-theta" to a constant value for performance reasons. The player gets to controlLφL_\varphiLφ​"L-phi", creating anorbiting lighteffect.

This means that we can extract constant coefficientsmmmandbbband rewrite the formula:

m
=
sin
⁡
N
θ
sin
⁡
L
θ
b
=
cos
⁡
N
θ
cos
⁡
L
θ
v
=
m
cos
⁡
(
N
φ
−
L
φ
)
+
b
\begin{aligned}
m &= \sin N_\theta \sin L_\theta \\
b &= \cos N_\theta \cos L_\theta \\
v &= m \cos(N_\varphi - L_\varphi) + b
\end{aligned}
m
b
v
​
=
sin
N
θ
​
sin
L
θ
​
=
cos
N
θ
​
cos
L
θ
​
=
m
cos
(
N
φ
​
−
L
φ
​
)
+
b
​

The ROM encodes each pixel as a 3-byte tuple of(Nφ,log⁡(m),b)(N_\varphi, \log(m), b)(Nφ​,log(m),b).

Whylog⁡(m)\log(m)log(m)? Well...

### The Game Boy has no multiply instruction

Not only does the SM83 CPUnotsupport multiplication, but it also doesn't support floats. That's a real bummer.

We have to get really creative when the entire mathematical foundation of this project involves multiplying non-integer numbers.

What do we do instead? We use logarithms and lookup tables!

Logarithms have this nice property of being able to factor products to outside thelog⁡\loglog. This way, we can add values instead!

log
⁡
b
(
x
⋅
y
)
=
log
⁡
b
(
x
)
+
log
⁡
b
(
y
)
x
⋅
y
=
b
log
⁡
(
x
)
+
log
⁡
(
y
)
\begin{aligned}
\log_b(x \cdot y) &= \log_b(x) + \log_b(y) \\
x \cdot y &= b^{\log(x) + \log(y)}
\end{aligned}
lo
g
b
​
(
x
⋅
y
)
x
⋅
y
​
=
lo
g
b
​
(
x
)
+
lo
g
b
​
(
y
)
=
b
l
o
g
(
x
)
+
l
o
g
(
y
)
​

This requires two lookups: aloglookup, and apowlookup.

In pseudocode, multiplying 0.3 and 0.5 looks like this:

pow
 = [ ... ]
# A 256-entry lookup table

# float_to_logspace() is compile-time. Accepts -1.0 to +1.0.

# x and y are 8-bit values in log-space

x = float_to_logspace(
0.3
)
y = float_to_logspace(
0.5
)

result =
pow
[x + y]

One limitation of this is that it's not possible to take the log of a negative number. e.g.log⁡(−1)\log(-1)log(−1)has no real solution.

We can overcome this by encoding a "sign" bit in the MSB of the log-space value. When adding two log-space values together, the sign bit is effectively XOR'd (toggled). We just need to ensure the remaining bits don't overflow into it. We ensure this by keeping the remaining bits small enough.

Thepowlookup accounts for this bit and returns a positive or negative result based on it.

### All scalars and lookups are 8-bit fractions

It's advantageous to restrict numbers to a single byte, for both run-time performance and ROM size. 8-bit fractions are pretty extreme by today's standards, but believe it or not, it works. It's lossy as hell, but it works!

All scalars we're working with are between -1.0 and +1.0.

Byte
Resolved linear-space value
Resolved log-space value
0
0
127
=
0
{0 \over 127} = 0
127
0
​
=
0
2
0
=
1
2^{0} = 1
2
0
=
1
1
1
127
≈
0.0079
{1 \over 127} \approx 0.0079
127
1
​
≈
0.0079
2
−
1
6
≈
0.89
2^{- {1 \over 6}} \approx 0.89
2
−
6
1
​
≈
0.89
2
2
127
≈
0.0158
{2 \over 127} \approx 0.0158
127
2
​
≈
0.0158
2
−
2
6
≈
0.79
2^{- {2 \over 6}} \approx 0.79
2
−
6
2
​
≈
0.79
...
126
126
127
≈
0.9921
{126 \over 127} \approx 0.9921
127
126
​
≈
0.9921
2
−
126
6
≈
0
{2^{-{126 \over 6}}} \approx 0
2
−
6
126
​
≈
0
127
127
127
=
1
{127 \over 127} = 1
127
127
​
=
1
2
−
127
6
≈
0
{2^{-{127 \over 6}}} \approx 0
2
−
6
127
​
≈
0
128
undefined
−
2
0
=
−
1
-2^{0} = -1
−
2
0
=
−
1
129
−
127
127
=
−
1
-{127 \over 127} = -1
−
127
127
​
=
−
1
−
2
−
1
6
≈
−
0.89
-2^{- {1 \over 6}} \approx -0.89
−
2
−
6
1
​
≈
−
0.89
130
−
126
127
≈
−
0.9921
-{126 \over 127} \approx -0.9921
−
127
126
​
≈
−
0.9921
−
2
−
2
6
≈
−
0.79
-2^{- {2 \over 6}} \approx -0.79
−
2
−
6
2
​
≈
−
0.79
...
254
−
2
127
≈
−
0.0158
-{2 \over 127} \approx -0.0158
−
127
2
​
≈
−
0.0158
−
2
−
126
6
≈
−
0
-{2^{-{126 \over 6}}} \approx -0
−
2
−
6
126
​
≈
−
0
255
−
1
127
≈
−
0.0079
-{1 \over 127} \approx -0.0079
−
127
1
​
≈
−
0.0079
−
2
−
127
6
≈
−
0
-{2^{-{127 \over 6}}} \approx -0
−
2
−
6
127
​
≈
−
0

Addition and multiplication both use... addition!

Consider adding the two bytes: 5 + 10 = 15

* Addition uses linear-space values:5127+10127=15127{5 \over 127} + {10 \over 127} = {15 \over 127}1275​+12710​=12715​
* Multiplication uses log-space values:2−56⋅2−106=2−1562^{-{5 \over 6}} \cdot 2^{-{10 \over 6}} = 2^{-{15 \over 6}}2−65​⋅2−610​=2−615​

Why is the denominator 127 instead of 128? It's because I needed to represent both positive and negative 1. In a two's-complement encoding, signed positive 128 doesn't exist.

You might notice that the log-space values cycle and become negative at byte 128. The log-space values use bit 7 of the byte to encode the "sign" bit. As mentioned in the previous section, this is important for toggling the sign during multiplication.

The log-space values also use2162^{1 \over 6}261​as a base, because I chose this as a sufficiently small base to meet the requirement that adding 3 of these log-space values won't overflow (42+42+42 = 126). Bytes 43 thru 127 are near 0, so in practice the ROM doesn't encode these values.

The lookup tables look like this:

Where:

* encode(y)\text{encode}(y)encode(y)takes a real number and returns an unsigned byte.
* decode(x)\text{decode}(x)decode(x)takes an unsigned byte and returns a return number.
And:
* encode(y)=round(127y)mod256\text{encode}(y) = \text{round}(127y) \bmod 256encode(y)=round(127y)mod256
* decode(x)=signedbyte(x)127\text{decode}(x) = {\text{signedbyte}(x) \over 127}decode(x)=127signedbyte(x)​

Reconstructed functions look like this. The precision error is shown in the jagged "staircase" patterns:

It may look like there's a lot of error, but it's fast and it's passable enough to look alright! ;)

### What's with cos_log?

It's basically a combinedlog⁡(cos⁡x)\log(\cos x)log(cosx). This exists because in practice, cosine is always used with a multiplication.

The core calculation for the shader is:

v
=
m
cos
⁡
(
N
φ
−
L
φ
)
+
b
v = m \cos(N_\varphi - L_\varphi) + b
v
=
m
cos
(
N
φ
​
−
L
φ
​
)
+
b

And we can rewrite it as:

v
=
pow
(
m
l
o
g
+
cos
⁡
l
o
g
(
N
φ
−
L
φ
)
)
+
b
v = \text{pow}(m_{log} + \cos_{log}(N_\varphi - L_\varphi)) + b
v
=
pow
(
m
l
o
g
​
+
cos
l
o
g
​
(
N
φ
​
−
L
φ
​
))
+
b

This amounts to, per-pixel:

* 1 subtraction
* 1 lookup tocos_log
* 1 addition
* 1 lookup topow
* 1 addition

For a total of, per-pixel:

* 3 additions/subtractions
* 2 lookups

### How fast is it?

The procedure processes 15 tiles per frame. It can process more if some of the tile's rows are empty (all 0), but it's guaranteed to process at least 15.

Figure: Mesen's "Event Viewer" window, showing a dot for each iteration (tile row) of the shader's critical loop.

There's some intentional visual tearing as well. The image itself is more than 15 tiles, so the ROM actually switches to rendering different portions of the image for each frame. The tearing is less noticeable because of ghosting on the LCD display, so I thought it was acceptable.

A pixel takes about 130 cycles, and an empty row's pixel takes about 3 cycles.

At one point I had calculated 15 tiles rendering at exactly 123,972 cycles, including the call and branch overhead. This is an overestimate now, because I since added an optimization for empty rows.

The Game Boy Color's CPU runs up to 8.388608 MHz, or roughly 139,810 T-cycles per frame (1/60 of a second).

123972139810≈89%{123972 \over 139810} \approx 89 \%139810123972​≈89%About 89% of a frame's available CPU time goes to rendering the 15 tiles per frame. The remaining time goes to other functionality like responding to user input and performing hardware IO.

### Self-modifying code

Figure: A hex representation of the shader subroutine instructions in RAM. The blue digits show a patch to changesub a, 0intosub a, 8.

The core shader subroutine contains a hot path that processes about 960 pixels per frame. It's really important to make this as fast as possible!

Self-modifying code is a super-effective way to make codefast. But most modern developers don't do this anymore, and there are good reasons: It's difficult, rarely portable, and it's hard to do it right without introducing serious security vulnerabilities. Modern developers are spoiled by an abundance of processing power, super-scalar processors that take optimal paths, and modern JIT (Just-In-Time) runtimes that generate code on the fly. But we're on the Game Boy, baybeee, so we don't have those options.

If you're a developer who uses higher-level languages like Python and JavaScript, the closest equivalent to self-modifying code iseval(). Think about how nervouseval()makes you feel. That's almost exactly how native developers feel about modifying instructions.

On the Game Boy'sSM83processor, it's faster to add and subtract by a hard-coded number than it is to load that number from memory.

i.e.x += 5is faster thanx += variable.

unsigned

char
 Ltheta =
8
;

// Slower

v = (*in++) - Ltheta;

// Faster

v = (*in++) -
8
;

In SM83 assembly, this looks like:

; Slower: 28 cycles
ld a, [Ltheta] ; 12 cycles: Read variable "Ltheta" from HRAM
ld b, a ; 4 cycles: Move value to B register
ld a, [hl+] ; 8 cycles: Read from the HL pointer
sub a, b ; 4 cycles: A = A - B

; Faster: 16 cycles
ld a, [hl+] ; 8 cycles: Read from the HL pointer
sub a, 8 ; 8 cycles: A = A - 8

The faster way shaves off 12 cycles. If we're rendering 960 pixels, this saves a total of 11,520 cycles. This doesn't sound like a lot, but it's roughly 10% of the shader's runtime!

## An overall failed attempt at using AI

"AI Will Be Writing 90% of Code in 3 to 6 Months"— Dario Amodei, CEO of Anthropic (March 2025 - 9 months ago as of writing)

95% of this project was made by hand. Large language models struggle to write Game Boy assembly. I don't blame them.

### A quick comment

Update: 2026-02-03:I attempted to use AI to try out the process, mostly because 1) the industry won't shut up about AI, and 2) I wanted a grounded opinion of it for novel projects, so I have a concrete and personal reference point when talking about it in the wild. At the end of the day, this is still a hobbyist project, so AI really isn't the point! But still...

I believe in disclosing all attempts or actual uses of generative AI output, because I think it's unethical to deceive people about the process of your work. Not doing so undermines trust, and amounts to disinformation or plagiarism. Disclosure also invites people who have disagreements to engage with the work, which they should be able to. I'm open to feedback, btw.

I'll probably write something about my experiences with AI in the future.

As far as disclosures go, I used AI for:

1. Python: Reading OpenEXR layers, as part of a conversion script to read normal map data
2. Python/Blender: Some Python scripts for populating Blender scenes, to demo the process in Blender
3. SM83 assembly: Snippets for Game Boy Color features like double-speed and VRAM DMA. Unsurprising, because these are likely available somewhere else.

Iattempted- and failed - to use AI for:

1. SM83 assembly:(Unused)Generating an initial revision of the shader code

I'll also choose to disclose whatI did NOT use AI for:

1. Writing this article
2. The algorithms, lookups, all other SM83 assembly
3. 3D assets
4. The soul 🌟 (AI techbros are groaning right now)

### I tried to make AI write Game Boy assembly

Just to see what it would do,I fed pseudocode into Claude Sonnet 4(the industry claims that it's the best AI model for coding in 2025), and got it to generate SM83 assembly:

https://claude.ai/share/846cb7d4-e4a6-40ab-8aaa-6e4c308e3da3

It was an interesting process. To start, I chewed Claude's food and gave it pseudocode, because I had a data format in mind, and I assumed it'd struggle with a higher-level description.

I was skeptical that it wouldn't do well, but it did better than I thought it would. It even produced code that worked when I persisted it and guided it enough. However, it wasn't very fast, and it made some initial mistakes by assuming the SM83 processor was the Z80 processor. I attempted to get Claude to optimize it by offering suggestions. It did well initially, but it introduced errors until I reached the conversation limit.

After that point, I manually rewrote everything. My final implementation is aggressively optimized and barely has any resemblance to Claude's take.

And itlovedtelling me how "absolutely right" I always was.🥺

It was better for small tasks and snippets of code. The tile demo in my video was partially AI scripted. A Game Boy subroutine for copying to VRAM was authored by AI - although this is also likewise trivial to find a snippet of online.

An early iteration of the normal map conversion script accepted OpenEXR files. I didn't feel like drudging through a new library, so I asked ChatGPT to convert an OpenEXR file to a numpy array. It did pretty well! It however also introduced a very subtle bug that I didn't catch for weeks. Once I finally read the code, I realized it was sorting channel names alphabetically (so XYZ sorts as XYZ, but RGB sorts as BGR). It's the sort of error I'd never make myself.

Update: 2026-02-03 - Yeah, so the OpenEXR code could've been done in two lines this whole time. One of the first examples inthe official PyPi readmeshows how to get a numpy array from an OpenEXR file - exactly what I needed. I could update this snippet for different channels too in theory, but basically it's this. ChatGPT gave me 30 lines to handle edge cases that simply won't happen.

with
 OpenEXR.File(
"readme.exr"
)
as
 infile:
 RGB = infile.channels()[
"RGB"
].pixels

At this point, I can't emphasizeverifiableenough.

This, and other experiences, made me realize how easy it is to let your guard down when using AI like this, even if you're an experienced coder. AI can be helpful, but discretion is very much a required skill.I'm just thankful I never relied on it for installing hallucinated packages.

## Comments

If you like this, share this post or like and comment on the YouTube video!

https://www.youtube.com/watch?v=SAQXEW3ePwo

(post will be updated once I post on Bluesky)
