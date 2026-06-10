---
title: Upcoming breaking changes for npm v12 - GitHub Changelog
url: https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/
site_name: hnrss
content_file: hnrss-upcoming-breaking-changes-for-npm-v12-github-chang
fetched_at: '2026-06-10T12:07:47.319660'
original_url: https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/
date: '2026-06-09'
description: Upcoming breaking changes for npm v12
tags:
- hackernews
- hnrss
---

Back to changelog

Our next npm major version, v12, introduces security-related default changes tonpm install. All these changes are available behind warnings in npm today on 11.16.0 or newer, so you can prepare before the upgrade. v12 is estimated to release in July 2026.

Each change turns annpm installbehavior that runs automatically today into one you explicitly opt into:

* allowScriptsdefaults to off:npm installwill no longer executepreinstall,install, orpostinstallscripts from dependencies unless they are explicitly allowed in your project. This includes nativenode-gypbuilds (i.e., a package with abinding.gypand no explicit install script still gets blocked, because npm runs an implicitnode-gyp rebuildfor it).preparescripts from git, file, and link dependencies are blocked the same way. To see what would be blocked, runnpm approve-scripts --allow-scripts-pending. Then allow the packages you trust withnpm approve-scriptsand block the rest withnpm deny-scripts. The resulting allowlist is written topackage.jsonand should be committed. If your install routine runs scripts, you can observe warnings in npm 11.16.0+.
* --allow-gitdefaults tonone:npm installwill no longer resolve Git dependencies (direct or transitive) unless explicitly allowed via--allow-git. This closes a code-execution path where a Git dependency’s.npmrccould override the Git executable, even with--ignore-scripts. This change waspreviously announced on 2026-02-18and is available in npm 11.10.0+.
* --allow-remotedefaults tonone:npm installwill no longer resolve dependencies from remote URLs, such as https tarballs (direct or transitive), unless explicitly allowed via--allow-remote. This flag is available in npm 11.15.0+. The related--allow-fileand--allow-directoryflags are not changing their defaults in v12.

### How to prepare

Upgrade to npm 11.16.0 or later, run your normal install, and review the warnings. Usenpm approve-scripts --allow-scripts-pendingto see which packages have scripts, approve the ones you trust, and commit the updatedpackage.json. After that, only the scripts you approved keep running once you upgrade. Anything you leave unapproved will stop. More details are available in our docs atnpm approve-scripts,npm deny-scripts, andallow-scriptsconfig(fornpxand global installs). Please share your comments and questions in ourcommunity discussion.

## Related Posts

### Jun.09Release

					Dependabot version updates now support the Deno ecosystem				

supply chain security

### May.26Release

					Dependabot version updates now support the sbt ecosystem				

supply chain security

### May.22Release

					Staged publishing and new install-time controls for npm				

supply chain security

### May.19Retired

					Upcoming deprecation of Python 3.9 for Dependabot				

supply chain security

### May.19Improvement

					Expanded OIDC support for Dependabot and code scanning				

application security

supply chain security

...

				+1			

### May.19Improvement

					Start a GitHub Advanced Security trial from a risk assessment				

application security

supply chain security

...

				+1			

### May.12Retired

					Synchronous SBOM API deprecated				

supply chain security

### May.11Improvement

					Cross-org Dependabot access for internal repositories				

supply chain security

### May.06Release

					Search and filter bar for repository security advisories				

supply chain security

 

## Subscribe to our developer newsletter

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

						Enter your email
*

						Subscribe					

By submitting, I agree to let GitHub and its affiliates use my information for personalized communications, targeted advertising, and campaign effectiveness. See theGitHub Privacy Statementfor more details.

				Back to top