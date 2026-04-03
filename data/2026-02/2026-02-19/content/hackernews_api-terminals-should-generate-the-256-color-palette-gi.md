---
title: Terminals should generate the 256-color palette · GitHub
url: https://gist.github.com/jake-stewart/0a8ea46159a7da2c808e5be2177e1783
site_name: hackernews_api
content_file: hackernews_api-terminals-should-generate-the-256-color-palette-gi
fetched_at: '2026-02-19T06:00:15.876472'
original_url: https://gist.github.com/jake-stewart/0a8ea46159a7da2c808e5be2177e1783
author: tosh
date: '2026-02-18'
description: 'Terminals should generate the 256-color palette. GitHub Gist: instantly share code, notes, and snippets.'
tags:
- hackernews
- trending
---

Instantly share code, notes, and snippets.

# jake-stewart/color256.md

 Last active

February 18, 2026 18:50



Show Gist options



* Download ZIP





* Star112(112)You must be signed in to star a gist
* Fork10(10)You must be signed in to fork a gist

* Embed# Select an optionEmbedEmbed this gist in your website.ShareCopy sharable link for this gist.Clone via HTTPSClone using the web URL.## No results foundLearn more about clone URLsClone this repository at &lt;script src=&quot;https://gist.github.com/jake-stewart/0a8ea46159a7da2c808e5be2177e1783.js&quot;&gt;&lt;/script&gt;
* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.
* Save jake-stewart/0a8ea46159a7da2c808e5be2177e1783 to your computer and use it in GitHub Desktop.



Embed

# Select an option



* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.

## No results found





Learn more about clone URLs





 Clone this repository at &lt;script src=&quot;https://gist.github.com/jake-stewart/0a8ea46159a7da2c808e5be2177e1783.js&quot;&gt;&lt;/script&gt;





Save jake-stewart/0a8ea46159a7da2c808e5be2177e1783 to your computer and use it in GitHub Desktop.

Download ZIP

 Terminals should generate the 256-color palette




Raw

 color256.md


Terminals should generate the 256-color palette from the user's
base16 theme.

If you've spent much time in the terminal, you've probably set a
custom base16 theme. They work well. You define a handful of colors
in one place and all your programs use them.

The drawback is that 16 colors is limiting. Complex and color-heavy
programs struggle with such a small palette.

The mainstream solution is to use truecolor and gain access to 16
million colors. But there are drawbacks:

* Each truecolor program needs its own theme configuration.
* Changing your color scheme means editing multiple config files.
* Light/dark switching requires explicit support from program maintainers.
* Truecolor escape codes are longer and slower to parse.
* Fewer terminals support truecolor.

The 256-color palette sits in the middle with more range than base16
and less overhead than truecolor. But it has its own issues:

* The default theme clashes with most base16 themes.
* The default theme has poor readability and inconsistent contrast.
* Nobody wants to manually define 240 additional colors.

The solution is to generate the extended palette from your existing
base16 colors. You keep the simplicity of theming in one place while
gaining access to many more colors.

If terminals did this automatically then terminal program maintainers
would consider the 256-color palette a viable choice, allowing them
to use a more expressive color range without requiring added
complexity or configuration files.

## Understanding the 256-Color Palette

The 256-color palette has a specific layout. If you are already
familiar with it, you can skip to the next section.

#### The Base 16 Colors

The first 16 colors form the base16 palette. It contains black,
white, and all primary and secondary colors, each with normal and
bright variants.

1. black
2. red
3. green
4. yellow
5. blue
6. magenta
7. cyan
8. white
9. bright black
10. bright red
11. bright green
12. bright yellow
13. bright blue
14. bright magenta
15. bright cyan
16. bright white

#### The 216-Color Cube

The next 216 colors form a 6x6x6 color cube. It works like 24-bit
RGB but with 6 shades per channel instead of 256.

You can calculate a specific index using this formula, where R, G,
and B range from 0 to 5:

16 + (36 * R) + (6 * G) + B

#### The Grayscale Ramp

The final 24 colors form a grayscale ramp between black and white.
Pure black and white themselves are excluded since they can be found
in the color cube at (0, 0, 0) and (5, 5, 5).

You can calculate specific index using this formula, where S is the
shade ranging from 0 to 23:

232 + S

## Problems with the 256-Color Palette

#### Base16 Clash

The most obvious problem with the 256-color palette is the inconsistency
with the user's base16 theme:

Using a custom 256-color palette gives a more pleasing result:

#### Incorrect Interpolation

The default 216-color cube interpolates between black and each color
incorrectly. It is shifted towards lighter shades (37% intensity
for the first non-black shade as opposed to the expected 20%), causing
readability issues when attempting to use dark shades as background:

If the color cube is instead interpolated correctly, readability
is preserved:

#### Inconsistent Contrast

The default 256-color palette uses fully saturated colors, leading
to inconsistent brightness against the black background. Notice
that blue always appears darker than green, despite having the same
shade:

