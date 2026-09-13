---
title: 'Homebrew: 7.0.0'
url: https://brew.sh/2026/09/13/homebrew-7.0.0/
site_name: hnrss
content_file: hnrss-homebrew-700
fetched_at: '2026-09-13T14:50:17.213250'
original_url: https://brew.sh/2026/09/13/homebrew-7.0.0/
author: MikeMcQuaid
date: '2026-09-13'
published_date: '2026-09-13T00:00:00+00:00'
description: Today, I’m proud to announce Homebrew 7.0.0. The most significant changes since 6.0.0 are faster installations and upgrades, stronger sandboxing, a native macOS app, built-in vulnerability checks and an advisory database, the end of macOS 10.15 support and Intel Macs moving to Tier 3.
tags:
- hackernews
- hnrss
---

## 7.0.0

### 13 September 2026

### MikeMcQuaid

Today, I’m proud to announce Homebrew 7.0.0.
The most significant changes since 6.0.0 are faster installations and upgrades, stronger sandboxing, a native macOS app, built-in vulnerability checks and an advisory database, the end of macOS 10.15 support and Intel Macs moving to Tier 3.

Contents

* ⬆️ Upgrading
* 🍺 All Homebrew users🏎️ Performance🔒 SecuritySecurity advisoriesInstallation and tap protection🔎 Commands and configuration🗃️ Casks
* 🏎️ Performance
* 🔒 SecuritySecurity advisoriesInstallation and tap protection
* Security advisories
* Installation and tap protection
* 🔎 Commands and configuration
* 🗃️ Casks
* 🍎 macOS users🖥️ Homebrew app
* 🖥️ Homebrew app
* 🐧 Linux users
* 🍾 Non-default prefix users
* 🔍 Security teams and auditors
* 🐳 Homebrew users in CI
* 🛠️ Tap maintainers🪜 Install steps
* 🪜 Install steps
* 🙏 Finally

### ⬆️ Upgrading

An auto-update or manualbrew update(if you have$HOMEBREW_NO_AUTO_UPDATEset) will upgrade Homebrew for you.

Nowmeans 7.0.0. Deprecated interfaces warn until disablement; disabled interfaces reject use and removed interfaces are unavailable.

Environment

7.0.0 behaviour and action

Timing

PR links

macOS 10.15 or earlier

Upgrade to macOS 11 or later

Now

Minimum version

macOS Sonoma 14

Tier 3; upgrade to Sequoia 15+ for bottles and 
.pkg
 installations

Now

Support window

macOS Golden Gate 27 on Apple Silicon

Fully supported (Tier 1), with prebuilt bottles

Now

Full support

ghcr.io/homebrew/ubuntu22.04

Image removed; migrate to 
ghcr.io/homebrew/brew

Now

Notice
, 
removal

