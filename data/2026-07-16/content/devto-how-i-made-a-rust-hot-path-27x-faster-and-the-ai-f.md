---
title: How I made a Rust hot path 27x faster, and the AI fix I refused to merge - DEV Community
url: https://dev.to/zacharylee/how-i-made-a-rust-hot-path-27x-faster-and-the-ai-fix-i-refused-to-merge-3llg
site_name: devto
content_file: devto-how-i-made-a-rust-hot-path-27x-faster-and-the-ai-f
fetched_at: '2026-07-16T03:36:58.540499'
original_url: https://dev.to/zacharylee/how-i-made-a-rust-hot-path-27x-faster-and-the-ai-fix-i-refused-to-merge-3llg
author: Zach
date: '2026-07-14'
description: Two years ago I open-sourced KeyEcho, a small desktop app that plays a mechanical-keyboard sound the... Tagged with rust, ai, performance, opensource.
tags: '#rust, #ai, #performance, #opensource'
---

Zero-copy audio and semantic AI errors

Two years ago I open-sourced KeyEcho, a small desktop app that plays a mechanical-keyboard sound the instant you press a key. It got 800+ stars. Then I shipped v0.0.5 in July 2024 and went quiet.

The issues never stopped. People asked for sound packs, reported platform bugs, and kept using a thing I had stopped maintaining. This month I came back and shipped 1.0 in a single PR: 130 files, 11,405 lines added and 9,292 removed. The core of it was a rebuild of the audio hot path. The cached-lookup microbenchmark went from 1184.07 ns/op with 66.84 KiB copied per key to 43.50 ns/op with zero sample bytes copied. That is 27x on the average slice and 38x on the largest.

I built it with an AI agent writing a lot of the code. This post is how the rework works, why Rust made that safe to do fast, and the one change the agent suggested that looked clean and would have quietly broken a feature.

## The hot path

KeyEcho's latency-sensitive path is short. A global keyboard hook fires on every key event. The first key-down of each press is pushed into a bounded queue. An audio thread pulls from the queue, maps the key to a slice of the selected sound pack, and plays it locally.

Because the path is short, anything left inside it is paid on every keystroke: any decode work, any allocation, any sample copy, any lock. The whole game is getting those out of the per-key path.

## v0.0.5 was already fast

Credit where it is due. v0.0.5 was a light, quick thing: Tauri + Rust, small builds, low memory; native keyboard listening I wrote by hand against each platform's API, with almost no unsafe; lossless WAV audio with no decompression step; and it already cached decoded audio in an LRU, so hitting the same key twice did not decode twice. It ran for two years and a few hundred people used it. It was not slow software.

But "already fast" and "no headroom left" are two different things. Even on a cache hit, each key press still copied the samples (66.84 KiB in the benchmark) and went through a global mutex shared with pack switching and volume changes. A cache miss still decoded on the spot. What 1.0 removed is exactly those: that copy, that lock, and the fact that cache misses happen at all.

## The rebuild

The rebuild came down to four moves.

Predecode once, when a pack is selected.A sound pack is a folder with asound.oggand aconfig.json. The config maps each key to a slice of the audio:key -> [start_ms, duration_ms]. When you select a pack, every slice is decoded up front, one time. Nothing decodes during a keystroke.

Deduplicate identical slices.Many keys point at the same slice, so decoding per key would decode the same audio many times. The builder keys a map on the(start_ms, duration_ms)pair, decodes each unique slice once, and shares it:

// Decode each unique slice once; identical slices share one buffer.

let
 
mut
 
slice_sources
:
 
HashMap
<
[
u64
;
 
2
],
 
AudioSource
>
 
=
 
HashMap
::
new
();

let
 
mut
 
key_sources
:
 
HashMap
<
Key
,
 
AudioSource
>
 
=
 
HashMap
::
new
();

for
 
(
key
,
 
slice
)
 
in
 
defines
 
{

 
let
 
source
 
=
 
slice_sources

 
.entry
(
slice
)

 
.or_insert_with
(||
 
{

 
let
 
[
start_ms
,
 
duration_ms
]
 
=
 
slice
;

 
let
 
samples
 
=
 
decode
(
start_ms
,
 
duration_ms
);
 
// Vec<f32>, once

 
AudioSource
::
new
(
Arc
::
from
(
samples
),
 
channels
,
 
sample_rate
)

 
})

 
.clone
();
 
// Arc clone, not a sample copy

 
key_sources
.insert
(
key
,
 
source
);

}

Enter fullscreen mode

Exit fullscreen mode

Zero-copy playback.Decoded samples live in anArc<[f32]>. A key lookup returns a clone of that Arc, which is a reference-count bump, not a sample copy. The per-key cost went to zero bytes copied.

Drop the global mutex.The old path guarded the current sound and the volume with a mutex. The new playback handle holds the current sound in anArcSwapOption<KeySound>and the volume in anAtomicU32(viaf32::to_bits). Looking up a key is a lock-free load:

struct
 
PlaybackSoundpack
 
{

 
current_sound
:
 
Arc
<
ArcSwapOption
<
KeySound
>>
,

 
volume_bits
:
 
Arc
<
AtomicU32
>
,

}

fn
 
source_for_key
(
&
self
,
 
key
:
 
Key
)
 
->
 
Option
<
(
AudioSource
,
 
f32
)
>
 
