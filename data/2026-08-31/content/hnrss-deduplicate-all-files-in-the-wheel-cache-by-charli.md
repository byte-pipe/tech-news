---
title: 'Deduplicate all files in the wheel cache by charliermarsh · Pull Request #21327 · astral-sh/uv · GitHub'
url: https://github.com/astral-sh/uv/pull/21327
site_name: hnrss
content_file: hnrss-deduplicate-all-files-in-the-wheel-cache-by-charli
fetched_at: '2026-08-31T17:51:47.915393'
original_url: https://github.com/astral-sh/uv/pull/21327
date: '2026-08-31'
description: 'An extremely fast Python package and project manager, written in Rust. - Deduplicate all files in the wheel cache by charliermarsh · Pull Request #21327 · astral-sh/uv'
tags:
- hackernews
- hnrss
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 astral-sh

 

/

uv

Public

* NotificationsYou must be signed in to change notification settings
* Fork3.5k
* Star89.3k

## Conversation

### charliermarshcommentedAug 27, 2026•edited

 

Member

## Summary

On main, we support content-addressed caching, but only at the wheel-level. That is, if you download the same wheel twice from different sources, they share a cache entry. But fileswithinoracrosswheels are not deduplicated at all.

This PR adds deduplication at the file level: every file is now stored under its BLAKE3 hash in afiles-v0bucket. We hardlink these objects into their original locations inarchive-v0, so the installation step doesn't change at all -- we're just dedupingwithinthe cache (and cache cleanup removes file objects when their hardlink count drops to one).

