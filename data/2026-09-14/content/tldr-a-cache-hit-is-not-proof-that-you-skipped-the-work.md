---
title: A cache hit is not proof that you skipped the work · Siddhant Khare
url: https://siddhantkhare.com/writing/kv-cache-truth-auditor
site_name: tldr
content_file: tldr-a-cache-hit-is-not-proof-that-you-skipped-the-work
fetched_at: '2026-09-14T16:47:31.792085'
original_url: https://siddhantkhare.com/writing/kv-cache-truth-auditor
author: Siddhant Khare
date: '2026-09-14'
published_date: '2026-09-13T11:30:00+05:30'
description: A deterministic KV-cache truth auditor checks engine attestations against an independent token oracle, observed prompt work, output identity, evaluator correctness, and a hash-bound bundle.
tags:
- tldr
---

Back to writing
 

An exact duplicate reused8 of 9 tokensand required1 token of prompt work.

One interior mutation cut safe reuse to3 of 9 tokens. Namespace isolation forced0 reuse. A capacity revisit ended as the typed verdictevicted. Across all ten cases, cached and no-cache outputs stayed token-identical and every evaluator passed.

That is the shipped result.

EXPECTED PREFIX / OBSERVED WORK
 

Nine tokens. Three different truths.

 
 reused
 
 prompt work
 
Exact duplicate
 
8-token prefix reused
 
verified_hit
 
1
2
3
4
5
6
7
8
9
 
8/9 reused
 
1/9 prompt work
Interior mutation
 
mutation stops reuse at token 3
 
partial_reuse
 
1
2
3
4
5
6
7
8
9
 
3/9 reused
 
6/9 prompt work
Suffix change
 
changed suffix leaves 8 safe tokens
 
partial_reuse
 
1
2
3
4
5
6
7
8
9
 
8/9 reused
 
1/9 prompt work
 
Figure 1.
 Reuse follows the exact safe prefix. Similar-looking requests can create
			different work boundaries, while a changed final token still leaves an eight-token prefix.

Evidence boundary:this is a deterministic synthetic token-level control. It validates the auditor, oracle, attestation path, evaluator, schemas, privacy rules, hashes, and standalone verifier. It does not establish MLX or vLLM speedup, production cache correctness, provider identity, GPU performance, latency savings, or runtime-memory savings.

A runtime can report a cache hit without proving that the intended prefix matched. It can report eight cached tokens while the prompt path still recomputes them. It can reuse state and return a different answer. It can label an isolated namespace as a miss without telling you whether the result came from isolation, eviction, or a cold cache.

The cache event is one statement from one part of the system.

The engine attestation is the statement under test. LLMTraceFX checks it against five independent checks: the token oracle, observed prompt work, output-token identity, evaluator correctness, and the checksum-bound evidence bundle. The claim survives only when the chain agrees.

The demo shipped inLLMTraceFX PR #74at merged commit1a1c195526c42ad0b06648e4840ca19b57767f5a. Its approved head was633fb7aa56b615d6e57712fa645a18c0a280a7ac, reviewed against base96d8a268e35918543f46ec50922d95bbee01e5d4.

## What the ten cases prove

The reference control runs a fixed request sequence through a token-granular cache. For each request, an oracle calculates the reusable prefix from exact token identity and the pinned cache policy. The engine reports its reuse. The prompt path records the work it processed. A no-cache control supplies the output identity and correctness checks.

TEN-CASE SYNTHETIC CONTROL
 

Every attestation matched the oracle and observed work.

 
10/10
 
identity + evaluator
 
Case
Input
Expected
Attested
Work
Verdict
capacity-seed
4
0
0
4
verified miss
cold
9
0
0
9
verified miss
exact-duplicate
9
8
8
1
verified hit
interior-mutation
9
3
3
6
partial reuse
boundary-mutation
9
4
4
5
partial reuse
same-length-different-ids
9
0
0
9
verified miss
suffix-change
9
8
8
1
partial reuse
namespace-isolation
9
0
0
9
verified miss
capacity-pressure
4
0
0
4
verified miss
capacity-revisit
4
0
0
4
evicted
 
capacity-seed
 
verified miss
 
Input
 
4
 
Expected
 
0
 
Attested
 
0
 
Work
 
4
 

Output identity: yes·Evaluator: yes

cold
 
verified miss
 
Input
 
9
 
Expected
 
0
 
Attested
 
0
 
Work
 
9
 

Output identity: yes·Evaluator: yes

exact-duplicate
 
verified hit
 
Input
 
9
 
Expected
 
8
 
Attested
 
8
 
Work
 
1
 

Output identity: yes·Evaluator: yes

interior-mutation
 
partial reuse
 
Input
 
9
 
Expected
 
3
 
Attested
 
3
 
Work
 
6
 

