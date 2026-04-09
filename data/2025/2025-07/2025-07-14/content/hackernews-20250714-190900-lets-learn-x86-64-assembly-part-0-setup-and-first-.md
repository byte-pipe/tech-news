---
title: Let's Learn x86-64 Assembly! Part 0 - Setup and First Steps
url: https://gpfault.net/posts/asm-tut-0.txt.html
site_name: hackernews
fetched_at: '2025-07-14T19:09:00.892827'
original_url: https://gpfault.net/posts/asm-tut-0.txt.html
author: 90s_dev
date: '2025-07-14'
---

# Let's Learn x86-64 Assembly! Part 0 - Setup and First Steps

published on Apr 18 2020

The way I was taught x86 assembly at the university had been completely outdated for many years by the time I had my first class. It was around 2008 or 2009, and 64-bit processors had already started becoming a thing even in my neck of the woods. Meanwhile, we were doing DOS, real-mode, memory segmentation and all the other stuff from the bad old days.

Nevertheless, I picked up enough of it during the classes (and over the subsequent years) to be able to understand the stuff coming out of the other end of a compiler, and that has helped me a few times. However, I've never manually written any substantial amount of x86 assembly for something non-trivial. Due to being locked up inside (on account of a global pandemic), I decided to change that situation, to pass the time.

I wanted to focus on x86-64 specifically, and completely forget/skip any and all legacy crap that is no longer relevant for this architecture. After getting a bit deeper into it, I also decided to publish my notes in the form of tutorials on this blog since there seems to be a desire for this type of content.

Everything I write in these posts will be a normal, 64-bit, Windows program. We'll be using Windows because that is the OS I'm running on all of my non-work machines, and when you drop down to the level of writing assembly it starts becoming incresingly impossible to ignore the operating system you're running on. I will also try to go as "from scratch" as possible - no libraries, we're only allowed to call out to the operating system and that's it.

