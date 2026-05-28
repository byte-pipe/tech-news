---
title: 'Vestige: A Gemma 4 Brain Tracker That Won''t Blow Smoke Up Your Ass - DEV Community'
url: https://dev.to/anchildress1/vestige-a-gemma-4-brain-tracker-that-wont-blow-smoke-up-your-ass-5caf
site_name: devto
content_file: devto-vestige-a-gemma-4-brain-tracker-that-wont-blow-smo
fetched_at: '2026-05-28T12:11:38.755977'
original_url: https://dev.to/anchildress1/vestige-a-gemma-4-brain-tracker-that-wont-blow-smoke-up-your-ass-5caf
author: Ashley Childress
date: '2026-05-24'
description: An ADHD brain tracker built on Gemma 4 (E4B + EmbeddingGemma 300M) that observes and never grades. Native audio, multi-lens extraction, on-device after one model download. Tagged with devchallenge, gemmachallenge, gemma, android.
tags: '#devchallenge, #gemmachallenge, #gemma, #android'
---

Gemma 4 Challenge: Build With Gemma 4 Submission

This is a submission for theGemma 4 Challenge: Build with Gemma 4

## TL;DR

* What:Vestige—an ADHD-friendly Android app designed to point out the things you don't know you're doing every day. 30-second voice entries in, sourced behavioral patterns out. No grading, no gamification, no feelings prompts.
* Gemma 4 doing real work:E4B handles native audio in (no SpeechRecognizer), transcription + persona-flavored follow-up in the foreground, then a 3-lens convergence extraction pass in the background. EmbeddingGemma 300M catches vocabulary drift over time: same state, different words.
* Privacy is enforced, not claimed:sealed-by-defaultNetworkGate+ averifyNoTelemetryGradle task with four independent scans (full list in§Code) that uploads privacy receipts as a CI artifact every run. After the model download, the app process has no remaining outbound code path.
* Proof artifacts:GitHub repo·APK + SHA-256

## What I Built

vestige(n.): a trace of something left behind.

Vestigeexists because I've been trying to work out the various reasons I do any particular thing, and I found it next to impossible to accurately keep track of everything in any form.

I don't want to journal. ChatGPT already handles the problem-solving end, and I don't need a second app for that. I don't want a tool that tells me how great I am, either; my eyes are incapable of rolling any more throughout the day than they already do at AI responses. What I wanted was the ADHD-friendly version that doesn't seem to exist anywhere: a voice notes app that points out the things that come up regularly in life that I'm not consciously aware of doing.

The fact that Gemma 4 runs locally means I can literally say anything out loud without wondering whether OpenAI should really know that thing I just said.Vestigeanalyzes patterns over time, not how I felt or what to do about them. That part is intentional because I assess plenty without AI's help telling me what to do about any of it. I can figure that part out on my own, thank you.

Besides, ADHD memory isn't always a storage problem—sometimes the recall just hasn't caught up.Vestigeis the receipt trail for that gap. Mine, specifically.

### Shapes that didn't make it 📼

The original v0 had a template grid on the capture screen. Pick "Crashed" or "Deep Space" or "Spiral" before you talk. That lasted about three days. The whole point of the app is that you don't know what shape the moment is in until after you've said the words, and making the user classify on the way in defeats the architecture. Now Gemma picks it for you.

Every cut feature failed the same test: did the app know more after the entry than before? Only one shape passed: capture first, observe after, never grade. This is not a journal, not a mood tracker, not a gratitude app, not a therapist disguised as a subscription, for the exact same reason.

### What I'm Not 🩻

I am not a mobile-first engineer. Android, Compose, and Material 3 were all new to me before this build, and I am not going to defend my history of avoiding UIs.

I made a mistake I caught too late to change: of the 6 ADRs I started with, I put UI as ADR-4. Then, not thinking about it, I translated those ADRs into stories, numbers included, and decided POC UI screens would suffice for the first bit—without ever actually writing those POC stories. That meant zero manual checks for the first half of the build—only tail logs and AI-configured tests.

A small miss in the ADR-to-stories translation, big cost in time and testing. Documenting it here because the don't-blow-smoke promise has to start at the build, not the marketing.

## Demo

Vestigeis a real Android app—sideloaded, fully offline after the model download, not a mockup wearing a trench coat.

Install:Android 14+ · 12 GB RAM · 6 GB free · Galaxy S24 Ultra reference ·APK + SHA-256

### What to watch for 🪧

Timestamp

Chapter

What it proves

0:00

Intro