Output identity: yes·Evaluator: yes

boundary-mutation
 
partial reuse
 
Input
 
9
 
Expected
 
4
 
Attested
 
4
 
Work
 
5
 

Output identity: yes·Evaluator: yes

same-length-different-ids
 
verified miss
 
Input
 
9
 
Expected
 
0
 
Attested
 
0
 
Work
 
9
 

Output identity: yes·Evaluator: yes

suffix-change
 
partial reuse
 
Input
 
9
 
Expected
 
8
 
Attested
 
8
 
Work
 
1
 

Output identity: yes·Evaluator: yes

namespace-isolation
 
verified miss
 
Input
 
9
 
Expected
 
0
 
Attested
 
0
 
Work
 
9
 

Output identity: yes·Evaluator: yes

capacity-pressure
 
verified miss
 
Input
 
4
 
Expected
 
0
 
Attested
 
0
 
Work
 
4
 

Output identity: yes·Evaluator: yes

capacity-revisit
 
evicted
 
Input
 
4
 
Expected
 
0
 
Attested
 
0
 
Work
 
4
 

Output identity: yes·Evaluator: yes

 
verified hit
partial reuse
verified miss
evicted
 
Figure 2.
 Input, expected reuse, engine attestation, and observed prompt work are
			token counts. Blocks are not applicable in this token-level control. Output identity and the evaluator
			passed in all ten cases.

The first two rows establish cold state.capacity-seedinserts a four-token candidate.coldthen submits a nine-token request with no reusable prefix. Both areverified_miss.

The exact duplicate is the clean positive control. The oracle expects eight reusable tokens, the engine attests eight, and the prompt path processes one. The verdict isverified_hit.

The interior and boundary mutations change where the exact token prefix stops. The interior mutation reuses three tokens and processes six. The boundary mutation reuses four and processes five. Both arepartial_reuse.

The same-length case is the trap. Its request still contains nine tokens, but the token IDs differ. The oracle expects zero reuse. The engine attests zero. The prompt path processes all nine. Equal length creates no identity.

The suffix-change case keeps an eight-token prefix. It processes the changed final token and returnspartial_reuse, not a full hit.

Namespace isolation also forces zero reuse. Capacity pressure fills the controlled cache. The later capacity revisit has zero reuse and four tokens of prompt work, but its verdict is not a generic miss. The retained predecessor proof and controlled residency observations show that the earlier candidate left the cache, so the verifier returnsevicted.

Every row preservesoutput identity: yesandevaluator: yes. Those checks do not change the cache verdict. They answer separate questions: did reuse alter the output, and did the result remain correct?

## A hit needs an evidence chain

FAIL-CLOSED EVIDENCE CHAIN
 

One statement. Five independent checks.

 
1. 01Engine attestationThe runtime statement under test
2. 02Independent oracleExpected reusable prefix from exact token identity and cache policy
3. 03Observed prompt workThe tokens the prompt path actually processed
4. 04Output identityCached and no-cache output token arrays agree
5. 05EvaluatorThe deterministic task result remains correct
6. 06Hash-bound verifierSchemas, artifacts, source, and checksums agree
 
Timing
null
 
Runtime memory
null
 

Not measured here. Null is not zero.

 
Figure 3.
 The engine attestation is the statement under test. It becomes evidence
			only when the oracle, observed work, output identity, evaluator, and hash-bound verifier agree.

The independent oracle matters because the engine cannot verify itself. It derives the safe prefix from the exact request, cache state, namespace, and policy. That expected count then has to match both the engine's attestation and the amount of prompt work observed.

Output identity adds another boundary. A correct reuse count does not prove that the response stayed the same. The evaluator adds one more. Token-different output can still be correct, and token-identical output can still fail a task if the control itself is wrong.

The bundle verifier binds those claims to artifacts. It checks the allowlist, checksums, schemas, request order, verdict predicates, derived summaries, deterministic report rendering, public privacy rules, and the digest of the Python source that generated the evidence.

Timing and runtime memory remainnullin this control. They are not zero. No token count is converted into latency saved, and no estimated avoided work is presented as observed compute.

## Three lessons from nine tokens

### Equal token count is not equal token identity

cold,same-length-different-ids, andnamespace-isolationall contain nine input tokens and all process nine tokens. The reasons differ.

The cold request has no candidate. The same-length request has the wrong token IDs. The isolated request cannot see a candidate from another namespace. A metric that records only request length and cache-hit rate collapses those distinct states.

The auditor keeps exact identity and namespace in the claim path. Length can describe the request. It cannot establish reusable state.

### Mutation position defines the reusable prefix

Similarity is not the rule. Prefix identity is.

An interior mutation after token three leaves three reusable tokens. A boundary mutation leaves four. A changed suffix leaves eight. The requests may look almost the same to a person, but the first changed token fixes the safe reuse boundary.

