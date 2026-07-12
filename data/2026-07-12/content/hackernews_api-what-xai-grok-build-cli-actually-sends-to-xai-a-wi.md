---
title: What xAI Grok Build CLI actually sends to xAI - a wire-level analysis (grok 0.2.93) · GitHub
url: https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547
site_name: hackernews_api
content_file: hackernews_api-what-xai-grok-build-cli-actually-sends-to-xai-a-wi
fetched_at: '2026-07-12T11:27:20.702851'
original_url: https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547
author: jhoho
date: '2026-07-12'
description: What xAI Grok Build CLI actually sends to xAI - a wire-level analysis (grok 0.2.93) - grok-build-cli-wire-analysis.md
tags:
- hackernews
- trending
---

Instantly share code, notes, and snippets.

# cereblab/grok-build-cli-wire-analysis.md

 Created
 
July 10, 2026 02:13

 

Show Gist options

 

* Download ZIP

 

 

* Star16(16)You must be signed in to star a gist
* Fork1(1)You must be signed in to fork a gist

* Embed# Select an optionEmbedEmbed this gist in your website.ShareCopy sharable link for this gist.Clone via HTTPSClone using the web URL.## No results foundLearn more about clone URLsClone this repository at &lt;script src=&quot;https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547.js&quot;&gt;&lt;/script&gt;
* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.
* Save cereblab/dc9a40bc26120f4540e4e09b75ffb547 to your computer and use it in GitHub Desktop.

 

Embed

# Select an option

 

* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.

## No results found

 

 
 
Learn more about clone URLs

 

 

 Clone this repository at &lt;script src=&quot;https://gist.github.com/cereblab/dc9a40bc26120f4540e4e09b75ffb547.js&quot;&gt;&lt;/script&gt;

 

 

Save cereblab/dc9a40bc26120f4540e4e09b75ffb547 to your computer and use it in GitHub Desktop.

Download ZIP

 What xAI Grok Build CLI actually sends to xAI - a wire-level analysis (grok 0.2.93)
 

 

Raw

 grok-build-cli-wire-analysis.md
 

# What xAI's Grok Build CLI Actually Sends to xAI: A Wire-Level Analysis

A measured, reproducible teardown. Findings are backed by captured artifacts (endpoint, HTTP method, status code, byte size, host) and repro commands; where an observation was seen live but not retained as a file, §7 says so explicitly. Section 8 is an evidence appendix with SHA-256s and a "what we did not prove" list. All captures are of my own traffic on my own machine, using a throwaway repository containing fake "canary" secrets — no real credentials were exposed.

## 0. Summary

xAI's officialGrok Buildcoding CLI (grok), on a normal consumer login, does three things worth documenting precisely:

