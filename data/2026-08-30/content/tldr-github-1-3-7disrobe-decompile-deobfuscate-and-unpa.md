---
title: 'GitHub - 1-3-7/disrobe: Decompile, deobfuscate, and unpack almost anything: a universal, deterministic, single-binary reverse-engineering toolkit in Rust for Python, JVM/Android, .NET, WebAssembly, JS, Go, and native packers (UPX/PyArmor/PyInstaller/Nuitka) and 20+ more. Built for malware analysis, CTFs, and security research. · GitHub'
url: https://github.com/1-3-7/disrobe
site_name: tldr
content_file: tldr-github-1-3-7disrobe-decompile-deobfuscate-and-unpa
fetched_at: '2026-08-30T15:12:07.500329'
original_url: https://github.com/1-3-7/disrobe
date: '2026-08-30'
description: 'Decompile, deobfuscate, and unpack almost anything: a universal, deterministic, single-binary reverse-engineering toolkit in Rust for Python, JVM/Android, .NET, WebAssembly, JS, Go, and native packers (UPX/PyArmor/PyInstaller/Nuitka) and 20+ more. Built for malware analysis, CTFs, and security research. - 1-3-7/disrobe'
tags:
- tldr
---

1-3-7

 

/

disrobe

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork5
* Star95

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

2,337 Commits
2,337 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.cargo
.cargo
 
 
.config
.config
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
benches
benches
 
 
bindings
bindings
 
 
corpus
corpus
 
 
crates
crates
 
 
docs
docs
 
 
editors
editors
 
 
evidence
evidence
 
 
fuzz
fuzz
 
 
hooks
hooks
 
 
playground
playground
 
 
plugins
plugins
 
 
schemas
schemas
 
 
scripts
scripts
 
 
xtask
xtask
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.pre-commit-hooks.yaml
.pre-commit-hooks.yaml
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LEGAL.md
LEGAL.md
 
 
LICENSE
LICENSE
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
action.yml
action.yml
 
 
book.toml
book.toml
 
 
clippy.toml
clippy.toml
 
 
committed.toml
committed.toml
 
 
deny.toml
deny.toml
 
 
justfile
justfile
 
 
lefthook.yml
lefthook.yml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
typos.toml
typos.toml
 
 
View all files

## Repository files navigation

disrobe is a Rust command-line suite that decompiles, deobfuscates, and unpacks compiled software. Its catalog spans 15 ecosystems: Python, JavaScript and TypeScript, WebAssembly, JVM and Android, .NET, native binaries, Go, Lua, PHP, Ruby, BEAM, Swift and Objective-C, ActionScript 3, mobile runtimes, and shell languages. Default recovery paths do not execute the sample or call a model. A committed determinism gate hashes three real fixture recoveries across Linux, macOS, Windows, and the batch runner at one and four workers.

Everystrongpublished number comes from a committed test graded against an independent reference: recovered Python must recompile to equivalent bytecode, recovered Android classes must pass the real JVM verifier, unpacked sections must byte-compare to the original.coverage-self-reportedrows visibly state when they count disrobe's own output and pin the population they inspect. Where the data is absent from the artifact, disrobe reports the limit instead of guessing past it. Numbers, evidence classes, and reproduce commands live inevidence/.

## Install

Prebuilt binaries for Windows, Linux (glibc and musl), and macOS, each for x86-64 and ARM64, are on theReleases pagewithSHA256SUMSand a cosign bundle per archive. Building from source needs Rust 1.95+ stable and nothing else. The in-house paths launch no external programs; backend-capable commands can invoke installed tools when selected explicitly or through--backend auto.

cargo install --git https://github.com/1-3-7/disrobe disrobe-cli

#
 or, from a clone

cargo build --release 
#
 about 4-6 minutes

./target/release/disrobe doctor 
#
 optional: probe 46 to 51 external tools depending on the platform

Optional external backends (Ghidra, CFR, jadx, ILSpy, de4dot) are not required. For.classand.jarinputs,jvm decompile --backend autouses the first available JVM backend; DEX and APK inputs stay on the in-house path unless an Android backend is selected.dotnet decompilealso defaults to--backend auto, selecting the first available backend in this order: ILSpy, dnSpyEx, dnSpy, then de4dot; its native CIL decompiler runs regardless, including when no external backend is available. Ghidra-backed decompilation runs only throughnative decompile --backend ghidra;disrobe doctormay separately launch Ghidra with-helpwhile probing installed tools. The slim build, the per-OS notes, and the split between build-time dependencies and the separate toolchains the graded numbers need are in theinstallation guideandevidence/README.md.

## Quickstart

disrobe auto suspect.exe --out recovered/ 
#
 fingerprint, then chain the whole pipeline

disrobe identify suspect.exe 
#
 format, packer, and compiler ID

disrobe py decompile module.pyc --out src/ 
#
 recover Python source from bytecode

