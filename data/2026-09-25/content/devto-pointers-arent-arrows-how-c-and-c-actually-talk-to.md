---
title: Pointers Aren't Arrows. How C and C++ Actually Talk to Hardware. - DEV Community
url: https://dev.to/smtahosin/pointers-arent-arrows-how-c-and-c-actually-talk-to-hardware-9d6
site_name: devto
content_file: devto-pointers-arent-arrows-how-c-and-c-actually-talk-to
fetched_at: '2026-09-25T21:59:48.359834'
original_url: https://dev.to/smtahosin/pointers-arent-arrows-how-c-and-c-actually-talk-to-hardware-9d6
author: S M Tahosin
date: '2026-09-25'
description: A visual, beginner-friendly guide to memory addresses, pointer arithmetic, and what happens when your code touches physical silicon. Discover why pointers are just numbers, why arrays decay, and what a Segmentation Fault really means. Tagged with cpp, c, programming, discuss.
tags: '#discuss, #cpp, #c, #programming'
---

Ask any software engineer to draw a pointer on a whiteboard.

Within three seconds, they will sketch two boxes and a little curved arrow pointing between them.

It looks neat. It feels intuitive. Computer science lectures have used that exact drawing for four decades.

And yet, that single diagram is why so many developers hit a psychological brick wall when learning C or C++.

Arrows don't exist inside your computer.

There is no wire inside your CPU labeled "arrow." There is no register that stores "direction." When you draw an arrow, you hide the one fundamental truth that makes low-level programming click:

A pointer is just an ordinary integer holding a street address.

The moment you discard the arrow and look at your computer through the eyes of the silicon, everything that felt terrifying about C and C++ suddenly turns simple. Pointer arithmetic stops looking like dark magic. Array decay makes total sense. And even the dreaded Segmentation Fault transforms from a random nightmare into a protective feature of your operating system.

Let us open the machine and see how C and C++ actually touch hardware.

## The Memory Street: What RAM Actually Looks Like

Forget about files, variables, and objects for a moment.

To your CPU, system memory (RAM) is nothing more than one gigantic, continuous street of numbered byte lockers.

Every locker holds exactlyone byte(8 bits).

And every single locker has a sequential house number. That house number is what we call anaddress.

Locker Address: 0x1000 0x1001 0x1002 0x1003 0x1004 0x1005
Stored Value: [ 0x2A ] [ 0x00 ] [ 0x00 ] [ 0x00 ] [ 0x48 ] [ 0x69 ]

Enter fullscreen mode

Exit fullscreen mode

When you write a normal variable in C:

int
 
score
 
=
 
42
;

Enter fullscreen mode

Exit fullscreen mode

The compiler does not build a box labeled "score."

Instead, it reserves 4 consecutive byte lockers (because a 32-bitintneeds 4 bytes), writes 42 in binary into those lockers, and records in its internal symbol table:

Whenever this programmer writesscore, look up locker number0x1000.

The namescoreexists only for human readability. Once your code compiles into machine instructions, the name disappears forever. The CPU only ever sees numeric addresses.

## Shattering the Arrow Lie

Now introduce a pointer:

int
 
score
 
=
 
42
;

int
*
 
ptr
 
=
 
&
score
;

Enter fullscreen mode

Exit fullscreen mode

The ampersand&is the address-of operator. It simply asks:"What is the house number where score lives?"

Ifscorelives at address0x1000, then&scoreevaluates to the number0x1000.

ptris a variable just like any other. It needs space to live. The compiler reserves lockers for it at address0x2000.

What value does the compiler store insideptr?

It stores the number0x1000. That is all. Nothing more, nothing less.

On a modern 64-bit operating system, every address is 64 bits wide (8 bytes). That meansevery pointer variable occupies exactly 8 bytes of memory, regardless of what type it points to.

You can verify this in your terminal:

#include
 
<stdio.h>

struct
 
HugePayload
 
