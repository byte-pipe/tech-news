---
title: Keyv and friends compromised in npm supply chain attack
url: https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack
date: 2026-08-04
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-05T06:02:05.861341
---

# Keyv and friends compromised in npm supply chain attack

# Keyv and friends compromised in active Shai‑Hulud supply chain attack

## Overview
- On 4 August 2026 the GitHub account of the maintainer of **keyv** was taken over.  
- The attacker added malicious files to the main branch, cut new releases, and published them to npm with valid GitHub Actions signatures.  
- The worm spreads automatically through npm installs and propagates to other maintainers’ packages.

## Compromised packages
- Core libraries:  
  - `keyv` 6.0.0 (604 M downloads/month)  
  - `flat-cache` 6.1.24 (580 M)  
  - `file-entry-cache` 11.1.6 (571 M)  
  - `cacheable-request` 13.0.20 (137 M)  
- Additional cache utilities: `cacheable`, `cache-manager`, `@cacheable/*` (total ≈ 30 M downloads/month).  
- Other infected packages reported in the community: `@deliveroo/reevent`, `@or-sdk/invitations`, `@picsart/ai-sdk`, `@qlik/embed-runtime`, `picasso.js`.  
- Update (13:37 CEST, 4 Aug 2026): **434 packages** across **1 381 versions** compromised, exceeding **2 billion** monthly installs.

## Attack mechanics
- Each affected package received two new files: `setup.mjs` and `Math_Symbol.js`.  
- `package.json` was modified to include `"preinstall": "node setup.mjs"`.  
- During `npm install`, `setup.mjs` runs automatically, downloading the Bun runtime and executing `Math_Symbol.js`.

## Payload functionality (`Math_Symbol.js`)
- Heavily obfuscated 728 KB script that:
  - Harvests a wide range of credentials (see below).  
  - Encrypts the collected data with the attacker’s RSA public key.  
  - Exfiltrates the encrypted bundle to public GitHub repositories whose description contains **“Shai‑Hulud: Here We Go Again”**.  
  - Falls back to `https://npm-cache.com:443/router` if GitHub upload fails; the domain is retrieved from an Ethereum smart contract, allowing dynamic infrastructure changes.

## Credentials harvested
- **npm tokens** – from `~/.npmrc` and other rc files, validated against the registry.  
- **GitHub tokens** – PATs, OAuth, App tokens, JWT OIDC tokens from config files, env vars, and GitHub Actions runner memory.  
- **AWS credentials** – from `~/.aws/*`, env vars, EC2/ECS metadata services, and Secrets Manager.  
- **Kubernetes secrets** – service‑account token, CA, namespace, and `KUBECONFIG` files.  
- **HashiCorp Vault tokens** – from env vars, token files, container paths, and AWS IAM auth.  
- **Stripe and Slack tokens** – API keys and tokens found in the filesystem.  
- **Generic secret scan** – ~200 glob patterns targeting `.env*`, private keys, SSH configs, Terraform state, Docker credentials, KeePass files, VPN configs, IDE settings, etc.  
- Files larger than 5 MB are skipped; up to 64 concurrent reads are used.

## Exfiltration
- Encrypted credential bundles are pushed to one of many public GitHub repositories matching the “Shai‑Hulud” description.  
- If the push fails, data is sent to the fallback domain `npm-cache.com`, whose address is resolved from an on‑chain contract.

## Self‑replicating worm
- **npm tarball infection**: using stolen npm tokens, the payload lists all packages the token can publish, modifies each tarball by:
  - Incrementing the patch version.  
  - Adding the malicious `preinstall` script.  
  - Injecting `setup.mjs` and `math_init.js` (a variant of `Math_Symbol.js`).  
  - Republishing the altered tarball.  
- This mechanism generated the second‑generation infections observed (identified by `math_init.js`).

## Impact
- Over 400 additional packages infected through community spread.  
- Combined download volume exceeds 2 billion installs per month, giving the attacker access to a massive pool of credentials across diverse environments.  
- The attack demonstrates a fully automated supply‑chain worm capable of credential theft, encrypted exfiltration, and rapid propagation via npm publishing rights.