In the prior proposal (#19694), we included the following table:

File selection

Additional savings

Files hardlinked

Distinct 
files-v0
 objects

Executables and native libraries

275.7 MiB

3,336

3,088

Any payload file ≥ 10 MiB

235.0 MiB

80

78

Any payload file ≥ 1 MiB

279.7 MiB

373

349

Any payload file ≥ 100 KiB

353.4 MiB

2,830

2,458

Any payload file ≥ 10 KiB

475.7 MiB

23,767

18,722

Any payload file ≥ 1 KiB

537.4 MiB

95,156

66,422

All payload files

545.2 MiB

134,222

87,129

So we're saving 545.2 MiB on my local machine, or about 10% of the cache.

In return, the net effect seems to be something like a <4% slowdown for cold installs (and no effect on warm installs), which I think isprobablyworthwhile here.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
🎉

3

 
wilson, alexfromapex, and RobertDeRose reacted with hooray emoji

 
🚀

34

 
ilkersigirci, madig, PixiBixi, blooalien, deadcoder0904, thomasmansencal, slaiyer, mattrighetti, pawelchcki, Pierre-Sassoulas, and 24 more reacted with rocket emoji

 
👀

3

 
EDM115, septatrix, and amingilani reacted with eyes emoji

 

All reactions

 

charliermarsh

temporarily deployed

 to
 automations

 
August 27, 2026 19:40
 — with 

GitHub Actions

 Inactive

astral-automations-bot

Bot

 mentioned this pull request
 

Aug 27, 2026

 Linux cargo-test setup fails when Depot runners lack Minix support
 
astral-sh/uv-dev#896

 

 Open

 

charliermarsh

temporarily deployed

 to
 automations

 
August 27, 2026 22:01
 — with 

GitHub Actions

 Inactive

### charliemarsh-oaicommentedAug 27, 2026•edited by charliermarsh

 

Contributor

N.B. Slop comment for benchmark data.

We benchmarked the optimization in85c3f7485against the binary-only cache ata3f977ece, with--preview-features content-addressed-cacheenabled on both. These are medians for the completeuv pip installprocess; positive changes mean slower.

Wheel

Cache

Parent median

Optimized median

Change (95% CI)

AnyIO 4.9.0

cold

90.4 ms

93.4 ms

+3.39% (+2.87% to +3.86%)

AnyIO 4.9.0

warm

29.9 ms

30.3 ms

+1.14% (-1.08% to +3.85%)

SymPy 1.14.0

cold

367.1 ms

381.6 ms

+3.95% (+3.49% to +4.46%)

SymPy 1.14.0

warm

84.6 ms

84.0 ms

-0.64% (-1.04% to -0.11%)

NumPy 2.2.6

cold

314.1 ms

326.5 ms

+3.95% (+3.24% to +4.82%)

NumPy 2.2.6

warm

62.5 ms

62.7 ms

+0.28% (-0.55% to +1.25%)

PyTorch 2.7.1+cpu

cold

2982.6 ms

3072.9 ms

+3.03% (+0.98% to +5.18%)

PyTorch 2.7.1+cpu

warm

404.0 ms

403.1 ms

-0.21% (-0.72% to +0.11%)

Before this optimization, the measured cold regressions were +4.02% for AnyIO 4.9.0, +19.41% for SymPy 1.14.0, +12.75% for NumPy 2.2.6, +15.30% for PyTorch 2.7.1+cpu.

All eight median regressions are below 5%.The PyTorch cold 95% interval still reaches 5.18%, so its upper bound is not below 5%. Every other upper bound is below 5%.

We retained all 1,860 measured installs, including outliers, and combined every confirmation run for this candidate. Cold measurements have 360 paired rounds for AnyIO, 120 each for SymPy and NumPy, and 90 for PyTorch; warm measurements have 60 paired rounds per wheel. Baseline/candidate order alternates, with three warmups per case. Intervals use a paired percentile bootstrap of the ratio of medians with 10,000 resamples.

These measurements ran on Linux/ext4, an AMD EPYC-Milan VM pinned to eight CPUs, with Python 3.12.13. Both binaries use Rust 1.98.0 and the sameprofilingprofile (optimized, no LTO). Each sample installs one pinned local wheel offline, without dependencies or bytecode compilation, using hardlinks into a fresh virtual environment. Cold removes the entire uv cache; warm retains a primed cache. Setup and cleanup are untimed, and the wheel OS page cache is warm. No compilation ran during the benchmarks. These results do not cover other platforms or network-inclusive installs.

All-file deduplication, content/executable identities, the cache layout, complete archives, and copy fallbacks are preserved. Inode checks confirmed that every archived file shares its file-store object for all four wheels. The five targeted integration tests passed ten stress iterations (50 executions), including local and streamed wheels with one and four workers, RECORD handling, cache cleanup, and cross-filesystem installation. Formatting and Clippy with warnings denied also passed.

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

charliermarsh

temporarily deployed

 to
 automations

 
August 27, 2026 23:35
 — with 

GitHub Actions

 Inactive

### codspeed-hqBotcommentedAug 27, 2026•edited

 

## Merging this PR willnot alter performance

✅ 25untouched benchmarks⏩ 12skipped benchmarks1

Comparingcharlie/dirhash-all-files(d12d2ad) withmain(7c1d80e)

## Footnotes

1. 12 benchmarks were skipped, so the baseline results were used instead. If they were deleted from the codebase,click here and archive them to remove them from the performance reports.↩

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

charliermarsh

 marked this pull request as ready for review

 
August 28, 2026 00:03

 

charliermarsh

force-pushed

 the
 

charlie/dirhash-binaries

 branch
 from
 
a3f977e
 to
 
1f28fd5
 
 

Compare

August 28, 2026 00:08

 

charliermarsh

force-pushed

 the
 

charlie/dirhash-all-files

 branch
 from
 
0a8edc0
 to
 
a108fab
 
 

Compare

August 28, 2026 00:08

 

charliermarsh

temporarily deployed

 to
 automations

 
August 28, 2026 00:09
 — with 

GitHub Actions

 Inactive

 

charliermarsh

 changed the base branch from
 

charlie/dirhash-binaries

 to
 

main

August 28, 2026 00:09

charliermarsh

 added
 

 enhancement

New feature or improvement to existing functionality

 preview

Experimental behavior

 labels

 
Aug 28, 2026

 

charliermarsh

 requested review from
 
woodruffw
 and 
 
zanieb

August 28, 2026 00:13

 

charliermarsh

temporarily deployed

 to
 automations

 
August 28, 2026 00:23
 — with 

GitHub Actions

 Inactive

charliermarsh

 mentioned this pull request
 

Aug 28, 2026

 Pipeline file cache publication for streamed wheels
 
#21333

 

 Draft

### astral-sh-botBotcommentedAug 28, 2026

 

## uv test inventory changes

This PR changes the tests when compared with themainbase revision.

* Added tests:5
* Removed tests:0
* Changed suites:2

uv-extract
: +1 / -0

Added:

* uv-extract::dirhash::archive::tests::extracted_file_executable_status

Removed:none

uv::pip_install
: +4 / -0

Added:

* uv::pip_install::pip_install::all_files_except_record_use_archive_file_store
* uv::pip_install::pip_install::binary_payload_copy_fallback_uses_archive_file_store
* uv::pip_install::pip_install::binary_payloads_stay_in_archive_without_preview
* uv::pip_install::pip_install::binary_payloads_use_archive_file_store

Removed:none

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

charliermarsh

 mentioned this pull request
 

Aug 28, 2026

 Store cached wheel permissions in archive manifests
 
#21334

 

 Draft

 

zsol

 self-requested a review

 
August 28, 2026 09:53

 This was referenced 
Aug 28, 2026

 Prefetch wheel central directories for streamed file publication
 
#21338

 

 Draft

 Pipeline wheel file publication with executable deferral
 
#21339

 

 Draft

charliemarsh-oai

 mentioned this pull request
 

Aug 28, 2026

 Reuse the hashing buffer across streamed wheel files
 
#21340

 

 Merged

charliermarsh
 

 added a commit
 that referenced
 this pull request

 

Aug 28, 2026

 

 

Reuse the hashing buffer across streamed wheel files (
#21340
)

…

dd85179

## Summary

When content hashing is enabled, we currently allocate and zero a new 64
KiB buffer for every file we copy and hash during streaming extraction.
This PR reuses one buffer across the wheel instead. For the PyTorch
wheel used in the benchmarks, that reduces buffer allocations for
hashing from 11,120 to one, while keeping the buffer size at 64 KiB per
active wheel.

The following measurements compare 
#21327
 at
`a188b8e833aef3c3b4b60a32ed9fafe6ac74186a` with this optimization
applied on top, before moving the change onto `main`. They are not
measurements against `main`. The Linux benchmarks alternate base and
candidate, using pinned wheels served over local HTTP with
content-addressed caching enabled:

| Cold install | 
#21327
 | 
#21327
 + buffer reuse | Change |
| --- | ---: | ---: | ---: |
| AnyIO | 110 ms | 107 ms | -2.6% |
| SymPy | 845 ms | 775 ms | -8.3% |
| NumPy | 627 ms | 567 ms | -9.5% |
| PyTorch CPU | 6.50 s | 5.99 s | -7.8% |
| 14-package environment, concurrency 4 | 6.95 s | 6.47 s | -7.0% |

The individual results above use 16 paired rounds; the full environment
uses 12. AnyIO, SymPy, and NumPy were repeated after an initial 20-pair
run: the initial AnyIO timings were noisy, while the initial SymPy and
NumPy improvements were 7.8% and 6.9%. All original samples were
retained. Cached installs and local-wheel controls showed no consistent
change. Across the initial runs, repeats, and controls, we measured 672
installs, excluding warmups and cache priming.

Co-authored-by: Charlie Marsh <charlie.r.marsh@gmail.com>

 

charliermarsh

force-pushed

 the
 

charlie/dirhash-all-files

 branch
 from
 
a188b8e
 to
 
694af80
 
 

Compare

August 28, 2026 16:56

 

charliermarsh

had a problem deploying

 to
 automations

 
August 28, 2026 16:57
 — with 

GitHub Actions

 Error

### charliermarshcommentedAug 28, 2026

 

Member

Author

Okay, I experimented with a bunch of alternatives to try and make this more performant:

* Store all files as non-executable, and then apply executable flags at install-time (Store cached wheel permissions in archive manifests#21334,Pipeline file cache publication for streamed wheels#21333). This would allow us to hardlink intofiles-v0while we unzip. Unfortunately, it also means we have tocopyevery executable that we want to install, since hardlinks share a mode. Ultimately, this was a bit tradeoff -- it was slower!
* Pre-fetching the central directory so that we can determine whether a given file is executable at extraction-time. (As-is, we only get the central directoryafterwe've unzipped, so we don't know if a file is executable untilafterit's been extracted.) This also turned out to be slower because we have additional overhead from making more HTTP requests.

I also considered something like "guess whether a file is executable" during extraction (and then, if we're wrong, copy it and change the mode after unzipping). I guess this could end up being more performant, but I wasn't very happy with the heuristics.

Ultimately, I think what we have here is good.

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

### charliermarshcommentedAug 28, 2026

 

Member

Author

If you bundle in#21340, I believe this is alsofasterthan before (i.e., gains from#21340outweigh the extra cost in this PR).

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

charliermarsh

temporarily deployed

 to
 automations

 
August 28, 2026 17:11
 — with 

GitHub Actions

 Inactive

 

charliermarsh

temporarily deployed

 to
 automations

 
August 28, 2026 17:28
 — with 

GitHub Actions

 Inactive

 17 hidden items
 

 Load more…
 

 

 
charliermarsh

and others

 added 
19
 commits
 
August 31, 2026 08:56

 

 

 

Simplify and document binary archive deduplication

4e7d0dc

 

 

 

Gate binary archive deduplication behind preview

5c29fbc

 

 

 

Simplify archive extraction and manifest validation

7b483f1

 

 

 

Share executable and large files with complete archives

412eb87

 

 

 

Expose the archive file size cutoff environment variable

fc6e334

 

 

 

Share executables and native libraries regardless of size

aed81af

 

 

 

Rename shared file and manifest cache buckets

7e944ef

 

 

 

Separate file-cache deduplication from installation

65f6c62

 

 

 

Keep cache-only callers and generated schema consistent

d0682a4

 

 

 

Model hashed and unhashed extraction explicitly

b6cdda1

 

 

 

Bundle hashed wheel metadata and trim helper tests

8acb8c8

 

 

 

Remove archive publication comment

7c10407

 

 

 

Avoid duplicate extracted wheel file records

390db4e

 

 

 

Deduplicate all files in the wheel cache

7818a02

 

 

 

 

Optimize wheel file cache publication

ef2a9b7

 

 

 

 

Exclude RECORD from wheel file deduplication

d2e340c

 

 

 

Include executable status in file cache hashes

b37fdee

 

 

 

Prune orphaned file objects when cleaning an unreferenced cache

af30c8c

 

 

 

Prune file objects once per cache clean

87bd56f

 

 

charliermarsh

force-pushed

 the
 

charlie/dirhash-all-files

 branch
 from
 
73c621b
 to
 
87bd56f
 
 

Compare

August 31, 2026 12:59

 

charliermarsh

temporarily deployed

 to
 automations

 
August 31, 2026 13:00
 — with 

GitHub Actions

 Inactive

 

 

Address wheel cache review feedback

d12d2ad

 

 

charliermarsh

temporarily deployed

 to
 automations

 
August 31, 2026 13:17
 — with 

GitHub Actions

 Inactive

charliermarsh

 mentioned this pull request
 

Aug 31, 2026

 Reuse cached small files during wheel extraction
 
#21375

 

 Draft

 
Hide details

View details

charliermarsh

 merged commit 
15bf04f

 into

 

main

Aug 31, 2026

 82 checks passed
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

charliermarsh

 
 deleted the
 

 charlie/dirhash-all-files

 

 branch

 
August 31, 2026 13:28

charliermarsh
 

 added a commit
 that referenced
 this pull request

 

Aug 31, 2026

 

 

Read file-cache link counts in bulk on macOS (
#21344
)

…

2577582

## Summary

Follow-up to 
#21327
.

Cache cleanup currently reads the hardlink count of every `files-v0`
object separately. On macOS, we can request names, file types, and link
counts in batches with `getattrlistbulk`, allocating paths only for
files with a single link.

Use this fast path for flat cache shards. We keep the existing walk on
other platforms, when bulk reads or required attributes aren't
available, and for nested directories. We don't follow symlinks, and
file removal still uses the existing storage accounting.

On macOS, with 87,129 distinct empty file objects across 256 shards and
two hardlinks per object, median full-command times across eight paired
warm-cache runs were:

| Command | Before | After |
| ------------------------------ | -----: | -----: |
| `uv cache clean <package>` | 386 ms | 105 ms |
| `uv cache clean <10 packages>` | 389 ms | 104 ms |
| `uv cache prune` | 386 ms | 101 ms |

These runs retain every object, so they measure scan cost rather than
deletion throughput. The scan is still single-threaded.

---------

Co-authored-by: Zanie Blue <contact@zanie.dev>

Foxhunt

 mentioned this pull request
 

Aug 31, 2026

 Daily Hacker News 31-08-2026
 
Foxhunt/daily-hackernews#783

 

 Open

github-actions

Bot

 mentioned this pull request
 

Aug 31, 2026

 [Trend Digest] Week of 2026-08-31
 
strikersam/autonomous-ai-agency#1397

 

 Open

blka

 mentioned this pull request
 

Aug 31, 2026

 Daily Hacker News 31/08/2026
 
blka/daily-hackernews#530

 

 Open

 

Sign up for free

to join this conversation on GitHub
.
 Already have an account?
 
Sign in to comment

Add this suggestion to a batch that can be applied as a single commit.
This suggestion is invalid because no changes were made to the code.
Suggestions cannot be applied while the pull request is closed.
Suggestions cannot be applied while viewing a subset of changes.
Only one suggestion per line can be applied in a batch.
Add this suggestion to a batch that can be applied as a single commit.
Applying suggestions on deleted lines is not supported.
You must change the existing code in this line in order to create a valid suggestion.
Outdated suggestions cannot be applied.
This suggestion has been applied or marked resolved.
Suggestions cannot be applied from pending reviews.
Suggestions cannot be applied on multi-line comments.
Suggestions cannot be applied while the pull request is queued to merge.
Suggestion cannot be applied right now. Please check back later.