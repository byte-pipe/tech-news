---
title: Open source security at Astral
url: https://astral.sh/blog/open-source-security-at-astral
site_name: hnrss
content_file: hnrss-open-source-security-at-astral
fetched_at: '2026-04-09T19:39:41.868554'
original_url: https://astral.sh/blog/open-source-security-at-astral
date: '2026-04-09'
description: Insights and guidance from our engineering team on how Astral secures its tools.
tags:
- hackernews
- hnrss
---

Back to blog

April
 8,
 2026

# Open source security at Astral

##### William Woodruff

@
woodruffw

Astral builds tools that millions of developers around the world depend on and trust.

That trust includes confidence in our security posture: developers reasonably expect that our tools
(and the processes that build, test, and release them) are secure. The rise of supply chain attacks,
typified by the recentTrivyandLiteLLMhacks, has developers questioning whether they can
trust their tools.

To that end, we want to share some of the techniques we use to secure our tools in the hope that
they're useful to:

1. Our users, who want to understand what we do to keep their systems secure;
2. Other maintainers, projects, and companies, who may benefit from some of the techniques we use;
3. Developers of CI/CD systems, so that projects do not need to follow non-obvious paths or avoid
useful features to maintain secure and robust processes.

## CI/CD security#

We sustain our development velocity onRuff,uv, andtythrough extensive CI/CD workflows that
run onGitHub Actions. Without these workflows we would struggle to review, test, and release our
tools at the pace and to the degree of confidence that we demand. Our CI/CD workflows are also a
critical part of our security posture, in that they allow us to keep critical development and
release processes away from local developer machines and inside of controlled, observable
environments.

GitHub Actions is a logical choice for us because of its tight first-party integration with GitHub,
along with its mature support forcontributor workflows: anybody who wants to contribute can
validate that their pull request is correct with the same processes we use ourselves.

Unfortunately, there's a flipside to this: GitHub Actions haspoor security defaults, and security
compromises like those ofUltralytics,tj-actions, andNxall began with well-trodden
weaknesses likepwn requests.

Here are some of the things we do to secure our CI/CD processes:

* We forbid many of GitHub's most dangerous and insecure triggers, such aspull_request_targetandworkflow_run, across our entire GitHub organization. These triggers are almost impossible to use
securely and attackers keep finding ways to abuse them, so we simply don't allow them.Our experience with these triggers is that many projectsthinkthat they need them, but the
overwhelming majority of their usages are better off being replaced with a less privileged trigger
(such aspull_request) or removed entirely. For example, many projects usepull_request_targetso that third-party contributor-triggered workflows can leave comments on PRs, but these use cases
are often well served byjob summariesor even just leaving the relevant information in the
workflow's logs.Of course, there are some use cases that do require these triggers, such as anything thatdoesreally need to leave comments on third-party issues or pull requests. In these instances we
recommend leaving GitHub Actions entirely and using a GitHub App (or webhook) that listens for the
relevant events and acts in an independent context. We cover this pattern in more detail underAutomationsbelow.