{

 
let
 
sound
 
=
 
self
.current_sound
.load
();
 
// lock-free

 
let
 
source
 
=
 
sound
.as_ref
()
?
.key_source
(
key
)
?
;
 
// map get + Arc clone

 
let
 
volume
 
=
 
f32
::
from_bits
(
self
.volume_bits
.load
(
Ordering
::
Relaxed
));

 
Some
((
source
,
 
volume
))

}

Enter fullscreen mode

Exit fullscreen mode

Predecoding trades work up front for RAM, so it needs two guardrails. Key events go through a bounded queue, so a burst applies backpressure instead of growing memory without limit. And a pack has to fit a decoded-sample budget of 10 MiB: before it loads, the app estimates decoded size from the unique slice durations and refuses anything larger. Predecoding is only safe when it is bounded.

## The numbers

Release-build microbenchmarks of the lookup path:

Path

v0.0.5

v1.0

Change

Cached lookup, average slice

1184.07 ns/op; 66.84 KiB copied

43.50 ns/op; 0 bytes copied

27.2x faster

Cached lookup, largest slice

1638.57 ns/op; 98.88 KiB copied

43.10 ns/op; 0 bytes copied

38.0x faster

Press/release gate

58.82 ns/tap; 2 messages

54.69 ns/tap; 1 message

half the messages

These are microbenchmarks of the lookup path, not end-to-end speaker latency, which depends on your OS and hardware. The method and memory budgets are indocs/performance.md, and the benchmarks ship in the repo. Runpnpm run bench:audioif you do not believe me.

## Why Rust made this safe to do fast

I leaned on the agent for most of this diff. The reason that felt safe is the compiler.

The borrow checker and the type system are the first reviewer for AI-generated code. Most wrong code does not survivecargo check. Moving shared audio buffers toArc<[f32]>and removing the mutex are exactly the changes where a mistake is an aliasing or aSend/Syncerror, and Rust rejects those at compile time, before they reach a human review or a user. The more of the diff an agent writes, the more that guardrail is worth.

## What the agent actually did

Not "it wrote the app." The useful work was narrower and, honestly, more valuable.

* Migration assistant.Tauri 1 to 2 touches config, permissions, the updater, and every plugin boundary. A partner that has read all the migration docs saves real hours.
* Hot-path auditor.It went through the old playback path with me line by line and drove the predecode, shared-buffer, no-mutex rework above.
* Backlog triage.I had it read every open issue and sort by what belonged in 1.0. One of them was a 10-month-old request from someone who had offered to pay for a specific sound. Replying to it after 1.0 turned into the project's first paying customer. The backlog was demand I had stopped reading.
* Benchmark and docs discipline.It kept the performance notes conclusion-first, reproducible, and honest about what the numbers do and do not measure.

I rarely gave step-by-step orders. I gave goals ("get sample copies in the key path to zero", "sort the backlog by what belongs in 1.0") and reviewed at the checkpoints. The speedups themselves come from the rework: predecoding, shared buffers, the dropped mutex, the bounded queue. The agent is what made finding, doing, and verifying that whole loop fast enough to actually happen.

## The change that looked clean and wasn't

This is the one I want you to steal.

CI for the Linux armv7 build failed under QEMU: libgit2 could not fetch a git dependency. The agent's fix was clean. Drop the git pin on the audio crate and use the crates.io release instead. CI went green.

I rejected it. That pin exists for a reason that is written nowhere in the code. It holdscpalat 0.18, which ships the default-device rerouting (and itsDeviceChangednotification) that makes the sound follow you when you unplug headphones or switch to a Bluetooth speaker. Reverting to the crates.io version silently downgradescpalto 0.17.3 and drops device-following. Two user issues, #41 and #20, were about exactly that behavior. No test covered "unplug the device and the sound follows," so nothing would have caught the regression except knowing why the pin was there.

The real fix was to vendor the dependencies withcargo vendorand build offline inside QEMU. The pin never moved.

Two lessons I now treat as rules:

1. Write the "why" next to every pin, hack, and magic number, in a comment or the project's AI rules file. Your agent has no memory of the incident that put it there. It is a talented engineer with zero context on your project.
2. Never accept a dependency version change you did not ask for, even when CI is green. A green pipeline proves the tests pass. It does not prove the tests cover what you are about to lose.

## What I cut

The armv7 build ran about two hours under emulation, and there was no clear user for 32-bit ARM Linux. I dropped it from 1.0.

An agent has no sense of sunk cost or opportunity cost. It will keep optimizing a build target forever if you let it. It can get arbitrarily close to "done." Deciding to stop is a human job.

## How the work was structured

Two smaller notes from shipping this.

Before release I ran an AI review pass inside git worktrees, so several agents could scan the code and propose fixes in parallel without touching the main tree. Each agent's output was a proposal, merged only after review. Exploration parallelizes cleanly. The synthesis still has to happen in one head, because each agent only sees its own slice.

The models are also starting to specialize. Claude Fable feels like an engineer who thinks outside the box and keeps surfacing angles I had missed. GPT-5.6 is the best executor I have used: hand it a decided plan and the code comes back close to perfect. It felt like running a two-person team where one thinks, one builds, and I decide and sign off.

## What 1.0 is

Still free, still open source. AGPL-3.0, small native installers, no account, no analytics. Rebuilt on Tauri 2 + SolidJS. Signed Windows builds and notarized macOS builds, which cut down unsigned-app warnings and antivirus false positives. Linux packages for x64 and ARM64.

You can try it without downloading anything: openkeyecho.appand type, and you will hear it in the browser. The benchmarks and method are in the repo.

I write a weekly build log about shipping real production systems with AI agents, honest numbers only. Subscribe atupweb.dev.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse