---
title: Robin Candau | Arch Linux now has a bit-for-bit reproducible Docker image
url: https://antiz.fr/blog/archlinux-now-has-a-reproducible-docker-image/
site_name: hnrss
content_file: hnrss-robin-candau-arch-linux-now-has-a-bit-for-bit-repr
fetched_at: '2026-04-24T06:00:53.675432'
original_url: https://antiz.fr/blog/archlinux-now-has-a-reproducible-docker-image/
author: Robin Candau
date: '2026-04-23'
published_date: '2026-04-21T22:30:00+02:00'
description: Linux system & DevOps engineer passionate about skateboarding, music, cycling and, obviously, Linux!
tags:
- hackernews
- hnrss
---

# Arch Linux Now Has a Bit-for-Bit Reproducible Docker Image

* Tue, Apr 21, 2026
* 3-minute read

As a follow-up to thesimilar milestone reached for our WSL image a few months ago, I’m happy to share that Arch Linux now has a bit-for-bit reproducible Docker image!

This bit-for-bit reproducible image is distributed under a new“repro” tag.The reason for this is due to onenoticeablecaveat: to ensure reproducibility, the pacman keys have to be stripped from the image, meaning that pacman is not usableout of the boxin this image. While waiting to find a suitable solution to this technical constraint, we are therefore providing this reproducible image under a dedicated tag as a first milestone.

In practice, that means that users will need to (re)generate the pacman keyring in the container before being able to install and update packages viapacman, by running:pacman-key --init && pacman-key --populate archlinux(whether interactively at first start or from aRUNstatement in a Dockerfile if using this image as base).Distrobox users can run this as a pre-init hook:distrobox create -n arch-repro -i docker.io/archlinux/archlinux:repro --pre-init-hooks "pacman-key --init && pacman-key --populate archlinux"

The bit-for-bit reproducibility of the image is confirmed by digest equality across builds (viapodman inspect --format '{{.Digest}}' <image>) and by usingdiffocito compare builds.Documentation to reproduce this Docker image is availablehere.

Building the base rootFS for the Docker image in a deterministic way was the main challenge, but it reusesthe same process as for our WSL image(as both share the same rootFS build system).

The main Docker-specific adjustments include (see also the relateddiffocireports):

* SetSOURCE_DATE_EPOCHand honor it in theorg.opencontainers.image.createdLABEL in the Dockerfile

TYPE NAME INPUT-0 INPUT-1

Cfg ctx:/config/config ? ?

* Remove the ldconfig auxiliary cache file (which introduces non-determinism) from the built image in the Dockerfile:

TYPE NAME INPUT-0 INPUT-1

File var/cache/ldconfig/aux-cache 656b08db599dbbd9eb0ec663172392023285ed6598f74a55326a3d95cdd5f5d0 ffee92304701425a85c2aff3ade5668e64bf0cc381cfe0a5cd3c0f4935114195

* Normalize timestamps duringdocker build/podman buildusing the--source-date-epoch=$SOURCE_DATE_EPOCHand--rewrite-timestampoptions:

TYPE NAME INPUT-0 INPUT-1

File etc/ 2026-03-31 07:57:46 +0000 UTC 2026-03-31 07:59:21 +0000 UTC

File etc/ld.so.cache 2026-03-31 07:57:46 +0000 UTC 2026-03-31 07:59:21 +0000 UTC

File etc/os-release 2026-03-31 07:57:46 +0000 UTC 2026-03-31 07:59:21 +0000 UTC

File sys/ 2026-03-31 07:57:46 +0000 UTC 2026-03-31 07:59:21 +0000 UTC

File var/cache/ 2026-03-31 07:57:46 +0000 UTC 2026-03-31 07:59:21 +0000 UTC

File var/cache/ldconfig/ 2026-03-31 07:57:46 +0000 UTC 2026-03-31 07:59:21 +0000 UTC

File proc/ 2026-03-31 07:57:46 +0000 UTC 2026-03-31 07:59:21 +0000 UTC

File dev/ 2026-03-31 07:57:46 +0000 UTC 2026-03-31 07:59:21 +0000 UTC

You can checkthe related change set in our archlinux-docker repositoryfor more details.Thanks toMarkfor his help on that front!

This represents yet another meaningful achievement regarding our general “reproducible builds” efforts and I’m already looking forward to the next step! 🤗

For what it’s worth, I’m eventually considering setting up a rebuilder for this Docker image (as well as forthe WSL imageand future eventual reproducible images) on my server in order to periodically / automatically rebuild the latest image available, verify it’s reproducibility status and share build logs / results publicly somewhere (if I find the time to get to it 👼).