---
title: Reddit - The heart of the internet
url: https://reddit.com/r/selfhosted/comments/1rckopd/huntarr_your_passwords_and_your_entire_arr_stacks/
date: 2026-02-25
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-25T06:01:58.015612
---

# Reddit - The heart of the internet

# Huntarr - Your passwords and your entire arr stack's API keys are exposed to anyone on your network, or worse, the internet.

A security review of Huntarr.io (v9.4.2) revealed critical authentication bypass vulnerabilities. Huntarr, which integrates with popular media management tools like Sonarr, Radarr, and Prowlarr, has zero authentication on sensitive endpoints, creating a significant security risk. Attackers can gain full control over a user's media stack by simply reaching their Huntarr instance.

## Key Findings:

* **Unauthenticated API Access:** The `/api/settings/general` endpoint allows anyone to access and modify the configuration, including API keys for integrated applications.
* **Unauthenticated 2FA Enrollment:** Attackers can enroll their own 2FA codes, leading to full account takeover without a password.
* **Unauthenticated Setup Clear:** An attacker can re-initialize the setup process and create a new owner account, replacing the legitimate one.
* **Unauthenticated Recovery Key Generation:** Attackers can generate recovery keys without authentication, enabling account takeover.
* **Full Cross-App Credential Exposure:** A single request to write settings reveals configuration for over 10 integrated apps.
* **Unauthenticated Plex Account Unlink:** Anyone can disconnect a Plex account from Huntarr.
* **Auth Bypass on Plex Account Linking:** The server skips session checks when `setup_mode` is set to true.
* **Zip Slip Vulnerability:** User-uploaded ZIP files are extracted without filename sanitization, posing a risk due to the container running as root.
* **Path Traversal Vulnerability:** User-supplied input in backup restore/delete operations can lead to arbitrary file deletion.
* **Local Access Bypass:** Trusting forwarded headers allows bypassing security measures and accessing protected endpoints.

## Developer Response and Process:

The maintainer claims to have implemented security checks and hardening, but these are not reflected in the code. The project lacks a code review process, with frequent commits and no second pair of eyes on changes. The maintainer cited budget constraints as a reason for the lack of security measures, but this is disputed.

## Concerns and Next Steps:

The maintainer censors security reports and bans users who raise concerns. The project's README includes a donation appeal, which is viewed as a red flag given the security vulnerabilities. The maintainer is likely to dismiss these findings, but the underlying issues with the development process need to be addressed to prevent future vulnerabilities.

## Proof of Vulnerabilities:

A proof-of-concept repository with automated CI is available, demonstrating each vulnerability. The maintainer's claim of cybersecurity expertise is questioned given the severity and prevalence of these vulnerabilities.
