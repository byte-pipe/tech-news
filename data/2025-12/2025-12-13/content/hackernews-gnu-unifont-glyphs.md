---
title: GNU Unifont Glyphs
url: https://unifoundry.com/unifont/index.html
site_name: hackernews
fetched_at: '2025-12-13T19:06:25.223211'
original_url: https://unifoundry.com/unifont/index.html
author: remywang
date: '2025-12-13'
description: GNU Unifont free software utilities
---

Plane 0 Chart

 Japanese
Plane 0 Chart

 Plane 1 Chart

 Chinese
Plane 2 Chart

 Japanese
Plane 2 Chart

 Plane 3 Chart

GNU Unifont is part of the GNU Project.This page contains the latest release of
 GNU Unifont, with glyphs for every printable code point
 in the Unicode Basic Multilingual Plane (BMP).The BMP occupies the first 65,536 code points of the Unicode space,
 denoted as U+0000..U+FFFF. There is also growing coverage of the
 Supplementary Multilingual Plane (SMP), in the range U+010000..U+01FFFF,
 and of Michael Everson's ConScript Unicode Registry (CSUR) with
 Rebecca Bettencourt's Under-CSUR additions.

### Commercial Use

A user has asked if GNU Unifont can be used with commercial
 (non-free) software. The answer is yes. The GNU Font Embedding
 Exception and the SIL OFL allow for that. See the next section
 for details. The main purpose of the licensing is to require
 derivative fonts that others create to be released to the public
 under the same licensing terms, not to prohibit the use of those
 fonts with certain software. Thus, preserving the license terms
 in derivative fonts provides a public benefit. The licenses also
 provide acknowledgement of previous Unifont contributors for their
 volunteer work.

### Copyright, Derivative Works, and License

Thousands of Unifont glyphs are creations of individual Unifont
 contributors; those glyphs enjoy copyright protections of various
 degrees. Some of those contributions are letter forms of established
 alphabets while others are icon (symbol) designs such as the many
 animal icons which, as artistic designs, have even stronger
 international protections. See for example this memorandum of
 applicable laws of Berne Union member country Germany (where
 Unifont was created):Unifont Copyright Protections.

Derivative variants of Unifont are permitted under the terms of
 the dual license: GNU GPLv2+ with the GNU Font Embedding Exception
 and the SIL Open Font License version 1.1. These are free licenses.
 The remainder of this section provides details.

These font files are licensed under the GNU General Public License,
 either Version 2 or (at your option) a later version, with the exception
 that embedding the font in a document does not in itself constitute a
 violation of the GNU GPL. The full terms of the license are inLICENSE.txt.

As of Unifont version 13.0.04, the fonts are dual-licensed under
 the SIL Open Font License (OFL) version 1.1 and the GNU GPL 2+ with
 the GNU font embedding exception. The SIL OFL is available atOFL-1.1.txt.

### Font Downloads

The standard font build— with and without the
 ConScript Unicode Registry (CSUR) / Under-CSUR Private Use Area
 (PUA) glyphs. Download in your favorite format:

* OpenType:The Standard Unifont OpenType Download:unifont-17.0.03.otf(5 Mbytes)Unifont Japanese OpenType Version:unifont_jp-17.0.03.otf(5 Mbytes)Glyphs above the Unicode Basic Multilingual Plane:unifont_upper-17.0.03.otf(1 Mbyte)Unicode ConScript Unicode Registry (CSUR) PUA Glyphs:unifont_csur-17.0.03.otf(0.5 Mbyte)
* The Standard Unifont OpenType Download:unifont-17.0.03.otf(5 Mbytes)
* Unifont Japanese OpenType Version:unifont_jp-17.0.03.otf(5 Mbytes)
* Glyphs above the Unicode Basic Multilingual Plane:unifont_upper-17.0.03.otf(1 Mbyte)
* Unicode ConScript Unicode Registry (CSUR) PUA Glyphs:unifont_csur-17.0.03.otf(0.5 Mbyte)
* PCF:unifont-17.0.03.pcf.gz(1 Mbyte)
* BDF:unifont-17.0.03.bdf.gz(1 Mbyte)Unifont Japanese BDF Version:unifont_jp-17.0.03.bdf.gz(1 Mbyte)
* unifont-17.0.03.bdf.gz(1 Mbyte)
* Unifont Japanese BDF Version:unifont_jp-17.0.03.bdf.gz(1 Mbyte)

Specialized versions— built by request:

* PSF:A specialized PSF 1 console frame buffer font
 consisting of 512 glyphs for use with APL,A Programming
 Language,in console mode (single-user mode on GNU/Linux,
 etc.), mainly to support GNU APL:Unifont-APL8x16-17.0.03.psf.gz(4 kbytes)
* HEX:All the Plane 0 glyphs in Roman's .hex format, for those who
 wish to experiment:unifont-17.0.03.hex.gz(1 Mbyte)
* HEX:The above .hex file with combining circles added:unifont_sample-17.0.03.hex.gz(1 Mbyte)

On Windows or Mac OS X, unzip the .ttf.zip file or download the
 uncompressed .ttf file and copy the font to your Fonts folder.
 On Microsoft Windows, this folder is located under the Windows
 folder on your main disk.
 On a Mac, this is located under the Library folder on your main disk.

For best appearance on a Mac in a Terminal window, select Terminal from
 the menu, then Preferences. A Settings window will appear. Make sure
 that you're on the Text tab in that window. Then make sure that the
 "Antialias text" box is checked. The OpenType version of the font should
 then look fine at point sizes of 12pt and larger. The font won't look
 very legible in a Mac Terminal window unless you select this antialias option.

Note:BDF, PCF, and OpenType files contain dimension and spacing
 information for each glyph in a font. Some font rendering engines ignore
 this glyph information that the font file provides. This is especially
 true of rendering engines designed to handle monospace fonts.
 Unifont will not display all glyphs correctly with such software.
 The BDF font follows BDF version 2.1 (not version 2.2) because the
 the X Window System standardized on version 2.1.
 The PSF 1 version of Unifontisa monospace font but is
 limited to 512 glyphs, and is only of use with font rendering engines
 that support more than 256 glyphs in a console frame buffer font.

All unifont.hex sources are in the fullUnifont Utilitiesdownload page.

### Unifont Limitations

Unifont only stores one glyph per printable Unicode code point.
 This means that complex scripts with special forms for letter
 combinations including consonant combinations and floating vowel
 marks such as with Indic scripts (Devanagari, Bengali, Tamil, etc.)
 or letters that change shape depending upon their position in a word
 (Indic and Arabic scripts) will not render well in Unifont.
 In those cases, Unifont is only suitable as a font of last resort.
 Users wishing to properly render such complex scripts should
 use full OpenType fonts that faithfully display such alternate
 forms.

### Drawing New Glyphs

If you would like to contribute glyphs, please email unifoundry at
 gmail in advance (not spelled out because of spammers). Several
 contributors are working on new glyphs, and it would be unfortunate
 to have multiple persons drawing the same glyphs.

### Special Note: New Plane 2 and Plane 3 CJK Glyphs

The People's Republic of China (PRC) has a set of 15-by-16 pixel
 Chinese glyphs for Unicode Plane 2 and Plane 3. However,
 those glyphs are copyrighted and licensed for sale by the Government
 of the PRC,and thus they cannot be used in a free font.If you happen to have any of those copyrighted 15-by-16 pixel glyphs,
 please do not send them for inclusion. Unifont includes many glyphs
 in this range, drawn by Chinese and Japanese volunteers.
 More are planned for the future.

### Release Notes

This latest release is part of the GNU Project. You can view theGNU Project Unifont Pageon Savannah.

The theoretical maximum number of printable glyphs in the
 Unicode Plane 0 range is 65,536 code points
 minus the 2,048 surrogate pair code points,
 minus the 6,400 Private Use Area code points,
 minus the two noncharacters (U+FFFE and U+FFFF).
 This amounts to 57,086 assignable code points
 apart from the Private Use Area.

The theoretical maximum number of printable glyphs in the
 higher Unicode planes is 65,534; the last two code points
 in each plane are reserved as noncharacters.

#### Unifont 17.0

* 1 November 2025 (Unifont 17.0.03)晓晓Akatsuki, Boris Zhang,Kusanagi_Sans,and
 others updated over 100 Chinese ideographs in Planes 0, 2, and 3:Modified ideographs containing the "馬" (Horse) and "鳥"
 (Bird) radicals to be more balancedThe first batch of simplified Chinese character lists
 (第一批簡體字表) (August 21, 1935~February 1936)Chinese Character Simplification Scheme (1956–1986)The simplified character list (1986–2013), including
 simplified radicals and Chinese characters used for
 descriptions and annotations in official documentsThe second list of the Second round of simplified Chinese
 characters (not officially implemented)Ideographs required by the Specification of Common
 Modern Chinese Character Components and Components Names
	 (现代常用字部件及部件名称规范), published in mainland
 China in 2009Other changes; see the ChangeLog file in
 the main package for details.
* 晓晓Akatsuki, Boris Zhang,Kusanagi_Sans,and
 others updated over 100 Chinese ideographs in Planes 0, 2, and 3:Modified ideographs containing the "馬" (Horse) and "鳥"
 (Bird) radicals to be more balancedThe first batch of simplified Chinese character lists
 (第一批簡體字表) (August 21, 1935~February 1936)Chinese Character Simplification Scheme (1956–1986)The simplified character list (1986–2013), including
 simplified radicals and Chinese characters used for
 descriptions and annotations in official documentsThe second list of the Second round of simplified Chinese
 characters (not officially implemented)Ideographs required by the Specification of Common
 Modern Chinese Character Components and Components Names
	 (现代常用字部件及部件名称规范), published in mainland
 China in 2009Other changes; see the ChangeLog file in
 the main package for details.
* Modified ideographs containing the "馬" (Horse) and "鳥"
 (Bird) radicals to be more balanced
* The first batch of simplified Chinese character lists
 (第一批簡體字表) (August 21, 1935~February 1936)
* Chinese Character Simplification Scheme (1956–1986)
* The simplified character list (1986–2013), including
 simplified radicals and Chinese characters used for
 descriptions and annotations in official documents
* The second list of the Second round of simplified Chinese
 characters (not officially implemented)
* Ideographs required by the Specification of Common
 Modern Chinese Character Components and Components Names
	 (现代常用字部件及部件名称规范), published in mainland
 China in 2009
* Other changes; see the ChangeLog file in
 the main package for details.
* 18 October 2025 (Unifont 17.0.02)Plane 0:Paul Hardymodififed U+1521, U+A93D, and U+FB30.David Corbettmodified U+2B96, U+!7CE, U+A7CF, and U+A7D2晓晓Akatsukiadjusted U+4748, U+6B25, and U+6F78 per the latest
 Unicode recommendations. Adjusted U+5100 to be 16 pixels tall.Plane 1:Paul Hardymodififed U+1E912 per Unicode 17.0.0 errata.David Corbettmodified U+1CEDD, U+1E6DE, U+1F778,
 U+1CEF0, U+1F77A, U+11DCC, U+11DCD, U+11DD6.
 Adjusted base height in chess glyphs U+1FA54..U+1FA57 and eye
 height in U+1FA55 and U+1FA57 to match eye height of knights.晓晓Akatsukidrew smaller versions of U+16FF2 and U+16FF3.Plane 2:For complete coverage of jf7000 0.9,Boris Zhangadded U+217DA and U+21A4B;湖 远星added U+24259, U+249DF, and U+270FD.晓晓Akatsukiredrew U+29B9A.Plane 3:晓晓Akatsukidrew U+323B0..U+32401, U+32403..U+32406,
	 U+32409..U+32452, U+32454..U+3246A, U+3246C..U+3247D,
	 U+3247F..U+32484, U+32486..U+3248D, and U+3248F..U+324A4.Boris Zhangredrew U+2B7A4, U+2B7E8, and U+2EC06.Boris Zhangdrew U+32402, U+32407, U+32408, U+32453, U+3246B,
 U+3247E, U+32485, U+3248E, U+324D1, U+324DD, U+324DE, U+324E0,
 U+3251F, U+32520, U+3261E, U+32623, U+32629, U+3262C, U+32631,
 U+32632, U+32635, U+3263B, U+3263C, U+3263F, U+32640, U+32641,
 U+32644, U+32646, U+32647, U+3264F, U+32650, U+32656, U+32657,
 U+3265A, U+3265D, U+3265E, U+3265F, U+32660, U+32662, U+32669,
 U+3266F, U+32672, U+32674, U+3267B, U+3267C, U+3267D, U+32688,
 U+3268A, U+3268F, U+32694, U+32695, U+3269A, U+326AD, U+326BD,
 U+326BE, U+326C0, U+326F5, U+326FA, U+32709, U+3270B, U+32714,
 U+32744, U+32748, U+3274B, U+3274C, U+3274E, U+32755, U+32765,
 U+32768, U+32769, U+327C0, U+327C3, U+327FB, U+32800, U+32859,
 U+3285A, U+3285F, U+3287C, U+32901, U+32940, U+3295B, U+32985,
 U+32996, U+32997, U+32A3A, U+32A3B, U+32A4C, U+32A5A, U+32A72,
 U+32A98, U+32ACE, U+32AF9, U+32BDD, U+32BE1, U+32BE8, U+32BFF,
 U+32C0A, U+32C0D, U+32C0E, U+32C13, U+32C36, U+32C37, U+32C39,
 U+32C3B, U+32C3C, U+32C82, U+32CCA, U+32CCC, U+32CCD, U+32CD3,
 U+32CD4, U+32CD6, U+32CDA, U+32CDC, U+32CDD, U+32CE4, U+32CE5,
 U+32CE6, U+32CF3, U+32CF4, U+32CF7, U+32CFD, U+32D09, U+32D46,
 U+32D49, U+32D4F, U+32D50, U+32D79, U+32D89, U+32DAF, U+32DB7,
 U+32E2F, U+32E31, U+32E34, U+32E8B, U+32EA3, U+32ED0, U+32EF0,
 U+32EF2, U+32F17, U+32F1D, U+32F1E, U+32F36, U+32F49, U+32F56,
 U+32F58, U+32F59, U+32F6C, U+32F8C, U+32F9D, U+32FF9, U+3301A,
 U+33074, U+33084, U+330AC, U+330D4, U+330F1, U+330F2, U+33113,
 U+33157, U+331B2, U+331E7, U+331E9, U+331EA, U+331EF, U+331F0,
 U+331F2, U+33211, U+33213, U+33214, U+33215, U+33216, U+33217,
 U+3321B, U+33220, U+3323A, U+33255, U+33257, U+33261, U+33279,
 U+3327A, U+3327C, U+33282, U+33283, U+33287, U+3328B, U+3328E,
 U+3328F, U+33291, U+33293, U+33294, U+332AD, U+332BF, U+332E1,
 U+3331A, U+3331E, U+33366, U+33397, U+33398, U+3339A, U+3339D,
 U+33400, U+3340A, and U+33410.
* Plane 0:Paul Hardymodififed U+1521, U+A93D, and U+FB30.David Corbettmodified U+2B96, U+!7CE, U+A7CF, and U+A7D2晓晓Akatsukiadjusted U+4748, U+6B25, and U+6F78 per the latest
 Unicode recommendations. Adjusted U+5100 to be 16 pixels tall.
* Paul Hardymodififed U+1521, U+A93D, and U+FB30.
* David Corbettmodified U+2B96, U+!7CE, U+A7CF, and U+A7D2
* 晓晓Akatsukiadjusted U+4748, U+6B25, and U+6F78 per the latest
 Unicode recommendations. Adjusted U+5100 to be 16 pixels tall.
* Plane 1:Paul Hardymodififed U+1E912 per Unicode 17.0.0 errata.David Corbettmodified U+1CEDD, U+1E6DE, U+1F778,
 U+1CEF0, U+1F77A, U+11DCC, U+11DCD, U+11DD6.
 Adjusted base height in chess glyphs U+1FA54..U+1FA57 and eye
 height in U+1FA55 and U+1FA57 to match eye height of knights.晓晓Akatsukidrew smaller versions of U+16FF2 and U+16FF3.
* Paul Hardymodififed U+1E912 per Unicode 17.0.0 errata.
* David Corbettmodified U+1CEDD, U+1E6DE, U+1F778,
 U+1CEF0, U+1F77A, U+11DCC, U+11DCD, U+11DD6.
 Adjusted base height in chess glyphs U+1FA54..U+1FA57 and eye
 height in U+1FA55 and U+1FA57 to match eye height of knights.
* 晓晓Akatsukidrew smaller versions of U+16FF2 and U+16FF3.
* Plane 2:For complete coverage of jf7000 0.9,Boris Zhangadded U+217DA and U+21A4B;湖 远星added U+24259, U+249DF, and U+270FD.晓晓Akatsukiredrew U+29B9A.
* For complete coverage of jf7000 0.9,Boris Zhangadded U+217DA and U+21A4B;湖 远星added U+24259, U+249DF, and U+270FD.
* 晓晓Akatsukiredrew U+29B9A.
* Plane 3:晓晓Akatsukidrew U+323B0..U+32401, U+32403..U+32406,
	 U+32409..U+32452, U+32454..U+3246A, U+3246C..U+3247D,
	 U+3247F..U+32484, U+32486..U+3248D, and U+3248F..U+324A4.Boris Zhangredrew U+2B7A4, U+2B7E8, and U+2EC06.Boris Zhangdrew U+32402, U+32407, U+32408, U+32453, U+3246B,
 U+3247E, U+32485, U+3248E, U+324D1, U+324DD, U+324DE, U+324E0,
 U+3251F, U+32520, U+3261E, U+32623, U+32629, U+3262C, U+32631,
 U+32632, U+32635, U+3263B, U+3263C, U+3263F, U+32640, U+32641,
 U+32644, U+32646, U+32647, U+3264F, U+32650, U+32656, U+32657,
 U+3265A, U+3265D, U+3265E, U+3265F, U+32660, U+32662, U+32669,
 U+3266F, U+32672, U+32674, U+3267B, U+3267C, U+3267D, U+32688,
 U+3268A, U+3268F, U+32694, U+32695, U+3269A, U+326AD, U+326BD,
 U+326BE, U+326C0, U+326F5, U+326FA, U+32709, U+3270B, U+32714,
 U+32744, U+32748, U+3274B, U+3274C, U+3274E, U+32755, U+32765,
 U+32768, U+32769, U+327C0, U+327C3, U+327FB, U+32800, U+32859,
 U+3285A, U+3285F, U+3287C, U+32901, U+32940, U+3295B, U+32985,
 U+32996, U+32997, U+32A3A, U+32A3B, U+32A4C, U+32A5A, U+32A72,
 U+32A98, U+32ACE, U+32AF9, U+32BDD, U+32BE1, U+32BE8, U+32BFF,
 U+32C0A, U+32C0D, U+32C0E, U+32C13, U+32C36, U+32C37, U+32C39,
 U+32C3B, U+32C3C, U+32C82, U+32CCA, U+32CCC, U+32CCD, U+32CD3,
 U+32CD4, U+32CD6, U+32CDA, U+32CDC, U+32CDD, U+32CE4, U+32CE5,
 U+32CE6, U+32CF3, U+32CF4, U+32CF7, U+32CFD, U+32D09, U+32D46,
 U+32D49, U+32D4F, U+32D50, U+32D79, U+32D89, U+32DAF, U+32DB7,
 U+32E2F, U+32E31, U+32E34, U+32E8B, U+32EA3, U+32ED0, U+32EF0,
 U+32EF2, U+32F17, U+32F1D, U+32F1E, U+32F36, U+32F49, U+32F56,
 U+32F58, U+32F59, U+32F6C, U+32F8C, U+32F9D, U+32FF9, U+3301A,
 U+33074, U+33084, U+330AC, U+330D4, U+330F1, U+330F2, U+33113,
 U+33157, U+331B2, U+331E7, U+331E9, U+331EA, U+331EF, U+331F0,
 U+331F2, U+33211, U+33213, U+33214, U+33215, U+33216, U+33217,
 U+3321B, U+33220, U+3323A, U+33255, U+33257, U+33261, U+33279,
 U+3327A, U+3327C, U+33282, U+33283, U+33287, U+3328B, U+3328E,
 U+3328F, U+33291, U+33293, U+33294, U+332AD, U+332BF, U+332E1,
 U+3331A, U+3331E, U+33366, U+33397, U+33398, U+3339A, U+3339D,
 U+33400, U+3340A, and U+33410.
* 晓晓Akatsukidrew U+323B0..U+32401, U+32403..U+32406,
	 U+32409..U+32452, U+32454..U+3246A, U+3246C..U+3247D,
	 U+3247F..U+32484, U+32486..U+3248D, and U+3248F..U+324A4.
* Boris Zhangredrew U+2B7A4, U+2B7E8, and U+2EC06.
* Boris Zhangdrew U+32402, U+32407, U+32408, U+32453, U+3246B,
 U+3247E, U+32485, U+3248E, U+324D1, U+324DD, U+324DE, U+324E0,
 U+3251F, U+32520, U+3261E, U+32623, U+32629, U+3262C, U+32631,
 U+32632, U+32635, U+3263B, U+3263C, U+3263F, U+32640, U+32641,
 U+32644, U+32646, U+32647, U+3264F, U+32650, U+32656, U+32657,
 U+3265A, U+3265D, U+3265E, U+3265F, U+32660, U+32662, U+32669,
 U+3266F, U+32672, U+32674, U+3267B, U+3267C, U+3267D, U+32688,
 U+3268A, U+3268F, U+32694, U+32695, U+3269A, U+326AD, U+326BD,
 U+326BE, U+326C0, U+326F5, U+326FA, U+32709, U+3270B, U+32714,
 U+32744, U+32748, U+3274B, U+3274C, U+3274E, U+32755, U+32765,
 U+32768, U+32769, U+327C0, U+327C3, U+327FB, U+32800, U+32859,
 U+3285A, U+3285F, U+3287C, U+32901, U+32940, U+3295B, U+32985,
 U+32996, U+32997, U+32A3A, U+32A3B, U+32A4C, U+32A5A, U+32A72,
 U+32A98, U+32ACE, U+32AF9, U+32BDD, U+32BE1, U+32BE8, U+32BFF,
 U+32C0A, U+32C0D, U+32C0E, U+32C13, U+32C36, U+32C37, U+32C39,
 U+32C3B, U+32C3C, U+32C82, U+32CCA, U+32CCC, U+32CCD, U+32CD3,
 U+32CD4, U+32CD6, U+32CDA, U+32CDC, U+32CDD, U+32CE4, U+32CE5,
 U+32CE6, U+32CF3, U+32CF4, U+32CF7, U+32CFD, U+32D09, U+32D46,
 U+32D49, U+32D4F, U+32D50, U+32D79, U+32D89, U+32DAF, U+32DB7,
 U+32E2F, U+32E31, U+32E34, U+32E8B, U+32EA3, U+32ED0, U+32EF0,
 U+32EF2, U+32F17, U+32F1D, U+32F1E, U+32F36, U+32F49, U+32F56,
 U+32F58, U+32F59, U+32F6C, U+32F8C, U+32F9D, U+32FF9, U+3301A,
 U+33074, U+33084, U+330AC, U+330D4, U+330F1, U+330F2, U+33113,
 U+33157, U+331B2, U+331E7, U+331E9, U+331EA, U+331EF, U+331F0,
 U+331F2, U+33211, U+33213, U+33214, U+33215, U+33216, U+33217,
 U+3321B, U+33220, U+3323A, U+33255, U+33257, U+33261, U+33279,
 U+3327A, U+3327C, U+33282, U+33283, U+33287, U+3328B, U+3328E,
 U+3328F, U+33291, U+33293, U+33294, U+332AD, U+332BF, U+332E1,
 U+3331A, U+3331E, U+33366, U+33397, U+33398, U+3339A, U+3339D,
 U+33400, U+3340A, and U+33410.