That boundary is why the demo compares expected reuse, attested reuse, and prompt work on the same row. If one value moves without the others, the claim fails closed.

### Eviction and isolation are not the same operational case

Zero reuse describes an amount. It does not describe a cause.

Namespace isolation means an otherwise matching candidate was outside the request's namespace. Eviction means a previously resident, compatible candidate was removed under controlled capacity pressure. A cold miss means no reusable predecessor existed.

Cold and namespace isolation both carry the typed verdictverified_miss; their case setup and evidence fields preserve the different causes. The cold case has no candidate. The namespace case records an otherwise matching request under an isolated namespace. Eviction carriesevicted, backed by retained predecessor proof and controlled residency observations. The verdict enum alone does not distinguish cold state from namespace isolation.

## Reproduce the public proof

From the merged LLMTraceFX repository:

make kv-cache-demo

The command writes the verified bundle under:

build/kv-cache-truth-demo/
├── DEMO-SHA256SUMS
├── truth-table.json
└── bundle/
 ├── SHA256SUMS
 ├── audit-manifest.json
 ├── cache-events.jsonl
 ├── claim-matrix.json
 ├── evidence_bundle.py
 ├── report.html
 ├── request-evidence.jsonl
 ├── reuse-alignment.svg
 └── summary.json

The committed public snapshot lives atexamples/cache-audit/kv-truth-demo. Aftermake kv-cache-demo, the merged README documents this locked offline command to verify the generated bundle without trusting the installed entry point:

uv run --offline --no-sync python -I \
 build/kv-cache-truth-demo/bundle/evidence_bundle.py verify \
 --public-dir build/kv-cache-truth-demo/bundle \
 --package-root .

The merged integrity anchors are:

Artifact

SHA-256

DEMO-SHA256SUMS

b27d91ef78679c6ab817611c0c612928a8f8d6008bcfeee998650bf4b97192a1

Bundle 
SHA256SUMS

e67bc0a1881d7d5280327f826f0236c763a1a94599c8f3121d6241717a523434

report.html

2f72af822979ffedb2a9cc675e6c926b89af998aa860b9c0e2de2243c9fcfa18

evidence_bundle.py

f4644e79a78c452c2fecd8e0742142bf4d24bd99e1a089d42b9b75fffdeaac36

truth-table.json

96fc36fc50d9f83ff216a2598edee991d0732442865c885e3421bfe2f1cd09e9

Demo snapshot

415b47b45ea143d5dd487157f671a3fe5e7da90f28e4e0d2a3fc517deeba8f6b

Historical snapshot

6b341c4d3a053cd0945a1b131bccc19dee6544c31d64f6f889eadc4a5d7145db

Evidence catalog

sha256:e727c4992c4582ee9db71801d792f1fe18e9c19a1ff7bcb2b540eaee7d64716f

Workload digest

sha256:71d744c08b9636bdaa151010a8cbc031b995091dda690bb6e8ad21c8702aace5

The bundle records blocks as not applicable because this synthetic reference cache works at token granularity. Timing and runtime-memory fields remain null.

## What was checked before merge

The full local suite completed with4,749 passed and 3 skipped. The focused evidence-catalog suite completed with91 passed.

The exact approved head passed a six-job test matrix, build and wheel checks, both clean bootstrap paths, quality checks, the CodeQL workflow, and CodeQL analysis. Exact-head reviews across code, security, operations UX, and methodology were clean.

One review found a time-of-check to time-of-use risk in standalone verifier execution. The merged change fixes it by creating a private verified script with exclusiveO_EXCLsemantics before execution. The final review and checks cover that fix.

## What this result does not prove

This demo does not prove:

* MLX or vLLM speedup;
* production cache correctness;
* provider or hardware identity;
* GPU performance;
* latency reduction;
* runtime-memory savings;
* block-level cache behavior; or
* that a runtime integration has enough evidence merely because it emits cache events.

It proves a narrower and more useful thing: for a deterministic synthetic token-level control, the auditor records full reuse, partial reuse, verified misses, and eviction while the case evidence preserves namespace isolation. Output identity, evaluator correctness, privacy rules, and hash-bound verification remain intact.

## The result

A cache hit can be true and still fail to prove that work was skipped.

The useful claim is stricter: the independent oracle expected the prefix, the engine attested it, the prompt path skipped it, the output stayed identical, the evaluator passed, and the verifier bound those facts to the exact public bundle.

That is when a cache event becomes evidence.

Evidence:LLMTraceFX·Merged PR #74·Exact merged commit1a1c195·KV-cache audit guide·Public demo snapshot

 
 

### Support independent writing

 

If this post was useful, consider supporting my open source work and independent writing.

 
Sponsor on GitHub
 
Buy me a coffee
 
 Back to all articles