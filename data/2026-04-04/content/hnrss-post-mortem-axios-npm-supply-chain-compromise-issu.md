---
title: 'Post Mortem: axios npm supply chain compromise · Issue #10636 · axios/axios · GitHub'
url: https://github.com/axios/axios/issues/10636
site_name: hnrss
content_file: hnrss-post-mortem-axios-npm-supply-chain-compromise-issu
fetched_at: '2026-04-04T11:11:53.003752'
original_url: https://github.com/axios/axios/issues/10636
date: '2026-04-03'
description: 'Post Mortem: axios npm supply chain compromise Date: March 31, 2026 Author: Jason Saayman Status: Remediation in progress On March 31, 2026, two malicious versions of axios (1.14.1 and 0.30.4) were published to the npm registry through m...'
tags:
- hackernews
- hnrss
---

axios

 

/

axios

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork11.6k
* Star109k

# Post Mortem: axios npm supply chain compromise#10636

Open
Open
Post Mortem: axios npm supply chain compromise
#10636
Assignees
 
Labels
type::security
The PR is a secuirty related changed normally from a CVE
The PR is a secuirty related changed normally from a CVE

## Description

jasonsaayman
opened 
on 
Apr 2, 2026
Issue body actions

# Post Mortem: axios npm supply chain compromise

Date:March 31, 2026Author:Jason SaaymanStatus:Remediation in progress

On March 31, 2026, two malicious versions of axios (1.14.1 and 0.30.4) were published to the npm registry through my compromised account. Both versions injected a dependency calledplain-crypto-js@4.2.1that installed a remote access trojan on macOS, Windows, and Linux.

The malicious versions were live for about 3 hours before being removed.

## Are you affected?

Check your lockfile:

grep -E 
"
axios@(1\.14\.1|0\.30\.4)|plain-crypto-js
"
 package-lock.json yarn.lock 
2>
/dev/null

If anything comes back, treat that machine as compromised:

1. Downgrade toaxios@1.14.0(or0.30.3for 0.x users)
2. Deletenode_modules/plain-crypto-js/
3. Rotate every secret, token, and credential on that machine
4. Check your network logs for connections tosfrclak[.]comor142.11.206.73on port 8000
5. If this happened on a CI runner, rotate any secrets that were injected during the affected build

If you were already pinned to a clean version and didn't run a fresh install between 00:21 and 03:15 UTC on March 31, you're fine.

For detailed remediation guidance, including CI/CD-specific steps, see:

* StepSecurity: full technical analysis and remediation
* Snyk: advisory and scanning guidance
* Socket: Supply Chain Attack on Axios Pulls Malicious Dependency from npm

## What happened

The attacker gained access to the lead maintainer's PC through a targeted social engineering campaign and RAT malware. This gave them access to the npm account credentials, which they used to publish the malicious versions.

The attack followed patterns documented in similar campaigns targeting open source maintainers.

## Resolution

Complete wipe of all lead maintainer devices as well as resetting of all credentials. This includes all accounts irrespective of platform, both personal and all other capacities.

## What's changing

To prevent this from happening again, these are the changes being made:

Action

Type

Reset of all devices and credentials

Prevention

Immutable release setup

Prevention

Proper adoption of OIDC flow for publishing

Prevention

Improvement of overall security posture

Prevention

Updating of all GitHub actions to adopt best practices

Prevention

This list is not the end. We will continue actively working on improving security beyond these items.

## Attack Timeline

I don't have an exact timeline for when the initial compromise occurred, but this is the sequence of events for the package itself:

* About 2 weeks before March 31: social engineering campaign initiated against the lead maintainer
* March 30, 05:57 UTC:plain-crypto-js@4.2.0published to npm
* March 31, 00:21 UTC:axios@1.14.1published withplain-crypto-js@4.2.1injected
* March 31, around 01:00 UTC:axios@0.30.4published with the same payload
* March 31, around 01:00 UTC: first external detections
* March 31, around 01:00 UTC: community members file issues reporting the compromise. The attacker deletes them using the compromised account.
* March 31, 01:38 UTC: axios collaborator DigitalBrainJS opens PRchore(ci): add deprecate action;#10591to deprecate the compromised versions, flags the deleted issues to the community, and contacts npm directly
* March 31, 03:15 UTC: malicious versions removed from npm
* March 31, 03:29 UTC:plain-crypto-jsremoved from npm

For detailed technical timelines:

* StepSecurity: forensic timeline
* Datadog Security Labs: full attack flow and response analysis

## Lessons learned

We are actively investigating how unauthorized access was obtained and reviewing all aspects of our security posture and access controls. While we do not have confirmed details to share at this time, this incident reinforces the need for continuous monitoring, strong account protections, and vigilance across both project infrastructure and individual maintainer environments.

We will continue to strengthen our practices in alignment with industry best practices and in collaboration with groups such as the OpenJS Security Working Group.

Security posture should be continuously monitored and improved. Specifically from this incident:

* Publishing directly from a personal account was a risk that could have been avoided. The OIDC flow and immutable release setup we are now adopting should have been in place before this happened.
* There was no automated way to detect an unauthorized publish. Detection depended entirely on the community noticing.
* Open source maintainers with high-impact packages are active targets for sophisticated social engineering. Hyper vigilance is needed both on the registry and in a personal capacity.

## Summary for broarder audience

We can confirm that two compromised versions of Axios were briefly made available through a widely used software download system due to unauthorized access to the lead maintainer's account, not a change to the underlying code.

We are working with the companies that operate this system, along with security experts, to investigate and contain the issue. Organizations that installed these versions should remove them immediately and treat affected systems as potentially compromised, including rotating any sensitive credentials.

This was the result of a compromised lead maintainer's account, and we are actively investigating how access was obtained. We do not have confirmed details to share at this time.

## Acknowledgments

Thanks to@DigitalBrainJSfor acting fast when the compromised account had higher permissions than his own and for getting npm to take action. Thanks to Open Source Community and the npm security team for their fast response.

The malicious versions have been removed from npm and are no longer infecting users. The immediate incident is resolved. We are actively working on the security improvements listed above to prevent this from happening again.

I'll update this as the investigation progresses. Questions welcome in this thread.

Reactions are currently unavailable

## Metadata

## Metadata