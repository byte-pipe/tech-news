---
title: 'IonStack part II: GhostLock, a stack-UAF that has existed in ALL Linux distributions for 15 years | Nebula Security'
url: https://nebusec.ai/research/ionstack-part-2/
site_name: hackernews_api
content_file: hackernews_api-ionstack-part-ii-ghostlock-a-stack-uaf-that-has-ex
fetched_at: '2026-07-13T12:03:27.272180'
original_url: https://nebusec.ai/research/ionstack-part-2/
author: ranger_danger
date: '2026-07-08'
published_date: '2026-07-07T00:00:00.000Z'
description: GhostLock (CVE-2026-43499) is a Linux kernel vulnerability found by VEGA that exists in every major distribution since 2011. Triggering the bug does not require any special kernel config or privilege. By turning it into a 97% stable privilege escalation and container escape, Google has rewarded us $92,337 in kernelCTF. This writeup covers the technical details of the exploit.
tags:
- hackernews
- trending
---

July 2026·linux

 

# IonStack part II: GhostLock, a stack-UAF that has existed in ALL Linux distributions for 15 years

 
 
 
 
Nebula Security
 
 
 
 
July 7, 2026
 
 
 
 17 min read 
 
 
 
 
 
 
 
 linux 
 
 
 
 CVE-2026-43499 
 
 
 
 GhostLock 
 
 
 
 vulnerability 
 
 
 
 ionstack 
 
 
 
 
Table of Contents
* Vulnerability Summary
* Vulnerability Analysis
* Overview
* Root cause
* Triggering the stack-UAF
* The initial primitive from GhostLock
* Exploit Details
* Exploit Summary
* Background of used tricks
* Prefetch ASLR Leak
* CEA spray and randomization bypass
* Reusing the stack: forging the waiter with PR_SET_MM_MAP
* From fake waiter to one controlled (limited) write
* Use inet6_protos[IPPROTO_UDP] to help
* The pivot and DirtyMode
* Appendix
* bigger ROP or NPerm
* Mitigation
* The patch
* RANDOMIZE_KSTACK_OFFSET
* STATIC_USERMODE_HELPER
* Timeline
* Disclosure policy
 
 
 
 
 
 
 
 
 
 
 
 

Need something less technical? Take a quick look at our bug summary.

 
 
 Read the bug summary 
→
 
 
 

GhostLock (CVE-2026-43499) is a Linux kernel vulnerability found byVEGAthat exists in every major distribution since 2011. Triggering the bug does not require any special kernel config or privilege. By turning it into a 97% stable privilege escalation and container escape, Google has rewarded us $92,337 in kernelCTF. This writeup covers the technical details of the exploit.

## Vulnerability Summary

GhostLock (CVE-2026-43499) lets an unprivileged local attacker:

* Get a dangling kernel pointer to kernel stack memory with only regular threading syscalls.
* Write a pointer to an almost arbitrary address.
* Hijack a function table to get control flow hijack and eventually get root access.

GhostLock was introduced in Linux 2.6.39 and fixed in Linux 7.1. It has existed in the Linux kernel for more than 15 years.Every Linux distributionwithout the patch is affected and should consider upgrading to the latest LTS version.

Your browser does not support the video tag.

## Vulnerability Analysis

 
 
 
 
 
I would like to see the exploit strategy directly
 
 
 

### Overview

GhostLock was introduced with the rtmutex rework in8161239a8bcc(“rtmutex: Simplify PI algorithm and make highest prio task get lock”), and sat untouched for about fifteen years until the April 2026 fix in3bfdc63936dd(“rtmutex: Use waiter::task instead of current in remove_waiter()”). The affected range isv2.6.39-rc1tov7.1-rc1, withCONFIG_FUTEX_PI=ythe only requirement and no capabilities or user namespaces needed.

