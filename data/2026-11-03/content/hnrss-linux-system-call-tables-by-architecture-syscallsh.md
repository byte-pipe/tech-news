---
title: Linux System Call Tables by Architecture · syscall.sh
url: https://syscall.sh/
site_name: hnrss
content_file: hnrss-linux-system-call-tables-by-architecture-syscallsh
fetched_at: '2026-11-03T06:07:44.533017'
original_url: https://syscall.sh/
date: '2026-11-02'
description: 'The Linux syscall table for 27 architectures: every system call number, argument and register, with a table per architecture, from Linux 3.3 to 7.3.'
tags:
- hackernews
- hnrss
---

# Linux syscall tables

Every Linux syscall table in one place, grouped by architecture: system calls for 27 architectures with their numbers, arguments and registers, from Linux 3.3 to 7.3.

## Architectures

* x64x86_64369 syscalls · since 3.3
* x86i386, 32 bit x86441 syscalls · since 3.3
* arm64AArch64326 syscalls · since 3.7
* armARM EABI, 32 bit426 syscalls · since 4.10
* riscv64RISC-V, 64 bit327 syscalls · since 4.15
* ia32IA-32 compat on x86_64439 syscalls · since 3.3
* x32x32 ABI on x86_64369 syscalls · since 3.4
* loongarch64LoongArch, 64 bit323 syscalls · since 5.19
* ppc64PowerPC, 64 bit383 syscalls · since 5.0
* ppcPowerPC, 32 bit425 syscalls · since 5.0
* s390xIBM Z378 syscalls · since 4.16
* mips64MIPS n64 ABI363 syscalls · since 5.0
* mipsn32MIPS n32 ABI387 syscalls · since 5.0
* mipso32MIPS o32 ABI413 syscalls · since 5.0
* alphaDEC Alpha403 syscalls · since 5.0
* arcSynopsys ARC350 syscalls · since 3.9
* cskyC-SKY346 syscalls · since 4.20
* hexagonQualcomm Hexagon345 syscalls · since 3.7
* m68kMotorola 68000435 syscalls · since 5.0
* microblazeXilinx MicroBlaze423 syscalls · since 5.0
* nios2Intel Nios II346 syscalls · since 3.19
* openriscOpenRISC346 syscalls · since 3.7
* pariscHP PA-RISC404 syscalls · since 5.0
* shSuperH433 syscalls · since 5.0
* sparcSPARC, 32 bit434 syscalls · since 5.0
* sparc64SPARC, 64 bit399 syscalls · since 5.0
* xtensaTensilica Xtensa388 syscalls · since 5.0

Every architecture's table, with the full history of when each syscall appeared and when it was dropped, is also a plain JSON file at/<arch>/syscalls.json, for example/x64/syscalls.json.

## Calling conventions

Number inNR, arguments inARG0toARG5, then the instruction. The result comes back inRETURN.

ARCH
INSTRUCTION
NR
RETURN
ARG0
ARG1
ARG2
ARG3
ARG4
ARG5

x64
syscall
rax
rax

rdi
rsi
rdx
r10
r8
r9

x86
int 0x80
eax
eax

ebx
ecx
edx
esi
edi
ebp

arm64
svc #0
x8
x0

x0
x1
x2
x3
x4
x5

arm
svc #0
r7
r0

r0
r1
r2
r3
r4
r5

riscv64
ecall
a7
a0

a0
a1
a2
a3
a4
a5

ia32
int 0x80
eax
eax

ebx
ecx
edx
esi
edi
ebp

x32
syscall
rax
rax

rdi
rsi
rdx
r10
r8
r9

loongarch64
syscall 0
a7
a0

a0
a1
a2
a3
a4
a5

ppc64
sc
r0
r3

r3
r4
r5
r6
r7
r8

ppc
sc
r0
r3

r3
r4
r5
r6
r7
r8

s390x
svc 0
r1
r2

r2
r3
r4
r5
r6
r7

mips64
syscall
v0
v0

a0
a1
a2
a3
a4
a5

mipsn32
syscall
v0
v0

a0
a1
a2
a3
a4
a5

mipso32
syscall
v0
v0

a0
a1
a2
a3
sp+16
sp+20

alpha
callsys
v0
v0

a0
a1
a2
a3
a4
a5

arc
trap0
r8
r0

r0
r1
r2
r3
r4
r5

csky
trap 0
r7
a0

a0
a1
a2
a3
r4
r5

hexagon
trap0(#1)
r6
r0

r0
r1
r2
r3
r4
r5

m68k
trap #0
d0
d0

d1
d2
d3
d4
d5
a0

microblaze
brki r14,8
r12
r3

r5
r6
r7
r8
r9
r10

nios2
trap
r2
r2

r4
r5
r6
r7
r8
r9

openrisc
l.sys 1
r11
r11

r3
r4
r5
r6
r7
r8

parisc
ble 0x100(%sr2, %r0)
r20
r28

r26
r25
r24
r23
r22
r21

sh
trapa #31
r3
r0

r4
r5
r6
r7
r0
r1

sparc
t 0x10
g1
o0

o0
o1
o2
o3
o4
o5

sparc64
t 0x6d
g1
o0

o0
o1
o2
o3
o4
o5

xtensa
syscall
a2
a2

a6
a3
a4
a5
a8
a9

## API

curl https://api.syscall.sh/v2/syscalls/x64/read

Any kernel release, diffs between releases and more in theAPI docs.

## Syscall tables across kernel versions

Entries get added and, rarely, removed between releases. Each architecture page has a kernel selector, and its JSON download records when each entry first appeared (since) and when it was dropped (removed_in).

Removed entries stay visible: pick "all, with removed" in the kernel selector and each dropped syscall is marked with the release that dropped it.

## Where the data comes from

Everything on this site is read from the kernel source itself. For each architecture, the generator walks the syscall table and theSYSCALL_DEFINEmacros of every mainline release it scans, so these are the numbers the kernel actually dispatches on.

It also records each architecture's calling convention, the instruction that enters the kernel, so every syscall table shows exactly where the number and the arguments go.

A syscall whosesinceequals the first release scanned for its architecture was already there back then, and may be much older.

### Descriptions and full history

The short descriptions come from theLinux man pages project, and theio_uringones fromliburing. Whenever the data changes, the site is rebuilt from thesyscall API.