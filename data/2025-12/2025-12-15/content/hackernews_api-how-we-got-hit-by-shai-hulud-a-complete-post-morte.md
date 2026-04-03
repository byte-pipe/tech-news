---
title: 'How we got hit by Shai-Hulud: A complete post-mortem | Trigger.dev'
url: https://trigger.dev/blog/shai-hulud-postmortem
site_name: hackernews_api
fetched_at: '2025-12-15T11:07:43.829064'
original_url: https://trigger.dev/blog/shai-hulud-postmortem
author: nkko
date: '2025-12-14'
description: On November 25th, one of our engineers was compromised by the Shai-Hulud npm supply chain worm. Here's what happened, how we responded, and what we've changed.
tags:
- hackernews
- trending
---

On November 25th, 2025, we were on a routine Slack huddle debugging a production issue when we noticed something strange: a PR in one of our internal repos was suddenly closed, showed zero changes, and had a single commit from... Linus Torvalds?

The commit message was just "init."

Within seconds, our #git Slack channel exploded with notifications. Dozens of force-pushes. PRs closing across multiple repositories. All attributed to one of our engineers.

We had been compromised byShai-Hulud 2.0, a sophisticated npm supply chain worm that compromised over 500 packages, affected 25,000+ repositories, and spread across the JavaScript ecosystem. We weren't alone:PostHog, Zapier, AsyncAPI, Postman, and ENS were among those hit.

This is the complete story of what happened, how we responded, and what we've changed to prevent this from happening again.