remove_waiter()inkernel/locking/rtmutex.cclearscurrent->pi_blocked_on. That is correct on the normal slow path, wherecurrentis the task that owns the waiter. It is wrong on the proxy path.rt_mutex_start_proxy_lock()enqueues, and on error rolls back, anrt_mutex_waiteron behalf of another task, socurrentis the requeuer rather than the waiter.

The waiter object lives on the stack of a task sleeping inFUTEX_WAIT_REQUEUE_PI. AFUTEX_CMP_REQUEUE_PIthen proxies that waiter onto the target PI futex. When the rtmutex chain walk reports a deadlock, the rollback dequeues the waiter from the lock but clearspi_blocked_onon the requeuer. The waiter task keepspi_blocked_onpointing at its own stack frame, which is popped the moment the waiter returns to userspace. Any later PI chain walk through that task follows the dangling pointer.

### Root cause

Like other lifecycle bugs, this occurs when a function is used by a caller it was never designed to support.

The helper functionremove_waiter()was originally written for exactly one scenario: a thread blocks on its own, then cleans up after itself.
So it has always assumed thatcurrent(whichever thread happens to be running) is thewaiterit needs to clean up, and clearscurrent->pi_blocked_onaccordingly.

However, Requeue-PI breaks that assumption. Throughrt_mutex_start_proxy_lock(), this helper is now used to clean up on behalf of a different, sleeping thread.
In that path,currentis the thread that issuedFUTEX_CMP_REQUEUE_PIrather than the actualwaiter.

When__rt_mutex_start_proxy_lock()returns-EDEADLK, it rolls back viaremove_waiter(), the misused helper.

1
int
 __sched 
rt_mutex_start_proxy_lock
(
struct
 rt_mutex_base 
*
lock
,
2
 
struct
 rt_mutex_waiter 
*
waiter
,
3
 
struct
 task_struct 
*
task
)
4
{
5
 
int
 ret;
6
 
raw_spin_lock_irq
(
&
lock->wait_lock);
7
 
ret 
=
 
__rt_mutex_start_proxy_lock
(lock, waiter, task);
8
 
if
 (
unlikely
(ret))
9
 
remove_waiter
(lock, waiter);
 // ret == -EDEADLK
10
 
raw_spin_unlock_irq
(
&
lock->wait_lock);
11
 
return
 ret;
12
}

remove_waiter()then scrubs the wrong task.

1
static
 
void
 __sched 
remove_waiter
(
struct
 rt_mutex_base 
*
lock
,
2
 
struct
 rt_mutex_waiter 
*
waiter
)
3
{
4
 
...
5
 
raw_spin_lock
(
&
current->pi_lock);
6
 
rt_mutex_dequeue
(lock, waiter);
7
 
current->pi_blocked_on 
=
 
NULL
;
 // should be waiter->task
8
 
raw_spin_unlock
(
&
current->pi_lock);
9
 
...
10
}

waiteris the object that lives on the sleeping thread’s own stack, whilecurrenthere is the thread that requested the requeue. The fix lockswaiter->task->pi_lockand clearswaiter->task->pi_blocked_oninstead. This issue slips past lockdep, which only checks that api_lockis held but not whose it is.

Triggering the -EDEADLK Path.Reaching the-EDEADLKrollback needs a PI dependency cycle built from three futex words and three threads.

* f_pi_chain, a PI futex, locked first by thewaiterthread.
* f_pi_target, a PI futex, locked first by theownerthread. This is the requeue target.
* f_wait, the plain futex the waiter blocks on withFUTEX_WAIT_REQUEUE_PI.

The sequence is:

1. The waiter takesf_pi_chain, then blocks inFUTEX_WAIT_REQUEUE_PI(f_wait -> f_pi_target). Itsrt_mutex_waiteris now on its stack.
2. The owner takesf_pi_target, then blocks onf_pi_chain, which the waiter holds.
3. The main thread callsFUTEX_CMP_REQUEUE_PI(f_wait -> f_pi_target).