* 9 September 2025 (Unifont 17.0.01)Plane 0:David Corbettcontributed the new Arabic glyphs:Arabic Extended-B: U+088FRiyal currency symbol: U+20C1Arabic Presentation Forms-A: U+FBC3..U+FBD2, U+FD90, U+FD91,
 and U+FDC8..U+FDCE.Paul Hardyadded:Telugu: U+0C5CKannada: U+0CDCCombining Diacritical Marks Extended: U+1ACF..U+1ADD,
 and U+1AE0..U+1AEBUpdated U+1BBFMiscellaneous Symbols and Arrows: U+2B96Latin Extended-D: U+A7CE, U+A7CF, U+A7D2, U+A7D4, and U+A7F1Latin Extended-E: modified U+AB4B and U+AB4C per Unicode
 17.0.0 recommendation.Plane 1:David Corbettcontributed the new Arabic Extended-C glyphs:
 U+10EC5..U+10EC7, U+10ED0..U+10ED8, U+10EFA, and U+10EFB.Johnnie Weavercontributed:U+10940..U+1095F (Sidetic)*U+11DB0..U+11DEF (Tolong Siki)*U+16EA0..U+16EDF (Beria Erfe)*U+1E900..U+1E95F (Adlam), modified per Unicode 17.0.0 changes.Paul Hardycontributed:U+11B60..U+11B67 (Sharada Supplement)*U+16FF2..U+16FF6 (Ideographic Symbols and Punctuation)U+1CCFA..U+1CCFC and U+1CEBA..U+1CEBF (Symbols for Legacy
 Computing Supplement).U+1CEC0..U+1DEFF (Miscellaneous Symbols Supplement)*U+1E6C0..U+1E6FF (Tai Yo)*U+1F6D8 (Transport and Map Symbols)U+1F8D0..U+1F8D8 (Supplemental Arrows-C)U+1FBFA (Symbols for Legacy Computing).Plane 2:Yzy32767made these contributions:Improved these glyphs in the first list of the second round
 of simplified Chinese characters: U+0200D3 and U+0201A8Added these glyphs in the first list of the second round
 of simplified Chinese characters: U+20B15, U+20BB5,
 U+20CAD, U+219F3, U+21C52, U+22342, U+22488, U+22A83,
 U+2418A, U+2462F, U+26678, U+26B01, U+2A9F7, U+2BA4F,
 U+2BA51, U+2BBDC, U+2BCB7, U+2BDC0, U+2BE6F, U+2D026,
 U+2D64F, U+2D70C, U+2DCFF, and U+2E0B9Fixed U+2CAD2, which wfz2020 noticed appeared
 as the glyph for code point U+2CA02.Plane 3:Yzy32767made these contributions:Improved these glyphs in the first list of the second
 round of simplified Chinese characters: U+030008, U+030061,
 U+03006C, U+03011D, U+03014A, and U+0301E3Added these glyphs: U+30180..U+301E2, U+301E4..U+301FF,
 U+30270, U+302D9, U+302DB, U+302DC, U+302DE, U+302F7,
 U+302FB, U+30335, U+3033B, U+3034E, U+30370, U+30371,
 U+30409, U+30414, U+3043A, U+3043F, U+3044A, U+3044C,
 U+30450, U+3045D, U+3045E, U+304CC, U+304E2, U+304E3,
 U+304E8, U+304ED, U+3057A, U+305D1, U+305DD, U+305F6,
 U+3067D, U+306D1, U+306D3, U+306EC, U+30708, U+30776,
 U+30831, U+30842, U+308F2, U+3094C, U+30955, U+30969,
 U+30993, U+309AA, U+309AB, U+30A1B, U+30A62, U+30AA9,
 U+30AB1, U+30AFE, U+30B04, U+30B0A, U+30B15, U+30B43,
 U+30B4B, U+30B5D, U+30BF6, U+30C21, U+30C2B, U+30CBD,
 U+30CC7, U+30D4B, U+30D55, U+30D5F, U+30DDF, U+30DE3,
 U+30E01, U+30E04, U+30E70, U+30E79, U+30F03, U+30F5F,
 U+30F64, U+30F82, U+310AA, U+3114C, and U+31151.*New in Unicode 17.0.0.
* Plane 0:David Corbettcontributed the new Arabic glyphs:Arabic Extended-B: U+088FRiyal currency symbol: U+20C1Arabic Presentation Forms-A: U+FBC3..U+FBD2, U+FD90, U+FD91,
 and U+FDC8..U+FDCE.Paul Hardyadded:Telugu: U+0C5CKannada: U+0CDCCombining Diacritical Marks Extended: U+1ACF..U+1ADD,
 and U+1AE0..U+1AEBUpdated U+1BBFMiscellaneous Symbols and Arrows: U+2B96Latin Extended-D: U+A7CE, U+A7CF, U+A7D2, U+A7D4, and U+A7F1Latin Extended-E: modified U+AB4B and U+AB4C per Unicode
 17.0.0 recommendation.
* David Corbettcontributed the new Arabic glyphs:Arabic Extended-B: U+088FRiyal currency symbol: U+20C1Arabic Presentation Forms-A: U+FBC3..U+FBD2, U+FD90, U+FD91,
 and U+FDC8..U+FDCE.
* Arabic Extended-B: U+088F
* Riyal currency symbol: U+20C1
* Arabic Presentation Forms-A: U+FBC3..U+FBD2, U+FD90, U+FD91,
 and U+FDC8..U+FDCE.
* Paul Hardyadded:Telugu: U+0C5CKannada: U+0CDCCombining Diacritical Marks Extended: U+1ACF..U+1ADD,
 and U+1AE0..U+1AEBUpdated U+1BBFMiscellaneous Symbols and Arrows: U+2B96Latin Extended-D: U+A7CE, U+A7CF, U+A7D2, U+A7D4, and U+A7F1Latin Extended-E: modified U+AB4B and U+AB4C per Unicode
 17.0.0 recommendation.
* Telugu: U+0C5C
* Kannada: U+0CDC
* Combining Diacritical Marks Extended: U+1ACF..U+1ADD,
 and U+1AE0..U+1AEB
* Updated U+1BBFMiscellaneous Symbols and Arrows: U+2B96Latin Extended-D: U+A7CE, U+A7CF, U+A7D2, U+A7D4, and U+A7F1Latin Extended-E: modified U+AB4B and U+AB4C per Unicode
 17.0.0 recommendation.
* Miscellaneous Symbols and Arrows: U+2B96
* Latin Extended-D: U+A7CE, U+A7CF, U+A7D2, U+A7D4, and U+A7F1
* Latin Extended-E: modified U+AB4B and U+AB4C per Unicode
 17.0.0 recommendation.
* Plane 1:David Corbettcontributed the new Arabic Extended-C glyphs:
 U+10EC5..U+10EC7, U+10ED0..U+10ED8, U+10EFA, and U+10EFB.Johnnie Weavercontributed:U+10940..U+1095F (Sidetic)*U+11DB0..U+11DEF (Tolong Siki)*U+16EA0..U+16EDF (Beria Erfe)*U+1E900..U+1E95F (Adlam), modified per Unicode 17.0.0 changes.Paul Hardycontributed:U+11B60..U+11B67 (Sharada Supplement)*U+16FF2..U+16FF6 (Ideographic Symbols and Punctuation)U+1CCFA..U+1CCFC and U+1CEBA..U+1CEBF (Symbols for Legacy
 Computing Supplement).U+1CEC0..U+1DEFF (Miscellaneous Symbols Supplement)*U+1E6C0..U+1E6FF (Tai Yo)*U+1F6D8 (Transport and Map Symbols)U+1F8D0..U+1F8D8 (Supplemental Arrows-C)U+1FBFA (Symbols for Legacy Computing).
* David Corbettcontributed the new Arabic Extended-C glyphs:
 U+10EC5..U+10EC7, U+10ED0..U+10ED8, U+10EFA, and U+10EFB.
* Johnnie Weavercontributed:U+10940..U+1095F (Sidetic)*U+11DB0..U+11DEF (Tolong Siki)*U+16EA0..U+16EDF (Beria Erfe)*U+1E900..U+1E95F (Adlam), modified per Unicode 17.0.0 changes.
* U+10940..U+1095F (Sidetic)*
* U+11DB0..U+11DEF (Tolong Siki)*
* U+16EA0..U+16EDF (Beria Erfe)*
* U+1E900..U+1E95F (Adlam), modified per Unicode 17.0.0 changes.
* Paul Hardycontributed:U+11B60..U+11B67 (Sharada Supplement)*U+16FF2..U+16FF6 (Ideographic Symbols and Punctuation)U+1CCFA..U+1CCFC and U+1CEBA..U+1CEBF (Symbols for Legacy
 Computing Supplement).U+1CEC0..U+1DEFF (Miscellaneous Symbols Supplement)*U+1E6C0..U+1E6FF (Tai Yo)*U+1F6D8 (Transport and Map Symbols)U+1F8D0..U+1F8D8 (Supplemental Arrows-C)U+1FBFA (Symbols for Legacy Computing).
* U+11B60..U+11B67 (Sharada Supplement)*
* U+16FF2..U+16FF6 (Ideographic Symbols and Punctuation)
* U+1CCFA..U+1CCFC and U+1CEBA..U+1CEBF (Symbols for Legacy
 Computing Supplement).
* U+1CEC0..U+1DEFF (Miscellaneous Symbols Supplement)*
* U+1E6C0..U+1E6FF (Tai Yo)*
* U+1F6D8 (Transport and Map Symbols)
* U+1F8D0..U+1F8D8 (Supplemental Arrows-C)
* U+1FBFA (Symbols for Legacy Computing).
* Plane 2:Yzy32767made these contributions:Improved these glyphs in the first list of the second round
 of simplified Chinese characters: U+0200D3 and U+0201A8Added these glyphs in the first list of the second round
 of simplified Chinese characters: U+20B15, U+20BB5,
 U+20CAD, U+219F3, U+21C52, U+22342, U+22488, U+22A83,
 U+2418A, U+2462F, U+26678, U+26B01, U+2A9F7, U+2BA4F,
 U+2BA51, U+2BBDC, U+2BCB7, U+2BDC0, U+2BE6F, U+2D026,
 U+2D64F, U+2D70C, U+2DCFF, and U+2E0B9Fixed U+2CAD2, which wfz2020 noticed appeared
 as the glyph for code point U+2CA02.
* Yzy32767made these contributions:Improved these glyphs in the first list of the second round
 of simplified Chinese characters: U+0200D3 and U+0201A8Added these glyphs in the first list of the second round
 of simplified Chinese characters: U+20B15, U+20BB5,
 U+20CAD, U+219F3, U+21C52, U+22342, U+22488, U+22A83,
 U+2418A, U+2462F, U+26678, U+26B01, U+2A9F7, U+2BA4F,
 U+2BA51, U+2BBDC, U+2BCB7, U+2BDC0, U+2BE6F, U+2D026,
 U+2D64F, U+2D70C, U+2DCFF, and U+2E0B9Fixed U+2CAD2, which wfz2020 noticed appeared
 as the glyph for code point U+2CA02.
* Improved these glyphs in the first list of the second round
 of simplified Chinese characters: U+0200D3 and U+0201A8
* Added these glyphs in the first list of the second round
 of simplified Chinese characters: U+20B15, U+20BB5,
 U+20CAD, U+219F3, U+21C52, U+22342, U+22488, U+22A83,
 U+2418A, U+2462F, U+26678, U+26B01, U+2A9F7, U+2BA4F,
 U+2BA51, U+2BBDC, U+2BCB7, U+2BDC0, U+2BE6F, U+2D026,
 U+2D64F, U+2D70C, U+2DCFF, and U+2E0B9
* Fixed U+2CAD2, which wfz2020 noticed appeared
 as the glyph for code point U+2CA02.
* Plane 3:Yzy32767made these contributions:Improved these glyphs in the first list of the second
 round of simplified Chinese characters: U+030008, U+030061,
 U+03006C, U+03011D, U+03014A, and U+0301E3Added these glyphs: U+30180..U+301E2, U+301E4..U+301FF,
 U+30270, U+302D9, U+302DB, U+302DC, U+302DE, U+302F7,
 U+302FB, U+30335, U+3033B, U+3034E, U+30370, U+30371,
 U+30409, U+30414, U+3043A, U+3043F, U+3044A, U+3044C,
 U+30450, U+3045D, U+3045E, U+304CC, U+304E2, U+304E3,
 U+304E8, U+304ED, U+3057A, U+305D1, U+305DD, U+305F6,
 U+3067D, U+306D1, U+306D3, U+306EC, U+30708, U+30776,
 U+30831, U+30842, U+308F2, U+3094C, U+30955, U+30969,
 U+30993, U+309AA, U+309AB, U+30A1B, U+30A62, U+30AA9,
 U+30AB1, U+30AFE, U+30B04, U+30B0A, U+30B15, U+30B43,
 U+30B4B, U+30B5D, U+30BF6, U+30C21, U+30C2B, U+30CBD,
 U+30CC7, U+30D4B, U+30D55, U+30D5F, U+30DDF, U+30DE3,
 U+30E01, U+30E04, U+30E70, U+30E79, U+30F03, U+30F5F,
 U+30F64, U+30F82, U+310AA, U+3114C, and U+31151.
* Yzy32767made these contributions:Improved these glyphs in the first list of the second
 round of simplified Chinese characters: U+030008, U+030061,
 U+03006C, U+03011D, U+03014A, and U+0301E3Added these glyphs: U+30180..U+301E2, U+301E4..U+301FF,
 U+30270, U+302D9, U+302DB, U+302DC, U+302DE, U+302F7,
 U+302FB, U+30335, U+3033B, U+3034E, U+30370, U+30371,
 U+30409, U+30414, U+3043A, U+3043F, U+3044A, U+3044C,
 U+30450, U+3045D, U+3045E, U+304CC, U+304E2, U+304E3,
 U+304E8, U+304ED, U+3057A, U+305D1, U+305DD, U+305F6,
 U+3067D, U+306D1, U+306D3, U+306EC, U+30708, U+30776,
 U+30831, U+30842, U+308F2, U+3094C, U+30955, U+30969,
 U+30993, U+309AA, U+309AB, U+30A1B, U+30A62, U+30AA9,
 U+30AB1, U+30AFE, U+30B04, U+30B0A, U+30B15, U+30B43,
 U+30B4B, U+30B5D, U+30BF6, U+30C21, U+30C2B, U+30CBD,
 U+30CC7, U+30D4B, U+30D55, U+30D5F, U+30DDF, U+30DE3,
 U+30E01, U+30E04, U+30E70, U+30E79, U+30F03, U+30F5F,
 U+30F64, U+30F82, U+310AA, U+3114C, and U+31151.
* Improved these glyphs in the first list of the second
 round of simplified Chinese characters: U+030008, U+030061,
 U+03006C, U+03011D, U+03014A, and U+0301E3
* Added these glyphs: U+30180..U+301E2, U+301E4..U+301FF,
 U+30270, U+302D9, U+302DB, U+302DC, U+302DE, U+302F7,
 U+302FB, U+30335, U+3033B, U+3034E, U+30370, U+30371,
 U+30409, U+30414, U+3043A, U+3043F, U+3044A, U+3044C,
 U+30450, U+3045D, U+3045E, U+304CC, U+304E2, U+304E3,
 U+304E8, U+304ED, U+3057A, U+305D1, U+305DD, U+305F6,
 U+3067D, U+306D1, U+306D3, U+306EC, U+30708, U+30776,
 U+30831, U+30842, U+308F2, U+3094C, U+30955, U+30969,
 U+30993, U+309AA, U+309AB, U+30A1B, U+30A62, U+30AA9,
 U+30AB1, U+30AFE, U+30B04, U+30B0A, U+30B15, U+30B43,
 U+30B4B, U+30B5D, U+30BF6, U+30C21, U+30C2B, U+30CBD,
 U+30CC7, U+30D4B, U+30D55, U+30D5F, U+30DDF, U+30DE3,
 U+30E01, U+30E04, U+30E70, U+30E79, U+30F03, U+30F5F,
 U+30F64, U+30F82, U+310AA, U+3114C, and U+31151.

#### Unifont 16.0

