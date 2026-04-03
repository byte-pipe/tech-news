---
title: 'Garnix Blog: Forwardly-evaluated build systems'
url: https://garnix.io/blog/garn2/
site_name: lobsters
content_file: lobsters-garnix-blog-forwardly-evaluated-build-systems
fetched_at: '2026-02-13T06:00:38.901824'
original_url: https://garnix.io/blog/garn2/
date: '2026-02-13'
description: Some of the many caches that can be used to make build systems evaluate faster.
tags: nix, performance
---

Nov 2, 2026
Julian K. Arni

# Forwardly-evaluated build systems

Some of the many caches that can be used to make build systems evaluate faster.

Build tools are very attentive to opportunities of caching build artifacts —
that's a large part of their job.
One area that is neglected caching of theevaluationneeded to figure out what to build
— even though in some of these systems that phase can be very slow!
In Nix in particular, large monorepos can see evaluation timesin the minutes,
which substantially increases CI times. At the other end of the spectrum, smaller
projects too soon hit UX difficulties with Nix as evaluation is on the critical
path for commands like entering a devshell. There, shaving off even a couple
dozen milliseconds matters.

In our own work on an alternative Nix frontend, we looked at various
techniques for speeding up evaluation by caching. The results are very
promising, and the techniques applicable in other projects.

# Context

The Nix pipeline is roughly this:

A Nix expression is evaluated; the result should be a derivation datatype. Those
are serialized into derivation files, which are the normalized build recipes.
The builder then builds these and puts the resulting artifacts in the Nix store.

The derivation files constitute the interface between Nix-the-language and
Nix-the-builder. Given this API, there is no reason why a different surface
language couldn't be used.

