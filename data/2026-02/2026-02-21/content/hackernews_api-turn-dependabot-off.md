---
title: Turn Dependabot Off
url: https://words.filippo.io/dependabot/
site_name: hackernews_api
content_file: hackernews_api-turn-dependabot-off
fetched_at: '2026-02-21T11:08:51.751021'
original_url: https://words.filippo.io/dependabot/
author: todsacerdoti
date: '2026-02-20'
published_date: '2026-02-20T19:48:08.591285Z'
description: I recommend turning Dependabot off and replacing it with a pair of scheduled GitHub Actions, one running govulncheck, and the other running CI against the latest version of your dependencies.
tags:
- hackernews
- trending
---

20 Feb 2026

# Turn Dependabot Off

Dependabot is a noise machine. It makes you feel like you’re doing work, but you’re actually discouraging more useful work. This isespeciallytrue for security alerts in the Go ecosystem.

I recommend turning it off and replacing it with a pair of scheduled GitHub Actions, one running govulncheck, and the other running your test suite against the latest version of your dependencies.

## A little case study

On Tuesday, Ipublished a security fixforfilippo.io/edwards25519. The(*Point).MultiScalarMultmethod would produce invalid results if the receiver was not the identity point.

A lot of the Go ecosystem depends on filippo.io/edwards25519, mostly throughgithub.com/go-sql-driver/mysql(228k dependents only on GitHub).Essentially no one uses(*Point).MultiScalarMult.

Yesterday, Dependabot openedthousands of PRsagainst unaffected repositories to update filippo.io/edwards25519. These PRs were accompanied by a security alert witha nonsensical, made up CVSS v4 scoreand by a worrying73% compatibility score, allegedly based on the breakage the update is causing in the ecosystem. Note that the diff between v1.1.0 and v1.1.1 isone line in the method no one uses.

We even gotone of these alertsfor the Wycheproof repository, whichdoes not import the affected filippo.io/edwards25519 package at all. Instead, it only imports the unaffected filippo.io/edwards25519/field package.

$ go mod why -m filippo.io/edwards25519
# filippo.io/edwards25519
github.com/c2sp/wycheproof/tools/twistcheck
filippo.io/edwards25519/field

We have turned Dependabot off.

## Use a serious vulnerability scanner instead

But isn’t this toil unavoidable, to prevent attackers from exploiting old vulnerabilities in your dependencies? Absolutely not!

Computers are perfectly capable of doing the work of filtering out these irrelevant alerts for you. TheGo Vulnerability Databasehas rich version, package,and symbolmetadata for all Go vulnerabilities.

Here’sthe entry for the filippo.io/edwards25519 vulnerability, also available instandard OSV format.

modules:
 - module: filippo.io/edwards25519
 versions:
 - fixed: 1.1.1
 vulnerable_at: 1.1.0
 packages:
 - package: filippo.io/edwards25519
 symbols:
 - Point.MultiScalarMult
summary: Invalid result or undefined behavior in filippo.io/edwards25519
description: |-
 Previously, if MultiScalarMult was invoked on an
 initialized point who was not the identity point, MultiScalarMult
 produced an incorrect result. If called on an
 uninitialized point, MultiScalarMult exhibited undefined behavior.
cves:
 - CVE-2026-26958
credits:
 - shaharcohen1
 - WeebDataHoarder
references:
 - advisory: https://github.com/FiloSottile/edwards25519/security/advisories/GHSA-fw7p-63qq-7hpr
 - fix: https://github.com/FiloSottile/edwards25519/commit/d1c650afb95fad0742b98d95f2eb2cf031393abb
source:
 id: go-security-team
 created: 2026-02-17T14:45:04.271552-05:00
review_status: REVIEWED

Any decent vulnerability scanner willat the very leastfilter based on the package, which requires a simplego list -deps ./.... This already silences a lot of noise, because it’s common and good practice for modules to separate functionality relevant to different dependents into different sub-packages.1For example, it would have avoided the false alert against the Wycheproof repository.

If you use a third-party vulnerability scanner, you should demand at least package-level filtering.

Goodvulnerability scanners will go further, though, and filter based on the reachability of the vulnerablesymbolusing static analysis. That’s whatgovulncheckdoes!

