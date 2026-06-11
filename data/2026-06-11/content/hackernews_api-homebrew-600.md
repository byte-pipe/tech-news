---
title: 'Homebrew: 6.0.0'
url: https://brew.sh/2026/06/11/homebrew-6.0.0/
site_name: hackernews_api
content_file: hackernews_api-homebrew-600
fetched_at: '2026-06-11T19:53:04.523455'
original_url: https://brew.sh/2026/06/11/homebrew-6.0.0/
author: MikeMcQuaid
date: '2026-06-11'
published_date: '2026-06-11T00:00:00+00:00'
description: Today, I’m proud to announce Homebrew 6.0.0. The most significant changes since 5.1.0 are a new tap trust security mechanism, the new faster, smaller, default internal Homebrew JSON API, sandboxing on Linux, better defaults informed by our user survey, many brew bundle improvements, improved performance and initial support for macOS 27 (Golden Gate).
tags:
- hackernews
- trending
---

## 6.0.0

### 11 June 2026

### MikeMcQuaid

Today, I’m proud to announce Homebrew 6.0.0.
The most significant changes since 5.1.0 are a new tap trust security mechanism, the new faster, smaller, default internal Homebrew JSON API, sandboxing on Linux, better defaults informed by our user survey, manybrew bundleimprovements, improved performance and initial support for macOS 27 (Golden Gate).

### ✨ Highlights since 5.1.0

#### 🔐 Tap trust

Homebrew 6.0.0 introduces tap trust. A third-party tap can contain arbitrary, unsandboxed Ruby that runs on your machine, so Homebrew now requires taps (and tap-qualified formulae and casks) to be explicitly trusted before their code is evaluated or run. This reduces the risk from malicious or compromised taps while leaving the official Homebrew taps trusted by default. See the newTap-Trust documentationfor details.

* Homebrewenforces initial tap trust so untrusted taps are flagged before their code runs,trusts qualified tap items before install,stops auto-tapping untrusted taps,pins tap allow, forbid and trust lists to remotesanduses tap trust when evaluating all formulae and casks.
* brew tapgains commands for managing tap trust, cantrust a tap by its remote URL,brew trustadds a--json=v1flagandbrew tap-infoadds atrustedfield.
* brew bundlehonours thetrusted:optionandbrew bundle dumprecords trusted bundle entries,marking custom-remote taps as trusted.
* docs.brew.sh has new pages, including Tap-Trust, explaining Homebrew’s new tap trust model, andHomebrew trusts taps in test-bot.

#### ⚡ Default internal JSON API

Theinternal JSON APIisnow the default,advancingthe smaller API that Homebrewre-enabledandturned on for developersrecently. It combines all Homebrew’s metadata into a single download, sobrewupdates faster and talks to the network less. It was opt-in viaHOMEBREW_USE_INTERNAL_APIsince 5.0.0; that variable is now deprecated (see below).

#### 🐧 Linux sandbox

TheLinux Bubblewrap sandboxaligns Linux with macOS, where build, test and postinstall phases already run sandboxed. It ison by default for developers, Homebrewmoved its macOS sandbox logicto share code,improved Linux sandbox behaviour(withHomebrew/homebrew-core setting the sandbox env in CI),hardened sandboxed install phases,sandboxed cask executable hooks,allowed logs in the build sandbox,installed Bubblewrap on hosted Ubuntuandskips sandbox setup for syntax-only jobs.

#### ⚙️ Better defaults

* Following ourHomebrew user survey, we have made many changes based on the results. The most notable ismakingaskmode the default for developers, sobrew installandbrew upgradeshow a dependency summary and confirmation prompt before making changes.
* Homebrewadds ask dependency plans and cask support,accepts one-key ask confirmationsandaligns ask dry-run prompts.
* Homebrewfetches ask upgrades together,prints the ask upgrade summary sooner,skips the upgrade ask prompt when empty,adds a finalbrew upgradesummaryandexplains the upgrade metadata fetch.

#### 📦brew bundle

* brew bundlegains many improvements, most notablyparallel formula installationthat nowruns jobs automatically by default, plusnpmandkrewextensions,wider cleanup supportand, on Windows,wingetsupport.
* Homebrewadds cleanup support to npm, cargo, go and uv extensionsandasks before removing during cleanup.
* Homebrew runsbrew bundle krewviakubectl-krewdirectly,respectsCARGO_HOMEand friends forcargo,adds a--describeflag tobrew bundle addandtriesmas installbefore falling back tomas get.
* Homebrewadds bundle type disable flags,improves check guidanceandchecks formula link status.
* Homebrewserialises formula locks,makes non-core DSLs a single file,removes description comments frombrew bundle/removerandavoids parsing the output ofbrew services list.
* brew bundleperforms npm installs more securely.