* 31 May 2025 (Unifont 16.0.04)Plane 0:Paul HardyModified the archaic Greek digamma glyphs,
 U+03DC and U+03DD.Modified the Korean Won currency symbol, U+20A9,
 to only have one bar.Removed Variation Selector glyphs (U+FE00..U+FE0F)
 from default OpenType and TrueType font builds;
 they remain in the sample and SBIT font builds.David CorbettModified Arabic glyphs U+0610, U+0616, U+061E,
 U+0620, and U+0626.Redrew the yeh-based glyphs in the ranges
 U+FC31..U+FDC7 (Arabic Presentation Forms-A) and
 U+FE89..U+FE8C (Arabic Presentation Forms-B).Johnnie Weavermodified some Georgian Supplement glyphs (U+2D00..U+2D2F).晓晓_Akatsuki (Xiao_Akatsuki)modified U+2EB2 per Unicode updates.Plane 1:Paul HardyUpdated Old Turkic glyph U+10C47.Updated Khitan Small Script glyph U+18CCA.Reverted several changes in Musical Symbols
 (U+1D100..U+1D1FF) for better positioning with combining
 characters. Thanks go out to David Corbett for requesting
 the changes.Modified mathematical bold digamma (U+1D7CA, U+1D7CB)
 to match the updated digamma glyphs in Plane 0.Josh Huffordcontributed modified emoji glyphs
 U+1F602, U+1F605, U+1F606, U+1F607, U+1F609, U+1F923, and
 U+1FAE0.Plane 14:Paul HardyRemoved Variation Selector glyphs (U+E0100..U+E01EF)
 from default OpenType and TrueType font builds;
 they remain in the sample and SBIT font builds.Plane 15 (CSUR/UCSUR):soweli Kape[sic] andNikZappUpdated Sitelen Pona (U+F1900..U+F19FF)Updated Sitelen Pona Radicals (U+F1C80..U+F1C9F).Paul HardyAdded Titi Pula (U+F1C40..UU+F1C60)Added Zbalermorna (U+F28A0..UU+F28DF).19 April 2025 (Unifont 16.0.03)Plane 0:David Corbettredrew some Arabic glyphs for consistency. Most of these
 are minor changes to baseline, i‘jam positioning, or making
 a derived letter match its origin letter. Code points:
 U+0625, U+0634, U+0673, U+06B9, U+06BC, U+0753, U+0754,
 U+0757, U+075C, U+0762, U+0767, U+0769, U+076A, U+076D,
 U+0770, U+0775, U+0776, U+0777, U+077D, U+077E, U+08A1,
 U+08A2, U+08A3, U+08A6, U+08A8, U+08B1, U+08BB, and U+08BC.晓晓_Akatsuki (Xiao_Akatsuki)submitted
 several CJK refinements from the team of湖 远星:Improved 褝 (U+891D) and 肞 (U+809E).Updated to reflect current Unicode rendering:
 㳽 (U+3CFD), 㸿 (U+3E3F), 䑮 (U+446E), 䒳 (U+44B3), 䕈 (U+4548),
 and 䩶 (U+4A76).Updated as per GB18030-2022 change: 垕 (U+5795).Modified to comply with the GB18030-2022 standard pertaining to
 character composition:姉 (U+59C9): This character is a phono-semantic character.
 Therefore, the right side should be "市" (U+5E02) instead
 of "巿" (U+5DFF).濲 (U+6FF2): This character is a variant of "瀔" (U+7014),
 and the "穀" (U+7A40) on the right side of "瀔" (U+7014) is
 a phono-semantic character, and its "semantic" part is "禾"
 (U+79BE), not "木" (U+6728).膥 (U+81A5): This character is a Cantonese character for "egg".
 Not yet (未) Become (成) Meat (肉) → Egg, so the upper left
 corner should be "未" (U+672A), not "末" (U+672B).David Corbett:Redrew some Arabic Presentation Forms:
 U+FD42, U+FD43, U+FD44, U+FD45, U+FDF0, U+FDF1, U+FDF4,
 U+FDF6, U+FDF7, U+FDFA, U+FDFB, U+FDFC, U+FE87, U+FE88,
 U+FEB5, and U+FEB6.Modified the top serifs of two Latin fullwidth letters, U+FF44 and U+FF4B.Plane 1:Paul Hardyadded new glyphs in Egyptian Hieroglyph Format Controls
 (U+13430..U+1345F).Paul HardyandDavid Corbettmade adjustments to
 glyphs in the Musical Symbols block (U+1D100..U+1D1FF).Plane 2:晓晓_Akatsukimodified U+25ED7 from 16 columns wide to 15 columns.Hayden Wongcontributed U+29B00..U+29CFF.Cod'dtesent a corrected left-hand side of U+2EE57.Plane 3:Luke036has drawn a much-improved glyph for taito (U+3106C).1 December 2024 (Unifont 16.0.02)Plane 0:Johnnie Weavermodified the
 U+13C9 Cherokee and U+AB99 Cherokee Supplement glyphs.湖 远星modified Chinese glyphs
 U+605C, U+6669, and U+6A37.Plane 1:Johnnie Weavermodified several glyphs in the
 ranges U+10880..U+108AF (Nabataean) and U+108E0..U+108FF
 (Hatran) so these scripts are now completely half-width.Paul Hardymodified several Tulu-Tilagari glyphs
 (U+11380..U+113FF), and modified the Kawi glyph U+11F5A
 to resemble U+11F49 (per David Corbett's recommendations).Xiao Akatsuki (晓晓 Akatsuki)fixed a missing
 vertical stroke in U+18B2D.湖 远星added more space between the two
 halves of U+1F232.Plane 2:Hayden Wongmade these changes:Modified U+20083, U+20087, U+20089, and
 U+200B4 from 16 columns wide to 15 columns.Added the missing glyphs in the range U+20000..U+299FF.Completed U+29D00..U+29DFF.Added U+2B64E, which is an incorrect variant
 of U+513A (儺).晓晓 Akatsukicontributed the missing glyphs
 in the range U+20700..U+207FF.湖 远星modified U+28A0F, U+28B4E, U+2CB5B,
 and U+2CB73 from 16 columns wide to 15 columns.Boris Zhangnoticed that U+2C7EC was the glyph
 for U+2CE7C, so it was removed.10 September 2024 (Unifont 16.0.01)Plane 0:David Corbettadded U+0897, ARABIC PEPET.Paul Hardyadded the new glyphs in
 Balinese (U+1B4E, U+1B4F, and U+1B7F),
 Cyrillic Extended-C (U+1C89, U+1C8A), and
 Latin Extended-D (U+A7CB..U+A7CD, U+A7DA..U+A7DC).Johnnie Weaver:Modified Cherokee glyphs U+13C9 and U+AB99.Changed these glyphs to half-width:
 U+210E, U+210F, U+212E, U+212F, U+2300, U+2329, U+232A, U+2610,
 U+2611, U+2612, U+2713, U+2717, U+A728, U+A729, U+A732, U+A733,
 U+A734, U+A735, U+A736, U+A737, U+A738, U+A739, U+A73A, U+A73B,
 U+A73C, U+A73D, U+A74E, U+A74F, U+A758, U+A759, U+A771, U+A772,
 U+A773, U+A774, U+A775, U+A776, U+A777, U+A797, U+A7C2, and U+A7C3.Boris Zhangdrew the Suzhou Numerals six through
 nine (U+3026..U+3029).Rebecca Bettencourtdrew the new Control Pictures
 glyphs, U+2427..U+2429.Yzy32767redrew the Bopomofo glyphs (U+3105..U+312F)
 in a Kai (楷) style.湖 远星contributed the new glyphs in CJK Strokes
 (U+31D2, U+31E4, and U+31E5).Hayden Wongmodified U+3862 per Unicode 15.1.0.Plane 0 CSUR/UCSUR:Rebecca Bettencourtcontributed:U+E400..U+E59F Herman Miller's previosuly missing scriptsU+E6D0..U+E6EF AmlinUnifon glyphs U+E6FD and U+E73D, previously missingU+EC70..U+ECEF Graflect.Danae Dekkercontributed:U+EC00..U+EC2F CylenianU+EC30..U+EC6F Syrrin.Plane 1:Johnnie Weavercontributed:U+105C0..U+105FF Todhri*U+10D40..U+10D8F Garay*U+11BC0..U+11BFF Sunuwar*U+16D40..U+16D7F Kirat Rai*Khitan Small Script (U+18BD2, U+18BFF)U+1E5D0..U+1E5FF Ol Onal.*David Corbettcontributed:Arabic Extended-C
 glyphs U+10EC2..U+10EC4, U+10EFC.U+16100..U+1613F Gurung Khema*Paul Hardycontributed:U+11380..U+113FF Tulu-Tigalari*U+116D0..U+116E3 Myanmar Extended-C*Kawi glyph U+11F5ASymbols and Pictographs Extended-A glyphs
 U+1FA89, U+1FA8F, U+1FABE, U+1FAC6, U+1FADC,
 U+1FADF, and U+1FAE9.Rebecca Bettencourtcontributed:U+1CC00..U+1CCF9 Symbols for Legacy Computing Supplement*Supplemental Arrows-C glyphs U+1F8B2..U+18BB,
 U+1F8C0, and U+1F8C1Symbols for Legacy Computing glyphs U+1FBCB..U+1FBEF.anonymous1redrew Enclosed Ideographic Supplement
 glyph U+1F200.Plane 2:Hayden Wongcontributed the new glyphs in
 CJK Unified Ideographs Extension B U+20020..U+2004F
 and U+29E00..2A0FF.twuchiutanncontributed the new glyphs in
 CJK Unified Ideographs Extension B U+20050..U+2073F.Boris Zhangredrew CJK Unified Ideographs
 Extension D glyphs U+2B75F, U+2B76B, and
 Extension I glyphs U+2B7EF, U+2EC1F, U+2EC20,
 U+2EC21, U+2EC2F, U+2EC6F, U+2ECBF, U+2ECEC, and U+2ED42.湖 远星contributed the following glyphs, which are common
 in Cantonese, Hokkien, Hakka,etc.,from a list provided
 with the Ichiten font.CJK Unified Ideographs Extension B glyphs:U+203B7 𠎷U+20546 𠕆U+20584 𠖄U+205FB 𠗻U+207A9 𠞩U+207AD 𠞭U+20803 𠠃U+2081D 𠠝U+20895 𠢕U+20BD7 𠯗U+20C41 𠱁U+20CBF 𠲿U+20CD4 𠳔U+20D5D 𠵝U+20D71 𠵱U+20DA7 𠶧U+20E76 𠹶U+20E98 𠺘U+20ED8 𠻘U+20F3B 𠼻U+20F7E 𠽾U+21014 𡀔U+210AB 𡂫U+210F6 𡃶U+21145 𡅅U+2176D 𡝭U+217D3 𡟓U+2180D 𡠍U+21883 𡢃U+2197C 𡥼U+21C2A 𡰪U+21CA2 𡲢U+21CDE 𡳞U+21DD1 𡷑U+21F0F 𡼏U+221A1 𢆡U+22399 𢎙U+224DC 𢓜U+2251B 𢔛U+22775 𢝵U+22AB1 𢪱U+22AE6 𢫦U+22BED 𢯭U+22BFE 𢯾U+22C4B 𢱋U+22C62 𢱢U+22C64 𢱤U+22CB4 𢲴U+22CB8 𢲸U+22CC6 𢳆U+22CEA 𢳪U+22D80 𢶀U+22F0C 𢼌U+22F1B 𢼛U+23073 𣁳U+23074 𣁴U+23350 𣍐U+236BA 𣚺U+236EE 𣛮U+23B88 𣮈U+23CA9 𣲩U+23EF8 𣻸U+23F0E 𣼎U+240D2 𤃒U+241AC 𤆬U+24259 𤉙U+242B6 𤊶U+2430D 𤌍U+24352 𤍒U+24364 𤍤U+24419 𤐙U+24430 𤐰U+24605 𤘅U+2479A 𤞚U+24C8D 𤲍U+24D80 𤶀U+24D83 𤶃U+24E01 𤸁U+24E31 𤸱U+24E85 𤺅U+24EA7 𤺧U+24EAA 𤺪U+25148 𥅈U+2517E 𥅾U+2531A 𥌚U+25349 𥍉U+25435 𥐵U+2546E 𥑮U+257C7 𥟇U+25BDF 𥯟U+25BE5 𥯥U+25C14 𥰔U+25D0A 𥴊U+25E86 𥺆U+2624E 𦉎U+26293 𦊓U+26706 𦜆U+267EA 𦟪U+2688A 𦢊U+2690E 𦤎U+26E05 𦸅U+2725F 𧉟U+27304 𧌄U+27371 𧍱U+27486 𧒆U+277F0 𧟰U+279A0 𧦠U+27A63 𧩣U+27B2A 𧬪U+27B99 𧮙U+27EF4 𧻴U+27FC1 𧿁U+27FEC 𧿬U+27FF3 𧿳U+280BE 𨂾U+280BF 𨂿U+280E9 𨃩U+280F0 𨃰U+28154 𨅔U+282CD 𨋍U+2837D 𨍽U+2838A 𨎊U+28487 𨒇U+28595 𨖕U+28891 𨢑U+28D99 𨶙U+28E39 𨸹U+2945D 𩑝U+2947E 𩑾U+294E5 𩓥U+296A8 𩚨U+296E9 𩛩U+29704 𩜄U+29730 𩜰U+29D71 𩵱U+29DD3 𩷓U+29E19 𩸙U+29E36 𩸶U+29EAC 𩺬U+29F27 𩼧U+29F30 𩼰U+29F48 𩽈U+29F70 𩽰U+2A04E 𪁎U+2A0BA 𪂺U+2A1E1 𪇡U+2A41E 𪐞U+2A590 𪖐U+2A612 𪘒U+2A64A 𪙊CJK Unified Ideographs Extension C glyphs:U+2A736 𪜶, U+2AE5A 𪹚, and U+2B4A2 𫒢CJK Unified Ideographs Extension E glyphs:U+2B8C6 𫣆, U+2C816 𬠖, and U+2C9B0 𬦰.Plane 3:twuchiutannmodified U+30EDD and U+30EDE (biang),
	 originally drawn by Ming Fan, to differentiate between
	 traditional and simplified Chinese versions.湖 远星contributed the following glyphs, which are common in
 Cantonese, Hokkien, Hakka,etc.,from a list given in the
 Ichiten font.CJK Unified Ideographs Extension G glyphs:U+301DB 𰇛, U+308FB 𰣻, and U+30E6C 𰹬CJK Unified Ideographs Extension H glyph:U+31C7F 𱱿.Plane 15 CSUR/UCSUR:Rebecca Bettencourtcontributed:U+F16B0..U+F16DF DeraniU+F2000..U+F267F Sadalian.Paul Hardycontributed
 U+F1C80..U+F1C9C Sitelen Pona Radicals.*New in Unicode 16.0.0.
* Plane 0:Paul HardyModified the archaic Greek digamma glyphs,
 U+03DC and U+03DD.Modified the Korean Won currency symbol, U+20A9,
 to only have one bar.Removed Variation Selector glyphs (U+FE00..U+FE0F)
 from default OpenType and TrueType font builds;
 they remain in the sample and SBIT font builds.David CorbettModified Arabic glyphs U+0610, U+0616, U+061E,
 U+0620, and U+0626.Redrew the yeh-based glyphs in the ranges
 U+FC31..U+FDC7 (Arabic Presentation Forms-A) and
 U+FE89..U+FE8C (Arabic Presentation Forms-B).Johnnie Weavermodified some Georgian Supplement glyphs (U+2D00..U+2D2F).晓晓_Akatsuki (Xiao_Akatsuki)modified U+2EB2 per Unicode updates.
* Paul HardyModified the archaic Greek digamma glyphs,
 U+03DC and U+03DD.Modified the Korean Won currency symbol, U+20A9,
 to only have one bar.Removed Variation Selector glyphs (U+FE00..U+FE0F)
 from default OpenType and TrueType font builds;
 they remain in the sample and SBIT font builds.
* Modified the archaic Greek digamma glyphs,
 U+03DC and U+03DD.
* Modified the Korean Won currency symbol, U+20A9,
 to only have one bar.
* Removed Variation Selector glyphs (U+FE00..U+FE0F)
 from default OpenType and TrueType font builds;
 they remain in the sample and SBIT font builds.
* David CorbettModified Arabic glyphs U+0610, U+0616, U+061E,
 U+0620, and U+0626.Redrew the yeh-based glyphs in the ranges
 U+FC31..U+FDC7 (Arabic Presentation Forms-A) and
 U+FE89..U+FE8C (Arabic Presentation Forms-B).
* Modified Arabic glyphs U+0610, U+0616, U+061E,
 U+0620, and U+0626.
* Redrew the yeh-based glyphs in the ranges
 U+FC31..U+FDC7 (Arabic Presentation Forms-A) and
 U+FE89..U+FE8C (Arabic Presentation Forms-B).
* Johnnie Weavermodified some Georgian Supplement glyphs (U+2D00..U+2D2F).
* 晓晓_Akatsuki (Xiao_Akatsuki)modified U+2EB2 per Unicode updates.
* Plane 1:Paul HardyUpdated Old Turkic glyph U+10C47.Updated Khitan Small Script glyph U+18CCA.Reverted several changes in Musical Symbols
 (U+1D100..U+1D1FF) for better positioning with combining
 characters. Thanks go out to David Corbett for requesting
 the changes.Modified mathematical bold digamma (U+1D7CA, U+1D7CB)
 to match the updated digamma glyphs in Plane 0.Josh Huffordcontributed modified emoji glyphs
 U+1F602, U+1F605, U+1F606, U+1F607, U+1F609, U+1F923, and
 U+1FAE0.
* Paul HardyUpdated Old Turkic glyph U+10C47.Updated Khitan Small Script glyph U+18CCA.Reverted several changes in Musical Symbols
 (U+1D100..U+1D1FF) for better positioning with combining
 characters. Thanks go out to David Corbett for requesting
 the changes.Modified mathematical bold digamma (U+1D7CA, U+1D7CB)
 to match the updated digamma glyphs in Plane 0.
* Updated Old Turkic glyph U+10C47.
* Updated Khitan Small Script glyph U+18CCA.
* Reverted several changes in Musical Symbols
 (U+1D100..U+1D1FF) for better positioning with combining
 characters. Thanks go out to David Corbett for requesting
 the changes.
* Modified mathematical bold digamma (U+1D7CA, U+1D7CB)
 to match the updated digamma glyphs in Plane 0.
* Josh Huffordcontributed modified emoji glyphs
 U+1F602, U+1F605, U+1F606, U+1F607, U+1F609, U+1F923, and
 U+1FAE0.
* Plane 14:Paul HardyRemoved Variation Selector glyphs (U+E0100..U+E01EF)
 from default OpenType and TrueType font builds;
 they remain in the sample and SBIT font builds.
* Paul HardyRemoved Variation Selector glyphs (U+E0100..U+E01EF)
 from default OpenType and TrueType font builds;
 they remain in the sample and SBIT font builds.
* Plane 15 (CSUR/UCSUR):soweli Kape[sic] andNikZappUpdated Sitelen Pona (U+F1900..U+F19FF)Updated Sitelen Pona Radicals (U+F1C80..U+F1C9F).Paul HardyAdded Titi Pula (U+F1C40..UU+F1C60)Added Zbalermorna (U+F28A0..UU+F28DF).
* soweli Kape[sic] andNikZappUpdated Sitelen Pona (U+F1900..U+F19FF)Updated Sitelen Pona Radicals (U+F1C80..U+F1C9F).
* Updated Sitelen Pona (U+F1900..U+F19FF)
* Updated Sitelen Pona Radicals (U+F1C80..U+F1C9F).
* Paul HardyAdded Titi Pula (U+F1C40..UU+F1C60)Added Zbalermorna (U+F28A0..UU+F28DF).
* Added Titi Pula (U+F1C40..UU+F1C60)
* Added Zbalermorna (U+F28A0..UU+F28DF).
* 19 April 2025 (Unifont 16.0.03)Plane 0:David Corbettredrew some Arabic glyphs for consistency. Most of these
 are minor changes to baseline, i‘jam positioning, or making
 a derived letter match its origin letter. Code points:
 U+0625, U+0634, U+0673, U+06B9, U+06BC, U+0753, U+0754,
 U+0757, U+075C, U+0762, U+0767, U+0769, U+076A, U+076D,
 U+0770, U+0775, U+0776, U+0777, U+077D, U+077E, U+08A1,
 U+08A2, U+08A3, U+08A6, U+08A8, U+08B1, U+08BB, and U+08BC.晓晓_Akatsuki (Xiao_Akatsuki)submitted
 several CJK refinements from the team of湖 远星:Improved 褝 (U+891D) and 肞 (U+809E).Updated to reflect current Unicode rendering:
 㳽 (U+3CFD), 㸿 (U+3E3F), 䑮 (U+446E), 䒳 (U+44B3), 䕈 (U+4548),
 and 䩶 (U+4A76).Updated as per GB18030-2022 change: 垕 (U+5795).Modified to comply with the GB18030-2022 standard pertaining to
 character composition:姉 (U+59C9): This character is a phono-semantic character.
 Therefore, the right side should be "市" (U+5E02) instead
 of "巿" (U+5DFF).濲 (U+6FF2): This character is a variant of "瀔" (U+7014),
 and the "穀" (U+7A40) on the right side of "瀔" (U+7014) is
 a phono-semantic character, and its "semantic" part is "禾"
 (U+79BE), not "木" (U+6728).膥 (U+81A5): This character is a Cantonese character for "egg".
 Not yet (未) Become (成) Meat (肉) → Egg, so the upper left
 corner should be "未" (U+672A), not "末" (U+672B).David Corbett:Redrew some Arabic Presentation Forms:
 U+FD42, U+FD43, U+FD44, U+FD45, U+FDF0, U+FDF1, U+FDF4,
 U+FDF6, U+FDF7, U+FDFA, U+FDFB, U+FDFC, U+FE87, U+FE88,
 U+FEB5, and U+FEB6.Modified the top serifs of two Latin fullwidth letters, U+FF44 and U+FF4B.Plane 1:Paul Hardyadded new glyphs in Egyptian Hieroglyph Format Controls
 (U+13430..U+1345F).Paul HardyandDavid Corbettmade adjustments to
 glyphs in the Musical Symbols block (U+1D100..U+1D1FF).Plane 2:晓晓_Akatsukimodified U+25ED7 from 16 columns wide to 15 columns.Hayden Wongcontributed U+29B00..U+29CFF.Cod'dtesent a corrected left-hand side of U+2EE57.Plane 3:Luke036has drawn a much-improved glyph for taito (U+3106C).1 December 2024 (Unifont 16.0.02)Plane 0:Johnnie Weavermodified the
 U+13C9 Cherokee and U+AB99 Cherokee Supplement glyphs.湖 远星modified Chinese glyphs
 U+605C, U+6669, and U+6A37.Plane 1:Johnnie Weavermodified several glyphs in the
 ranges U+10880..U+108AF (Nabataean) and U+108E0..U+108FF
 (Hatran) so these scripts are now completely half-width.Paul Hardymodified several Tulu-Tilagari glyphs
 (U+11380..U+113FF), and modified the Kawi glyph U+11F5A
 to resemble U+11F49 (per David Corbett's recommendations).Xiao Akatsuki (晓晓 Akatsuki)fixed a missing
 vertical stroke in U+18B2D.湖 远星added more space between the two
 halves of U+1F232.Plane 2:Hayden Wongmade these changes:Modified U+20083, U+20087, U+20089, and
 U+200B4 from 16 columns wide to 15 columns.Added the missing glyphs in the range U+20000..U+299FF.Completed U+29D00..U+29DFF.Added U+2B64E, which is an incorrect variant
 of U+513A (儺).晓晓 Akatsukicontributed the missing glyphs
 in the range U+20700..U+207FF.湖 远星modified U+28A0F, U+28B4E, U+2CB5B,
 and U+2CB73 from 16 columns wide to 15 columns.Boris Zhangnoticed that U+2C7EC was the glyph
 for U+2CE7C, so it was removed.10 September 2024 (Unifont 16.0.01)Plane 0:David Corbettadded U+0897, ARABIC PEPET.Paul Hardyadded the new glyphs in
 Balinese (U+1B4E, U+1B4F, and U+1B7F),
 Cyrillic Extended-C (U+1C89, U+1C8A), and
 Latin Extended-D (U+A7CB..U+A7CD, U+A7DA..U+A7DC).Johnnie Weaver:Modified Cherokee glyphs U+13C9 and U+AB99.Changed these glyphs to half-width:
 U+210E, U+210F, U+212E, U+212F, U+2300, U+2329, U+232A, U+2610,
 U+2611, U+2612, U+2713, U+2717, U+A728, U+A729, U+A732, U+A733,
 U+A734, U+A735, U+A736, U+A737, U+A738, U+A739, U+A73A, U+A73B,
 U+A73C, U+A73D, U+A74E, U+A74F, U+A758, U+A759, U+A771, U+A772,
 U+A773, U+A774, U+A775, U+A776, U+A777, U+A797, U+A7C2, and U+A7C3.Boris Zhangdrew the Suzhou Numerals six through
 nine (U+3026..U+3029).Rebecca Bettencourtdrew the new Control Pictures
 glyphs, U+2427..U+2429.Yzy32767redrew the Bopomofo glyphs (U+3105..U+312F)
 in a Kai (楷) style.湖 远星contributed the new glyphs in CJK Strokes
 (U+31D2, U+31E4, and U+31E5).Hayden Wongmodified U+3862 per Unicode 15.1.0.Plane 0 CSUR/UCSUR:Rebecca Bettencourtcontributed:U+E400..U+E59F Herman Miller's previosuly missing scriptsU+E6D0..U+E6EF AmlinUnifon glyphs U+E6FD and U+E73D, previously missingU+EC70..U+ECEF Graflect.Danae Dekkercontributed:U+EC00..U+EC2F CylenianU+EC30..U+EC6F Syrrin.Plane 1:Johnnie Weavercontributed:U+105C0..U+105FF Todhri*U+10D40..U+10D8F Garay*U+11BC0..U+11BFF Sunuwar*U+16D40..U+16D7F Kirat Rai*Khitan Small Script (U+18BD2, U+18BFF)U+1E5D0..U+1E5FF Ol Onal.*David Corbettcontributed:Arabic Extended-C
 glyphs U+10EC2..U+10EC4, U+10EFC.U+16100..U+1613F Gurung Khema*Paul Hardycontributed:U+11380..U+113FF Tulu-Tigalari*U+116D0..U+116E3 Myanmar Extended-C*Kawi glyph U+11F5ASymbols and Pictographs Extended-A glyphs
 U+1FA89, U+1FA8F, U+1FABE, U+1FAC6, U+1FADC,
 U+1FADF, and U+1FAE9.Rebecca Bettencourtcontributed:U+1CC00..U+1CCF9 Symbols for Legacy Computing Supplement*Supplemental Arrows-C glyphs U+1F8B2..U+18BB,
 U+1F8C0, and U+1F8C1Symbols for Legacy Computing glyphs U+1FBCB..U+1FBEF.anonymous1redrew Enclosed Ideographic Supplement
 glyph U+1F200.Plane 2:Hayden Wongcontributed the new glyphs in
 CJK Unified Ideographs Extension B U+20020..U+2004F
 and U+29E00..2A0FF.twuchiutanncontributed the new glyphs in
 CJK Unified Ideographs Extension B U+20050..U+2073F.Boris Zhangredrew CJK Unified Ideographs
 Extension D glyphs U+2B75F, U+2B76B, and
 Extension I glyphs U+2B7EF, U+2EC1F, U+2EC20,
 U+2EC21, U+2EC2F, U+2EC6F, U+2ECBF, U+2ECEC, and U+2ED42.湖 远星contributed the following glyphs, which are common
 in Cantonese, Hokkien, Hakka,etc.,from a list provided
 with the Ichiten font.CJK Unified Ideographs Extension B glyphs:U+203B7 𠎷U+20546 𠕆U+20584 𠖄U+205FB 𠗻U+207A9 𠞩U+207AD 𠞭U+20803 𠠃U+2081D 𠠝U+20895 𠢕U+20BD7 𠯗U+20C41 𠱁U+20CBF 𠲿U+20CD4 𠳔U+20D5D 𠵝U+20D71 𠵱U+20DA7 𠶧U+20E76 𠹶U+20E98 𠺘U+20ED8 𠻘U+20F3B 𠼻U+20F7E 𠽾U+21014 𡀔U+210AB 𡂫U+210F6 𡃶U+21145 𡅅U+2176D 𡝭U+217D3 𡟓U+2180D 𡠍U+21883 𡢃U+2197C 𡥼U+21C2A 𡰪U+21CA2 𡲢U+21CDE 𡳞U+21DD1 𡷑U+21F0F 𡼏U+221A1 𢆡U+22399 𢎙U+224DC 𢓜U+2251B 𢔛U+22775 𢝵U+22AB1 𢪱U+22AE6 𢫦U+22BED 𢯭U+22BFE 𢯾U+22C4B 𢱋U+22C62 𢱢U+22C64 𢱤U+22CB4 𢲴U+22CB8 𢲸U+22CC6 𢳆U+22CEA 𢳪U+22D80 𢶀U+22F0C 𢼌U+22F1B 𢼛U+23073 𣁳U+23074 𣁴U+23350 𣍐U+236BA 𣚺U+236EE 𣛮U+23B88 𣮈U+23CA9 𣲩U+23EF8 𣻸U+23F0E 𣼎U+240D2 𤃒U+241AC 𤆬U+24259 𤉙U+242B6 𤊶U+2430D 𤌍U+24352 𤍒U+24364 𤍤U+24419 𤐙U+24430 𤐰U+24605 𤘅U+2479A 𤞚U+24C8D 𤲍U+24D80 𤶀U+24D83 𤶃U+24E01 𤸁U+24E31 𤸱U+24E85 𤺅U+24EA7 𤺧U+24EAA 𤺪U+25148 𥅈U+2517E 𥅾U+2531A 𥌚U+25349 𥍉U+25435 𥐵U+2546E 𥑮U+257C7 𥟇U+25BDF 𥯟U+25BE5 𥯥U+25C14 𥰔U+25D0A 𥴊U+25E86 𥺆U+2624E 𦉎U+26293 𦊓U+26706 𦜆U+267EA 𦟪U+2688A 𦢊U+2690E 𦤎U+26E05 𦸅U+2725F 𧉟U+27304 𧌄U+27371 𧍱U+27486 𧒆U+277F0 𧟰U+279A0 𧦠U+27A63 𧩣U+27B2A 𧬪U+27B99 𧮙U+27EF4 𧻴U+27FC1 𧿁U+27FEC 𧿬U+27FF3 𧿳U+280BE 𨂾U+280BF 𨂿U+280E9 𨃩U+280F0 𨃰U+28154 𨅔U+282CD 𨋍U+2837D 𨍽U+2838A 𨎊U+28487 𨒇U+28595 𨖕U+28891 𨢑U+28D99 𨶙U+28E39 𨸹U+2945D 𩑝U+2947E 𩑾U+294E5 𩓥U+296A8 𩚨U+296E9 𩛩U+29704 𩜄U+29730 𩜰U+29D71 𩵱U+29DD3 𩷓U+29E19 𩸙U+29E36 𩸶U+29EAC 𩺬U+29F27 𩼧U+29F30 𩼰U+29F48 𩽈U+29F70 𩽰U+2A04E 𪁎U+2A0BA 𪂺U+2A1E1 𪇡U+2A41E 𪐞U+2A590 𪖐U+2A612 𪘒U+2A64A 𪙊CJK Unified Ideographs Extension C glyphs:U+2A736 𪜶, U+2AE5A 𪹚, and U+2B4A2 𫒢CJK Unified Ideographs Extension E glyphs:U+2B8C6 𫣆, U+2C816 𬠖, and U+2C9B0 𬦰.Plane 3:twuchiutannmodified U+30EDD and U+30EDE (biang),
	 originally drawn by Ming Fan, to differentiate between
	 traditional and simplified Chinese versions.湖 远星contributed the following glyphs, which are common in
 Cantonese, Hokkien, Hakka,etc.,from a list given in the
 Ichiten font.CJK Unified Ideographs Extension G glyphs:U+301DB 𰇛, U+308FB 𰣻, and U+30E6C 𰹬CJK Unified Ideographs Extension H glyph:U+31C7F 𱱿.Plane 15 CSUR/UCSUR:Rebecca Bettencourtcontributed:U+F16B0..U+F16DF DeraniU+F2000..U+F267F Sadalian.Paul Hardycontributed
 U+F1C80..U+F1C9C Sitelen Pona Radicals.*New in Unicode 16.0.0.
* Plane 0:David Corbettredrew some Arabic glyphs for consistency. Most of these
 are minor changes to baseline, i‘jam positioning, or making
 a derived letter match its origin letter. Code points:
 U+0625, U+0634, U+0673, U+06B9, U+06BC, U+0753, U+0754,
 U+0757, U+075C, U+0762, U+0767, U+0769, U+076A, U+076D,
 U+0770, U+0775, U+0776, U+0777, U+077D, U+077E, U+08A1,
 U+08A2, U+08A3, U+08A6, U+08A8, U+08B1, U+08BB, and U+08BC.晓晓_Akatsuki (Xiao_Akatsuki)submitted
 several CJK refinements from the team of湖 远星:Improved 褝 (U+891D) and 肞 (U+809E).Updated to reflect current Unicode rendering:
 㳽 (U+3CFD), 㸿 (U+3E3F), 䑮 (U+446E), 䒳 (U+44B3), 䕈 (U+4548),
 and 䩶 (U+4A76).Updated as per GB18030-2022 change: 垕 (U+5795).Modified to comply with the GB18030-2022 standard pertaining to
 character composition:姉 (U+59C9): This character is a phono-semantic character.
 Therefore, the right side should be "市" (U+5E02) instead
 of "巿" (U+5DFF).濲 (U+6FF2): This character is a variant of "瀔" (U+7014),
 and the "穀" (U+7A40) on the right side of "瀔" (U+7014) is
 a phono-semantic character, and its "semantic" part is "禾"
 (U+79BE), not "木" (U+6728).膥 (U+81A5): This character is a Cantonese character for "egg".
 Not yet (未) Become (成) Meat (肉) → Egg, so the upper left
 corner should be "未" (U+672A), not "末" (U+672B).David Corbett:Redrew some Arabic Presentation Forms:
 U+FD42, U+FD43, U+FD44, U+FD45, U+FDF0, U+FDF1, U+FDF4,
 U+FDF6, U+FDF7, U+FDFA, U+FDFB, U+FDFC, U+FE87, U+FE88,
 U+FEB5, and U+FEB6.Modified the top serifs of two Latin fullwidth letters, U+FF44 and U+FF4B.Plane 1:Paul Hardyadded new glyphs in Egyptian Hieroglyph Format Controls
 (U+13430..U+1345F).Paul HardyandDavid Corbettmade adjustments to
 glyphs in the Musical Symbols block (U+1D100..U+1D1FF).Plane 2:晓晓_Akatsukimodified U+25ED7 from 16 columns wide to 15 columns.Hayden Wongcontributed U+29B00..U+29CFF.Cod'dtesent a corrected left-hand side of U+2EE57.Plane 3:Luke036has drawn a much-improved glyph for taito (U+3106C).
* David Corbettredrew some Arabic glyphs for consistency. Most of these
 are minor changes to baseline, i‘jam positioning, or making
 a derived letter match its origin letter. Code points:
 U+0625, U+0634, U+0673, U+06B9, U+06BC, U+0753, U+0754,
 U+0757, U+075C, U+0762, U+0767, U+0769, U+076A, U+076D,
 U+0770, U+0775, U+0776, U+0777, U+077D, U+077E, U+08A1,
 U+08A2, U+08A3, U+08A6, U+08A8, U+08B1, U+08BB, and U+08BC.
* 晓晓_Akatsuki (Xiao_Akatsuki)submitted
 several CJK refinements from the team of湖 远星:Improved 褝 (U+891D) and 肞 (U+809E).Updated to reflect current Unicode rendering:
 㳽 (U+3CFD), 㸿 (U+3E3F), 䑮 (U+446E), 䒳 (U+44B3), 䕈 (U+4548),
 and 䩶 (U+4A76).Updated as per GB18030-2022 change: 垕 (U+5795).Modified to comply with the GB18030-2022 standard pertaining to
 character composition:姉 (U+59C9): This character is a phono-semantic character.
 Therefore, the right side should be "市" (U+5E02) instead
 of "巿" (U+5DFF).濲 (U+6FF2): This character is a variant of "瀔" (U+7014),
 and the "穀" (U+7A40) on the right side of "瀔" (U+7014) is
 a phono-semantic character, and its "semantic" part is "禾"
 (U+79BE), not "木" (U+6728).膥 (U+81A5): This character is a Cantonese character for "egg".
 Not yet (未) Become (成) Meat (肉) → Egg, so the upper left
 corner should be "未" (U+672A), not "末" (U+672B).
* Improved 褝 (U+891D) and 肞 (U+809E).
* Updated to reflect current Unicode rendering:
 㳽 (U+3CFD), 㸿 (U+3E3F), 䑮 (U+446E), 䒳 (U+44B3), 䕈 (U+4548),
 and 䩶 (U+4A76).
* Updated as per GB18030-2022 change: 垕 (U+5795).
* Modified to comply with the GB18030-2022 standard pertaining to
 character composition:姉 (U+59C9): This character is a phono-semantic character.
 Therefore, the right side should be "市" (U+5E02) instead
 of "巿" (U+5DFF).濲 (U+6FF2): This character is a variant of "瀔" (U+7014),
 and the "穀" (U+7A40) on the right side of "瀔" (U+7014) is
 a phono-semantic character, and its "semantic" part is "禾"
 (U+79BE), not "木" (U+6728).膥 (U+81A5): This character is a Cantonese character for "egg".
 Not yet (未) Become (成) Meat (肉) → Egg, so the upper left
 corner should be "未" (U+672A), not "末" (U+672B).
* 姉 (U+59C9): This character is a phono-semantic character.
 Therefore, the right side should be "市" (U+5E02) instead
 of "巿" (U+5DFF).
* 濲 (U+6FF2): This character is a variant of "瀔" (U+7014),
 and the "穀" (U+7A40) on the right side of "瀔" (U+7014) is
 a phono-semantic character, and its "semantic" part is "禾"
 (U+79BE), not "木" (U+6728).
* 膥 (U+81A5): This character is a Cantonese character for "egg".
 Not yet (未) Become (成) Meat (肉) → Egg, so the upper left
 corner should be "未" (U+672A), not "末" (U+672B).
* David Corbett:Redrew some Arabic Presentation Forms:
 U+FD42, U+FD43, U+FD44, U+FD45, U+FDF0, U+FDF1, U+FDF4,
 U+FDF6, U+FDF7, U+FDFA, U+FDFB, U+FDFC, U+FE87, U+FE88,
 U+FEB5, and U+FEB6.Modified the top serifs of two Latin fullwidth letters, U+FF44 and U+FF4B.
* Redrew some Arabic Presentation Forms:
 U+FD42, U+FD43, U+FD44, U+FD45, U+FDF0, U+FDF1, U+FDF4,
 U+FDF6, U+FDF7, U+FDFA, U+FDFB, U+FDFC, U+FE87, U+FE88,
 U+FEB5, and U+FEB6.
* Modified the top serifs of two Latin fullwidth letters, U+FF44 and U+FF4B.
* Paul Hardyadded new glyphs in Egyptian Hieroglyph Format Controls
 (U+13430..U+1345F).
* Paul HardyandDavid Corbettmade adjustments to
 glyphs in the Musical Symbols block (U+1D100..U+1D1FF).
* 晓晓_Akatsukimodified U+25ED7 from 16 columns wide to 15 columns.
* Hayden Wongcontributed U+29B00..U+29CFF.
* Cod'dtesent a corrected left-hand side of U+2EE57.
* Luke036has drawn a much-improved glyph for taito (U+3106C).
* 1 December 2024 (Unifont 16.0.02)Plane 0:Johnnie Weavermodified the
 U+13C9 Cherokee and U+AB99 Cherokee Supplement glyphs.湖 远星modified Chinese glyphs
 U+605C, U+6669, and U+6A37.Plane 1:Johnnie Weavermodified several glyphs in the
 ranges U+10880..U+108AF (Nabataean) and U+108E0..U+108FF
 (Hatran) so these scripts are now completely half-width.Paul Hardymodified several Tulu-Tilagari glyphs
 (U+11380..U+113FF), and modified the Kawi glyph U+11F5A
 to resemble U+11F49 (per David Corbett's recommendations).Xiao Akatsuki (晓晓 Akatsuki)fixed a missing
 vertical stroke in U+18B2D.湖 远星added more space between the two
 halves of U+1F232.Plane 2:Hayden Wongmade these changes:Modified U+20083, U+20087, U+20089, and
 U+200B4 from 16 columns wide to 15 columns.Added the missing glyphs in the range U+20000..U+299FF.Completed U+29D00..U+29DFF.Added U+2B64E, which is an incorrect variant
 of U+513A (儺).晓晓 Akatsukicontributed the missing glyphs
 in the range U+20700..U+207FF.湖 远星modified U+28A0F, U+28B4E, U+2CB5B,
 and U+2CB73 from 16 columns wide to 15 columns.Boris Zhangnoticed that U+2C7EC was the glyph
 for U+2CE7C, so it was removed.
* Plane 0:Johnnie Weavermodified the
 U+13C9 Cherokee and U+AB99 Cherokee Supplement glyphs.湖 远星modified Chinese glyphs
 U+605C, U+6669, and U+6A37.
* Johnnie Weavermodified the
 U+13C9 Cherokee and U+AB99 Cherokee Supplement glyphs.
* 湖 远星modified Chinese glyphs
 U+605C, U+6669, and U+6A37.
* Plane 1:Johnnie Weavermodified several glyphs in the
 ranges U+10880..U+108AF (Nabataean) and U+108E0..U+108FF
 (Hatran) so these scripts are now completely half-width.Paul Hardymodified several Tulu-Tilagari glyphs
 (U+11380..U+113FF), and modified the Kawi glyph U+11F5A
 to resemble U+11F49 (per David Corbett's recommendations).Xiao Akatsuki (晓晓 Akatsuki)fixed a missing
 vertical stroke in U+18B2D.湖 远星added more space between the two
 halves of U+1F232.
* Johnnie Weavermodified several glyphs in the
 ranges U+10880..U+108AF (Nabataean) and U+108E0..U+108FF
 (Hatran) so these scripts are now completely half-width.
* Paul Hardymodified several Tulu-Tilagari glyphs
 (U+11380..U+113FF), and modified the Kawi glyph U+11F5A
 to resemble U+11F49 (per David Corbett's recommendations).
* Xiao Akatsuki (晓晓 Akatsuki)fixed a missing
 vertical stroke in U+18B2D.
* 湖 远星added more space between the two
 halves of U+1F232.
* Plane 2:Hayden Wongmade these changes:Modified U+20083, U+20087, U+20089, and
 U+200B4 from 16 columns wide to 15 columns.Added the missing glyphs in the range U+20000..U+299FF.Completed U+29D00..U+29DFF.Added U+2B64E, which is an incorrect variant
 of U+513A (儺).晓晓 Akatsukicontributed the missing glyphs
 in the range U+20700..U+207FF.湖 远星modified U+28A0F, U+28B4E, U+2CB5B,
 and U+2CB73 from 16 columns wide to 15 columns.Boris Zhangnoticed that U+2C7EC was the glyph
 for U+2CE7C, so it was removed.
* Hayden Wongmade these changes:Modified U+20083, U+20087, U+20089, and
 U+200B4 from 16 columns wide to 15 columns.Added the missing glyphs in the range U+20000..U+299FF.Completed U+29D00..U+29DFF.Added U+2B64E, which is an incorrect variant
 of U+513A (儺).
* Modified U+20083, U+20087, U+20089, and
 U+200B4 from 16 columns wide to 15 columns.
* Added the missing glyphs in the range U+20000..U+299FF.
* Completed U+29D00..U+29DFF.
* Added U+2B64E, which is an incorrect variant
 of U+513A (儺).
* 晓晓 Akatsukicontributed the missing glyphs
 in the range U+20700..U+207FF.
* 湖 远星modified U+28A0F, U+28B4E, U+2CB5B,
 and U+2CB73 from 16 columns wide to 15 columns.
* Boris Zhangnoticed that U+2C7EC was the glyph
 for U+2CE7C, so it was removed.
* 10 September 2024 (Unifont 16.0.01)Plane 0:David Corbettadded U+0897, ARABIC PEPET.Paul Hardyadded the new glyphs in
 Balinese (U+1B4E, U+1B4F, and U+1B7F),
 Cyrillic Extended-C (U+1C89, U+1C8A), and
 Latin Extended-D (U+A7CB..U+A7CD, U+A7DA..U+A7DC).Johnnie Weaver:Modified Cherokee glyphs U+13C9 and U+AB99.Changed these glyphs to half-width:
 U+210E, U+210F, U+212E, U+212F, U+2300, U+2329, U+232A, U+2610,
 U+2611, U+2612, U+2713, U+2717, U+A728, U+A729, U+A732, U+A733,
 U+A734, U+A735, U+A736, U+A737, U+A738, U+A739, U+A73A, U+A73B,
 U+A73C, U+A73D, U+A74E, U+A74F, U+A758, U+A759, U+A771, U+A772,
 U+A773, U+A774, U+A775, U+A776, U+A777, U+A797, U+A7C2, and U+A7C3.Boris Zhangdrew the Suzhou Numerals six through
 nine (U+3026..U+3029).Rebecca Bettencourtdrew the new Control Pictures
 glyphs, U+2427..U+2429.Yzy32767redrew the Bopomofo glyphs (U+3105..U+312F)
 in a Kai (楷) style.湖 远星contributed the new glyphs in CJK Strokes
 (U+31D2, U+31E4, and U+31E5).Hayden Wongmodified U+3862 per Unicode 15.1.0.Plane 0 CSUR/UCSUR:Rebecca Bettencourtcontributed:U+E400..U+E59F Herman Miller's previosuly missing scriptsU+E6D0..U+E6EF AmlinUnifon glyphs U+E6FD and U+E73D, previously missingU+EC70..U+ECEF Graflect.Danae Dekkercontributed:U+EC00..U+EC2F CylenianU+EC30..U+EC6F Syrrin.Plane 1:Johnnie Weavercontributed:U+105C0..U+105FF Todhri*U+10D40..U+10D8F Garay*U+11BC0..U+11BFF Sunuwar*U+16D40..U+16D7F Kirat Rai*Khitan Small Script (U+18BD2, U+18BFF)U+1E5D0..U+1E5FF Ol Onal.*David Corbettcontributed:Arabic Extended-C
 glyphs U+10EC2..U+10EC4, U+10EFC.U+16100..U+1613F Gurung Khema*Paul Hardycontributed:U+11380..U+113FF Tulu-Tigalari*U+116D0..U+116E3 Myanmar Extended-C*Kawi glyph U+11F5ASymbols and Pictographs Extended-A glyphs
 U+1FA89, U+1FA8F, U+1FABE, U+1FAC6, U+1FADC,
 U+1FADF, and U+1FAE9.Rebecca Bettencourtcontributed:U+1CC00..U+1CCF9 Symbols for Legacy Computing Supplement*Supplemental Arrows-C glyphs U+1F8B2..U+18BB,
 U+1F8C0, and U+1F8C1Symbols for Legacy Computing glyphs U+1FBCB..U+1FBEF.anonymous1redrew Enclosed Ideographic Supplement
 glyph U+1F200.Plane 2:Hayden Wongcontributed the new glyphs in
 CJK Unified Ideographs Extension B U+20020..U+2004F
 and U+29E00..2A0FF.twuchiutanncontributed the new glyphs in
 CJK Unified Ideographs Extension B U+20050..U+2073F.Boris Zhangredrew CJK Unified Ideographs
 Extension D glyphs U+2B75F, U+2B76B, and
 Extension I glyphs U+2B7EF, U+2EC1F, U+2EC20,
 U+2EC21, U+2EC2F, U+2EC6F, U+2ECBF, U+2ECEC, and U+2ED42.湖 远星contributed the following glyphs, which are common
 in Cantonese, Hokkien, Hakka,etc.,from a list provided
 with the Ichiten font.CJK Unified Ideographs Extension B glyphs:U+203B7 𠎷U+20546 𠕆U+20584 𠖄U+205FB 𠗻U+207A9 𠞩U+207AD 𠞭U+20803 𠠃U+2081D 𠠝U+20895 𠢕U+20BD7 𠯗U+20C41 𠱁U+20CBF 𠲿U+20CD4 𠳔U+20D5D 𠵝U+20D71 𠵱U+20DA7 𠶧U+20E76 𠹶U+20E98 𠺘U+20ED8 𠻘U+20F3B 𠼻U+20F7E 𠽾U+21014 𡀔U+210AB 𡂫U+210F6 𡃶U+21145 𡅅U+2176D 𡝭U+217D3 𡟓U+2180D 𡠍U+21883 𡢃U+2197C 𡥼U+21C2A 𡰪U+21CA2 𡲢U+21CDE 𡳞U+21DD1 𡷑U+21F0F 𡼏U+221A1 𢆡U+22399 𢎙U+224DC 𢓜U+2251B 𢔛U+22775 𢝵U+22AB1 𢪱U+22AE6 𢫦U+22BED 𢯭U+22BFE 𢯾U+22C4B 𢱋U+22C62 𢱢U+22C64 𢱤U+22CB4 𢲴U+22CB8 𢲸U+22CC6 𢳆U+22CEA 𢳪U+22D80 𢶀U+22F0C 𢼌U+22F1B 𢼛U+23073 𣁳U+23074 𣁴U+23350 𣍐U+236BA 𣚺U+236EE 𣛮U+23B88 𣮈U+23CA9 𣲩U+23EF8 𣻸U+23F0E 𣼎U+240D2 𤃒U+241AC 𤆬U+24259 𤉙U+242B6 𤊶U+2430D 𤌍U+24352 𤍒U+24364 𤍤U+24419 𤐙U+24430 𤐰U+24605 𤘅U+2479A 𤞚U+24C8D 𤲍U+24D80 𤶀U+24D83 𤶃U+24E01 𤸁U+24E31 𤸱U+24E85 𤺅U+24EA7 𤺧U+24EAA 𤺪U+25148 𥅈U+2517E 𥅾U+2531A 𥌚U+25349 𥍉U+25435 𥐵U+2546E 𥑮U+257C7 𥟇U+25BDF 𥯟U+25BE5 𥯥U+25C14 𥰔U+25D0A 𥴊U+25E86 𥺆U+2624E 𦉎U+26293 𦊓U+26706 𦜆U+267EA 𦟪U+2688A 𦢊U+2690E 𦤎U+26E05 𦸅U+2725F 𧉟U+27304 𧌄U+27371 𧍱U+27486 𧒆U+277F0 𧟰U+279A0 𧦠U+27A63 𧩣U+27B2A 𧬪U+27B99 𧮙U+27EF4 𧻴U+27FC1 𧿁U+27FEC 𧿬U+27FF3 𧿳U+280BE 𨂾U+280BF 𨂿U+280E9 𨃩U+280F0 𨃰U+28154 𨅔U+282CD 𨋍U+2837D 𨍽U+2838A 𨎊U+28487 𨒇U+28595 𨖕U+28891 𨢑U+28D99 𨶙U+28E39 𨸹U+2945D 𩑝U+2947E 𩑾U+294E5 𩓥U+296A8 𩚨U+296E9 𩛩U+29704 𩜄U+29730 𩜰U+29D71 𩵱U+29DD3 𩷓U+29E19 𩸙U+29E36 𩸶U+29EAC 𩺬U+29F27 𩼧U+29F30 𩼰U+29F48 𩽈U+29F70 𩽰U+2A04E 𪁎U+2A0BA 𪂺U+2A1E1 𪇡U+2A41E 𪐞U+2A590 𪖐U+2A612 𪘒U+2A64A 𪙊CJK Unified Ideographs Extension C glyphs:U+2A736 𪜶, U+2AE5A 𪹚, and U+2B4A2 𫒢CJK Unified Ideographs Extension E glyphs:U+2B8C6 𫣆, U+2C816 𬠖, and U+2C9B0 𬦰.Plane 3:twuchiutannmodified U+30EDD and U+30EDE (biang),
	 originally drawn by Ming Fan, to differentiate between
	 traditional and simplified Chinese versions.湖 远星contributed the following glyphs, which are common in
 Cantonese, Hokkien, Hakka,etc.,from a list given in the
 Ichiten font.CJK Unified Ideographs Extension G glyphs:U+301DB 𰇛, U+308FB 𰣻, and U+30E6C 𰹬CJK Unified Ideographs Extension H glyph:U+31C7F 𱱿.Plane 15 CSUR/UCSUR:Rebecca Bettencourtcontributed:U+F16B0..U+F16DF DeraniU+F2000..U+F267F Sadalian.Paul Hardycontributed
 U+F1C80..U+F1C9C Sitelen Pona Radicals.*New in Unicode 16.0.0.
* Plane 0:David Corbettadded U+0897, ARABIC PEPET.Paul Hardyadded the new glyphs in
 Balinese (U+1B4E, U+1B4F, and U+1B7F),
 Cyrillic Extended-C (U+1C89, U+1C8A), and
 Latin Extended-D (U+A7CB..U+A7CD, U+A7DA..U+A7DC).Johnnie Weaver:Modified Cherokee glyphs U+13C9 and U+AB99.Changed these glyphs to half-width:
 U+210E, U+210F, U+212E, U+212F, U+2300, U+2329, U+232A, U+2610,
 U+2611, U+2612, U+2713, U+2717, U+A728, U+A729, U+A732, U+A733,
 U+A734, U+A735, U+A736, U+A737, U+A738, U+A739, U+A73A, U+A73B,
 U+A73C, U+A73D, U+A74E, U+A74F, U+A758, U+A759, U+A771, U+A772,
 U+A773, U+A774, U+A775, U+A776, U+A777, U+A797, U+A7C2, and U+A7C3.Boris Zhangdrew the Suzhou Numerals six through
 nine (U+3026..U+3029).Rebecca Bettencourtdrew the new Control Pictures
 glyphs, U+2427..U+2429.Yzy32767redrew the Bopomofo glyphs (U+3105..U+312F)
 in a Kai (楷) style.湖 远星contributed the new glyphs in CJK Strokes
 (U+31D2, U+31E4, and U+31E5).Hayden Wongmodified U+3862 per Unicode 15.1.0.
* David Corbettadded U+0897, ARABIC PEPET.
* Paul Hardyadded the new glyphs in
 Balinese (U+1B4E, U+1B4F, and U+1B7F),
 Cyrillic Extended-C (U+1C89, U+1C8A), and
 Latin Extended-D (U+A7CB..U+A7CD, U+A7DA..U+A7DC).
* Johnnie Weaver:Modified Cherokee glyphs U+13C9 and U+AB99.Changed these glyphs to half-width:
 U+210E, U+210F, U+212E, U+212F, U+2300, U+2329, U+232A, U+2610,
 U+2611, U+2612, U+2713, U+2717, U+A728, U+A729, U+A732, U+A733,
 U+A734, U+A735, U+A736, U+A737, U+A738, U+A739, U+A73A, U+A73B,
 U+A73C, U+A73D, U+A74E, U+A74F, U+A758, U+A759, U+A771, U+A772,
 U+A773, U+A774, U+A775, U+A776, U+A777, U+A797, U+A7C2, and U+A7C3.
* Modified Cherokee glyphs U+13C9 and U+AB99.
* Changed these glyphs to half-width:
 U+210E, U+210F, U+212E, U+212F, U+2300, U+2329, U+232A, U+2610,
 U+2611, U+2612, U+2713, U+2717, U+A728, U+A729, U+A732, U+A733,
 U+A734, U+A735, U+A736, U+A737, U+A738, U+A739, U+A73A, U+A73B,
 U+A73C, U+A73D, U+A74E, U+A74F, U+A758, U+A759, U+A771, U+A772,
 U+A773, U+A774, U+A775, U+A776, U+A777, U+A797, U+A7C2, and U+A7C3.
* Boris Zhangdrew the Suzhou Numerals six through
 nine (U+3026..U+3029).Rebecca Bettencourtdrew the new Control Pictures
 glyphs, U+2427..U+2429.Yzy32767redrew the Bopomofo glyphs (U+3105..U+312F)
 in a Kai (楷) style.湖 远星contributed the new glyphs in CJK Strokes
 (U+31D2, U+31E4, and U+31E5).Hayden Wongmodified U+3862 per Unicode 15.1.0.
* Rebecca Bettencourtdrew the new Control Pictures
 glyphs, U+2427..U+2429.
* Yzy32767redrew the Bopomofo glyphs (U+3105..U+312F)
 in a Kai (楷) style.湖 远星contributed the new glyphs in CJK Strokes
 (U+31D2, U+31E4, and U+31E5).Hayden Wongmodified U+3862 per Unicode 15.1.0.
* 湖 远星contributed the new glyphs in CJK Strokes
 (U+31D2, U+31E4, and U+31E5).
* Hayden Wongmodified U+3862 per Unicode 15.1.0.
* Plane 0 CSUR/UCSUR:Rebecca Bettencourtcontributed:U+E400..U+E59F Herman Miller's previosuly missing scriptsU+E6D0..U+E6EF AmlinUnifon glyphs U+E6FD and U+E73D, previously missingU+EC70..U+ECEF Graflect.Danae Dekkercontributed:U+EC00..U+EC2F CylenianU+EC30..U+EC6F Syrrin.
* Rebecca Bettencourtcontributed:U+E400..U+E59F Herman Miller's previosuly missing scriptsU+E6D0..U+E6EF AmlinUnifon glyphs U+E6FD and U+E73D, previously missingU+EC70..U+ECEF Graflect.
* U+E400..U+E59F Herman Miller's previosuly missing scripts
* U+E6D0..U+E6EF Amlin
* Unifon glyphs U+E6FD and U+E73D, previously missing
* U+EC70..U+ECEF Graflect.
* Danae Dekkercontributed:U+EC00..U+EC2F CylenianU+EC30..U+EC6F Syrrin.
* U+EC00..U+EC2F Cylenian
* U+EC30..U+EC6F Syrrin.
* Plane 1:Johnnie Weavercontributed:U+105C0..U+105FF Todhri*U+10D40..U+10D8F Garay*U+11BC0..U+11BFF Sunuwar*U+16D40..U+16D7F Kirat Rai*Khitan Small Script (U+18BD2, U+18BFF)U+1E5D0..U+1E5FF Ol Onal.*David Corbettcontributed:Arabic Extended-C
 glyphs U+10EC2..U+10EC4, U+10EFC.U+16100..U+1613F Gurung Khema*Paul Hardycontributed:U+11380..U+113FF Tulu-Tigalari*U+116D0..U+116E3 Myanmar Extended-C*Kawi glyph U+11F5ASymbols and Pictographs Extended-A glyphs
 U+1FA89, U+1FA8F, U+1FABE, U+1FAC6, U+1FADC,
 U+1FADF, and U+1FAE9.Rebecca Bettencourtcontributed:U+1CC00..U+1CCF9 Symbols for Legacy Computing Supplement*Supplemental Arrows-C glyphs U+1F8B2..U+18BB,
 U+1F8C0, and U+1F8C1Symbols for Legacy Computing glyphs U+1FBCB..U+1FBEF.anonymous1redrew Enclosed Ideographic Supplement
 glyph U+1F200.
* Johnnie Weavercontributed:U+105C0..U+105FF Todhri*U+10D40..U+10D8F Garay*U+11BC0..U+11BFF Sunuwar*U+16D40..U+16D7F Kirat Rai*Khitan Small Script (U+18BD2, U+18BFF)U+1E5D0..U+1E5FF Ol Onal.*
* U+105C0..U+105FF Todhri*
* U+10D40..U+10D8F Garay*
* U+11BC0..U+11BFF Sunuwar*
* U+16D40..U+16D7F Kirat Rai*
* Khitan Small Script (U+18BD2, U+18BFF)
* U+1E5D0..U+1E5FF Ol Onal.*
* David Corbettcontributed:Arabic Extended-C
 glyphs U+10EC2..U+10EC4, U+10EFC.U+16100..U+1613F Gurung Khema*
* Arabic Extended-C
 glyphs U+10EC2..U+10EC4, U+10EFC.
* U+16100..U+1613F Gurung Khema*
* Paul Hardycontributed:U+11380..U+113FF Tulu-Tigalari*U+116D0..U+116E3 Myanmar Extended-C*Kawi glyph U+11F5ASymbols and Pictographs Extended-A glyphs
 U+1FA89, U+1FA8F, U+1FABE, U+1FAC6, U+1FADC,
 U+1FADF, and U+1FAE9.
* U+11380..U+113FF Tulu-Tigalari*
* U+116D0..U+116E3 Myanmar Extended-C*
* Kawi glyph U+11F5A
* Symbols and Pictographs Extended-A glyphs
 U+1FA89, U+1FA8F, U+1FABE, U+1FAC6, U+1FADC,
 U+1FADF, and U+1FAE9.
* Rebecca Bettencourtcontributed:U+1CC00..U+1CCF9 Symbols for Legacy Computing Supplement*Supplemental Arrows-C glyphs U+1F8B2..U+18BB,
 U+1F8C0, and U+1F8C1Symbols for Legacy Computing glyphs U+1FBCB..U+1FBEF.
* U+1CC00..U+1CCF9 Symbols for Legacy Computing Supplement*
* Supplemental Arrows-C glyphs U+1F8B2..U+18BB,
 U+1F8C0, and U+1F8C1
* Symbols for Legacy Computing glyphs U+1FBCB..U+1FBEF.
* anonymous1redrew Enclosed Ideographic Supplement
 glyph U+1F200.
* Plane 2:Hayden Wongcontributed the new glyphs in
 CJK Unified Ideographs Extension B U+20020..U+2004F
 and U+29E00..2A0FF.twuchiutanncontributed the new glyphs in
 CJK Unified Ideographs Extension B U+20050..U+2073F.Boris Zhangredrew CJK Unified Ideographs
 Extension D glyphs U+2B75F, U+2B76B, and
 Extension I glyphs U+2B7EF, U+2EC1F, U+2EC20,
 U+2EC21, U+2EC2F, U+2EC6F, U+2ECBF, U+2ECEC, and U+2ED42.湖 远星contributed the following glyphs, which are common
 in Cantonese, Hokkien, Hakka,etc.,from a list provided
 with the Ichiten font.CJK Unified Ideographs Extension B glyphs:U+203B7 𠎷U+20546 𠕆U+20584 𠖄U+205FB 𠗻U+207A9 𠞩U+207AD 𠞭U+20803 𠠃U+2081D 𠠝U+20895 𠢕U+20BD7 𠯗U+20C41 𠱁U+20CBF 𠲿U+20CD4 𠳔U+20D5D 𠵝U+20D71 𠵱U+20DA7 𠶧U+20E76 𠹶U+20E98 𠺘U+20ED8 𠻘U+20F3B 𠼻U+20F7E 𠽾U+21014 𡀔U+210AB 𡂫U+210F6 𡃶U+21145 𡅅U+2176D 𡝭U+217D3 𡟓U+2180D 𡠍U+21883 𡢃U+2197C 𡥼U+21C2A 𡰪U+21CA2 𡲢U+21CDE 𡳞U+21DD1 𡷑U+21F0F 𡼏U+221A1 𢆡U+22399 𢎙U+224DC 𢓜U+2251B 𢔛U+22775 𢝵U+22AB1 𢪱U+22AE6 𢫦U+22BED 𢯭U+22BFE 𢯾U+22C4B 𢱋U+22C62 𢱢U+22C64 𢱤U+22CB4 𢲴U+22CB8 𢲸U+22CC6 𢳆U+22CEA 𢳪U+22D80 𢶀U+22F0C 𢼌U+22F1B 𢼛U+23073 𣁳U+23074 𣁴U+23350 𣍐U+236BA 𣚺U+236EE 𣛮U+23B88 𣮈U+23CA9 𣲩U+23EF8 𣻸U+23F0E 𣼎U+240D2 𤃒U+241AC 𤆬U+24259 𤉙U+242B6 𤊶U+2430D 𤌍U+24352 𤍒U+24364 𤍤U+24419 𤐙U+24430 𤐰U+24605 𤘅U+2479A 𤞚U+24C8D 𤲍U+24D80 𤶀U+24D83 𤶃U+24E01 𤸁U+24E31 𤸱U+24E85 𤺅U+24EA7 𤺧U+24EAA 𤺪U+25148 𥅈U+2517E 𥅾U+2531A 𥌚U+25349 𥍉U+25435 𥐵U+2546E 𥑮U+257C7 𥟇U+25BDF 𥯟U+25BE5 𥯥U+25C14 𥰔U+25D0A 𥴊U+25E86 𥺆U+2624E 𦉎U+26293 𦊓U+26706 𦜆U+267EA 𦟪U+2688A 𦢊U+2690E 𦤎U+26E05 𦸅U+2725F 𧉟U+27304 𧌄U+27371 𧍱U+27486 𧒆U+277F0 𧟰U+279A0 𧦠U+27A63 𧩣U+27B2A 𧬪U+27B99 𧮙U+27EF4 𧻴U+27FC1 𧿁U+27FEC 𧿬U+27FF3 𧿳U+280BE 𨂾U+280BF 𨂿U+280E9 𨃩U+280F0 𨃰U+28154 𨅔U+282CD 𨋍U+2837D 𨍽U+2838A 𨎊U+28487 𨒇U+28595 𨖕U+28891 𨢑U+28D99 𨶙U+28E39 𨸹U+2945D 𩑝U+2947E 𩑾U+294E5 𩓥U+296A8 𩚨U+296E9 𩛩U+29704 𩜄U+29730 𩜰U+29D71 𩵱U+29DD3 𩷓U+29E19 𩸙U+29E36 𩸶U+29EAC 𩺬U+29F27 𩼧U+29F30 𩼰U+29F48 𩽈U+29F70 𩽰U+2A04E 𪁎U+2A0BA 𪂺U+2A1E1 𪇡U+2A41E 𪐞U+2A590 𪖐U+2A612 𪘒U+2A64A 𪙊CJK Unified Ideographs Extension C glyphs:U+2A736 𪜶, U+2AE5A 𪹚, and U+2B4A2 𫒢CJK Unified Ideographs Extension E glyphs:U+2B8C6 𫣆, U+2C816 𬠖, and U+2C9B0 𬦰.
* Hayden Wongcontributed the new glyphs in
 CJK Unified Ideographs Extension B U+20020..U+2004F
 and U+29E00..2A0FF.
* twuchiutanncontributed the new glyphs in
 CJK Unified Ideographs Extension B U+20050..U+2073F.
* Boris Zhangredrew CJK Unified Ideographs
 Extension D glyphs U+2B75F, U+2B76B, and
 Extension I glyphs U+2B7EF, U+2EC1F, U+2EC20,
 U+2EC21, U+2EC2F, U+2EC6F, U+2ECBF, U+2ECEC, and U+2ED42.
* 湖 远星contributed the following glyphs, which are common
 in Cantonese, Hokkien, Hakka,etc.,from a list provided
 with the Ichiten font.CJK Unified Ideographs Extension B glyphs:U+203B7 𠎷U+20546 𠕆U+20584 𠖄U+205FB 𠗻U+207A9 𠞩U+207AD 𠞭U+20803 𠠃U+2081D 𠠝U+20895 𠢕U+20BD7 𠯗U+20C41 𠱁U+20CBF 𠲿U+20CD4 𠳔U+20D5D 𠵝U+20D71 𠵱U+20DA7 𠶧U+20E76 𠹶U+20E98 𠺘U+20ED8 𠻘U+20F3B 𠼻U+20F7E 𠽾U+21014 𡀔U+210AB 𡂫U+210F6 𡃶U+21145 𡅅U+2176D 𡝭U+217D3 𡟓U+2180D 𡠍U+21883 𡢃U+2197C 𡥼U+21C2A 𡰪U+21CA2 𡲢U+21CDE 𡳞U+21DD1 𡷑U+21F0F 𡼏U+221A1 𢆡U+22399 𢎙U+224DC 𢓜U+2251B 𢔛U+22775 𢝵U+22AB1 𢪱U+22AE6 𢫦U+22BED 𢯭U+22BFE 𢯾U+22C4B 𢱋U+22C62 𢱢U+22C64 𢱤U+22CB4 𢲴U+22CB8 𢲸U+22CC6 𢳆U+22CEA 𢳪U+22D80 𢶀U+22F0C 𢼌U+22F1B 𢼛U+23073 𣁳U+23074 𣁴U+23350 𣍐U+236BA 𣚺U+236EE 𣛮U+23B88 𣮈U+23CA9 𣲩U+23EF8 𣻸U+23F0E 𣼎U+240D2 𤃒U+241AC 𤆬U+24259 𤉙U+242B6 𤊶U+2430D 𤌍U+24352 𤍒U+24364 𤍤U+24419 𤐙U+24430 𤐰U+24605 𤘅U+2479A 𤞚U+24C8D 𤲍U+24D80 𤶀U+24D83 𤶃U+24E01 𤸁U+24E31 𤸱U+24E85 𤺅U+24EA7 𤺧U+24EAA 𤺪U+25148 𥅈U+2517E 𥅾U+2531A 𥌚U+25349 𥍉U+25435 𥐵U+2546E 𥑮U+257C7 𥟇U+25BDF 𥯟U+25BE5 𥯥U+25C14 𥰔U+25D0A 𥴊U+25E86 𥺆U+2624E 𦉎U+26293 𦊓U+26706 𦜆U+267EA 𦟪U+2688A 𦢊U+2690E 𦤎U+26E05 𦸅U+2725F 𧉟U+27304 𧌄U+27371 𧍱U+27486 𧒆U+277F0 𧟰U+279A0 𧦠U+27A63 𧩣U+27B2A 𧬪U+27B99 𧮙U+27EF4 𧻴U+27FC1 𧿁U+27FEC 𧿬U+27FF3 𧿳U+280BE 𨂾U+280BF 𨂿U+280E9 𨃩U+280F0 𨃰U+28154 𨅔U+282CD 𨋍U+2837D 𨍽U+2838A 𨎊U+28487 𨒇U+28595 𨖕U+28891 𨢑U+28D99 𨶙U+28E39 𨸹U+2945D 𩑝U+2947E 𩑾U+294E5 𩓥U+296A8 𩚨U+296E9 𩛩U+29704 𩜄U+29730 𩜰U+29D71 𩵱U+29DD3 𩷓U+29E19 𩸙U+29E36 𩸶U+29EAC 𩺬U+29F27 𩼧U+29F30 𩼰U+29F48 𩽈U+29F70 𩽰U+2A04E 𪁎U+2A0BA 𪂺U+2A1E1 𪇡U+2A41E 𪐞U+2A590 𪖐U+2A612 𪘒U+2A64A 𪙊CJK Unified Ideographs Extension C glyphs:U+2A736 𪜶, U+2AE5A 𪹚, and U+2B4A2 𫒢CJK Unified Ideographs Extension E glyphs:U+2B8C6 𫣆, U+2C816 𬠖, and U+2C9B0 𬦰.
* CJK Unified Ideographs Extension B glyphs:U+203B7 𠎷U+20546 𠕆U+20584 𠖄U+205FB 𠗻U+207A9 𠞩U+207AD 𠞭U+20803 𠠃U+2081D 𠠝U+20895 𠢕U+20BD7 𠯗U+20C41 𠱁U+20CBF 𠲿U+20CD4 𠳔U+20D5D 𠵝U+20D71 𠵱U+20DA7 𠶧U+20E76 𠹶U+20E98 𠺘U+20ED8 𠻘U+20F3B 𠼻U+20F7E 𠽾U+21014 𡀔U+210AB 𡂫U+210F6 𡃶U+21145 𡅅U+2176D 𡝭U+217D3 𡟓U+2180D 𡠍U+21883 𡢃U+2197C 𡥼U+21C2A 𡰪U+21CA2 𡲢U+21CDE 𡳞U+21DD1 𡷑U+21F0F 𡼏U+221A1 𢆡U+22399 𢎙U+224DC 𢓜U+2251B 𢔛U+22775 𢝵U+22AB1 𢪱U+22AE6 𢫦U+22BED 𢯭U+22BFE 𢯾U+22C4B 𢱋U+22C62 𢱢U+22C64 𢱤U+22CB4 𢲴U+22CB8 𢲸U+22CC6 𢳆U+22CEA 𢳪U+22D80 𢶀U+22F0C 𢼌U+22F1B 𢼛U+23073 𣁳U+23074 𣁴U+23350 𣍐U+236BA 𣚺U+236EE 𣛮U+23B88 𣮈U+23CA9 𣲩U+23EF8 𣻸U+23F0E 𣼎U+240D2 𤃒U+241AC 𤆬U+24259 𤉙U+242B6 𤊶U+2430D 𤌍U+24352 𤍒U+24364 𤍤U+24419 𤐙U+24430 𤐰U+24605 𤘅U+2479A 𤞚U+24C8D 𤲍U+24D80 𤶀U+24D83 𤶃U+24E01 𤸁U+24E31 𤸱U+24E85 𤺅U+24EA7 𤺧U+24EAA 𤺪U+25148 𥅈U+2517E 𥅾U+2531A 𥌚U+25349 𥍉U+25435 𥐵U+2546E 𥑮U+257C7 𥟇U+25BDF 𥯟U+25BE5 𥯥U+25C14 𥰔U+25D0A 𥴊U+25E86 𥺆U+2624E 𦉎U+26293 𦊓U+26706 𦜆U+267EA 𦟪U+2688A 𦢊U+2690E 𦤎U+26E05 𦸅U+2725F 𧉟U+27304 𧌄U+27371 𧍱U+27486 𧒆U+277F0 𧟰U+279A0 𧦠U+27A63 𧩣U+27B2A 𧬪U+27B99 𧮙U+27EF4 𧻴U+27FC1 𧿁U+27FEC 𧿬U+27FF3 𧿳U+280BE 𨂾U+280BF 𨂿U+280E9 𨃩U+280F0 𨃰U+28154 𨅔U+282CD 𨋍U+2837D 𨍽U+2838A 𨎊U+28487 𨒇U+28595 𨖕U+28891 𨢑U+28D99 𨶙U+28E39 𨸹U+2945D 𩑝U+2947E 𩑾U+294E5 𩓥U+296A8 𩚨U+296E9 𩛩U+29704 𩜄U+29730 𩜰U+29D71 𩵱U+29DD3 𩷓U+29E19 𩸙U+29E36 𩸶U+29EAC 𩺬U+29F27 𩼧U+29F30 𩼰U+29F48 𩽈U+29F70 𩽰U+2A04E 𪁎U+2A0BA 𪂺U+2A1E1 𪇡U+2A41E 𪐞U+2A590 𪖐U+2A612 𪘒U+2A64A 𪙊
* CJK Unified Ideographs Extension C glyphs:U+2A736 𪜶, U+2AE5A 𪹚, and U+2B4A2 𫒢
* CJK Unified Ideographs Extension E glyphs:U+2B8C6 𫣆, U+2C816 𬠖, and U+2C9B0 𬦰.
* Plane 3:twuchiutannmodified U+30EDD and U+30EDE (biang),
	 originally drawn by Ming Fan, to differentiate between
	 traditional and simplified Chinese versions.湖 远星contributed the following glyphs, which are common in
 Cantonese, Hokkien, Hakka,etc.,from a list given in the
 Ichiten font.CJK Unified Ideographs Extension G glyphs:U+301DB 𰇛, U+308FB 𰣻, and U+30E6C 𰹬CJK Unified Ideographs Extension H glyph:U+31C7F 𱱿.
* twuchiutannmodified U+30EDD and U+30EDE (biang),
	 originally drawn by Ming Fan, to differentiate between
	 traditional and simplified Chinese versions.
* 湖 远星contributed the following glyphs, which are common in
 Cantonese, Hokkien, Hakka,etc.,from a list given in the
 Ichiten font.CJK Unified Ideographs Extension G glyphs:U+301DB 𰇛, U+308FB 𰣻, and U+30E6C 𰹬CJK Unified Ideographs Extension H glyph:U+31C7F 𱱿.
* CJK Unified Ideographs Extension G glyphs:U+301DB 𰇛, U+308FB 𰣻, and U+30E6C 𰹬
* CJK Unified Ideographs Extension H glyph:U+31C7F 𱱿.
* Plane 15 CSUR/UCSUR:Rebecca Bettencourtcontributed:U+F16B0..U+F16DF DeraniU+F2000..U+F267F Sadalian.Paul Hardycontributed
 U+F1C80..U+F1C9C Sitelen Pona Radicals.
* Rebecca Bettencourtcontributed:U+F16B0..U+F16DF DeraniU+F2000..U+F267F Sadalian.
* U+F16B0..U+F16DF Derani
* U+F2000..U+F267F Sadalian.
* Paul Hardycontributed
 U+F1C80..U+F1C9C Sitelen Pona Radicals.

#### Unifont 15.1

* 24 February 2024 (Unifont 15.1.05)Plane 0:Ho-seok Eeredrew all Hangul glyphs not in the
 Hangul Syllables range, so their style more closely
 resembles the style of the Hangul Syllables range:
 U+1100..U+11FF Hangul Jamo, U+3131..U+318E Hangul
 Compatibility Jamo, U+A960..U+A97C Hangul Jamo Extended-A,
 U+D7B0..U+D7FB Hangul Jamo Extended-B.Hayden Wongimproved several glyphs in the range
 U+2100..U+214F Letterlike Symbols.Johnnie Weaverredrew U+013D LATIN CAPITAL LETTER L
 WITH CARON for better compatibility with other glyphs in
 the Czech and Slovak alphabets.Planes 2 and 3:almost 600 new ideographs, including:Boris ZhangandYzy32767contributed
 U+20000..U+2001F.Boris ZhangandYzy32767contributed
 the entire CJK Unified Ideographs Extension D range,
 U+2B740..U+2B81D.湖 远星contributed 335 glyphs across Plane 2
 and Plane 3 with common Cantonese ideographs.Other new idegraphs in CJK Unified Ideographs Extension I.Plane F: Paul Hardymodified the Sitelen Pona script,
 added combining character indicators and adding several new
 glyphs since the last release. This completes the most current
 version of Sitelen Pona.
 encodings
* Plane 0:Ho-seok Eeredrew all Hangul glyphs not in the
 Hangul Syllables range, so their style more closely
 resembles the style of the Hangul Syllables range:
 U+1100..U+11FF Hangul Jamo, U+3131..U+318E Hangul
 Compatibility Jamo, U+A960..U+A97C Hangul Jamo Extended-A,
 U+D7B0..U+D7FB Hangul Jamo Extended-B.Hayden Wongimproved several glyphs in the range
 U+2100..U+214F Letterlike Symbols.Johnnie Weaverredrew U+013D LATIN CAPITAL LETTER L
 WITH CARON for better compatibility with other glyphs in
 the Czech and Slovak alphabets.
* Ho-seok Eeredrew all Hangul glyphs not in the
 Hangul Syllables range, so their style more closely
 resembles the style of the Hangul Syllables range:
 U+1100..U+11FF Hangul Jamo, U+3131..U+318E Hangul
 Compatibility Jamo, U+A960..U+A97C Hangul Jamo Extended-A,
 U+D7B0..U+D7FB Hangul Jamo Extended-B.
* Hayden Wongimproved several glyphs in the range
 U+2100..U+214F Letterlike Symbols.
* Johnnie Weaverredrew U+013D LATIN CAPITAL LETTER L
 WITH CARON for better compatibility with other glyphs in
 the Czech and Slovak alphabets.
* Planes 2 and 3:almost 600 new ideographs, including:Boris ZhangandYzy32767contributed
 U+20000..U+2001F.Boris ZhangandYzy32767contributed
 the entire CJK Unified Ideographs Extension D range,
 U+2B740..U+2B81D.湖 远星contributed 335 glyphs across Plane 2
 and Plane 3 with common Cantonese ideographs.Other new idegraphs in CJK Unified Ideographs Extension I.
* Boris ZhangandYzy32767contributed
 U+20000..U+2001F.
* Boris ZhangandYzy32767contributed
 the entire CJK Unified Ideographs Extension D range,
 U+2B740..U+2B81D.
* 湖 远星contributed 335 glyphs across Plane 2
 and Plane 3 with common Cantonese ideographs.
* Other new idegraphs in CJK Unified Ideographs Extension I.
* Plane F: Paul Hardymodified the Sitelen Pona script,
 added combining character indicators and adding several new
 glyphs since the last release. This completes the most current
 version of Sitelen Pona.
 encodings
* 29 October 2023 (Unifont 15.1.04)Default and Japanese versions have larger supersets
 of Plane 2 and Plane 3 glyphs.Johnnie Weavercontributed updates for
 U+266D..U+266F and U+26BC.
* Default and Japanese versions have larger supersets
 of Plane 2 and Plane 3 glyphs.
* Johnnie Weavercontributed updates for
 U+266D..U+266F and U+26BC.
* 21 October 2023 (Unifont 15.1.03)Boris ZhangandYzy32767contributed
 CJK Unified Ideographs Extension I glyphs
 (U+2EBF0..U+2EE5D).湖 远星contributed 14 glyphs to CJK
 Unified Ideographs Extensions B and C
 and updated U+5C81 and U+6708.
* Boris ZhangandYzy32767contributed
 CJK Unified Ideographs Extension I glyphs
 (U+2EBF0..U+2EE5D).
* 湖 远星contributed 14 glyphs to CJK
 Unified Ideographs Extensions B and C
 and updated U+5C81 and U+6708.
* 21 September 2023 (Unifont 15.1.02)湖 远星:Adjusted 46 glyphs in the Plane 0 Wen Quan Yi range,
 U+2F00..U+9FFF.Contributed Plane 3 CJK Unified Ideographs Extension G
 glyphs in the range U+30000..U+3017F.
* 湖 远星:Adjusted 46 glyphs in the Plane 0 Wen Quan Yi range,
 U+2F00..U+9FFF.Contributed Plane 3 CJK Unified Ideographs Extension G
 glyphs in the range U+30000..U+3017F.
* Adjusted 46 glyphs in the Plane 0 Wen Quan Yi range,
 U+2F00..U+9FFF.
* Contributed Plane 3 CJK Unified Ideographs Extension G
 glyphs in the range U+30000..U+3017F.
* 12 September 2023 (Unifont 15.1.01)As mentioned during the year leading up to this release,TrueType fonts are no longer produced by the default build;
 OpenType fonts have taken their place.This change has been
 driven by the diminishing support for TrueType fonts in the Pango
 font rendering engine. TrueType fonts can still be built from
 the distribution tarball using the command "make truetype" in
 the font directory.Ho-Seok Eeproposeda new Johab encoding for
 algorithmic Hangul Syllables generation.The resulting
 scheme uses 6 variations of initial consonants
 (choseong), 3 of medial vowels and diphthongs
 (jungseong), and 1 of final consonants (jongseong).
 The image on the left is partial output from a new supporting
 Unifont utility,unijohab2html, which gives
 an overview of how the three components of a Hangul syllable
 combine with each other and outputs any overlaps for a font
 designer's analysis. A full discussion of this new Johab
 6/3/1 encoding appears on theUnifont Hangul Syllables Generationweb page.Minseo Lee (이민서)provided feedback on the
 glyphs prior to their release.Following a suggestion by Ho-Seok Ee, thehangul-base.hexfile that contains the
 Johab 6/3/1 glyphs for Hangul syllable formation now begins
 at code point U+E000. This allows building a Unifont variant
 with that entire Hangul johab glyph set in the Uniode Plane 0
 Private Use Area (PUA) using the command
 "make PUA=plane00/hangul/hangul-base.hex".
 in the font directory. Unifont builds have traditionally
 left the PUA available for CSUR/UCSUR glyphs, which is still
 the default; see below for a discussion of the CSUR/UCSUR glyphs.Johnnie Weavermodified "IJ" ligature glyphs U+0132 and
 U+0133. He also modified U+1E9E LATIN CAPITAL LETTER SHARP S.Paul Hardy:Modified U+2CC2 COPTIC CAPITAL LETTER CROSSED SHEI and
 U+2CC3 COPTIC SMALL LETTER CROSSED SHEI for consistency
 with the redrawn U+03E2 COPTIC CAPITAL LETTER SHEI and
 U+03E3 COPTIC SMALL LETTER SHEI.Redrew Ideographic Description Characters (U+2FF0..U+2FFB)
 for consistency and added new glyphs (U+2FFC..U+2FFF).
 Also added CJK Strokes glyph U+31EF IDEOGRAPHIC DESCRIPTION
 CHARACTER SUBTRACTION.Modified star glyphs U+2605, U+2606, and U+2BE8 for
 consistency.Modified several Chinese ideographs and Korean ideographs in
 CJK Unified Ideographs Extension A (U+3400..U+4DBF) per the
 Unicode Standard version 15.1.0.Wen Quan Yi Glyphs:Made modifications to Korean
 ideographs in CJK Unified Ideographs Extension A
 (U+3400..U+4DBF) per Unicode 15.1.0 changes.
 Modified CJK Unified Ideographs Extension A U+3B9D, U+454E,
 U+49C8 (from 湖 远星) and U+56B8.
 Modified CJK Unified Ideographs Extension U+809E and U+891D.Modified Alchemical Symbols (U+1F700..U+1F77F) per Unicode
 15.1.0 changes.Added three hexadecimal digit notations to the Plane 0 UCSUR:U+EBE0..U+EBEF:
 Boby Lapointe's "bibi-binary" notation.U+EBF0..U+EBFF:
 Bruce Alan Martin's bit location notation.U+ECF0..U+ECFF:
 Ronald O. Whitaker's triangular notation.Implemented other glyph changes per the Unicode Standard version
 15.1.0.Several other minor changes; see the ChangeLog file in the
 main tarball for details.
* As mentioned during the year leading up to this release,TrueType fonts are no longer produced by the default build;
 OpenType fonts have taken their place.This change has been
 driven by the diminishing support for TrueType fonts in the Pango
 font rendering engine. TrueType fonts can still be built from
 the distribution tarball using the command "make truetype" in
 the font directory.
* Ho-Seok Eeproposeda new Johab encoding for
 algorithmic Hangul Syllables generation.The resulting
 scheme uses 6 variations of initial consonants
 (choseong), 3 of medial vowels and diphthongs
 (jungseong), and 1 of final consonants (jongseong).
 The image on the left is partial output from a new supporting
 Unifont utility,unijohab2html, which gives
 an overview of how the three components of a Hangul syllable
 combine with each other and outputs any overlaps for a font
 designer's analysis. A full discussion of this new Johab
 6/3/1 encoding appears on theUnifont Hangul Syllables Generationweb page.Minseo Lee (이민서)provided feedback on the
 glyphs prior to their release.
* Following a suggestion by Ho-Seok Ee, thehangul-base.hexfile that contains the
 Johab 6/3/1 glyphs for Hangul syllable formation now begins
 at code point U+E000. This allows building a Unifont variant
 with that entire Hangul johab glyph set in the Uniode Plane 0
 Private Use Area (PUA) using the command
 "make PUA=plane00/hangul/hangul-base.hex".
 in the font directory. Unifont builds have traditionally
 left the PUA available for CSUR/UCSUR glyphs, which is still
 the default; see below for a discussion of the CSUR/UCSUR glyphs.
* Johnnie Weavermodified "IJ" ligature glyphs U+0132 and
 U+0133. He also modified U+1E9E LATIN CAPITAL LETTER SHARP S.
* Paul Hardy:Modified U+2CC2 COPTIC CAPITAL LETTER CROSSED SHEI and
 U+2CC3 COPTIC SMALL LETTER CROSSED SHEI for consistency
 with the redrawn U+03E2 COPTIC CAPITAL LETTER SHEI and
 U+03E3 COPTIC SMALL LETTER SHEI.Redrew Ideographic Description Characters (U+2FF0..U+2FFB)
 for consistency and added new glyphs (U+2FFC..U+2FFF).
 Also added CJK Strokes glyph U+31EF IDEOGRAPHIC DESCRIPTION
 CHARACTER SUBTRACTION.Modified star glyphs U+2605, U+2606, and U+2BE8 for
 consistency.Modified several Chinese ideographs and Korean ideographs in
 CJK Unified Ideographs Extension A (U+3400..U+4DBF) per the
 Unicode Standard version 15.1.0.Wen Quan Yi Glyphs:Made modifications to Korean
 ideographs in CJK Unified Ideographs Extension A
 (U+3400..U+4DBF) per Unicode 15.1.0 changes.
 Modified CJK Unified Ideographs Extension A U+3B9D, U+454E,
 U+49C8 (from 湖 远星) and U+56B8.
 Modified CJK Unified Ideographs Extension U+809E and U+891D.Modified Alchemical Symbols (U+1F700..U+1F77F) per Unicode
 15.1.0 changes.Added three hexadecimal digit notations to the Plane 0 UCSUR:U+EBE0..U+EBEF:
 Boby Lapointe's "bibi-binary" notation.U+EBF0..U+EBFF:
 Bruce Alan Martin's bit location notation.U+ECF0..U+ECFF:
 Ronald O. Whitaker's triangular notation.
* Modified U+2CC2 COPTIC CAPITAL LETTER CROSSED SHEI and
 U+2CC3 COPTIC SMALL LETTER CROSSED SHEI for consistency
 with the redrawn U+03E2 COPTIC CAPITAL LETTER SHEI and
 U+03E3 COPTIC SMALL LETTER SHEI.
* Redrew Ideographic Description Characters (U+2FF0..U+2FFB)
 for consistency and added new glyphs (U+2FFC..U+2FFF).
 Also added CJK Strokes glyph U+31EF IDEOGRAPHIC DESCRIPTION
 CHARACTER SUBTRACTION.
* Modified star glyphs U+2605, U+2606, and U+2BE8 for
 consistency.
* Modified several Chinese ideographs and Korean ideographs in
 CJK Unified Ideographs Extension A (U+3400..U+4DBF) per the
 Unicode Standard version 15.1.0.
* Wen Quan Yi Glyphs:Made modifications to Korean
 ideographs in CJK Unified Ideographs Extension A
 (U+3400..U+4DBF) per Unicode 15.1.0 changes.
 Modified CJK Unified Ideographs Extension A U+3B9D, U+454E,
 U+49C8 (from 湖 远星) and U+56B8.
 Modified CJK Unified Ideographs Extension U+809E and U+891D.
* Modified Alchemical Symbols (U+1F700..U+1F77F) per Unicode
 15.1.0 changes.
* Added three hexadecimal digit notations to the Plane 0 UCSUR:U+EBE0..U+EBEF:
 Boby Lapointe's "bibi-binary" notation.U+EBF0..U+EBFF:
 Bruce Alan Martin's bit location notation.U+ECF0..U+ECFF:
 Ronald O. Whitaker's triangular notation.
* U+EBE0..U+EBEF:
 Boby Lapointe's "bibi-binary" notation.
* U+EBF0..U+EBFF:
 Bruce Alan Martin's bit location notation.
* U+ECF0..U+ECFF:
 Ronald O. Whitaker's triangular notation.
* Implemented other glyph changes per the Unicode Standard version
 15.1.0.
* Several other minor changes; see the ChangeLog file in the
 main tarball for details.

#### Earlier Releases

See the Archive link at the top of this page for information on
 earlier Unifont releases.

### Unifont Glyph Tables

Unifont font files contain glyphs in several Unicode planes.
 The following table provides an overview of this coverage.

GNU Unifont Font File Plane Coverage

Font Filename

Plane 0

Plane 1

Plane 2

Plane 3

Plane 14

Plane 15

unifont-*

X



X
1,2

X
1,2





unifont_jp-*

X



X
1,2

X
1,2





unifont_upper-*



X

X
3

X
3

X



unifont_csur-*

X









X

Notes:

1PCF fonts can only include glyphs in Plane 0.

2Only a subset of Plane 2 and Plane 3 CJK glyphs plus
 the Plane 1 Copyleft glyph (U+1F12F) are included, to stay within the
 OpenType limit of 65,536 glyphs.

3unifont_upperfonts will contain a superset
 of Chinese Plane 2 and Plane 3 glyphs plus JIS X 0213 glyphs
 until the OpenType font nears its limit of 65,536 code points.

Click on each link in the tables below to show its corresponding
 256-code point range within the respective Unicode planes.

#### Plane 0 Glyphs

The table below links to the glyphs in the Plane 0 (Basic
 Multilingual Plane)unifontfont files.

 GNU Unifont Glyphs

Unicode Basic Multilingual Plane


00

01

02

03

04

05

06

07

08

09

0A

0B

0C

0D

0E

0F

10

11

12

13

14

15

16

17

18

19

1A

1B

1C

1D

1E

1F

20

21

22

23

24

25

26

27

28

29

2A

2B

2C

2D

2E

2F

30

31

32

33

34

35

36

37

38

39

3A

3B

3C

3D

3E

3F

40

41

42

43

44

45

46

47

48

49

4A

4B

4C

4D

4E

4F

50

51

52

53

54

55

56

57

58

59

5A

5B

5C

5D

5E

5F

60

61

62

63

64

65

66

67

68

69

6A

6B

6C

6D

6E

6F

70

71

72

73

74

75

76

77

78

79

7A

7B

7C

7D

7E

7F

80

81

82

83

84

85

86

87

88

89

8A

8B

8C

8D

8E

8F

90

91

92

93

94

95

96

97

98

99

9A

9B

9C

9D

9E

9F

A0

A1

A2

A3

A4

A5

A6

A7

A8

A9

AA

AB

AC

AD

AE

AF

B0

B1

B2

B3

B4

B5

B6

B7

B8

B9

BA

BB

BC

BD

BE

BF

C0

C1

C2

C3

C4

C5

C6

C7

C8

C9

CA

CB

CC

CD

CE

CF

D0

D1

D2

D3

D4

D5

D6

D7

Surrogate Pairs

Private Use Area

Private Use Area

F9

FA

FB

FC

FD

FE

FF

This next table links to the glyphs in the Plane 0 (Basic
 Multilingual Plane)unifont_jpJapanese variant font files.
 See also the Plane 2 glyphs further down, which are only
 included in theunifont_jpOpenType and TrueType font files.

GNU Unifont Glyphs — Japanese Version
with Page Coverage for Plane 0
(Green=100%, Red=0%)

00

01

02

03

04

05

06

07

08

09

0A

0B

0C

0D

0E

0F

10

11

12

13

14

15

16

17

18

19

1A

1B

1C

1D

1E

1F

20

21

22

23

24

25

26

27

28

29

2A

2B

2C

2D

2E

2F

30

31

32

33

34

35

36

37

38

39

3A

3B

3C

3D

3E

3F

40

41

42

43

44

45

46

47

48

49

4A

4B

4C

4D

4E

4F

50

51

52

53

54

55

56

57

58

59

5A

5B

5C

5D

5E

5F

60

61

62

63

64

65

66

67

68

69

6A

6B

6C

6D

6E

6F

70

71

72

73

74

75

76

77

78

79

7A

7B

7C

7D

7E

7F

80

81

82

83

84

85

86

87

88

89

8A

8B

8C

8D

8E

8F

90

91

92

93

94

95

96

97

98

99

9A

9B

9C

9D

9E

9F

A0

A1

A2

A3

A4

A5

A6

A7

A8

A9

AA

AB

AC

AD

AE

AF

B0

B1

B2

B3

B4

B5

B6

B7

B8

B9

BA

BB

BC

BD

BE

BF

C0

C1

C2

C3

C4

C5

C6

C7

C8

C9

CA

CB

CC

CD

CE

CF

D0

D1

D2

D3

D4

D5

D6

D7

Surrogate Pairs

Private Use Area

Private Use Area

F9

FA

FB

FC

FD

FE

FF

#### Plane 1 Glyphs

The next table links to glyphs in Plane 1 (Supplementary
 Multilingual Plane) OpenType and TrueTypeunifont_upperfont files.

GNU Unifont Glyphs
with Page Coverage for Plane 1
(Green=100%, Red=0%)

0100

0101

0102

0103

0104

0105

0106

0107

0108

0109

010A

010B

010C

010D

010E

010F

0110

0111

0112

0113

0114

0115

0116

0117

0118

0119

011A

011B

011C

011D

011E

011F

0120

0121

0122

0123

0124

0125

0126

0127

0128

0129

012A

012B

012C

012D

012E

012F

0130

0131

0132

0133

0134

0135

0136

0137

0138

0139

013A

013B

013C

013D

013E

013F

0140

0141

0142

0143

0144

0145

0146

0147

0148

0149

014A

014B

014C

014D

014E

014F

0150

0151

0152

0153

0154

0155

0156

0157

0158

0159

015A

015B

015C

015D

015E

015F

0160

0161

0162

0163

0164

0165

0166

0167

0168

0169

016A

016B

016C

016D

016E

016F

0170

0171

0172

0173

0174

0175

0176

0177

0178

0179

017A

017B

017C

017D

017E

017F

0180

0181

0182

0183

0184

0185

0186

0187

0188

0189

018A

018B

018C

018D

018E

018F

0190

0191

0192

0193

0194

0195

0196

0197

0198

0199

019A

019B

019C

019D

019E

019F

01A0

01A1

01A2

01A3

01A4

01A5

01A6

01A7

01A8

01A9

01AA

01AB

01AC

01AD

01AE

01AF

01B0

01B1

01B2

01B3

01B4

01B5

01B6

01B7

01B8

01B9

01BA

01BB

01BC

01BD

01BE

01BF

01C0

01C1

01C2

01C3

01C4

01C5

01C6

01C7

01C8

01C9

01CA

01CB

01CC

01CD

01CE

01CF

01D0

01D1

01D2

01D3

01D4

01D5

01D6

01D7

01D8

01D9

01DA

01DB

01DC

01DD

01DE

01DF

01E0

01E1

01E2

01E3

01E4

01E5

01E6

01E7

01E8

01E9

01EA

01EB

01EC

01ED

01EE

01EF

01F0

01F1

01F2

01F3

01F4

01F5

01F6

01F7

01F8

01F9

01FA

01FB

01FC

01FD

01FE

01FF

#### Plane 2 Glyphs

The table below links to the Japanese glyphs in Plane 2 (Supplementary Ideographic
 Plane) contained in theunifont_jpOpenType and TrueType font files.Note:These Plane 2 glyphs along with the Plane 0 glyphs inunifont_jpfont files provide complete coverage of the JIS X 0213
 standard. Only 303 glyphs appear in the files below. Files with no glyphs appear
 with a gray background.

 GNU Unifont Glyphs — Japanese Version
with Page Coverage for Plane 2

 (Gray=0%)


0200

0201

0202

0203

0204

0205

0206

0207

0208

0209

020A

020B

020C

020D

020E

020F

0210

0211

0212

0213

0214

0215

0216

0217

0218

0219

021A

021B

021C

021D

021E

021F

0220

0221

0222

0223

0224

0225

0226

0227

0228

0229

022A

022B

022C

022D

022E

022F

0230

0231

0232

0233

0234

0235

0236

0237

0238

0239

023A

023B

023C

023D

023E

023F

0240

0241

0242

0243

0244

0245

0246

0247

0248

0249

024A

024B

024C

024D

024E

024F

0250

0251

0252

0253

0254

0255

0256

0257

0258

0259

025A

025B

025C

025D

025E

025F

0260

0261

0262

0263

0264

0265

0266

0267

0268

0269

026A

026B

026C

026D

026E

026F

0270

0271

0272

0273

0274

0275

0276

0277

0278

0279

027A

027B

027C

027D

027E

027F

0280

0281

0282

0283

0284

0285

0286

0287

0288

0289

028A

028B

028C

028D

028E

028F

0290

0291

0292

0293

0294

0295

0296

0297

0298

0299

029A

029B

029C

029D

029E

029F

02A0

02A1

02A2

02A3

02A4

02A5

02A6

02A7

02A8

02A9

02AA

02AB

02AC

02AD

02AE

02AF

02B0

02B1

02B2

02B3

02B4

02B5

02B6

02B7

02B8

02B9

02BA

02BB

02BC

02BD

02BE

02BF

02C0

02C1

02C2

02C3

02C4

02C5

02C6

02C7

02C8

02C9

02CA

02CB

02CC

02CD

02CE

02CF

02D0

02D1

02D2

02D3

02D4

02D5

02D6

02D7

02D8

02D9

02DA

02DB

02DC

02DD

02DE

02DF

02E0

02E1

02E2

02E3

02E4

02E5

02E6

02E7

02E8

02E9

02EA

02EB

02EC

02ED

02EE

02EF

02F0

02F1

02F2

02F3

02F4

02F5

02F6

02F7

02F8

02F9

02FA

02FB

02FC

02FD

02FE

02FF

This next table links to the Chinese glyphs in Plane 2 (Supplementary Ideographic
 Plane) contained inunifontOpenType and TrueType font files.Note:These Plane 2 glyphs along with the default Plane 0 glyphs
 in Unifont provide complete coverage of the Table of General Standard Chinese
 Characters (通用规范汉字表). Only 232 glyphs appear in the files below.
 Files with no glyphs appear with a gray background.

 GNU Unifont Glyphs — Chinese Version

 with Page Coverage for Plane 2
(Gray=0%)


0200

0201

0202

0203

0204

0205

0206

0207

0208

0209

020A

020B

020C

020D

020E

020F

0210

0211

0212

0213

0214

0215

0216

0217

0218

0219

021A

021B

021C

021D

021E

021F

0220

0221

0222

0223

0224

0225

0226

0227

0228

0229

022A

022B

022C

022D

022E

022F

0230

0231

0232

0233

0234

0235

0236

0237

0238

0239

023A

023B

023C

023D

023E

023F

0240

0241

0242

0243

0244

0245

0246

0247

0248

0249

024A

024B

024C

024D

024E

024F

0250

0251

0252

0253

0254

0255

0256

0257

0258

0259

025A

025B

025C

025D

025E

025F

0260

0261

0262

0263

0264

0265

0266

0267

0268

0269

026A

026B

026C

026D

026E

026F

0270

0271

0272

0273

0274

0275

0276

0277

0278

0279

027A

027B

027C

027D

027E

027F

0280

0281

0282

0283

0284

0285

0286

0287

0288

0289

028A

028B

028C

028D

028E

028F

0290

0291

0292

0293

0294

0295

0296

0297

0298

0299

029A

029B

029C

029D

029E

029F

02A0

02A1

02A2

02A3

02A4

02A5

02A6

02A7

02A8

02A9

02AA

02AB

02AC

02AD

02AE

02AF

02B0

02B1

02B2

02B3

02B4

02B5

02B6

02B7

02B8

02B9

02BA

02BB

02BC

02BD

02BE

02BF

02C0

02C1

02C2

02C3

02C4

02C5

02C6

02C7

02C8

02C9

02CA

02CB

02CC

02CD

02CE

02CF

02D0

02D1

02D2

02D3

02D4

02D5

02D6

02D7

02D8

02D9

02DA

02DB

02DC

02DD

02DE

02DF

02E0

02E1

02E2

02E3

02E4

02E5

02E6

02E7

02E8

02E9

02EA

02EB

02EC

02ED

02EE

02EF

02F0

02F1

02F2

02F3

02F4

02F5

02F6

02F7

02F8

02F9

02FA

02FB

02FC

02FD

02FE

02FF

#### Plane 3 Glyphs

Plane 3 begins with the CJK Unified Ideographs Extension G block, from U+30000 through
 U+3134A. This includes the highly complex biang Chinese ideograph and
 taito Japanese ideograph:

* Biang(U+30EDD and U+30EDE)
* Taito (Kanji)(U+3106C).

 GNU Unifont Glyphs

 with Page Coverage for Plane 3
(Gray=0%)


0300

0301

0302

0303

0304

0305

0306

0307

0308

0309

030A

030B

030C

030D

030E

030F

0310

0311

0312

0313

0314

0315

0316

0317

0318

0319

031A

031B

031C

031D

031E

031F

0320

0321

0322

0323

0324

0325

0326

0327

0328

0329

032A

032B

032C

032D

032E

032F

0330

0331

0332

0333

0334

0335

0336

0337

0338

0339

033A

033B

033C

033D

033E

033F

0340

0341

0342

0343

0344

0345

0346

0347

0348

0349

034A

034B

034C

034D

034E

034F

0350

0351

0352

0353

0354

0355

0356

0357

0358

0359

035A

035B

035C

035D

035E

035F

0360

0361

0362

0363

0364

0365

0366

0367

0368

0369

036A

036B

036C

036D

036E

036F

0370

0371

0372

0373

0374

0375

0376

0377

0378

0379

037A

037B

037C

037D

037E

037F

0380

0381

0382

0383

0384

0385

0386

0387

0388

0389

038A

038B

038C

038D

038E

038F

0390

0391

0392

0393

0394

0395

0396

0397

0398

0399

039A

039B

039C

039D

039E

039F

03A0

03A1

03A2

03A3

03A4

03A5

03A6

03A7

03A8

03A9

03AA

03AB

03AC

03AD

03AE

03AF

03B0

03B1

03B2

03B3

03B4

03B5

03B6

03B7

03B8

03B9

03BA

03BB

03BC

03BD

03BE

03BF

03C0

03C1

03C2

03C3

03C4

03C5

03C6

03C7

03C8

03C9

03CA

03CB

03CC

03CD

03CE

03CF

03D0

03D1

03D2

03D3

03D4

03D5

03D6

03D7

03D8

03D9

03DA

03DB

03DC

03DD

03DE

03DF

03E0

03E1

03E2

03E3

03E4

03E5

03E6

03E7

03E8

03E9

03EA

03EB

03EC

03ED

03EE

03EF

03F0

03F1

03F2

03F3

03F4

03F5

03F6

03F7

03F8

03F9

03FA

03FB

03FC

03FD

03FE

03FF

#### Plane 14 Glyphs

This table links to the two ranges of 256 assigned code points
 in Plane 14 (Tags and Variation Selector Supplement) that appear
 in theunifont_upperOpenType and TrueType font files.

 GNU Unifont Glyphs

Unicode Plane 14


0E00

0E01

#### Plane 0 and Plane 15 Private Use Area Glyphs

Finally, this last glyph table shows ConScript Unicode Registry (CSUR)
 and Under CSUR glyphs that appear in theunifont_csurOpenType
 and TrueType font files. Not all of the Plane 0 CSUR and UCSUR scripts
 have been drawn, but given the esoteric nature of some CSUR and UCSUR scripts
 (including the unavailability of glyph samples for many of the more obscure
 constructed scripts), the boxes in the table all have a green background color
 even if not at 100% coverage.

 GNU Unifont Glyphs

Private Use Area, Planes 0 and 15 — ConScript Unicode Registry


E0

E1

E2

E3

E4

E5

E6

E7

E8

E9

EA

EB

EC

ED

EE

EF

F0

F1

F2

F3

F4

F5

F6

F7

F8

Unicode Assigned Code Points

0F00

0F01

0F02

0F03

0F04

0F05

0F06

0F07

0F08

0F09

0F0A

0F0B

0F0C

0F0D

0F0E

0F0F

0F10

0F11

0F12

0F13

0F14

0F15

0F16

0F17

0F18

0F19

0F1A

0F1B

0F1C

0F1D

0F1E

0F1F

0F20

0F21

0F22

0F23

0F24

0F25

0F26

0F27

0F28

0F29

0F2A

0F2B

0F2C

0F2D

0F2E

0F2F

### Contributing Glyphs

If you would like to contribute glyphs to the GNU Unifont effort,
 you can download the associated PNG file from the tables above
 (SMP and CSUR need additions). Then draw new glyphs in the 16-by-16
 pixel area that is inside the inner box you see in the image on
 the left.

When done, erase the surrounding inner box and ruler lines around the
 inner box. You can then save the file as a monochrome bitmap image.
 Then convert the .png file into a .hex file with the unipng2hex utility
 in the source tarball. Or you can just email the .png file to me as
 a contribution to this effort and I will do the conversion.

Q: Why is the outer grid so much larger than the 16-by-16 pixel
 inner box?

A: Because in a future version, unipng2hex, unihex2png, and other
 utilities should be able to handle larger glyphs.

The table below shows the current state of completion of the Supplementary
 Multilingual Plane (Plane 1). Any range in the table that doesn't have
 a green background has missing glyphs. To see which scripts are in a
 particular range, consult the "Supplementary Multilingual Plane" list
 in the Current Coverage section below. The more red a range appears
 in the table below, the more glyphs are missing from that range.

### Current Coverage

Links in this section reference the first block of 256 glyphs
 where a script begins.

The list below shows the scripts that are in the Unicode
 Basic Multilingual Plane, with coverage in this release of Unifont.

 Covered Range Script
 ------- ----- ------
 100.0%
U+0000..U+007F
 C0 Controls and Basic Latin
 100.0%
U+0080..U+00FF
 C1 Controls and Latin-1 Supplement
 100.0%
U+0100..U+017F
 Latin Extended-A
 100.0%
U+0180..U+024F
 Latin Extended-B
 100.0%
U+0250..U+02AF
 IPA Extensions
 100.0%
U+02B0..U+02FF
 Spacing Modifier Letters
 100.0%
U+0300..U+036F
 Combining Diacritical Marks
 100.0%
U+0370..U+03FF
 Greek and Coptic
 100.0%
U+0400..U+04FF
 Cyrillic
 100.0%
U+0500..U+052F
 Cyrillic Supplement
 100.0%
U+0530..U+058F
 Armenian
 100.0%
U+0590..U+05FF
 Hebrew
 100.0%
U+0600..U+06FF
 Arabic
 100.0%
U+0700..U+074F
 Syriac
 100.0%
U+0750..U+077F
 Arabic Supplement
 100.0%
U+0780..U+07BF
 Thaana
 100.0%
U+07C0..U+07FF
 N'Ko
 100.0%
U+0800..U+083F
 Samaritan
 100.0%
U+0840..U+085F
 Mandaic
 100.0%
U+0860..U+086F
 Syriac Supplement
 100.0%
U+0870..U+089F
 Arabic Extended-B
 100.0%
U+08A0..U+08FF
 Arabic Extended-A
 100.0%
U+0900..U+097F
 Devanagari
 100.0%
U+0980..U+09FF
 Bengali
 100.0%
U+0A00..U+0A7F
 Gurmukhi
 100.0%
U+0A80..U+0AFF
 Gujarati
 100.0%
U+0B00..U+0B7F
 Oriya
 100.0%
U+0B80..U+0BFF
 Tamil
 100.0%
U+0C00..U+0C7F
 Telugu
 100.0%
U+0C80..U+0CFF
 Kannada
 100.0%
U+0D00..U+0D7F
 Malayalam
 100.0%
U+0D80..U+0DFF
 Sinhala
 100.0%
U+0E00..U+0E7F
 Thai
 100.0%
U+0E80..U+0EFF
 Lao
 100.0%
U+0F00..U+0FFF
 Tibetan
 100.0%
U+1000..U+109F
 Myanmar
 100.0%
U+10A0..U+10FF
 Georgian
 100.0%
U+1100..U+11FF
 Hangul Jamo
 100.0%
U+1200..U+137F
 Ethiopic
 100.0%
U+1380..U+139F
 Ethiopic Supplement
 100.0%
U+13A0..U+13FF
 Cherokee
 100.0%
U+1400..U+167F
 Unified Canadian Aboriginal Syllabics
 100.0%
U+1680..U+169F
 Ogham
 100.0%
U+16A0..U+16FF
 Runic
 100.0%
U+1700..U+171F
 Tagalog
 100.0%
U+1720..U+173F
 Hanunoo
 100.0%
U+1740..U+175F
 Buhid
 100.0%
U+1760..U+177F
 Tagbanwa
 100.0%
U+1780..U+17FF
 Khmer
 100.0%
U+1800..U+18AF
 Mongolian
 100.0%
U+18B0..U+18FF
 Unified Canadian Aboriginal Syllabics Extended
 100.0%
U+1900..U+194F
 Limbu
 100.0%
U+1950..U+197F
 Tai Le
 100.0%
U+1980..U+19DF
 New Tai Lue
 100.0%
U+19E0..U+19FF
 Khmer Symbols
 100.0%
U+1A00..U+1A1F
 Buginese
 100.0%
U+1A20..U+1AAF
 Tai Tham
 100.0%
U+1AB0..U+1AFF
 Combining Diacritical Marks Extended
 100.0%
U+1B00..U+1B7F
 Balinese
 100.0%
U+1B80..U+1BBF
 Sundanese
 100.0%
U+1BC0..U+1BFF
 Batak
 100.0%
U+1C00..U+1C4F
 Lepcha
 100.0%
U+1C50..U+1C7F
 Ol Chiki
 100.0%
U+1C80..U+1C8F
 Cyrillic Extended-C
 100.0%
U+1C90..U+1CBF
 Georgian Extended
 100.0%
U+1CC0..U+1CCF
 Sundanese Supplement
 100.0%
U+1CD0..U+1CFF
 Vedic Extensions
 100.0%
U+1D00..U+1D7F
 Phonetic Extensions
 100.0%
U+1D80..U+1DBF
 Phonetic Extensions Supplement
 100.0%
U+1DC0..U+1DFF
 Combining Diacritical Marks Supplement
 100.0%
U+1E00..U+1EFF
 Latin Extended Additional
 100.0%
U+1F00..U+1FFF
 Greek Extended
 100.0%
U+2000..U+206F
 General Punctuation
 100.0%
U+2070..U+209F
 Superscripts and Subscripts
 100.0%
U+20A0..U+20CF
 Currency Symbols
 100.0%
U+20D0..U+20FF
 Combining Diacritical Marks for Symbols
 100.0%
U+2100..U+214F
 Letterlike Symbols
 100.0%
U+2150..U+218F
 Number Forms
 100.0%
U+2190..U+21FF
 Arrows
 100.0%
U+2200..U+22FF
 Mathematical Operators
 100.0%
U+2300..U+23FF
 Miscellaneous Technical
 100.0%
U+2400..U+243F
 Control Pictures
 100.0%
U+2440..U+245F
 Optical Character Recognition
 100.0%
U+2460..U+24FF
 Enclosed Alphanumerics
 100.0%
U+2500..U+257F
 Box Drawing
 100.0%
U+2580..U+259F
 Block Elements
 100.0%
U+25A0..U+25FF
 Geometric Shapes
 100.0%
U+2600..U+26FF
 Miscellaneous Symbols
 100.0%
U+2700..U+27BF
 Dingbats
 100.0%
U+27C0..U+27EF
 Miscellaneous Mathematical Symbols-A
 100.0%
U+27F0..U+27FF
 Supplemental Arrows-A
 100.0%
U+2800..U+28FF
 Braille Patterns
 100.0%
U+2900..U+297F
 Supplemental Arrows-B
 100.0%
U+2980..U+29FF
 Miscellaneous Mathematical Symbols-B
 100.0%
U+2A00..U+2AFF
 Supplemental Mathematical Operators
 100.0%
U+2B00..U+2BFF
 Miscellaneous Symbols and Arrows
 100.0%
U+2C00..U+2C5F
 Glagolithic
 100.0%
U+2C60..U+2C7F
 Latin Extended-C
 100.0%
U+2C80..U+2CFF
 Coptic
 100.0%
U+2D00..U+2D2F
 Georgian Supplement
 100.0%
U+2D30..U+2D7F
 Tifinagh
 100.0%
U+2D80..U+2DDF
 Ethiopic Extended
 100.0%
U+2DE0..U+2DFF
 Cyrillic Extended-A
 100.0%
U+2E00..U+2E7F
 Supplemental Punctuation
 100.0%
U+2E80..U+2EFF
 CJK Radicals Supplement
 100.0%
U+2F00..U+2FDF
 Kangxi Radicals
 100.0%
U+2FE0..U+2FEF
 Unassigned
 100.0%
U+2FF0..U+2FFF
 Ideographic Description Characters
 100.0%
U+3000..U+303F
 CJK Symbols and Punctuation
 100.0%
U+3040..U+309F
 Hiragana
 100.0%
U+30A0..U+30FF
 Katakana
 100.0%
U+3100..U+312F
 Bopomofo
 100.0%
U+3130..U+318F
 Hangul Compatibility Jamo
 100.0%
U+3190..U+319F
 Kanbun
 100.0%
U+31A0..U+31BF
 Bopomofo Extended
 100.0%
U+31C0..U+31EF
 CJK Strokes
 100.0%
U+31F0..U+31FF
 Katakana Phonetic Extensions
 100.0%
U+3200..U+32FF
 Enclosed CJK Letters and Months
 100.0%
U+3300..U+33FF
 CJK Compatibility
 100.0%
U+3400..U+4DBF
 CJK Unified Ideographs Extension A
 100.0%
U+4DC0..U+4DFF
 Yijing Hexagram Symbols
 100.0%
U+4E00..U+9FFF
 CJK Unified Ideographs
 100.0%
U+A000..U+A48F
 Yi Syllables
 100.0%
U+A490..U+A4CF
 Yi Radicals
 100.0%
U+A4D0..U+A4FF
 Lisu
 100.0%
U+A500..U+A63F
 Vai
 100.0%
U+A640..U+A69F
 Cyrillic Extended-B
 100.0%
U+A6A0..U+A6FF
 Bamum
 100.0%
U+A700..U+A71F
 Modifier Tone Letters
 100.0%
U+A720..U+A7FF
 Latin Extended-D
 100.0%
U+A800..U+A82F
 Syloti Nagri
 100.0%
U+A830..U+A83F
 Common Indic Number Forms
 100.0%
U+A840..U+A87F
 Phags-pa
 100.0%
U+A880..U+A8DF
 Saurashtra
 100.0%
U+A8E0..U+A8FF
 Devanagari Extended
 100.0%
U+A900..U+A92F
 Kayah Li
 100.0%
U+A930..U+A95F
 Rejang
 100.0%
U+A960..U+A97F
 Hangul Jamo Extended-A
 100.0%
U+A980..U+A9DF
 Javanese
 100.0%
U+A9E0..U+A9FF
 Myanmar Extended-B
 100.0%
U+AA00..U+AA5F
 Cham
 100.0%
U+AA60..U+AA7F
 Myanmar Extended-A
 100.0%
U+AA80..U+AADF
 Tai Viet
 100.0%
U+AAE0..U+AAFF
 Meetei Mayek Extensions
 100.0%
U+AB00..U+AB2F
 Ethiopic Extended-A
 100.0%
U+AB30..U+AB6F
 Latin Extended-E
 100.0%
U+AB70..U+ABBF
 Cherokee Supplement
 100.0%
U+ABC0..U+ABFF
 Meetei Mayek
 100.0%
U+AC00..U+D7AF
 Hangul Syllables
 100.0%
U+D7B0..U+D7FF
 Hangul Jamo Extended-B
 0.0%
U+D800..U+DFFF
 Surrogate Pairs - Not Used
 0.0%
U+E000..U+F8FF
 Private Use Area - drawn but not included
 100.0%
U+F900..U+FAFF
 CJK Compatibility Ideographs
 100.0%
U+FB00..U+FB4F
 Alphabetic Presentation Forms
 100.0%
U+FB50..U+FDFF
 Arabic Presentation Forms-A
 100.0%
U+FE00..U+FE0F
 Variation Selectors
 100.0%
U+FE10..U+FE1F
 Vertical Forms
 100.0%
U+FE20..U+FE2F
 Combining Half Marks
 100.0%
U+FE30..U+FE4F
 CJK Compatibility Forms
 100.0%
U+FE50..U+FE6F
 Small Form Variants
 100.0%
U+FE70..U+FEFF
 Arabic Presentation Forms-B
 100.0%
U+FF00..U+FFEF
 Halfwidth and Fullwidth Forms
 100.0%
U+FFF0..U+FFFF
 Specials


The list below shows the scripts that are in the Unicode
 Supplementary Multilingual Plane, with coverage in this release of Unifont.
 Scripts labeled "(Pending)" are being drawn currently.

 Covered Range Script
 ------- ----- ------
 100.0%
U+010000..U+01007F
 Linear B Syllabary
 100.0%
U+010080..U+0100FF
 Linear B Ideograms
 100.0%
U+010100..U+01013F
 Aegean Numbers
 100.0%
U+010140..U+01018F
 Ancient Greek Numbers
 100.0%
U+010190..U+0101CF
 Ancient Symbols
 100.0%
U+0101D0..U+0101FF
 Phaistos Disc
 100.0%
U+010280..U+01029F
 Lycian
 100.0%
U+0102A0..U+0102DF
 Carian
 100.0%
U+0102E0..U+0102FF
 Coptic Epact Numbers
 100.0%
U+010300..U+01032F
 Old Italic
 100.0%
U+010330..U+01034F
 Gothic
 100.0%
U+010350..U+01037F
 Old Permic
 100.0%
U+010380..U+01039F
 Ugaritic
 100.0%
U+0103A0..U+0103DF
 Old Persian
 100.0%
U+010400..U+01044F
 Deseret
 100.0%
U+010450..U+01047F
 Shavian
 100.0%
U+010480..U+0104AF
 Osmanya
 100.0%
U+0104B0..U+0104FF
 Osage
 100.0%
U+010500..U+01052F
 Elbasan
 100.0%
U+010530..U+01056F
 Caucasian Albanian
 100.0%
U+010570..U+0105BF
 Vithkuqi
 100.0%
U+0105C0..U+0105FF
 Todhri
 100.0%
U+010600..U+01077F
 Linear A
 100.0%
U+010780..U+0107BF
 Latin Extended-F
 100.0%
U+010800..U+01083F
 Cypriot Syllabary
 100.0%
U+010840..U+01085F
 Imperial Aramaic
 100.0%
U+010860..U+01087F
 Palmyrene
 100.0%
U+010880..U+0108AF
 Nabataean
 100.0%
U+0108E0..U+0108FF
 Hatran
 100.0%
U+010900..U+01091F
 Phoenecian
 100.0%
U+010920..U+01093F
 Lydian
 100.0%
U+010940..U+01095F
 Sidetic
 100.0%
U+010980..U+01099F
 Meroitic Hieroglyphs
 100.0%
U+0109A0..U+0109FF
 Meroitic Cursive
 100.0%
U+010A00..U+010A5F
 Kharoshthi
 100.0%
U+010A60..U+010A7F
 Old South Arabian
 100.0%
U+010A80..U+010A9F
 Old North Arabian
 100.0%
U+010AC0..U+010AFF
 Manichaean
 100.0%
U+010B00..U+010B3F
 Avestan
 100.0%
U+010B40..U+010B5F
 Inscriptional Parthian
 100.0%
U+010B60..U+010B7F
 Inscriptional Pahlavi
 100.0%
U+010B80..U+010BAF
 Psalter Pahlavi
 100.0%
U+010C00..U+010C4F
 Old Turkic
 100.0%
U+010C80..U+010CFF
 Old Hungarian
 100.0%
U+010D00..U+010D3F
 Hanifi Rohingya
 100.0%
U+010D40..U+010D8F
 Garay
 100.0%
U+010E60..U+010E7F
 Rumi Numeral Symbols
 100.0%
U+010E80..U+010EBF
 Yezidi
 100.0%
U+010EC0..U+010EFF
 Arabic Extended-C
 100.0%
U+010F00..U+010F2F
 Old Sogdian
 100.0%
U+010F30..U+010F6F
 Sogdian
 100.0%
U+010F70..U+010FAF
 Old Uyghur
 100.0%
U+010FB0..U+010FDF
 Chorasmian
 100.0%
U+010FE0..U+010FFF
 Elymaic
 100.0%
U+011000..U+01107F
 Brahmi
 100.0%
U+011080..U+0110CF
 Kaithi
 100.0%
U+0110D0..U+0110FF
 Sora Sompeng
 100.0%
U+011100..U+01114F
 Chakma
 100.0%
U+011150..U+01117F
 Mahajani
 100.0%
U+011180..U+0111DF
 Sharada
 100.0%
U+0111E0..U+0111FF
 Sinhala Archaic Numbers
 100.0%
U+011200..U+01124F
 Khojki
 100.0%
U+011280..U+0112AF
 Multani
 100.0%
U+0112B0..U+0112FF
 Khudawadi
 100.0%
U+011300..U+01137F
 Grantha
 100.0%
U+011380..U+0113FF
 Tulu-Tigalari
 100.0%
U+011400..U+01147F
 Newa
 100.0%
U+011480..U+0114DF
 Tirhuta
 100.0%
U+011580..U+0115FF
 Siddham
 100.0%
U+011600..U+01165F
 Modi
 100.0%
U+011660..U+01167F
 Mongolian Supplement
 100.0%
U+011680..U+0116CF
 Takri
 100.0%
U+0116D0..U+0116FF
 Myanmar Extended-C
 100.0%
U+011700..U+01174F
 Ahom
 100.0%
U+011800..U+01184F
 Dogra
 100.0%
U+0118A0..U+0118FF
 Warang Citi
 100.0%
U+011900..U+01195F
 Dives Akuru
 100.0%
U+0119A0..U+0119FF
 Nandinagari
 100.0%
U+011A00..U+011A4F
 Zanabazar Square
 100.0%
U+011A50..U+011AAF
 Soyombo
 100.0%
U+011AB0..U+011ABF
 Unified Canadian Aboriginal Syllabics Extended-A
 100.0%
U+011AC0..U+011AFF
 Pau Cin Hau
 100.0%
U+011B60..U+011B7F
 Sharada Supplement
 100.0%
U+011BC0..U+011BFF
 Sunuwar
 100.0%
U+011C00..U+011C6F
 Bhaiksuki
 100.0%
U+011C70..U+011CBF
 Marchen
 100.0%
U+011D00..U+011D5F
 Masaram Gondi
 100.0%
U+011D60..U+011DAF
 Gunjala Gondi
 100.0%
U+011DB0..U+011DEF
 Tolong Siki
 100.0%
U+011EE0..U+011EFF
 Makasar
 100.0%
U+011F00..U+011F5F
 Kawi
 100.0%
U+011FC0..U+011FFF
 Tamil Supplement
 0.0%
U+012000..U+0123FF
 Cuneiform*
 0.0%
U+012400..U+01247F
 Cuneiform Numbers and Punctuation*
 0.0%
U+012480..U+01254F
 Early Dynastic Cuneiform*
 100.0%
U+012F90..U+012FFF
 Cypro-Minoan
 0.0%
U+013000..U+01342F
 Egyptian Hieroglyphs*
 100.0%
U+013430..U+01345F
 Egyptian Hieroglyph Format Controls
 0.0%
U+013460..U+0143FF
 Egyptian Hieroglyphics Extended-A
 0.0%
U+014400..U+01467F
 Anatolian Hieroglyphs*
 100.0%
U+016100..U+01613F
 Gurung Khema
 0.0%
U+016800..U+0168BF
 Bamum Supplement*
 100.0%
U+016A40..U+016A6F
 Mro
 100.0%
U+016A70..U+016ACF
 Tangsa
 100.0%
U+016AD0..U+016AFF
 Bassa Vah
 100.0%
U+016D40..U+016D7F
 Kirat Rai
 100.0%
U+016B00..U+016B8F
 Pahawh Hmong
 100.0%
U+016E40..U+016E9F
 Medefaidrin
 100.0%
U+016EA0..U+016EDF
 Beria Erfe
 100.0%
U+016F00..U+016F9F
 Miao
 100.0%
U+016FE0..U+016FFF
 Ideographic Symbols and Punctuation
 0.0%
U+017000..U+0187FF
 Tangut
 0.0%
U+018800..U+018AFF
 Tangut Components
 100.0%
U+018B00..U+018CFF
 Khitan Small Script
 0.0%
U+018D00..U+018D7F
 Tangut Supplement
 0.0%
U+018D80..U+018DFF
 Tangut Components Supplement
 100.0%
U+01AFF0..U+01AFFF
 Kana Extended-B
 100.0%
U+01B000..U+01B0FF
 Kana Supplement
 100.0%
U+01B100..U+01B12F
 Kana Extended-A
 100.0%
U+01B130..U+01B16F
 Small Kana Extension
 100.0%
U+01B170..U+01B2FF
 Nushu
 100.0%
U+01BC00..U+01BC9F
 Duployan
 100.0%
U+01BCA0..U+01BCAF
 Shorthand Format Controls
 100.0%
U+01CC00..U+01CEBF
 Symbols for Legacy Computing
 100.0%
U+01CEC0..U+01CEFF
 Miscellaneous Symbols Supplement
 100.0%
U+01CF00..U+01CFCF
 Znamenny Musical Notation
 100.0%
U+01D000..U+01D0FF
 Byzantine Musical Symbols
 100.0%
U+01D100..U+01D1FF
 Musical Symbols
 100.0%
U+01D200..U+01D24F
 Ancient Greek Musical Notation
 100.0%
U+01D2E0..U+01D2FF
 Mayan Numerals
 100.0%
U+01D300..U+01D35F
 Tai Xuan Jing Symbols
 100.0%
U+01D360..U+01D37F
 Counting Rod Numerals
 100.0%
U+01D400..U+01D7FF
 Mathematical Alphanumeric Symbols
 100.0%
U+01D800..U+01DAAF
 Sutton SignWriting
 100.0%
U+01DF00..U+01DFFF
 Latin Extended-G
 100.0%
U+01E000..U+01E02F
 Glagolitic Supplement
 100.0%
U+01E100..U+01E14F
 Nyiakeng Puachue Hmong
 100.0%
U+01E290..U+01E2BF
 Toto
 100.0%
U+01E2C0..U+01E2FF
 Wancho
 100.0%
U+01E5D0..U+01E5FF
 Ol Onal
 100.0%
U+01E6C0..U+01E6FF
 Tai Yo
 100.0%
U+01E7E0..U+01E7FF
 Ethiopic Extended-B
 100.0%
U+01E800..U+01E8DF
 Mende Kikakui
 100.0%
U+01E900..U+01E95F
 Adlam
 100.0%
U+01EC70..U+01ECBF
 Indic Siyaq Numbers
 100.0%
U+01ED00..U+01ED4F
 Ottoman Siyaq Numbers
 100.0%
U+01EE00..U+01EEFF
 Arabic Mathematical Alphabetic Symbols
 100.0%
U+01F000..U+01F02F
 Mahjong Tiles
 100.0%
U+01F030..U+01F09F
 Domino Tiles
 100.0%
U+01F0A0..U+01F0FF
 Playing Cards
 100.0%
U+01F100..U+01F1FF
 Enclosed Alphanumeric Supplement
 100.0%
U+01F200..U+01F2FF
 Enclosed Ideographic Supplement
 100.0%
U+01F300..U+01F5FF
 Miscellaneous Symbols and Pictographs
 100.0%
U+01F600..U+01F64F
 Emoticons
 100.0%
U+01F650..U+01F67F
 Ornamental Dingbats
 100.0%
U+01F680..U+01F6FF
 Transport and Map Symbols
 100.0%
U+01F700..U+01F77F
 Alchemical Symbols
 100.0%
U+01F780..U+01F7FF
 Geometric Shapes Extended
 100.0%
U+01F800..U+01F8FF
 Supplemental Arrows-C
 100.0%
U+01F900..U+01F9FF
 Supplemental Symbols and Pictographs
 100.0%
U+01FA00..U+01FA6F
 Chess Symbols
 100.0%
U+01FA70..U+01FAFF
 Symbols and Pictographs Extended-A
 100.0%
U+01FB00..U+01FBFF
 Symbols for Legacy Computing


*Note: Scripts such as Cuneiform, Egyptian
 Hieroglyphs, and Bamum Supplement will not be drawn on a 16-by-16
 pixel grid. There are plans to draw these scripts on a 32-by-32
 pixel grid in the future.

Plane 14 has two scripts, both of which Unifont covers:

 GNU Unifont Glyphs

Plane 14


 Range
Script

U+0E0000..U+0E007F

Tags

U+0E0100..U+0E01EF

Variations Selectors Supplement

The list below shows the scripts that are in Michael Everson's
 ConScript Unicode Registry (CSUR) and Rebecca Bettencourt's Under-CSUR
 that have coverage in this release of Unifont:

 GNU Unifont Glyphs

Private Use Area, Planes 0 and 15 — ConScript Unicode Registry


 Range
Script

U+E000..U+E07F

Tengwar

U+E080..U+E0FF

Cirth

U+E100..U+E14F

Engsvanyáli

U+E150..U+E1AF

Kinya

U+E1B0..U+E1CF

Ilianóre

U+E1D0..U+E1FF

Syai

U+E200..U+E26F

Verdurian

U+E280...U+E29F

aUI

U+E2A0...U+E2CF

Amman-iar

U+E2D0...U+E2FF

Xaîni

U+E300...U+E33F

Mizarian

U+E340...U+E35F

Zíirí:nka

U+E3B0...U+E3FF

Olaetyan

U+E400...U+E42F

Nísklôz

U+E430...U+E44F

Kazat ?Akkorou

U+E450...U+E46F

Kazvarad

U+E470...U+E48F

Zarkhánd

U+E490...U+E4BF

Røzhxh

U+E4C0...U+E4EF

Serivelna [Not Drawn]

U+E4F0...U+E4FF

Kelwathi

U+E500..U+E51F

Saklor

U+E520..U+E54F

Rynnan

U+E550..U+E57F

Alzetjan

U+E580..U+E59F

Telarasso

U+E5A0..U+E5BF

Ssûraki [Not Drawn]

U+E5C0..U+E5DF

Gargoyle

U+E5E0..U+E5FF

Ophidian

U+E630..U+E64F

Seussian Latin Extensions

U+E650..U+E67F

Sylabica

U+E680..U+E6CF

Ewellic

U+E6D0..U+E6EF

Amlin

U+E6F0..U+E6FF

Unifon Extended

U+E740..U+E76F

Unifon

U+E770..U+E77F

Solresol

U+E780..U+E7FF

Visible Speech

U+E800..U+E82F

Monofon

U+E830..U+E88F

D'ni

U+E890..U+E8DF

Aurebesh

U+E8E0..U+E8FF

Tonal

U+E900..U+E97F

Glaitha-A

U+E980..U+E9FF

Glaitha-B

U+EAA0..U+EAFF

Wanya

U+EB00..U+EB3F

Orokin

U+EB40..U+EB5F

Standard Galactic

U+EB60..U+EB9F

Braille Extended

U+EBA0..U+EBDF

Cistercian Numerals

U+EBE0..U+EBEF

Boby Lapointe's "bibi-binary" hexadecimal notation

U+EBF0..U+EBFF

Bruce Alan Martin's hexadecimal bit location notation

U+EC00..U+EC2F

Cylenian

U+EC30..U+EC6F

Syrrin

U+EC70..U+ECEF

Graflect

U+ECF0..U+ECFF

Ronald O. Whitaker's triangular hexadecimal notation

U+ED00..U+ED3F

Deini

U+ED40..U+ED5F

Niji

U+F4C0..U+F4EF

Ath

U+F8A0..U+F8CF

Aiha

U+F8D0..U+F8FF

Klingon

U+F0000..U+F00FF

U+F0100..U+F01FF

U+F0200..U+F02FF

U+F0300..U+F03FF

U+F0400..U+F04FF

U+F0500..U+F05FF

U+F0600..U+F06FF

U+F0700..U+F07FF

U+F0800..U+F08FF

U+F0900..U+F09FF

U+F0A00..U+F0AFF

U+F0B00..U+F0BFF

U+F0C00..U+F0CFF

U+F0D00..U+F0DFF

U+F0E00..U+F0E6F

Kinya Syllables

U+F0E70..U+F0EFF

U+F0F00..U+F0FFF

U+F1000..U+F10FF

U+F1100..U+F11E7

Pikto

U+F16B0..U+F16DF

Derani

U+F1900..U+F19FF

Sitelen Pona

U+F1B00..U+F1BFF

U+F1C00..U+F1C3F

Shidinn

U+F1C40..U+F1C7F

Titi Pula

U+F1C80..U+F1C9F

Sitelen Pona Radicals

U+F2000..U+F20FF

U+F2100..U+F21FF

U+F2200..U+F22FF

U+F2300..U+F23FF

U+F2400..U+F24FF

U+F2500..U+F25FF

U+F2600..U+F267F

Sadalian

U+F28A0..U+F28DF

Zbalermorna

Initially I just posted my additions toRoman Czyborra'soriginal
 unifont.hex file. Then in mid-January 2008, his website went down.
 So I started posting font updates here. Roman has encouraged me to continue
 with my additions.

Roman's website is now back online, and you can read his
 Unifont description and motivation for its creation on his website,
 along with his archive of Unifont's changes:http://czyborra.com/unifont.

### TrueType Font Generation

Luis Alejandro González Mirandawrote a cool combination of scripts to
 convert GNU Unifont from .hex format into FontForge .sfd format, then to
 have FontForge convert this to a TrueType outline font (see the Unicode
 Utilities web page on this site for more information). Pixels are drawn
 as outlined squares, so they scale to all point sizes. This works well with
 GNOME; I haven't tried it with any other Unix windowing environment.
 I've removed the OpenType SBIT font link from this page because the outline
 font is much more flexible.

Luis has given me permission to modify his scripts to convert the latest
 GNU Unifont versions to TrueType. I've modified his original scripts to
 handle Unicode combining characters.

### JIS X 0213 Kanji

#### Jiskan16

Unifont 12.1.02 added Japanese BDF and TrueType versions,unifont_jp. This replaced over 10,000 ideographs
 in the default Unifont font with Japanese kanji from the 16 × 16
 pixel Jiskan 16 font. The font is available in two files,
 corresponding to the two planes in JIS X 0213. Both files are
 in the public domain.

The comments in the BDF source font files (downloadable from theJapanese Fontspage) credit the following contributors (in order): Toshiyuki Imamura,
 HANATAKA Shinya, Taichi Kawabata, Koichi Yasuoka, TOYOSHIMA Masayuki,
 Kazuo Koike, and SATO Yasunao.

For the Unifont release, the glyphs from the two JIS X 0213 planes
 were converted into Unifont .hex files and mapped to code points
 in Unicode's Plane 0 and Plane 2 for Unifont. The result
 provides complete representation of the kanji in JIS X 0213 in a free
 Unicode font.

#### Izumi16

Unifont 12.1.03 replaced the Jiskan16 glyphs with the public domain
 Izumi16 glyphs. These provide improvements on the earlier Jiskan16
 glyphs.

### Wen Quan Yi: Spring of Letters
 (文泉驛 / 文泉驿)

The original Unifont CJK glyphs were replaced by new CJK glyphs from
 version 1.1 ofQianqian Fang'sUnibit font. The Unibit font
 began as a combination of the original GNU Unifont glyphs and a basic
 CJK bitmap font placed in the public domain by the People's Republic
 of China. It adopted GNU Unifont's scheme of 8x16 and 16x16
 glyphs. Qianqian Fang and many others then added about 10,000
 more glyphs.

Qianqian states in the Unibit distribution:"The entire CJK Unified Ideographics (U4E00-U9FA5) and CJK Unified
 Ideographics Extension A(U3400-U4DB5) blocks were replaced by
 high-quality glyphs from China National Standard GB19966-2005
 (public domain)."Wen Quan Yi volunteeers then edited thousands
 of these characters. Qianqian also drew the new 22 CJK ideographs
 in the range U+9FA6..U+9FBB that appear in GNU Unifont.

Wen Quan Yi (WQY) means "spring of letters," as in a spring of water.
 This is an interesting choice of words, as the British spelling of
 "font" is "fount" (but still pronounced "font"). See his website for
 more details:http://wqy.sourceforge.net/cgi-bin/enindex.cgi, or in Chinese athttp://wenq.org/wqy2/index.cgi.

The following code points in the latest unifont.hex file are
 taken from the WQY Unibit font (with my additions to complete the
 U+3000..U+33FF range, particularly the missing Hiragana, Katakana,
 and Kanji), including glyphs updated by the Wen Quan Yi volunteers
 and other modifications as part of the Unifont font:

* U+2E80..U+2EFF: CJK Radicals Supplement
* U+2F00..U+2FDF: Kangxi Radicals
* U+2FF0..U+2FFF: Ideographic Description Characters
* U+3000..U+303F: CJK Symbols and Punctuation
* U+31C0..U+31EF: CJK Strokes
* U+3200..U+32FF: Enclosed CJK Letters and Months
* U+3300..U+33FF: CJK Compatibility
* U+3400..U+4DBF: CJK Unified Ideographs Extension A
* U+4E00..U+9FBF: CJK Unified Ideographs
* U+F900..U+FAFF: CJK Compatibility Ideographs
* U+FF00..U+FF60: Fullwidth Forms of Roman Letters

Qianqian has given his okay to add these CJK glyphs from the
 Wen Quan Yi project into GNU Unifont. Likewise, I've told him
 to incorporate any glyphs he wants from my contributions to GNU
 Unifont into his Unibit font. In October 2020, Qianqian Fang also
 granted permission to apply the SIL Open Font License version 1.1
 to Wen Quan Yi glyphs in Unifont as a dual license.

### What's Next?

All of the glyphs in the Supplementary Multilingual Plane that could
 easily be drawn in a 16-by-16 pixel grid have been drawn as of the
 Unifont 9.0.01 release. There are no plans to draw Tangut.
 A number of ConScript Unicode Registry (CSUR) scripts remain to be drawn.
 If you are interested in contributing glyphs to this
 effort, please contact me. All new contributions must be licensed under
 the same license as the rest of Unifont (in a nutshell, GPL 2+ with the
 GNU font embedding exception and the SIL OFL 1.1).

With the great work done by contributors in providing ConScript Unicode
 Registry (CSUR) glyphs, they are available in font files that have
 "_csur" in their name.