1. It transmits the contents of files it reads — including a.envsecrets file — to xAI, verbatim and unredacted.The secret appears intwochannels: the live model turn (POST /v1/responses) and asession_statearchive uploaded andaccepted (HTTP 200)viaPOST /v1/storage— the endpoint the binary routes to thegrok-code-session-tracesGCS bucket (see §5).
2. It uploads thewhole repository— every tracked file's content plus git history — independent of what the agent reads.Grok packages the workspace and uploads it viaPOST /v1/storage. Proven directly: on a real codebase, with the prompt"reply OK, do not read any files", Grok uploaded theentire repo as a git bundle(POST /v1/storage → 200);git clone-ing the captured bundle recovers a file the agent wastold not to open—src/_probe/never_read_canary.txt— with its unique markerverbatim, plus the full git history (appendixuploaded_repo.bundle). And it scales: on a12 GBrepo of never-read random files,/v1/storagemoved5.10 GiB, all HTTP 200(truncated mid-stream), while the model-turn channel moved just192 KB— a~27,800× ratiothat pins the upload to the codebase, not to what was read. No storage upload failed; the only non-200s were amodel-usage quota(402/429) on/v1/responsesand one unrelated 404 —nota storage size cap.
3. The storage destination is a Google Cloud Storage bucket,grok-code-session-traces(not AWS S3) — named verbatim in the binary and in a capturedmetadata.json(gs://grok-code-session-traces/…). I did not find this mechanism surfaced in the CLI's install/quickstart materials (not an exhaustive docs audit — §7), it is active by default, anddisabling "Improve the model" does not turn it off(/v1/settingsstill returnedtrace_upload_enabled: true; §6).

None of this proves xAItrainson the data — that is a policy question addressed in §6. What is proven is transmission, acceptance, and storage.

## 1. Subject under test (provenance)

Install: curl -fsSL https://x.ai/cli/install.sh | bash # → ~/.grok/bin/grok
Auth: first launch opens a browser → login to X / SuperGrok (consumer account, not an API key)

Binary identity (repro:file $(readlink -f ~/.grok/bin/grok); ~/.grok/bin/grok --version; shasum -a 256 $(readlink -f ~/.grok/bin/grok)):

~/.grok/bin/grok -> ../downloads/grok-macos-aarch64
Mach-O 64-bit executable arm64
grok 0.2.93 (f00f96316d4b)
SHA-256: 2a97ba675bd992aa9b981e2e83776460d94f469b510c0b8efe28b50d236d767c

The upload machinery is a first-party Rust crate.stringson the binary yields these source paths and constants (repro:strings <binary> | grep -E 'xai-data-collector|grok-code-session-traces|storage.googleapis'):

crates/codegen/xai-data-collector/src/gcs.rs
crates/codegen/xai-data-collector/src/storage_client.rs
crates/codegen/xai-data-collector/src/queue.rs
crates/codegen/xai-data-collector/src/file_access_tracker.rs
crates/codegen/xai-data-collector/src/circuit_breaker_observer.rs
crates/codegen/xai-grok-shell/src/upload/{gcs,turn,trace,manifest}.rs
grok-code-session-traces
storage.googleapis.com
"Uploading bytes to GCS via proxy"

## 2. Method (reproducible)

Environment: macOS, Apple Silicon,grok 0.2.93, July 2026.

1. brew install mitmproxy; run once to generate its CA at~/.mitmproxy/.
2. Trust the CA in theloginkeychain (no sudo; Grok does not certificate-pin against it):security add-trusted-cert -r trustRoot -k ~/Library/Keychains/login.keychain-db \
 ~/.mitmproxy/mitmproxy-ca-cert.pem
3. Run Grok routed through the proxy (amitmdumpaddon logs, per request: method, host, path,response status, request byte size; and saves request bodies for xAI hosts):HTTPS_PROXY=http://127.0.0.1:8080 SSL_CERT_FILE=~/.mitmproxy/mitmproxy-ca-cert.pem \
 grok -p "<prompt>" --cwd <repo>
4. For staged-artifact inspection, race-copy~/.grok/upload_queue/*during the run, thengzip -dc | tar -xO.

Canary repo: each file carries a unique marker so anything appearing in captured traffic is unambiguously traceable to a file. Secrets filesecrets.env/.env:

API_KEY=CANARY7F3A9-SECRET-should-not-leave
DB_PASSWORD=CANARY7F3A9-DBPASS

## 3. Finding 1 — File contents, including a secrets file, are transmitted and accepted (200)

Claim:when Grok reads a file, its contents are transmitted to xAI — serialized into thePOST /v1/responsesmodel-turn body, and packaged into asession_statearchive that is uploaded andaccepted (HTTP 200)viaPOST /v1/storage— with no redaction of the file's contents. A.envis sent like any other file.

Wire artifact— a decrypted 48,070-bytePOST cli-chat-proxy.grok.com/v1/responsesrequest body (identifiable as a model turn by its embedded"messages":[…]"model":"grok-4.5"JSON). It contains the secrets fileverbatim(appendix:secrets_responses_body.bin,secret_verbatim.txt):

…API_KEY=CANARY7F3A9-SECRET-should-not-leave\nDB_PASSWORD=CANARY7F3A9-DBPASS\n…"model":"grok-4.5"…

Repro:grep -a "CANARY7F3A9-DBPASS" secrets_responses_body.bin→ matches. All six file markers (source, logic, README, nested JS, API key, DB password) are recoverable from the decrypted/v1/responsesbodies. (This artifact proves the secret wastransmittedto the/v1/responsesendpoint; the raw body file does not carry the response status, so theacceptance (200)claim is anchored to the/v1/storagechannel immediately below, which is status-mapped inwire_12gb.log.)

Second channel — persisted to Google Cloud Storage.The same content is packaged into asession_statearchive uploaded viaPOST /v1/storage. Proven by decompressing the staged artifact before it drains (appendix:secrets_session_state.tar.gz):

gzip -dc secrets_session_state.tar.gz | tar -xO | grep -ao 'CANARY7F3A9-[A-Z]*'
→ CANARY7F3A9-SECRET, CANARY7F3A9-DBPASS, + all others

So the secret is not only processed in-flight; it is written into an archive destined for storage.

Pre-empting "you told it to read the secrets."A control run with a file the agent was toldnotto open (untouched_secret.txt) and the prompt"Reply exactly OK, do not read any files"producednooccurrence of that file's marker in any captured body. The leak is therefore scoped to files Grokdoesread — but it reads liberally (any file relevant to the task, including a.env) and appliednoredaction to that file's contents. The defect is that a secrets file was transmitted unredacted, not the act of reading.Important scope reconciliation:this control shows the unread file is absent from the/v1/responsesbodies — that isChannel A(files the agent reads). It doesnotclear the separate whole-repo/v1/storagesnapshot in §4 (Channel B), which — by the volume evidence there — does sweep in never-read files; I could not decompress the/v1/storagecodebase chunk to check this specific file. So "unread file not uploaded" is trueonly for the model-turn channel, not for the codebase snapshot. (Two further scope notes: (i) in my runs the.env/secrets.envwas git-tracked; I did not separately test whether a.gitignored file is still uploaded, so I make no gitignore claim — the mechanism is read-driven per thefile_access_trackercrate, but that specific case is untested. (ii) The canary values sat inAPI_KEY=/DB_PASSWORD=keys inside a.env/secrets.envbut were not real-format high-entropy tokens; I provedthis.envwas transmitted unredacted, not that no redactor exists for, say, ansk-…-shaped key.)

## 4. Finding 2 — The whole repo is uploaded at multi-GB scale; the only ceiling is a model quota, not storage size

Claim:Grok uploads a whole-repo snapshot with no storage size wall in the tested range. As the repo grows it switches upload strategy and keeps returning 200; on a 12 GB repo, 73 chunks of ~75.0 MB (5.10 GiB) uploaded with zero failures before the capture was truncated mid-stream.

Wire-captured size sweep (incompressible content so the tar cannot shrink; fresh session each step).Only the 12 GB row was retained as a file(wire_12gb.log); the smaller rows were observed live during the sweep but their logs were not saved (see §7):

Repo size

Upload behavior (observed on the wire)

Status

Artifact

64 MB

single 
POST /v1/storage
, 
req=50548145b
 (48 MB)

200

observed, not retained

~600 MB

POST /v1/storage
 in ~7.5 MB chunks (dozens)

all 200

observed, not retained

~3 GB

POST /v1/storage/multipart/init
 → 
PUT storage.googleapis.com/grok-code-session-traces/multipart/<id>
 in 50 MB parts (direct-GCS PUT lines 
not preserved
 — §7)

all 200

observed, not retained

~12 GB

POST /v1/storage
 in 75 MB chunks (
req≈75014840b
); 73 chunks (~5.1 GB) captured before I stopped the run

all 200, 0 failures

wire_12gb.log

Preserved artifact:wire_12gb.log(appendix). It contains83/v1/storage*200 responses:82content-uploadPOST …/v1/storagerequests — of which73 are chunks of ~75.0 MB each(byte sizes min 75,014,811 / max 75,014,871, totaling5,476,083,317 B = 5.10 GiB / 5.48 GB) plus9smaller POSTs — and1/v1/storage/batch_existsdedup check. Total/v1/storage*request bytes: 5,476,228,005 B.Zerostorage requests failed. The capture was stopped while uploads were still streaming (the last line is another ~75 MB chunk → 200), so this demonstrates≥5.1 GiB uploaded, still climbing when truncated—notthat the full 12 GB completed. Repro (three greps, so no count is ambiguous):grep 'cli-chat-proxy.grok.com/v1/storage' wire_12gb.log | grep -c '> 200'→83(all/v1/storage*);grep 'POST cli-chat-proxy.grok.com/v1/storage ' wire_12gb.log | grep -c '> 200'→82(content POSTs only);grep req=75014 wire_12gb.log | grep -c '> 200'→73(the ~75 MB chunks).

Scope — this is thewhole repo, not just files the agent read.Channel A (§3,/v1/responses) carries files the agent opens. This §4 upload is a separateChannel B: a snapshot of the entire workspace. Two lines of evidence:

* (a) The decisive byte split (load-bearing).In thesamecaptured 12 GB session — a repo of100 % random files the agent never read— the two channels moved wildly different volumes:Channel A/v1/responses(model turns): 196,705 B = 192 KB total, across 5 requests, largest single turn 60,394 B.Channel B/v1/storage: 5,476,228,005 B = 5.10 GiB.That is a~27,800× ratio(5,476,083,317 ÷ 196,705). The modeldemonstrably never ingested the files(192 KB cannot carry 5 GiB of content), yet 5.10 GiB of them left via/v1/storage— and across the sweep the/v1/storagevolumetracks total repo size(64 MB → 12 GB). GB-scale bytes leaving a never-read repo can only be a whole-repo snapshot.
* Channel A/v1/responses(model turns): 196,705 B = 192 KB total, across 5 requests, largest single turn 60,394 B.
* Channel B/v1/storage: 5,476,228,005 B = 5.10 GiB.
* That is a~27,800× ratio(5,476,083,317 ÷ 196,705). The modeldemonstrably never ingested the files(192 KB cannot carry 5 GiB of content), yet 5.10 GiB of them left via/v1/storage— and across the sweep the/v1/storagevolumetracks total repo size(64 MB → 12 GB). GB-scale bytes leaving a never-read repo can only be a whole-repo snapshot.
* (b) The binary's own paths/stringscorroborate the mechanism:after_codebase.tar.gz,xai-grok-shell/src/upload/{trace,turn}.rs,repo_state.upload,"collecting workspace files","spawning background coordinator".
* (c) A staged codebase manifest enumerates a never-read file and content-addresses it to the GCS bucket.In a separate run on areal 298-filecereblab_apicodebase, I race-copied the snapshot Grok staged for upload (appendix:staged_base_tree_manifest.json,staged_metadata.json). The manifest listssrc/_probe/never_read_canary.txt— a file I planted and never asked Grok to open — alongside the real sources (src/apns.ts,src/index.ts, …); andmetadata.jsongives each file a destinationfileIdof the formgs://grok-code-session-traces/repo_changes_dedup/v2/supplemental/sha256_…. So the whole tree, unread files included, is enumerated and content-addressed for upload to the named GCS bucket. (That run was quota-blocked before the content blobs uploaded; the 12 GB run above independently provesGB-scale content actually leaves the wire, all 200.)
* (d) DEFINITIVE — a never-read file'scontentrecovered verbatim from an uploaded git bundle (single SuperGrok run).With the account upgraded (quota lifted), I re-ran on the realcereblab_apirepo with the explicit promptReply with exactly: OK. Do not read or open any files., having planted a unique markerCANARY-XR47P2-NEVERREAD-UNIQUEinsrc/_probe/never_read_canary.txt. Grok uploaded theentire repository as a git bundleviaPOST cli-chat-proxy.grok.com/v1/storage → 200 (req=152102b)(appendixuploaded_repo.bundle, SHA-25673b9c0af06311bae35c3ed03274d0eec2846e76762828d10b09757ca41bd6024). Runninggit clone uploaded_repo.bundlereconstructs the repo, andsrc/_probe/never_read_canary.txtcontains the markerverbatim— a file the agent was explicitly told not to open. The bundle also carries thefull git history(4 commits, 47 files). This is the airtight per-file-content proof: the whole repo — unread files included — left the machine and was accepted (200). The upload mechanism is agit bundle, so "whole repo" is literal (every tracked file + history).Replicated on a second, unrelated codebase:the identical capture on thecereblab_authCloudflare-Worker repo produced a git-bundle upload (POST /v1/storage → 200, 31,743 B) from whichgit clonerecovered its own never-read markerCANARY-AUTH-4T8K2-NEVERREADverbatim (appendixuploaded_repo_auth.bundle, SHA-2560ee536538bcd1ee72a258f9977ab69f8a9b1ac240491b91a4e94335b4d83c768). Two independent repos, same result.

(Prompt note: the 12 GB session was interactive and I did not log its verbatim prompt, but the 192 KB Channel-A total is dispositive that no bulk read occurred whatever the prompt was; a separate headless control run used the explicit promptReply exactly OK, do not read any filesand confirmed an unread file is absent from Channel A.)

(The earlier "one gap" is nowclosedby evidence (d): a single SuperGrok run where a specific never-read file's content is recovered from a wire-captured, 200-status git-bundle upload. The 12 GB run remains the proof that this scales to GB volumes.)

No storage/upload request failed — every one of the 82/v1/storagecalls returned 200.The only non-200s in the entire capture were on the model endpoint plus one session-bookkeeping call (full set fromwire_12gb.log;/v1/responseslines also inmodel_limit.txt):

POST /v1/responses -> 402 (Payment Required) ×1
POST /v1/responses -> 429 (Too Many Requests) ×3
POST /v1/sessions/<id>/replicas/update -> 404 ×1 (session bookkeeping, not an upload)

and finally, in plain text, on stdout:

You've reached your free Grok Build usage limit for now. Get SuperGrok for much higher limits…

The 402/429 are amodel-usage quota; the lone 404 is unrelated to storage. Notably, storage uploads continued to return 200afterthe model turn was rate-limited (76/v1/storage200s occur at or after the first 429) — the codebase upload is independent of whether the model answers.

Pre-empting "you're confusing a local disk cache with an upload."This claim rests strictly onwire-captured 200-status uploadsof file bytes leaving the machine (/v1/storagerequest bodies of 7.5–75 MB in the preservedwire_12gb.log; the 3 GB 50 MBPUTs tostorage.googleapis.comwere also seen on the wire, but that log was not retained — §7). It doesnotrely on the~/.grok/upload_queuedraining — queue-drain is ambiguous (it empties on both success and drop) and is explicitlynotused as evidence here. (An earlier draft that inferred upload from queue-drain was wrong and has been retracted; see §7.)

## 5. Finding 3 — Destination, telemetry, and what's not surfaced in the docs

* Storage destination is Google Cloud Storage, bucketgrok-code-session-traces. This rests on thepreservedbinary stringsgrok-code-session-traces,storage.googleapis.com, and"Uploading bytes to GCS via proxy"(crate_strings.txt),and on a preserved stagedmetadata.jsonwhose per-filefileIds are literallygs://grok-code-session-traces/repo_changes_dedup/v2/…/sha256_…(staged_metadata.json), corroborated by the directstorage.googleapis.commultipart PUTs observed at 3 GB (observed live; that log was not retained — see §7). It isnotAWS S3 (the binary linksaws-sdk-s3for an alternate path and AWS STS/SSO for auth, but the destination named in the binary — and seen on the wire at 3 GB — is GCS).
* Third-party telemetry:POST api.mixpanel.com/trackand/engage(Mixpanel), plusPOST grok.com/_data/v1/events— all 200.
* Not surfaced in setup docs (scope-limited claim):I did not find therepo_state/session_stateupload togrok-code-session-traces, or the~/.grok/upload_queuestaging, described in the CLI's install script or quickstart materials I reviewed (this is not an exhaustive audit of all xAI docs — see §7). The mechanism is active by default on the standard consumer login.
* Reliability note (separate from privacy):~/.grok/upload_queuestages ~3 GB snapshots per turn and, under load, can grow to tens of GB and exhaust the disk. This is a real bug, independent of whether uploads succeed.

## 6. Consent and policy — stated honestly

* "Cloud AI tools send context; this is normal."True, and conceded: any cloud coding agent must send code to its server to act on it. Thenovel deltashere are (a) asecretsfile (e.g..env) is transmittedunredacted, (b) the content ispersistedto a named GCS bucket, not just processed transiently, and (c) the upload mechanism isnot surfaced in the CLI's setup materials(§7) and on by default.
* "It's in the ToS / opt-in."xAI's consumer policy broadly discloses data use for model improvement with an opt-out (grok.com → Settings → Data → "Improve the model"; Private Chat auto-opts-out; opt-out is prospective, not retroactive). Butbroad training disclosure ≠ documenting this specific mechanism.I did not find therepo_state/upload_queue/grok-code-session-tracespipeline described in the CLI materials I reviewed (§7 notes this is not an exhaustive docs audit), so — on those materials — a user is not informed ofitspecifically. Sources: xAI Privacy Policy (https://x.ai/legal/privacy-policy), Consumer ToS (https://x.ai/legal/terms-of-service).
* The "Improve the model" toggle makes no difference — ON or OFF, the whole repo is uploaded the same way.At default settings, Grok uploaded 5.10 GiB of a never-read repo (§4). Then Iturned "Improve the model" offand re-ran: Grokstilluploaded the entire repo as a git bundle (§4(d),POST /v1/storage → 200, the never-read file recovered bygit clone), and the server's/v1/settingsresponse to the CLIstillreturned"trace_upload_enabled": true,"upload_enabled": true,"session_registry_enabled": true(and"max_upload_file_bytes": 1073741824, a 1 GiB per-file cap). The opt-out governstraining, not whether your code is uploaded/stored: the codebase upload togrok-code-session-tracescontinues either way.Opting out does not stop your repository from leaving the machine.

## 7. What we did NOT prove (intellectual honesty)

* We did not prove xAI trains on this data.Upload/storage ≠ training. That is governed by policy and account tier; we measured transmission only.
* The directstorage.googleapis.com/grok-code-session-tracesPUT wire-lines were observed at 3 GB but not preserved in this session(the log was overwritten during the sweep, and re-capture is currently blocked by the model quota). The multi-GB claim in §4 therefore rests on thepreservedwire_12gb.log(/v1/storage200s at 75 MB chunks) plus the binary strings naming the bucket; the direct-PUT capture is reproducible once quota resets.
* Only the 12 GB sweep log was retained.The 64 MB / 600 MB / 3 GB rows were observed live but their capture logs were not saved (reproducible once quota resets). The 12 GB capture itself was stopped mid-stream (~5.1 GB / 73 chunks captured), so it proves multi-GB uploadsucceeds with no failures, not that an entire 12 GB repo run completes end-to-end.
* The "not documented" claim is scope-limited.I based it on the CLI's install script and quickstart, not an exhaustive search of all xAI documentation, help-center articles, or policies. It is possible the mechanism is described somewhere I did not check; the defensible statement is "not surfaced in the CLI's own setup materials."
* Channel B (whole-repo) — now CLOSED (was the one open gap).Evidence §4(d): on a SuperGrok account, a single run wire-captured Grok uploading theentire repository as a git bundleviaPOST /v1/storage → 200;git cloneof the preserveduploaded_repo.bundlerecoverssrc/_probe/never_read_canary.txt— a file the agent was told not to open — with its unique markerverbatim, plus the full git history. So the never-read file'scontent(not just its hash) demonstrably left the machine and was accepted. Thewire_12gb.logrun remains the proof that the same mechanism scales to GB volumes.
* Universal vs. conditional (partially answered):multi-GB upload succeeds on free-tier; the git-bundle content upload succeeds on SuperGrokwith "Improve the model" turned OFF(/v1/settingsreturnedtrace_upload_enabled: true). I didnotfind a setting that disables the upload in these tests, but I did not exhaustively enumerate every account/config permutation, so I don't claim it canneverbe gated.
* One earlier claim was retracted:an initial "the multi-GB blobs fail and are deleted locally, not exfiltrated" conclusion — based on aPID-scopednettopreading (<1 MB) — was wrong. PID/host-scoped egress misses (a) a separate upload coordinator process and (b) presignedPUTs that godirectly to Google IPs, never touching the API host. The wire capture (this document) supersedes that inference.

## 8. Evidence appendix

All artifacts and SHA-256s (MANIFEST.sha256). Binary SHA-256:2a97ba675bd992aa9b981e2e83776460d94f469b510c0b8efe28b50d236d767c.

Artifact

What it proves

secrets_responses_body.bin
 (48 KB)

.env
 contents verbatim in a 
POST /v1/responses
 body

secret_verbatim.txt

the two 
.env
 lines as extracted

secrets_session_state.tar.gz
 (16 KB)

same secret inside the archive uploaded via 
/v1/storage

wire_12gb.log

83 
/v1/storage*
 → 200 on a 12 GB repo = 82 content POSTs (73 chunks ~75.0 MB = 5.10 GiB + 9 small) + 1 
batch_exists
; Channel-A 
/v1/responses
 = 196,705 B (192 KB) total (~27,800× less); 0 storage failures; truncated mid-stream

model_limit.txt

the 
/v1/responses
 failures (402×1, 429×3 — model quota)

crate_strings.txt

xai-data-collector
 paths + 
grok-code-session-traces
 + 
storage.googleapis.com

binary.sha256

binary provenance

gcs_puts.txt

placeholder (empty capture)
 — the 3 GB direct-GCS PUT lines were not retained; note inside explains, re-capture pending quota (§7)

uploaded_repo.bundle
 (152 KB, SHA-256 
73b9c0af…
)

the smoking gun
 — a git bundle wire-captured leaving via 
POST /v1/storage → 200
; 
git clone
 recovers 
src/_probe/never_read_canary.txt
 (never-read) verbatim + full git history (real 
cereblab_api
 repo, SuperGrok, "Improve the model" OFF)

uploaded_repo_auth.bundle
 (SHA-256 
0ee53653…
)

replication
 on a 2nd unrelated repo (
cereblab_auth
 Worker) — git bundle via 
POST /v1/storage → 200
; 
git clone
 recovers its never-read canary 
CANARY-AUTH-4T8K2-NEVERREAD
 verbatim

staged_base_tree_manifest.json

real-code run: the codebase snapshot manifest 
enumerating 
src/_probe/never_read_canary.txt
 (never-read) + 30 real 
src/*.ts
 files

staged_metadata.json

real-code run: per-file destinations 
fileId: gs://grok-code-session-traces/repo_changes_dedup/v2/…/sha256_…
 (names the GCS bucket)

Repro (condensed):

brew install mitmproxy && mitmdump -q -p 8080 # generates ~/.mitmproxy CA
security add-trusted-cert -r trustRoot -k ~/Library/Keychains/login.keychain-db ~/.mitmproxy/mitmproxy-ca-cert.pem
# capture a run:
HTTPS_PROXY=http://127.0.0.1:8080 SSL_CERT_FILE=~/.mitmproxy/mitmproxy-ca-cert.pem grok -p "read every file" --cwd <repo>
# secrets: grep -a CANARY <saved /v1/responses body>
# staged: gzip -dc <staged session_state> | tar -xO | grep CANARY

Integrity:all captures were of my own traffic on my own machine; the "secrets" were fake canary strings; no real credentials were exposed. Findings are version-specific togrok 0.2.93(July 2026); xAI may change behavior at any time.

### tomholfordcommentedJul 12, 2026

 

# either env:
export GROK_TELEMETRY_TRACE_UPLOAD=0
# or broader:
export GROK_TELEMETRY_ENABLED=0

# or ~/.grok/config.toml
[features]
telemetry = false

[telemetry]
trace_upload = false
mixpanel_enabled = false

[harness]
disable_codebase_upload = true

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Sign up for free

to join this conversation on GitHub
.
 Already have an account?
 
Sign in to comment