{

 
char
 
data
[
10000
];

};

int
 
main
(
void
)
 
{

 
char
*
 
c_ptr
;

 
int
*
 
i_ptr
;

 
struct
 
HugePayload
*
 
struct_ptr
;

 
printf
(
"char* size: %zu bytes
\n
"
,
 
sizeof
(
c_ptr
));

 
printf
(
"int* size: %zu bytes
\n
"
,
 
sizeof
(
i_ptr
));

 
printf
(
"struct* size: %zu bytes
\n
"
,
 
sizeof
(
struct_ptr
));

 
return
 
0
;

}

Enter fullscreen mode

Exit fullscreen mode

Output:

char* size: 8 bytes
int* size: 8 bytes
struct* size: 8 bytes

Enter fullscreen mode

Exit fullscreen mode

If a pointer was an arrow, pointing to a 10,000-byte struct might require a bigger arrow than pointing to a 1-byte char.

In reality, a house number is always the same length, whether the house is a tiny studio apartment or a sprawling warehouse. It is just an address.

Dereferencing (*ptr) simply tells the CPU:

Read the house number stored insideptr(0x1000). Go to locker0x1000. Read or write the bytes living there.

## Whyptr + 1Doesn't Add One (Pointer Arithmetic)

Look at this common beginner surprise:

int
 
numbers
[
3
]
 
=
 
{
10
,
 
20
,
 
30
};

int
*
 
p
 
=
 
&
numbers
[
0
];

printf
(
"Before: %p
\n
"
,
 
(
void
*
)
p
);

p
 
=
 
p
 
+
 
1
;

printf
(
"After: %p
\n
"
,
 
(
void
*
)
p
);

Enter fullscreen mode

Exit fullscreen mode

You might expect adding1to increment the address by 1. But run it:

Before: 0x1000
After: 0x1004

Enter fullscreen mode

Exit fullscreen mode

It skipped 4 bytes.

Why? Because the compiler knowspis anint*. Anintoccupies 4 bytes.

Ifp + 1moved forward by only 1 byte,pwould point into the middle of the integer's binary representation, reading corrupted data.

During pointer arithmetic, the compiler scales every step by the size of the underlying type:

Destination
 
Address
 
=
 
Current
 
Address
 
+
 
(
Step
 
*
 
sizeof
(
*
p
))

Enter fullscreen mode

Exit fullscreen mode

* Forchar*(1 byte),p + 1moves forward by 1 byte.
* Forint*(4 bytes),p + 1moves forward by 4 bytes.
* Fordouble*(8 bytes),p + 1moves forward by 8 bytes.

This explains why arithmetic on avoid*is disallowed in standard ISO C. Becausevoidhas no defined size, the compiler cannot calculate how many bytes to step forward down the street.

## The Array Decay Shock: Whyarr[i]Equalsi[arr]

In languages like JavaScript or Java, an array is an object with methods and length properties.

In C and C++,an array has zero runtime metadata.

An array is simply a contiguous strip of byte lockers sitting side by side.

When you declare:

int
 
arr
[
4
]
 
=
 
{
10
,
 
20
,
 
30
,
 
40
};

Enter fullscreen mode

Exit fullscreen mode

The compiler places four 4-byte integers consecutively:0x1000,0x1004,0x1008, and0x100C.

In the C specification, the bracket syntaxarr[i]is defined as:

arr
[
i
]
 
is
 
identical
 
to
:
 
*
(
arr
 
+
 
i
)

Enter fullscreen mode

Exit fullscreen mode

The brackets are just syntactic sugar for pointer arithmetic and dereferencing.

Because addition is commutative (a + b == b + a),*(arr + 2)is identical to*(2 + arr).

And since*(arr + 2)is written asarr[2], then*(2 + arr)can be written as2[arr].

#include
 
<stdio.h>

int
 
main
(
void
)
 