The requeue tries to proxy the waiter ontof_pi_target. The owner off_pi_targetis already blocked behind the waiter throughf_pi_chain, so the chain walk closes the loopwaiter -> f_pi_target -> owner -> f_pi_chain -> waiter. It returns-EDEADLKand takes the buggy rollback. The waiter wakes with a danglingpi_blocked_on.

Here the only ordering that matters is the requeuer rolling back the waiter while the waiter still owns the soon-to-be-freed object, and once the cycle is staged that happens on its own. After it resolves there is no time pressure at all. The waiter sits in userspace with a danglingpi_blocked_on, and the follow-upsched_setattr()that walks the chain can fire whenever it likes. The UAF window is wide open.

The catch is where the freed object lives on the kernel stack (stack-UAF if we callretout of the futex syscall a “free”). To reclaim it, we need to find a syscall that can land controlled bytes back on the same stack at the same depth (offset).

### Triggering the stack-UAF

Staging the three-futex cycle leaves the waiter task in userspace withpi_blocked_ondangling into its oldFUTEX_WAIT_REQUEUE_PIframe. Everything below rides on that one pointer.

Note that three threads is for better understanding. To win the race and trigger UAF, you only need one CPU core.

 
 

#### The initial primitive from GhostLock

By now we hold a pointer into freed kernel stack, and we can trigger, at will, a kernel access that dereferences it as anrt_mutex_waiter. We can spray controlled bytes onto that stack and forge thert_mutex_waiteroutright. Depending on the layout we forge, this one access yields several primitives, two main ones:

* write a pointer to an arbitrary (but constrained) address
* write 8 bytes of zero to an arbitrary (but constrained) address

Several pointer dereferences and integrity checks run before the primitive fires, and after it fires the kernel returns normally, no crash.

So our main questions, each answered in a section below:

* how do we get the freed stack memory back (spray)?-> Reusing the stack
* how do we get the fakert_mutex_waiterpast its built-in structural checks, and forge pointers that read as valid?-> From fake waiter to a write
* which write primitive, and what do we write where? what does the primitive constrain about the “arbitrary” address?-> Use inet6_protos

## Exploit Details

### Exploit Summary

* prefetch-> Leak the kernel image slide and the physmap base.
* GhostLock-> Leave a danglingrt_mutex_waiterin the waiter task’spi_blocked_on.
* (stack-)UAF Reclaim-> UsePR_SET_MM_MAPto reclaim the waiter’s own kernel stack and forge a fakert_mutex_waiterover the freed frame.
* Arb address writer-> Rtmutex rb-tree erase: one constrained pointer write (which we can reclaim its content), overwrite struct which contains a function table:inet6_protos[IPPROTO_UDP] = <CEA pointer>.
* CPU entry area-> Host {fakeinet6_protocol, pivot slots, ROP stack} all together at a known direct-map address.
* Trigger CFH-> Trigger a loopback IPv6 UDP packet calls through the overwritten handler and pivots.
* DirtyMode-> One write flipscore_pattern’s mode bits, then the rest LPE is pure userspace.

 
 
 
 
 
I am an experienced kernel security researcher, I would like to see the exploit detail directly
 
 
 
 
 
 
 
 
 What about Android? 
 
 
 
 
 
 

This part we are focusing on basic exploit steps of generic x86 Linux systems, our next blog will discuss how to exploit GhostLock on Android, reclaiming stack frame, bypassing both ASLR and CFI.

 
 

### Background of used tricks

#### Prefetch ASLR Leak

Aprefetchon a given address runs in a different number of cycles depending on whether that address is mapped in the current page tables, so an unprivileged process can timeprefetchacross the kernel range and read off which addresses are mapped (theprefetch paperhas the details).

It works here as Linux barely randomizes the base of its default kernel image (~9 bits of entropy for text base), so a little averaging can recover the KASLR base with near 100% reliability.

