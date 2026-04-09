---
title: Why xor eax, eax? — Matt Godbolt’s blog
url: https://xania.org/202512/01-xor-eax-eax
date: 2025-12-01
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-02T11:09:43.520181
---

# Why xor eax, eax? — Matt Godbolt’s blog

**Why xor EAX, EAX?**

* The executable file's machine code implementation reveals a common optimization technique used by compilers.
* This technique involves using the "exclusive OR" operation (xor) with itself to save bytes in register values.
* Compilers use this instruction to zero out registers like EAX quickly.
* By replacing mov eax, 0 with xor eax, eax, the optimizer can take advantage of this optimization and allocate a new zero-value slot for EAX.

**Example: Saving Code Space and Execution Time**

* In this example, GCC optimizes the mov eax, 0 instruction to write into EAX.
* On 32-bit systems like Linux desktops, the result is a sequence of mov eax, value instructions, whereas on 64-bit systems like x86 machines, it only uses xor eax, eax.
* This optimization technique saves code space and execution time by reusing existing registers instead of allocating new ones.

**Advantages**

* The use of xor EAX, EAX allows for more efficient usage of register values.
* By reducing the number of instructions required to set a zero-value register, the compiler can optimize the program further.

**Additional Facts**

* On 64-bit systems like x86 machines, this optimization is specifically enabled by the "in-order" tracking system.
* Clang and other compilers also use similar optimizations for EAX-zeroing operations.
