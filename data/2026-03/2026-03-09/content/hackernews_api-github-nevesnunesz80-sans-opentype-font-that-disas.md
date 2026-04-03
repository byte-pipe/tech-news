---
title: 'GitHub - nevesnunes/z80-sans: OpenType font that disassembles Z80 instructions · GitHub'
url: https://github.com/nevesnunes/z80-sans
site_name: hackernews_api
content_file: hackernews_api-github-nevesnunesz80-sans-opentype-font-that-disas
fetched_at: '2026-03-09T19:20:10.512071'
original_url: https://github.com/nevesnunes/z80-sans
author: pabs3
date: '2026-03-05'
description: OpenType font that disassembles Z80 instructions. Contribute to nevesnunes/z80-sans development by creating an account on GitHub.
tags:
- hackernews
- trending
---

nevesnunes

 

/

z80-sans

Public

* NotificationsYou must be signed in to change notification settings
* Fork3
* Star394

 
 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

6 Commits
6 Commits
fontcustom
fontcustom
 
 
modules
modules
 
 
resources
resources
 
 
test
test
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
LICENSE.Apache.txt
LICENSE.Apache.txt
 
 
LICENSE.LGPL3.txt
LICENSE.LGPL3.txt
 
 
LICENSE.OFL.txt
LICENSE.OFL.txt
 
 
LICENSE.txt
LICENSE.txt
 
 
README.md
README.md
 
 
gen.py
gen.py
 
 
ttf_to_ttx.sh
ttf_to_ttx.sh
 
 
ttx_to_ttf.sh
ttx_to_ttf.sh
 
 
View all files

## Repository files navigation

# Z80 Sans

What's your favourite disassembler? Mine's a font:

1.mp4

This font converts sequences of hexadecimal lowercase characters into disassembled Z80 instructions, by making extensive use of OpenType'sGlyph Substitution Table (GSUB)andGlyph Positioning Table (GPOS).

If you just want to try it out, a copy is available under./test/z80-sans.ttf.

# Install

Tested on Debian GNU/Linux 12. Note that this Debian version ships with ruby version 3, while fontcustom was written for ruby version 2, and is incompatible with later versions (e.g. syntax errors). A ruby install also requires a compatible OpenSSL version. Therefore, RVM can be used to manage both ruby and a local install of OpenSSL.

apt install imagemagick potrace
pip install fonttools

git submodule update --init --recursive

#
 fontforge

(

cd
 ./modules/fontforge/
git checkout 4f4907d9541857b135bd0b361099e778325b4e28
git apply ../../resources/fontforge.diff
mkdir -p build

cd
 build
cmake -GNinja ..
ninja
ninja install
)

#
 woff2

(

cd
 ./modules/woff2/
make clean all
)

#
 fontcustom

rvm use 2.7
rvm pkg install openssl
rvm install 2.4 --with-openssl-dir=
$HOME
/.rvm/usr
gem update --system 3.3.22
(

export
 PATH=
$PWD
/modules/woff2/build:
$PATH

cd
 ./modules/fontcustom/
git apply ../../resources/fontcustom.diff
gem build fontcustom.gemspec
gem install ./fontcustom-2.0.0.gem
)

# Running

cp ./resources/droid-sans-mono.ttf /tmp/base.ttf
./gen.py ./resources/instructions.json

The .ttf font file is copied to~/.local/share/fonts/, which is used by e.g. LibreOffice.

# Design

Compared to other cursed fonts, Z80 Sans has these challenges:

* Multiple characters to render: it would be impractical to manually define character by character all substitution rules for rendering, so we can create glyphs that combine multiple literals (e.g. mnemonics likeCALL), however this also ties to the next point...
* Multiple combinations: recall that some Z80 instructions can take 16-bit addresses and registers as operands, which means that a single instruction can have up to65536 * 7 = 458752possible combinations;
* Out-of-order operands: e.g. register and offsets can be encoded into hexadecimal bytes in one order, but disassembled in another order, which complicates backtracking/lookaheads rules;
* Little-endian addresses: Characters for the least-significant byte need to be rendered before the most-significant byte;
* Signed offsets: All offsets in range0x80..0xffneed to be rendered as a negative two's-complement number;