Homebrew/actions/*@master
 or 
@main

master
 removed; pin a 
CalVer release
 or full SHA

Now

Branch migration
, 
releases

Setuid wrappers with different real and effective UIDs

Rejected; run as the installation’s owner without a wrapper

Now

Execution model

Third-party 
brew
 wrappers

Tier 3; internal commands bypass wrappers; seek support from the wrapper project

Now

Wrapper changes

Homebrew/brew 
master

Frozen bootstrap; switch to 
main
 before removal

2027-03-01

Bootstrap

Intel macOS 11 or later

Tier 3; no new bottles; migrate to 
MacPorts
 before Homebrew stops running

2027-09-01

Support
, 
bottles

Apple Silicon macOS 11

Upgrade to macOS 12 or later before support ends

2027-09-01

Support schedule

Third-party formula 
post_install
 and cask flight blocks

Deprecated; migrate to 
*_steps
; 
brew style --fix
 converts common hooks

2027-12-11

Deprecation
, 
migration

### 🍺 All Homebrew users

The following improvements apply across platforms unless stated otherwise.

#### 🏎️ Performance

Greater concurrency across downloads, preparation and installation maximises performance while coordinating failures and summaries.

* brew install,brew reinstallandbrew upgradeoverlap package preparation and downloads, includingbrew bundlebatches, reducing waits between packages and allowing aBrewfileto benefit from the same shared installation work as a command naming several packages.
* brew configgathers independent system details concurrently, so compiler, operating-system and repository checks overlap instead of making diagnostic reports wait for every subprocess in turn.
* brew tap-info --installed --json=v1collects tap metadata concurrently, shortening inventory requests when several repositories need Git or network checks while preserving the output order expected by scripts.
* brew cleanupavoids repeated cache scans, speeding up cleanup for installations with many packages.
* brew fetchreads download information directly from API metadata forbottlesandcasks, starting downloads without loading complete package definitions merely to discover URLs and checksums.
* brew updateprepares Ruby caches so subsequent commands start faster.
* Homebrew reuses parsed API data on warm runs while verifying signatures on every load, reducing preparation time for repeated package commands without dropping authenticity checks.
* Homebrewlaunches fewer subprocesses during startup, reducing command overhead, andreads terminal dimensions directly, avoiding hangs with uutilsstty.

#### 🔒 Security

Homebrew 7.0.0 includes various security fixes and new installation protections.

##### Security advisories

The first fixed releases are listed below.

* GHSA-rg9r-ppxp-87hm, High, fixed in 6.0.12:unsigned cask-removal metadata could execute commands withsudo;all vulnerable recovery code and API accessors have been deleted.
* GHSA-5263-whxq-77hp, Moderate, fixed in 7.0.0:a malicious cask could execute code outside the macOS install sandbox through LaunchServices; Homebrew restrictsapplication launching,Mach servicesandUnix socket connections.
* GHSA-hqpg-hjr9-c7j8, Moderate, fixed in 6.0.12:the macOS installerignores prefix-owned Git configurationthat could execute programs as root.
* GHSA-x82f-cj53-gqfr, Low, fixed in 6.0.7:brew livecheckrestricts redirectsto prevent server-side request forgery.
* GHSA-3m5g-jfx7-3p65, Low, fixed in 6.0.7:download redirects cannot forward secret headers to other hosts.
* GHSA-r9gp-p4vv-f93x, Low, fixed in 6.0.6:Git redirects cannot bypass tap restrictions.
* GHSA-9g4r-vmj2-j2gj, Low, fixed in 6.0.7:Subversion external URLs cannot become command options.
* GHSA-r7qx-325v-4ccx, Low, fixed in 6.0.6:patch targets cannot escape the staged source tree.

##### Installation and tap protection

Tap trustremains the primary protection against malicious third-party casks; sandboxing mainly limits accidental damage and adds installation safeguards. It cannot make untrusted software safe to run: applications execute with the user’s privileges, andvendor.pkginstallers run outside the sandboxand may requiresudo. We balance tighter restrictions with keeping existing software working.

* Homebrew delivers structured setup as signed data and sandboxesformulaandcask operations, reducing arbitrary Ruby execution and repeated package loading.
* Homebrew begins migrating dependency downloads into afetchphase: migrated formulae download with network access and writable caches, theninstalldisables networking and makes those caches read-only; migration remains ongoing.
* Homebrew blocks sandboxed reads of the home directory by default, keeping unrelated personal files outside package builds while allowing required Homebrew paths;private temporary directories let build tools communicate locally without enabling network access.
* Homebrewrejects mismatched real and effective user IDsbefore reading configuration, removing untested privilege-switching code for unsupported shared installations.

Trust and environment migrations and replacements.

#### 🔎 Commands and configuration

Commands provide clearer previews, package information and service configuration.

* brew install --dry-runpreviews formulae and casks together.
* brew list --no-installed-on-requestidentifies formulae installed as dependencies.
* brew infodistinguishes uninstallable packages with⊘from uninstalled packages with✘andmarks unmet operating-system and architecture requirements, making it easier to understand whether a package can run on the current machine before starting an installation.
* brew servicesreads persistent overrides from$HOMEBREW_USER_CONFIG_HOME/services/<formula>.env, allowing local service settings to survive package upgrades and take effect on restart without editing generated service files. New and restarted services usesh.brew.<formula>onmacOSandLinux, recognising legacy registrations until restart.
* brew bundlerestores language tools from declared sources:Cargo Git repositories or pathsandsource:for remoteuvtools.
* brew doctor --jsonprovides structured diagnostics for automation;brew doctoralsowarns when anotherbrewshadows the current installation inPATH, helping diagnose wrapper and installation conflicts.
* brew deps --brewfileinspects a Brewfile’s dependencies, making it easier to review the packages a development environment will bring in before installing that environment.
* brew untapoffers to uninstall a tap’s packages first, allowing an unwanted package source and its installed software to be removed together.
* HOMEBREW_AUTO_UPDATE_QUIETsuppresses automatic-update package details, keeping routine command output focused while still allowing Homebrew to update in the background of normal use.
* Homebrew stops exporting its ownBUNDLER_VERSIONto child processes, allowing formula builds to use their required Bundler version.

Brewfiles record language-tool sources alongside other packages, reducing separate installation instructions when reproducing an environment on another machine.

Command and configuration migrations and replacements.

#### 🗃️ Casks

Formula links take precedence when formulae and casks provide the same commands, with warnings explaining how to restore the cask links.

* brew upgradeskips incompatible casks while upgrading compatible applications; both it andbrew outdatedhonourHOMEBREW_NO_UPGRADE_AUTO_UPDATES_CASKS, preservingself-updating applications’ opt-out.
* brew uninstallremoves records for casks missing from the API, warning about possible leftovers, andavoids needless password prompts when files are already owned by the current user.
* brew linkandbrew unlinkaccept--cask/--casksand--formula/--formulae, allowing cask binaries, manpages and completions to be disabled or restored without reinstalling;--dry-runpreviews changes, whilebrew link --overwritereplaces conflicts and--forcereplaces only symlinks from the same cask.
* Homebrew’s API includes cask language variants, allowing installation to select the appropriate URL, checksum and artifacts from package data without evaluating the cask’s Ruby definition for each language choice.

Cask configuration migrations and replacements.

### 🍎 macOS users

Homebrew moves macOS Intelx86_64to Tier 3 in September 2026,announced in August 2025andrepeated in the 5.0.0 release notes on 12 November 2025; 7.0.0 also drops macOS 10.15.Homebrew still runs on Intel until September 2027, without project support or routine bottle builds. Apple and GitHub’s retreat from Intel support exceeds what Homebrew’s volunteers can replace.

* brew services runapplies per-service environment overrides without registering a login service, making temporary runs use the same configuration as a permanently registered service.
* brew shellenvsetsPATHdirectly, avoiding macOSpath_helpersubprocesses and configuration-file writes.
* Homebrewmoves Intel to Tier 3:existing bottles remain, but updated formulae may require source buildsafterunreliable infrastructure ended routine Intel bottle updates.
* Homebrew’s.pkginstaller is Apple Silicon onlyandrequires macOS Sequoia 15 or later;MacPorts may offer Intel users better binary package coverage.
* Homebrew installs prebuilt casks without Xcode Command Line Tools, removing a compiler dependency from application setup.
* Homebrewfully supports macOS Golden Gate 27, following itsbottle rollout; Sequoia 15, Tahoe 26 and Golden Gate 27 are Tier 1 on Apple Silicon.
* Homebrew permits Metal shader compilation inside the macOS sandbox, allowing ggml and whisper.cpp tests to use GPU acceleration without network access.

macOS support migrations

Interface or platform

Status in 7.0.0

Timing

Replacement

macOS Catalina 10.15 and earlier

Removed

Now

Upgrade to macOS Big Sur 11 or later.

Intel macOS

Tier 3; no new bottles

Now

Apple Silicon or 
MacPorts
.

macOS Sonoma 14

Tier 3; no new bottles

Now

macOS Sequoia 15 or later.

macOS Golden Gate 27 on Apple Silicon

Supported; Tier 1

Now

No migration required; prebuilt bottles available.

Running Homebrew on Intel Macs

Upcoming removal

2027-09-01

Apple Silicon or another package manager.

macOS Big Sur 11 on Apple Silicon

Upcoming removal

2027-09-01

macOS Monterey 12 or later.

#### 🖥️ Homebrew app

BrewUI is Homebrew’s fully released official graphical interface for macOS, making package management more approachable through a native application.

* brew install homebrew-appinstalls BrewUI on macOS Tahoe 26 or later.
* BrewUI brings package browsing, search and installed-version details into one window, making it easier to explore available software and review an existing installation.
* BrewUI shows the underlyingbrewcommands for package operations, keeping the work visible and helping connect graphical actions with familiar terminal commands.

### 🐧 Linux users

Homebrew 6.0.0introduced Bubblewrap sandboxing. Homebrew 7.0.0replaces it with Landlock, requiring no dependencies or escalated Docker permissions, which caused setup problems with Bubblewrap.

Status in 7.0.0:kernels without Landlock continue working without Linux sandboxing in the less secure pre-6.0.0 configuration;brew doctorreports missing protection as an advisory.

* brew configreports the Landlock ABI for troubleshooting.
* Homebrew supports Landlock ABI 2 on Linux 6.1, warning when the kernel cannot enforce network restrictions.
* Homebrew moves AppImages to their application destination, matching macOS.appinstallations instead of versioned symlinks, so self-updates preserve launchers.

Linux configuration

Interface or platform

Status in 7.0.0

Timing

Replacement

HOMEBREW_SANDBOX_LINUX

Disabled

Now

Remove it; Landlock is used automatically where available.

HOMEBREW_NO_SANDBOX_LINUX

Deprecated

2027-12-11

No replacement opt-out; unavailable Landlock remains advisory.

HOMEBREW_ARCH

Deprecated

2027-12-11

Default native CPU optimisation.

### 🍾 Non-default prefix users

Homebrew relocates compatible bottles to shorter prefixes, avoiding source builds outside the default installation location.

Status in 7.0.0:limits are 13 bytes on Apple Silicon macOS, 26 on Linux and 10 for existing Intel macOS bottles. These count the full path, including slashes; the Cellar must also fit its build-time length. Bottles marked:anyor:any_skip_relocationare relocatable to any prefix.

* Homebrew relocates prefix symlinks so they remain usable elsewhere.
* Homebrew records relocation metadata at build time, reducing repeated installation scans and allowing installation to apply the recorded changes instead of rediscovering every embedded path on each machine.

Upcoming rollout:padded buildsaim to makeevery bottle and dependency relocatable to prefixes up to 64 bytes on Apple Silicon macOS and both Linux architectures. This may eventually allow full support within those limits; non-default prefixes remain unsupported for now, with no rollout date.

### 🔍 Security teams and auditors

Homebrew’s new advisory databaserecords vulnerabilities against the formula versions and revisions Homebrew ships, including backported security fixes.brew vulnsis built in, checking known vulnerabilities usingOSV.devwithout another tap or gem.

* brew vulnsscans installed formulae and reports untrusted-tap skips, with--severity=high,--depsand--brewfilefor focused checks. It prioritises remediation using--fix-availableand--no-fix-available,--fix-typefor released versus patched fixes and--list-skippedfor coverage gaps.
* Homebrew publishesadvisory findings in the formula APIand adownloadable advisory index, helping other tools distinguish outstanding vulnerabilities from fixes already shipped. The database’sOSV-format records are freely reusable under CC0, giving security teams a shared source of Homebrew-specific vulnerability data.
* Homebrew recognises security patches annotated withresolves, avoiding vulnerability reports for fixes already included in a package.
* Homebrew adds upstream package identifiers to software bills of materials, allowing external tools to connect source archives with registries such as PyPI, npm and Cargo rather than relying only on Homebrew formula names.
* Homebrew verifies attestations for supported third-party tap bottles, extending build-provenance checks beyondhomebrew/corewhen a tap publishes the required attestations.

### 🐳 Homebrew users in CI

Homebrew imagesandGitHub Actionsprovide maintained migration targets.

* brew test-bot --build-dependents-from-sourcelimits source builds to ten dependants per formula per shard, prioritising popular packages, enablingbroader Linux source-build coveragewhile keeping CI runtime manageable.
* Homebrewruns routine Golden Gate dependant testsonGitHub’sxcode-27runners, reducing reliance on self-hosted infrastructure.
* Homebrew retires the Ubuntu 22.04 image; use the maintained general-purpose image below.
* Homebrew’s versioned actions pin internal dependencies, making workflow upgrades reviewable; migrate@mainand removed@masterreferences to releases or full SHAs.
* Homebrew usesHomebrew/actions/setup-rubywithportable-ruby: truein itsRuby workflow, allowing CI jobs to select the same interpreter as Homebrew without depending on internal Ruby entry points.

CI migrations

Interface or platform

Status in 7.0.0

Timing

Replacement

ghcr.io/homebrew/ubuntu22.04

Removed

Now

ghcr.io/homebrew/brew
.

Homebrew/actions/*@master

Removed

Now

CalVer release
 or full SHA; no redirect.

Homebrew/actions/*@main

Migration recommended

Now

CalVer release
 or full SHA.

### 🛠️ Tap maintainers

Authoring tools reduce manual setup and encourage safer package definitions.

* brew audit --cask --online --fixcorrects macOS requirements and application-name case;brew audit --strictdetects downloaded prebuilt npm executables in installedhomebrew/coreformulae, helping maintainers enforce source-build requirements.
* brew style --fixconsolidates platform-specific cask checksums and sorts dependencies, simplifying cross-platform definitions;brew stylealsorejects broadcom.install4j.*uninstall and zap patternsthat could affect unrelated applications.
* brew tap-newgenerates automatic update workflows for new taps, checking upstream versions on a schedule and opening pull requests so maintainers can review updates without manually checking each formula. It alsogenerates attesting bottle-publishing workflows by default, with--no-attestationsas an opt-out, helping new taps publish the provenance that Homebrew can verify when their users install bottles.
* brew bump-cask-prcan generate separate Intel and Apple Silicon version stanzas from architecture-specific update results, allowing maintainers to follow upstream applications that release different versions for each architecture without manually rewriting supported root-level definitions.
* brew bump-formula-prupdates Git resources whose version is a commit hash, keeping both the version and pinned revision in sync for projects without release tags.
* brew creategenerates syntactically valid formula templates, withseparate fetch and offline-build phases for Go and Rustto prevent downloads during compilation.
* brew update-python-resources --ignore-main-package-cooldownbypasses only the main package’s cooldown in third-party formulae.
* brew benchmarkmeasures cold and warm install/fetch workloads separately, with--runs=controlling repetitions and--execsupporting custom Hyperfine commands, so contributors can identify whether a change improves fresh downloads, cached installations or command overhead rather than relying on one combined timing.
* brew bump-compatibility-versionrecords changes requiring dependant rebuilds.
* brew formula-python-resources --all/--tap=inventories Python resources, whilebrew bump-python-resources-pr --packages=opens security updates, with-n/--dry-run,--install-dependencies,--no-fork,--branch=,--message=and--output=supporting automation.
* Homebrew formulae usepython3to select their direct Python dependency without hardcoded interpreter paths.
* Homebrew formulae can declarestop_timeoutfor services, giving databases and other stateful applications longer to shut down gracefully before the service manager terminates them;stop_timeout 60sets a one-minute allowance on both macOS and Linux.
* Homebrew’spython_major_minor_versionhelper supplies the selected Python version, avoiding repeated version-detection code in formula definitions that need versioned paths or arguments.
* Homebrew’sstd_go_args(ldflags: :goreleaser)supplies common GoReleaser build metadata, including version, commit and build date, helping upstream applications report useful version information from Homebrew builds without each formula recreating those linker arguments.
* Homebrew formulae and casks can record a human homepage check withhomepage ..., browsed: "YYYY-MM-DD", pausing automated availability checks for one year when a site works in browsers but blocks automated requests, while ensuring the manual check has an expiry.
* Homebrew services can use shared package path helpers, allowing service definitions to refer to package locations consistently without duplicating path construction between their commands and environment settings.

#### 🪜 Install steps

Formulapost_installand cask*flightRuby blocks are deprecated in favour of declared*_steps. Explicit operations and paths allow validation, sandboxing and signed API delivery, making setup safer and avoiding repeated package evaluation.

Status in 7.0.0:official taps reject legacy hooks; third-party taps receive warnings until 11 December 2027.

* brew style --fixconverts common hooks;manual migrationsrequire rewriting the block’s contents as declared steps, following theFormula CookbookorCask Cookbook.
* Homebrew provides structured file operations and configuration writes, preserving common setup without arbitrary Ruby; formula authors describe the intended operation and target, while Homebrew handles validation and execution consistently.
* Homebrew validates serialised steps before execution, giving package authors a defined set of supported operations and allowing API-delivered setup to follow the same rules as locally loaded definitions.

Install hook migrations

Interface or platform

Status in 7.0.0

Timing

Replacement

Formula 
post_install

Deprecated

2027-12-11

post_install_steps

Cask 
preflight

Deprecated

2027-12-11

preflight_steps

Cask 
postflight

Deprecated

2027-12-11

postflight_steps

Cask 
uninstall_preflight

Deprecated

2027-12-11

uninstall_preflight_steps

Cask 
uninstall_postflight

Deprecated

2027-12-11

uninstall_postflight_steps

The migration guide lists install-step names, DSLs and public API replacements.

Maintenance command removals and replacements are also documented.

### 🙏 Finally

* The Intel support decision reflects the limits of a volunteer-run project:Apple have dropped Intelx86_64support from macOS 27 Golden GateandGitHub Actions will retire Intel macOS runners in autumn 2027. If Apple and Microsoft’s GitHub, two of the world’s largest technology companies, cannot continue supporting macOS Intelx86_64, sadly neither can Homebrew.MacPorts still supports macOS Intelx86_64and is likely to provide better results on this platform.
* Homebrew is a non-profit project run entirely by volunteers, not employees. We need your funds to pay for software, hardware and hosting around continuous integration and future improvements to the project. Every donation will be spent on making Homebrew better for our users. Please consider a regular donation throughGitHub Sponsors,OpenCollectiveandPatreon.
* Homebrew/brew (still) has no open issuesat the time of writing, as has been the case for most of the period since Homebrew 6.0.0 🎉.

Thanks to all our hard-working volunteer maintainers, contributors, sponsors and supporters for getting us this far.

### Latest Posts

* 6.0.011 Jun 2026Today, I’m proud to announce Homebrew 6.0.0. The most significant changes since 5.1.0 are a new tap trust security mechanism, the new faster, smaller, default internal...
* 5.1.010 Mar 2026Homebrew 5.1.0 has been released. Homebrew’s most significant changes since 5.0.0 are expanded brew bundle support, brew version-install, new -full formula handling an...
* 5.0.012 Nov 2025Today, I’d like to announce Homebrew 5.0.0. The most significant changes since 4.6.0 are download concurrency by default, official support for Linux ARM64/AArch64, tim...
* 4.6.005 Aug 2025Today, I’d like to announce Homebrew 4.6.0. The most significant changes since 4.5.0 are opt-in concurrent downloads with HOMEBREW_DOWNLOAD_CONCURRENCY, preliminary ma...

### Subscribe to be notified about new posts

Email