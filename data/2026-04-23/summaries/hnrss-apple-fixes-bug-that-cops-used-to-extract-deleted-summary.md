---
title: Apple fixes bug that cops used to extract deleted chat messages from iPhones | TechCrunch
url: https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/
date: 2026-04-22
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-23T09:46:28.573364
---

# Apple fixes bug that cops used to extract deleted chat messages from iPhones | TechCrunch

# Apple fixes bug that cops used to extract deleted chat messages from iPhones

## Issue and fix
- Apple released an iOS/iPadOS update (iOS 18) that stops notifications of deleted messages from being retained on the device.
- The bug caused notification content to be cached for up to a month, allowing forensic tools to recover messages that users had deleted in apps like Signal.
- Apple’s security notice described the problem as “notifications marked for deletion could be unexpectedly retained on the device.”
- The fix was back‑ported to older iOS 18 versions.

## Background
- 404 Media reported that the FBI used forensic tools to retrieve deleted Signal messages from an iPhone because the message content remained in the notification database.
- Signal’s president Meredith Whittaker asked Apple to address the issue, stating that notifications for deleted messages should not persist in any OS notification database.
- The bug’s existence was confirmed after the 404 Media report; Apple has not explained why the notifications were stored initially.

## Reactions
- Privacy activists expressed alarm that the FBI could bypass a security feature meant to protect at‑risk users.
- The ability to set auto‑deletion timers in messaging apps (Signal, WhatsApp, etc.) is a key privacy safeguard, especially when devices are seized.

## Contact and author information
- For more details on forensic tools used on iPhones or Android devices, contact Lorenzo Franceschi‑Bicchierai securely via Signal (+1 917 257 1382), Telegram, or Keybase (@lorenzofb).
- Lorenzo Franceschi‑Bicchierai is a senior cybersecurity reporter at TechCrunch; reachable at lorenzo@techcrunch.com or the encrypted contacts listed above.