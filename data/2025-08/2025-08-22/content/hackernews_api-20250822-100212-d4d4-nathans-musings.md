---
title: D4D4 — Nathan's Musings
url: https://www.nmichaels.org/musings/d4d4/d4d4/
site_name: hackernews_api
fetched_at: '2025-08-22T10:02:12.175068'
original_url: https://www.nmichaels.org/musings/d4d4/d4d4/
author: csense
date: '2025-08-18'
description: D4D4
tags:
- hackernews
- trending
---

# D4D4¶

A co-worker of mine was looking at some disassembled ARM code the
other day, and discovered something weird. Lots ofd4d4instructions, scattered about. LLVM’s objdump says this is a relative
branch to-0x58. The weird part is that they were always
unreachable.

## Experiments¶

Here’s an example in a minimal reproducer I wrote:

00020100

<
one
>:

 20100: 4770 bx lr

 20102: d4d4 bmi 0x200ae <__dso_handle+0x100ae> @ imm = #-0x58

Thatbxlrright before thed4d4branches to the link
register. In other words, it returns. Here’s the C code that goes
with this function:

#include

"mod.h"

static

void

one
(
void
)

{


return
;

}

int

main
(
void
)

{


void

*
fn
;


fn

=

one
;


use_ptr
(
fn
);


return

0
;

}

Theuse_ptrfunction is declared inmod.h(defined inmod.c),
and what it does with the pointer is not important. You can see that
there’s a function calledone, and that function just
returns. Thusbxlrbeing the only thing. But why is there an
extrad4d4after it in the disassembled object code? My first
thought was that it was there for alignment. Of course, Thumb
instructions are 16 bits and maybe functions need to be 32-bit
aligned. Weird that it would use a branch to a real relative address
instead of a nop or something that would cause a fault, but let’s try
expanding the experiment.

code:

static

void

one
(
void
)

{


return
;

}

static

void

two
(
void
)

{


return
;

}

int

main
(
void
)

{


void

*
fn
;


fn

=

one
;


use_ptr
(
fn
);


fn

=

two
;


use_ptr
(
fn
);


return

0
;

}

And the disassembly:

000200f4