#### 🏎️ Performance

Homebrew is faster across the board, withstartup performance tweaks,a ~30% fasterbrew leaves,parallelised bottle tab fetching on upgradeandless work loading Ruby libraries at startup.

#### 🍎 macOS 27 (Golden Gate)

Homebrew adds initial support for macOS 27 (Golden Gate).

### 🔮 Upcoming changes

* macOS 27 (Golden Gate) drops Intel support, so per ourSupport Tiers: in September 2026,macOS Intelx86_64moves to Tier 3with no CI support and no new bottles (binary packages) built for macOS Intel; in September 2027,macOS Intelx86_64will be unsupported entirely and all related code deleted.
* Themastertomainmigration begun in 4.6.0 continues: more repositories no longer updatemaster,GitHub Actions warn@masterusers to migrate to@mainand thesync-default-branchesworkflows are removed fromHomebrew/homebrew-caskandHomebrew/homebrew-core.
* Casks that fail macOS Gatekeeper checks, deprecated in 5.0.0, remain on track to be disabled in September 2026.

### 🔒 Security

#### 🚨 Security advisories

Homebrew published three security advisories:

* The POST download strategy bypassed the documented HTTPS-to-HTTP redirect protection by discarding the resolved URL (GHSA-7699-qf8c-q47m), fixed byenforcing secure redirects.
* Root code execution was possible via Git hooks in the macOS.pkgpostinstall (GHSA-6689-q779-c33m), fixed bycleaning Homebrew git stateandreplacing the installer git directory.
* The macOS installer package trusted a user-controlled/var/tmpplist and could assign Homebrew ownership to a local attacker (GHSA-59v8-x8q4-px5c), fixed bytweaking the macOS.pkgpackage-user plist handling.

#### 🛡️ Other security improvements

* Homebrewfilters sensitive environment variables during Ruby evaluationsanddefersHOMEBREW_*environment secrets to download time.
* Homebrewruns forbidden checks for casks and formulae before downloadand lets yourequire checksums for casks withHOMEBREW_CASK_OPTS_REQUIRE_SHA.
* Homebrew links to a shared security policy.

### 🗑️ Deprecations

* Homebrew deprecates default opt-ins.
* Homebrew deprecates now-default bundle and internal API environment variables such asHOMEBREW_BUNDLE_NO_SECRETSandHOMEBREW_USE_INTERNAL_API.
* Homebrew marks unused options for deprecation.
* Various other Homebrew 6.0.0 deprecations.
* Homebrew’s SBOM support is now opt-in withHOMEBREW_SBOM.

### 🎁 Features

#### 🖥️ Casks

* Homebrewcan pin casksandsupports casks inbrew missing.
* Homebrewadds AppImage support for Linuxandimplements a Linux freedesktop trash for casks.
* Homebrew improves cask upgrades bysharing upgrade download queues,moving upgrade summaries before fetch,adding a quit opt-outandreopening closed apps during upgrade.
* Homebrew improvesauto_updatescasks:improving how they update,refining the behaviourfurther,gating auto-updates behind opt-inandupgrading them when the bundle version is stale.
* caskadds agenerate_completions_from_executableDSL artifactandincludes resolved artifact targets in JSON output.
* Homebrewshows a cask version transition in per-cask upgrade output,skips valid cached cask fetches,speeds up cask backup copiesand hascaskroomuse the user’s primary group on Linux.
* brew doctorandbrew cleanuphandle corrupt Caskroom directories.

#### 💻 Operating system support

* Homebrewmakes Linux cask requirements explicit,aligns cask macOS dependencies,supports baredepends_on :macosin casks,tracks macOS support explicitlyandemits Linux variations for casks with Linux checksums.
* Homebrew adds a maximum macOS for cask dependencies.Homebrew/homebrew-cask adopts thenewdepends_on maximum_macos:syntaxand fixes its macOS dependencies inHomebrew/homebrew-caskandHomebrew/homebrew-core.
* Homebrewadds M5 and M5 Pro/Max CPU recognitionandcaps the OCLP tier when macOS is outdated.
* Homebrewlabels WSL analytics,shows the Windows build on WSL inbrew configandmoves thewsl?boolean fromOS::Linuxup to theOSmodule.