* We require all actions to be pinned to specific commits (rather than tags or branches, which are
mutable). Additionally, we cross-check these commits to ensure they match an actual released
repository state and are notimpostor commits.We do this in two ways: first with zizmor'sunpinned-usesandimpostor-commitaudits, and
again with GitHub's own "require actions to be pinned to a full-length commit SHA" policy. The
former gives us a quick check that we can run locally (and prevents impostor commits), while the
latter is a hard gate on workflow execution that actually ensures thatallactions, including
nested actions, are fully hash-pinned.Enabling the latter is a nontrivial endeavor, since it requiresindirectaction usages (the
actions called by the actions we call) to be hash-pinned as well. To achieve this, we coordinated
with our downstreams (example) to land hash-pinning across our entire dependency graph.Together, these checks increase our confidence in thereproducibilityandhermeticityof our
workflows, which in turn increases our confidence in their security (in the presence of an
attacker's ability to compromise a dependent action).However, whilenecessary, this isn'tsufficient: hash-pinning ensures that theaction'scontents are immutable, but doesn't prevent those immutable contents from making mutable decisions
(such as installing the latest version of a binary from a GitHub repository's releases). Neither
GitHub nor third-party tools perform well at detecting these kinds of immutability gaps yet, so we
currently rely on manual review of our action dependencies to detect this class of risks.When manual reviewdoesidentify gaps, we work with our upstreams to close them. For example,
for actions that use native binaries internally, this is achieved by embedding a mapping between
the download URL for the binary and a cryptographic hash. This hash in turn becomes part of the
action's immutable state. While this doesn't ensure that the binaryitselfis authentic, it does
ensure that an attacker cannot effectively tamper with a mutable pointer to the binary (such as a
non-immutable tag or release).

* We limit our workflow and job permissions in multiple places: we default to read-only permissions
at the organization level, and we additionally start every workflow withpermissions: {}and
only broaden beyond that on a job-by-job basis.
* We isolate our GitHub Actions secrets, wherever possible: instead of using organization- or
repository-level secrets, we use deployment environments and environment-specific secrets. This
allows us to further limit the blast radius of a potential compromise, as a compromised test or
linting job won't have access to, for example, the secrets needed to publish release artifacts.

To do these things, we leverage GitHub's own settings, as well as tools likezizmor(for static
analysis) andpinact(for automatic pinning).

## Repository and organizational security#

Beyond our CI/CD processes, we also take a number of steps to limit both the likelihood and the
impact of account and repository compromises within the Astral organization:

* We limit the number of accounts with admin- and other highly-privileged roles, with most
organization members only having read and write access to the repositories they need to work on.
This reduces the number of accounts that an attacker can compromise to gain access to our
organization-level controls.
* We enforcestrong2FA methods for all members of the Astral organization, beyond GitHub's
default of requiringany2FA method. In effect, this requires all Astral organization members to
have a 2FA method that's no weaker thanTOTP. If and when GitHub allows us to enforce only 2FA
methods that are phishing-resistant (such as WebAuthn and Passkeys only), we will do so.

* We impose branch protection rules on an org-wide basis: changes tomaincannot be force-pushed
and must always go through a pull request. We also forbid the creation of particular branch
patterns (likeadvisory-*andinternal-*) to prevent premature disclosure of security work.
* We impose tag protection rules that prevent release tags from being created until arelease deploymentsucceeds, with the release deployment itself being gated
on a manual approval by at least one other team member. We also prevent the updating or deletion
of tags, making them effectively immutable once created. On top of that we layer a branch
restriction: release deployments may only be created againstmain, preventing an attacker from
using an unrelated first-party branch to attempt to bypass our controls.
* Finally, we ban repository admins from bypassing all of the above protections. All of our
protections are enforced at the organization level, meaning that an attacker who manages to
compromise an account that has admin access to a specific repository still won't be able to
disable our controls.

To help others implement these kinds of branch and tag controls, we'resharing a gistthat shows
some of the rulesets we use. These rulesets are specific to our GitHub organization and
repositories, but you can use them as a starting point for your own policies!

## Automations#

There are certain things that GitHub Actions can do, butcan'tdo securely, such as leaving
comments on third-party issues and pull requests. Most of the time it's better to just forgo these
features, but in some cases they're a valuable part of our workflows.

In these latter cases, we useastral-sh-botto safely isolate these tasks outside of GitHub
Actions: GitHub sends us the same event data that GitHub Actions would have received (since GitHub
Actions consumes the same webhook payloads as GitHub Apps do), but with much more control and much
less implicit state.

However, there's still a catch with GitHub Apps: an app doesn'teliminateany sensitive
credentials needed for an operation, it just moves them into an environment that doesn't mix code
and data as pervasively as GitHub Actions does. For example, an app won't be susceptible to atemplate injectionattack like a workflow would be, but could still contain SQLi, prompt
injection, or other weaknesses that allow an attacker to abuse the app's credentials. Consequently,
it'sessentialto treat GitHub App development with the same security mindset as any other
software development. This also extends to untrusted code: using a GitHub App doesnotmake it
safe to run untrusted code, it just makes it harder to do so unexpectedly. If your processesneedto run untrusted code, theymustusepull_requestor another "safe" trigger that doesn't
provide any privileged credentials to third-party pull requests.

With all that said, we've found that the GitHub App pattern works well for us, and we recommend it
to other maintainers and projects who have similar needs. The main downside to it comes in the form
of complexity: it requires developing and hosting a GitHub App, rather than writing a workflow that
GitHub orchestrates for you. We've found that frameworks likeGidgethubmake the development
process for GitHub Apps relatively straightforward, but that hosting remains a burden in terms of
time and cost.

It's an unfortunate reality that there still aren't great GitHub App options for one-person and
hobbyist open source projects; it's our hope that usability enhancements in this space can be led by
companies and larger projects that have the resources needed to paper over GitHub Actions'
shortcomings as a platform.

We recommendthis tutorial by Mariattaas a good introduction to building GitHub Apps in Python.
We also plan to open sourceastral-sh-botin the future.

## Release security#

So far, we've covered aspects that tie closely to GitHub, as the source host for Astral's tools. But
many of our users install our tools via other mechanisms, such asPyPI,Homebrew, and ourDocker images. These distribution channels add another "link" to the metaphorical supply chain,
and require discrete consideration:

* Where possible, we useTrusted Publishingto publish to registries (like PyPI,crates.io, andNPM). This technique eliminates the need for long-lived registry credentials, in turn
ameliorating one of the most common sources of package takeover (credential compromise in CI/CD
platforms).
* Where possible (currently our binary and Docker images releases), we generate Sigstore-based
attestations. These attestations establish a cryptographically verifiable link between the
released artifact and the workflow that produced it, in turn allowing users to verify that their
build of uv, Ruff, or ty came from our actual release processes. You can see ourrecent
attestations for uvas an example of this.1

* We use GitHub'simmutable releasesfeature to prevent the post-hoc modification of the builds we
publish on GitHub. This addresses a common attacker pivoting technique where previously published
builds are replaced with malicious builds. Avariant of this techniquewas used in the recent
Trivy attack, with the attacker force-pushing over previous tags to introduce compromised versions
of thetrivy-actionandsetup-trivyactions.
* We do not use caching to improve build times during releases, to prevent an attacker from
compromising our builds via aGitHub Actions cache poisoning attack.

* To reduce the risk of an attacker publishing anewmalicious version of our tools, we use a
stack of protections on our release processes:Our release process is isolated within a dedicated GitHubdeployment environment. This means
that jobs that don't run in the release environment (such as tests and linters) don't have
access to our release secrets.In order toactivatethe release environment, the activating job must be approved by at least
one other privileged member of the Astral organization. This mitigates the risk of a single
rogue or compromised account being able to publish a malicious release (or exfiltrate release
secrets); the attacker needs to compromise at least two distinct accounts, both with strong 2FA.In repositories (like uv) where we have a large number of release jobs, we use a distinctrelease-gateenvironment to work the fact that GitHub triggers approvals foreveryjob that
uses the release environment. This retains the two-person approval requirement, with one
additional hop: asmall, minimally-privileged GitHub Appmediates the approval fromrelease-gatetoreleasevia adeployment protection rule.Finally, we use a tag protectionrulesetto prevent the creation of a release's tag until the
release deployment succeeds. This prevents an attacker from bypassing the normal release process
to create a tag and release directly.
* Our release process is isolated within a dedicated GitHubdeployment environment. This means
that jobs that don't run in the release environment (such as tests and linters) don't have
access to our release secrets.
* In order toactivatethe release environment, the activating job must be approved by at least
one other privileged member of the Astral organization. This mitigates the risk of a single
rogue or compromised account being able to publish a malicious release (or exfiltrate release
secrets); the attacker needs to compromise at least two distinct accounts, both with strong 2FA.In repositories (like uv) where we have a large number of release jobs, we use a distinctrelease-gateenvironment to work the fact that GitHub triggers approvals foreveryjob that
uses the release environment. This retains the two-person approval requirement, with one
additional hop: asmall, minimally-privileged GitHub Appmediates the approval fromrelease-gatetoreleasevia adeployment protection rule.
* Finally, we use a tag protectionrulesetto prevent the creation of a release's tag until the
release deployment succeeds. This prevents an attacker from bypassing the normal release process
to create a tag and release directly.

* For users who install uv via ourstandalone installer, we enforce the integrity of the installed
binaries via checksums embedded directly into the installer's source code2.

Our release processes also involve "knock-on" changes, like updating the our public documentation,
version manifests, and theofficialpre-commit hooks. These are privileged operations that we
protect through dedicated bot accounts and fine-grained PATs issued through those accounts.

Going forwards, we're alsolooking atadding codesigning with official developer certificates on
macOS and Windows.

## Dependency security#

Last but not least is the question of dependencies. Like almost all modern software, our tools
depend on an ecosystem of third-party dependencies (both direct and transitive), each of which is in
an implicit position of trust. Here are some of the things we do to measure and mitigate upstream
risk:

* We use dependency management tools likeDependabotandRenovateto keep our dependencies
updated,andto notify us when our dependencies contain known vulnerabilities.
* In general, we employcooldownsin conjunction with the above to avoid updating dependencies
immediately after a new release, as this is when temporarily compromised dependencies are most
likely to affect us.Both Dependabot and Renovate support cooldowns, anduv also has built-in support. We've found
Renovate's ability to configure cooldowns on a per-group basis to be particularly useful, as it
allows us to relax the cooldown requirement for our own (first-party) dependencies while keeping
it in place for most third-party dependencies.

* We maintain social connections with many of our upstream dependencies, and we perform both regular
and security contributions with them (including fixes to their own CI/CD and release processes).
For example, here's arecent contribution we made to apache/opendal-reqsignto help them ratchet
down their CI/CD security.
* Separately, we maintain social connections withadjacentprojects and working groups in the
ecosystem, including thePython Packaging Authorityand thePython Security Response Team.
These connections have proven invaluable for sharing information, such as when a report against
pip also affects uv (or vice versa), or when a security release for CPython will require a release
ofpython-build-standalone.
* We're conservative about addingnewdependencies, and we look toeliminatedependencies where
practical and minimally disruptive to our users. Over the coming release cycles, we hope to remove
some dependencies related to support for rarely used compression schemes, as part of a larger
effort to align ourselves with Python packaging standards.
* More generally, we're also conservative aboutwhatour dependencies bring in: we try to avoid
dependencies that introduce binary blobs, and we carefully review our dependencies' features to
disable functionality that we don't need or desire.
* Finally, we contribute financially (in the form of ourOSS Fund) to the sustainability of
projects that we depend on or that push the OSS ecosystem as a whole forwards.

## Concluding thoughts#

Open source security is a hard problem, in part because it's really many problems (some technical,
some social) masquerading as one. We've covered many of the techniques we use to tackle this
problem, but this post is by no means an exhaustive list. It's also not astaticlist: attackers
are dynamic participants in the security process, and defenses necessarily evolve in response to
their changing techniques.

