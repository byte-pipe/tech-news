---
title: '[BUG] bionic: wcscspn()/wcspbrk() treat every wchar_t >= 0x100 as a match (Android 17, CP3A.260905.009) · Issue #2260 · android/ndk · GitHub'
url: https://github.com/android/ndk/issues/2260
site_name: hackernews_api
content_file: hackernews_api-bug-bionic-wcscspnwcspbrk-treat-every-wchar_t-0x10
fetched_at: '2026-10-14T15:44:19.885378'
original_url: https://github.com/android/ndk/issues/2260
author: tharen
date: '2026-10-14'
description: Description On Android 17 builds from September 2026, wcscspn() and wcspbrk() stop at the first character of the string that is >= U+0100 whenever the reject set has two or more characters that are all < U+0100. The character is reported...
tags:
- hackernews
- trending
---

# [BUG] bionic: wcscspn()/wcspbrk() treat every wchar_t >= 0x100 as a match (Android 17, CP3A.260905.009)#2260

Open
Open
[BUG] bionic: wcscspn()/wcspbrk() treat every wchar_t >= 0x100 as a match (Android 17, CP3A.260905.009)
#2260
Labels
bug

## Description

francisdb
opened 
on Oct 12, 2026
Issue body actions

### Description

On Android 17 builds from September 2026,wcscspn()andwcspbrk()stop at the first character of the string that is >= U+0100 whenever the reject set has two or more characters that are all < U+0100. The character is reported as a match even though it is not in the set.wcsspn(),wcschr(),wcsrchr(),wmemchr()andwcsstr()are correct.

Any code that scans wide strings for ASCII delimiters, for example newline or wildcard characters, breaks as soon as the text contains an emoji, CJK, Cyrillic, Greek or Latin Extended character.

## Affected / unaffected

Device

Build

Result

Pixel 7

google/panther/panther:17/CP3A.260905.009/16091614:user/release-keys

broken

Pixel 8a

google/akita/akita:17/CP3A.260905.009/16091614:user/release-keys (patch 2026-09-05)

broken

Nothing Phone 2

Nothing/PongEEA/Pong:16/BQ2A.250721.001-BP2A.250605.031.A3 (patch 2026-08-01)

ok

The public android17-release sources (android-17.0.0_r1, June 2026) buildwcscspn/wcspbrkfrom external/llvm-libc, which is a plain nested loop overwchar_tand is correct. The code on the September builds is different (see "Mechanism"), so the regression was introduced between the June and September releases.

## Reproducer

Build with the NDK (aarch64-linux-android30-clang), push to/data/local/tmp, run withadb shell:

#include
 
<stdio.h>

#include
 
<wchar.h>

int
 
main
(
void
)
{
 
wchar_t
 
s
[] 
=
 {
'a'
, 
0x1F680
, 
0x100
, 
'b'
, 
'x'
, 
'\n'
, 
0
};
 
printf
(
"wcscspn(s, L\"x\\n\") = %zu (expected 4)\n"
, 
wcscspn
(
s
, 
L"x\n"
));
 
printf
(
"wcspbrk(s, L\"x\\n\") = index %ld (expected 4)\n"
, (
long
)(
wcspbrk
(
s
, 
L"x\n"
) 
-
 
s
));
 
printf
(
"wcsspn(s, L\"a\\U0001F680\") = %zu (expected 2)\n"
, 
wcsspn
(
s
, 
L"a\U0001F680"
));
 
return
 
0
;
}

Output on CP3A.260905.009:

wcscspn(s, L"x\n") = 1 (expected 4)
wcspbrk(s, L"x\n") = index 1 (expected 4)
wcsspn(s, L"a\U0001F680") = 2 (expected 2)

A sweep of every code point from U+0001 to U+10FFFF (skipping surrogates and the two set members) withwcscspn(L"<cp>\n", L"x\n")returns 0 instead of 1 for 1,111,808 code points: every one from U+0100 to U+10FFFF. U+0001 to U+00FF are correct.

Which set shapes trigger it (all measured on the Pixel 8a):

Reject set

Result

one character

ok

two or more characters, all < U+0100 (e.g. 
L"x\n"
, 
L"\xe9\n"
)

broken

two or more characters, at least one >= U+0100

ok

haystack limited to U+0080..U+00FF

ok

## Mechanism (from the shipped libc.so)

Disassembly ofwcscspnin/apex/com.android.runtime/lib64/bionic/libc.soon CP3A.260905.009 shows three paths selected by the set:

1. One character: a plain compare loop. Correct.
2. Two or more characters: a 256-bytebooltable on the stack is filled from the set while the set characters are in 1..0xFF. If a set character >= 0x100 is seen, the function falls back to callingwcschr()for each haystack character. Correct.
3. Otherwise the haystack is scanned against the table:

a2564: ldrb w8, [x9, x8] ; table[c]
a2568: tbnz w8, #0, a2578 ; in set -> stop (correct)
a256c: ldr w8, [x22, #0x4]! ; next character
a2570: cmp w8, #0x100
a2574: b.lo a2564 ; c < 0x100 -> keep scanning
a2578: ... ; c >= 0x100 -> STOP, reported as a match

A character >= 0x100 cannot be in a set whose members are all < 0x100, so forwcscspnthe scan must continue past it. The code stops instead.wcsspnhas the same structure, and there stopping is the correct answer (the character is not in the keep set), which is why only the complement functions are wrong.wcspbrkis implemented on top of this scan and inherits the bug.

The existing bionic testTEST(wchar, wcspbrk)in tests/wchar_test.cpp only uses ASCII input, so it does not catch this. A test such asEXPECT_EQ(3u, wcscspn(L"aĀb\n", L"x\n"))would.

## Real-world impact

Visual Pinball on Android (libwinevbs, a Unix build of Wine's vbscript engine) stopped loading any table whose VBScript source contains a comment with an emoji after the September update: the lexer useswcspbrk(ptr, L"\n\r")to skip comments, got the position of the first emoji instead of the line end, and reported "Invalid character".FileSystem.MoveFolderlikewise treated every path containing a character >= U+0100 as a wildcard pattern viawcspbrk(src, L"*?><").

Worked around downstream by replacing the calls with plain loops:vpinball/libwinevbs#41(shipped invpinball/vpinball@e7837322f4).

Full disassembly of the affected functions and the probe sources are available on request.

### I am using a supported NDK

* I have checked and the NDK I'm using is currently supported

### Affected versions

r29

Reactions are currently unavailable

## Metadata

## Metadata