$ go mod why -m filippo.io/edwards25519
# filippo.io/edwards25519
filippo.io/sunlight/internal/ctlog
github.com/google/certificate-transparency-go/trillian/ctfe
github.com/go-sql-driver/mysql
filippo.io/edwards25519

$ govulncheck ./...
=== Symbol Results ===

No vulnerabilities found.

Your code is affected by 0 vulnerabilities.
This scan also found 1 vulnerability in packages you import and 2
vulnerabilities in modules you require, but your code doesn't appear to call
these vulnerabilities.
Use '-show verbose' for more details.

govulncheck noticed that my project indirectly depends on filippo.io/edwards25519 through github.com/go-sql-driver/mysql, which does not make the vulnerable symbol reachable, so it chose not to notify me.

If you want, you can tell it to show the package- and module-level matches.

$ govulncheck -show verbose,color ./...
Fetching vulnerabilities from the database...

Checking the code against the vulnerabilities...

The package pattern matched the following 16 root packages:
 filippo.io/sunlight
 filippo.io/sunlight/internal/stdlog
 [...]
Govulncheck scanned the following 54 modules and the go1.26.0 standard library:
 filippo.io/sunlight
 crawshaw.io/sqlite@v0.3.3-0.20220618202545-d1964889ea3c
 filippo.io/bigmod@v0.0.3
 filippo.io/edwards25519@v1.1.0
 filippo.io/keygen@v0.0.0-20240718133620-7f162efbbd87
 filippo.io/torchwood@v0.8.0
 [...]

=== Symbol Results ===

No vulnerabilities found.

=== Package Results ===

Vulnerability #1: GO-2026-4503
 Invalid result or undefined behavior in filippo.io/edwards25519
 More info: https://pkg.go.dev/vuln/GO-2026-4503
 Module: filippo.io/edwards25519
 Found in: filippo.io/edwards25519@v1.1.0
 Fixed in: filippo.io/edwards25519@v1.1.1

=== Module Results ===

Vulnerability #1: GO-2025-4135
 Malformed constraint may cause denial of service in
 golang.org/x/crypto/ssh/agent
 More info: https://pkg.go.dev/vuln/GO-2025-4135
 Module: golang.org/x/crypto
 Found in: golang.org/x/crypto@v0.44.0
 Fixed in: golang.org/x/crypto@v0.45.0

Vulnerability #2: GO-2025-4134
 Unbounded memory consumption in golang.org/x/crypto/ssh
 More info: https://pkg.go.dev/vuln/GO-2025-4134
 Module: golang.org/x/crypto
 Found in: golang.org/x/crypto@v0.44.0
 Fixed in: golang.org/x/crypto@v0.45.0

Your code is affected by 0 vulnerabilities.
This scan also found 1 vulnerability in packages you import and 2
vulnerabilities in modules you require, but your code doesn't appear to call
these vulnerabilities.

It’s easy to integrate govulncheck into your processes or scanners, either using thegovulncheck -jsonCLI or thegolang.org/x/vuln/scanGo API.

### Replace Dependabot with a govulncheck GitHub Action

You can replace Dependabot security alerts with this GitHub Action.

name: govulncheck
on:
 push:
 pull_request:
 schedule: # daily at 10:22 UTC
 - cron: '22 10 * * *'
 workflow_dispatch:
permissions:
 contents: read
jobs:
 govulncheck:
 runs-on: ubuntu-latest
 steps:
 - uses: actions/checkout@v5
 with:
 persist-credentials: false
 - uses: actions/setup-go@v6
 with:
 go-version-file: go.mod
 - run: |
 go run golang.org/x/vuln/cmd/govulncheck@latest ./...

It will run every day and only notify you if there is an actual vulnerability you should pay attention to.

### The cost of alert fatigue

False positive alerts are not only a waste of time, they also reduce security by causing alert fatigue and making proper triage impractical.

A security vulnerability should be assessed for its impact: production might need to be updated, secrets rotated, users notified! A business-as-usual dependency bump is a woefully insufficient remediation for an actual vulnerability, but it’s the only practical response to the constant stream of low-value Dependabot alerts.

This is why as Go Security Team lead back in 2020–2021 I insisted the team invest in staffing the Go Vulnerability Database and implement a vulnerability scanner with static analysis filtering.