In theory any CPU withprefetchand without proper Kernel Page-Table Isolation is affected. But in practice it is more of an x86 technique (unless the ARM target runs KPTI off). kernelCTF images keep KPTI disabled.

kernelCTF images keep KPTI disabled, but even with KPTI on,prefetchpaired withEntryBleedcan still recover the kernel image base through the trampoline.

#### CEA spray and randomization bypass

The CEA (CPU entry area) is a per-CPU x86 structure holding the stacks and register context used for entry and exception handling: on an exception, interrupt, or syscall the CPU switches to a stack that lives in the CEA, and the entry code spills the register frame (pt_regs) there. An unprivileged userspace program can trigger a software exception and write its own register context into thept_regssaved on a CEA exception stack. Before6.2the CEA sat at a completely fixed address, so we can place about 120 bytes of contiguous controlled memory at a known kernel address, which is very handy for forging structures, for absorbing the side effects of the pointer dereferences along the way, and for staging a ROP stack.

After Project Zero’sBringing back the stack attackwriteup, the kernel started strongly randomizing the CEA’s virtual address (since6.2). But the virtual address of the CPU entry area is never needed, as the CEA’s physical offset is fixed, so its direct-map alias follows from the physmap base (same observation@kqxused).

That direct-map address is easy to leak withprefetch, plus candidate-edge normalization and a check against the predicted CEA page to reject neighbouring aliases. (The direct-map leak is noisier than the text one and may need a little more tuning, but it lands at very high accuracy on the target in the end.) So we can always compute the CEA’s other virtual-address mapping:

1
cea_direct = physmap_base + CPU1_CEA_BASE

Note that each CPU’s CEA virtual address is randomized to a different place. Their physical addresses are all fixed, though, and this offset depends mainly on the target’s kernel version and boot memory size. In the kernelCTF LTS6.12.803.5G-boot environment, it is0x11c517000(+0x1f58).

 
 

### Reusing the stack: forging the waiter withPR_SET_MM_MAP

The dangling object is the waiter’s own stackrt_mutex_waiter.

1
struct
 rt_mutex_waiter {
2
 
struct
 rt_waiter_node tree;
 // rb node, lives in lock->waiters
3
 
struct
 rt_waiter_node pi_tree;
4
 
struct
 task_struct 
*
task;
5
 
struct
 rt_mutex_base 
*
lock;
6
 
unsigned
 
int
 wake_state;
7
 
struct
 ww_acquire_ctx 
*
ww_ctx;
8
};

Controlled bytes have to land back over that exact frame, on the waiter thread’s own stack, and stay there long enough to be read. The waiter thread returns from the futex syscall and immediately callsprctl(PR_SET_MM, PR_SET_MM_MAP, ...). Inside,prctl_set_mm_map()copies a user-supplied auxv into a fixed-sizeunsigned long user_auxv[AT_VECTOR_SIZE]stack buffer. That buffer sits at roughly the same stack depth as the freed waiter, so it is a large, naturally-aligned, namespace-free block of controlled qwords landing right on top of the old object.

The auxv is laid out so the overlapping qwords become:

* tree, an rb node crafted so erasing it promotes one chosen child pointer (W0_BASE, below) into the tree root.
* task, set to&init_task, a validtask_structso the chain walk’s task derefs are safe.
* lock, set to&inet6_protos[IPPROTO_UDP] - 8, the write target.
* wake_state, set to0.

The auxv is backed by a memfd and positioned so the copy straddles a page boundary. A sibling thread racesfallocate(PUNCH_HOLE)on the trailing page during theprctl, which stretches thecopy_from_userwindow. The forged waiter stays live on the stack while, on another CPU, a consumer thread firessched_setattr()on the waiter to walk the PI chain.The race window is wide and we believe GhostLock is also exploitable on a single-core CPU.

