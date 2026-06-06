---
title: 'Cool down before you install: give new gems a few days to be vetted - RubyGems Blog'
url: https://blog.rubygems.org/2026/06/03/cooldown-let-new-gems-be-vetted.html
site_name: hnrss
content_file: hnrss-cool-down-before-you-install-give-new-gems-a-few-d
fetched_at: '2026-06-06T11:50:27.071741'
original_url: https://blog.rubygems.org/2026/06/03/cooldown-let-new-gems-be-vetted.html
date: '2026-06-03'
published_date: '2026-06-03T00:00:00+00:00'
description: 'Most supply-chain attacks against RubyGems exploit a narrow window: an account is compromised, a malicious version ships, and any bundle install in the minutes that follow resolves straight to it. ...'
tags:
- hackernews
- hnrss
---

# Cool down before you install: give new gems a few days to be vetted

Hiroshi SHIBATA

·

03 Jun 2026

Ruby core committer and RubyGems maintainer.

Most supply-chain attacks against RubyGems exploit a narrow window: an account is compromised, a malicious version ships, and anybundle installin the minutes that follow resolves straight to it.Bundler 4.0.13introducescooldown, a time-based filter that refuses to resolve to a version until it has been public for at leastNdays. Releases too new to have been scrutinized are passed over in favor of ones that have aged past the window.

The feature wasdesigned in the open, drawing onhow other ecosystems approach the same problem. It is opt-in, and complements rather than replaces existing defenses like mandatory 2FA and trusted publishing.

Cooldown reads the per-versioncreated_attimestamp that rubygems.org’s v2 compact index now serves. A version whose source does not exposecreated_at, such as older gem servers, historical entries from before the v2 cutover, or private registries still on the v1 format, is treated as outside the window and stays resolvable. Cooldown never blocks resolution silently; it only holds back versions it can prove are too new.

### Getting started

Cooldown ships inBundler 4.0.13. If you are on an earlier release, update Bundler in place and pin the same version in your lockfile so the whole team moves together:

$
 
gem update 
--system
 
# or: gem install bundler -v 4.0.13

$
 
bundle update 
--bundler
=
4.0.13

Then declare a small cooldown on your source in theGemfile. This is the right setup for most teams: it is committed alongside your code, so every developer and CI run enforce the same window with no extra setup.

source
 
"https://rubygems.org"
,
 
cooldown: 
7

gem
 
"rails"

gem
 
"puma"

Cooldown takes effect during resolution. Runbundle installwhen there is no lockfile yet, orbundle updateto re-resolve against it once a lockfile exists; an existingGemfile.lockis always honored as-is, so adding a cooldown never disturbs versions you have already locked. Cooldown is unset by default, so a project without it keeps resolving to the newest versions.

That is all most projects need. The rest of this post covers the finer-grained controls.

### Other ways to set it

Beyond the per-source keyword, thecooldownsetting applies one value across every source, scoped per-project, globally, or through the environment:

$
 
bundle config 
set 
cooldown 7 
# stored in .bundle/config for this project

$
 
bundle config 
set
 
--global
 cooldown 7 
# applies to every project for this user

$
 
BUNDLE_COOLDOWN
=
7 bundle 
install
 
# no lockfile yet, e.g. a fresh CI checkout

$
 
BUNDLE_COOLDOWN
=
7 bundle update 
# re-resolve when a lockfile already exists

For a one-off run, pass--cooldowntoinstall,update,add, oroutdated:

$
 
bundle 
install
 
--cooldown
 7

$
 
bundle update 
--cooldown
 7

$
 
bundle add rails 
--cooldown
 7

$
 
bundle outdated 
--cooldown
 7

When more than one of these is present, they resolve in a fixed order of precedence:command-line flag > configuration setting > per-sourcecooldown:in theGemfile. A--cooldownflag overrides thecooldownsetting (bundle configorBUNDLE_COOLDOWN), which in turn overrides acooldown:declared on a source. The cooldown value is always anon-negative integer number of days; a string, float, negative number, or array is rejected with anInvalidOptionerror.

### Mixing sources

Because the flag and the setting applyuniformly to every source, the per-source keyword is what you reach for when policy differs by registry, for instance cooling down public gems while trusting an internal registry you operate:

source
 
"https://rubygems.org"
,
 
cooldown: 
7

source
 
"https://gems.internal.example.com"
,
 
cooldown: 
0
 
do

 
gem
 
"internal-tool"

end

cooldown: 0on the private source keeps it permanently exempt while public gems still age. Note that a command-line--cooldown Noverrides every source for that run, including the exempt one.

### The escape hatch

Passing0disables cooldown for the run. It is the reliable way to reach the newest version on demand and to override a per-source or configured cooldown. This matters most when waiting is the wrong default: a fix lands for an actively exploited 0-day, or a vulnerability disclosure tells you to upgrade immediately. In those cases the freshest release is exactly the one you want, and--cooldown 0lets you take it without removing the policy for everyone else:

$
 
bundle 
install
 
--cooldown
 0

$
 
BUNDLE_COOLDOWN
=
0 bundle update rails 
# ignore any configured cooldown this time

You will reach for this when every candidate version of a gem is still inside the window. Rather than fall back to a too-new release, Bundler stops, reports how many versions the cooldown excluded, and points you at--cooldown 0to proceed.

### Seeing what is held back

bundle outdatedis cooldown-aware. It annotates versions that are newer but still inside the window with the days left before they become resolvable, so “up to date” stays distinct from “deliberately waiting”:

$
 
bundle outdated 
--cooldown
 7

Gem Current Latest Requested Groups
aws-partitions 1.1251.0 1.1256.0 (cooldown 3d) = 1.1251.0 default

### One layer among many

Cooldown is most useful as one part of the wider security investment happening on rubygems.org. The registry now validates gem contents at push time and checks logins against Have I Been Pwned so that compromised passwords cannot be reused, work described inProtecting rubygems.org from the outside in. A dedicated team is runningAI-assisted vulnerability scanning against the most critical gems, backed by Alpha Omega and Anthropic, and the direction of all of this is tracked on apublic roadmap. Trusted publishing and mandatory 2FA already raise the bar for who can push a release in the first place.

Cooldown itself only works because rubygems.org now publishes the per-versioncreated_attimestamp through itsv2 compact index(v2 is an internal format version, not a public API change), delivered through a careful dual-write migration and a flagged cutover with no disruption for clients. I’m grateful to the rubygems.org team for that groundwork. Cooldown is a thin client-side filter on top of it.

Each of these defenses covers a different gap, and they compound. Resolving your dependencies against rubygems.org is what puts all of them to work on your behalf, which makes it the safest default for Ruby projects.