disrobe native unpack packed.exe --out unpacked.bin 
#
 stub-emulator unpack, byte-recovery graded

disrobe webview desktop.exe --out frontend/ 
#
 recover Electron, Tauri, or Wails assets

For recognized inputs with a viable chain,disrobe autofingerprints the input and composes the whole pipeline in one call:PE -> UPX -> demangle,APK -> dex -> Java,PyInstaller -> PyArmor -> .pyc decompile. With--capture-stageseach stage lands inout/01-*/,out/02-*/, ...,out/final/. If it recovers no files, it reports that limit and directs you todisrobe detectand the relevant dedicated command.

Try it in your browser at1-3-7.github.io/disrobe/playground: the passes compile to WebAssembly and run client-side, and nothing is uploaded.

## Coverage

Ecosystem

Tier

Headline measured figure

Oracle

Guide

Python bytecode

Recover

96.53% per code object, 123 of 200 modules whole

strong 
[CI]

python

PyArmor

Recover

72 / 72 manifest-named v8/v9 default-trial wrappers decode one complete header-anchored root 
CodeObject

coverage-self-reported 
[CI]

python

Python pickle

Recover

470 / 470 reconstructed fixtures re-execute equal

strong 
[CI]

pickle

JVM classfile

Recover

131 of 131 methods recompile

recompile-only 
[CI]

jvm

Android DEX

Recover

118 / 118 verifier-presented classes

strong 
[CI]

android

.NET CIL

Recover

Eazfuscator VM and KoiVM lifted

strong 
[CI]

dotnet

JavaScript, TypeScript

Recover

obfuscator.io, JS-Confuser, Jscrambler

pass-gated

js

WebAssembly

Recover

57 / 57 eligible functions execute equal

strong 
[CI]

wasm

Native symbols, structure, disasm, IR

Recover

PE / ELF / Mach-O symbols; Windows and OS/2 NE segments, entries, imports, and resources

pass-gated

native

Native decompile

Recover

x86-64 C and Rust output re-executes equal; AArch64 pseudo-C scalar floating-point output is raw-bit graded, with NaN payloads canonicalized only when both results are NaNs

pass-gated

decompile

Native packers

Recover

UPX 
.text
 and 
.pdata
 byte-identical

strong 
[CI]

unpack

Native VM protectors

Detect-only

CLI and auto detect only; the Rust 
recover_detected
 helper carves VMProtect and Themida protected sections

pass-gated

unpack

Go

Recover

838 of 838 stripped type names

strong 
[CI]

go

Swift, Objective-C

Recover

committed symbols produce pinned renderings

coverage-self-reported 
[CI]

swift

Lua

Recover

IronBrew2 devirt runs equal

strong 
[CI]

lua

Ruby

Recover

greeter 100% under MRI recompile

strong 
[CI]

ruby

PHP

Partial

eval-chain peel, static-key decode loops, Phar decode

pass-gated

php

BEAM

Recover

18 / 19 stripped Core Erlang cases match 
test/0

strong 
[CI]

beam

AS3, Flash

Recover

ABC method-body source

pass-gated

as3

Hermes, React Native

Recover

8 of 8 functions, no fallback ops

strong 
[CI]

mobile

Flutter Dart AOT

Partial

class and method attribution over a self-authored Dart 3.12.2 corpus, plus a real RustDesk build graded locally

pass-gated

mobile

Haxe HashLink

Recover

class names 100%, methods floor 75%

strong 
[CI]

scriptlang

Shell, VBA, XLM

Recover

PowerShell, bash, batch, VBA, Excel 4.0

pass-gated

shell

Perl, R, Tcl

Partial

op-tree, 
.rds
 round-trip, starkit

pass-gated

scriptlang

Nim, Zig, Crystal, D

Partial

demangle plus DWARF aggregates

pass-gated

native

Containers, firmware

Recover

Of 103 detected formats, 42 generic routes write member bytes from a committed input, one committed DMG input reaches detection only, and 59 have no committed input; LUKS1 is metadata-only through the generic route and graded separately through raw-volume-key routing

measured 
[CI]

containers

Recon, secrets, format ID

Recover

6 / 6 planted IOC categories

strong 
[CI]

frisk

A row's tier is the strongest level any family in that ecosystem reaches, not a promise for every family in it.Recovermeans real recovered output, source or bytes or structure, on the run path.Partialmeans a structural peel or constants only, with the residual stated.Detect-onlymeans identification plus a stated reason the rest is not statically present, which is a legitimate triage result rather than a failure. Per-family tiers are in the linked guide and indisrobe catalog [ecosystem], which prints the roster the binary itself carries. Breadth and depth are separate axes:disrobe identifyanddisrobe catalogspan the full ecosystem list, while recovery depth per family runs from full source recovery down to detect-only.

Roster sizes the binary carries: Python source obfuscators (20), JS bundlers (11), JVM and Android obfuscators (10), .NET protectors (23), Packers (29 families), Lua (16 catalog entries), shell obfuscators (19), Android RASP (8 vendors).

