---
title: Cyber Index Benchmarking | Artificial Analysis
url: https://artificialanalysis.ai/methodology/cyber-index
site_name: tldr
content_file: tldr-cyber-index-benchmarking-artificial-analysis
fetched_at: '2026-09-29T07:30:24.165364'
original_url: https://artificialanalysis.ai/methodology/cyber-index
date: '2026-09-29'
description: Methodology for the Artificial Analysis Cyber Index, which measures AI model capability on enterprise cyber defense.
tags:
- tldr
---

Artificial Analysis
K
 Benchmarking Methodology

# Artificial Analysis Cyber Index Benchmarking Methodology

## Artificial Analysis Cyber Index

The Artificial Analysis Cyber Index tests agentic cyber defense work: discovering vulnerabilities in a codebase, reproducing and validating them, and patching them without breaking existing functionality. It combines three evaluations from industry partners and academia: CWE-Bench-AA (Collinear AI), DeepsecBench-AA (Vercel), and CyberGym-E2E-AA (Berkeley RDI).

The Cyber Index measures defense only. Every task starts with access to the source code, as a security engineer auditing an application would, and no task asks a model to turn a vulnerability into a working exploit. Like all evaluation metrics, it has limitations and may not apply directly to every use case.

The Cyber Index covers identifying and remediating vulnerabilities in source code. It does not cover incident response, writing new code without introducing vulnerabilities, targets without source access such as compiled software or live servers, or exploit realization.

We run every evaluation on our open-source agent harness,Stirrup, giving every model the same prompts and tools within each evaluation. We record cases where a model or provider declines a task on safety grounds and report them separately from the score.

Cyber Index evaluation suite

The Cyber Index is an equally weighted average of its three evaluations.

Evaluation
Tasks
Repeats
Response Type
Scoring
Cyber Index 
 Weighting
Tool 
 Usage
CWE-Bench-AA
120 held-out tasks (10 OWASP categories)
1
Agentic audit-and-patch of a real open-source repository
Deterministic verifier (exploit blocked + legitimate behavior still works), pass@1
1/3
✓
DeepsecBench-AA
Private evaluation, scored against an expert-verified golden set
3
Agentic static review of open-source application code, submitting findings
LLM judge validates findings and matches them to the golden set, median F2 across repeats
1/3
✓
CyberGym-E2E-AA
131 memory-safety vulnerabilities from 131 C/C++ projects*
1
Agentic proof-of-concept input and source patch
Sanitizer crash, patch and functionality test verification (stage 3), pass@1
1/3
✓

* A filtered subset of the CyberGym-E2E dataset, with one task per project. SeeCyberGym-E2E-AAfor how the tasks were selected.

## Artificial Analysis Cyber Index Evaluations

The three evaluations in the Artificial Analysis Cyber Index.

### CWE-Bench-AA