{

 
int
 
arr
[
4
]
 
=
 
{
10
,
 
20
,
 
30
,
 
40
};

 
printf
(
"arr[2] = %d
\n
"
,
 
arr
[
2
]);

 
printf
(
"*(arr+2) = %d
\n
"
,
 
*
(
arr
 
+
 
2
));

 
printf
(
"2[arr] = %d
\n
"
,
 
2
[
arr
]);

 
return
 
0
;

}

Enter fullscreen mode

Exit fullscreen mode

Output:

arr
[
2
]
 
=
 
30

*
(
arr
+
2
)
 
=
 
30

2
[
arr
]
 
=
 
30

Enter fullscreen mode

Exit fullscreen mode

Do not write2[arr]in production code, but understanding why it works clarifies the architecture: in C, arrays don't have magical lookup engines. There are only base addresses, offsets, and byte fetches.

## Stack vs. Heap: Physical Reality Inside Your RAM

Where do these street addresses come from?

When your program launches, the operating system assigns it a virtual memory territory divided into two primary working zones:The StackandThe Heap.

### The Stack: A Single CPU Register

The stack is fast because it requires almost no bookkeeping.

Your CPU has a dedicated hardware register calledRSP(Stack Pointer on x86_64).

When you call a function with local variables:

void
 
calculate
(
void
)
 
{

 
int
 
a
 
=
 
10
;

 
int
 
b
 
=
 
20
;

}

Enter fullscreen mode

Exit fullscreen mode

The CPU executes a single assembly instruction:

sub rsp, 16

Enter fullscreen mode

Exit fullscreen mode

In less than a nanosecond, the stack pointer moves down by 16 bytes. That newly opened space belongs toaandb.

When the function exits:

add rsp, 16
ret

Enter fullscreen mode

Exit fullscreen mode

The stack pointer slides back up. Deallocation is instant.

Notice:the CPU never cleared those memory bytes.They still sit in the lockers. The stack pointer simply moved past them. The next function called will overwrite them. This is why uninitialized local variables in C hold random garbage data.

### The Heap: The Dynamic Warehouse

When data must outlive the function that created it, or when its size is only known at runtime, you allocate from the Heap:

int
*
 
buffer
 
=
 
(
int
*
)
malloc
(
1024
 
*
 
sizeof
(
int
));

Enter fullscreen mode

Exit fullscreen mode

