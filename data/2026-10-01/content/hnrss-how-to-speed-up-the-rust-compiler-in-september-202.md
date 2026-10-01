---
title: How to speed up the Rust compiler in September 2026 | Nicholas Nethercote
url: https://nnethercote.github.io/2026/09/30/how-to-speed-up-the-rust-compiler-in-september-2026.html
site_name: hnrss
content_file: hnrss-how-to-speed-up-the-rust-compiler-in-september-202
fetched_at: '2026-10-01T17:18:26.241248'
original_url: https://nnethercote.github.io/2026/09/30/how-to-speed-up-the-rust-compiler-in-september-2026.html
date: '2026-10-01'
published_date: '2026-09-30T00:00:00+00:00'
description: My last post on the Rust compiler’s performance was two months ago and a lot has happened since then.
tags:
- hackernews
- hnrss
---

Mylast
poston the Rust compiler’s performance was two months ago and a lot has happened
since then.

## Overall progress

The measurements for the period 2026-07-29 to 2026-09-28 can be seenhere.

The mean wall-time reduction was 4.57%, which is a remarkable improvement in
just two months. Of the 629 benchmark measurements, 555 of them improved and
only 74 regressed. A number of benchmarks saw double-digit percentage
reductions. The technical term for this result is “a sea of green”.

## rustdoc

In my last post I mentioned howNoah Levgot some
enormous speed wins on rustdoc. He recently wrotea
postexplaining in
some detail exactly how he did this. It’s an interesting and satisfying read.

## Clippy

#159642: In this PRJakub Beránekenabled PGO for Clippy, giving
wall-time improvements across most Clippy benchmarks, in the best case by 18%!

## LLVM update

#158734: In this PRNikita
Popovupgraded the LLVM version used by the compiler
to LLVM 23. As often happens when we upgrade LLVM, we saw some nice speedups.
The mean wall-time reduction across all benchmarks was 1.2%, which might not
sound like much but is really impressive for a single PR. Great work from the
LLVM folks!

## The new borrow checker

The new borrow checker,PoloniusAlpha(no relation toNapoleonDynamite), wasenabled on
Nightly.
It is more precise than the existing borrow checker and accepts some valid
programs that the old borrow checker would reject. It does do more work than the
old borrow checker, enough to make a measurable difference to compile time in a
minority of cases, including the popularserdecrate. Fortunately,Jack
Hueyhas been on the case.

#161938: In this PR Jack made
some liveness computations lazy, which reduced instruction counts forserdeby 3-5%, and for some other benchmarks by less than 1%.

#163027: In this PR Jack
adjusted a data structure and tweaked some inlining, for mostly sub-1%
instruction count reductions across numerous benchmarks.

There is more work to be done to reduce the remaining Polonius Alpha
regressions, but it’s worth noting that the “sea of green” shows these
regressions were swamped by the many other recent improvements.

## The new trait solver

The new trait solver,PenelopeHammertime,[Ed. note: is that right?]was alsoenabled on
Nightly.

As I said, a lot has been happening.

Like the new borrow checker, the new trait solver is slower in a minority of
cases.Jana Dönszelmannwrote adetailed
postabout the efforts to
improve the performance of this new solver.

Jana’s post is detailed enough that I won’t say much more about the large
amount of ongoing work on the new solver, but I will mention in passing the PRs
I made:#160479,#160605,#160801,#160892,#161077,
and#161211.
Some of these reduced compile times greatly for certain outlier crates: 50%
here, 25% there, 15% there, andeven
moreon one stress test. And I am not the only one who has made progress here… go
read Jana’s post.

## xmakro

New contributorxmakrocontinued their run of good
improvements.

#157281: In this PR xmakro
optimized impl handling when building the specialization graph. This gave a
mean cycle count reduction of 1.58% across all benchmarks, which is huge for a
single PR.

#158059: In this PR xmakro
optimized one aspect of the loading of incremental compilation data, reducing
instruction counts across multiple benchmarks, in the best case by 6%.

#160473: In this PR xmakro
avoided some allocations in a hot obligations processing path, reducing
instruction counts across numerous benchmarks, in the best case by 2%.

#160268: In this PR xmakro
avoided a lot of allocations by changing the old/new trait solver selection
code to use static dispatch instead of dynamic dispatch. This gave mostly
sub-1% instruction count reductions across a number of benchmarks. This hot
allocation path had been showing up in profiles for a while and I had earlier
tried exactly the same idea in#155714. But I got regressions
on a couple of benchmarks, possibly due to slightly different choices of where
to place some#[inline]attributes. It was good to see this obvious
inefficiency fixed.

## Dataflow analysis

#160193: In this PR I changed
the CFG traversal algorithm used by the dataflow analyses in the compiler.
These analyses iterate to a fixpoint and the traversal algorithm can affect how
quickly the fixpoint is reached. For most code the new algorithm makes no
difference, but thecranelift-codegencrate has one enormous function with
over 18,000 basic blocks. The old algorithm required 1.5 million calls toapply_effects_in_blockto reach a fixpoint for theEverInitializedPlacesanalysis used by the borrow checker; the new algorithm requires 90,000. This
gave an enormous ~30% wall-time reduction for acheckbuild of this crate.

#160033: In this PR I madeEverInitializedPlacesmore efficient again, this time by not tracking
unnecessary data for projections. This reduced instruction counts on thematch-stressbenchmark by 17%, and on a few other benchmarks by less than 1%.

## LLMs

They’ve gotten very good at certain kinds of analysis. I’m still writing all my
own code and text, because (a) that’s paramount, and (b) theproject
policyrequires it, but I
had useful LLM analysis assistance on several of the PRs mentioned in this post.

Anyway, enough about that.

## Miscellaneous

#160535: In this PRChris
Dentonincreased the default stack size used
by the compiler, which allowed the removal ofensure_sufficient_stack, a
manual stack extension mechanism sprinkled about in places prone to high levels
of recursion. There was a lot of discussion about this one because it can be
difficult to decide how to best deal with stack exhaustion. But the performance
effects are clear, with reduced instruction counts across many benchmarks, in
the best case by almost 3%.

#160506: The project uses a
lot of “rollup” PRs, where multiple PRs are merged together. This is because we
don’t have sufficient CI capacity to merge every PR individually. Normally PRs
that affect performance are merged by themselves so we can measure their
effects clearly. For the first time ever, at one point we had so many
performance improvement PRs waiting in the merge queue thatJonathan
Brouwercreated a rollup containing 10
performance-improving PRs to keep things moving! This is a good problem to
have. And later on we had#162859which contained four
performance-improving PRs. (You needn’t worry about unexpected effects slipping
in because we have the ability to run the perf benchmark suite on the
individual PRs after merging, to make sure each PR had the expected performance
effect.)

#162747: In this PR I made
some minor improvements to the code that lowers AST to HIR. It was a cleanup
that wasn’t expected to affect performance but it reduced instruction counts
across numerous benchmarks, in the best case by 1.5%. Sometimes you get lucky.

## Job status

Tomorrow I will start working atHexcaton thecompiler
performance
optimizationsproject goal. It’s exciting! Many thanks to Mara Bos, Predrag Gruevski, and all
the other people who helped make this happen.

### Editor’s postscript

The new solver’s name is notPenelopeHammertime; that was a joke.

#### Author’s postscript

Its real name isPineappleHäagen-Dazs.