Theanti-analysis guidedocuments each defeat capability with the gate behind it: opaque-predicate folding, control-flow deflattening, verified MBA simplification, stack-string emulation, calling-convention and type recovery, indirect-dispatch resolution, and generic VM devirtualization. Thechain runner guidecovers recursive payload peeling, the encoding and cipher set it reverses, and the structural check that stops a decode from advancing on garbage.

## How the numbers are checked

Two independent labels qualify every figure below. The first is oracle strength, which says what could have rejected a wrong answer.

* strong: the result passes an external-equivalence, execution, or byte-identity check against an independent reference. This README reserves the word "proves" for this tier.
* recompile-only: the recovered source compiles under the real toolchain; no gate asserts byte-equivalence.
* coverage-self-reported: the tool counts its own coverage; no external check grades the count. The tier is lower-confidence and never blends into astrongfigure.
* pass-gated: an in-tree gate exercises the pass on real input, but no single headline figure is published for it. The linked guide names the gate and its strength.

The second is reproducibility.[CI]means a committed test gate reproduces the number on every run.[local]means the input is kept out of the tree by license or size; the stated command still reproduces the number, just not inside CI. The two axes are orthogonal, so astrongfigure can be[local]and a[CI]figure can be self-reported.

Each[CI]number links to a committed corpus or fixture, a runnable reproduce command, and a public CI log. Descriptors and rendered results live underevidence/;.github/workflows/ci.ymland.github/workflows/evidence.ymlrun the gates that produce them. The evidence harness renders its report from committed descriptors,xtask/data/recovery.json, and measured JSON.

## Benchmarks

### Strong

Read the first three Python rows together. A module counts as recovered only when every one of its code objects recompiles to equivalent bytecode. A module typically holds dozens of code objects, so a small per-object miss rate compounds into a large per-module one. To know whether a whole readable module comes back, use the whole-module figure of 123 of 200 modules (61.5%), not the measured per-object 96.53%. That gap is the center of the evaluation rather than a footnote, and thewhitepaperworks through it.

The Oracle column names the independent reference in a few words. What that reference is and how it can reject a wrong answer is in the cited test and in the linked guide.

Metric

Measured

Oracle

Reproduce

Python 
.pyc
, full 3.14 stdlib

95.09% per code object 
[local]

recompile-equivalence, over a population CI does not run

crates/disrobe-pass-py-decompile/tests/harness/py_arbitrary_measure.py

Python 
.pyc
, pinned 200-module corpus

96.53% per object, floor 96.51% 
[CI]

recompile-equivalence

crates/disrobe-pass-py-decompile/tests/arbitrary_recompile_gate.rs

Python 
.pyc
, whole-module exact

123 of 200 modules recompile whole, floor 123 
[CI]

recompile-equivalence

crates/disrobe-pass-py-decompile/tests/arbitrary_recompile_gate.rs

Python legacy 1.0-3.7

150 of 191 gate-verified 
[CI]

recompile or token match

crates/disrobe-pass-py-decompile/tests/legacy_recompile.rs

Pickle safety

102 / 102 fixtures classify 
[CI]

pickletools semantics

crates/disrobe-pass-pickle/tests/corpus.rs

Pickle reconstruction roundtrip

470 / 470 re-execute equal, floor 100% 
[CI]

CPython re-execution

crates/disrobe-pass-pickle/tests/roundtrip.rs

Android DEX, committed corpus

118 / 118 verifier-presented classes clean, 317 re-hosted bodies clean 
[CI]

real JVM verifier

crates/disrobe-pass-jvm/tests/dalvik_verifier_gate.rs

.NET Eazfuscator VM

67 / 67 instructions lifted, ordered-CIL match 
[CI]

independent clean DLL

crates/disrobe-pass-dotnet/tests/real_eazvm.rs

.NET KoiVM

6 / 6 bodies lifted, structural recovery >= 75% 
[CI]

independent clean build

crates/disrobe-pass-dotnet/tests/real_koivm.rs

.NET protectors

23 classified, ConfuserEx2 decrypted 
[CI]

plaintext-absent check

crates/disrobe-pass-dotnet/tests/confuserex2_full.rs

WebAssembly, execution-equiv

57 / 57 eligible functions equal, 6 byte-identical 
[CI]

wasmtime differential

crates/disrobe-pass-wasm-deob/tests/semantic_differential.rs

BEAM, stripped Core Erlang

18 / 19 committed cases recompile, preserve exports, and match 
test/0
 
[CI]

real 
erlc
 and 
erl
, OTP 27.3.4

crates/disrobe-pass-beam/tests/erlc_recompile_equivalence.rs

WebAssembly obfuscator helpers

4 cataloged direct-helper families; 3 transformations run through 
wasm deob
, while Tigress-via-Emscripten is detected only 
[CI]

