---
title: Bitwarden adds support for passkey login on Windows 11
url: https://www.bleepingcomputer.com/news/security/bitwarden-adds-support-for-passkey-login-on-windows-11/
site_name: tldr
content_file: tldr-bitwarden-adds-support-for-passkey-login-on-window
fetched_at: '2026-03-07T19:09:34.123745'
original_url: https://www.bleepingcomputer.com/news/security/bitwarden-adds-support-for-passkey-login-on-windows-11/
date: '2026-03-07'
description: Bitwarden announced support for logging into Windows 11 devices using passkeys stored in the manager's vault, enabling phishing-resistant authentication.
tags:
- tldr
---

# Bitwarden adds support for passkey login on Windows 11

 By

###### Bill Toulas

* March 4, 2026
* 05:34 PM
* 2

Bitwarden announced support for logging into Windows 11 devices using passkeys stored in the manager's vault, enabling phishing-resistant authentication.

The new feature is available for all plans, including the free tier, and allows logging into Windows by selecting the security key option and scanning a QR code with a mobile device to confirm access to the passkey stored in the Bitwarden encrypted vault.

Bitwarden is an open-source password and secrets manager that can store account passwords, passkeys, API keys, credit card details, identity data, and private notes.

To use the new feature, there arethree required conditions:

1. Have Entra ID–joined devices
2. FIDO2 security key sign-in is enabled
3. Have a registered Entra ID passkey stored in their Bitwarden vault

“Windows now supports industry-standard passkeys secured in the Bitwarden vault, enabling passwordless authentication during sign-in,”Bitwarden saysin a press release.

“Users can choose to log in with a passkey stored in the Bitwarden vault, allowing Windows to authenticate using cryptographic credentials rather than passwords, without transmitting shared secrets.”

Bitwarden acts as the passkey provider in the Windows authentication flow, storing the credential in the user’s synced vault rather than binding it to a single device. This also allows recovery using other devices in case of losing the phone.

More importantly, by removing password entry from the login process and using cryptographic challenges signed with private keys stored in the vault, the risk of credential exposure to phishing drops dramatically.

Bitwarden states that Microsoft will roll out passkey login on Windows this month, and it depends on the Microsoft Entra ID configuration.

In November 2025,Microsoft announcedthe introduction of a passkey provider API on Windows 11, allowing third-party apps like Bitwarden and 1Password to store and manage passkeys for websites and apps on the OS.

The latest announcement extends this further, to a more fundamental authentication layer, that of the OS itself.

## Red Report 2026: Why Ransomware Encryption Dropped 38%

Malware is getting smarter. The Red Report 2026 reveals how new threats use math to detect sandboxes and hide in plain sight.

Download our analysis of 1.1 million malicious samples to uncover the top 10 techniques and see if your security stack is blinded.

Download The Report

### Related Articles:

Bitwarden introduces ‘Cupid Vault’ for secure password sharing

Microsoft to disable NTLM by default in future Windows releases

Microsoft testing Windows 11 batch file security improvements

Microsoft expands Windows restore to more enterprise devices

Windows 11 KB5077241 update improves BitLocker, adds Sysmon tool