A while back, we decided to try to make TypeScript the frontend language. It's
familiar to a lot more people, and moreover, Nix has a lot of problems that
come from being relatively obscure (it's slower, has less nice error messages,
documentation generation is bad, LSPs aren't as advanced, etc.). The result
wasgarn.

Our first version looked like this:

It created Nix strings in TypeScript, and then passed it on to the usual
pipeline. The experience ofwritinggarn files was great, but because of
this extra step, everything was slower.

That's quite unfortunate, because slowNixevaluation is already a problem.
To fix this, the natural thing to do is to skip Nix evaluation entirely. TypeScript
is a faster language than Nix, so that should be a good basis to start. We created
a new TypeScript runtime that takes the V8 sandbox (via the great Deno/rustyscript
libraries), removes almost all the primops that are side-effects (writing files,
doing network fetches, random numbers), and put in just:

* readFile(file: string). Reads a file *from within the same directoryas thegarn.ts`/entrypoint file.
* path(path: string, { gitignore?: bool }). Given a directory, adds
(potentially filtering) all files of the directory to a read-only copy, and
returns the path of that copy (which is named by the hash of the contents).
* import(URL/file/git-repo: string). Read a file or git repo from a URL or
local file path. If it's a remote file, add its hash toGarn.lock.

In other words, we made TypeScript be a pure and deterministic language ifGarn.lockand the entire directory is considered as input. In fact, it is
deterministic as a function of Garn.lock and exactly the files it reads during
execution. (This observation, we'll see, is crucial: it means we can make the
cache key depend on actual dependencies, rather than the entire repository.)

We've been calling this versiongarn2,
though throughout this blog I'll refer to it as simply “garn” when that is not
ambiguous.

Using TypeScript seems to have paid off — our baseline performance is
quite good.

Benchmark 1: garn.ts (change Cargo.toml)
 Time (mean ± σ): 455.1 ms ± 35.1 ms [User: 292.5 ms, System: 90.9 ms]
 Range (min … max): 413.4 ms … 530.5 ms 10 runs

Benchmark 2: default.nix (change Cargo.toml)
 Time (mean ± σ): 877.1 ms ± 25.8 ms [User: 571.8 ms, System: 102.1 ms]
 Range (min … max): 836.0 ms … 928.3 ms 10 runs

Benchmark 3: flake.nix (change Cargo.toml)
 Time (mean ± σ): 1.603 s ± 0.205 s [User: 0.721 s, System: 0.127 s]
 Range (min … max): 1.420 s … 1.972 s 10 runs

(A note on methodology: for each type of benchmark, we run the build first, so
libraries etc. are imported. Then we change a source file, and time the build
again (doing this 10 times each). We'll come back to why there's such a big
difference betweendefault.nixandflake.nix.)?

The story of getting to that baseline is for another time. In this blog
post we're going to improve that, specifically with caching.

# Trace-based caching

Nix, when used with flakes, has a form of evaluation caching. It stores maps
between repo state and flake output attributes to value; so if you evaluatedpackages.x86_64-linux.fooand it returns/nix/store/...-foo.drv, that
mapping will be cached. If you again evaluated that same attribute, Nix won't
have to compute it again.

This saves time, but only in the very narrow case where it applies. Most
notably, ifanythingchanges in the repository, all the caches are
invalidated.?Even if the change is to something completely unrelated to your evaluation, it
will invalidate the cache.

This is annoying locally, but in CI, and especially for monorepos, this is a big
missed opportunity.

Instead, what garn does is, on evaluation, keep a record of the hash
ofgarn.ts,andof all reads that the evaluation did. If you imported
something, or calledpathorreadFile, that's tracked. The result is also
cached at the end.

On subsequent runs, garn checks whether it has a cache for that version ofgarn.ts. If it does, it checks what reads the last run did, and whether the
results are all the same now. If so, it returns the cached value.?It's safe to do this because garn scripts are as pure as a
function of those inputs.

Benchmark 1: garn.ts (change nothing)
 Time (mean ± σ): 16.8 ms ± 3.0 ms [User: 4.4 ms, System: 12.5 ms]
 Range (min … max): 9.9 ms … 22.7 ms 39 runs

Benchmark 2: default.nix (change nothing)
 Time (mean ± σ): 865.7 ms ± 31.5 ms [User: 581.1 ms, System: 100.4 ms]
 Range (min … max): 812.8 ms … 914.5 ms 10 runs

Benchmark 3: flake.nix (change nothing)
 Time (mean ± σ): 213.2 ms ± 4.2 ms [User: 54.6 ms, System: 24.0 ms]
 Range (min … max): 206.6 ms … 219.2 ms 10 runs

garn takes about2%of the timedefault.nixdoes, and 7% of the (also cached)flake.nix!

The above is a comparison of evaluating whennothinghas changed. But for garn,the cache is only invalidated when it should be. If you have a
package that only reads some directories or files, and imports only certain
modules, it will retain its evaluation cache if onlyotherthings change.

Benchmark 1: garn.ts (change README.md)
 Time (mean ± σ): 15.8 ms ± 1.4 ms [User: 4.3 ms, System: 11.8 ms]
 Range (min … max): 11.4 ms … 18.4 ms 44 runs

Benchmark 2: default.nix (change README.md)
 Time (mean ± σ): 808.9 ms ± 30.5 ms [User: 572.8 ms, System: 103.2 ms]
 Range (min … max): 753.2 ms … 849.0 ms 10 runs

Benchmark 3: flake.nix (change README.md)
 Time (mean ± σ): 1.112 s ± 0.026 s [User: 0.728 s, System: 0.119 s]
 Range (min … max): 1.089 s … 1.171 s 10 runs

(In the repo we are benchmarking,flatbuffers, 97% of commits don't touch the Rust code. Theflake.nixcache is not
helpful for 100% of commits; the garn cache is valid for 97% of them. The
percentage won't always be this high, of course.)

When you have large projects where evaluation alone is
huge, that's a big deal, not just in terms of time, but also in terms of the
memory usage you can save.

This cache avoids even entering the V8 runtime entirely. But there's a downside
to it: if certain computations that are expensive are used by two different
outputs (e.g.,garn build fooandgarn build barboth compute somebaz),
the cache won't be reused between them. (The Nix flake cache also suffers from
this.) We'll return to this.

This isn't a new idea.fabricate,memoize,rattleand others have based build systems
on tracing effects.Spall et al (2022)call these build systemsforward
build systems; unlikeMakeand the like, they don't reason backwards from
a target, satisfying its dependencies, but instead run the build script forwards
once, keeping track of its dependencies. Most of them usestraceor the like
(on Linux) to observe these dependencies or side effects. The ideal is that
you can runan unmodified program(e.g. a bash script) and get an
automatically cachable version of it. The possible side effects in an arbitrary
Linux program are, however, huge, and keeping track of them efficiently and
correctly is quite difficult. This is even harder to do in a cross-platform way.
As a result, these programs fall somewhat short of their ideal. With garn, on
the other hand, we keep track of side-effects at a language level, which is
much easier to do and do correctly.

These programs are also about forwardbuilds; what garn is doing is using
tracing atevaluation time, to figure out what the build recipe is.

# Adding incrementalism

There's a pattern that a lot of big Nix repos use to bring down their
evaluation time that would be abominable if it weren't necessary. It's moving
evaluation into IFDs so that the evaluation is cachedas a build artifact.
There are a few ways of doing this, but one is to check the output ofnix eval <expensive computation>to your git repo, regenerating as needed. Then
you have your Nix code import that.

The problem isn't only that keeping generated code in your repo, and keeping it
up-to-date, is a pain. It's also that the existence of IFD itself negatively
affects the performance of evaluation. Suddenly you have to spin up a whole
sandbox, and potentially install in it a lot of software, to calculate some
value. This is made worse by the fact that there is no concurrency and very
little parallelism in Nix (in evaluation, at any rate). Moreover, because Nix
builds are only “best-effort” deterministic (not doing anything about
non-determinism introduced by parallelism, for example), IFD degrades the
determinism ofevaluationto that otherwise-lower level one of builds.

But there is an important idea there. It's to split the expensive computation
into parts, so that one part depends on as little as possible, so as to get
a form of incrementalism. After all, even if our previous cache wasprecise,
in that it didn't invalidate a computation unless it really had to, it was
all-or-nothing: either theentirecomputation was cached or none of it.

Our approach to supporting a form of user-guided incrementalism was to
provide language-level access to something very similar to the cache mentioned
in the previous section. The API is via a functionmemoize, that takes two
arguments: afilewith amainfunction to be memoized, and the arguments to
call it with. The file can have imports, or read files, just like everything
else. (It can evenitselfcallmemoize!). Additionally, it can callgetArgsto get its arguments. These effects are tracked as above. On rerun,
if its reads didn't change, the result can be taken from the cache. Because it
is a separate file, it is easy to prevent mutable variables from being shared
between the computation that's memoized and the world outside (which would
compromise cache correctness). (This is in fact the same reasoning that led
Web Workers to being designed the way they did, as a separate script. The
motivation there relates to parallelism rather than memoization, but the
solution is the same. Indeed, ourmemoizeusesweb workers, which has the
added advantage of providing more opportunities for parallelism.)

This approach of trackinggetArgsas aneffect, we realized, makes it
possible to solve the problem we encountered earlier, of the cache not being
shared between different computations. The original design of garn makes the
available targets be whatever derivations/packages you happen to export; garn
does the job of matching the name you provided in the command line (e.g.,fooingarn build foo) with a variable yourgarn.tsexported. But we could
instead provide agetTargetfunction which returns the targetand track its
usage as an effect. Any calls tomemoizethat happenbeforegetTargetwon't be invalidated (if none of the other reads changed).

The results:

Benchmark 1: garn.ts (change rust/flatbuffers/src/lib.rs)
 Time (mean ± σ): 311.5 ms ± 14.2 ms [User: 227.6 ms, System: 76.3 ms]
 Range (min … max): 283.9 ms … 330.7 ms 10 runs

Benchmark 2: default.nix (change rust/flatbuffers/src/lib.rs)
 Time (mean ± σ): 866.4 ms ± 20.2 ms [User: 570.0 ms, System: 97.2 ms]
 Range (min … max): 836.4 ms … 892.5 ms 10 runs

Benchmark 3: flake.nix (change rust/flatbuffers/src/lib.rs)
 Time (mean ± σ): 1.552 s ± 0.173 s [User: 0.715 s, System: 0.128 s]
 Range (min … max): 1.402 s … 2.006 s 10 runs

About 70% of the time of the uncached version (which was, as a reminder, 455ms),
and nearly one fifth offlake.nix. Not bad, but not as fast as the
fully-cached computation, which was in fact 10x faster.

This is as far as we've implemented caches. But let's consider what could be
improved next.

# Partial evaluation

There are few reasons for this difference:

* You have to spin up the whole V8 VMsince there is stuff to do before and
after getting the memoized value.
* You actually have to do (i.e., compute) that stuff
* What's in the cache could be quite big, and storing and retrieving that takes more time
* You then have to pass a relatively big datastructure from TypeScript into
Rust, and let it be processed.

If you're trying to get the eval down from a fewminutesto a few
seconds or a few hundred milliseconds, that might not be relevant; but if you
also care about going down totens of milliseconds, it matters a lot.

If you look at most stacks, they follow a common pattern: there are a couple of
files (Cargo.toml,Cargo.lock,package.json,package-lock.json,<project>.cabal, etc.) which determinealmost everythingabout the
resulting derivation — i.e., of the build —exceptwhat source files
are in the directory when the build kicks off. Almost all the work that happensduring the evaluationdoesn't need to know about the actual source. It also
happens that those config and lock files change much more rarely than source
files themselves.

In essence, we have something likebuildPackage(configFiles, src) -> Derivation,
but it's possible to split it intobuildPackageBuilder(configFiles) -> (src -> Derivation)such that all the expensive work happens by the time the first function returns.
If we could in this way partially evaluatebuildPackageand then cache the
result, we would have evaluations that are essentially instantaneousunless a config file changes. Caching e.g. a parsed config file might only be
part of the computation that's independent ofsrc, and it's not always easy
to refactor things to include more of it. But if we could return the partially
evaluated function, things would be much easier.

Functions aren't serializable, at least not easily; since the cache is persistent,
that means we can't cache the function itself.

The “common” case is that we return a datatype (the derivation) that doesn't vary
structurally based on the source, but only in the values of certain primitive
fields (mostly strings/paths). So when user code returns a value that has a source
path, we can figure out where in that value the source is used (by diffing two
versions of it, by just inspecting the string, or by more reasonable but
involved techniques such as keeping metadata of usage, sort of like “taints”).
We can then in the Rust side do as much processing as doesn't touch that value
(adding dependency derivations and calculating hashes), and then store just the
remainder, with a pointer to what needs to be changed. We even control the
length of the string, so it might even be possible to operate directly on the
bytes of the persisted data.

The problem we had is that calls topathinvalidate the cache, even though
usually the path is just abuild-timedependency (in the sense that
the derivations generally produced when paths differ differonlyby substitution
of one path by the other; there's no branching or parsing of the store path
going on). We came up with a technique for very fast caching in case that
assumption of howpathis used is true. To make this safe, the type returned
bypathmust be opaque so it can never be inspected.

The upside of all this is a fast cache that does not get invalidated by
calls topath, and which requires no change from the user's side.
All of that is quite a bit of work, however. So far we've been treating this
version of garn as more of an exploration; most of these caches took only
a couple of days to implement. Likely we won't continue in this direction for
now, but it's good to know the option exists.

# Conclusion

Here are all the results gathered together:

Not bad.

Though this version of garn can already build itself, it is by no means ready
for production, and not only because of missing features. It's an experimental
implementation, about exploring ideas more than being production-grade. (It
also involved a fair bit of LLM code.) The code itself can be foundhere.

Besides caching, there are lots of ways performance can be (or has been)
improved. A lot of these are also really exciting.

In theory a lot of these improvements could be ported to Nix as well:
Nix-the-language is already deterministic and has a way to control access to mutable
variables (it disallows them altogether), which are the main requirements. In
practice I suspect they would require too much change in the codebase to be
realistic.

If you have open source repositories where evaluation is in the minutes, reach
out to us! Having these examples is great for guiding performance improvements.

Similarly, if you would like to collaborate on garn in some capacity, also
reach out, onMatrix,Discord, or byemail.

## Other Posts:

Dec 17, 2025
Julian K. Arni

## Hardware-Attested Nix Builds

Read Article
→

More confidence in the integrity of your Nix artifacts.

Nov 25, 2025
Julian K. Arni

## garnix actions

Read Article
→

Running Nix apps outside a sandbox

Oct 30, 2025
Alex David, Sönke Hahn, and Julian K. Arni

## Fix your FODs

Read Article
→

A supply-chain attack on Nix, and our approach to solving it.

View Archive
→

## Say hi, ask questions, give feedback

Discord
→
Matrix
→
Report an issue
→
