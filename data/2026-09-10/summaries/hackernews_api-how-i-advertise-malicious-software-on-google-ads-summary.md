---
title: How I advertise malicious software on Google Ads
url: https://xlii.space/eng/malicious-software-on-google-ads/
date: 2026-09-09
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-10T07:22:00.176545
---

# How I advertise malicious software on Google Ads

# How I advertise malicious software on Google Ads

## Background
- I created **RACE**, a native macOS terminal multiplexer written in Rust, with a static website (race-term.com) hosted on Cloudflare.
- The app is signed, notarized, and manages terminal processes, allowing background shells to persist after the UI closes.
- I launched a Google Ads campaign spending $500 to promote the tool.

## Google Ads suspension
- Google suspended my Ads account labeling it as “Malicious software” and “Compromised Site”.
- No specific reason or evidence was given; the appeal process repeatedly rejected my submissions.
- The suspension prevented any further advertising and left the account blocked for a week after each appeal.

## Security verification I performed
- **Google Safe Browsing**: no issues reported for the download URL.
- **VirusTotal**: the DMG file scanned clean.
- **Signatures**: application signatures verified as valid and clean.
- **JavaScript assets**: reviewed source and bundles; no malicious or obfuscated code found.
- **Google Search Console**: both domains showed no security issues.
- **Application behavior**: documented subprocess‑management; not hidden or malicious; users can configure alternative multiplexers.

## Checklist of checks
1. Confirmed Safe Browsing status for both domains.
2. Reviewed Security Issues in Google Search Console for each domain.
3. Scanned the distributed DMG with VirusTotal – clean.
4. Verified file signatures, notarization, JavaScript output, Cloudflare logs, and accessibility across user agents.
5. Tested a version (1.0.39) that performs a cleanup of background processes after deletion; still received the same suspension.

## Appeal outcome
- Multiple appeals submitted with the above evidence were all rejected.
- Google suggested deleting the account if no resolution could be found and pointed to EU redress options, but gave no concrete explanation.

## Current situation and next steps
- The suspension appears to be a false positive, possibly triggered by the legitimate background‑process behavior of a terminal multiplexer.
- I am considering continued appeals, pursuing an EU court case, or abandoning the advertising route altogether.
- The incident highlights a catch‑22: no clear guidance from Google and no way to prove compliance beyond the provided security checks.