* Status:Included in the Artificial Analysis Cyber Index at 1/3 weighting.
* Description:CWE-Bench-AA is Artificial Analysis' implementation of Collinear AI'sCWE-bench, a defensive cybersecurity benchmark that evaluates coding agents on auditing open-source codebases for security weaknesses and patching them without breaking legitimate behavior. Each task mirrors a real security audit: the agent receives a repository checkout and a single instruction to audit the code and fix what it finds. Collinear AI includes tasks that reproduce disclosed CVEs. The task describes the area of concern but does not give the exact location, and agents are never asked to create exploits.
* Benchmark:https://cwe-bench.com/
* Dataset:120 held-out tasks, private to Collinear AI and Artificial Analysis. The set covers all ten OWASP Top 10 (2025) categories across C/C++, Go, Java, JavaScript/TypeScript, Python, and Rust. Collinear AI built the set to exclude tasks solvable from memorized fixes alone.
* Agent harness:https://github.com/ArtificialAnalysis/Stirrup
* Implementation:Each task runs in an isolated sandboxed container on our Harbor runtime with no internet access. The agent is given the repository checkout and the audit instruction only.We run all models on our open-source agent harness,Stirrup, in a standard reason-and-act tool-use loop, with 2 hours to complete each task.Grading is deterministic and runs inside the same sandbox after the agent finishes. The task's programmatic verifier confirms that the exploit no longer works and that legitimate behavior still works, returning 1 if both hold and 0 otherwise.We run each task once. The headline score ispass@1, the mean score across the 120 tasks.Differences from Collinear AI's leaderboard:CWE-Bench-AA is our implementation, run on our Stirrup harness and agent prompts, so our numbers are not directly comparable to the results published at cwe-bench.com.
* Each task runs in an isolated sandboxed container on our Harbor runtime with no internet access. The agent is given the repository checkout and the audit instruction only.
* We run all models on our open-source agent harness,Stirrup, in a standard reason-and-act tool-use loop, with 2 hours to complete each task.
* Grading is deterministic and runs inside the same sandbox after the agent finishes. The task's programmatic verifier confirms that the exploit no longer works and that legitimate behavior still works, returning 1 if both hold and 0 otherwise.
* We run each task once. The headline score ispass@1, the mean score across the 120 tasks.
* Differences from Collinear AI's leaderboard:CWE-Bench-AA is our implementation, run on our Stirrup harness and agent prompts, so our numbers are not directly comparable to the results published at cwe-bench.com.

### DeepsecBench-AA

* Status:Included in the Artificial Analysis Cyber Index at 1/3 weighting.
* Description:DeepsecBench-AA is our implementation of Vercel'sDeepsecBench, a benchmark that measures how well models find vulnerabilities in application code. The agent reviews real open-source application code, pinned to a commit from before major vulnerability fixes, and reports the vulnerabilities and significant bugs it finds. In each task, the agent is given up to five files flagged by the Deepsec scanner, plus the flags themselves, and investigates whether they point to real vulnerabilities. We score findings against a golden set of vulnerabilities verified by human experts. The agent reviews source code only and is never asked to run the application or exploit what it finds.
* Benchmark:https://vercel.com/blog/deepsecbench-evaluating-model-performance-in-finding-cybersecurity-vulnerabilities
* Dataset:A private evaluation scored against a golden set of vulnerabilities and bugs verified by human experts.
* Agent harness:https://github.com/ArtificialAnalysis/Stirrup
* Implementation:Each batch runs in an isolated E2B sandbox containing the pinned repository, with no internet access. We run all models on our open-source agent harness,Stirrup, with code execution and image viewing tools and a limit of 500 turns per batch. The agent submits its findings through asubmit_findingstool.The prompt is adapted from DeepsecBench's investigation prompt. It asks for security vulnerabilities, classified as critical, high or medium severity, alongside non-security bugs, and lists the vulnerability categories to look for and the mitigations to check before reporting a finding.GPT-5.6 Sol (high) is the judge. It first decides whether each finding is a true or false positive, then matches findings to the golden set.Recall is the share of golden findings the agent matched. Precision is the share of reported findings the judge accepts as real, with duplicate reports counted against precision. Real findings outside the golden set count toward precision but not recall.Following Vercel, the headline score isF2, which weights recall more heavily than precision: a missed vulnerability goes unfixed, while a false positive costs triage time.where P is precision and R is recall. We run the evaluation three times and report the median F2.Differences from Vercel's results:DeepsecBench-AA runs every model on our Stirrup harness, so our numbers are not directly comparable to the results Vercel publishes.
* Each batch runs in an isolated E2B sandbox containing the pinned repository, with no internet access. We run all models on our open-source agent harness,Stirrup, with code execution and image viewing tools and a limit of 500 turns per batch. The agent submits its findings through asubmit_findingstool.
* The prompt is adapted from DeepsecBench's investigation prompt. It asks for security vulnerabilities, classified as critical, high or medium severity, alongside non-security bugs, and lists the vulnerability categories to look for and the mitigations to check before reporting a finding.
* GPT-5.6 Sol (high) is the judge. It first decides whether each finding is a true or false positive, then matches findings to the golden set.
* Recall is the share of golden findings the agent matched. Precision is the share of reported findings the judge accepts as real, with duplicate reports counted against precision. Real findings outside the golden set count toward precision but not recall.
* Following Vercel, the headline score isF2, which weights recall more heavily than precision: a missed vulnerability goes unfixed, while a false positive costs triage time.where P is precision and R is recall. We run the evaluation three times and report the median F2.
* Differences from Vercel's results:DeepsecBench-AA runs every model on our Stirrup harness, so our numbers are not directly comparable to the results Vercel publishes.

