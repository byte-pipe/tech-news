---
title: Cool down before you install: give new gems a few days to be vetted - RubyGems Blog
url: https://blog.rubygems.org/2026/06/03/cooldown-let-new-gems-be-vetted.html
date: 2026-06-03
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-06T11:51:40.157751
---

# Cool down before you install: give new gems a few days to be vetted - RubyGems Blog

# Cool down before you install: give new gems a few days to be vetted

## Overview
- Supply‑chain attacks on RubyGems often exploit a narrow window where a compromised account publishes a malicious version that is immediately installed.
- Bundler 4.0.13 introduces **cooldown**, a time‑based filter that refuses to resolve a gem version until it has been publicly available for at least *N* days.
- The feature is opt‑in, works alongside existing defenses (2FA, trusted publishing), and only blocks versions it can prove are too new.

## How Cooldown Works
- Reads the `created_at` timestamp from RubyGems.org’s v2 compact index.
- Versions without a reliable `created_at` (old servers, pre‑v2 entries, private registries on v1) are treated as outside the window and remain resolvable.
- Never blocks silently; it simply skips versions that are younger than the configured window.

## Getting Started
1. Update Bundler to 4.0.13 (or later) and pin the version in the lockfile.  
   ```bash
   gem update --system          # or gem install bundler -v 4.0.13
   bundle update --bundler=4.0.13
   ```
2. Declare a cooldown in the `Gemfile` for the source you want to protect:
   ```ruby
   source "https://rubygems.org", cooldown: 7

   gem "rails"
   gem "puma"
   ```
3. Run `bundle install` (no lockfile) or `bundle update` (re‑resolve) to apply the filter. Existing `Gemfile.lock` files are left untouched.

## Configuration Options
- **Per‑source keyword** (as shown above) – applies only to that source.
- **Project‑level config**: `bundle config set cooldown 7` (stores in `.bundle/config`).
- **Global config**: `bundle config set --global cooldown 7`.
- **Environment variable**: `BUNDLE_COOLDOWN=7 bundle install`.
- **Command‑line flag**: `bundle install --cooldown 7` (overrides all other settings).

Precedence (highest to lowest): command‑line flag → environment variable → global/project config → per‑source keyword.

## Mixing Sources
- Use different cooldown values per registry:
  ```ruby
  source "https://rubygems.org", cooldown: 7
  source "https://gems.internal.example.com", cooldown: 0 do
    gem "internal-tool"
  end
  ```
- A `--cooldown` flag of `0` disables the filter for that run, even for exempted sources.

## Escape Hatch
- Setting the cooldown to `0` forces Bundler to consider the newest versions, useful for urgent security patches:
  ```bash
  bundle install --cooldown 0
  BUNDLE_COOLDOWN=0 bundle update rails
  ```

## Seeing What Is Held Back
- `bundle outdated --cooldown 7` marks newer versions that are still within the cooldown window and shows the remaining days, e.g.:
  ```
  aws-partitions 1.1251.0 1.1256.0 (cooldown 3d) = 1.1251.0 default
  ```

## Cooldown in the Wider Security Landscape
- Complements other RubyGems.org defenses:
  - Content validation at push time.
  - Password breach checks via “Have I Been Pwned”.
  - AI‑assisted vulnerability scanning (Alpha Omega, Anthropic).
  - Mandatory 2FA and trusted publishing.
- Relies on the v2 compact index’s `created_at` timestamps, made possible by a careful dual‑write migration on RubyGems.org.
- Together, these layers reduce the attack surface for Ruby projects; using RubyGems.org as the primary source remains the safest default.