#### 🚰 Taps

* Homebrew recognises more equivalent tap remote forms, ignoring a.gitsuffix when matching GitHub remotes and consolidating tap remote normalisation.(andmore)
* Homebrewhandles formulae and casks more uniformly across commands,installs explicitly requested tapsandstops implicit tap installation.
* Homebrewuses worktrees for local core tapsandblocks worktree updates.
* Homebrewshares full-name parsing helpersanduses full-name helpers for split names.

#### ℹ️brew infoandbrew tap-info

* brew infooutput is clearer:more consistent and helpful, witha Binaries section listing executables,a clearer recursive runtime dependencies line,clearer same-named conflicts and shadowed formulaeanda list versions JSON output.
* brew infoshows installed state better:the upgrade target for outdated@-versioned formulae,installed dependents with--verbose,deprecated and disabled packages in install status,installed formulae resolved from the receipt’s tap with a shadowing warning,the installed version and an upgrade hint on the headline,other installed versionsandan installed info inventory.
* brew infoandbrew tap-infoskip the uninstalled marker when not a problem,show more tap info for packagesandbrew tap-infolists formulae and casks.
* brew which-formulashows install statusandHomebrew shows quarantine script usage.

#### 🆕 New commands, flags and output

* brew execis a new command, likenpx, thatsupports formulae environments.
* brew as-console-useris a new command for running Homebrew as the right user under MDM/rootenvironmentsandbrew update <formula>is aliased toupgrade.
* Homebrew tidies help and completions:omitting aliases from completions,hidingHOMEBREW_CASK_OPTS_*from help,hiding maintainer commandsandhidinghide_from_man_pagecommands frombrew commands.
* Homebrewavoids install warning annotationsandwarns when formula executables are shadowed onPATH.

#### 🧊 Cooldowns, livecheck and bumping

* Homebrew adds download cooldowns forBundler,RubyGems livecheck,npm and pip defaults,PyPI resource resolutionandnpm and PyPI inbumpto avoid upstream supply-side security risks.
* Homebrewprintsbumpskip status, messages and errorsandchecks RubyGems licences.
* Homebrewrespectslivecheckthrottle days inaudit,adds livecheck throttling by daysandspeeds up the formula throttle days check.

#### ⬇️ Downloads and fetching

* brew fetch --all-platformsfetches every variant, Homebrewprints download error details when using concurrency,preserves partial downloads on network errors,avoids cached manifest downloadsandhints when a download is HTML, not a binary.
* Homebrew avoids redundant Caskroomchgrp.

#### 🛎️ Services

* Homebrewstarts systemd timers for services,creates service path directories automatically(withHomebrew/homebrew-core adopting the new service path creation logic) andaudits redundant service path setup.
* brew servicesno longer fails to load with--sudo-service-user.

#### 🧪 Formulae and packaging

* Homebrewadds the VCS revision asscm_revisionin the tab,supports in-repository patch files,supports CPS metadata directoriesandincludes patches informulato_hash.
* Homebrewrespects installed dependents during autoremoveandcross-checksautoremovecandidates against formula definitions.

#### 🪜 Install steps framework

* Theinstall steps frameworkexpresses common postinstall, preflight and postflight behaviour as ordered, literal-only DSL data that is exposed through the JSON APIs. Where a formula or cask only does simple file preparation, it no longer needs to download and evaluate a Ruby file at install time. Homebrew addsformula install steps,cask install steps,an audit for formula install steps,install step rebuild actions,rebuild step methods,rebuild step RuboCop checksandan audit of cask flight step conversions;homebrew/coreandhomebrew/caskadopt the new DSLs (post_install_steps,postinstallandflight steps). Inhomebrew/coreandhomebrew/caskthis covers a large share ofpost_installand*flightblocks (creating directories, touching markers, moving and symlinking files), with more operation types planned.

#### 🔀 Other changes

* brew vulnsis a new Homebrew tap and subcommand that checks installed packages for known vulnerabilities🔒.
* Homebrew warns for Nix-managed Homebrew.

#### 🧹 Internals, typing and refactors