If a less saturated blue is used instead then the consistent
brightness is preserved:

## Generating the Palette

These problems can be solved by generating the 256-color palette
from the user's base16 colors.

The base16 palette has 8 normal colors which map to the 8 corners
of the 216-color cube. The terminal foreground and background should
be used instead of the base16 black and white.

These colors can be used to construct the 216-color cube via trilinear
interpolation, and the grayscale ramp with a simple background to
foreground interpolation.

The LAB colorspace should be used to achieve consistent apparent
brightness across hues of the same shade.

Solarized with RGB interpolation:

Solarized with LAB interpolation:

Combined image of many generated themes:

Before and after using 256 palette generation with default colors:

#### Implementation

This code is public domain, intended to be modified and used anywhere
without friction.

def

lerp_lab
(
t
,
lab1
,
lab2
):

return
 (

lab1
[
0
]
+

t

*
 (
lab2
[
0
]
-

lab1
[
0
]),

lab1
[
1
]
+

t

*
 (
lab2
[
1
]
-

lab1
[
1
]),

lab1
[
2
]
+

t

*
 (
lab2
[
2
]
-

lab1
[
2
]),
 )

def

generate_256_palette
(
base16
,
bg
=
None
,
fg
=
None
):

base8_lab

=
 [
rgb_to_lab
(
c
)
for

c

in

base16
[:
8
]]

bg_lab

=

rgb_to_lab
(
bg
)
if

bg

else

base8_lab
[
0
]

fg_lab

=

rgb_to_lab
(
fg
)
if

fg

else

base8_lab
[
7
]


palette

=
 [
*
base16
]


for

r

in

range
(
6
):

c0

=

lerp_lab
(
r

/

5
,
bg_lab
,
base8_lab
[
1
])

c1

=

lerp_lab
(
r

/

5
,
base8_lab
[
2
],
base8_lab
[
3
])

c2

=

lerp_lab
(
r

/

5
,
base8_lab
[
4
],
base8_lab
[
5
])

c3

=

lerp_lab
(
r

/

5
,
base8_lab
[
6
],
fg_lab
)

for

g

in

range
(
6
):

c4

=

lerp_lab
(
g

/

5
,
c0
,
c1
)

c5

=

lerp_lab
(
g

/

5
,
c2
,
c3
)

for

b

in

range
(
6
):

c6

=

lerp_lab
(
b

/

5
,
c4
,
c5
)

palette
.
append
(
lab_to_rgb
(
c6
))


for

i

in

range
(
24
):

t

=
 (
i

+

1
)
/

25


lab

=

lerp_lab
(
t
,
bg_lab
,
fg_lab
)

palette
.
append
(
lab_to_rgb
(
lab
))


return

palette

## Conclusion

The default 256-color palette has room for improvement. Considering
its poor readability and its clash with the user's theme, program
authors avoid it, opting for the less expressive base16 or more
complex truecolor.

Terminals should generate the 256-color palette from the user's
base16 theme. This would make the palette a viable option especially
considering its advantages over truecolor:

* Access to a wide color palette without needing config files.
* Light/dark switching capability without developer effort.
* Broader terminal support without compatibility issues.



### epagecommentedFeb 18, 2026

Full repo for this gist:https://github.com/jake-stewart/color256/

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### jake-stewartcommentedFeb 18, 2026•edited

🟢GhosttyImplementedghostty-org/ghostty#10554🟢iTerm2Implementedgnachman/iTerm2@39bafa8🟢SwiftTermImplementedmigueldeicaza/SwiftTerm@36642aa⚪️kittyRequestedkovidgoyal/kitty#9426⚪️WeztermRequestedwezterm/wezterm#7596

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### timthelioncommentedFeb 18, 2026

What is thergb_to_labandlab_to_rgbfunction?

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### jake-stewartcommentedFeb 18, 2026

What is thergb_to_labandlab_to_rgbfunction?

CIELAB color space.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### cevingcommentedFeb 18, 2026

Please consider using Oklch:https://en.wikipedia.org/wiki/Oklab_color_space

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### jake-stewartcommentedFeb 18, 2026

Please consider using Oklch:https://en.wikipedia.org/wiki/Oklab_color_space

I use CIELAB because it is an ISO standard.However, this is being discussed inghostty-org/ghostty#10554.I will move forward with whichever Ghostty decides (and update existing PRs).

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### JobLeonardcommentedFeb 18, 2026

Do you have any idea how this would interact with palettes that attempt to be colorblind-friendly, likeametameric?

I guess I'm really asking: does the color science get more complicated, or would a good "base" palette be enough to also generate a more colorblind-friendly palette of 256 colors?

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### fapdashcommentedFeb 18, 2026

@jake-stewartAwesome work, thank you! ❤️

Any chance you could open a PR forfoot? It's the default terminal emulator for the Fedora Sway and Fedora Micacle WM spin.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### jake-stewartcommentedFeb 18, 2026