Frame for the demo—what 
Vestige
 is and what it refuses to be

1:14

Airplane mode (privacy claim, on camera)

Every radio off before the capture loop runs—privacy demonstrated, not asserted

2:46

Capture voice

One tap to record; foreground call returns transcription + persona follow-up in a single streaming response

4:12

Gemma 3-lens results

Background extraction lands; Literal / Inferential / Skeptical produce different reads and the resolver picks a verdict

5:56

Android app tour

Pattern card with receipts—counts, dates, quoted snippets pulled from source entries; Material 3 UI

9:18

Review code highlights

ConvergenceResolver
— convergence as pure function

16:51

Export — markdown from the database

Entries leave as plain markdown; ObjectBox is the source of truth, export is portable user-owned text

## Code

Runtime is LiteRT-LM vialitertlm-android:0.11.0(pinned), with the model artifactlitert-community/gemma-4-E4B-it-litert-lmfrom Hugging Face. One inference runtime. No llama.cpp shim, no MediaPipe parallel path, no AICore alternative. A boring choice, which is how runtime choices should behave in public.

Audio adapter is forced to CPU (AudioBackendChoice.Cpu)—E4B rejects GPU there withModel requires one of [cpu]. Text decode still runs on GPU. The SDK made that one ugly, not me.

⚖️ This project is licensed underPolyform Shield 1.0.0with supplemental terms.

## anchildress1/vestige

### Brain tracker that won't blow smoke up your ass. Gemma 4, Android, fully local.

# Vestige

A brain tracker that won't blow smoke up your ass. Gemma 4, Android, fully local.

Built for theGemma 4 Challenge— submission category: Build with Gemma 4.Canonical product spec lives underdocs/; seeAGENTS.mdfor AI agent rules

## Table of Contents

* About
* Status
* Features
* Tech Stack
* Architecture
* Project Structure
* Getting Started
* Configuration
* Security & Privacy
* How to Contribute
* What's Next
* Known Limitations
* License
* Acknowledgements
* Author

## About

Vestige observes behavioral traces and surfaces patterns without therapy framing, mood scoring, or wellness vocabulary. It runs Gemma 4 E4B locally via LiteRT-LM — your voice never leaves the device, the audio bytes are discarded after inference, and entries can be exported as readable markdown at any time.

The positioning is deliberate: cognition tracker, not journal app. Patterns are sourced — every claim cites the entries it counted. Full product spec:docs/concept-locked.md.

## Status

The full loop is implemented and…

View on GitHub

### Stack 🧰

* Inference runtime:LiteRT-LMlitertlm-android:0.11.0(pinned)
* Models:Gemma 4 E4B (~3.66 GB, native audio + text) · EmbeddingGemma 300M (~200 MB, tone-word Vocab Drift clustering)
* Platform:Android 14+, Kotlin, Jetpack Compose, Material 3
* Persistence:ObjectBox (entries, patterns, embeddings); SharedPreferences for onboarding flags
* Build:Gradle KTS with a customverifyNoTelemetrytask (four scans, CI artifact every run)
* Pre-commit / pre-push:Lefthook running ktlint, detekt, secret-scan, actionlint, then full build + test
* CI:GitHub Actions running CodeQL, Sonar, Kover, commitlint, andverifyNoTelemetry
* Tests:JUnit 5 Jupiter on JVM (viauseJUnitPlatform()), JUnit 4 + Robolectric + AndroidX Compose UI on instrumented; MockK, Turbine, coroutines-test

### What's worth looking at 🪛

1. Privacy as construction, not policy.Two layers—build-time gate, runtime gate—either one failing catches a leak.

* NetworkGate.kt—sealedAtomicReference, opened only for the model download, resealed infinally. The app's only HTTP path.
* verifyNoTelemetryGradle task—four independent scans (classpath, manifest, APK, host list); any fails the build. Receipts upload as a CI artifact every run.

2. Convergence math as a pure function.ConvergenceResolver.kt—3-lens verdict in deterministic Kotlin, no model call. ≥2-of-3 →CONSENSUS; one lens only →CANDIDATE; disagreement →AMBIGUOUS; Skeptical conflict over agreement →CONSENSUS_WITH_CONFLICT.

3. Engineering paper trail.ADR-008—full wrong-probe / right-probe correction at the top as a callout, not a footnote. Deleted ADR-009 isn't archived as superseded; per AGENTS.md, genuine mistakes get removed outright. Thefull suite of ADRsis preserved in GitHub.