parser and execution gates

crates/disrobe-pass-wasm-deob/tests/obfuscators_e2e.rs

Lua IronBrew2 2.7.0 devirt

runs equal, standard and MAX mode 
[CI]

real-
lua
 differential

crates/disrobe-pass-lua/tests/ironbrew2_real_oracle.rs

Ruby YARV, greeter

100% 
[CI]

MRI recompile, opcode multiset

crates/disrobe-pass-ruby/tests/yarv_recompile_oracle.rs

Ruby YARV, megafile

98.67% of 23966 opcodes 
[CI]

MRI recompile, opcode multiset

crates/disrobe-pass-ruby/tests/yarv_recompile_oracle.rs

Go type-name recovery

838 of 838 type names, stripped 
[CI]

typelinks survive 
-s -w

crates/disrobe-pass-go/tests/go_typemeta.rs

Go BuildInfo and garble undo

BuildInfo recovered, 
-literals
 rebuilt 
[CI]

real toolchain output

crates/disrobe-pass-go/tests/go_buildinfo_oracle.rs

HashLink (Haxe 
.hl
)

class names 100%, method names floor 75% 
[CI]

names vs the original 
.hx

crates/disrobe-pass-scriptlang/tests/real_hashlink_decompile.rs

Native UPX

.text
 and 
.pdata
 byte-identical, floor 96.0% 
[CI]

byte-identity

crates/disrobe-pass-native/tests/upx_unpack_all.rs
, 
nrv2b_content_section_byte_recovery_meets_floor

Native packers, MPRESS

.text
 >= 90%, 
.rdata
 >= 85% 
[CI]

RVA-aligned recovery

crates/disrobe-pass-native/tests/mpress_gauntlet.rs

Native packers, Yoda's Crypter

.rsrc
, 
.text
, 
.data
 byte-identical 
[CI]

byte-identity

crates/disrobe-pass-native/tests/packer_real_samples.rs

Native packers, ASPack and PECompact

content and rebuilt IAT >= 98% byte-identical 
[CI]

RVA-aligned recovery

crates/disrobe-pass-native/tests/aspack_pecompact_phase2.rs

Native packers, MEW

structural loaded-image recovery 
[CI]

RVA-aligned recovery

crates/disrobe-pass-native/tests/mew_unpack.rs

Native packers, committed pairs

nspack 57721 / 60060, fsg 55263 / 60060, petite 86986 / 89648 
[CI]

content-section bytes

crates/disrobe-pass-native/tests/committed_packer_byte_recovery.rs

Native packers, larger local samples

no figure published, 
corpus/native/packers/petite/megafile_DirCmp.exe
 uncommitted 
[local]

whole-image comparison

crates/disrobe-pass-native/tests/petite_unpack.rs

Native packers, kkrunchy

kkrunchy and kkrunchy classic payloads 
[CI]

payload byte-identity

crates/disrobe-pass-native/tests/kkrunchy_unpack.rs

Native stub-emulator unpack

dispatch and decode round-trip 
[CI]

stub-emu equivalence

crates/disrobe-pass-native/tests/stub_pack_oracle_roundtrip.rs

Hermes HBC v96

8 of 8 functions, 0 fallback 
[CI]

op-coverage, source bodies

crates/disrobe-pass-mobile/tests/real_hermes_sample.rs

Hermes production bundle

122,633-function parse 
[local]

parse scale, gitignored input

crates/disrobe-pass-mobile/tests/real_hermes_discord.rs

APK secrets vs apkleaks

8 / 8 planted secrets vs 5 / 8 
[CI]

planted ground truth

cargo run -p disrobe-bench-head-to-head

frisk IOC detection

6 / 6 planted IOC categories 
[CI]

planted ground truth

crates/disrobe-core/tests/frisk_gauntlet.rs

Container / archive / firmware extraction

42 of 103 detected formats reached through the generic entry point by a committed input 
[CI]
; LUKS1 has a separate tracked decryption fixture

extraction over the committed corpus

crates/disrobe-cli/tests/container_breadth.rs
, 
crates/disrobe-binfmt/tests/real_luks1.rs

Cross-platform determinism

3 / 3 real fixtures byte-identical, 3-OS matrix 
[CI]

BLAKE3 hash equality

crates/disrobe-cli/tests/determinism_cross_platform.rs

Native taint, Juliet CWE-78

93 / 190 flows recalled (48.9%), 0 false positives, gcc 16.1.0 -O2 
[local]

NIST SARD Juliet Test Suite's own manifest; CI does not provision the corpus

crates/disrobe-taint/tests/graded_corpus.rs

Each bar states how it was checked, in colour and again in the tag beside it. A lighter bar means a
stronger reference could have rejected the number. A filled mark means a committed gate reproduces
the figure on every run, and a hollow mark means the input stays outside the tree and the stated
command reproduces it locally. Each tier comes from the evidence descriptor that owns the figure, so
a bar cannot be drawn stronger than the reference behind it.

