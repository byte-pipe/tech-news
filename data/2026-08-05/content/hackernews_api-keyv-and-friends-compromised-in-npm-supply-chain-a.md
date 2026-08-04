---
title: Keyv and friends compromised in npm supply chain attack
url: https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack
site_name: hackernews_api
content_file: hackernews_api-keyv-and-friends-compromised-in-npm-supply-chain-a
fetched_at: '2026-08-05T06:00:23.903000'
original_url: https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack
author: cimi_
date: '2026-08-04'
description: Mini Shai-Hulud malware was injected into keyv and eight related npm packages on August 4, 2026 after an attacker compromised the maintainer's GitHub account
tags:
- hackernews
- trending
---

Blog
Vulnerabilities & Threats
Keyv and friends compromised in active Shai-Hulud supply chain attack

# Keyv and friends compromised in active Shai-Hulud supply chain attack

Written by
Ilyas Makari
Published on:
Aug 4, 2026

On August 4, 2026, attackers compromised the GitHub account of the maintainer behindkeyv, a key-value storage library with roughly 127 million weekly npm downloads, and used that access to inject a credential-stealing worm across the entire package family. The same maintainer ownscacheable(29M downloads/month),flat-cache(565M downloads/month),file-entry-cache(557M downloads/month), and several other widely-used caching utilities, all of which were swept up in the same attack.

The compromise was carried out by pushing malicious files directly to themainbranch and then immediately cutting a new release, meaning the poisoned versions were published to npm with valid provenance signed by GitHub Actions.

The compromised packages include:

* keyv6.0.0 (604M/month)
* flat-cache6.1.24 (580M/month)
* file-entry-cache11.1.6 (571M/month)
* cacheable-request13.0.20 (137M/month)
* cacheable2.5.1 (30M/month)
* @cacheable/memory2.2.1 (28M/month)
* cache-manager7.2.10 (16M/month)
* @cacheable/node-cache3.1.2 (6M/month)
* @cacheable/utils2.5.1 (34M/month)
* @cacheable/net2.1.1 (3.7K/month)
* ecto5.0.1 (4.5K/month)

We are also also seeing very active community spread of this supply chain worm to other maintainers and packages, including major organizations:

* @deliveroo/reevent1.0.1
* @or-sdk/invitations1.4.9
* @picsart/ai-sdk3.32.2
* @qlik/embed-runtime1.6.4
* picasso.js2.11.6

Update — August 4, 2026, 13:37 CEST:At least 434 packages (across 1381 versions) have been compromised by the worm, with a combined total of over2 billion monthly installsat the time of writing.

## What happened

Every package in the family received two new files,setup.mjsandMath_Symbol.js, along with a"preinstall": "node setup.mjs"entry added to eachpackage.json. Anyone who rannpm installagainst an affected version would have hadsetup.mjsexecute automatically before their install completed.

setup.mjsis a heavily obfuscated dropper. Its only job is to silently download the Bun JavaScript runtime from github[.]com/oven-sh/bun/releases/download/bun-v1.3.13/ and use it to execute the real payload,Math_Symbol.js:

execFileSync
(<bun binary>, ['<script_dir>/
Math_Symbol
.js'], {

 stdio: 'inherit',

 cwd: <script_dir>

})

TheMath_Symbol.jsis a heavily obfuscated 728 KB JavaScript file containing credential stealers that harvest secrets from the victim's environment, encrypt the findings, and exfiltrate them to a public GitHub repository whose description reads "Shai-Hulud: Here We Go Again". The payload also contains worm-like propagation functionality to infect packages of other maintainers that have installed one of the compromised packages.

## What it steals

TheMath_Symbol.jsfile implements a set of credential extractors, each targeting a different secret store on the victim machine.

npm tokens

Reads~/.npmrcand scans the filesystem for any other.npmrcfiles. ExtractsauthTokenvalues and any//registry.*:_authToken=...entries. Validates each token live againstregistry.npmjs[.]org/-/whoamibefore exfiltrating.

GitHub tokens

Three token formats are targeted: classic PATs (ghp_...) and OAuth tokens (gho_...), GitHub App server-to-server tokens (ghs_...), and JWT OIDC tokens. Sources include~/.config/gh/hosts.yml, environment variables, and a filesystem scan.