4. Test discipline.1,200+ JVM@Testmethods across 110+ files; 12 instrumented*SmokeTest.ktruns on the Galaxy S24 Ultra;docs/stt-results/is logcat from real on-device runs, not synthesized fixtures.lefthook.ymlgates ktlint / detekt / secret-scan / actionlint pre-commit and the full build + test pre-push; CI adds Sonar, Kover, CodeQL, commitlint, andverifyNoTelemetry.

### How the lenses differ 🪞

Three lens prompts define HOW to read; five surface specs define WHAT to extract. The composer joins them at runtime, the worker iterates, the resolver decides. The architecture lives in the text below.

Literal(lenses/literal.txt):

## Lens: Literal

Extract only what is explicitly stated in the entry text. No inference, no filling gaps.

Rules:

- Read each word and phrase at face value. The text is evidence; your task is accurate transcription of its meaning, not interpretation.
- Tags: extract short kebab-case tokens for every named activity, object, time anchor, person, state word, or pattern word in the text.
- Time anchors are behavioral tags, not metadata. Capture them.
- `stated_commitment`: only explicit statements of intent with a specific named object.
- Do not infer what was not said.

Enter fullscreen mode

Exit fullscreen mode

Inferential(lenses/inferential.txt):

## Lens: Inferential

Apply a charitable reading. Go beyond explicit words to what the text most plausibly means for this person's cognitive and behavioral state.

Rules:

- Read for pattern and meaning, not just surface vocabulary. What is this person experiencing?
- Decision loops: when the user describes returning to the same choice with new framing and no resolution, capture it as a tag.
- Avoidance sequences: when the user approaches a task and retreats, or states an intention then does something else, tag both the avoidance and the specific task.
- User-coined idioms carry their meaning: tag the user's own phrasing verbatim and let it stand for the state it names.

Inference limits:

- Do not infer causes or motivations.
- Do not infer emotional states the user did not name.
- Retrieved history can corroborate inferences but cannot supply content that isn't anchored in the current entry.

Enter fullscreen mode

Exit fullscreen mode

Skeptical(lenses/skeptical.txt):

## Lens: Skeptical

Apply an adversarial reading. Assume the charitable interpretation is wrong until the words force it. Challenge the obvious read — do not echo it.

Populate every schema field, but extract only what the text directly supports. Where the natural read takes an inferential leap, refuse it: take the more conservative value the literal evidence backs, even when that disagrees with the other lenses.

Adversarial layer — flag the leaps you refused to take:

- `commitment-without-anchor` — a modal commitment with no specific object or deadline.
- `unsupported-recurrence` — the user signals recurrence with no retrieved history to corroborate.
- `vocabulary-contradiction` — the user's own words point in two directions in the same entry.
- `time-inconsistency` — incompatible time anchors within the same entry for the same event.

`flag` output format — one `flag:` line per flag: `flag: <kind> | <snippet> | <note>`.

Enter fullscreen mode

Exit fullscreen mode

Surface specs define what each schema field captures — example,State(surfaces/state.txt):

## Surface: State

Captures the user's cognitive and energy state.

- The state word the user uses for their physical or cognitive condition (drained, crashed, foggy, flat, wired). Use the user's exact word, not clinical paraphrase. It must describe the person, not the event — discard manner qualifiers and effects.
- A before/after transition between two distinct states.

What goes in the schema:

- Append the state word to `tags` as a short lowercase kebab-case token. Single root word only — never a clause. Omit when the entry names no such condition.

Enter fullscreen mode

Exit fullscreen mode

Backed byConvergenceResolverTest.kt(every convergence verdict including the survivors-of-failed-lens fallback) and theSTT-D divergence run(73% meaningful divergence on-device against a ≥50% bar).

## How I Used Gemma 4

Gemma 4 E4B does the heavy lifting. EmbeddingGemma 300M is the tone-word clustering helper that earns its 200 MB when the user's vocabulary drifts. They do not share a job, because that is how you avoid building soup with a logo on it.

### Why E4B 🧭

E4B is the path I validated end-to-end: native audio in, local structured extraction, and enough quality for the 3-lens resolver to be worth the wait. The 31B Dense and 26B MoE are the wrong hardware story for a phone; the real choice was E2B vs E4B.

Requirement

E2B

E4B

Native audio in (no SpeechRecognizer)

✅

✅

Foreground answer fast enough that the app still feels usable

✅ (lighter, faster)

✅

Structured background extraction quality floor under 3-lens load

E4B was the validated path; E2B traded down quality/headroom for size/speed

Holds, but the prompt stack was already trimmed once to land it