The Python figures count code objects, not modules. The full-stdlib row covers 17378 of 18276 objects across 574 modules; the pinned row covers 6068 of 6286 objects across 200 modules, and the same legacy gate reaches 166 of 191 locally. The Go row is measured on a stripped go1.26.3 fixture, its gate pins the count and holds the ratio above a 85% floor, andgo_garble_undo.rscovers the garble leg beside it.

The Android committed-corpus row is measured on small methods; 37 of 155 classes are link-skipped and ungraded, and the real-apk row further down carries the production scale. The WebAssembly execution row covers the functions that can be run at all, which is a smaller population than the 133-function corpus: a function needs a callable signature and no host imports before wasmtime can run it. The .NET Eazfuscator row has a second[CI]leg in which the recovered CIL re-injects to byte-identical stdout; CI provisions the required .NET runtime.

The BEAM figure is scoped to the committedtest/0observation in each case. The test compiles the original Erlang source with OTP 27.3.4, strips bothDbgiandDocs, recovers through the Core Erlang path, recompiles the recovered source, compares exports, and then comparestest/0exit status and stdout under realerl. It does not claim equivalence for every input to every export. CI enforces this gate on Linux; macOS and Windows report it as unmeasured when Erlang is absent.

The Swift row is pinned against a committed fixture's own symbol table and expected in-process renderings. The parity leg against the referenceswift-demangleruns only where that tool is installed; CI neither requires nor provisions it, so it is not a guaranteed CI-graded public comparison. HashLink also parses the whole HLB image byte-exact, 336 functions and 421 types on the committed fixture. The PyArmor row is limited to 72 manifest-named v8/v9 default-trial wrapper/runtime pairs. Its test statically decrypts each body and requires its header-anchored marshal stream to decode as one complete rootCodeObject; it does not compare source, emitted.pycbytes, semantic or execution behavior, or external-tool output. The container measurement follows the exercised-format roster pinned incrates/disrobe-cli/tests/golden/container_breadth.txt. Its 42 generic routes have committed inputs that reach member bytes, the committed DMG input reaches detection only, and 59 generic routes have no committed input. LUKS1 is graded separately through raw-volume-key routing. The six planted IOC categories graded by frisk are endpoints, manifest findings, URLs, IPv4, email, and.onion.

Native UPX recovers about 96% of the whole image beyond the two byte-identical sections. For the committed packer pairs,.textand.dataare byte-identical for all three families, and nspack's.rdatais byte-identical too. One packed-and-original pair per family is committed, so each figure reproduces from a clean checkout. The same decoders score lower on the whole-image measure over larger uncommitted vendor samples, with the content sections holding up far better than the whole image.fsg_unpack.rsandnspack_byte_recovery.rssit beside the cited petite test, but no figure is published for them because nothing there reproduces or is pinned. Determinism is also checked across worker-pool sizes: the same fixtures run throughdisrobe auto <dir>'s batch runner at--jobs 1and--jobs 4produce identical bytes, and that batch runner is the one real concurrent code path in the CLI.

### Recompile-only

Metric

Measured

Oracle

Reproduce

JVM classfile 
recompile-only

131 of 131 methods recompile error-free, floor 131 
[CI]

real 
javac
, JDK 25

crates/disrobe-pass-jvm/tests/decompile_recompile_rate.rs

Nothing asserts bytecode-equivalence for that row. The recovered source compiles, which is a weaker statement than the Strong tier makes.

### Self-reported coverage

Metric

Measured

Oracle

Reproduce

Android DEX, real APKs 
coverage-self-reported

99.6% of methods that declare a code item 
[local]

self-reported, gitignored apks

crates/disrobe-pass-jvm/tests/dex2jar_realworld_apks.rs

Android DEX, real APKs, count 
coverage-self-reported

83609 / 83943 
[local]

self-reported, gitignored apks

crates/disrobe-pass-jvm/tests/dalvik_realworld_body_attest.rs

WebAssembly, op-coverage 
coverage-self-reported

1034 of 1034 opcodes across 38 parseable modules 
[CI]

wasm-tools 1.250.0 supplies the denominator; lowering is self-counted

crates/disrobe-pass-wasm-deob/tests/external_op_denominator.rs

Swift symbol rendering 
coverage-self-reported

committed symbols produce pinned renderings 
[CI]

binary 
LC_SYMTAB
 membership with pinned in-process output

crates/disrobe-pass-swift-objc/tests/swift_hello_symbol_pin.rs

PyArmor v8/v9 default-trial wrappers 
coverage-self-reported

72 / 72 manifest-named wrappers decode one complete header-anchored root 
CodeObject
 
[CI]

self-reported structural check

crates/disrobe-pass-pyarmor/tests/static_unpack_corpus.rs

That figure is the total across all three apks and not any one of them. The per-apk split, and a separate verifier-attested population with its own smaller denominator, are in theAndroid guide.

