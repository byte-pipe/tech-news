---
title: Tweede golf
url: https://tweedegolf.nl/en/blog/237/async-rust-never-left-the-mvp-state
site_name: hnrss
content_file: hnrss-tweede-golf
fetched_at: '2026-05-05T11:59:52.753823'
original_url: https://tweedegolf.nl/en/blog/237/async-rust-never-left-the-mvp-state
author: Dion
date: '2026-05-05'
description: I've previously explained async bloat and some work-arounds for it, but would much prefer to solve the issue at the root, in the compiler. I've submitted a Project Goal, and am looking for help to ...
tags:
- hackernews
- hnrss
---

May 4, 2026

# Async Rust never left the MVP state

Dion
Embedded software engineer
embedded
async
rust
I've previously explained async bloat and some work-arounds for it, but would much prefer to solve the issue at the root, in the compiler. I've submitted a Project Goal, and am looking for help to fund the effort.

I love me some async Rust! It's amazing how we can write executor agnostic code that can run concurrently on huge servers and tiny microcontrollers.

But especially on those tiny microcontrollers we notice that async Rust is far from thezero cost abstractionswe were promised. That's because every byte of binary size counts and async introduces a lot of bloat. This bloat exists on desktops and servers as well, but it's much less noticable when you have substantially more memory and compute available.

I've previouslyexplained some work-aroundsfor this issue, but would much prefer to get to the root of the problem, and work on improving async bloat in the compiler. As such I have submitted aProject Goal.

This is part 2 of my blog series on this topic. Seepart 1for the initial exploration of the topic and what you can do when writing async code to avoid some of the bloat. In this second part we'll dive into the internals and translate the methods of blog 1 into optimizations for the compiler.

What I won't be talking about is the often discussed problem of futures becoming bigger than necessary and them doing a lot of copying. People are aware of that already. In fact, there is an open PR that tackles part of it:https://github.com/rust-lang/rust/pull/135527

## Anatomy of a generated future

We're going to be looking at this code:

fn foo() -> impl Future<Output = i32> {
 async { 5 }
}

fn bar() -> impl Future<Output = i32> {
 async {
 foo().await + foo().await
 }
}

godbolt

We're using the desugared syntax for futures because it's easier to see what's happening.

So what does thebarfuture look like?

There are two await points, so the state machine must have at least two states, right?

Well, yes. But there's more.

Luckily we can ask the compiler to dump MIR for us at various passes. An interesting pass is thecoroutine_resumepass. This is the last async-specific MIR pass. Why is this important? Well, async is a language feature that still exists in MIR, but not in LLVM IR. So the transformation of async to state machine happens as a MIR pass.

Thebarfunction generates 360 lines of MIR. Pretty crazy, right? Although this gets optimized somewhat later on, the non-async version uses only 23 lines for this.

The compiler also outputs theCoroutineLayout. It's basically an enum with these states (comments my own):

variant_fields: {
 Unresumed(0): [], // Starting state
 Returned (1): [],
 Panicked (2): [],
 Suspend0 (3): [_s1], // At await point 1, _s1 = the foo future
 Suspend1 (4): [_s0, _s2], // At await point 2, _s0 = result of _s1, s2 = the second foo future
},

So what areReturnedandPanicked?

Well,Future::pollis a safe function. Calling it must not induce any UB, even when the future is done. So afterSuspend1the future returnsReadyand the future is changed to theReturnedstate. Once polled again in that state, the poll function will panic.

ThePanickedstate exists so that after an async fn has panicked, but the catch-unwind mechanism was used to catch it, the future can't be polled anymore. Polling a future in thePanickedstate will panic. If this mechanism wasn't there, we could poll the future again after a panic. But the future may be in an incomplete state and so that could cause UB. This mechanism is very similar to mutex poisoning.