clone/setsockopt/pselect/keyctland other syscalls with large controlled stack locals work the same way.prctlis just convenient here. The buffer is large, aligned, and needs no namespace.Here’s more useful syscalls that can reclaim the stack frame in ouropen-sourced PoC code.

### From fake waiter to one controlled (limited) write

Controlling the waiter does not give an arbitrary write. The chain walk only does:

1
task->pi_blocked_on -> fake waiter
2
fake waiter->lock -> fake rt_mutex_base
3
rt_mutex_dequeue(lock, waiter) // rb_erase on lock->waiters

rt_mutex_dequeue()is an rb-tree erase, and erasing a single-child root writes that child into the root slot. Pointinglockattarget - 8lines thert_mutex_basefields up over the data around the target pointer.

1
target - 8 -> raw_spinlock_t wait_lock (must read as "unlocked")
2
target -> waiters.rb_root.rb_node (this slot gets written)
3
target + 8 -> waiters.rb_leftmost
4
target + 16 -> owner

The fake waiter’s rb node is crafted so the erase writes exactly one child pointer intorb_root.rb_node. The write primitive itself is a single constrained store:*(uint64_t *)target = W0_BASE.

The constraints are also highly strict: The qword before the target must read as an unlocked spinlock, meaning zero in the low 4 bytes, or the trylock fails and the walk exits without writing. The qwords after it (rb_leftmost,owner) must not steer the walk into an uncontrolled top waiter or owner. An unmapped value there faults and panics the box.
The equivalent target address constraint is roughly as follows (*target will be written to a pointer):

1
*
(u32 
*
)(target 
-
 
0x
08
) 
==
 
0
2
*
(u64 
*
)(target 
+
 
0x
08
) 
==
 
0
 // simplified
3
((
*
(u64 
*
)(target 
+
 
0x
10
)) 
&
 
~
1
ULL
) 
==
 
0
4
// Then we can do:
5
*
(u64 
*
)target 
=
 
&
W0
->
tree.entry
 // W0_BASE

Here theW0_BASEhas to point at something that stays valid through the comparisons and the no-owner wakeup later in the samert_mutex_adjust_prio_chain(). We point it at the direct-map alias of the CPU entry area, which pays off twice:

* Before the write: the CEA is controllable memory at a known address, so we can forge a self-consistent fake waiter and lock atW0that survives the walk.
* After the write: the target now points into the CEA. Once the walk is over,W0no longer has to look like a waiter at all, so we can re-spray the CEA with whatever the kernel expects the target to point at (if we overwritten a function table pointer withW0, we can now fake function pointer in CEA to get 	Control Flow Hijack).

 
 
 
 
 
 Why the CEA? 
 
 
 
 
 
 

There’s several ways to spray controlled memory at a fixed (knowned) kernel address. The CEA is one of the more efficient, and its main limit is the ~120-byte small size. NPerm, kernelsnitch and other tricks can do the same job with more room.

 
 

Before the trigger,W0is spraied as that fake waiter and lock pair:task = &init_task, a legitprio, and alockwhosewait_lockreads unlocked and whose owner is benign, so the dequeue, re-enqueue, priority update and wakeup all survive.

The following figure shows how CPU entry area is used to first hold fakert_mutex_waiterandlockstructures, then serveinet6(next section), ROP stack and JOP gadgets for stack pivoting at the same time, and eventually use a very short ROP to perform the DirtyMode and safely halt the core.

### Useinet6_protos[IPPROTO_UDP]to help

Start from now the exploit path would differ from targets, as of regular x86_64 Linux kernel, we can pick a shorter path by just overwriting some function table (or any object that contains one), as we already have KASLR leaked and ready to get a CFH.

A scan of writable data turns up many pointer tables whose neighbours satisfy the layout above.inet6_protos[IPPROTO_UDP]is a nice one. The neighbours fall out for free, and the trigger is a trivial unprivileged loopback packet.

1
inet6_protos[16] == NULL // fake wait_lock -> unlocked
2
inet6_protos[17] == &udpv6_protocol // <- target (IPPROTO_UDP)
3
inet6_protos[18] == NULL // fake rb_leftmost
4
inet6_protos[19] == NULL // fake owner

After the write,inet6_protos[IPPROTO_UDP]points into the CEA page, where the kernel expects aninet6_protocol.

1
struct
 inet6_protocol {
2
 
int
 (
*
handler)(
struct
 sk_buff 
*
skb);
3
 
int
 (
*
err_handler)(...);
4
 
unsigned
 
int
 flags;
5
};

SoW0is re-spraied as a fakeinet6_protocol.handleris the first pivot gadget,err_handleris unused, andflagsisINET6_PROTO_NOPOLICY | INET6_PROTO_FINAL. Once we send a loopback IPv6 UDP (connectthenwriteto::1), the kernel will dereference thehandlerand give us a PC control.

### The pivot and DirtyMode

We use the same compact CEA window to holds multiple objects: {the fakeinet6_protocol, a few JOP/pivot slots, the final ROP stack}. On Google’s lts-6.12.80 kernel target we are not lucky enough to find a nice single stack pivot target, so the chain takes one extra load/call to land the CEA address inrbp, then pivots withmov rsp, rbp; pop rbp; ret.

Aret2usror a full/proc/%P/fd/xoverwrite would run to around ten gadget qwords, which is too long. So we useDirtyModeas the final exploit stage: a single write, with an almost-garbage value, that flips a permission bit. After it, LPE can be done purely in userspace.

Here we target at thecore_patternsysctl’s mode flags:

1
static
 
struct
 ctl_table coredump_sysctls
[]
 
=
 {
2
 
...
3
 
{ .procname 
=
 
"core_pattern"
,
4
 
.data 
=
 core_pattern,
5
 
.maxlen 
=
 CORENAME_MAX_SIZE,
6
 
.mode 
=
 
0
644
,
7
 
.proc_handler 
=
 proc_dostring_coredump },
8
 
...
9
};

coredump_sysctlslives in writable kernel data (share same KASLR slide with kernel image). The ROP writes a permissive value tocoredump_sysctls[1].mode. Any value with the write bit (2nd LSB) set is enough.

Here we uses a shortpop reg; mov [reg], reg; retplus anmsleepto park the hijacked thread safely. And now/proc/sys/kernel/core_patternis now world-writable, so an unprivileged process opens it, writes|/proc/%P/fd/666 %P, and crashes a helper to trick kernel runs our binary as root.

The initial write primitive (the rb-tree write) cannot reachcoredump_sysctls[1].modedirectly because of where it lands, so the mode flip is done from the short ROP stage.

## Appendix

The full exploit code can be found in ouropen source security research project, CyberMeowfia.

### bigger ROP or NPerm

kernelCTF is a race, and the shortest reliable chain wins.NPerm-backed memory makes a fine large fake stack after the hijack, and there are heavier routes that would also work, includingLukas Maar’s heap-KASLR leak. Each adds another stage and increases time cost. CEA plus DirtyMode is the shortest path to a one-write win, and on the remote it win us the flag in about 5 seconds.

### Mitigation

#### The patch