The govulncheck Action will not automatically open a PR for you, and that’s a good thing! Now that security alerts are not mostly noise, you can afford to actually look at them and take them seriously, including any required remediation.

Noisy vulnerability scanners also impact the open source ecosystem. I often get issues and PRs demanding I update the dependencies of my projects due to vulnerabilities that don’t affect them, because someone’s scanner is failing to filter them. That’s extra toil dropped at the feet of open source maintainers, which is unsustainable. The maintainer’sresponsibilityis making sure projects are not affected by security vulnerabilities. The responsibility of scanning tools is making sure they don’t disturb their users with false positives.

## Test against latest instead of updating

The other purpose of Dependabot is to keep dependencies up to date, regardless of security vulnerabilities. Your practices and requirements will vary, but I find this misguided, too.

Dependencies should be updated according toyourdevelopment cycle, not the cycle of each of your dependencies. For example you might want to update dependencies all at once when you begin a release development cycle, as opposed to when each dependency completes theirs.

There are two benefits to quick updates, though: first, you can notice and report (or fix) breakage more rapidly, instead of being stalled by an incompatibility that could have been addressed a year prior; second, you reduce your patch deltain caseyou need to update due to a security vulnerability, reducing the risk of having to rush through a refactor or unrelated fixes.

You can capture both of those benefits without actually updating the dependencies by simply running CI against the latest versions of your dependencies every day. You just need to rungo get -u -t ./...before your test suite. In the npm ecosystem, you just runnpm updateinstead ofnpm ci.

This way, you will still be alerted quickly of any potential issues, without having to pay attention to unproblematic updates, which you can defer to whenever fits your project best.

This is a lot safer, too, because malicious code recently added to a dependency will not rapidly reach users or production, but only CI. Supply chain attacks have a short half-life! You can further mitigate the risk by using a CI sandboxing mechanism likegeomys/sandboxed-step, which uses gVisor to removethe ambient authority that GitHub Actions grants every workflow, including supposedly read-only ones.

name: Go tests
on:
 push:
 pull_request:
 schedule: # daily at 10:22 UTC
 - cron: '22 10 * * *'
 workflow_dispatch:
permissions:
 contents: read
jobs:
 test:
 runs-on: ubuntu-latest
 strategy:
 fail-fast: false
 matrix:
 go:
 - { go-version: stable }
 - { go-version-file: go.mod }
 deps:
 - locked
 - latest
 steps:
 - uses: actions/checkout@v5
 with:
 persist-credentials: false
 - uses: actions/setup-go@v6
 with:
 go-version: ${{ matrix.go.go-version }}
 go-version-file: ${{ matrix.go.go-version-file }}
 - uses: geomys/sandboxed-step@v1.2.1
 with:
 run: |
 if [ "${{ matrix.deps }}" = "latest" ]; then
 go get -u -t ./...
 fi
 go test -v ./...

For more spicy open source opinions, follow me on Bluesky at@filippo.abyssdomain.expertor on Mastodon at@filippo@abyssdomain.expert.

## The picture

The Tevere has overflowed its lower banks, so a lot of previously familiar landscapes have changed slightly, almost eerily. This is the first picture I took after being able to somewhat safely descend onto (part of) the river’s banks.

My work is made possible byGeomys, an organization of professional Go maintainers, which is funded byAva Labs,Teleport,Tailscale, andSentry. Through our retainer contracts they ensure the sustainability and reliability of our open source maintenance work and get a direct line to my expertise and that of the other Geomys maintainers. (Learn more in theGeomys announcement.)
Here are a few words from some of them!

Teleport — For the past five years, attacks and compromises have been shifting from traditional malware and security breaches to identifying and compromising valid user accounts and credentials with social engineering, credential theft, or phishing.Teleport Identityis designed to eliminate weak access patterns through access monitoring, minimize attack surface with access requests, and purge unused permissions via mandatory access reviews.

Ava Labs — We atAva Labs, maintainer ofAvalancheGo(the most widely used client for interacting with theAvalanche Network), believe the sustainable maintenance and development of open source cryptographic protocols is critical to the broad adoption of blockchain technology. We are proud to support this necessary and impactful work through our ongoing sponsorship of Filippo and his team.

1. This also makes it possible to prune the tree of dependencies only imported by packages that are not relevant to a specific dependent, which has a large security benefit.↩
