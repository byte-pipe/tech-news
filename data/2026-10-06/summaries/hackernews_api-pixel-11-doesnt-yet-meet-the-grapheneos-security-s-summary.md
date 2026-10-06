---
title: "Pixel 11 doesn't yet meet the GrapheneOS security standards and may be skipped - GrapheneOS Discussion Forum"
url: https://discuss.grapheneos.org/d/41564-pixel-11-doesnt-yet-meet-the-grapheneos-security-standards-and-may-be-skipped
date: 2026-10-06
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-06T16:49:40.620781
---

# Pixel 11 doesn't yet meet the GrapheneOS security standards and may be skipped - GrapheneOS Discussion Forum

# Pixel 11 doesn't yet meet the GrapheneOS security standards and may be skipped

## Main announcement (GrapheneOS)

- A partial GrapheneOS port to the Pixel 11 series was created after a week of work, but it cannot be completed because ARM hardware memory tagging (MTE) is not supported in the device’s software, firmware, and likely hardware.  
- MTE is a core security feature for GrapheneOS; it is used throughout the base OS, including the kernel and all standard processes, and is only temporarily disabled for a few device‑specific processes.  
- Pixel 8 launched with hardware MTE support in October 2023. GrapheneOS integrated MTE into its hardened_malloc project and the OS later that month, while Android and Pixel OS never enabled it by default (Android 16 AAPM enables it for a few processes).  
- Apple’s Memory Integrity Enforcement (MIE) on the iPhone 17 is an always‑on, high‑quality implementation of MTE, used in the kernel and many user processes.  
- Unlike iOS and Android, GrapheneOS forces MTE for most user‑installed apps, offering a per‑app opt‑out toggle for incompatibilities.  
- Pixel 11 adds post‑quantum verified boot (ML‑DSA) and a Titan M3 chip, improving pre‑first‑unlock (BFU) security, but the loss of MTE represents a major security regression.  
- Compared with the Snapdragon 8 Elite Gen 5, the Pixel 11’s CPU, GPU, and cellular radio are weaker (≈40 % lower single‑thread CPU, 80 % lower multi‑thread, >100 % lower GPU performance) and the Snapdragon chip includes MTE.  
- Pixel support was removed from AOSP with Android 16, making Pixel devices harder to maintain; progress toward open‑source firmware and driver libraries has been lost.  
- GrapheneOS delivers AOSP and kernel patches earlier than stock Pixel OS, but still depends on Google for firmware and driver updates; a partnership with Motorola could improve this situation.  
- Recommendation: do **not** buy Pixel 11 devices. Pixels 8‑10 provide better overall security for GrapheneOS, and Pixel 10 is cheaper with similar hardware and MTE. Pixel 11’s Titan M3 improves BFU security only for users without strong passphrases, while the missing MTE weakens AFU security.  
- The team is undecided but may skip the Pixel 11 series entirely and shift focus to upcoming Motorola devices. Hope remains that a future Pixel 11a will match the Pixel 10a (10th‑gen hardware) and include MTE.

## Selected community responses

- **AtmosphericIgnition**: asks how to determine if MTE hardware is physically present or merely disabled by firmware.  
- **MetropleX**: confirms the lack of MTE support across software, firmware, and likely hardware.  
- **alonely0**: prefers retaining Pixel support despite missing MTE, arguing other GrapheneOS benefits still apply.  
- **Sonic**: stresses that GrapheneOS must not compromise on security; without MTE the Pixel 11 should not be supported.  
- **ClickClickDrone**: reiterates that MTE is a minimum requirement for future GrapheneOS support.  
- **deltuzirtu**: suggests focusing development on Motorola devices instead.  
- Other users express disappointment, discuss the potential Pixel 11a, and share personal experiences with MTE on their devices.

## Conclusions

- MTE is treated as a non‑negotiable security requirement for GrapheneOS.  
- The Pixel 11 series lacks reliable MTE support, making it a security downgrade compared to earlier Pixels.  
- The project may skip the Pixel 11 line and prioritize Motorola hardware where MTE is available.  
- Users seeking a secure GrapheneOS experience are advised to choose Pixel 8‑10 models or wait for supported Motorola devices.