All of this invites a programmatic solution. While fontcustom and ImageMagick take care of generating glyphs, it seems that a convenient way to write lookup rules is the .fea format, but I didn't find a way to integrate it with fonttools' .ttx format (which is basically xml). I took the lowest common denominator approach of directly editing the .ttx of Noto Sans Mono (although glyph shapes are computed from Droid Sans Mono, as that's what I started with when patching FontForge).

A recursive descent parser is used to generate all possible glyphs, which helps with evaluating expressions in encodings (e.g.SET b,(IX+o)takes a bit and a displacement, encoded as expressionDD CB o C6+8*b). These encodings were then expanded to all possible values that operands can take, before finally associating 1 or more hexadecimal bytes to each disassembly glyph required to render an expanded instruction.

There are some nice references for OpenType features, but they are written at a high-level, or in .fea(?) format:

* OpenType Feature File Specification | afdko
* GSUB — Glyph Substitution Table (OpenType 1.9.1) - Typography | Microsoft Learn
* Fonts and Layout for Global Scripts
* GitHub - brew/opentype-feature-intro: An introduction to OpenType features for type designers.
* Features, part 3: advanced contextual alternates | Glyphs
* Opentype subtitution many by many (different number) - Glyphs Forum

It's never very clear how to translate them to .ttx, so in the end I just converted all of the Noto Sans family and used the good ol' fashioned bruteforce approach of "learning by example". This is even more fun that it sounds, thanks to plenty of silent failures when converting from .ttx to .ttf, where lookups will not match due to some assumptions not validated by fonttools (e.g. class definitions for contextual chaining substitutions must have at least one coverage glyph with class value="1").

Pretty much most challenges were solved with contextual chaining rules. To handle addresses, each nibble in range0..fwas encoded with distinct glyphs, with spacing characters used to create multiple substitutions, one character at a time. Displacements also have additional signed variants. This gives us a total of(4 + 2) * 16glyphs for numbers. This was already enough to keep the font file under the 65536 glyphs limit.

The worst part was of course out-of-order operands. However, due to the limited number of variations these have in instructions, they could be covered by the same strategy as instructions with ambiguously encoded prefixes, e.g.

["SET b,(IX+o)", "DD CB o C6+8*b"],
["SET b,(IY+o)", "FD CB o C6+8*b"],

Is covered by the same lookup rules as:

["SRA (IX+o)", "DD CB o 2E"],
["SRA (IY+o)", "FD CB o 2E"],
["SRL (IX+o)", "DD CB o 3E"],
["SRL (IY+o)", "FD CB o 3E"],

An interesting property in the Z80 ISA is that bits and registers have up to 8 variations, and these out-of-order cases only involve offsets and one of those specific operands. Therefore, we can encode bits or registers as literals. With sufficient lookaheads, we can match up to the last hexadecimal byte, and create dedicated lookups for each case. The last literals can be reduced by generating a ligature that matches the suffix glyph. The end result was dozens more generated lookups for these cases (which can likely be grouped to reduce this number).

# Known Issues

* While all of the original instruction set should be disassembled, some instructions have minor glitches:LD (IX+o),ris rendered asLD (IX+o r),;SET b,(IX+o)is rendered asSET b,(IX+o));
* LD (IX+o),ris rendered asLD (IX+o r),;
* SET b,(IX+o)is rendered asSET b,(IX+o));
* "CTF quality" code 😅;

# Future Work

FontForge supports scriptable modification of features using commandsGenerateFeatureFile()andMergeFeature()(briefly covered inThe Terrible Secret of OpenType Glyph Substitution - Ansuz - mskala's home page). I was only aware of this after making the .ttx based implementation, but it could potentially have avoided messing with .ttx files.

For more complex instruction sets, an alternative approach that seems to have less constraints is to use font shapers. Some examples:

* fuglede/llama.ttf: A font for writing tiny stories;
* hsfzxjy/handwriter.ttf: Handwriting synthesis with Harfbuzz WASM.;

# Credits

* Droid Sans MonoandNoto Sans Monowere used as base for Z80 Sans;
* ./resources/instructions.jsonwas adapted frommaziac/z80-instruction-set;
* Inspiration for GSUB substitutions:Font with Built-In Syntax Highlighting;Fontemon, in particular"How I did it";Addition Font;Sans Bullshit Sans;
* Font with Built-In Syntax Highlighting;
* Fontemon, in particular"How I did it";
* Addition Font;
* Sans Bullshit Sans;

# License

* Droid Sans Mono is underApache Licence;
* Noto Sans Mono is underOpen Font License;
* ./resources/instructions.jsonis underGNU Lesser General Public License version 3;
* Other files are underMIT License;

## About

OpenType font that disassembles Z80 instructions

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

394

 stars
 

### Watchers

5

 watching
 

### Forks

3

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors1

* nevesnunes

## Languages

* Python99.4%
* Shell0.6%