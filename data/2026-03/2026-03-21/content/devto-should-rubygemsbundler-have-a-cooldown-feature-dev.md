---
title: Should RubyGems/Bundler Have a Cooldown Feature? - DEV Community
url: https://dev.to/hsbt/should-rubygemsbundler-have-a-cooldown-feature-40cp
site_name: devto
content_file: devto-should-rubygemsbundler-have-a-cooldown-feature-dev
fetched_at: '2026-03-21T11:08:58.107180'
original_url: https://dev.to/hsbt/should-rubygemsbundler-have-a-cooldown-feature-40cp
author: SHIBATA Hiroshi
date: '2026-03-19'
description: I'm Hiroshi Shibata (hsbt), a Ruby committer and the maintainer of RubyGems and Bundler. ... Tagged with ruby, security, supplychainsecurity, packaging.
tags: '#ruby, #security, #supplychainsecurity, #packaging'
---

I'm Hiroshi Shibata (hsbt), a Ruby committer and the maintainer of RubyGems and Bundler.

## TL;DR

Every major package manager is adding "cooldown" — a waiting period before you can install newly released packages. RubyGems/Bundler doesn't have one yet. I've been discussing whether we should add it. Short answer: yes, as an opt-in option, but cooldown alone isn't enough.

## What Is a Cooldown?

A cooldown prevents upgrading to a new package version until a certain time has passed since its release. The idea is simple: if a malicious package is published, the waiting period gives security researchers time to catch it before it reaches yourGemfile.lock.

William Woodruff's analysisfound that 8 out of 10 supply chain attacks he examined had an exploitation window of less than one week. A 7-day cooldown could have prevented most of them.

As Andrew Nesbitt summarizes in "Package Managers Need to Cool Down", from late 2025 into 2026, cooldown adoption has accelerated rapidly.

## The Landscape

Cooldown started in dependency update tools, then spread to package managers themselves. One complication: every tool picked a different config name —minimumReleaseAge,min-release-age,npmMinimalAgeGate,exclude-newer,uploaded-prior-to, and so on. At least 10 different names exist. Polyglot developers, beware.

### Dependency Update Tools

Dependabot added acooldownblock in July 2025. You can set different waiting periods per semver level, and security updates bypass the cooldown:

# .github/dependabot.yml

version
:

2

updates
:


-

package-ecosystem
:

"
bundler"


directory
:

"
/"


schedule
:


interval
:

"
weekly"


cooldown
:


default-days
:

3


semver-major-days
:

7

Enter fullscreen mode

Exit fullscreen mode

Renovate hasminimumReleaseAge(formerlystabilityDays), with per-package and per-update-type granularity:

{


"minimumReleaseAge"
:

"3 days"
,


"packageRules"
:

[


{


"matchUpdateTypes"
:

[
"major"
],


"minimumReleaseAge"
:

"7 days"


}


]

}

Enter fullscreen mode

Exit fullscreen mode

### Package Managers

pnpm was first, shippingminimumReleaseAgein v10.16 (September 2025):

# pnpm-workspace.yaml

minimumReleaseAge
:

1440

# 24 hours

minimumReleaseAgeExclude
:


-

'
@myorg/*'

Enter fullscreen mode

Exit fullscreen mode

npm followed withmin-release-agein CLI 11.x (February 2026). Bun addedminimumReleaseAgein October 2025, Deno added--minimum-dependency-age. All major JavaScript runtimes now support cooldowns.

On the Python side, uv extended its--exclude-newerflag (originally for reproducible builds) to accept relative durations like"7 days". pip introduced--uploaded-prior-toin 26.0 (January 2026), though pip only takes absolute timestamps.

## Where Does Ruby Stand?

RubyGems and Bundler have no cooldown feature. A community member opened aDiscussion on ruby/rubygemsrequesting one, and I discussed it with Ruby community members and the RubyGems team.

What follows is my take on the discussion. I'm the RubyGems/Bundler maintainer, so keep that bias in mind.

### The "guinea pig" problem

My first concern. Cooldowns implicitly assume thatsomeone elsewill install the new version first and find problems. But if everyone enables cooldowns, nobody tries new releases during the waiting period — and the mechanism becomes useless. Better than nothing, probably. But it's a structural limitation of how OSS works.

### Delayed security fixes

A strict cooldown also delays urgent security patches. Distinguishing a malicious release from a legitimate security fix automatically is extremely difficult. Cooldowns could actuallyincreaserisk in some cases.

### The illusion of safety

Software that hasn't been updated in 10 years may contain undiscovered vulnerabilities. Consider a gem that's been on RubyGems for years without updates — age tells you nothing about whether it's been audited. Time passing doesn't guarantee security. Cooldowns provide a sense of security, but a sense of security isn't the same as actual security.

### Buying time for security researchers

On the other hand — and this is the strongest argument for cooldowns — they buy time for people who are actually scanning packages.

A concrete example:Maciej Mensfeld, a member of the RubyGems security team and developer of Diffend (a supply chain security platform for Ruby). He has detected and reported over 20,000 malicious packages across ecosystems.

In the RubyGems ecosystem specifically, he found over 700 typosquatting gems in 2020 (e.g.,railtargetingrails), and in 2022, more than 400 malicious packages were removed. His RubyKaigi 2023 talk "RubyGems on the watch" covers these efforts.

Today, the security team including Maciej reviews gems after release on rubygems.org. Gems found to contain malicious code are removed. A cooldown isn't just about waiting — it becomes effective when combined with this kind of scanning infrastructure.

## What We're Considering

My current thinking: offer cooldown as an opt-in option in the short term, pursue more technically effective measures longer term.

### Bundler Cooldown Option

Enterprise environments want this. Dependabot and Renovate already have equivalent features, so it makes sense to support it at the Bundler level too.

What the spec might look like:

* bundle update --cooldown 3(CLI option)
* bundle config set cooldown 3(global config)
* Block syntax in the Gemfile for per-gem cooldowns
* gem installsupport for CI/CD environments like GitHub Actions

Opt-in, disabled by default. Users choose based on their own needs.

### Scanning and Metadata on RubyGems.org

To make cooldowns actually useful, "has this gem been scanned?" matters as much as "has enough time passed?" On the rubygems.org side, we're considering:

* Automated scanning of new releases, with scan status published as index metadata
* Delays for high-risk releases (recent ownership changes, Trusted Publishing disabled)
* Letting RubyGems/Bundler reference this metadata to adjust behavior

There's also been a suggestion for a "scanned" badge on rubygems.org — worth exploring.

### Beyond Cooldown

Separately, there's discussion about sandboxing code execution duringgem install:ruby/rubygems#9138.

RubyGems and Bundler recently landed a change that separates the download and install phases:ruby/rubygems#9381. This was for performance, but the separation opens the door to running SAST or other verification after download and before install — potentially more effective than cooldown alone.

## Conclusion

Cooldown is not a silver bullet. But combined with server-side scanning and metadata on rubygems.org, it can be a meaningful layer of defense. We plan to offer it as an opt-in option in RubyGems/Bundler.

If you have thoughts, join theGitHub Discussion.

## Notes

* Written in March 2026. The ecosystem is evolving quickly — specifics may change.
* I'm a Ruby committer and the maintainer of RubyGems/Bundler. My perspective is shaped by that role.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