Do you have any idea how this would interact with palettes that attempt to be colorblind-friendly, likeametameric?

I guess I'm really asking: does the color science get more complicated, or would a good "base" palette be enough to also generate a more colorblind-friendly palette of 256 colors?

In the PRs I've made, palette generation can be turned off. Additionally, manually set palette entries are never replaced. It is at least impossible for this change to reduce accessibility.

I imagine the generated palette would be more colorblind-friendly than the default palette considering the generated colors are more similar to those hand-picked values. You can try it yourselfhere.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### jake-stewartcommentedFeb 18, 2026

@jake-stewartAwesome work, thank you! ❤️

Any chance you could open a PR forfoot? It's the default terminal emulator for the Fedora Sway and Fedora Micacle WM spin.

I plan to very soon. Right now I am waiting to see whether Ghostty switches to the OKLAB color space. Ideally all the implementations are the same for consistency.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### akdor1154commentedFeb 18, 2026

I was going to ask if the interpolation you're using is gamma-correct, but I googled first and I think the answer is 'yes because you're doing it in LAB'. Great stuff!

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### septatrixcommentedFeb 18, 2026

It would be great to have an implementation based on this libraryhttps://github.com/trapd00r/colorcokewhich uses ANSI escapes to modify the terminal palette (for those terms who support it). This way one could drop it into their bashrc (or similar file for ZSH/fish) and have it work, even if their terminal does not natively do the palette generation

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### jake-stewartcommentedFeb 18, 2026•edited

It would be great to have an implementation based on this libraryhttps://github.com/trapd00r/colorcokewhich uses ANSI escapes to modify the terminal palette (for those terms who support it). This way one could drop it into their bashrc (or similar file for ZSH/fish) and have it work, even if their terminal does not natively do the palette generation

You can usethe python scriptto do that:

python3 color256.py --apply themes/century.dark.txt

You can also use it to generate terminal configurations:

python3 color256.py --generate kitty themes/century.dark.txt

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### stuaxocommentedFeb 18, 2026

Maybe this scheme should be opted into by a new control code?

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### jake-stewartcommentedFeb 18, 2026•edited

Maybe this scheme should be opted into by a new control code?

It should be opt-out rather than opt-in:

If terminals did this automatically then terminal program maintainers would consider the 256-color palette a viable choice, allowing them to use a more expressive color range without requiring added complexity or configuration files.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### epagecommentedFeb 18, 2026

Whether opt-in or opt-out, there needs to be a documented way to detect this

* whether terminal version detection and/or feature detection (preferrably through env)
* maybe a standardized flag for base16 or color256

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### migueldeicazacommentedFeb 18, 2026

Incredible, SwiftTerm now has support for it too:

https://github.com/migueldeicaza/SwiftTerm/

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







Author

### jake-stewartcommentedFeb 18, 2026

Whether opt-in or opt-out, there needs to be a documented way to detect this

* whether terminal version detection and/or feature detection (preferrably through env)
* maybe a standardized flag for base16 or color256

Regardless of whether the terminal supports this new palette generation, each 256-color palette entry points to the same kind of color.

In other words, your program will be correct regardless of whether the terminal uses the default or the generated 256-color palette.

For this reason, I do not consider the distinction important. The generated palette behaves conceptually identical to the default and can be treated as such.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### tracker1commentedFeb 18, 2026

Requested forTabbyandMS Terminal

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### epagecommentedFeb 18, 2026

For this reason, I do not consider the distinction important. The generated palette behaves conceptually identical to the default and can be treated as such.

Maybe I'm misunderstanding this proposal. One of the reasons I avoid 256-color and truecolor is that they are independent of base16 and could cause readability issues (contrast with the background). I had assumed that this would resolve those readability issues. As such, for a program likecargoorrustc, we would only want to emit 256-color if we know there won't be reaability issues. So we'd need detection for support for this proposal.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### DHowettcommentedFeb 18, 2026

Maybe this scheme should be opted into by a new control code?

Many terminal emulators, especially those listed above, support using OSC 4 to change the palette. It is broadly possible to implement this without any terminal emulator support other than that.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### ku1ikcommentedFeb 18, 2026

I think this looks great. I get how people can see 256-color both ways, either as a "stable, low res RGB", or an "extended palette". I lean towards treating it as a palette, and I believe setting it ON by default has potential of making CLIs and TUIs look awesome.

Anyway, I got nerd-sniped by this today and I alreadyimplemented this in asciinema player😅 (I used OKLAB+OKLCH).

Demo using Gruvbox Dark theme here:https://asciinema.org/a/CIyrgpv8Ztlqlk6W

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.







### dgudimcommentedFeb 18, 2026

Damn, this is awesome! Immediately tried using it in konsole and it doesn't change the colors 😅 time to open a feature request

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.





Sign up for free

to join this conversation on GitHub
.
 Already have an account?

Sign in to comment
