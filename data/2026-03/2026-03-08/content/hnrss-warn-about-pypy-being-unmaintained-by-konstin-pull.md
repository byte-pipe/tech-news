---
title: 'Warn about PyPy being unmaintained by konstin · Pull Request #17643 · astral-sh/uv · GitHub'
url: https://github.com/astral-sh/uv/pull/17643
site_name: hnrss
content_file: hnrss-warn-about-pypy-being-unmaintained-by-konstin-pull
fetched_at: '2026-03-08T11:07:45.619953'
original_url: https://github.com/astral-sh/uv/pull/17643
date: '2026-03-08'
description: 'An extremely fast Python package and project manager, written in Rust. - Warn about PyPy being unmaintained by konstin · Pull Request #17643 · astral-sh/uv'
tags:
- hackernews
- hnrss
---

astral-sh

 

/

uv

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.7k
* Star80.5k

## Conversation

 

Member

### konstincommentedJan 21, 2026

It seems that PyPy is not being actively developed anymore and is phased out even by numpy (numpy/numpy#30416). There's no official statement from the project, but the numpy issue is from a PyPy developer. I added a warning to avoid users assuming PyPy properly supported and developed Python distribution, and in anticipation of PyPy being eventually, slowly deprecated.

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

All reactions

 

 

Warn about PyPy being unmaintained

 …

 

35b675e

It seems that PyPy is not being actively developed anymore and is phased out even by numpy (
numpy/numpy#30416
). There's no official statement from the project, but the numpy issue is from a PyPy developer. I added a warning to avoid users assuming PyPy properly supported and developed Python distribution.

 

konstin

 added
 the 

 documentation

Improvements or additions to documentation

 label

 
Jan 21, 2026

 

EliteTK

 approved these changes

 

Jan 22, 2026

 

View reviewed changes

 

 

Contributor

### EliteTKleft a comment

There was a problem hiding this comment.

### Choose a reason for hiding this comment

The reason will be displayed to describe this comment to others.Learn more.

 Choose a reason
 

Spam

Abuse

Off Topic

Outdated

Duplicate

Resolved

 

Hide 
comment

Is it intentional that the note is duplicated?

It feels like it might be, but they're very close together - seems somewhat excessive?

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

All reactions

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

docs/concepts/python-versions.md

 Outdated

 

!!! note

 
PyPy is [not actively developed anymore](https://github.com/numpy/numpy/issues/30416) and

 
supports only up to Python 3.11.

 

 

Member

### zaniebcommentedJan 22, 2026

Yeah I think maybe let's just note it on the managed distributions section?

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 
konstin

and others

 added 
3
 commits
 
January 22, 2026 10:06

 

 

 

 

Update docs/concepts/python-versions.md

 …

 

3c8b3b8

Co-authored-by: Tomasz Kramkowski <tom@astral.sh>

 

 

 

Mention only once

fdc933e

 

 

 

Review

4e85a43

 

 

Member

Author

### konstincommentedJan 22, 2026

I reduced it to be only one note.

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

konstin

enabled auto-merge (squash)

 
January 22, 2026 09:17

 
Hide details

View details

konstin

 merged commit 
7a3e731

 into

 

main

Jan 22, 2026

 52 checks passed
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

konstin

 
 deleted the
 

 konsti/warn-pypy

 

 branch

 
January 22, 2026 09:23

BrewTestBot

 mentioned this pull request
 

Jan 26, 2026

 uv 0.9.27
 
Homebrew/homebrew-core#264626

 

 Merged

tmeijn
 

 pushed a commit
 to tmeijn/dotfiles
 that referenced
 this pull request

 

Jan 27, 2026

 

build(deps): update astral-sh/uv to v0.9.27

…

8696371

This MR contains the following updates:

| Package | Update | Change |
|---|---|---|
| [astral-sh/uv](
https://github.com/astral-sh/uv
) | patch | `0.9.26` → `0.9.27` |

MR created with the help of [el-capitano/tools/renovate-bot](
https://gitlab.com/el-capitano/tools/renovate-bot
).

**Proposed changes to behavior should be submitted there as MRs.**

---

### Release Notes

<details>
<summary>astral-sh/uv (astral-sh/uv)</summary>

### [`v0.9.27`](
https://github.com/astral-sh/uv/blob/HEAD/CHANGELOG.md#0927
)

[Compare Source](
astral-sh/uv@
0.9.26...0.9.27
)

Released on 2026-01-26.

##### Python

- Upgrade Pyodide to 0.29.2 ([#&#8203;17652](
astral-sh/uv#17652
))
- Upgrade to GraalPy 25.0.2 ([#&#8203;17634](
astral-sh/uv#17634
))

##### Enhancements

- Add `-t` shortform for `--target` to `uv pip` subcommands ([#&#8203;17501](
astral-sh/uv#17501
))
- Add support for ROCm 7.0 and 7.1 accelerator backends ([#&#8203;17681](
astral-sh/uv#17681
))
- Further improve free-threading ABI incompatibility errors ([#&#8203;17491](
astral-sh/uv#17491
))
- Implement `uv pip freeze --exclude` flag ([#&#8203;17045](
astral-sh/uv#17045
))
- Improve warnings for `--system` and `--no-system` in `uv venv` ([#&#8203;17647](
astral-sh/uv#17647
))
- Make `uv pip compile` attempt to download a specified `--python-version` if it can. ([#&#8203;17249](
astral-sh/uv#17249
))
- Support Trusted Publishing with pyx ([#&#8203;17438](
astral-sh/uv#17438
))
- Fix JSON schema for `exclude-newer-package` ([#&#8203;17665](
astral-sh/uv#17665
))

##### Preview features

- Better detection for conflicting packages ([#&#8203;17623](
astral-sh/uv#17623
))
- Upgrade based on outdated build versions in `uv python upgrade` ([#&#8203;17653](
astral-sh/uv#17653
))

##### Bug fixes

- Change chocolatey system test to ensure uv uses the right python ([#&#8203;17533](
astral-sh/uv#17533
))
- Fix infinite loop when `SSL_CERT_FILE` is a directory ([#&#8203;17503](
astral-sh/uv#17503
))

##### Documentation

- Add cargo-xwin to the CONTRIBUTING guide ([#&#8203;17507](
astral-sh/uv#17507
))
- Fix typo in the documentation of UV\_PUBLISH\_INDEX ([#&#8203;17672](
astral-sh/uv#17672
))
- Move MSRV to platform support section ([#&#8203;17534](
astral-sh/uv#17534
))
- Update the testing instructions in the CONTRIBUTING guide ([#&#8203;17528](
astral-sh/uv#17528
))
- Use `--locked` to install `cargo-xwin` in guide ([#&#8203;17530](
astral-sh/uv#17530
))
- Warn about PyPy being unmaintained ([#&#8203;17643](
astral-sh/uv#17643
))
- docs: Correct gitlab-ci.yml to .gitlab-ci.yml ([#&#8203;17682](
astral-sh/uv#17682
))

##### Other changes

- Update MSRV to 1.91 ([#&#8203;17677](
astral-sh/uv#17677
))

</details>

---

### Configuration

📅 **Schedule**: Branch creation - At any time (no schedule defined), Automerge - At any time (no schedule defined).

🚦 **Automerge**: Disabled by config. Please merge this manually once you are satisfied.

♻ **Rebasing**: Whenever MR becomes conflicted, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this MR and you won't be reminded about this update again.

---

 - [ ] <!-- rebase-check -->If you want to rebase/retry this MR, check this box

---

This MR has been generated by [Renovate Bot](
https://github.com/renovatebot/renovate
).
<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0Mi45Mi40IiwidXBkYXRlZEluVmVyIjoiNDIuOTIuNCIsInRhcmdldEJyYW5jaCI6Im1haW4iLCJsYWJlbHMiOlsiUmVub3ZhdGUgQm90IiwiYXV0b21hdGlvbjpib3QtYXV0aG9yZWQiLCJkZXBlbmRlbmN5LXR5cGU6OnBhdGNoIl19-->

github-actions

bot

 mentioned this pull request
 

Mar 8, 2026

 Verify: nye trusler til review
 
LaZyDK/dkcyber-threat-monitor#103

 

 Open

 

### EirikurcommentedMar 8, 2026

This is a very bad situation. NodeJS nearly melted-down when the left-pad-string library went unmaintained and got a new hostile maintainer. I'd love to see a PyPi replacement with uv-like smarts.

 
👎

23

 
djmattyg007, jordigh, TomasLoow, jcamiel, jonnybrooks, Sofahamster, danielsamuels, jwd83, danthedaniel, vadym-shavalda, and 13 more reacted with thumbs down emoji

 
😄

2

 
chowder and usdogu reacted with laugh emoji

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

### dharmabcommentedMar 8, 2026

This is a very bad situation. NodeJS nearly melted-down when the left-pad-string library went unmaintained and got a new hostile maintainer. I'd love to see a PyPi replacement with uv-like smarts.

This thread is aboutPyPy, notPyPI.

 
👍

17

 
shiyu15, marianhlavac, Sofahamster, adithyabsk, nwalters512, wkhere, jwd83, danthedaniel, auscompgeek, winterrdog, and 7 more reacted with thumbs up emoji

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Foxhunt

 mentioned this pull request
 

Mar 8, 2026

 Daily Hacker News 08-03-2026
 
Foxhunt/daily-hackernews#606

 

 Open

github-actions

bot

 mentioned this pull request
 

Mar 8, 2026

 🌐 Global Tech Briefing - 2026-03-08
 
AtomChen0425/Global_Trends#20

 

 Open

blka

 mentioned this pull request
 

Mar 8, 2026

 Daily Hacker News 08-03-2026
 
blka/daily-hackernews#328

 

 Open

github-actions

bot

 mentioned this pull request
 

Mar 8, 2026

 Daily Content Summary 2026-03-08
 
jhengy/content-aggregator#419

 

 Open

 

### stuaxocommentedMar 8, 2026

Pypy is maintained, it's always been behind CPython, here is one of the Devs saying as much:

https://news.ycombinator.com/item?id=47295551

[cfbolztereick] PyPy isn't unmaintained. We are certainly fixing bugs and are occasionally improving the jit. However, the remaining core devs (me among them) don't have the capacity to keep up with cpython. So for supporting new cpython versions we'll need new people to step up. For 3.12 this has started, we have a new contributor who is pushing this along.

 

All reactions

Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

 

Sign up for free

to join this conversation on GitHub
.
 Already have an account?
 
Sign in to comment

Add this suggestion to a batch that can be applied as a single commit.
This suggestion is invalid because no changes were made to the code.
Suggestions cannot be applied while the pull request is closed.
Suggestions cannot be applied while viewing a subset of changes.
Only one suggestion per line can be applied in a batch.
Add this suggestion to a batch that can be applied as a single commit.
Applying suggestions on deleted lines is not supported.
You must change the existing code in this line in order to create a valid suggestion.
Outdated suggestions cannot be applied.
This suggestion has been applied or marked resolved.
Suggestions cannot be applied from pending reviews.
Suggestions cannot be applied on multi-line comments.
Suggestions cannot be applied while the pull request is queued to merge.
Suggestion cannot be applied right now. Please check back later.