On GitHub Actions runners, the payload also executes a shell command that reads the runner process memory directly to dump the entire secret store. It readsACTIONS_ID_TOKEN_REQUEST_TOKENandACTIONS_ID_TOKEN_REQUEST_URLto steal OIDC tokens used for npm publishing.

AWS credentials

* ~/.aws/credentialsand~/.aws/config, parsing all named profiles
* AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY, andAWS_SESSION_TOKENenvironment variables
* EC2 Instance Metadata Service at169.254.169.254, trying IMDSv2 first with a fallback to IMDSv1
* ECS container metadata endpoint at169.254.170.2
* AWS Secrets Manager, callingsecretsmanager:ListSecretsacross multiple regions to enumerate and exfiltrate all secrets stored there

Kubernetes secrets

Reads the service account token, CA certificate, and namespace from/var/run/secrets/kubernetes.io/serviceaccount/. Uses the service account token to query the Kubernetes API directly and retrieve all secrets in the namespace. Also targetsKUBECONFIGand~/.kube/config.

HashiCorp Vault tokens

Checks six sources in priority order: theVAULT_TOKENenvironment variable,~/.vault-token, the GitHub Actions runner path/home/runner/.vault-token, several well-known container paths, a Kubernetes auth login using the stolen service account JWT, and Vault's AWS IAM auth endpoint using any stolen AWS credentials. After obtaining a token, it enumerates all KV stores via/v1/sys/mountsand reads every secret from KV v1 and v2 paths.

Stripe and Slack tokens

Scans for Stripe API keys (both test and live,sk_andpk_prefixes) and Slack tokens (xox[baprs]-...) across all files touched by the filesystem scanner.

Generic filesystem scan

A platform-aware scanner (macOS vs Linux) runs roughly 200 glob patterns across the filesystem, targeting among other things:

* .env,.env.*, and.envrcfiles
* Private key files (*.pem,*.key,*.p12,*.pfx,*.jks)
* SSH keys and config (id_rsa,id_ed25519,.ssh/config)
* Terraform state files and.tfvars
* Docker registry credential files (docker/config.json)
* KeePass databases (*.kdbx)
* VPN configs (*.ovpn)
* IDE config files including.vscode/tasks.jsonand.claude/settings.json

Files over 5 MB are skipped. Up to 64 concurrent reads are used. A generic regex engine is also applied across all scanned files, flagging PEM private keys, SSH public keys, Azure storage keys, database connection strings with embedded credentials, and generickey=valuepatterns matching common secret field names.

## Exfiltration

Once credentials are harvested, the payload encrypts the entire bundle before sending it anywhere. Only the attacker, who holds the corresponding RSA private key, can decrypt what gets uploaded. This means the stolen data sits in plain sight on public infrastructure but is unreadable to anyone else.

The primary exfiltration destination is a public GitHub repository whose description contains the string "Shai-Hulud: Here We Go Again". At the time of writing, GitHub contains roughly 1,300 public repositories matching that string, each serving as a drop point for a victim's encrypted credential bundle.

If the GitHub upload fails, the payload falls back tohttps://npm-cache[.]com:443/router, a domain registered on 2026-05-22 that appears to serve no legitimate purpose. This domain is fetched dynamically from an Ethereum smart contract at0xE1f2395ee43e45A1556EC6438a88c31B83493103, allowing the attacker to rotate infrastructure at any time without touching the payload.

## Self-replicating worm

Beyond stealing credentials, the payload actively uses them to spread the malware to other maintainers and repositories. It has two distinct infection vectors.

npm tarball infection

Using the stolen npm token, the payload callshttps://registry.npmjs[.]org/-/npm/v1/tokensto list every package that token has publish rights to, then fetches and unpacks the current tarball for each one. Before republishing, it makes the following modifications:

* Bumps the patch version by one (e.g.1.2.3becomes1.2.4)
* Adds"preinstall": "node setup.mjs"to the package scripts
* Injectssetup.mjsandmath_init.js(functionally identical toMath_Symbol.js) into the package

It then repacks and publishes the modified tarball to the registry.

