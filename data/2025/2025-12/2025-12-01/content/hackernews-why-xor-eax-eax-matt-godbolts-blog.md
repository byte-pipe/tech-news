---
title: Why xor eax, eax? — Matt Godbolt’s blog
url: https://xania.org/202512/01-xor-eax-eax
site_name: hackernews
fetched_at: '2025-12-01T19:10:02.000544'
original_url: https://xania.org/202512/01-xor-eax-eax
author: hasheddan
date: '2025-12-01'
description: Why do compilers love xor-ing registers so much?
---

## Why xor eax, eax?

Written by me, proof-read by an LLM.Details at end.

Inone of my talks on assembly, I show a list of the20 most executed instructionson an average x86 Linux desktop. All the usual culprits are there,mov,add,lea,sub,jmp,calland so on, but the surprise interloper isxor- “eXclusive OR”. In my 6502 hacking days, the presence of an exclusive OR was a sure-fire indicator you’d either found the encryption part of the code, or some kind of sprite routine. It’s surprising then, that a Linux machine just minding its own business, would be executing so many.

That is, until you remember that compilers love to emit axorwhen setting a register to zero:

We know that exclusive-OR-ing anything with itself generates zero, but whydoesthe compiler emit this sequence? Is it just showing off?

In the example above, I’ve compiled with-O2and enabledCompiler Explorer’s “Compile to binary object” so you can view the machine code that the CPU sees, specifically:

31 c0

xor

eax
,

eax

c3

ret

If you change GCC’s optimisation level down to-O1you’ll see:

b8 00 00 00 00

mov

eax
,

0x0

c3

ret

The much clearer, more intention-revealingmov eax, 0to set the EAX register to zero takes up five bytes, compared to the two of the exclusive OR. By using a slightly more obscure instruction, we save three bytes every time we need to set a register to zero, which is a pretty common operation. Saving bytes makes the program smaller, and makes more efficient use of the instruction cache.

It gets better though! Since this is averycommon operation, x86 CPUs spot this “zeroing idiom” early in the pipeline and can specifically optimise around it: the out-of-order tracking systems knows that the value of “eax” (or whichever register is being zeroed) does not depend on the previous value of eax, so it can allocate a fresh, dependency-free zero register renamer slot. And, having done thatit removes the operation from the execution queue- that is thexortakes zero execution cycles!1It’s essentially optimised out by the CPU!

You may wonder why you seexor eax, eaxbut neverxor rax, rax(the 64-bit version), even when returning along:

In this case, even thoughraxis needed to hold the full 64-bitlongresult, by writing toeax, we get a nice effect: Unlike other partial register writes, when writing to aneregister likeeax, the architecture zeros the top 32 bits for free. Soxor eax, eaxsets all 64 bits to zero.

Interestingly, when zeroing the “extended” numbered registers (liker8), GCC still uses thed(double width, ie 32-bit) variant:

Note how it’sxor r8d, r8d(the 32-bit variant) even though with the REX prefix (here45) it would be the same number of bytes toxor r8, r8the full width. Probably makes something easier in the compilers, as clang does this too.

xor eax, eaxsaves you code spaceandexecution time! Thanks compilers!

Seethe videothat accompanies this post.

This post is day 1 ofAdvent of Compiler Optimisations 2025,
a 25-day series exploring how compilers transform our code.

This post was written by a human (Matt Godbolt) and reviewed and proof-read by LLMs and humans.

Support Compiler Explorer onPatreonorGitHub,
or by buying CE products in theCompiler Explorer Shop.

1. It still has to retire, so some on-chip resources are still allocated to it.↩

Permalink

 Filed under:


Coding

AoCO2025

Posted at 06:00:00 CST on 1
st
 December 2025.

### About Matt Godbolt

Matt Godboltis a C++ developer living in Chicago.
 He works forHudson River Tradingon super fun but secret things.
 Follow him onMastodonorBluesky.

Copyright 2007-2025 Matt Godbolt.
 Unless otherwise stated, all content is licensed under theCreative Commons Attribution-Noncommercial 3.0 Unported License.
 This blog is powered by the MalcBlogSystem byMalcolm Rowe.Note:This is my personal website. The views expressed on
 these pages are mine alone and almost certainly not those of my employer.