The recovered bodies that can be presented to the verifier are attested at 2985 of 2998, graded by realjava -Xverify:allover bodies rather than methods, which is a different and smaller population than the method-coverage figure above.

The WebAssembly denominator is external and frozen:wasm-tools 1.250.0disassembles each committed.watand its per-function instruction inventory is checked in, keyed by the fixture's BLAKE3, so a decoder that stops seeing opcodes scores lower rather than shrinking the population it is divided by. The two decoders agree instruction for instruction, 1034 accounted against 1034 counted. The row stays self-reported because the numerator is still disrobe counting the opcodes it lowered, and a lowering rule firing is not the same as the lowering being right. The 2 corpus files outside the 38 are the oneswasm-toolsrejects too, pinned with its own error text.

Reproduce every number

Every figure above traces to the cited test gate or runner and eitherxtask/data/recovery.jsonor a measured JSON file underevidence/results/measured/. To regenerate the public report and re-check those sources:

./evidence/run.sh 
#
 render evidence/results/EVIDENCE.md + index.json

cargo run -p xtask -- evidence --check 
#
 drift gate: rendered numbers must match their sources and floors must hold

cargo run -p xtask -- evidence --list 
#
 every descriptor: ecosystem, strength, [CI]/[local], measured, floor

To re-run an individual gate, use theReproducecommand in its row, for example:

cargo 
test
 -p disrobe-pass-py-decompile --test arbitrary_recompile_gate 
#
 Python .pyc recompile-equivalence

cargo 
test
 -p disrobe-pass-jvm --test dalvik_verifier_gate 
#
 Android -Xverify:all

cargo 
test
 -p disrobe-pass-wasm-deob --test semantic_differential --features sandbox 
#
 WASM wasmtime differential

DISROBE_REQUIRE_ERLANG=1 cargo 
test
 -p disrobe-pass-beam --test erlc_recompile_equivalence -- --nocapture 
#
 BEAM OTP differential

cargo run -p disrobe-bench-native-unpack 
#
 native packer byte-recovery table

evidence/README.mddocuments the build/runtime dependency boundary and the offline-vs-network reproducibility tiers.

## Head-to-head

The head-to-head runner compares the same committed input with pinned tool versions and records the reference each row uses. A missing same-input runner is not treated as a win. The runner isbenches/head-to-head/; pinned tools live inevidence/competitors/.

Surface

disrobe

Leading tool

Result

Reproduce

JVM classfile

181 / 181 methods recompile

CFR 0.152: 152 / 166 methods recompile

disrobe
 leads on clean methods and clean rate

cargo run --locked -p disrobe-bench-head-to-head -- --check --only apk-jadx-cfr

Android DEX

60 / 163 methods recompile

JADX 1.5.5: 281 / 303 methods recompile

JADX recovers 221 more clean methods; JADX has the higher clean rate

cargo run --locked -p disrobe-bench-head-to-head -- --check --only apk-jadx-cfr

APK secrets

8 / 8 planted secrets

apkleaks 2.6.3: 5 / 8

disrobe
 catches the AWS secret key, Basic credential, and JWT apkleaks misses

cargo run -p disrobe-bench-head-to-head

Missing rows are not implied wins. Every surface without a same-input runner stays in the edge table below until one exists.

Edge comparison

Matchups without a same-input runner are tracked inevidence/edge-comparison.mduntil one exists. A missing row there is not an implied win.

## Limits

Recovery is bounded by what the compiler or protector left in the artifact.disrobereports those bounds rather than rounding them away.

Native VM-protector devirtualization.recover_detectedemits bounded verbatim protected-section artifacts for VMProtect and Themida; the Themida route reports.winlicesections as WinLicense. Direct WinLicense, Enigma Protector, Armadillo, Obsidium, PE-Protector, PELock, and Yoda's Protector routes emit no recovered image. Yoda's Protector has an original-assisted comparison carve and an emulator report, but no single-input recovered-image route. The generic VM lifter is validated on Tigress-shape inputs and does not lift these commercial protectors back to source.

Runtime-only decrypt keys.PyArmor v3-v5, ionCube, SourceGuardian, modern Zend Guard, ILProtector, MaxToCode, and Themida-.NET derive their key in a native loader or a live process, and it was never written into the artifact.disrobedetects and identifies the envelope for all of them, plus a partialop_arrayskeleton for the products with a statically-keyed legacy tier.

One-way name hashing.Seedless garble storesbase64(hmac-sha256(name, seed))with the seed absent in-trimpathbuilds. Structure, types, and control flow recover regardless; names are canonicalized, not restored.

Vendor-firmware runtime key.The Airoha OTP-AES key is not present in the carved firmware image, so the format is detected and its members carved, and nothing further.

