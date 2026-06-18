---
title: AMD silently removes memory encryption from consumer Ryzen CPUs, leaving users unaware that they may be vulnerable — security feature vanishes after n...
url: https://www.tomshardware.com/pc-components/cpus/amd-silently-removes-memory-encryption-from-consumer-ryzen-cpus-leaving-users-unaware-that-they-may-be-vulnerable-security-feature-vanishes-after-newer-agesa-firmware-amd-engineers-go-radio-silent-when-pressed-about-the-change
date: 2026-06-18
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-19T01:19:08.244579
---

# AMD silently removes memory encryption from consumer Ryzen CPUs, leaving users unaware that they may be vulnerable — security feature vanishes after n...

# AMD silently removes memory encryption from consumer Ryzen CPUs, leaving users unaware that they may be vulnerable

## Background
- Transparent Secure Memory Encryption (TSME) encrypts all RAM at firmware level, protecting against physical attacks such as cold‑boot, DRAM snooping, and memory module removal.  
- Initially launched on high‑end AMD CPUs, the feature was later extended to lower‑end consumer Ryzen processors and became an assumed part of the chip package.  
- AMD distinguishes TSME from Secure Memory Encryption (SME); SME is OS‑managed and limited to PRO/EPYC tiers, while TSME is firmware‑managed and works transparently when enabled in BIOS.

## Discovery
- Ars Technica reported that TSME disappeared from consumer Ryzen CPUs after a firmware update.  
- The investigation, tracked on GitHub, was led by Linux hobbyist Ben Kilpatrick, who noticed that Host Security ID (HSI) flagged TSME as “not supported” on a Ryzen 7 9700X despite the BIOS setting being enabled.  
- Kilpatrick contacted MSI (motherboard maker) and filed a bug on AMD’s public engineering GitHub repository, prompting responses from AMD engineers Tom Lendacky and Mario Limonciello.

## Findings
- Tests by MSI showed TSME was functional under older AGESA firmware but reported “not supported” under AGESA 1.2.7.0 on consumer chips; Pro CPUs retained support regardless of firmware.  
- An internal AGESA flag controlling TSME activation returned FALSE for consumer parts and TRUE for Pro parts when the BIOS option was enabled.  
- The removal is invisible on Windows systems and requires technical effort to detect on Linux, leaving users unaware of the change.

## AMD’s Response
- AMD’s only public statement was an email confirming that TSME is “a security feature only applied to PRO CPUs as part of AMD PRO Technologies.”  
- Engineers could not provide a clear reason for the disappearance; Limonciello ended the discussion with “My apologies, but I don’t have any more information to share on this topic.”  
- No official acknowledgment, explanation, or timeline for restoring support has been given.

## Implications for Users
- For most consumer Ryzen owners, the practical impact is limited to scenarios involving physical access to the machine (theft, seizure, tampering).  
- Users who rely on full‑disk encryption, handle confidential data, or need protection against cold‑boot attacks now effectively require a Ryzen Pro, EPYC, or a system with SME support.  
- The silent removal undermines trust, as the feature was previously assumed to be part of the processor’s security suite.

## Open Questions
- Was the removal an intentional product‑segmentation decision to reserve TSME for PRO chips, or an accidental regression introduced by the newer AGESA firmware?  
- If it is a firmware bug, can AMD issue a fix to re‑enable TSME on consumer CPUs?  
- Will AMD provide clearer communication and documentation regarding the availability of memory‑encryption features across its product lines?