No Trigger.dev packages were ever compromised. The@trigger.dev/*packages andtrigger.devCLI were never infected with Shai-Hulud malware. This incident involved one of our engineers installing a compromised package on their development machine, which led to credential theft and unauthorized access to our GitHub organization. Our published packages remained safe throughout.

## The Attack Timeline

Time (UTC)
Event
Nov 24, 04:11
Malicious packages go live
Nov 24, ~20:27
Engineer compromised
Nov 24, 22:36
First attacker activity
Nov 25, 02:56-05:32
Overnight reconnaissance
Nov 25, 09:08-15:08
Legitimate engineer work (from Germany)
Nov 25, 09:10-09:17
Attacker monitors engineer activity
Nov 25, 15:17-15:27
Final recon
Nov 25, 15:27-15:37
Destructive attack
Nov 25, ~15:32
Detection
Nov 25, ~15:36
Access revoked
Nov 25, 16:35
AWS session blocked
Nov 25, 22:35
All branches restored
Nov 26, 20:16
GitHub App key rotated

## The compromise

On the evening of November 24th, around 20:27 UTC (9:27 PM local time in Germany), one of our engineers was experimenting with a new project. They ran a command that triggeredpnpm install. At that moment, somewhere in the dependency tree, a malicious package executed.

We don't know exactly which package delivered the payload. The engineer was experimenting at the time and may have deleted the project directory as part of cleanup. By the time we investigated, we couldn't trace back to the specific package. The engineer checked their shell history and they'd only run install commands in our main trigger repo, cloud repo, and one experimental project.

This is one of the frustrating realities of these attacks: once the malware runs, identifying the source becomes extremely difficult. The package doesn't announce itself. Thepnpm installcompletes successfully. Everything looks normal.

What we do know is that the Shai-Hulud malware ran apreinstallscript that:

1. Downloaded and executedTruffleHog, a legitimate security tool repurposed for credential theft
2. Scanned the engineer's machine for secrets: GitHub tokens, AWS credentials, npm tokens, environment variables
3. Exfiltrated everything it found

When the engineer later recovered files from their compromised laptop (booted in recovery mode), they found the telltale signs:

The.trufflehog-cachedirectory andtrufflehog_3.91.1_darwin_amd64.tar.gzfile found on the compromised machine. Theextractdirectory was empty, likely cleaned up by the malware to cover its tracks.

## 17 hours of reconnaissance

The attacker had access to our engineer's GitHub account for 17 hours before doing anything visible. According to our GitHub audit logs, they operated methodically.

Just over two hours after the initial compromise, the attacker validated their stolen credentials and began mass cloning:

Time (UTC)
Location
Activity
22:36:50
US
First attacker access, mass cloning begins
22:36-22:39
US
73 repositories cloned
22:48-22:50
US
~70 more repositories cloned (second wave)
22:55-22:56
US
~90 repositories cloned (third wave)
22:59-23:04
US
~70 repositories cloned (fourth wave)
23:32:59
India
Attacker switches to India-based infrastructure
23:32-23:37
India
73 repositories cloned
23:34-23:35
US + India
Simultaneous cloning from both locations

The simultaneous activity from US and India confirmed we were dealing with a single attacker using multiple VPNs or servers, not separate actors.

While our engineer slept in Germany, the attacker continued their reconnaissance. More cloning at 02:56-02:59 UTC (middle of the night in Germany), sporadic activity until 05:32 UTC. Total repos cloned: 669 (527 from US infrastructure, 142 from India).

Here's where it gets unsettling. Our engineer woke up and started their normal workday:

Time (UTC)
Actor
Activity
09:08:27
Engineer
Triggers workflow on cloud repo (from Germany)
09:10-09:17
Attacker
Git fetches from US, watching the engineer
09:08-15:08
Engineer
Normal PR reviews, CI workflows (from Germany)

The attacker was monitoring our engineer's activity while they worked, unaware they were compromised.

During this period, the attacker created repositories with random string names to store stolen credentials, a known Shai-Hulud pattern:

* github.com/[username]/xfjqb74uysxcni5ztn
* github.com/[username]/ls4uzkvwnt0qckjq27
* github.com/[username]/uxa7vo9og0rzts362c

They also created three repos marked with "Sha1-Hulud: The Second Coming" as a calling card. These repositories were empty by the time we examined them, but based on the documented Shai-Hulud behavior, they likely contained triple base64-encoded credentials.

## 10 minutes of destruction

At 15:27 UTC on November 25th, the attacker switched from reconnaissance to destruction.

The attack began on ourcloudrepo from India-based infrastructure:

Time (UTC)
Event
Repo
Details
15:27:35
First force-push
triggerdotdev/cloud
Attack begins
15:27:37
PR closed
triggerdotdev/cloud
PR #300 closed
15:27:44
BLOCKED
triggerdotdev/cloud
Branch protection rejected force-push
15:27:50
PR closed
triggerdotdev/trigger.dev
PR #2707 closed

The attack continued on our main repository:

Time (UTC)
Event
Details
15:28:13
PR closed
triggerdotdev/trigger.dev PR #2706 (release PR)
15:30:51
PR closed
triggerdotdev/trigger.dev PR #2451
15:31:10
PR closed
triggerdotdev/trigger.dev PR #2382
15:31:16
BLOCKED
Branch protection rejected force-push to trigger.dev
15:31:31
PR closed
triggerdotdev/trigger.dev PR #2482

At 15:32:43-46 UTC, 12 PRs on jsonhero-web were closed in 3 seconds. Clearly automated. PRs #47, #169, #176, #181, #189, #190, #194, #197, #204, #206, #208 all closed within a 3-second window.

Our critical infrastructure repository was targeted next:

Time (UTC)
Event
Details
15:35:41
PR closed
triggerdotdev/infra PR #233
15:35:45
BLOCKED
Branch protection rejected force-push (India)
15:35:48
PR closed
triggerdotdev/infra PR #309
15:35:49
BLOCKED
Branch protection rejected force-push (India)

The final PR was closed on json-infer-types at 15:37:13 UTC.

## Detection and response

We got a lucky break. One of our team members was monitoring Slack when the flood of notifications started:

Our #git Slack channel during the attack. A wall of force-pushes, all with commit message "init."

Every malicious commit was authored as:

Author: Linus Torvalds <
[email protected]
>
Message: init

An attacked branch: a single "init" commit attributed to Linus Torvalds, thousands of commits behind main.

We haven't found reports of other Shai-Hulud victims seeing this same "Linus Torvalds" vandalism pattern. The worm's documented behavior focuses on credential exfiltration and npm package propagation, not repository destruction. This destructive phase may have been unique to our attacker, or perhaps a manual follow-up action after the automated worm had done its credential harvesting.

Within 4 minutes of detection we identified the compromised account, removed them from the GitHub organization, and the attack stopped immediately.

Our internal Slack during those first minutes:

"Urmmm guys? what's going on?"

"add me to the call @here"

"Nick could you double check Infisical for any machine identities"

"can someone also check whether there are any reports of compromised packages in our CLI deps?"

Within the hour:

Time (UTC)
Action
~15:36
Removed from GitHub organization
~15:40
Removed from Infisical (secrets manager)
~15:45
Removed from AWS IAM Identity Center
~16:00
Removed from Vercel and Cloudflare
16:35
AWS SSO sessions blocked via deny policy (sessions can't be revoked)
16:45
IAM user console login deleted

## The damage

Repository clone actions: 669 (public and private), including infrastructure code, internal documentation, and engineering plans.

Branches force-pushed: 199 across 16 repositories

Pull requests closed: 42

Protected branch rejections: 4. Some of our repositories have main branch protection enabled, but we had not enabled it for all repositories at the time of the incident.

npm packages werenotcompromised. This is the difference between "our repos got vandalized" and "our packages got compromised."

Our engineer didn't have an npm publishing token on their machine, and even if they did we had already required 2FA for publishing to npm. Without that, Shai-Hulud would have published malicious versions of@trigger.dev/sdk,@trigger.dev/core, and others, potentially affecting thousands of downstream users.

Production databases or any AWS resources werenotaccessed. Our AWS CloudTrail audit showed only read operations from the compromised account:

Event Type
Count
Service
ListManagedNotificationEvents
~40
notifications
DescribeClusters
8
ECS
DescribeTasks
4
ECS
DescribeMetricFilters
6
CloudWatch

These were confirmed to be legitimate operations by our engineer.

One nice surprise: AWS actually sent us a proactive alert about Shai-Hulud. They detected the malware's characteristic behavior (ListSecrets, GetSecretValue, BatchGetSecretValue API calls) on an old test account that hadn't been used in months, so we just deleted it. But kudos to AWS for the proactive detection and notification.

## The recovery

GitHub doesn't have server-side reflog. When someone force-pushes, that history is gone from GitHub's servers.

But we found ways to recover.

Push events are retained for 90 days via the GitHub Events API. We wrote a script that fetched pre-attack commit SHAs:

# Find pre-attack commit SHA from events
gh api repos/$REPO/events --paginate | \
 jq -r '.[] | select(.type=="PushEvent") |
 select(.payload.ref=="refs/heads/'$BRANCH'") |
 .payload.before' | head -1

Public repository forks still contained original commits. We used these to verify and restore branches.

Developers who hadn't rungit fetch --prune(all of us?) still had old SHAs in their local reflog.

Within 7 hours, all 199 branches were restored.

## GitHub app private key exposure

During the investigation, our engineer was going through files recovered from the compromised laptop and discovered something concerning: the private key for our GitHub App was in the trash folder.

When you create a private key in the GitHub App settings, GitHub automatically downloads it. The engineer had created a key at some point, and while the active file had been deleted, it was still in the trash, potentially accessible to TruffleHog.

Our GitHub App has the following permissions on customer repositories:

Permission
Access Level
Risk
contents
read/write
Could read/write repository contents
pull_requests
read/write
Could read/create/modify PRs
deployments
read/write
Could create/trigger deployments
checks
read/write
Could create/modify check runs
commit_statuses
read/write
Could mark commits as passing/failing
metadata
read
Could read repository metadata

To generate valid access tokens, an attacker would need both the private key (potentially compromised) and the installation ID for a specific customer (stored in our database which was not compromised, not on the compromised machine).

We immediately rotated the key:

Time (UTC)
Action
Nov 26, 18:51
Private key discovered in trash folder
Nov 26, 19:54
New key deployed to test environment
Nov 26, 20:16
New key deployed to production

We found no evidence of unauthorized access to any customer repositories. The attacker would have needed installation IDs from our database to generate tokens, and our database was not compromised as previously mentioned.

However, we cannot completely rule out the possibility. An attacker with the private key could theoretically have called the GitHub API to enumerate all installations. We've contacted GitHub Support to request additional access logs. We've also analyzed the webhook payloads to our GitHub app, looking for suspicious push or PR activity from connected installations & repositories. We haven't found any evidence of unauthorized activity in these webhook payloads.

We've sent out an email to potentially effected customers to notify them of the incident with detailed instructions on how to check if they were affected. Please check your email for more details if you've used our GitHub app.

## Technical deep-dive: how Shai-Hulud works

For those interested in the technical details, here's what we learned about the malware fromSocket's analysisand our own investigation.

When npm runs thepreinstallscript, it executessetup_bun.js:

1. Detects OS/architecture
2. Downloads or locates theBunruntime
3. Caches Bun in~/.cache
4. Spawns a detached Bun process runningbun_environment.jswith output suppressed
5. Returns immediately sonpm installcompletes successfully with no warnings

The malware runs in the background while you think everything is fine.

The payload uses TruffleHog to scan$HOMEfor GitHub tokens (from env vars, gh CLI config, git credential helpers), AWS/GCP/Azure credentials, npm tokens from.npmrc, environment variables containing anything that looks like a secret, and GitHub Actions secrets (if running in CI).

Stolen credentials are uploaded to a newly-created GitHub repo with a random name. The data is triple base64-encoded to evade GitHub's secret scanning.

Files created:

* contents.json(system info and GitHub credentials)
* environment.json(all environment variables)
* cloud.json(cloud provider credentials)
* truffleSecrets.json(filesystem secrets from TruffleHog)
* actionsSecrets.json(GitHub Actions secrets if any)

If an npm publishing token is found, the malware validates the token against the npm registry, fetches packages maintained by that account, downloads each package, patches it with the malware, bumps the version, and re-publishes, infecting more packages.

This is how the worm spread through the npm ecosystem, starting fromPostHog's compromised CIon November 24th at 4:11 AM UTC. Our engineer was infected roughly 16 hours after the malicious packages went live.

If no credentials are found to exfiltrate or propagate, the malware attempts to delete the victim's entire home directory. Scorched earth.

File artifacts to look for:setup_bun.js,bun_environment.js,cloud.json,contents.json,environment.json,truffleSecrets.json,actionsSecrets.json,.trufflehog-cache/directory.

Malware file hashes (SHA1):

* bun_environment.js:d60ec97eea19fffb4809bc35b91033b52490ca11
* bun_environment.js:3d7570d14d34b0ba137d502f042b27b0f37a59fa
* setup_bun.js:d1829b4708126dcc7bea7437c04d1f10eacd4a16

We've published adetection scriptthat checks for Shai-Hulud indicators.

## What we've changed

We disabled npm scripts globally:

npm config set ignore-scripts true --location=global

This preventspreinstall,postinstall, and other lifecycle scripts from running. It's aggressive and some packages will break, but it's the only reliable protection against this class of attack.

We upgraded to pnpm 10. This was significant effort (had to migrate through pnpm 9 first), but pnpm 10 brings critical security improvements. Scripts are ignored by default. You can explicitly whitelist packages that need to run scripts viapnpm.onlyBuiltDependencies. And theminimumReleaseAgesetting prevents installing packages published recently.

# pnpm-workspace.yaml
minimumReleaseAge: 4320 # 3 days in minutes
preferOffline: true

To whitelist packages that legitimately need build scripts:

pnpm approve-builds

This prompts you to select which packages to allow (likeesbuild,prisma,sharp).

For your global pnpm config:

pnpm config set minimumReleaseAge 4320
pnpm config set --json minimumReleaseAgeExclude '["@trigger.dev/*", "trigger.dev"]'

We switched npm publishing to OIDC. No more long-lived npm tokens anywhere. Publishing now usesnpm's trusted publisherswith GitHub Actions OIDC. Even if an attacker compromises a developer machine, they can't publish packages because there are no credentials to steal. Publishing only happens through CI with short-lived, scoped tokens.

We enabled branch protection on all repositories. Not just critical repos or just OSS repos. Every repository with meaningful code now has branch protection enabled.

We've adoptedGrantedfor AWS SSO. Granted encrypts SSO session tokens on the client side, unlike the AWS CLI which stores them in plaintext.

Based onPostHog's analysisof how they were initially compromised (viapull_request_target), we've reviewed our GitHub Actions workflows. We now require approval for external contributor workflow runs on all our repositories (previous policy was only for public repositories).

## Lessons for other teams

The ability for packages to run arbitrary code during installation is the attack surface. Until npm fundamentally changes, add this to your~/.npmrc:

ignore-scripts=true

Yes, some things will break. Whitelist them explicitly. The inconvenience is worth it.

pnpm 10 ignores scripts by default and lets you set a minimum age for packages:

pnpm config set minimumReleaseAge 4320 # 3 days

Newly published packages can't be installed for 3 days, giving time for malicious packages to be detected.

Branch protection takes 30 seconds to enable. It prevents attackers from pushing to a main branch, potentially executing malicious GitHub action workflows.

Long-lived npm tokens on developer machines are a liability. Usetrusted publisherswith OIDC instead.

If you don't need a credential on your local machine, don't have it there. Publishing should happen through CI only.

Our #git Slack channel is noisy. That noise saved us.

## A note on the human side

One of the hardest parts of this incident was that it happened to a person.

"Sorry for all the trouble guys, terrible experience"

Our compromised engineer felt terrible, even though they did absolutely nothing wrong. It could have happened to any team member.

Runningnpm installis not negligence. Installing dependencies is not a security failure. The security failure is in an ecosystem that allows packages to run arbitrary code silently.

They also discovered that the attacker had made their GitHub account star hundreds of random repositories during the compromise. Someone even emailed us: "hey you starred my repo but I think it was because you were hacked, maybe remove the star?"

## Summary

Metric
Value
Time from compromise to first attacker activity
~2 hours
Time attacker had access before destructive action
~17 hours
Duration of destructive attack
~10 minutes (15:27-15:37 UTC)
Time from first malicious push to detection
~5 minutes
Time from detection to access revocation
~4 minutes
Time to full branch recovery
~7 hours
Repository clone actions by attacker
669
Repositories force-pushed
16
Branches affected
199
Pull requests closed
42
Protected branch rejections
4

## Resources

About the Attack:

* Socket.dev: Shai-Hulud Strikes Again V2- Technical deep-dive into the malware
* PostHog Post-Mortem- Another company's experience with Shai-Hulud
* Wiz Blog: Shai-Hulud 2.0 Supply Chain Attack
* The Hacker News Coverage
* Endor Labs Analysis
* HelixGuard Advisory(referenced in AWS alert)

Mitigation Resources:

* npm Trusted Publishers- OIDC-based publishing
* pnpm onlyBuiltDependencies- Whitelist packages allowed to run scripts
* pnpm minimumReleaseAge- Delay installation of new packages
* Granted- AWS SSO credential management

Have questions about this incident? Reach out onTwitter/XorDiscord.

* On this page
* The Attack Timeline
* The compromise
* 17 hours of reconnaissance
* 10 minutes of destruction
* Detection and response
* The damage
* The recovery
* GitHub app private key exposure
* Technical deep-dive: how Shai-Hulud works
* What we've changed
* Lessons for other teams
* A note on the human side
* Summary
* Resources

Share this article

### How GovSignals is solving government procurement using Trigger.dev

Customer story

•

December 11

### Accelerating global logistics workflows using AI copilots

Customer story

•

November 13

### How we built a kanban-style triage agent for managing coding agents

Customer story

•

October 7

### Our roadmap for the next 3 months and beyond

Article

•

September 4

### Powering HeroUI Chat's complex deployment pipeline with Trigger.dev

Customer story

•

August 29

### Official MCP server & agent rules

Launch week

•

August 22

### Ready to start building?

Build and deploy your first task in 3 minutes.

Get started now