<
main
>:

 200f4: b580 push {r7, lr}

 200f6: 466f mov r7, sp

 200f8: 4803 ldr r0, [pc, #0xc] @ 0x20108 <main+0x14>

 200fa: f000 f80b bl 0x20114 <use_ptr> @ imm = #0x16

 200fe: 4803 ldr r0, [pc, #0xc] @ 0x2010c <main+0x18>

 20100: f000 f808 bl 0x20114 <use_ptr> @ imm = #0x10

 20104: 2000 movs r0, #0x0

 20106: bd80 pop {r7, pc}

 20108: 11 01 02 00 .word 0x00020111

 2010c: 13 01 02 00 .word 0x00020113

00020110

<
one
>:

 20110: 4770 bx lr

00020112

<
two
>:

 20112: 4770 bx lr

00020114

<
use_ptr
>:

 20114: 4770 bx lr

Not only does the compiler not feel the need to align functions to
32-bit boundaries, but adding a second single-instruction function
actually got rid of thed4d4entirely. And note howuse_ptr(I
made it just return also)doesn’thave ad4d4in it. Curious.

What happens if I go to 3 functions?

code:

00020124

<
one
>:

 20124: 4770 bx lr

00020126

<
two
>:

 20126: 4770 bx lr

00020128

<
three
>:

 20128: 4770 bx lr

 2012a: d4d4 bmi 0x200d6 <__dso_handle+0x100d6> @ imm = #-0x58

0002012c

<
use_ptr
>:

 2012c: 4770 bx lr

It’s back! But now only once. It seems like it aligns the end ofmain.oso thatmod.ocan start on a 32-bit boundary. Ok, maybe
this makes sense. So let’s take a look at the compiler’s output
directly. Here’smain.o:

00000028

<
one
>:

 28: 4770 bx lr

0000002a

<
two
>:

 2a: 4770 bx lr

0000002c

<
three
>:

 2c: 4770 bx lr

Oh, the compiler didn’t put that in at all, it must have been the
linker! So lld is rounding the end of an object file up to 32-bit
alignment using thisd4d4instruction. If that’s true, then
linking mod.o before main.o ought to move where thed4d4is.

000200e4

<
use_ptr
>:

 200e4: 4770 bx lr

 200e6: d4d4 bmi 0x20092 <__dso_handle+0x10092> @ imm = #-0x58

000200e8

<
main
>:

 200e8: b5d0 push {r4, r6, r7, lr}

 200ea: af02 add r7, sp, #0x8

 200ec: 4804 ldr r0, [pc, #0x10] @ 0x20100 <main+0x18>

 200ee: 4c05 ldr r4, [pc, #0x14] @ 0x20104 <main+0x1c>

 200f0: 47a0 blx r4

 200f2: 4805 ldr r0, [pc, #0x14] @ 0x20108 <main+0x20>

 200f4: 47a0 blx r4

 200f6: 4805 ldr r0, [pc, #0x14] @ 0x2010c <main+0x24>

 200f8: 47a0 blx r4

 200fa: 2000 movs r0, #0x0

 200fc: bdd0 pop {r4, r6, r7, pc}

 200fe: bf00 nop

 20100: 11 01 02 00 .word 0x00020111

 20104: e5 00 02 00 .word 0x000200e5

 20108: 13 01 02 00 .word 0x00020113

 2010c: 15 01 02 00 .word 0x00020115

00020110

<
one
>:

 20110: 4770 bx lr

00020112

<
two
>:

 20112: 4770 bx lr

00020114

<
three
>:

 20114: 4770 bx lr

It did! The extra instruction got moved up to align the beginning of
the object code that contains main!

One more check: if I use the GNU linker, does it do the same thing?

00008000

<
use_ptr
>:

 8000: 4770 bx lr

 8002: 0000 movs r0, r0

No! GNU ld (2.44) inserts zeroes to align files. It’s notnop,
though it may as well be. ARMv7-M actually has anopinstruction:bf00orf3af8000depending on encoding. You can see it in
main, inserted by the compiler between the end of the function and its
constants.

## Conclusion¶

So now we know. LLD is inserting the weirdd4d4instructions, and
it’s doing it to align across object file boundaries. Why did they
pick such a weird constant, though? GNU ld went with zeroes, which
seems benign.

## Research¶

A little bit of checking outthe codelater, and we find this in
ARM.cpp:

trapInstr

=

{
0xd4
,

0xd4
,

0xd4
,

0xd4
};

That was actually way easier than I was expecting. The git blame path
meanders a little before getting tothis commitwhere Rui Ueyama explains:

Add trap instructions for ARM and MIPS.

This patch fills holes in executable sections with 0xd4 (ARM) or
0xef (MIPS). These trap instructions were suggested by Theo de Raadt.

llvm-svn: 306322

This appears to have been precipitated bythis message,
also from Rui Ueyama, to the llvm-bugs mailing list. In it, the
question is asked whether LLD should use a trap instruction for
ARM/AArch64 like x86 and x86-64’s0xCC. I didn’t find any replies,
though.

I couldn’t find any messages on the mailing list about this from Theo
de Raadt, so I guess we just have to live with Ueyama’s testimony that
he thought0xd4would be a good byte to repeat as a trap
instruction. But a trap instruction is supposed to halt the processor,
so what’s with the disassembler saying it’s a branch?

## RTFM¶

Let’s take a look at the ARMv7-M Architecture Reference Manual, theARM. First
of all, it says that we’re using the Thumb instruction set, and most
instructions are 16 bits. Any instructions that begin with0b11101,0b11110, or0b11111are the beginnings of 32-bit
instructions, but all the rest are 16 bits. Sinced4is0b11010100, we can safely assume that the instruction decoder will
always treat it like a 16-bit instruction.

Next up, we have table A5-1, showing how 16-bit instructions are
encoded. The first 6 bits are the opcode, followed by 10 bits of other
stuff. As we established earlier, the bits we’re looking for are0b110101. That matchesconditional branch and supervisor call’s0b1101xx. Well, so far it’s still looking like a branch..

Page A5-134 leads us to the statement that the encoding here is0b1101followed by a 4 bit opcode.0xdis the0b1101and
the next 4 bits are the number 4:0b0100. This doesn’t matchUDF, which seems like a reasonable choice for this
purpose. Instead, any opcode not matching111xis a conditional
branch, explained underBon page A7-207, according to table A5-8.

This page tells us that theBinstruction has several encodings,
but only one that begins with a0xd: T1.

With0xd4d4,condin this table is0x4or0b0100. That
doesn’t match UDF (again) orSVC.InITBlock()just checks if
we’re within 4 instructions of anIT.ITis a weird
instruction, but not important for our purposes. What’s important is
thatimm32is now those least significant 8 bits, sign
extended. That’s0xffffffd4, or-44. That’s-0x2cin hex,
not the-0x58from objdump. However, immediate offsets count
half-words, not bytes. So the offset is-88, or-0x58.

The other field,cond, is0b0100, which means some bits in the
condition registers have to be set in order for the branch to be
taken. Which bits don’t particularly matter, since this code is
supposed to be unreachable, but for completeness, it’s(ASPR.C=='1')&&(ASPR.Z=='0').

## More Conclusions¶

So it looks to me like objdump is behaving correctly, and Theo’s
suggestion was a bad one, at least for Thumb. Instead of a trap, it’s
a relative jump. In the tiny program I made above, it jumps right out
of.text, but in a more substantial program, it will usually land
somewhere in code. It should be unreachable, but the whole point of a
trap instruction is to halt the processor, not send it off on a random
walk through your codebase.

This feels like a bug in LLD to me. The linker’s inserting something
called “trapInstr” but it’s nothing like a trap. In fact, it’s a
(conditional) jump to a constant relative address.

So after a fun night of spelunking through source code, commit logs,
and manuals, I feel like I’ve learned something. I guess maybe it’s
time to file a bug report.