This is how the worm propagates beyond the original maintainer. After the initial compromise of thekeyvmaintainer, we observed over 400 packages being infected through community spread. These second-generation infections are identifiable by the use ofmath_init.jsrather thanMath_Symbol.js, since they were seeded by the npm tarball injection worm.

GitHub repo infection

When the payload finds aghs_token, it commits into every branch it can reach, up to 50 branches per repo, working through the most recently active branches first and skippingdependabotandcopilotbranches. It adds malicious hooks to.claude/settings.jsonand.vscode/tasks.jsonso that the payload executes automatically the next time any developer opens the repository in VS Code or starts a Claude Code session inside it, with no npm install required. The commits are authored asclaudewith the emailclaude@users.noreply.github[.]comand carry the messagechore: update config, blending in with real commits.

## How Aikido detects this

If you are an Aikido user, check your central feed and filter on malware issues. This will surface as a 100/100 critical issue. Aikido rescans nightly, but we recommend triggering a manual rescan now.

If you are not yet an Aikido user, you cancreate an accountand connect your repos. Our malware coverage is included in the free plan, no credit card required.

For broader coverage across your whole team, Aikido'sDevice Protectiongives you visibility and control over the software packages installed on your team's devices. It covers browser extensions, code libraries, IDE plugins, and build dependencies, all in one place. Stop malware before it gets installed.

For future protection, considerAikido Safe Chain(open source). Safe Chain sits in your existing workflow, intercepting npm, npx, yarn, pnpm, and pnpx commands and checking packages againstAikido Intelbefore install.

## Indicators of Compromise (IOCs)

Files

* setup.mjs‍SHA-25654dc7ea54a1317cca0e890a2770630cf7fa6c97813e0cb9d2caa93012b350668
* SHA-25654dc7ea54a1317cca0e890a2770630cf7fa6c97813e0cb9d2caa93012b350668
* setup.mjs(community-spread version)SHA-256fd3ca4007b225fdf8de7af4345a19179d5efa8c4bb9205f88cda806e5684b1eb
* SHA-256fd3ca4007b225fdf8de7af4345a19179d5efa8c4bb9205f88cda806e5684b1eb
* Math_Symbol.jsandmath_init.js‍SHA-2569fc2570b7cef51c1b8df116d144d11ff4096357be7d2c4c6367cfc2509cf1bcc
* SHA-2569fc2570b7cef51c1b8df116d144d11ff4096357be7d2c4c6367cfc2509cf1bcc

Network

* https://npm-cache[.]com:443/router— exfiltration endpoint
* eth-mainnet.nodereal[.]iorequest containing0xE1f2395ee43e45A1556EC6438a88c31B83493103

Other

* Any public GitHub repository with description containing"Shai-Hulud: Here We Go Again"— these are the attacker-controlled repos used for credential exfiltration.

‍

4.7/
5
Tired of false positives? 
Try Aikido like 
100k others.
Start Now
Get a personalized walkthrough

Trusted by 100k+ teams

Book Now
Scan your app for IDORs and real attack paths

Trusted by 100k+ teams

Start Scanning
See how AI pentests your app

Trusted by 100k+ teams

Start Testing
Start Now
Similar Posts
See all

July 31, 2026
•
Vulnerabilities & Threats

## Anthropic's Fever Dream: Claude's package that stole real keys

Anthropic disclosed an agent that pushed real malware to PyPI. We think we found the package, and every mistake in it points back to the AI.

#
AI
#
AI Safety
#
Malware

July 22, 2026
•
Vulnerabilities & Threats

## Finding eight high-severity vulnerabilities in NodeBB in six hours

Eight high-severity NodeBB vulnerabilities, found by our AI Pentest in six hours. Full technical breakdown of the XSS chains, auth bypasses, and post hijacking.

#
AI Penetration Testing
#
Vulnerabilities

July 19, 2026
•
Vulnerabilities & Threats

## SleeperGem: RubyGems supply chain attack targets dormant maintainer accounts

SleeperGem: two dormant RubyGems maintainer accounts were hijacked to inject malware into trusted gems, one with over 500,000 total downloads

#
Malware

## Get secure now

Secure your code, cloud, and runtime in one central system.Find and fix vulnerabilitiesfastautomatically.

Start Scanning
Book a demo
No credit card required | Scan results in 32secs.