(I'm 90% sure I'm correct about thePanickedstate, but I can't really find any docs that actually describe this.)

Cool, this seems reasonable.

## Why panic?

But is it reasonable? Futures in theReturnedstate will panic. But they don't have to. The only thing we can't do is cause UB to happen.

Panics are relatively expensive. They introduce a path with a side-effect that's not easily optimized out. What if instead, we just returnPendingagain? Nothing unsafe going on, so we fulfill the contract of theFuturetype.

I've hacked this in the compiler to try it out and saw a 2%-5% reduction in binary size for async embedded firmware.

So I propose this should be a switch, just likeoverflow-checks = falseis for integer overflow. In debug builds it would still panic so that wrong behavior is immediately visible, but in release builds we get smaller futures.

Similarly, whenpanic=abortis used, we might be able to get rid of thePanickedstate altogether. I want to look into the repercussions of that.

## Always a state machine

We've looked atbar, but not yet atfoo.

fn foo() -> impl Future<Output = i32> {
 async { 5 }
}

Let's implement it manually, to see what the optimal solution would be.

struct FooFut;
impl Future for FooFut {
 type Output = i32;
 
 fn poll(self: Pin<&mut Self>, _cx: &mut Context<'_>) -> Poll<Self::Output> {
 Poll::Ready(5)
 }
}

Easy right? We don't need any state. We just return the number.

Let's see what the generated MIR is for the version the compiler gives us:

// MIR for `foo::{closure#0}` 0 coroutine_resume
/* coroutine_layout = CoroutineLayout {
 field_tys: {},
 variant_fields: {
 Unresumed(0): [],
 Returned (1): [],
 Panicked (2): [],
 },
 storage_conflicts: BitMatrix(0x0) {},
} */

fn foo::{closure#0}(_1: Pin<&mut {async block@src\main.rs:5:5: 5:10}>, _2: &mut Context<'_>) -> Poll<i32> {
 debug _task_context => _2;
 let mut _0: core::task::Poll<i32>;
 let mut _3: i32;
 let mut _4: u32;
 let mut _5: &mut {async block@src\main.rs:5:5: 5:10};

 bb0: {
 _5 = copy (_1.0: &mut {async block@src\main.rs:5:5: 5:10});
 _4 = discriminant((*_5));
 switchInt(move _4) -> [0: bb1, 1: bb4, otherwise: bb5];
 }

 bb1: {
 _3 = const 5_i32;
 goto -> bb3;
 }

 bb2: {
 _0 = Poll::<i32>::Ready(move _3);
 discriminant((*_5)) = 1;
 return;
 }

 bb3: {
 goto -> bb2;
 }

 bb4: {
 assert(const false, "`async fn` resumed after completion") -> [success: bb4, unwind unreachable];
 }

 bb5: {
 unreachable;
 }
}

Yikes! That's a lot of code!

Notice at line 4 that we still have the 3 default states and at line 22 that we're still switching on it. There's a big optimization opportunity here that we're not using, i.e. to have no states and always returnPoll::Ready(5)on every poll.

I've also hacked this in the compiler and it saved 0.2% of binary size. Not a lot, but it's quite a simple optimization, so likely still worthwhile.

It does change the behavior a bit, but only for executors that aren't compliant. It means that the future always returnsReady. The behavior in the compiler right now is that any subsequent polls will panic.

## LLVM to the rescue?

Ok, so the MIR output isn't great. But LLVM will pick up the pieces right?

Well, sometimes, yeah. But only when the futures are simple enough and you're runningopt-level=3. If the future grows too complex (which happens fast because futures nest very deeply in idiomatic async Rust code) or you're optimizing for size (which we often do with embedded or wasm), LLVM doesn't optimize this all away.

Here's an example in godbolt:https://godbolt.org/z/58ahb3nne

If you look through the generated assembly, you'll notice that it does know thatfooreturns 5, but that it doesn't optimize the answer ofbarto be 10. The poll function offoois also still called. This is done because of the potential panic the compiler can't fully account for. It doesn't realizefoois only called once and won't ever panic in practice.

If we comment out the panicking branch in the IR, we see it gets optimized better:https://godbolt.org/z/38KqjsY8E

LLVM is not our savior here sadly. We really do need to give it good inputs.

It does better withopt-level=3, but eventually can't keep up either when the code gets less trivial. And that's because we're relying on LLVM to spot that it should optimize out the things we're asking it to do.

## Futures aren't (trivially) inlined

Inlining is great since it enables further optimization passes. Sadly, generated Rust futures are never inlined. After each future gets its implementation, then LLVM and the linker get an opportunity to do inlining. But as we've seen above, that's too late.

The prime opportunity for inlining is this:

async fn foo(blah: SomeType) -> OtherType {
 // ...
}

async fn bar(blah: SomeType) -> OtherType {
 foo(blah).await
}

This is a pattern that happens a lot when creating abstractions using traits. With the current compiler,bargets its own state machine that calls thefoostate machine, which is very wasteful. Instead,barcould alsobecomefooby just returning thefoofuture.

Things get a little more difficult when we add a preamble and a postamble to the example.

async fn foo(blah: bool) -> i32 {
 // ...
}

async fn bar(input: u32) -> i32 {
 let blah = input > 10; // Preamble
 let result = foo(blah).await;
 result * 2 // Postamble
}

This pattern is common when translating an async function from one signature to another, which happens for trait impls.

Note thatbardoesn't need any async state of its own here either. No data is kept over the single await point that isn't captured byfoo.barcan't simplybecomefoo, but we can mostly rely on the state offoo. The manual implementation would be something like:

enum BarFut {
 Unresumed { input: u32 },
 Inlined { foo: FooFut }
}
impl Future for BarFut {
 type Output = i32;
 
 fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output> {
 // Ignoring pin projection here
 loop {
 match self {
 Unresumed { input } => {
 let blah = input > 10; // Preamble
 *self = BarFut::Inlined { foo: foo(blah) };
 },
 Inlined { foo } => {
 break foo
 .poll(cx)
 .map(|result| result * 2) // Postamble
 },
 }
 }
 }
}

That's a lot better than what's currently generated. If only we were allowed to execute the code up to the first await point, then we could get rid of theUnresumedstate. But "futures don't do anything unless polled" isguaranteed, so we can't change that.

There are more optimizations you could do with inlining if you were able to query properties of the futures you're polling. I don't think this is possible, at least not with the current architecture in rustc. Every async block is transformed individually and no data is kept about it afterwards.

For example, if you could query if a future always returns ready at the first poll, you wouldn't have to create a state for the await point in the future of the caller. If that were possible and you could apply these optimizations recursively, you could collapse a lot of futures into much simpler state machines.

I haven't tested out inlining yet, but I think this would significantly help binary size and performance.

## Collapsing states

The state machine gets an extra state for each await point in the async block. But there's code where multiple states could be collapsed into 1.

Take this example:

pub async fn process_command() {
 match get_command() {
 CommandId::A => send_response(123).await,
 CommandId::B => send_response(456).await,
 }
}

It's very natural to write it that way. But what happens is that we're getting two identical states:

/* coroutine_layout = CoroutineLayout {
 field_tys: {
 _s0: CoroutineSavedTy { // Identical to _s1
 ty: Coroutine(
 DefId(0:11 ~ mir_test[b831]::send_response::{closure#0}),
 [
 (),
 std::future::ResumeTy,
 (),
 (),
 (u32,),
 ],
 ),
 source_info: SourceInfo {
 span: src/main.rs:13:25: 13:49 (#14),
 scope: scope[0],
 },
 ignore_for_traits: false,
 },
 _s1: CoroutineSavedTy { // Identical to _s0
 ty: Coroutine(
 DefId(0:11 ~ mir_test[b831]::send_response::{closure#0}),
 [
 (),
 std::future::ResumeTy,
 (),
 (),
 (u32,),
 ],
 ),
 source_info: SourceInfo {
 span: src/main.rs:14:25: 14:49 (#16),
 scope: scope[0],
 },
 ignore_for_traits: false,
 },
 },
 variant_fields: {
 Unresumed(0): [],
 Returned (1): [],
 Panicked (2): [],
 Suspend0 (3): [_s0], // 2 states
 Suspend1 (4): [_s1],
 },
 storage_conflicts: BitMatrix(2x2) {
 (_s0, _s0),
 (_s1, _s1),
 },
} */

The MIR for this function is 456 lines long and many basic blocks are essentially duplicates.

We can refactor the code manually to:

pub async fn process_command() {
 let response = match get_command() {
 CommandId::A => 123,
 CommandId::B => 456,
 };
 send_response(response).await;
}

Here we don't get the duplicate states:

/* coroutine_layout = CoroutineLayout {
 field_tys: {
 _s0: CoroutineSavedTy {
 ty: Coroutine(
 DefId(0:11 ~ mir_test[b831]::send_response::{closure#0}),
 [
 (),
 std::future::ResumeTy,
 (),
 (),
 (u32,),
 ],
 ),
 source_info: SourceInfo {
 span: src/main.rs:16:5: 16:34 (#14),
 scope: scope[1],
 },
 ignore_for_traits: false,
 },
 },
 variant_fields: {
 Unresumed(0): [],
 Returned (1): [],
 Panicked (2): [],
 Suspend0 (3): [_s0],
 },
 storage_conflicts: BitMatrix(1x1) {
 (_s0, _s0),
 },
} */

The total MIR length is now 302 lines and nothing is duplicated.

So it seems like a good optimization pass to search for identical code paths and states and collapse them into one. This optimization probably stacks well with the inlining pass.

## Some testing results

* ReplaceReturned' panic withPoll::Pending: 2-5% binary size savings on embedded.
* When no await, no statemachine: 0.2% binary size savings on embedded.
* Together: ~3% perf increase on x86 in synthetic benchmark withsmolexecutor.

Future inlining should have a greater effect again.

Ultimately it's hard to know the improvements until after it can be benched in real systems.

## Summary

Hopefully this article shed some light on some of the async Rust issues!

I would love to work on these items in the compiler:

* Returnedstate no longer panics in release mode
* Async blocks without awaits should not get state machines, but just return ready every time
* Future inlining for futures with a single await
* Collapse identical states

Links to my hacks:

* No panics in poll after ready:https://github.com/rust-lang/rust/compare/main...diondokter:rust:resume-pending
* No await, no statemachine:https://github.com/rust-lang/rust/compare/main...diondokter:rust:no-statemachine-when-no-await

## Supporting this Project Goal

I want to work on this in the compiler and as such have submitted it as a Project Goal:https://rust-lang.github.io/rust-project-goals/2026/async-statemachine-optimisation.html

But I need your help because I can't do much without funding.

If you're with a company or organization that would benefit from this work and would be willing to (partially) fund it, please contact me atdion@tweedegolf.com. The scope is flexible and so is the amount of funding required. However, I have estimated that €30k could get all or at least a lot of this work done.

Dion
Embedded software engineer
dion@tweedegolf.com
embedded
async
rust

## Stay up-to-date

Stay up-to-date with our work and blog posts?

## Related articles

April 13, 2026

### Debloat your async Rust

Async Rust is amazing, but far from flawless. In this blog, I'll walk you through the current struggles and possible solutions.
embedded
async
rust
Read article
September 15, 2025

### Embedded async debugging and inspect-embassy

As part of my internship at Tweede golf this summer I was tasked with improving the async debugging experience for embedded development. This work resulted in a prototype async debugger for embassy, a common async runtime for embedded systems.
development
embedded
async
rust
Read article
January 31, 2022

### Async Rust vs RTOS showdown!

It's time for another technical blog post about async Rust on embedded.
This time we're going to pitch Embassy/Rust against FreeRTOS/C on an STM32F446 microcontroller.

embedded
IoT
async
rust
Read article