### CyberGym-E2E-AA

* Status:Included in the Artificial Analysis Cyber Index at 1/3 weighting.
* Description:CyberGym-E2E-AA is our implementation ofCyberGym-E2E, from the Berkeley Center for Responsible, Decentralized Intelligence (RDI), which tests the full defensive loop on real memory-safety vulnerabilities. The agent must locate a vulnerability in a C/C++ open-source project, write a proof-of-concept (PoC) input that triggers a sanitizer crash, and patch the code so the crash no longer reproduces while the project's functionality tests still pass. It extends CyberGym, which asked agents only to reproduce vulnerabilities, by adding the patch.
* Benchmark:https://www.cybergym.io/cybergym-e2e/
* Paper:https://arxiv.org/abs/2606.04460
* Original dataset:https://huggingface.co/datasets/sunblaze-ucb/cybergym-e2e
* Dataset:The original dataset contains 920 vulnerabilities across 139 open-source projects, drawn from Google's OSS-Fuzz. We use a filtered set of 131 tasks, with one task per project, selecting tasks based on difficulty and filtering out those with oracle leaks or sandbox compatibility constraints.### View all131tasks and sandbox configurationsRepoTask IDCPUsMemory (GB)arduinojsonarduinojson/arvo_2463324arrowarrow/arvo_63679816assimpassimp/arvo_5905648bind9bind9/arvo_6318624binutilsbinutils/arvo_5702524boringsslboringssl/arvo_5555648botanbotan/arvo_658148c-blosc2c-blosc2/arvo_2644248capstonecapstone/arvo_1346724clamavclamav/arvo_2349948cpython3cpython3/oss-fuzz_368076875832curlcurl/arvo_6601248cycloneddscyclonedds/arvo_5129224duckdbduckdb/arvo_56682816elfutilselfutils/arvo_56179816exiv2exiv2/arvo_4599324faad2faad2/arvo_5828724ffmpegffmpeg/oss-fuzz_42537616816filefile/arvo_4873624flacflac/arvo_1706924flatbuffersflatbuffers/arvo_4688324fluent-bitfluent-bit/arvo_3375024fmtfmt/arvo_2588448freetype2freetype2/arvo_36824fribidifribidi/arvo_3469548gdalgdal/arvo_407148ghostscriptghostscript/oss-fuzz_40245173124glibglib/arvo_2845848gpacgpac/arvo_6704324gpsdgpsd/oss-fuzz_4253788324gstreamergstreamer/arvo_5481124h2oh2o/arvo_262324h3h3/arvo_5120824haproxyhaproxy/oss-fuzz_41585046224harfbuzzharfbuzz/arvo_2109248hdf5hdf5/arvo_5870124hiredishiredis/arvo_2877724hoextdownhoextdown/arvo_2376424htslibhtslib/arvo_6582024hunspellhunspell/arvo_5219524igraphigraph/arvo_2940824imagemagickimagemagick/arvo_571024irssiirssi/arvo_3149124jqjq/arvo_6457424jsoncppjsoncpp/arvo_1814024kamailiokamailio/arvo_4223824kmimekmime/oss-fuzz_441263171816lcmslcms/arvo_5041424leptonicaleptonica/arvo_2343348libaomlibaom/arvo_1057424libarchivelibarchive/arvo_3876624libavclibavc/arvo_5596424libbpflibbpf/arvo_4036324libconfiglibconfig/oss-fuzz_39197564724libdwarflibdwarf/oss-fuzz_38574212524libexiflibexif/arvo_4691724libgit2libgit2/arvo_1888224libheiflibheif/arvo_6171848libhevclibhevc/arvo_2319724libicallibical/oss-fuzz_39294887124libidn2libidn2/arvo_1242024libjxllibjxl/oss-fuzz_450328034816liblouisliblouis/arvo_6072324libpcaplibpcap/arvo_4886324libphonenumberlibphonenumber/oss-fuzz_41316135748libplistlibplist/arvo_4469524librawlibraw/oss-fuzz_39913850224librawspeedlibrawspeed/arvo_439648libsndfilelibsndfile/arvo_2680324libspectrelibspectre/arvo_2163824libspnglibspng/arvo_1493524libsshlibssh/arvo_1048624libssh2libssh2/arvo_6521224libtpmslibtpms/oss-fuzz_4253712824libultrahdrlibultrahdr/oss-fuzz_4253544724libvipslibvips/arvo_3948148libwebplibwebp/oss-fuzz_449246999816libwebsocketslibwebsockets/arvo_4895924libxaaclibxaac/arvo_6238824libxml2libxml2/arvo_5741024libxsltlibxslt/arvo_5743624lldpdlldpd/arvo_5200624lualua/arvo_3154124mapservermapserver/arvo_5206624matiomatio/oss-fuzz_40718536124md4cmd4c/arvo_3133224minizminiz/arvo_2787124mongoosemongoose/arvo_5175724mosquittomosquitto/arvo_5700224mrubymruby/arvo_4721324mupdfmupdf/arvo_5920748net-snmpnet-snmp/arvo_5246524ntopngntopng/arvo_6542848oatppoatpp/oss-fuzz_391916478816open62541open62541/arvo_3974124openexropenexr/arvo_46309816openjpegopenjpeg/arvo_1897948openscopensc/arvo_2818548opensipsopensips/arvo_5308024opensslopenssl/arvo_824148openthreadopenthread/oss-fuzz_41146053024p11-kitp11-kit/arvo_3127624pcappluspluspcapplusplus/arvo_4340824pcre2pcre2/arvo_6729748phpphp/arvo_6199348qpdfqpdf/oss-fuzz_4253515248quickjsquickjs/oss-fuzz_41629814924radare2radare2/arvo_1370448readstatreadstat/arvo_1266224selinuxselinux/arvo_4320924skcmsskcms/arvo_652124sleuthkitsleuthkit/arvo_3695524spice-usbredirspice-usbredir/arvo_3686124sudoerssudoers/arvo_3125024swift-protobufswift-protobuf/oss-fuzz_42534949816tinygltftinygltf/arvo_4212324tinysparqltinysparql/oss-fuzz_396460492816unitunit/oss-fuzz_4253634824upxupx/oss-fuzz_38319407948uriparseruriparser/oss-fuzz_38973191324util-linuxutil-linux/arvo_5314924wamrwamr/oss-fuzz_40492104748wasm3wasm3/arvo_3331824wavpackwavpack/arvo_2006024wiresharkwireshark/arvo_1436816wolfsslwolfssl/oss-fuzz_44577394448wtwt/oss-fuzz_37068942148yarayara/arvo_3895224zeekzeek/arvo_55430816zlibzlib/arvo_4990324zstdzstd/arvo_4336524
* ### View all131tasks and sandbox configurationsRepoTask IDCPUsMemory (GB)arduinojsonarduinojson/arvo_2463324arrowarrow/arvo_63679816assimpassimp/arvo_5905648bind9bind9/arvo_6318624binutilsbinutils/arvo_5702524boringsslboringssl/arvo_5555648botanbotan/arvo_658148c-blosc2c-blosc2/arvo_2644248capstonecapstone/arvo_1346724clamavclamav/arvo_2349948cpython3cpython3/oss-fuzz_368076875832curlcurl/arvo_6601248cycloneddscyclonedds/arvo_5129224duckdbduckdb/arvo_56682816elfutilselfutils/arvo_56179816exiv2exiv2/arvo_4599324faad2faad2/arvo_5828724ffmpegffmpeg/oss-fuzz_42537616816filefile/arvo_4873624flacflac/arvo_1706924flatbuffersflatbuffers/arvo_4688324fluent-bitfluent-bit/arvo_3375024fmtfmt/arvo_2588448freetype2freetype2/arvo_36824fribidifribidi/arvo_3469548gdalgdal/arvo_407148ghostscriptghostscript/oss-fuzz_40245173124glibglib/arvo_2845848gpacgpac/arvo_6704324gpsdgpsd/oss-fuzz_4253788324gstreamergstreamer/arvo_5481124h2oh2o/arvo_262324h3h3/arvo_5120824haproxyhaproxy/oss-fuzz_41585046224harfbuzzharfbuzz/arvo_2109248hdf5hdf5/arvo_5870124hiredishiredis/arvo_2877724hoextdownhoextdown/arvo_2376424htslibhtslib/arvo_6582024hunspellhunspell/arvo_5219524igraphigraph/arvo_2940824imagemagickimagemagick/arvo_571024irssiirssi/arvo_3149124jqjq/arvo_6457424jsoncppjsoncpp/arvo_1814024kamailiokamailio/arvo_4223824kmimekmime/oss-fuzz_441263171816lcmslcms/arvo_5041424leptonicaleptonica/arvo_2343348libaomlibaom/arvo_1057424libarchivelibarchive/arvo_3876624libavclibavc/arvo_5596424libbpflibbpf/arvo_4036324libconfiglibconfig/oss-fuzz_39197564724libdwarflibdwarf/oss-fuzz_38574212524libexiflibexif/arvo_4691724libgit2libgit2/arvo_1888224libheiflibheif/arvo_6171848libhevclibhevc/arvo_2319724libicallibical/oss-fuzz_39294887124libidn2libidn2/arvo_1242024libjxllibjxl/oss-fuzz_450328034816liblouisliblouis/arvo_6072324libpcaplibpcap/arvo_4886324libphonenumberlibphonenumber/oss-fuzz_41316135748libplistlibplist/arvo_4469524librawlibraw/oss-fuzz_39913850224librawspeedlibrawspeed/arvo_439648libsndfilelibsndfile/arvo_2680324libspectrelibspectre/arvo_2163824libspnglibspng/arvo_1493524libsshlibssh/arvo_1048624libssh2libssh2/arvo_6521224libtpmslibtpms/oss-fuzz_4253712824libultrahdrlibultrahdr/oss-fuzz_4253544724libvipslibvips/arvo_3948148libwebplibwebp/oss-fuzz_449246999816libwebsocketslibwebsockets/arvo_4895924libxaaclibxaac/arvo_6238824libxml2libxml2/arvo_5741024libxsltlibxslt/arvo_5743624lldpdlldpd/arvo_5200624lualua/arvo_3154124mapservermapserver/arvo_5206624matiomatio/oss-fuzz_40718536124md4cmd4c/arvo_3133224minizminiz/arvo_2787124mongoosemongoose/arvo_5175724mosquittomosquitto/arvo_5700224mrubymruby/arvo_4721324mupdfmupdf/arvo_5920748net-snmpnet-snmp/arvo_5246524ntopngntopng/arvo_6542848oatppoatpp/oss-fuzz_391916478816open62541open62541/arvo_3974124openexropenexr/arvo_46309816openjpegopenjpeg/arvo_1897948openscopensc/arvo_2818548opensipsopensips/arvo_5308024opensslopenssl/arvo_824148openthreadopenthread/oss-fuzz_41146053024p11-kitp11-kit/arvo_3127624pcappluspluspcapplusplus/arvo_4340824pcre2pcre2/arvo_6729748phpphp/arvo_6199348qpdfqpdf/oss-fuzz_4253515248quickjsquickjs/oss-fuzz_41629814924radare2radare2/arvo_1370448readstatreadstat/arvo_1266224selinuxselinux/arvo_4320924skcmsskcms/arvo_652124sleuthkitsleuthkit/arvo_3695524spice-usbredirspice-usbredir/arvo_3686124sudoerssudoers/arvo_3125024swift-protobufswift-protobuf/oss-fuzz_42534949816tinygltftinygltf/arvo_4212324tinysparqltinysparql/oss-fuzz_396460492816unitunit/oss-fuzz_4253634824upxupx/oss-fuzz_38319407948uriparseruriparser/oss-fuzz_38973191324util-linuxutil-linux/arvo_5314924wamrwamr/oss-fuzz_40492104748wasm3wasm3/arvo_3331824wavpackwavpack/arvo_2006024wiresharkwireshark/arvo_1436816wolfsslwolfssl/oss-fuzz_44577394448wtwt/oss-fuzz_37068942148yarayara/arvo_3895224zeekzeek/arvo_55430816zlibzlib/arvo_4990324zstdzstd/arvo_4336524
* Agent harness:https://github.com/ArtificialAnalysis/Stirrup
* Implementation:Each task runs in an isolated sandbox built from the project's OSS-Fuzz build image. The agent receives the vulnerable source tree, build scripts and test scripts, and builds the project with AddressSanitizer or MemorySanitizer.We run all models on our open-source agent harness,Stirrup, with a 90-minute agent time limit per task. While working, the agent can run the first three verification stages itself to check that its PoC crashes the unpatched build, that its patch stops the crash, and that the project's tests still pass.If the agent concludes it cannot demonstrate a vulnerability, it can finish without a finding. This scores zero, and we record it separately from a submission that fails verification.Grading is execution-based and runs after the agent finishes in a separate verifier container, isolated from the agent's environment and built from the original source, in four cumulative stages:Stage 1:the agent's PoC crashes the unpatched buildStage 2:the agent's patch fixes that crashStage 3:the patched project still passes its developer-written functionality testsStage 4 (diagnostic):the patch also fixes the ground-truth vulnerabilityA task scores 1 only if stages 1 to 3 all pass. Stage 4 is recorded as a diagnostic and does not count toward the score. The headline score ispass@1: the share of the 131 tasks solved on a single attempt.Differences from Berkeley RDI's results:We run a 131-task subset on our Stirrup harness, so our numbers are not directly comparable to the results Berkeley RDI publishes.
* Each task runs in an isolated sandbox built from the project's OSS-Fuzz build image. The agent receives the vulnerable source tree, build scripts and test scripts, and builds the project with AddressSanitizer or MemorySanitizer.
* We run all models on our open-source agent harness,Stirrup, with a 90-minute agent time limit per task. While working, the agent can run the first three verification stages itself to check that its PoC crashes the unpatched build, that its patch stops the crash, and that the project's tests still pass.
* If the agent concludes it cannot demonstrate a vulnerability, it can finish without a finding. This scores zero, and we record it separately from a submission that fails verification.
* Grading is execution-based and runs after the agent finishes in a separate verifier container, isolated from the agent's environment and built from the original source, in four cumulative stages:Stage 1:the agent's PoC crashes the unpatched buildStage 2:the agent's patch fixes that crashStage 3:the patched project still passes its developer-written functionality testsStage 4 (diagnostic):the patch also fixes the ground-truth vulnerability
* Stage 1:the agent's PoC crashes the unpatched build
* Stage 2:the agent's patch fixes that crash
* Stage 3:the patched project still passes its developer-written functionality tests
* Stage 4 (diagnostic):the patch also fixes the ground-truth vulnerability
* A task scores 1 only if stages 1 to 3 all pass. Stage 4 is recorded as a diagnostic and does not count toward the score. The headline score ispass@1: the share of the 131 tasks solved on a single attempt.
* Differences from Berkeley RDI's results:We run a 131-task subset on our Stirrup harness, so our numbers are not directly comparable to the results Berkeley RDI publishes.

## Version History

Version 1.0

September 2026 to current

* Launched the Artificial Analysis Cyber Index with three evaluations, each weighted 1/3: CWE-Bench-AA, DeepsecBench-AA, and CyberGym-E2E-AA