With that in mind, we'd like to recall some of the points mentioned above that deserve the most
attention:

* Respect the limits of CI/CD: it's extremely tempting to do everything in CI/CD, but there are
some things that CI/CD (and particularly GitHub Actions) just can't do securely. For these things,
it's often better to forgo them entirely, or isolate them outside of CI/CD with a GitHub App or
similar.With that said, it's important to notovercorrectand throw CI/CD away entirely: as mentioned
above, CI/CD is a critical part of our security posture and probably yours too! It's unfortunate
that securing GitHub Actions is so difficult, but we consider it worth the effort relative to the
velocity and security risks that would come with not using hosted CI/CD at all.In particular, westrongly recommendusing CI/CD for release processes, rather than relying on
local developer machines,particularlywhen those release processes can be secured with misuse-
and disclosure-resistant credential schemes like Trusted Publishing.
* Isolate and eliminate long-lived credentials: the single most common form of post-compromise
spread is the abuse of long-lived credentials. Wherever possible, eliminate these credentials
entirely (for example, with Trusted Publishing or other OIDC-based authentication mechanisms).Where elimination isn't possible,isolatethese credentials to the smallest possible scope: put
them in specific deployment environments with additional activation requirements, and only issue
credentials with the minimum necessary permissions to accomplish a given task.
* Strengthen release processes: if you're on GitHub, use deployment environments, approvals, tag
and branch rulesets, and immutable releases to reduce the degrees of freedom the attacker has in
the event of an account takeover or repository compromise.
* Maintain awareness of your dependencies: maintaining awareness of the overall health of your
dependency tree is critical to understanding your own risk profile. Use both tools and elbow
grease to keep your dependencies secure,andto help them keep their own processes and
dependencies secure too.

Finally, we're still evaluating many of the techniques mentioned above, and will almost certainly be
tweaking (and strengthening) them over the coming weeks and months as we learn more about their
limitations and how they interact with our development processes. That's to say that this post
represents a point in time, not the final word on how we think about security for our open source
tools.

## Footnotes#

1. PyPI allows files to be uploaded with attestations, perPEP 740. However, we don't currently upload our
attestations to PyPI because of some incompatibilities between PyPI's implementation of Trusted
Publishing and the identities we use for our attestations. We hope to resolve these
incompatibilities in the near future.↩
2. It's worth noting that the installer is served from the same host as the releases themselves, so
a user who doescurl ... | bashdirectly doesn't benefit substantially from checksums within
the installer itself. However, checksums in the installer scriptdobenefit users who wish to
vendor our installer script elsewhere, e.g. into their own build or CI/CD processes.↩