malloccannot just subtract a register. The heap allocator (like glibc's ptmalloc) searches linked lists of free memory bins for a suitable block. If it runs out of pre-allocated space, it issues a kernel system call (brkormmap) to expand its boundary.

When finished, you release the block:

free
(
buffer
);

Enter fullscreen mode

Exit fullscreen mode

### The Dangling Pointer Trap

What happens when you callfree(buffer)?

1. The allocator marks that memory block as available for future allocations.
2. It does NOT touch thebuffervariable.
3. It does NOT erase the bytes in memory.

bufferstill holds the old address. If you access*bufferlater, you trigger aUse-After-Freebug. Another thread or function may have received that address, meaning you will read or overwrite someone else's live data.

The fix is immediate:

free
(
buffer
);

buffer
 
=
 
NULL
;

Enter fullscreen mode

Exit fullscreen mode

## What Actually Happens During a Segmentation Fault?

Consider the classic crash:

int
*
 
ptr
 
=
 
NULL
;

*
ptr
 
=
 
100
;

Enter fullscreen mode

Exit fullscreen mode

Your program immediately halts with:

Segmentation fault (core dumped)

Enter fullscreen mode

Exit fullscreen mode

What actually happened in the machine during that millisecond?

Your code did not break physical RAM. Your pointer never touched physical RAM in the first place.

### The Hardware Guardian: The MMU

Modern operating systems never expose raw physical memory directly to applications. Instead, they useVirtual Memory.

Between your CPU core and physical memory sits theMMU(Memory Management Unit).

Memory is organized into 4KB pages. The operating system maintains aPage Tablethat maps virtual pages to physical RAM frames:

* Virtual page0x1000maps to Physical RAM0x8A40(Read/Write).
* Virtual page0x0000(NULL) isUnmapped(No access allowed).

When you execute*ptr = 100withptr = NULL:

1. The CPU sends address0x0to the MMU.
2. The MMU looks up0x0in the Page Table and finds no valid mapping.
3. The MMU blocks the write and triggers aHardware Page Fault Exception(CPU Interrupt 14).
4. The CPU pauses your program and transfers control to the OS kernel.
5. The kernel identifies the violation and sends signal 11 (SIGSEGV) to your process.
6. With no custom signal handler registered, the OS terminates the process to protect system stability.

A Segmentation Fault is not a computer malfunction. It is your operating system's security barrier actively preventing illegal memory corruption.

## Double Pointers: Demystifying**ptr

Double pointers (char**,int**) often confuse learners because people try to visualize stacked arrows.

Use the street address model instead:

* A regular variable holds data (val = 42).
* A single pointer (ptr) holds the house number of data (0x1000).
* A double pointer (pptr) holds the house number of another pointer variable (0x2000).

int
 
val
 
=
 
99
;
 
// Address 0x1000: holds 99

int
*
 
ptr
 
=
 
&
val
;
 
// Address 0x2000: holds 0x1000

int
**
 
pptr
 
=
 
&
ptr
;
 
// Address 0x3000: holds 0x2000

Enter fullscreen mode

Exit fullscreen mode

Why do we need this?

Because C passes all arguments by value (copying them).

If you want a function to modify an integer in the caller, you pass its address (int*).

Similarly, if you want a function to allocate memory and modify apointerin the caller, you must pass the pointer's address (int**):

void
 
allocate_memory
(
int
**
 
p
)
 
{

 
*
p
 
=
 
(
int
*
)
malloc
(
sizeof
(
int
));
 
// Modifies the caller's pointer variable

}

int
 
main
(
void
)
 
{

 
int
*
 
data
 
=
 
NULL
;

 
allocate_memory
(
&
data
);
 
// Pass address of data

 
*
data
 
=
 
42
;

 
free
(
data
);

 
return
 
0
;

}

Enter fullscreen mode

Exit fullscreen mode

When you see**p, don't think about arrows. Think:"I am receiving the address of a pointer so I can rewrite where it points."

## Practical Mental Model: The Survival Cheat Sheet

Syntax / Concept

The Arrow Lie

The Hardware Reality

int* ptr

A line pointing to an integer

An 8-byte variable storing a memory address

&x

Drawing an arrow

Extracting the numeric locker number of 
x

*ptr

Following the arrow

Telling the CPU to read or write bytes at that address

ptr + 1

Advancing one box

address + (1 * sizeof(*ptr))
 bytes forward in RAM

arr[i]

Array lookup

Shorthand for 
*(arr + i)
. Direct address offset.

free(ptr)

Wiping data

Returning the address reservation to the heap manager

NULL
 (
nullptr
)

Empty space

Address 
0x0
. Guaranteed unmapped to trigger an MMU trap

Segfault

Program glitch

Hardware MMU exception caught by the OS for illegal access

## The Shift That Makes Everything Click

High-level languages like Python and JavaScript provide garbage collection and abstraction to protect developers from raw memory. That convenience is valuable, but it obscures how computers work at the silicon level.

C and C++ strip away that insulation and hand you direct control of the memory bus.

Pointers are not mysterious entities or floating arrows. They are simply the numeric coordinates your computer uses every microsecond to execute software.

Once you picture memory as a numbered street of byte lockers, pointer arithmetic, array decay, and memory allocation all fall into place. You write cleaner code, avoid subtle memory corruption bugs, and truly understand the hardware beneath your programs.

If you have ever wrestled with a baffling segfault or a pointer bug in C or C++, what was the bug, and what was the moment that finally made pointers click for you?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse