---
title: How we found a bug in Go's arm64 compiler
url: https://blog.cloudflare.com/how-we-found-a-bug-in-gos-arm64-compiler/
site_name: hackernews_api
fetched_at: '2025-10-09T11:07:17.375262'
original_url: https://blog.cloudflare.com/how-we-found-a-bug-in-gos-arm64-compiler/
author: jgrahamc
date: '2025-10-08'
published_date: 2025-10-08T14:00+00:00
description: 84 million requests a second means even rare bugs appear often. We'll reveal how we discovered a race condition in the Go arm64 compiler and got it fixed.
tags:
- hackernews
- trending
---

# How we found a bug in Go's arm64 compiler

2025-10-08

* Thea Heinen
10 min read

Every second, 84 million HTTP requests are hitting Cloudflare across our fleet of data centers in 330 cities. It means that even the rarest of bugs can show up frequently. In fact, it was our scale that recently led us to discover a bug in Go's arm64 compiler which causes a race condition in the generated code.

This post breaks down how we first encountered the bug, investigated it, and ultimately drove to the root cause.

## Investigating a strange panic

We run a service in our network which configures the kernel to handle traffic for some products likeMagic TransitandMagic WAN. Our monitoring watches this closely, and it started to observe very sporadic panics on arm64 machines.

We first saw one with a fatal error stating thattraceback did not unwind completely. That error suggests that invariants were violated when traversing the stack, likely because of stack corruption. After a brief investigation we decided that it was probably rare stack memory corruption. This was a largely idle control plane service where unplanned restarts have negligible impact, and so we felt that following up was not a priority unless it kept happening.

And then it kept happening.

#### Coredumps per hour

When we first saw this bug we saw that the fatal errors correlated with recovered panics. These were caused by some old code which used panic/recover as error handling.

At this point, our theory was:

1. All of the fatal panics happen within stack unwinding.
2. We correlated an increased volume of recovered panics with these fatal panics.
3. Recovering a panic unwinds goroutine stacks to call deferred functions.
4. A relatedGo issue (#73259)reported an arm64 stack unwinding crash.
5. Let’s stop using panic/recover for error handling and wait out the upstream fix?

So we did that and watched as fatal panics stopped occurring as the release rolled out. Fatal panics gone, our theoretical mitigation seemed to work, and this was no longer our problem. We subscribed to the upstream issue so we could update when it was resolved and put it out of our minds.

But, this turned out to be a much stranger bug than expected. Putting it out of our minds was premature as the same class of fatal panics came back at a much higher rate. A month later, we were seeing up to 30 daily fatal panics with no real discernible cause; while that might account for only one machine a day in less than 10% of our data centers, we found it concerning that we didn’t understand the cause. The first thing we checked was the number of recovered panics, to match our previous pattern, but there were none. More interestingly, we could not correlate this increased rate of fatal panics with anything. A release? Infrastructure changes? The position of Mars?

At this point we felt like we needed to dive deeper to better understand the root cause. Pattern matching and hoping was clearly insufficient.

We saw two classes of this bug -- a crash while accessing invalid memory and an explicitly checked fatal error.

#### Fatal Error

goroutine 153 gp=0x4000105340 m=324 mp=0x400639ea08 [GC worker (active)]:
/usr/local/go/src/runtime/asm_arm64.s:244 +0x6c fp=0x7ff97fffe870 sp=0x7ff97fffe860 pc=0x55558d4098fc
runtime.systemstack(0x0)
 /usr/local/go/src/runtime/mgc.go:1508 +0x68 fp=0x7ff97fffe860 sp=0x7ff97fffe810 pc=0x55558d3a9408
runtime.gcBgMarkWorker.func2()
 /usr/local/go/src/runtime/mgcmark.go:1102
runtime.gcDrainMarkWorkerIdle(...)
 /usr/local/go/src/runtime/mgcmark.go:1188 +0x434 fp=0x7ff97fffe810 sp=0x7ff97fffe7a0 pc=0x55558d3ad514
runtime.gcDrain(0x400005bc50, 0x7)
 /usr/local/go/src/runtime/mgcmark.go:212 +0x1c8 fp=0x7ff97fffe7a0 sp=0x7ff97fffe6f0 pc=0x55558d3ab248
runtime.markroot(0x400005bc50, 0x17e6, 0x1)
 /usr/local/go/src/runtime/mgcmark.go:238 +0xa8 fp=0x7ff97fffe6f0 sp=0x7ff97fffe6a0 pc=0x55558d3ab578
runtime.markroot.func1()
 /usr/local/go/src/runtime/mgcmark.go:887 +0x290 fp=0x7ff97fffe6a0 sp=0x7ff97fffe560 pc=0x55558d3acaa0
runtime.scanstack(0x4014494380, 0x400005bc50)
 /usr/local/go/src/runtime/traceback.go:447 +0x2ac fp=0x7ff97fffe560 sp=0x7ff97fffe4d0 pc=0x55558d3eeb7c
runtime.(*unwinder).next(0x7ff97fffe5b0?)
 /usr/local/go/src/runtime/traceback.go:566 +0x110 fp=0x7ff97fffe4d0 sp=0x7ff97fffe490 pc=0x55558d3eed40
runtime.(*unwinder).finishInternal(0x7ff97fffe4f8?)
 /usr/local/go/src/runtime/panic.go:1073 +0x38 fp=0x7ff97fffe490 sp=0x7ff97fffe460 pc=0x55558d403388
runtime.throw({0x55558de6aa27?, 0x7ff97fffe638?})
runtime stack:
fatal error: traceback did not unwind completely
 stack=[0x4015d6a000-0x4015d8a000
runtime: g8221077: frame.sp=0x4015d784c0 top=0x4015d89fd0

#### Segmentation fault

goroutine 187 gp=0x40003aea80 m=13 mp=0x40003ca008 [GC worker (active)]:
 /usr/local/go/src/runtime/asm_arm64.s:244 +0x6c fp=0x7fff2afde870 sp=0x7fff2afde860 pc=0x55557e2d98fc
runtime.systemstack(0x0)
 /usr/local/go/src/runtime/mgc.go:1489 +0x94 fp=0x7fff2afde860 sp=0x7fff2afde810 pc=0x55557e279434
runtime.gcBgMarkWorker.func2()
 /usr/local/go/src/runtime/mgcmark.go:1112
runtime.gcDrainMarkWorkerDedicated(...)
 /usr/local/go/src/runtime/mgcmark.go:1188 +0x434 fp=0x7fff2afde810 sp=0x7fff2afde7a0 pc=0x55557e27d514
runtime.gcDrain(0x4000059750, 0x3)
 /usr/local/go/src/runtime/mgcmark.go:212 +0x1c8 fp=0x7fff2afde7a0 sp=0x7fff2afde6f0 pc=0x55557e27b248
runtime.markroot(0x4000059750, 0xb8, 0x1)
 /usr/local/go/src/runtime/mgcmark.go:238 +0xa8 fp=0x7fff2afde6f0 sp=0x7fff2afde6a0 pc=0x55557e27b578
runtime.markroot.func1()
 /usr/local/go/src/runtime/mgcmark.go:887 +0x290 fp=0x7fff2afde6a0 sp=0x7fff2afde560 pc=0x55557e27caa0
runtime.scanstack(0x40042cc000, 0x4000059750)
 /usr/local/go/src/runtime/traceback.go:458 +0x188 fp=0x7fff2afde560 sp=0x7fff2afde4d0 pc=0x55557e2bea58
runtime.(*unwinder).next(0x7fff2afde5b0)
goroutine 0 gp=0x40003af880 m=13 mp=0x40003ca008 [idle]:
PC=0x55557e2bea58 m=13 sigcode=1 addr=0x118
SIGSEGV: segmentation violation

Now we could observe some clear patterns. Both errors occur when unwinding the stack in(*unwinder).next. In one case we saw an intentionalfatal erroras the runtime identified that unwinding could not complete and the stack was in a bad state. In the other case there was a direct memory access error that happened while trying to unwind the stack. The segfault was discussed in theGitHub issueand a Go engineer identified it as dereference of a go scheduler struct,m, whenunwinding.

### A review of Go scheduler structs

Go uses a lightweight userspace scheduler to manage concurrency. Many goroutines are scheduled on a smaller number of kernel threads – this is often referred to as M:N scheduling. Any individual goroutine can be scheduled on any kernel thread. The scheduler has three core types –g(the goroutine),m(the kernel thread, or “machine”), andp(the physical execution context, or  “processor”). For a goroutine to be scheduled a freemmust acquire a freep, which will execute a g. Eachgcontains a field for its m if it is currently running, otherwise it will benil. This is all the context needed for this post but thego runtime docsexplore this more comprehensively.

At this point we can start to make inferences on what’s happening: the program crashes because we try to unwind a goroutine stack which is invalid. In the first backtrace, if areturn address is null, we callfinishInternaland abort because the stack was not fully unwound. The segmentation fault case in the second backtrace is a bit more interesting: if instead the return address is non-zero but not a function then the unwinder code assumes that the goroutine is currently running. It'll then dereference m and fault by accessingm.incgo(the offset ofincgointostruct mis 0x118, the faulting memory access).

What, then, is causing this corruption? The traces were difficult to get anything useful from – our service has hundreds if not thousands of active goroutines. It was fairly clear from the beginning that the panic was remote from the actual bug. The crashes were all observed while unwinding the stack and if this were an issue any time the stack was unwound on arm64 we would be seeing it in many more services. We felt pretty confident that the stack unwinding was happening correctly but on an invalid stack.

Our investigation stalled for a while at this point – making guesses, testing guesses, trying to infer if the panic rate went up or down, or if nothing changed. There wasa known issueon Go’s GitHub issue tracker which matched our symptoms almost exactly, but what they discussed was mostly what we already knew. At some point when looking through the linked stack traces we realized that their crash referenced an old version of a library that we were also using – Go Netlink.

goroutine 1267 gp=0x4002a8ea80 m=nil [runnable (scan)]:
runtime.asyncPreempt2()
 /usr/local/go/src/runtime/preempt.go:308 +0x3c fp=0x4004cec4c0 sp=0x4004cec4a0 pc=0x46353c
runtime.asyncPreempt()
 /usr/local/go/src/runtime/preempt_arm64.s:47 +0x9c fp=0x4004cec6b0 sp=0x4004cec4c0 pc=0x4a6a8c
github.com/vishvananda/netlink/nl.(*NetlinkSocket).Receive(0x14360300000000?)
 /go/pkg/mod/github.com/!data!dog/
[email protected]
/nl/nl_linux.go:803 +0x130 fp=0x4004cfc710 sp=0x4004cec6c0 pc=0xf95de0

We spot-checked a few stack traces and confirmed the presence of this Netlink library. Querying our logs showed that not only did we share a library – every single segmentation fault we observed had happened while preemptingNetlinkSocket.Receive.

### What’s (async) preemption?

In the prehistoric era of Go (<=1.13) the runtime was cooperatively scheduled. A goroutine would run until it decided it was ready to yield to the scheduler – usually due to explicit calls toruntime.Gosched()or injected yield points at function calls/IO operations. SinceGo 1.14the runtime instead does async preemption. The Go runtime has a threadsysmonwhich tracks the runtime of goroutines and will preempt any that run for longer than 10ms (at time of writing). It does this by sendingSIGURGto the OS thread and in the signal handler will modify the program counter and stack to mimic a call toasyncPreempt.

At this point we had two broad theories:

* This is a Go Netlink bug – likely due tounsafe.Pointerusage which invoked undefined behavior but is only actually broken on arm64
* This is a Go runtime bug and we're only triggering it inNetlinkSocket.Receivefor some reason

After finding the same bug publicly reported upstream, we were feeling confident this was caused by a Go runtime bug. However, upon seeing that both issues implicated the same function, we felt more skeptical – notably the Go Netlink library uses unsafe.Pointer so memory corruption was a plausible explanation even if we didn't understand why.

After an unsuccessful code audit we had hit a wall. The crashes were rare and remote from the root cause. Maybe these crashes were caused by a runtime bug, maybe they were caused by a Go Netlink bug. It seemed clear that there was something wrong with this area of the code, but code auditing wasn’t going anywhere.

## Breakthrough

At this point we had a fairly good understanding of what was crashing but very little understanding ofwhyit was happening. It was clear that the root cause of the stack unwinder crashing was remote from the actual crash, and that it had to do with(*NetlinkSocket).Receive, but why? We were able to capture acoredumpof a production crash and view it in a debugger. The backtrace confirmed what we already knew – that there was a segmentation fault when unwinding a stack. The crux of the issue revealed itself when we looked at the goroutine which had been preempted while calling(*NetlinkSocket).Receive.

(dlv) bt
0 0x0000555577579dec in runtime.asyncPreempt2
 at /usr/local/go/src/runtime/preempt.go:306
1 0x00005555775bc94c in runtime.asyncPreempt
 at /usr/local/go/src/runtime/preempt_arm64.s:47
2 0x0000555577cb2880 in github.com/vishvananda/netlink/nl.(*NetlinkSocket).Receive
 at
/vendor/github.com/vishvananda/netlink/nl/nl_linux.go:779
3 0x0000555577cb19a8 in github.com/vishvananda/netlink/nl.(*NetlinkRequest).Execute
 at
/vendor/github.com/vishvananda/netlink/nl/nl_linux.go:532
4 0x0000555577551124 in runtime.heapSetType
 at /usr/local/go/src/runtime/mbitmap.go:714
5 0x0000555577551124 in runtime.heapSetType
 at /usr/local/go/src/runtime/mbitmap.go:714
...
(dlv) disass -a 0x555577cb2878 0x555577cb2888
TEXT github.com/vishvananda/netlink/nl.(*NetlinkSocket).Receive(SB) /vendor/github.com/vishvananda/netlink/nl/nl_linux.go
 nl_linux.go:779 0x555577cb2878 fdfb7fa9 LDP -8(RSP), (R29, R30)
 nl_linux.go:779 0x555577cb287c ff430191 ADD $80, RSP, RSP
 nl_linux.go:779 0x555577cb2880 ff434091 ADD $(16<<12), RSP, RSP
 nl_linux.go:779 0x555577cb2884 c0035fd6 RET

The goroutine was paused between two opcodes in the function epilogue. Since the process of unwinding a stack relies on the stack frame being in a consistent state, it felt immediately suspicious that we preempted in the middle of adjusting the stack pointer. The goroutine had been paused at 0x555577cb2880, betweenADD $80, RSP, RSP and ADD $(16<<12), RSP, RSP.

We queried the service logs to confirm our theory. This wasn’t isolated – the majority of stack traces showed that this same opcode was preempted. This was no longer a weird production crash we couldn’t reproduce. A crash happened when the Go runtime preempted between these two stack pointer adjustments. We had our smoking gun.

## Building a minimal reproducer

At this point we felt pretty confident that this was actually just a runtime bug and it should be reproducible in an isolated environment without any dependencies. The theory at this point was:

1. Stack unwinding is triggered by garbage collection
2. Async preemption between a split stack pointer adjustment causes a crash
3. What if we make a function which splits the adjustment and then call it in a loop?

package main

import (
	"runtime"
)

//go:noinline
func big_stack(val int) int {
	var big_buffer = make([]byte, 1 << 16)

	sum := 0
	// prevent the compiler from optimizing out the stack
	for i := 0; i < (1<<16); i++ {
		big_buffer[i] = byte(val)
	}
	for i := 0; i < (1<<16); i++ {
		sum ^= int(big_buffer[i])
	}
	return sum
}

func main() {
	go func() {
		for {
			runtime.GC()
		}
	}()
	for {
		_ = big_stack(1000)
	}
}

This function ends up with a stack frame slightly larger than can be represented in 16 bits, and so on arm64 the Go compiler will split the stack pointer adjustment into two opcodes. If the runtime preempts between these opcodes then the stack unwinder will read an invalid stack pointer and crash.

; epilogue for main.big_stack
ADD $8, RSP, R29
ADD $(16<<12), R29, R29
ADD $16, RSP, RSP
; preemption is problematic between these opcodes
ADD $(16<<12), RSP, RSP
RET

After running this for a few minutes the program panicked as expected!

SIGSEGV: segmentation violation
PC=0x60598 m=8 sigcode=1 addr=0x118

goroutine 0 gp=0x400019c540 m=8 mp=0x4000198708 [idle]:
runtime.(*unwinder).next(0x400030fd10)
 /home/thea/sdk/go1.23.4/src/runtime/traceback.go:458 +0x188 fp=0x400030fcc0 sp=0x400030fc30 pc=0x60598
runtime.scanstack(0x40000021c0, 0x400002f750)
 /home/thea/sdk/go1.23.4/src/runtime/mgcmark.go:887 +0x290

[...]

goroutine 1 gp=0x40000021c0 m=nil [runnable (scan)]:
runtime.asyncPreempt2()
 /home/thea/sdk/go1.23.4/src/runtime/preempt.go:308 +0x3c fp=0x40003bfcf0 sp=0x40003bfcd0 pc=0x400cc
runtime.asyncPreempt()
 /home/thea/sdk/go1.23.4/src/runtime/preempt_arm64.s:47 +0x9c fp=0x40003bfee0 sp=0x40003bfcf0 pc=0x75aec
main.big_stack(0x40003cff38?)
 /home/thea/dev/stack_corruption_reproducer/main.go:29 +0x94 fp=0x40003cff00 sp=0x40003bfef0 pc=0x77c04
Segmentation fault (core dumped)

real 1m29.165s
user 4m4.987s
sys 0m43.212s

A reproducible crash with standard library only? This felt like conclusive evidence that our problem was a runtime bug.

This was an extremely particular reproducer! Even now with a good understanding of the bug and its fix, some of the behavior is still puzzling. It's a one-instruction race condition, so it’s unsurprising that small changes could have large impact. For example, this reproducer was originally written and tested on Go 1.23.4, but did not crash when compiled with 1.23.9 (the version in production), even though we could objdump the binary and see the split ADD still present! We don’t have a definite explanation for this behavior – even with the bug present there remain a few unknown variables which affect the likelihood of hitting the race condition.

## A single-instruction race condition window

arm64 is a fixed-length 4-byte instruction set architecture. This has a lot of implications on codegen but most relevant to this bug is the fact that immediate length is limited.addgets a 12-bit immediate,movgets a 16-bit immediate, etc. How does the architecture handle this when the operands don't fit? It depends –ADDin particular reserves a bit for "shift left by 12" so any 24 bit addition can be decomposed into two opcodes. Other instructions are decomposed similarly, or just require loading an immediate into a register first.

The very last step of the Go compiler before emitting machine code involves transforming the program intoobj.Progstructs. It's a very low level intermediate representation (IR) that mostly serves to be translated into machine code.

//https://github.com/golang/go/blob/fa2bb342d7b0024440d996c2d6d6778b7a5e0247/src/cmd/internal/obj/arm64/obj7.go#L856

// Pop stack frame.
// ADD $framesize, RSP, RSP
p = obj.Appendp(p, c.newprog)
p.As = AADD
p.From.Type = obj.TYPE_CONST
p.From.Offset = int64(c.autosize)
p.To.Type = obj.TYPE_REG
p.To.Reg = REGSP
p.Spadj = -c.autosize

Notably, this IR is not aware of immediate length limitations. Instead, this happens inasm7.gowhen Go's internal intermediate representation is translated into arm64 machine code. The assembler will classify an immediate inconclassbased on bit size and then use that when emitting instructions – extra if needed.

The Go assembler uses a combination of (mov, add) opcodes for some adds that fit in 16-bit immediates, and prefers (add, add + lsl 12) opcodes for 16-bit+ immediates.

Compare a stack of (slightly larger than)1<<15:

; //go:noinline
; func big_stack() byte {
; 	var big_stack = make([]byte, 1<<15)
; 	return big_stack[0]
; }
MOVD $32776, R27
ADD R27, RSP, R29
MOVD $32784, R27
ADD R27, RSP, RSP
RET

With a stack of1<<16:

; //go:noinline
; func big_stack() byte {
; 	var big_stack = make([]byte, 1<<16)
; 	return big_stack[0]
; }
ADD $8, RSP, R29
ADD $(16<<12), R29, R29
ADD $16, RSP, RSP
ADD $(16<<12), RSP, RSP
RET

In the larger stack case, there is a point betweenADD x, RSP, RSPopcodes where the stack pointer is not pointing to the tip of a stack frame. We thought at first that this was a matter of memory corruption – that in handling async preemption the runtime would push a function call on the stack and corrupt the middle of the stack. However, this goroutine is already in the function epilogue – any data we corrupt is actively in the process of being thrown away. What's the issue then?

The Go runtime often needs tounwindthe stack, which means walking backwards through the chain of function calls. For example: garbage collection uses it to find live references on the stack, panicking relies on it to evaluatedeferfunctions, and generating stack traces needs to print the call stack. For this to work the stack pointermust be accurate during unwindingbecause of how golang dereferences sp to determine the calling function. If the stack pointer is partially modified, the unwinder will look for the calling function in the middle of the stack. The underlying data is meaningless when interpreted as directions to a parent stack frame and then the runtime will likely crash.

//https://github.com/golang/go/blob/66536242fce34787230c42078a7bbd373ef8dcb0/src/runtime/traceback.go#L373

if innermost && frame.sp < frame.fp || frame.lr == 0 {
 lrPtr = frame.sp
 frame.lr = *(*uintptr)(unsafe.Pointer(lrPtr))
}

When async preemption happens it will push a function call onto the stack but the parent stack frame is no longer correct because sp was only partially adjusted when the preemption happened. The crash flow looks something like this:

1. Async preemption happens between the two opcodes thatadd x, rspexpands to
2. Garbage collection triggers stack unwinding (to check for heap object liveness)
3. The unwinder starts traversing the stack of the problematic goroutine and correctly unwinds up to the problematic function
4. The unwinder dereferencesspto determine the parent function
5. Almost certainly the data behindspis not a function
6. Crash

We saw earlier a faulting stack trace which ended in(*NetlinkSocket).Receive– in this case stack unwinding faulted while it was trying to determine the parent frame.

goroutine 90 gp=0x40042cc000 m=nil [preempted (scan)]:
runtime.asyncPreempt2()
/usr/local/go/src/runtime/preempt.go:306 +0x2c fp=0x40060a25d0 sp=0x40060a25b0 pc=0x55557e299dec
runtime.asyncPreempt()
/usr/local/go/src/runtime/preempt_arm64.s:47 +0x9c fp=0x40060a27c0 sp=0x40060a25d0 pc=0x55557e2dc94c
github.com/vishvananda/netlink/nl.(*NetlinkSocket).Receive(0xff48ce6e060b2848?)
/vendor/github.com/vishvananda/netlink/nl/nl_linux.go:779 +0x130 fp=0x40060b2820 sp=0x40060a27d0 pc=0x55557e9d2880

Once we discovered the root cause we reported it with a reproducer and the bug was quickly fixed. This bug is fixed ingo1.23.12,go1.24.6, andgo1.25.0. Previously, the go compiler emitted a singleadd x, rspinstruction and relied on the assembler to split immediates into multiple opcodes as necessary. After this change, stacks larger than 1<<12 will build the offset in a temporary register and then add that torspin a single, indivisible opcode. A goroutine can be preempted before or after the stack pointer modification, but never during. This means that the stack pointer is always valid and there is no race condition.

LDP -8(RSP), (R29, R30)
MOVD $32, R27
MOVK $(1<<16), R27
ADD R27, RSP, RSP
RET

This was a very fun problem to debug. We don’t often see bugs where you can accurately blame the compiler. Debugging it took weeks and we had to learn about areas of the Go runtime that people don’t usually need to think about. It’s a nice example of a rare race condition, the sort of bug that can only really be quantified at a large scale.

We’re always looking for people who enjoy this kind of detective work.Our engineering teams are hiring.

Cloudflare's connectivity cloud protects
entire corporate networks
, helps customers build
Internet-scale applications efficiently
, accelerates any
website or Internet application
,
wards off DDoS attacks
, keeps
hackers at bay
, and can help you on
your journey to Zero Trust
.
Visit
1.1.1.1
 from any device to get started with our free app that makes your Internet faster and safer.
To learn more about our mission to help build a better Internet,
start here
. If you're looking for a new career direction, check out
our open positions
.


Deep Dive
Go
Programming