1
diff --git a/kernel/locking/rtmutex.c b/kernel/locking/rtmutex.c
2
--- a/kernel/locking/rtmutex.c
3
+++ b/kernel/locking/rtmutex.c
4
@@ -1544,6 +1544,8 @@
 static bool rtmutex_spin_on_owner(struct rt_mutex_base *lock,
5
 
*
6
 
* Must be called with lock->wait_lock held and interrupts disabled. It must
7
 
* have just failed to try_to_take_rt_mutex().
8
+ *
9
+ * When invoked from rt_mutex_start_proxy_lock() waiter::task != current !
10
 
*/
11
 
static void __sched remove_waiter(struct rt_mutex_base *lock,
12
 
struct rt_mutex_waiter *waiter)
13
@@ -1551,14 +1553,15 @@
 static void __sched remove_waiter(struct rt_mutex_base *lock,
14
 
{
15
 
bool is_top_waiter = (waiter == rt_mutex_top_waiter(lock));
16
 
struct task_struct *owner = rt_mutex_owner(lock);
17
+ struct task_struct *waiter_task = waiter->task;
18
 
struct rt_mutex_base *next_lock;
19

20
 
lockdep_assert_held(&lock->wait_lock);
21

22
- raw_spin_lock(&current->pi_lock);
23
- rt_mutex_dequeue(lock, waiter);
24
- current->pi_blocked_on = NULL;
25
- raw_spin_unlock(&current->pi_lock);
26
+ scoped_guard(raw_spinlock, &waiter_task->pi_lock) {
27
+ rt_mutex_dequeue(lock, waiter);
28
+ waiter_task->pi_blocked_on = NULL;
29
+ }
30

31
 
/*
32
 
* Only update priority if the waiter was the highest priority
33
@@ -1594,7 +1597,7 @@
 static void __sched remove_waiter(struct rt_mutex_base *lock,
34
 
raw_spin_unlock_irq(&lock->wait_lock);
35

36
 
rt_mutex_adjust_prio_chain(owner, RT_MUTEX_MIN_CHAINWALK, lock,
37
- next_lock, NULL, current);
38
+ next_lock, NULL, waiter_task);

We had also sent a fix tosecurity@kernel.orgbefore v1 landed. Its core:

1
static void __sched remove_waiter(struct rt_mutex_base *lock,
2
 
struct rt_mutex_waiter *waiter)
3
 
struct rt_mutex_waiter *waiter,
4
 
struct task_struct *task)
5
{
6
 
...
7
 
raw_spin_lock(&current->pi_lock);
8
 
raw_spin_lock(&task->pi_lock);
9
 
rt_mutex_dequeue(lock, waiter);
10
 
current->pi_blocked_on = NULL;
11
 
raw_spin_unlock(&current->pi_lock);
12
 
if (task->pi_blocked_on == waiter)
13
 
task->pi_blocked_on = NULL;
14
 
raw_spin_unlock(&task->pi_lock);
15
 
...
16
 
rt_mutex_adjust_prio_chain(owner, RT_MUTEX_MIN_CHAINWALK, lock,
17
 
next_lock, NULL, current);
18
 
next_lock, NULL, task);
19
}

Instead of reading the task out ofwaiter->task, the callers pass in the owning task (currenton the self-blocking path, the proxiedtaskon thert_mutex_start_proxy_lock()rollback), andpi_blocked_onis cleared only when it still points at this waiter.taskis always a valid task and the clear is guarded.

#### RANDOMIZE_KSTACK_OFFSET

The stack-reuse step relies on the freed waiter frame and the lateruser_auxvframe overlapping deterministically. WithRANDOMIZE_KSTACK_OFFSETon they no longer do, and the step becomes a roughly 1/32 (5-bit) stack-offset guess. Both submitted targets leave it off by default. The mitigation target turns it on, so this path was not used there.

#### STATIC_USERMODE_HELPER

STATIC_USERMODE_HELPERwould close this particular DirtyMode path. But the same idea can be generalized to any/proc/sysknob whosectl_table::modegates access and whose table sits in predictable writable kernel data.

### Timeline

* 2026-04-18: We reported the bug and sent a draft patch tosecurity@kernel.org.
* 2026-04-20: The bug was fixed with another patch.
* 2026-05-04: The fix v1 was backported.
* 2026-06-30: Google acknowledged our kernelCTF submission.
* 2026-07-07: We published this blog post.

### Disclosure policy

For all bugs found byVEGA, we follow our standard 90+30 days disclosure policy as described on ourAbout page.