In this first, introductory part (yeah, I'm planning a series and I know I will regret this later), I will talk about the tools we will need, show how to use them, explain how I generally think about programming in assembly and show how to write what is perhaps the smallest viable Windows program.

## Getting the Tools

There are two main tools that we will use throughout this series.

### Assembler

CPUs execute machine code - an efficient representation of instructions for the processor that is almost completely impenetrable to humans. The assembly language is a human-readable representation of it. A program that converts this symbolic representation into machine code ready to be executed by a CPU is called anassembler.

There is no single, agreed-upon standard for x86-64 assembly language. There are many assemblers out there, and even though some of them share a great deal of similarities, each has its own set of features and quirks. It is therefore important which assembler you choose. In this series, we will be usingFlat Assembler(or FASM for short). I like it because it's small, easy to obtain and use, has a nice macro system and comes with a handy little editor.

### Debugger

Another important tool is the debugger. We'll use it to examine the state of our programs. While I'm pretty sure it's possible to use Visual Studio's integrated debugger for this, I think a standalone debugger is better when all you want to do is look at the disassembly, memory and registers. I've always usedOllyDbgfor stuff like that, but unfortunately it does not have a 64-bit version. Therefore we will be usingWinDbg. The version linked here is a revamp of this venerable tool with a slightly nicer interface. Alternatively, you can get the non-Windows-store versionhereas part of the Windows 10 SDK. Just make sure you deselect everything else besides WinDbg during installation. For our purposes, the two versions are mostly interchangeable.

## Thinking in Assembly

Now that we have our tools, I want to spend a bit of time to discuss some basics. For the purpose of these tutorials I'm assuming some knowledge of languages like C or C++, but little or no previous exposure to assembly, therefore many readers will find this stuff familiar.

### A 10000-foot view

CPUs only "know" how to do a fixed number of certain things. When you hear someone talk about an "instruction set", they're referring to the set of things a particular CPU has been designed to do, and the term "instruction" just means "one of the things a CPU can do". Most instructions are parameterized in one way or another, and they're generally really simple. Usually an instruction is somthing along the lines of "write a given 8-bit value to a given location in memory", or "interpreting the values from registers A and B as 16-bit signed integers, multiply them and record the result into register A".

Below is a simple mental model of the architecture that we'll start with.

This skips atonof things (there can be more than one core executing instructions and reading/writing memory, there's different levels of cache, etc. etc.), but should serve as a good starting point.

To be effective at low-level programming or debugging you need to understand that every high-level concept eventually maps to this low-level model, and learning how the mapping works will help you.

### Registers

You can think ofregistersas a special kind of memory built right into the CPU that is very small, but extremely fast to access. There are many different kinds of registers in x86-64, and for now we'll concern ourselves only with the so-calledgeneral-purposeregisters, of which there are sixteen. Each of them is 64 bits wide, and for each of them the lower byte, word and double-word can be addressed individually (incidentally, 1 "word" = 2 bytes, 1 "double-word" = 4 bytes, in case you haven't heard this terminology before).

Register

Lower byte

Lower word

Lower dword

rax

al

ax

eax

rbx

bl

bx

ebx

rcx

cl

cx

ecx

rdx

dl

dx

edx

rsp

spl

sp

esp

rsi

sil

si

esi

rdi

dil

di

edi

rbp

bpl

bp

ebp

r8

r8b

r8w

r8d

r9

r9b

r9w

r9d

r10

r10b

r10w

r10d

r11

r11b

r11w

r11d

r12

r12b

r12w

r12d

r13

r13b

r13w

r13d

r14

r14b

r14w

r14d

r15

r15b

r15w

r15d

Additionally, the higher 8 bits ofrax,rbx,rcxandrdxcan be referred to asah,bh,chanddh.

Note that even though I said those were "general-purpose" registers, some instructions can only be used with certain registers, and some registers have special meaning for certain instructions. In particular,rspholds the stack pointer (which is used by instructions likepush,pop,callandret), andrsiandrdiserve as source and destination index for "string manipulation" instructions. Another example where certain registers get "special treatment" are the multiplication instructions, which require one of the multiplier values to be in the registerrax, and write the result into the pair of registersraxandrdx.

In addition to these registers, we will also consider the special registersripandrflags.ripholds the address of the next instruction to execute. It is modified by control flow instructions likecallorjmp.rflagsholds a bunch of binary flags indicating various aspects of the program's state, such as whether the result of the last arithmetic operation was less, equal or greater than zero. The behavior of many instructions depends on those flags, and many instructions update certain flags as part of their execution. The flags register can also be read and written "wholesale" using special instructions.

There are a lot more registers on x86-64. Most of them are used for SIMD or floating-point instructions, and we'll not be considering them in this series.

### Memory and Addresses

You can think of memory as a large array of byte-sized "cells", numbered starting at 0. We'll call these numbers "memory addresses". Simple, right?

Well... addressing memory used to be rather annoying back in the old days. You see, registers in old x86 processors used to be only 16-bit wide. Sixteen bits is enough to address 64 kilobytes worth of memory, but not more. The hardware was actually capable of using addresses as wide as 20 bits, but you had put a "base" address into a special segment register, and instructions that read or wrote memory would use a 16-bit offset into that segment to obtain the final 20-bit "linear" address. There were separate segment registers for code, data and stack portions (and a few more "extra" ones), and segments could overlap.

In x86-64 these concerns are non-existant. The segment registers for code, data and stack are still present, and they're loaded with some special values, but as a user-space programmer you needn't concern yourself with them. For all intents and purposes you can assume that all segments start at 0 and extend for the entire addressable length of memory. So, as far as we're concerned, on x86-64 our programs see memory as a "flat" contiguous array of bytes, with sequential addresses, starting at 0, just like we said in the beginning of this section...

Okay, I may have distorted the truth a little bit. Things aren't quite as simple. While it is true that on 64-bit Windows your programs see memory as a flat contiguous array of bytes with addresses starting at 0, it is actually an elaborate illusion maintained by the OS and CPU working together.

The truth is, if you were really able to read and write any byte in memory willy-nilly, you'd stomp all over other programs' code and data (something that indeed could happen in the Bad Old Days). To prevent that, special protection mechanisms exist. I won't get too deep into their inner workings here because this stuff matters mostly for OS developers. Nevertheless, here's a very short overview:

Each process gets a "flat" address space as described above (we'll call it the "virtual address space"). For each process, the OS sets up amappingbetween its virtual addresses and actual physical addresses in memory. This mapping is respected by the hardware: the "virtual" addresses get translated to physical addresses dynamically at runtime. Thus, the same address (e.g. 0x410F119C) can map to two different locations in physical memory for two different processes. This, in a nutshell, is how the separation between processes in enforced.

The final thing I want to invite your attention to here is how the instructions and data which they operate on are held in the same memory. While it may seem an obvious choice, it's not how computers necessarilyhaveto work. This is a property characteristic of the von Neumann model - as opposed to the Harvard model, where instructions and data are held in separate memories. A real-world example of a Harvard computer is the AVR microcontroller on your Arduino.

## Our First Program

Hopefully by this point you have downloaded FASM and are ready to write some code. Our first program will be really simple: it will load and then immediately exit. We mostly want it just to get acquainted with the tools.

Here's the code for our first program in x86-64 assembly:




format PE64 NX GUI 6.0
entry start

section '.text' code readable executable
start:
 int3
 ret



### Analyzing the Code

We'll go through this line-by-line.format PE64 NX GUI 6.0- this is a directive telling FASM the format of the binary we expect it to produce - in our case, Portable Executable Format (which is what most Windows programs use). We'll talk about it in a bit more detail later.entry start- this defines theentry pointinto our program. The entry directive requires a label, which in this case is "start". A label can be thought of as a name for an address within our program, so in this case we're saying "the entry point to the program is at whatever address the 'start' label is". Note that you're allowed to refer to labels even if they're defined later in the program code (as is the case here).section '.text' code readable executable- this directive indicates the beginning of a new section in a Portable Executable file, in this case a section containing executable code. More on this later.start:- this is the label that denotes the entry point to our program. We referred to it earlier in the "entry" directive. Note that labels themselves don't produce any executable machine code: they're just a way for the programmer to mark locations within the executable's address space.int3- this is a special instruction that causes the program to call the debug exception handler - when running under a debugger, this will pause the program and allow us to examine its state or proceed with the execution step-by-step. This is how breakpoints are actually implemented - the debugger replaces a single byte in the executable with the opcode corresponding to int3, and when the program hits it, the debugger takes over (obviously, the original content of the memory at breakpoint address has to be remembered and restored before proceeding with execution or single-stepping). In our case, we are hard-coding a breakpoint immediately at the entry point for convenience, so that we don't have to set it manually via the debugger every time.ret- this instruction pops off an address from the top of the stack, and transfers execution to that address. In our case, we'll return into the OS code that initially invoked our entry point.

Fire up FASMW.EXE, paste the code above into the editor, save the file and pressCtrl+F9. Your first assembly program is now complete! Let's now load it up in a debugger and single-step through it to see it actually working.

### Using the Debugger

Open up WinDbg. Go to the View tab and make sure the following windows are visible: Disassembly, Registers, Stack, Memory and Command. Go to File > Launch Executable and select the executable you just built with FASM. At this point your workspace should resemble something like this:

In thedisassemblywindow you can see the code that is currently being executed. Right now it's not our program's code, but some OS loader code - this stuff will load our program into memory and eventually transfer execution to our entry point. WinDbg ensures a breakpoint is triggered before any of that happens.

In theregisterswindow, you can see the contents of x86-64 registers that we discussed earlier.

Thememorywindow shows the raw content of the program's memory around a given virtual address. We'll use it later.

Thestackwindow shows the current call stack (as you can see, it's all inside ntdll.dll right now).

Finally, thecommandwindow allows entering text commands and shows log messages.

If you press F5 at this time, it will cause the program to continue running until it hits another breakpoint. The next breakpoint it will hit is the one we hardcoded. Try pressing F5, and you'll see something like this:

You should be able to recognize the two instructions we wrote - int3 and ret. To advance to the next instruction, press F8. When you do that, pay attention to theregisterswindow - you should see theripregister being updated as you advance (WinDbg highlights the registers that change in red).

Right after theretinstruction is executed, you will return to the code that invoked our program's entry point.

As you can see from the image above, the next thing that will happen is a call to RtlExitUserThread (a pretty self-explanatory name). If you press F5 now, your program's main thread will clean up and end, and so will the program. Or will it?...

The truth is, by usingret, I took a bit of a shortcut. On Windows a process will terminate if any of the following conditions are met:Any thread calls the WinAPI functionExitProcessexplicitlyAll threads have exited

But, we're exiting the main thread here so we should be good, right? Well, sort of. There's no guarantee that Windows hasn't started anyotherbackground threads (for example, to load DLLs or something like that) within our process. It seems that at least in this example, the main thread is the only one (I've checked and the process doesn't stick around), but this may change. A well-behaved Windows program should always callExitProcessat the appropriate time.

In order to be able to call WinAPI functions, we need to learn a few things about the Portable Executable file format, how DLLs are loaded and calling conventions.

## The PE Format and DLL Imports

TheExitProcessfunction lives in KERNEL32.DLL (yes, that's not a typo, KERNEL32 is the name of the 64-bit library. The 32-bit versions of those libs provided for back-compat pueporses, live in a folder names SysWOW64. I'm not joking.). In order to be able to call it, we first need toimportit.

We won't cover the Portable Executable format in its entirety here. It isdocumented extensivelyon the Microsoft docs website. Here are a couple of basic facts we'll need to know:PE files are comprised ofsections. We have already seen a section containing executable code in our program, but sections may contain other types of data.Information about what symbols are imported from what DLLs is stored in a special section called '.idata'.Let's have a look at the .idata section.

As per thedocs, the .idata section begins with animport directory table(IDT). Each entry in the IDT corresponds to one DLL, is 20 bytes in length and consists of the following fields:A 4-byterelative virtual address(RVA) of the Import Lookup Table (ILT), which contains the names of functions to import. More on that laterA 4-byte timestamp field (usually 0)Forwarder chain index (usually 0)A 4-byte RVA of a null-terminated string containing the name of the DLLA 4-byte RVA of the Import Address Table (IAT). The structure of the IAT is the same as ILT, the only difference is that the content of IAT is modified at runtime by the loader - it overwrites each entry with the address of the corresponding imported function. So theoretically, you can have both ILT and IAT fields point to the same exact piece of memory. Moreover, I've found that setting the ILT pointer to zero also works, although I am not sure if this behavior is officially supported.The Import Directory Table is terminated by an entry where all fields are equal zero.

The ILT/IAT is an array of 64-bit values terminated by a null value. The bottom 31 bits of each entry contain the RVA of an entry in a hint/name table (containing the name of the imported function). During runtime, the entries of the IAT are replaced with the actual addresses of the imported functions.

The hint/name table mentioned above consists of entries, each of which needs to be aligned on an even boundary. Each entry begins by a 2-byte hint (which we'll ignore for now) and a null-terminated string containing the imported function name, and a null byte (if necessary), to align the next entry on an even boundary.

With that out of the way, let's see how we would define our executable's .idata section in FASM




section '.idata' import readable writeable
idt: ; import directory table starts here
 ; entry for KERNEL32.DLL
 dd rva kernel32_iat
 dd 0
 dd 0
 dd rva kernel32_name
 dd rva kernel32_iat
 ; NULL entry - end of IDT
 dd 5 dup(0)
name_table: ; hint/name table
 _ExitProcess_Name dw 0
 db "ExitProcess", 0, 0

kernel32_name: db "KERNEL32.DLL", 0
kernel32_iat: ; import address table for KERNEL32.DLL
 ExitProcess dq rva _ExitProcess_Name
 dq 0 ; end of KERNEL32's IAT



The directive for a new PE section is already familiar to us. In this case, we're communicating that the section we're about to introduce contains the imports data and needs to be made writeable when loaded into memory (since addresses of the imported functions will be written in there).

The directives db, dw, dd and dq all cause FASM to emit a raw byte/word/double-word/quad-word value respectively. Thervaoperator, unsurprisingly, yields the relative virtual address of its argument. So,dd rva kernel32_iatwill cause FASM to emit a 4-byte binary value equal to the RVA ofkernel32_iatlabel.

Here we've just made use of fasm's db/dw/etc. directives to precisely describe the contents of our .idata section.

## The 64-bit Windows Calling Convention

We're now almost ready to finally call ExitProcess. One thing we have to answer though, is - how does a function call work? Think about it. There is acallinstruction, which pushes the current value ofriponto the stack, and transfers execution to the address specified by its parameter. There is also theretinstruction, which pops off an address from the stack and transfers execution there. Nowhere is it specified how arguments should be passed to a function, or how to handle the return values. The hardware simply doesn't care about that. It is the job of the caller and the callee to establish a contract between themselves. These rules might look along the lines of:The caller shall push the arguments onto the stack (starting from the last one)The callee shall remove the parameters from the stack before returning.The callee shall place return values in the registereax...

A set of rules like that is referred to as thecalling convention, and there are many different calling conventions in use. When you try to call a function from assembly, you must know what type of calling convention it expects.

The good news is that on 64-bit Windows there's pretty much only one calling convention that you need to be aware of - theMicrosoft x64 calling convention. The bad news is that it's a tricky one - unlike many of the older conventions, it requires the first few parameters to be passed via registers (as opposed to being passed on the stack), which can be good for performance.

You may read the full docs if you're interested in details, I will cover only the parts of the calling convention relevant to us here:The stack pointer has to be aligned to a 16-byte boundaryThe first four integer or pointer arguments are passed in the registers rcx, rdx, r8 and r9; the first four floating point arguments are passed in registers xmm0 to xmm3. Any additional args are passed on the stack.Even though the first 4 arguments aren't passed on the stack, the caller is still required to allocate 32 bytes of space for them on the stack. This has to be done even if the function has less than 4 arguments.The caller is responsible for cleaning up the stack.

Armed with this knowledge, we can finally call ExitProcess:format PE64 NX GUI 6.0
entry start

section '.text' code readable executable
start:
 int3
 sub rsp, 8 * 5 ; adjust stack ptr and allocate shadow space.
 xor rcx, rcx ; The first and only argument is the return code - passed in rcx.
 call [ExitProcess]


section '.idata' import readable writeable
idt: ; import directory table starts here
 ; entry for KERNEL32.DLL
 dd rva kernel32_iat
 dd 0
 dd 0
 dd rva kernel32_name
 dd rva kernel32_iat
 ; NULL entry - end of IDT
 dd 5 dup(0)
name_table: ; hint/name table
 _ExitProcess_Name dw 0
 db "ExitProcess", 0, 0

kernel32_name db "KERNEL32.DLL", 0
kernel32_iat: ; import address table for KERNEL32.DLL
 ExitProcess dq rva _ExitProcess_Name
 dq 0 ; end of KERNEL32's IAT

Let's go through the new lines one-by-one.sub rsp, 8 * 5- thesubinstruction subtracts its second operand from its first operand and stores the result in the first operand. In this case, we're subtracting 40 from the current value of the stack pointer (note that somewhat counterintuitively, the stack "grows" downward, i.e. pushing onto the stack or allocating space on it diminishes the value of the stack pointer). Thus, we're aligning the stack to a 16-byte boundary, and allocating a "shadow space" for the first 4 arguments in one fell swoop. How does this work? Well, before our entry point was invoked, the stack pointer was aligned to a 16-byte boundary. As a result of the call, a return address was pushed onto the stack, diminishing the stack pointer value by 8 and throwing it out of alignment. We need to subtract another 8 bytes to bring it into alignment again, and another 32 bytes to account for the shadow space, hence the value 40.xor rcx, rcx- recall that the first integer argument should be passed in the rcx register. Here, we're setting the value of that register to zero by performing a bitwise exclusive-or operation with itself.call [ExitProcess]- this is what finally calls ExitProcess. The square brackets around the label name denote indirection - rather than calling the address referred to by the label, the value recorded in memory at that address is used as the target address for the call. Of course, the label we're using is pointing to the location within the import table where the loader has written the address of the required function!

Fire it up in WinDbg again, run until our hardcoded breakpoint, then single-step to see how we eventually call ExitProcess, making note of how the rsp and rcx registers change.

That's it for this first part. Next time, we'll try to do something more interesting than just exiting the process :)

Like this post?Followme on bluesky for more!
