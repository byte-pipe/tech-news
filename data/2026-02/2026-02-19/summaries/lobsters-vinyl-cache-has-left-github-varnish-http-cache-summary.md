---
title: Vinyl Cache has left github — Varnish HTTP Cache
url: https://vinyl-cache.org/organization/moving.html
date: 2026-02-19
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-19T06:04:20.478965
---

# Vinyl Cache has left github — Varnish HTTP Cache

# Vinyl Cache has left github

## … what you need to do

The Vinyl Cache project has moved to a self-hosted forge instance at https://code.vinyl-cache.org/vinyl-cache/. Interested collaborators can register an account via this link, which expires on 2026-03-20. Existing accounts should remain functional unless spam issues necessitate further registration closure. Users experiencing email confirmation issues should check their spam folders.

## About the new forge

The new forge has a dedicated website for more information and issue reporting: <https://code.vinyl-cache.org/vinyl-cache/code.vinyl-cache.org>.

## Location mapping old/new

The following URL translations exist for accessing the project:
* The prefix changes from `https://github.com/varnishcache/` to `https://code.vinyl-cache.org/vinyl-cache/`.
* "varnish" in the project name is replaced with "vinyl".
* The main/trunk branch is now named "main".

A bash script is provided to automate these changes within a Git directory. Git clone URLs and SSH access have also been updated accordingly. Some repositories may be archived in the future.

## Changing your git settings

A bash script is available to automate the update of the Git origin and main branch. Users should run this script within a Git directory, adjusting the `origin=origin` line if their primary origin is named differently.

## What is happening after the forge migration?

The project is currently focused on restoring tooling like VTest and automated website updates. Mirror repositories providing read-only access will be added later and announced on https://vinyl-cache.org.

## Mini-Retro: What we did

The project migrated repositories from GitHub to the new forge one by one. This involved tagging repositories, adding migration notes to README files, updating build scripts to point to the README, archiving the GitHub repositories, migrating the code, and then opening the repositories on the new forge.

## What went wrong

During the migration, some README changes were incorrect, requiring re-archiving and re-archiving on GitHub. A specific issue arose with the migration of the main `vinyl-cache` repository, where renaming the master branch caused pull requests based on master to become invalid. This was resolved by directly fixing the issue at the SQL level.
