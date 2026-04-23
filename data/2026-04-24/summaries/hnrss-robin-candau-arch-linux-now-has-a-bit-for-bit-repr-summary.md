---
title: Robin Candau | Arch Linux now has a bit-for-bit reproducible Docker image
url: https://antiz.fr/blog/archlinux-now-has-a-reproducible-docker-image/
date: 2026-04-23
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-24T06:03:16.535535
---

# Robin Candau | Arch Linux now has a bit-for-bit reproducible Docker image

# Arch Linux Now Has a Bit‑for‑Bit Reproducible Docker Image

## Overview
- The new Docker image is tagged **repro** to indicate its reproducibility.
- Pacman keys are stripped from the image, so pacman cannot be used until the keyring is regenerated inside the container.

## How to Use
- Initialise the pacman keyring after starting the container:  
  `pacman-key --init && pacman-key --populate archlinux`
- For Dockerfile usage, add the command in a RUN statement.
- Distrobox users can apply it as a pre‑init hook:  
  `distrobox create -n arch-repro -i docker.io/archlinux/archlinux:repro --pre-init-hooks "pacman-key --init && pacman-key --populate archlinux"`

## Reproducibility Verification
- Digest equality across builds can be checked with:  
  `podman inspect --format '{{.Digest}}' <image>`
- Differences between builds are examined using `diffoci`.

## Build Process Highlights
- The deterministic rootFS build mirrors the process used for the Arch Linux WSL image.
- Docker‑specific adjustments include:
  - Setting `SOURCE_DATE_EPOCH` and reflecting it in `org.opencontainers.image.created` label.
  - Removing the `ldconfig` auxiliary cache file to eliminate nondeterminism.
  - Normalising timestamps during build with `--source-date-epoch=$SOURCE_DATE_EPOCH` and `--rewrite-timestamp` options.

## Documentation & Sources
- Full documentation for reproducing the image is linked in the article.
- Change set details are available in the `archlinux-docker` repository; special thanks to Mark for his contributions.

## Future Plans
- The author intends to set up an automated rebuilder that periodically rebuilds the image, verifies reproducibility, and publishes build logs and results.