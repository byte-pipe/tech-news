---
title: "I don't like passkeys | Ethan Hawksley"
url: https://hawksley.dev/blog/i-dont-like-passkeys
date: 2026-09-18
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-19T06:01:17.128013
---

# I don't like passkeys | Ethan Hawksley

# I don't like passkeys | Ethan Hawksley

## Overview
- Passkeys are promoted by big tech as the ultimate login method, but the author finds them unsuitable for personal use.  
- While they improve security against phishing and data breaches, they introduce higher risks of permanent lockout, device loss, and account bans.

## Benefits of passkeys
- Tied to the specific site, preventing credential theft via phishing.  
- Asymmetric cryptography means server‑side breaches cannot reveal the secret.  
- Ideal for corporate environments where device management is controlled.

## Risks for individuals
- Permanent account lockout if recovery methods (SMS, email, security questions) are weak or missing.  
- Loss of a device or hardware key can make all accounts inaccessible.  
- Reliance on a single recovery path creates a false sense of security.

## Hardware keys
- Passkeys cannot be backed up to a hardware key; they can only be added or deleted.  
- Users must buy multiple keys and enroll each one for every site, which becomes costly as accounts grow.  
- Discoverable credentials have limits (≈25‑100 accounts per key, up to 300 on premium models); exceeding limits forces deletion or purchase of more keys.

## Synced passkeys
- Apple and Google tie passkeys to their OS accounts, offering a “happy path” for synced management.  
- If the provider bans the user’s account, all synced passkeys are lost irreversibly.  
- Exporting passkeys is still fragmented; passwords remain easier to copy and move manually.

## Third‑party synced passkeys
- Password managers (e.g., Bitwarden, KeePassXC) can store passkeys via new OS APIs, but the experience is inconsistent.  
- Autofill in browsers and native apps lacks the polish of long‑standing password solutions.  
- The author expects third‑party solutions to improve, but they are not ready today.

## When passkeys don’t work
- Using a colleague’s computer is cumbersome: hardware ports may be unavailable, trusting a synced device is risky, and “Hybrid Transport” (QR + Bluetooth) often fails.  
- These edge cases make passkeys impractical for occasional or shared device access.

## Conclusion
- Enterprise users have solid reasons to adopt passkeys, but the current ecosystem is immature for everyday individuals.  
- The lockout and recovery risks outweigh the phishing protection for most users.  
- A combination of strong, randomly generated passwords stored in a third‑party password manager plus an independent TOTP app offers better control and flexibility.  
- For users who previously reused passwords, passkeys are an improvement; for everyone else, they represent a step backward.