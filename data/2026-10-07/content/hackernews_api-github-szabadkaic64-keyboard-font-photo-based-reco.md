---
title: 'GitHub - szabadkai/c64-keyboard-font: Photo-based reconstruction of classic Commodore 64 keycap lettering, with desktop fonts, webfont, editable outlines, and a specimen. · GitHub'
url: https://github.com/szabadkai/c64-keyboard-font/
site_name: hackernews_api
content_file: hackernews_api-github-szabadkaic64-keyboard-font-photo-based-reco
fetched_at: '2026-10-07T17:42:32.562800'
original_url: https://github.com/szabadkai/c64-keyboard-font/
author: sohkamyung
date: '2026-10-07'
description: Photo-based reconstruction of classic Commodore 64 keycap lettering, with desktop fonts, webfont, editable outlines, and a specimen. - szabadkai/c64-keyboard-font
tags:
- hackernews
- trending
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

10 Commits
10 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
docs
docs
 
 
fonts
fonts
 
 
glyphs
glyphs
 
 
scripts
scripts
 
 
.gitignore
.gitignore
 
 
C64-Keyboard.zip
C64-Keyboard.zip
 
 
CHANGELOG.md
CHANGELOG.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
latest-reference-comparison.png
latest-reference-comparison.png
 
 
normalization-comparison.png
normalization-comparison.png
 
 
petscii-specimen.png
petscii-specimen.png
 
 
preview.html
preview.html
 
 
requirements.txt
requirements.txt
 
 
specimen.png
specimen.png
 
 
View all files

## Repository files navigation

# C64 Keyboard

A font recreated from photographs of classic Commodore 64 keycaps, with cleaned-up shapes and consistent proportions.

Download TTF·OTF·Webfont·Complete package

## Use it

Install the TTF or OTF, then selectC64 Keyboardin your application.

To try it out, download and extract the complete package, then openpreview.html. Click a special-key or PETSCII button to insert its symbol into the type tester, then copy the text into your application and selectC64 Keyboard.

If you have an earlier version installed, replace it withversion 1.108and restart applications that still show the old font. The former U+E000 symbol is no longer included.

## Included

* Uppercase letters, numbers, punctuation, arrows, and £.
* Selected accented letters, including Hungarian characters.
* Function-key labels f1–f12 and classic C64 key legends.
* All 63 PETSCII graphic front legends, arranged by key in the preview.

Lowercase input displays as uppercase. This recreates printed key legends, including smooth geometric reconstructions of the PETSCII graphics, rather than the screen bitmap font.

## PETSCII front legends

Openpreview.htmland use the PETSCII buttons to insert the symbols, then copy them from the type tester. Left legends correspond to Commodore + key, right legends to Shift + key in uppercase/graphics mode. Pi on the up-arrow key also works with Commodore.

These are reconstructed outlines: identities and key assignments come from theUltimate Commodore 64 Reference; frame thickness, curves, and print proportions are inferred from the supplied keyboard photograph. They are not exact photo traces. Pi is unframed as on the key.

The preview handles the special character codes for you. Copied symbols need this font to display correctly. See thePETSCII key map and encoding guidefor codes and keyboard combinations.

Editable outlines are inglyphs/, with build tools inscripts/. Original photographs are not included.

Build instructions·Version history

## License

To the extent possible under law, Levente Szabadkai dedicates the copyright and related rights he holds in this repository to the public domain underCC0 1.0 Universal. This covers the font files, editable outlines and traces, build scripts, preview, documentation, mappings, and specimen images. You may use, modify, and redistribute these contributions, including commercially, without attribution.

The private source photographs are not included. CC0 does not grant rights held by others in the historical keycap designs or any trademarks.C64 Keyboardis an independent, unofficial reconstruction and is not endorsed by Commodore.