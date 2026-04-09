---
title: How NixOS is built
url: https://blog.erethon.com/blog/2025/07/31/how-nixos-is-built/
site_name: lobsters
fetched_at: '2025-08-02T23:07:44.574502'
original_url: https://blog.erethon.com/blog/2025/07/31/how-nixos-is-built/
author: Dionysis Grigoropoulos
date: '2025-08-02'
tags: nix
---

# How NixOS is built

 Jul 31, 2025


I recently got the urge to better understand how NixOS is built and how secure
the build pipeline is. So, I started looking at all the build systems involved,
the infrastructure they run on, how everything is managed and which build jobs
are running in these systems. This is my attempt at documenting the above.Table of contents:## Repos and infrastructureI'll focus on two main repositories,NixOS/nixpkgsandNixOS/infra. Nixpkgs is
the main repository where all the packages and modules of NixOS are defined,
while infra is the repository that specifies most of the infrastructure used by
the NixOS foundation.Anyone with a GitHub account can contribute to Nixpkgs, there are no special
groups one needs to belong in to open a PR. There are about200 committerscurrently with access to merge PRs.The infra repository contains Terraform/OpenTofu files that define the cloud
infrastructure used and nix expressions for configuring the hosts. The two main
cloud services used in infra are AWS S3 for object storage and Fastly that acts
as a CDN and a cache for the S3 buckets. Again, anyone can contribute to the
infra repository, but it's generally managed by theInfra team.## Getting the NixOS ISOLet's start from the beginning of a user's journey to installing NixOS. We first
need to download the NixOS ISO, so we visit thedownload page, scroll to the
bottom of the page and find the link for the ISO. Right now this is:https://channels.nixos.org/nixos-25.05/latest-nixos-minimal-x86_64-linux.iso.What is thischannels.nixos.orgwebsite and where is it defined and configured?### Defining domains, S3 buckets and CDN#### DomainsWe can usedigto figure out where the nixos.orgnameserversare hosted.$ dig NS nixos.org +shortns-61-b.gandi.net.ns-161-c.gandi.net.ns-177-a.gandi.net.Turns out they're hosted ongandi.net. Let's move on to see where this is
defined.On NixOS/infra there's adnsdirectory with aflake-module.nixin it, where we
see thatDNSControlis used to configure domains. Looking atcreds.jsonthere's
an entry to setup Gandi credentials which matches what we discovered
earlier. Furthermore, atdnsconfig.jswe include four more files, one for each
of the following domains:nixcon.orgnix.devnixos.orgofborg.orgFollowing this breadcrumb, we arrive atdns/nixos.orgwherechannels.nixos.orgis defined as aCNAMEto a Fastly domain. The exact same setup is used forcache.nixos.org, the NixOS binary cache from where users download prebuilt
binaries.#### S3 buckets and CDNIninfra/terraformwe find the Terraform files for managing the S3 buckets and
the Fastly CDN setup. Forchannelsin particular, wedefine a S3 bucketwith a
website endpoint enabled which we can view innix-channels.s3-website-us-east-1.amazonaws.com.Further down the file, there's adefinition for a Fastly Servicewhich uses the
public website endpoint of thebucket as a backend. Again, we have asimilar
setupforcache.nixos.org.To recap,channels.nixos.orgpoints to Fastly which caches responses and acts
as a global CDN, which in turn uses an AWS S3 bucket as the source for channels
and packages.## Building the packagesNow that we know the flow for getting the iso and packages, let's figure out how
they're built in the first place.### Nixpkgs and GitHub ActionsAs mentioned previously, Nixpkgs is the main repository where packages and NixOS
modules are defined and built from. In order for a package to be available viacache.nixos.orgit must first be added to Nixpkgs. Nixpkgs has a lot of
automated checks that prevent common problems, help with organizing Pull
Requests (PRs) and Issues and generally make the life of contributors and
reviewers easier.The actions are defined innixpkgs/.github/workflows. One thing that is
interesting to note is that almost all actions run on an ARM build of Ubuntu
24.04 and just install Nix as one of their steps, they don't run on NixOS
itself. I assume we're running on ARM because it's about two thirds of the price
of running on x86-64 according toGitHub pricing.The monthly cost for all the
actions in July of 2025 came out to a bitover 14500 USDwhich GitHub covers in
its entirety.Some actions run on a periodic schedule, while others run each time someone
opens or updates a PR.#### Periodic actionsThere are two main actions that run on a schedule. The first one isperiodic
mergeswhich merges the master branch into staging every few hours. The other
one islabelswhich runs every ten minutes and automatically applies labels to
PRs and issues viathis script.#### Pull Request actionsEvery time someone opens a new pull request or a pull request is updated, some
actions run. In particular these actions revolve around different areas of the
PR, from linting or building the code changes to applying labels and pinging the
maintainers of a package to get a review.Thelint workflowlints the changes and also callsnixpkgs-vetwhich is a
software specifically made to enforceNixOS RFC 140.Eval, as the name suggests, evaluates the derivations (in all supported
systems),
calculates some statistics for later use and verifies things still
evaluate. These statistics might include what paths were added or changed in a
PR. UsingPR #429664as an example, we get the following artifact out of the
diff between the PR and the previous master branch for x86_64.{"added": [],"changed": ["python312Packages.llm-ollama.x86_64-linux","python313Packages.llm-ollama.x86_64-linux","release-checks"],"removed": []}This information is later used by the previously mentioned labels workflow to
add related labels to a PR.Build, as the name suggests, buildsdocs,shell,lib,tarballbut
doesn't actually build the package. A point of interest here is the fact that
the build actionuses Cachix, ahosted Nix binary cache. This cache is only
meant to be used by the Nixpkgs CI and shouldn't be trusted.Reviewersfigures out which contributors should get a ping to review the PR.### Nixpkgs and OfBorgYou might have noticed that we never actually build any packages or ran any
NixOS VM tests in the GitHub Actions previously. This is because these actions
happen on a different system,OfBorg. The namecomes from Star Trek.OfBorg automatically builds any PRs thatfollow a certain naming
schemeor you cantrigger builds/tests/evals manually. The results of these
actions then get reported back to GitHub.Up until the end of 2024,OfBorg was the main CI for Nixpkgs, however the
company was sponsoring the hosts decided to end the sponsorship. This event
triggered the creation of a big part of the previously mentioned GitHub Actions
workflows.Nowadays, the OfBorg x86-64 builders are hosted intetaneutral, while the Darwin
builders are hosted in MacStadium. The core/orchestrator service
(core01.ofborg.org) is hosted in Hetzner Cloud. There's also an adjacent
project toview build logsthat's deployed oncore01.ofborg.orgas well.The OfBorg infrastructure is managed viaofborg/ofborg-infrastructure.### HydraWhile OfBorg builds packages, runs tests and reports the results back to the
GitHub PR, it never actually signs the packages or uploads them tocache.nixos.org. Building packages that are meant to end up in the official
cache requires trusted hardware that only a few people have access to. This is
the role ofhydra.nixos.org.Hydrais yet another CI service for Nix based projects. It's written in Perl and
supports a typical CI architecture with multiple job runners. I believe it was
the first CI system for Nix, the initial commit was on the 10th of October 2008!Similarly with OfBorg, the Hydra builders had to quickly be scrapped and
recreated at the end of 2024. Nowadays, the builders and the machine that hosts
the actual Hydra application areHetzner dedicated machines. You can see a list
of all the current and past buildershere.Hydra only builds packagesaftera PR has been reviewed and merged.#### Projects, jobsets and jobsBuilds in Hydra are organized in the following structure:Project -> Jobset -> JobTo get back to the initial question of how the ISO is built, let's look at theNixOS project. We have a jobset for each release (release-25.05, staging,
unstable-small, etc). Next, if we search for iso there's a job callednixos_iso_minimal. Theconfigurationof the `release-25.05` jobset callsnixos/release-combined.nixfrom Nixpkgs.This nix file specifies all the jobs that Hydra should build for this
jobset. One of these jobs isnixos.iso_minimal, which is our entry point for
building the ISO.Similarly, for Nixpkgs there's a Nixpkgs project with a jobset calledtrunkthat builds the latest committed version of a package.#### Signing and uploading to cache.nixos.orgAnything that Hydra builds is signed and uploaded to the S3 bucket forcache.nixos.org.We can verify this by querying the cache. This is thelatest buildof a package
I maintain. On the details tabs we see:Output store paths/nix/store/zi6ypq21r8534cx53bx8rx930k749xs8-python3.13-llm-ollama-0.12.0-dist,/nix/store/clz5dsk4cxsakbw9zw634riwhpjwhjk7-python3.13-llm-ollama-0.12.0Let's query the cache for the narinfo file of this build:$ curl https://cache.nixos.org/clz5dsk4cxsakbw9zw634riwhpjwhjk7.narinfoStorePath: /nix/store/clz5dsk4cxsakbw9zw634riwhpjwhjk7-python3.13-llm-ollama-0.12.0URL: nar/0xpnlv3q605ljcid91kn72awipjh58x9f3iaqrj1d662q9m3gvh3.nar.xzCompression: xzFileHash: sha256:0xpnlv3q605ljcid91kn72awipjh58x9f3iaqrj1d662q9m3gvh3FileSize: 22620NarHash: sha256:10g4imc7s0yhlx042ly44pfr98z1kjc5j3g7p74n1ani0zp36hb0NarSize: 102152References: 9yh9ak97gn659bk4d3n411fx6c0ng7s2-python3-3.13.5 clz5dsk4cxsakbw9zw634riwhpjwhjk7-python3.13-llm-ollama-0.12.0 dz5gpk4mxg7hhyxcnb5jg6696an7hlrn-python3.13-ollama-0.5.1 r48mlzgpdzj04lyq17hbn4nw5y85wnzl-python3.13-llm-0.26 wa8b4x0vsvxz1dvgwnm9gdwhvba7ka70-python3.13-pydantic-2.11.7 zbzpxnsm8j0rqakmdvsrf36zh28xick2-python3.13-click-8.1.8Deriver: 06ni1ca50ndxh2pgxy0kznbyv07pxmyr-python3.13-llm-ollama-0.12.0.drvSig: cache.nixos.org-1:5FnqydQlPAWi9bVeDoN2MVxzHiez0CV43SIpjdKIo0SEwCmNXoiTq+snEOYwGHOfI/OEqtaMXu2kcHqR4kEaCw==The signing and uploading to the cache behaviour is configured innixos/infra.My understanding is that builds of Hydra started getting signed inJune of
2015. Moreover, the key haslikely never been rotated before! There is an
ongoingeffortto support multiple key signatures at the same time and rotate
the old key.#### My security fearsI don't mind Perl that much, but I think Hydra shows its age since it's littered
with practices that today are considered antipatterns. A simple example, here's
aremote endpointthat shells out to git. If thatdie()line that validates
the two revs was missing, it would be a command injection vector. This pattern
can be seen all over Hydra.It took me a couple of hours to find a (minor?) security issue in Hydra when I
started looking. I reported it upstream, but it was already reported by someone
else. I think it will be out of embargo towards the end of August.## ConclusionI believe this is the complete flow for how NixOS is built. Nixpkgs is the
source of truth for packages and modules, GitHub Actions and OfBorg help with
catching errors and automation, Hydra is the authoritative builder that has the
keys to the kingdom.Hydra is definitely the scariest part of the whole pipeline for me. Both the
fact that the signing key hasn't been rotated in ten years (how many people had
access to it?) and the general vibes I get from the Hydra source code are
creeping me out.Ilovethe fact that it's possible to figure out all of the above by just
looking at the code in GitHub, past issues and discourse threads. Ideally, I
would prefer if things were documented better, but I feel the need to emphasize
how transparent everything is,ifyou're willing to invest the
time. Improvements can definitely be made, but even the state we're in is a
great starting point.I'm looking forward to the next steps in this journey of better understanding
the security of NixOS. I'm sure there's a lot more things to discover.

 Tags:
 nix

 nixos

Source:GitHubComments onFediverse.
