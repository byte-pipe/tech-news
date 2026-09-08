---
title: 'GitHub - argonautlabsai/deltafin: ARGODRIVE Deltafin: Kimi K3 (2.8T MoE) streamed from SSDs on Apple Silicon — fork of gavamedia/deltafin with the ARGODRIVE storage work and benchmark package · GitHub'
url: https://github.com/argonautlabsai/deltafin
site_name: hnrss
content_file: hnrss-github-argonautlabsaideltafin-argodrive-deltafin-k
fetched_at: '2026-09-09T08:37:29.415265'
original_url: https://github.com/argonautlabsai/deltafin
date: '2026-09-08'
description: 'ARGODRIVE Deltafin: Kimi K3 (2.8T MoE) streamed from SSDs on Apple Silicon — fork of gavamedia/deltafin with the ARGODRIVE storage work and benchmark package - argonautlabsai/deltafin'
tags:
- hackernews
- hnrss
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 argonautlabsai

 

/

deltafin

Public

 forked from 
gavamedia/deltafin

* NotificationsYou must be signed in to change notification settings
* Fork0
* Star24

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu
 
 

## Latest commit

 

## History

45 Commits
45 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
 
 
docs
docs
 
 
k3-public-bench
k3-public-bench
 
 
native
native
 
 
research/
study
research/
study
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
CREDITS.md
CREDITS.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# ARGODRIVE Deltafin

TL;DR— Kimi K3 (2.8T-parameter MoE, 1.45 TB of expert weights) running on one M5 Max MacBook Pro with 128 GB, experts streamed from four SSDs.