E2B is lighter and probably wins on raw foreground latency. The reason it did not get its own bake-off is that the E4B run was already tight: the 3-lens prompt stack only landed after I scaled the guidance back once, and the product still needed native audio, structured extraction, and enough reasoning headroom for the resolver to matter. A smaller model would have meant another prompt cut against a quality floor that was already the hard part. Cold-start cost is uglier than I'd like, but I chose the path that survived the on-device receipts.

A cloud-class model would have made the latency story nicer and taken the user's voice entry somewhere the entire product says it will not go. E4B keeps the sensitive part on the phone, with no outbound path from the app process during normal use.

### Native audio, no SpeechRecognizer 🛰️

The foreground call is the only one the user waits on directly. Audio goes in viaLiteRtLmEngine.streamMessageContents; transcription and the persona follow-up come back together as a single streaming{transcription, follow_up}response—so the user waits once instead of through two consecutive spinners while the model gets philosophical in a broom closet. I tried splitting it in two on-device; didn't help. Back together it stays.

Behind the foreground sits the rest of the inference work: 3 background lens calls per entry (Literal / Inferential / Skeptical, sequential per ADR-008's single-session ceiling), 1 background pattern analysis pass every 3 completed entries, and a best-effort Gemma wording call when a temporal-relative pattern lands. All background, all queued, all invisible to the user.

The follow-up is single-turn by design in v1. Cross-entry intelligence lives in pattern detection, deterministic prior-entry candidates, tone-word clustering, and stored evidence—exactly where it can be audited instead of hand-waved.

### Three lenses, one resolver 🪞

Once the entry is saved, the background pass runs three independent Gemma reads over the same transcript:

1. Literal
2. Inferential
3. Skeptical

Each pass extracts across five surfaces:

1. Behavior
2. State
3. Vocabulary
4. Commitment
5. Recurrence

Recurrence is the one surface the model doesn't decide alone—the app builds a deterministic candidate from prior entries first, then asks the model to judge whether the current entry actually repeats the candidate or just happens to land at the same clock time. The model never emits a pattern ID; the app owns that mapping. The Skeptical lens still addsunsupported-recurrenceflags when the user signals "again" with no corroborating history.

The resolver (see§Code) compares the three reads before anything is committed, and surfaces conflict as conflict instead of guessing with better typography.

Step

Purpose

Example

User entry

Input

"Crashed at noon. Fine before — wired even. Then gone."

Literal

Surface words only.

Tags: 
crashed
, 
noon
, 
wired
Vocabulary: 
crashed

Inferential

Adds the pattern read.

Tags: 
crashed
, 
noon
, 
wired
, 
post-noon-crash
, 
energy-flip
Vocabulary: 
depleted
.

Skeptical

Flags inconsistencies.

Tags: 
crashed
, 
noon
, 
wired
Vocabulary: 
crashed
Flag: 
vocabulary-contradiction

Resolver

Reconcile differences.

Vocabulary lands 
CONSENSUS_WITH_CONFLICT
 on 
crashed
.
Literal and Skeptical agree, but Skeptical's 
vocabulary-contradiction
 flag elevates the verdict above plain 
CONSENSUS
.

The multi-lens approach only earns its keep if the lenses actually produce different reads. Three identical responses would have been useless and three times the wait.

So I built a test for that. The bar: at least 50% of test entries showing meaningful field-level divergence between the three reads. TheSTT-D divergence runhit 73% with 97.8% parse stability and zero timeouts; with greedy decoding plus a fixed seed the outputs were byte-identical across runs—so 73% is signal, not sampling noise.

After the flatkey: valuelens contract + model-emittedtemplate_labellanded, the rebuilt path was re-captured inSTT-H 2026-05-24: 12/12 entries succeed, 3/3 lenses parse on first attempt, zero retries, AUDIT dropped 8/12 → 4/12, and six distinct archetypes are in play (up from near-total audit). Lens disagreement is real—wired-third-nightresolves AUDIT on lens votes tunnel-exit/audit/audit;tuesday-stalledresolves AFTERMATH on aftermath/aftermath/audit—which is exactly the disagreement the convergence math was built to resolve. Mean latency landed ~38s per entry (thermal on a back-to-back GPU session; the same path ran 21.2s cold on 2026-05-23).

### I was wrong about being wrong 🪨

ADR-008started as a parallel 3-lens dispatch design. The paper version looked clean: one engine, multiple session contexts, same convergence math, cheaper wall-clock. The first probe said no. The second probe said maybe. The on-device run said absolutely not, and it gave me a table because apparently humiliation has formatting preferences.

Lens

Attempts

Wall clock

Outcome

SKEPTICAL

1

14.7s

parsed ✅

LITERAL

2

95ms

FAILED_PRECONDITION
 ❌

INFERENTIAL

2

92ms

FAILED_PRECONDITION
 ❌

One session won the race; the other two never got a turn. The scary part was not the SDK limitation. The scary part was that the resolver fallback could have made the app look successful while silently running one lens instead of three.

v1 ships sequential—the one path LiteRT-LM actually executes on-device. The convergence verdicts stay the same. v1 trades wall-clock, not correctness.

### The wrapper had to go 🪤

Smoke tests gauged cold-start at 3–5s; actual on-device runs landed near 20s, and a background extraction thread kicked off the moment recording stopped—so a second recording attempt sat there ~30s before the user saw anything.

Fix: drop the long-livedConversationwrapper and callLiteRtLmEngine.streamMessageContentsdirectly per inference. Each call gets a fresh ephemeral conversation that front-loads the KV for the 3×5 lens prompt and—the actual UX win—lets a foreground capture cancel any running background inference instead of queueing behind it. Doesn't speed the model up, but the user stops waiting on processes they didn't know existed.

### EmbeddingGemma catches vocabulary drift 🪡

EmbeddingGemma 300M powers one surface in v1: theVocab Driftpattern card. Each entry's tone word—the single felt-quality word the vocabulary lens emits (vocabularyWord)—gets embedded, andEmbeddingClusteringgroups entries by cosine similarity. Threshold is 0.30, unchanged across calibration: the root cause was the axis, not the threshold. When the same state shows up under different words—"drained" one week, "wiped" the next, "running on empty" the week after—the cluster forms on the feeling, not on the topic. That is the +200 MB justification.

Cost: ~200 MB resident and ~880ms per embed on CPU.

Verified on-device (S24 Ultra, EXTRACT=1 re-seed): 18 toned entries clustered to sizes[6, 4, 2, …]; theDrained Vocab Frequencypattern minted and surfaces on the scoreboard. A toneless entry (novocabularyWord) is excluded entirely so factual logs don't get assigned a fabricated feeling.

The clustering only shows up when entries have actually been vectored: clustering needs at least six usable vectors before it runs, and a Vocab Drift pattern needs a cluster of at least four members (VOCAB_THRESHOLD). Seed the debug build without extraction running and there's nothing to display.

## What's next 🎟️

v1 ships narrow on purpose. Two deferrals carry the headline weight.

Tighten the archetype language— movingtemplate_labeloff the deterministicTemplateLabelerto a model-emitted, majority-resolved pick landed in v1. The latest STT-H run parsed 12/12 entries with zero retries, droppedAUDITfrom 8/12 to 4/12, and surfaced six distinct archetypes. The next pass is prompt polish for borderline entries, not fixing a broken picker.

Agentic tool-calling— letting E4B call into the pattern-detection layer as functions (resolver-as-tool-call instead of deterministic Kotlin). External benchmarks land local function-calling around 75% reliability; the shipped path parses 12/12 lens calls on first attempt with deterministic Kotlin doing the convergence math. Not a swap until the tool-calling floor rises.

## What helped 🪙

Planning ran through Claude Cowork and Codex Chat—messy thinking before any of it became a story.

In the codebase: Claude Code as primary, Codex as the secondary and reviewer, GitHub Copilot keeping things tidy on the way to merge. CI in GitHub Actions ran CodeQL and theverifyNoTelemetryprivacy gate on every PR. Sonar ran the whole way (always free).

For the Android knowledge I didn't have, I sourced existing skills where they existed and wrote new ones where they didn't. The Lefthook pre-push gate enforced 1,200+ tests on every push—slowed things down, caught a ton of errors before they made it into the codebase. A trade I'd make again.

ADRs kept up with my thinking over time. Stories kept the build on schedule—mostly...

--

## Closing 🎬

I still don't know why I do half the things I do. WithVestigeI just don't get to pretend I haven't done them.

Your brain drops things.Vestigedoes not.

## Ashley ChildressFollow

Distributed backend specialist. Perfectly happy playing second fiddle—it means I get to chase fun ideas, dodge meetings, and break things no one told me to touch, all without anyone questioning it. 😇

### 🛡️ Consensus_With_Conflict

Claude drafted this footer after I told it "enterprise voice is the one thingVestigerefuses to use." Every ADR was human-signed before merge—convergence didn't apply to the writing, and one verdict was enough when it was mine.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse