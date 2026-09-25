---
title: Fearless SIMD v1.0 is here - Linebender
url: https://linebender.org/blog/fearless-simd-1-0/
site_name: hnrss
content_file: hnrss-fearless-simd-v10-is-here-linebender
fetched_at: '2026-09-25T15:44:51.823498'
original_url: https://linebender.org/blog/fearless-simd-1-0/
date: '2026-09-22'
description: Fearless SIMD v1.0 is here
tags:
- hackernews
- hnrss
---

# Fearless SIMD v1.0 is here

### Shnatsel, September 22, 2026

fearless_simdtakesunsafeout of SIMD.

It has come a long way since theoriginal prototype 8 years ago. We are now confident that whatever it is you need, be it just autovectorization and multiversioning, or full-blown portable SIMD abstractions, or safe access to intrinsics and nothing more, Fearless SIMD will serve you well.

Instead of paraphrasing thechangelog, I'd like to take this opportunity to reflect on the goals of Fearless SIMD, how it achieves them, and what sets it apart from other SIMD abstractions.

# Performance

A common criticism leveled at portable SIMD abstractions is that they aren't performant enough, so we've put a lot of effort into making sure that Fearless SIMD never holds you back.

For example, when implementing portable abstractions for operations with different behavior in edge cases on different platforms, such asswizzlesorfloating-point maximum, we provide both a precise variant that's the same on all platforms, and a fast variant that returns a platform-dependent result for use when you expect the edge cases to never happen.

We also made it easy toexpress SIMD algorithms in terms of the hardware's native vector size, so that your code always takes full advantage of the hardware, no matter where it runs. Fixed vector sizes are also supported for algorithms that need them.

We also put a lot of effort into making sure the implementations of our portable SIMD operations are state-of-the-art, and even contributed improvements upstream - both toRustandLLVM.

But if you need an instruction that isn't covered by portable abstractions, or want even more control, you cansafely drop down to platform intrinsicswith no overhead for the parts of your code that need it, and keep the rest simple and portable.

Thanks to safe access to intrinsics, thereisno performance ceiling.

# Safety

If you look up the source code of any other SIMD abstraction, you will find that it is full ofunsafecode. Something likerg unsafewill turn up severalthousandunsafeblocks.

But not in Fearless SIMD! The crate is carefully engineered not to require ad-hocunsafecode.

One piece of the puzzle is thekernel! macro, which leans ontarget feature v1.1in the compiler to invoke most SIMD intrinsics withoutunsafe. I have described the design in detailin an earlier blog post, so check this out if you'd like to learn more.

That removes most of the ad-hocunsafe, but doesn't cover SIMD load/store operations which operate on raw pointers. That's where oursafe transmute module, inspired by crates such asbytemuckandzerocopy, comes into play.

SIMD intrinsics like_mm_loadu_epi32may seem special, but actually turn into plain loads and stores behind the scenes. So you can fully replicate their functionality with asingle, reusable wrapper.

Thanks to the power of Rust's type system, we only need to audit these two small, self-contained building blocks. As long as they are memory-safe, the rest of the codebase is guaranteed to be memory-safe as well.

At last, SIMD in Rust can be truly fearless.

# Ergonomics

Function multiversioning is tricky.

Previous solutions eitherrequire adding#[inline(always)]annotationsand understanding their implications, orimpose a small overhead on every function call. The latter is fine most of the time, but degrades performance on very small functions, and still requires you to surgically add#[inline(always)]to get around that.

Both are leaky abstractions - you still need to think about what is happening under the hood!

Alongsidefearless_simdv1.0, we are launchingfearless_simd_macrosv0.1, which provides a non-leaky abstraction: the#[simd]macro. With it, you don't have to think about what's happening under the hood at all! Put it on any SIMD function and it Just Works.

That said, while this is a big step forward for the ecosystem, there is stillsome boilerplateinvolved. We are keen to reduce it further, either with compiler support via theStruct Target Features RFCto get rid of the#[simd]annotation entirely, or perhaps throughother trickswe will explore in the future.

And if you don't like procedural macros, the old way of doing things is still available, if less convenient.

Ergonomics is the one area we expect may still evolve. But this does not compromise the stability guarantees of the corefearless_simdcrate, and the code written today with or without the#[simd]macro will continue working indefinitely.

# Stability

Fearless SIMD is here to stay. We will be providing3 years of security updatesfor v1.0 and all later versions.

While we cannot see the future, there are viable paths to supporting both near-term Rust features, such as thef16type, and longer-term features such asSVEandRISC-V Vector Extensionif/when these hardware extensions become relevant, without API-breaking changes.

## Relation to std::simd

We would love to seestd::simdstabilized, but it would not make Fearless SIMD obsolete.

The Rust standard library implements only the parts that absolutely have to be in it, and the rest (e.g. multiversioning, hardware-width vectors) is left up to the ecosystem crates.

fearless_simdincludes an equivalent ofstd::simdthat works on stable Rust, but that is just one part of a bigger whole.

Oncestd::simdis stabilized, we will port Fearless SIMD to it to delete a lot of custom code and gain support for all sorts of obscure platforms. But the need for ecosystem crates such asfearless_simdwill remain.

# Adoption

It doesn't matter how brilliant your crate is if nobody is using it.

Fearless SIMD is already used by30 other cratesas a direct dependency, and is indirectly relied on byover a thousand crates!

It already underpins a nontrivial fraction of the Rust ecosystem, and we hope that v1.0 will take this even further.

If you'd like to use Fearless SIMD in your project, check out thedocumentationandexamples, and feel free to ask questionson Zulip!