* Homebrewreplacesbrew which-update,uses an AST for source rewritesandenforces public API visibility and docs.
* Homebrew reworks command parsing:parser subcommand scaffolding, converting thebundle,servicesandremainingsubcommands,scoping subcommand option constraintsandusage help, and no longerrestricting global options to subcommands.
* Homebrewlimits Sorbet runtime defaultsandlimits recursive Sorbet in test-bot.

#### 🛠️ Continuous integration and developer tooling

* The Ubuntu 24.04 CI migration flagged in 5.1.0 for 6.0.0 has now landed, raising the Linux baseline.
* Homebrewannotates test-bot dependency impact,closes API-created issues that do not match a templateandcloses incomplete PRs.
* Homebrew’ssetup-homebrewGitHub Action defaults to the stable tagandtrusts taps on non-stablebrew.
* brew lgtmcovers tap audits and formula testsand Homebrewworks around a non-writable cache for lgtm commands inbrew.sh.
* workflows/dockerbuilds Ubuntu 26.04 imagesandtestdisablesreturn falsehandling.

#### 📚 Documentation

* Homebrew’s documentation improves: theRosetta cask support policy,unsupported multi-user setups,notability requirements,-fullformula guidance,upstream expectationsandlifecycle requests,the newauto_updatesbehaviourand aconsolidated deprecation policy.
* Homebrew clarifiescompatibility_versionguidanceandHomebrew/homebrew-core backfillscompatibility_version 1. This will help reduce the number of formulae that need upgraded bybrew upgradeover time.

Finally:

* Homebrew is a non-profit project run entirely by volunteers, not employees. We need your funds to pay for software, hardware and hosting around continuous integration and future improvements to the project. Every donation will be spent on making Homebrew better for our users. Please consider a regular donation throughGitHub Sponsors,OpenCollectiveandPatreon.
* Homebrew/brew has no open issuesat the time of writing 🎉.
* Homebrew has a brand newbrew.shhomepage style.
* BrewUI is Homebrew’s upcoming official graphical interface. It’s not ready for general use yet.
* Thebrew-rsexperiment in moving parts of Homebrew’s Ruby frontend to Rusthas concluded: benchmarks showed Homebrew’s Rust frontend only ahead on narrow, already-cached bottle fetches, not on representative full installs (pouring bottles, linking, writing metadata and health checks), so the performance focus has moved back to Ruby and to starting useful network and disk I/O sooner. We’veadded an FAQ entryexplaining all of this. Our numbers come from honest, fully-compatible comparisons. Not all unofficial Homebrew frontends seem to apply the same rigor to their benchmarks, compatability or security: your mileage with those may vary.
* Homebrew is increasingly a“package manager for everywhere”: Homebrew is recommended inMicrosoft’s Windows Developer Config for WSL comfort, works well onBazziteand nowsupportswingetinbrew bundleas a Windows-only feature.
* The Homebrew team is aware of the supply-side security issues with other package managers. We’ve taken various steps to mitigate these risks for our users, some existing (e.g. macOS sandboxing, human review on all changes, environment filtering, all package maintainers are Homebrew maintainers), some new (e.g. Linux sandboxing, sandboxing reads of sensitive locations, cooldown from riskier ecosystems). We will continue to monitor the supply-side security landscape and take further steps as needed. See the newSupply Chain Security documentationwe’veaddedfor details.
* Homebrew hasdocumented the principles behind our AI and LLM usage rulesin a newResponsible AI Usagepage.
* Homebrew has joined the Open Source Resistance and you should too.

Thanks to all our hard-working volunteer maintainers, contributors, sponsors and supporters for getting us this far.

### Latest Posts

* 5.1.010 Mar 2026Homebrew 5.1.0 has been released. Homebrew’s most significant changes since 5.0.0 are expanded brew bundle support, brew version-install, new -full formula handling an...
* 5.0.012 Nov 2025Today, I’d like to announce Homebrew 5.0.0. The most significant changes since 4.6.0 are download concurrency by default, official support for Linux ARM64/AArch64, tim...
* 4.6.005 Aug 2025Today, I’d like to announce Homebrew 4.6.0. The most significant changes since 4.5.0 are opt-in concurrent downloads with HOMEBREW_DOWNLOAD_CONCURRENCY, preliminary ma...
* 4.5.029 Apr 2025Today, I’d like to announce Homebrew 4.5.0. The most significant changes since 4.4.0 are major improvements to brew bundle/services, preliminary Linux support for cask...

### Subscribe to be notified about new posts

Email