Encrypted volumes.disrobe extractdetects LUKS1 and, without a key, returns a successful typed wall that names the cipher, mode, digest, iteration count, and missing raw volume key.--luks1-raw-volume-key-file PATHaccepts a bounded key file, while--luks1-raw-volume-key-file -reads the bounded key from standard input. This route supports only LUKS1aes-cbc-plainwith a 128-, 192-, or 256-bit raw volume key and SHA-1, SHA-256, or SHA-512 PBKDF2 header digests. It does not unlock passphrases or keyslots and does not accept XTS or LUKS2. A detached LUKS1 header requires its separately stored encrypted payload. VeraCrypt and TrueCrypt may be undetectable without a key; headerless dm-crypt has no header to detect.

PyArmor BCC native blobs are carved and passed to an in-tree static lift under--allow-bcc. The dedicated PyArmor command and the path-awaredisrobe autoroute emitbcc/bcc-recovery.json,bcc/bcc-pseudo-c.c, andbcc/bcc-recovered.py. The JSON usesdisrobe.pyarmor.bcc.recovery/v1and embeds the existingdisrobe.pyarmor.bcc.function_map/1map. It records modeled functions, unmodeled native disassembly, and typed blob refusals without executing the sample. The lift uses the Microsoft x64 ABI for Windows x86-64, the System V ABI for Linux x86-64, and AAPCS64 for Darwin ARM64. Nuitka, Nim, Zig, and Crystal native bodies are compiled machine code present in the artifact rather than absent; their dedicated recovery paths report what they can lift instead of inheriting a claim from the PyArmor path.

Bytecode-to-source is structurally faithful but never byte-identical:.class,.dex, and CIL erase local names, generics, comments, and exact formatting.

Native decompilation runs on an in-tree backend, which is the default: x86-64 to C or to Rust, AArch64 to pseudo-C, and it rejects a form it cannot recover rather than guessing at one. The two grading levels are separate and are not interchangeable. Leaf-level recompile equivalence is gated bypseudo_c_leaf_oracle.rsandpseudo_rust_leaf_oracle.rs; whole-program bypseudo_c_wholeprog_oracle.rsandpseudo_rust_wholeprog_oracle.rs; the register-only return channel byreturn_channel_corpus.rs. AArch64 is behind x86-64, emits no Rust, and its whole-program path covers validated direct same-image calls in linked ELF inputs only. No committed benchmark compares this backend with Ghidra or IDA, so this page states no ranking against them. Ghidra remains available throughnative decompile --backend ghidra, andnative export --format ghidra|ida|jsonhands either one unpacked, symbol-rich input. Each of these five files grades against a real gcc or clang and falls back to an unmeasured skip when neither is on PATH; settingDISROBE_REQUIRE_NATIVE_TOOLCHAIN=1, which CI does, turns that skip into a failure instead.

## CLI surface

disrobe --helplists direct analysis commands and ecosystem command families. Representative commands:

disrobe auto sample.bin --out recovered/ --capture-stages 
#
 detect and chain, keeping every stage

disrobe catalog native 
#
 supported families and recovery tier

disrobe py decompile module.pyc --out src/ 
#
 CPython 1.0-3.15

disrobe pyarmor unpack protected.py --out out/ --allow-bcc 
#
 static unpack and BCC publication

disrobe js unbundle app.bundle.js --out src/ 
#
 un-webpack, source-map reconstruction

disrobe wasm decompile module.wasm --target rust 
#
 also ts, wat, c

disrobe jvm decompile app.apk --out src/ 
#
 in-house Dalvik decompiler is the default

disrobe dotnet decompile App.dll --out src/ 
#
 in-house CIL to C#/F#/VB

disrobe native unpack packed.exe --out unpacked.bin 
#
 in-house decoders plus x86 stub emulator

disrobe native decompile app.exe --backend native 
#
 x86-64 to C or Rust; AArch64 to pseudo-C

disrobe native disasm stripped.bin --emit cfg-dot 
#
 function discovery plus per-function CFG

disrobe native 
export
 packed.exe --format ghidra 
#
 rebuilt PE plus a Ghidra/IDA/JSON symbol map

disrobe query packed.exe string-decoders 
#
 queryable IR over stripped code

disrobe capabilities packed.exe 
#
 MITRE ATT&CK and MBC with per-match evidence

disrobe taint malware.exe --source recv --sink system 
#
 source-to-sink dataflow over the shared IR

disrobe go recover app --out symbols.json 
#
 pclntab symbols, BuildInfo, garble undo

disrobe lua decompile script.luac --out script.lua 
#
 5.1-5.4, LuaJIT, Luau, IronBrew2 devirt

disrobe shell deob payload.ps1 --out clean.ps1 
#
 PowerShell, bash, batch, VBA, Excel 4.0

disrobe extract firmware.bin --out carved/ --recursive 
#
 carve every supported container format

disrobe webview desktop.exe --out frontend/ 
#
 Electron ASAR, Tauri, or Wails frontend assets