* 1.00 tok/ssteady decode over a 512-token answer; 1.13 over 128; 0.96 on the public 17-token prompt (upstream reported 0.68).
* The honest limit:a 512-token prompt takes ~6.3 minutes to its first token. Cause found (prefill re-reads each layer's experts 8×), fix planned, not built.
* Useful findings:one drive gives ≈52% of four-drive speed, two ≈73%, three ≈90% — the slowest of each layer's 16 reads sets the pace, not total bandwidth.
* Every number is one cold run with the exact prompt; per-run logs and placement manifests are ink3-public-bench/.
* Fork ofgavamedia/deltafin(MIT), who built the engine — seeCREDITS.md. Instruments:ARGODRIVE.

## ARGODRIVE Deltafin benchmarks — M5 Max, 128 GB, experts streamed from four SSDs

Measured 2026-09-08 with this fork's configuration of record
(k3-public-bench/env.sh); every number is one cold
run with the exact prompt, and the per-run logs are ink3-public-bench/results/.

test

drafter off

drafter on

steady decode, 512 generated tokens

0.9232 tok/s

1.0015 tok/s

steady decode, 128 generated tokens

0.9261

1.1252

17-token prompt from issue #15 (upstream reported 0.684 there), median of 3

—

0.9631

time to first token, 512-token prompt

≈376 s

≈375 s

Drive-count ladder on the same prompts: one drive ≈52% of the four-drive
speed, two full mirrors ≈73%, three ≈90% (results/SCALING.md).
Why prefill is slow and what fixes it:results/PREFILL.md.
Definitions, identity scope and precision statement:k3-public-bench/README.md.

	____ _ _ __ _
	| _ \ ___| | |_ __ _ / _(_)_ __
	| | | |/ _ \ | __/ _` | |_| | '_ \
	| |_| | __/ | || (_| | _| | | | |
	|____/ \___|_|\__\__,_|_| |_|_| |_|

## Run thefull, never-pruned, 2.8-trillion-parameterKimi K3on consumer hardware, as "fast" as possible

Deltafin is a single native binary that runs full Kimi K3. Nothing pruned. Nothing skipped. K3 decides every token.

All 16 experts, every single token. No shortcuts, no "close enough." It's exactly what Moonshot shipped.

The quality rule is simple:K3 itself decides every token, and nobody else. Small draft models are allowed to guess ahead (that's where much of the speed comes from), but K3 checks every guess, and nothing reaches you without its official sign-off.

### Upstream benchmarks on an M1 Max laptop (gavamedia/deltafin, unchanged — not this fork's numbers)

* 0.2901 token/s (3.447 s/token) — 1.9% higher throughput than last update

#### Upstream's historical M1 benchmarks:

* 0.2847 token/s (August 2, 2026) — 7.0% higher throughput
* 0.2660 token/s (July 30, 2026) — 102.9% higher throughput
* 0.1311 token/s (July 28, 2026) — 829.8% higher throughput
* 0.0141 token/s (July 27, 2026)

## Mission Statement

Pure raw uncut K3 quality, as fast as possible.Speed mustnever come from reducing model quality. Deltafin keeps all 16 routed experts and the full K3 target as the sole authority for every single token.

Our goal is to squeeze out every last drop of efficiency possible when running a huge model like K3, with all options on the table...except for reducing quality.

## But Why?!?

Deltafin is not a product pitch. It is an experiment in how far consumer hardware can be pushed, and what we can learn by attempting something so challenging.

Kimi K3 targets infrastructure on the scale of 16 nodes and roughly 4.8 TB of aggregate VRAM. That means the full 2.8T parameters and the 1M-token context window, with the expert bank never pruned. On any home setup, this is an extreme constraint. Every 1% improvement is very hard-won. But each gain can teach something.

Research and exploration is the point.Thatis our mission. Not everything has to be a "minimum viable product" to impress venture capitalists. If Deltafin helps make frontier models usable on a $15,000 home setup, instead of a$2,000,000 infrastructurelike Kimi recommends, we believe that is worthwhile progress on our self-hosted AI journey. Plus everything learned along the way could even benefit other projects in unexpected ways.

“We choose to run the full 2.8-trillion-parameter model locally, and do the other things, not because they are easy, but because they are hard.”
— John F. Kennedy probably

Other projects appear to run full K3, somehow faster. But look closer: they've re-encoded K3's expert bank down to ~3 bits. Clever engineering toward a different goal: the smallest K3 that fits and is "close enough." Those weights are no longer the ones Moonshot released, and nobody, including them, has measured what those compromises cost.

Deltafin is the other experiment: every expert byte exactly as Moonshot shipped it, made as fast as physics allows.

## 1. New Installation

Deltafin installs almost everything it needs. SeeRequirementsif you're missing anything.

#
 1. Get it

git clone https://github.com/gavamedia/deltafin.git

cd
 deltafin

#
 2. Build it

cargo build --locked --release

#
 3. Download the FULL 1.7 TB K3 model to disk (optional, but fastest)

./target/release/deltafin setup --full

Or, if you don't have enough disk space:

#
 3. Stream K3 as you use it (slower, but 215 GB to start) 

./target/release/deltafin setup --stream

setup --streaminstalls the resident model and fetches exact experts on-demand only, initially running far more slowly when routes have no local cache yet. As you build up your cache over time, this can be a way to save space, storing only the parts of the model you use, running entirely off cache on disk.

#### Default DSpark (and optional Qwen)

The normal setup includesInferact's Kimi-K3-DSpark. It takes6.635 GiB on diskand approximately4.49 GiBwhen admitted at runtime. Deltafin avoids materializing DSpark's redundant copy of K3's embedding. Chat and server requests use DSpark automatically when beneficial; any failures, insufficient headroom, or bad live economics simply leaves full K3 running by itself.

Qwen is a separate add-on for faster raw text continuation:

#
 4. Optionally install qwen later

./target/release/deltafin setup-qwen

Qwen speeds up raw completion only: the small models guess what comes next, K3 checks the guess, and you get identical output in less time. That helps code autocomplete and other/v1/completionstraffic, plusdeltafin run --prompt ...— one measured 17-token completion ran2.7× fasterwith the same output IDs.

This adds4.337 GiBon disk, and because Qwen willnotimprove chat speed, we make it an optional add-on. You can add it to a fresh install withdeltafin setup --full --include-qwen, or add it later with the command above.

## 2. Upgrading

From the Deltafin folder:

./target/release/deltafin upgrade

upgradegets what you need, and rebuilds the binary. Models, converted weights, and caches are left alone. It never re-runs setup or re-downloads K3.

#### NOTE: Upgrading from our old python version? Inspect it first:

git status --short

#
 ⬆️ Continue only when that returns nothing

git pull --ff-only
cargo build --locked --release
./target/release/deltafin upgrade

Continue only whengit status --shortis empty. If it lists files, preserve or commit that work yourself, rather than allowing an upgrade procedure to guess. Existing model data remains in the same repository-root directories.

upgradeneeds a clean, non-diverged branch, and it remembers how the binary was built, so an NVIDIA/CUDA build stays a CUDA build rather than quietly falling back to CPU. Anything unexpected safely stops the upgrade.

upgradeignores build environment variables — it reuses whatever the binary was already built with. So to switch configuration (CPU to CUDA, say, or a moved LibTorch tree), runcargo build --locked --releaseyourself once with the new variables set; seeRequirements. That becomes the recorded setup, and later upgrades keep it.

## 3. Use from the command line

#
 Chat: apply K3's audited chat template and stop at the model's end marker.

./target/release/deltafin run --chat \
 --prompt 
"
What are the three largest moons of Saturn?
"

#
 Raw continuation: cap output because raw text has no chat end boundary.

./target/release/deltafin run \
 --prompt 
"
The capital of France is
"
 --max-new 17

#
 Add cumulative throughput and native transaction statistics.

./target/release/deltafin run \
 --prompt 
"
The largest planet in our solar system is
"
 --max-new 17 --stats

Without--stats, generated text streams normally instead of printing one diagnostic line per token.--max-new Nlimits new tokens; it does not alter the prompt or context. Chat output stops at K3's control boundary, while raw completion should normally use a bound.

Long conversations are far slower than short completions — prefill and cache grow with history, and startup prints the actual usable context bound.

## 4. Use through an OpenAI-compatible server

./target/release/deltafin serve --host 127.0.0.1 --port 8000

curl http://127.0.0.1:8000/v1/chat/completions \
 -H 
'
Content-Type: application/json
'
 \
 -d 
'
{"model":"deltafin-kimi-k3","stream":true,"messages":[{"role":"user","content":"Hello!"}]}
'

The native server implements/v1/chat/completions,/v1/completionsand/v1/models, including server-sent-event streaming. Point an OpenAI-compatible client athttp://127.0.0.1:8000/v1and use any non-empty local API key expected by that client.

The server implements a deliberately small, strictly-checked subset of the OpenAI API — text-only, one generation at a time, always greedy and reproducible — and refuses anything it cannot honor exactly with a normal OpenAI-shaped error instead of silently ignoring it. Growing chats automatically benefit from exact conversation-state reuse, draft-verified DSpark speedups and an exact-response memo; every accepted field, refusal rule and caching detail is inthe server reference.

The default server response ceiling is one million tokens. Lower it with--max-tokens Nwhen integrating clients, and raise client timeouts because full K3 responses are slow. Request JSON is bounded by--max-request-bytes(128 MiB by default). Keep the server on loopback unless you add your own authentication and network boundary.

## Documentation

* How the native runtime works— the one-binary in-process design: Rust core, C-ABI providers, router tracing, expert prefetch and native tokenization.
* OpenAI-compatible server reference— exactly which API fields are accepted or refused, the automatic chat speedups, and the exact-response memo.
* Health checks— read-only, network-free auditors that verify the runtime and each installed component after an install, upgrade or problem.
* Native storage preparation— the default row-int8 resident spine that setup prepares for you, selecting the original BF16 explicitly, packing either into contiguous DFSP files, and lossless scale4 expert sidecars.
* Performance reference— how to reproduce measurements with the benchmark harness, and the established M1 Max reference results.
* Configuration— the few flags and environment variables that matter, and the quality guard behind them.
* Supported platforms— what each host class runs (MPS/Metal, CUDA, native CPU) and the evidence status per platform.
* Development reference material— why historicaltools/*.pyfiles remain in the tree as frozen reference material the native runtime never executes.

## Credits

Deltafin exists because other people published amazing work:

* Moonshot AIreleased K3's weights, architecture and readable model semantics.
* Inferactreleased the unchanged K3-specific DSpark checkpoint;TorchSpecdocuments its training framework, and thevLLM teampublished K3 integration and recurrent/attention cache research. Deltafin's native runtime, verifier, scheduling and state transactions are its own.
* GigaToken, byMarcel Rød, inspired Deltafin's automatic stable-order parallel tokenization path for large server histories.
* Maurice Brown (trumb)contributed Linux, aarch64, x86 SIMD and NVIDIA findings plus DGX Spark measurements inpull request #2. Deltafin retained those findings behind reviewed capability and ABI gates.
* colibridemonstrated aggressive MoE streaming and router-lookahead ideas.ds4 / DwarfStarprovided especially clear prior art for exact expert streaming, cache ownership and correctness-first measurement.
* Qwensupplies the optional 0.6B/1.7B proposal-only raw-completion models.
* flash-linear-attention,PyTorch,llama.cpp/ggml,tiktokenand the broader local-model community supplied essential semantics and prior art.

Exact provenance and distribution boundaries are recorded inThird-party provenance and notices.

## License

Deltafin's tracked project code isMIT. Kimi K3 weights, the DSpark checkpoint, optional Qwen checkpoints and all other third-party material retain their upstream terms. Deltafin is an independent project with no affiliation to Moonshot AI.