disrobe frisk recovered/ --format sarif 
#
 secrets, endpoints, buckets, IOCs

disrobe prowl example.com --subs --format json 
#
 the one command that touches the network

disrobe report out/ --format html 
#
 self-contained offline forensic report

The complete surface, flag by flag, is in thecommand reference; the flags that apply everywhere are inglobal flags.disrobe passeslists the passes,disrobe catalog [ecosystem]lists every recognized family and its tier, anddisrobe explain <code>looks up anyDR-diagnostic with its cause and fix.

## Library, bindings, and daemon

The CLI is a thin layer over the same crates, so a TUI, an IDE plugin, a web service, or a batch engine drives the full pass set directly. Each pass is its own Rust crate over shareddisrobe-coreanddisrobe-irtypes.import disrobegives a pyo3abi3module for Python 3.9+ that ships.pyiandpy.typed. It takes bytes in, returns typed report objects, and never touches the filesystem.disrobe servespeaks HTTP, gRPC, and LSP, anddisrobe serve --mcpexposes the same operations as Model Context Protocol tools. Signed WebAssembly Component plugins verify and execute under the sandbox as a library capability; the CLI does not yet dispatch an analysis pass through one.

See thelibrary guide, thePython bindings, andthe daemon.

## Architecture

disrobeis a chain runner over single-purpose passes that lower every artifact onto one shared intermediate-representation ladder. Detection fingerprints the input, and the chain runner recursively unpacks and routes it. Each pass recovers what is statically present and reports the rest with a measured score.

 Raw --> Disasm --> MIR --> HIR --> Surface
 bytes opcodes mid high source

Unpacking and decryption operate at Raw, where byte recovery lives. Disassembly produces Disasm. Decompilers do their structural work at MIR and HIR, then render Surface for the checks available to that pass.disrobe-nir-liftcontains bytecode front ends for AVM2, BEAM, CIL, Dalvik, JVM, Lua, Python, WebAssembly, and YARV; native lifting enters through the disassembler.disrobe query,disrobe capabilities, anddisrobe taintconsume the normalized IR through direct CLI commands.disrobe passesprints the separate set of pass IDs that the standard CLI build can reach throughdisrobe auto.

The shared artifact layer can persist recovered state as a.drenvelope: an rkyv payload, a postcard metadata sidecar, and a BLAKE3 root over both. Chain runs also writechain.jsonandrecovery.json;--capture-stagesrecords the exact bytes written by each stage. Commands that implement metadata bundles accept--metadata-pack-1through--metadata-pack-4;--llmis a compatibility alias for pack 4. The bundle is deterministic data for downstream tooling and does not invoke a model.

Thearchitecture guidehas the full model, theIR ladder pagethe rung definitions, and thewhitepaperthe deterministic CPython decompiler, the typed-AST x86-64 lift, managed-VM devirtualization, and the grading discipline behind every claim.

## Safety posture

Every default path is pure static analysis and never executes the sample. The pickle suite is symbolic and never unpickles. Only the PyArmor v6/v7 dynamic hook executes sample code, behind--allow-dynamicwith a watchdog.--allow-bccpermits only in-tree static analysis and does not execute the sample or invoke external tools. Run the dynamic hook inside a sandbox. The parsing surface is hardened against malformed and oversized input. SeeForensics and malware-safety postureand thethreat model.

## Documentation

Full docs site:1-3-7.github.io/disrobe, covering the architecture, the IR ladder, the chain runner, per-language guides,webview desktop recovery, the Python-bindings reference, the complete CLI reference, and the safety posture. The book source is underdocs/.Per-protector stancesrecords the legal posture behind a gray-zone recognizer escalating to a full peel.

Integrations: aGitHub Actionthat scans a path or glob and uploads SARIF to code scanning, apre-commit hookthat blocks a commit on a packed or obfuscated artifact, anMCP server, andeditor pluginsfor VS Code, IDA Pro, Ghidra, and Binary Ninja.

## Legal

Decompilation for security research, interoperability, and recovery of your own source is permitted in most jurisdictions (17 U.S.C. section 1201(f), Directive 2009/24/EC Art. 6, CDPA 1988 ss. 50B-50BA, and equivalents in CA/AU/JP). The full posture with statutory citations and a takedown channel is inLEGAL.md. Legally sensitive recovery paths that need an explicit authorization assertion expose--i-have-authorizationand refuse without it.

## Contributing

Contributions are welcome; see thecontributing guide. For security issues, open aprivate advisoryrather than a public issue. SeeSECURITY.md.

## License

Elastic License 2.0, source-available. Companies and security researchers may use, copy, modify, and distributedisrobefor free; attribution is mandatory, so keep the author, copyright, and licensing notices intact. You may not providedisrobeto third parties as a hosted or managed service, and you may not remove or obscure any licensing, copyright, or other notices. Thedisrobename and marks are reserved and granted no rights by the license. SeeLICENSEandNOTICE.