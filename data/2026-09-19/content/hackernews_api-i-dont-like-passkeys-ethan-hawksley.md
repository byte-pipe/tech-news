---
title: I don't like passkeys | Ethan Hawksley
url: https://hawksley.dev/blog/i-dont-like-passkeys
site_name: hackernews_api
content_file: hackernews_api-i-dont-like-passkeys-ethan-hawksley
fetched_at: '2026-09-19T06:00:20.915814'
original_url: https://hawksley.dev/blog/i-dont-like-passkeys
author: Ethan Hawksley
date: '2026-09-18'
published_date: '2026-09-18T00:00:00.000Z'
description: 'Why passkeys are a step back for personal security: examining account lockout risks, platform lock-in, hardware key limits, and fragile recovery flows.'
tags:
- hackernews
- trending
---

←
 Blog

For the past few years, the tech industry has kept pushing passkeys as the ultimate solution to logging in. Many Big Tech companies “helpfully” inform you every time you sign in how much easier and effortless passkeys are. The only way to make them stop is either to concede and set up a passkey or dig into the settings to find the off-switch.

Google goes as far as to name the setting“Skip password when possible”(opens in a new tab), and Microsoft advertises that you shouldmake your account passwordless(opens in a new tab).

Passkeys are a fantastic technology. Since they are bound to the site they are created for, they cannot be phished by a hacker’s fake login screen. If a site suffers a data breach, passkeys are asymmetric and cannot be recovered from the server-side details.

This leads to passkeys being the perfect fit for a corporate environment, but a poor fit for personal security. To an individual, the greatest risks are instead permanent account lockout, automated account bans, and device loss. By using passkeys, you gain better security against man-in-the-middle attacks but face the higher probability scenario of losing access to your accounts.

Phishing through the standard login flow is eliminated by passkeys, but it creates a false sense of security. An account’s security is still dictated by the weakest recovery method: SMS, email links, security questions, and so on. If these recovery methods aren’t enabled, then the risk of permanent lockout remains for the user.

## Hardware keys

By design, you cannot create a backup of passkeys on a hardware key: passkeys can only be added or deleted but never moved. Instead, you need to purchase 2-3 hardware keys and enroll every key for every site. This can quickly get expensive and doesn’t scale well as the number of accounts starts to grow.

Hardware keys support discoverable credentials, where websites can query for your username instead of you typing it in. These are becoming increasingly popular amongst website developers, yet have limits of25-100 accounts(opens in a new tab)per hardware key, and top of the line keys can have up to 300. Once you exceed the limit, you must either delete some accounts or you have to buy another set of hardware keys.

## Synced passkeys

Both Apple and Google want your identity anchored to their operating systems. The “happy path” on their devices is to use their synced passkey management tied to your Apple or Google account. If their automated systems decide one day toban your account(opens in a new tab), you irreversibly lose access to all your passkeys used across all third-party accounts too.

The FIDO alliance has been working to improve interoperability and make it easier to export passkeys, but the experience is still fragmented and inconsistent across providers. This is set to improve over the coming years, but currently it is too immature to rely on. Compare with a password, which is just a string you can easily export by hand if necessary.

## Third-party synced passkeys

When storing passkeys in a password manager likeBitwarden(opens in a new tab)orKeePassXC(opens in a new tab), you end up fighting the platform. Although operating systems have recently introduced APIs (like Android’sCredential Manager(opens in a new tab)) for third-party tools to hook into, the experience remains fragmented and lacks the decades of UX polish towards password autofill. Autofill outside the browser and inside native applications remains especially inconsistent. In the future, I believe third-party passkeys will be the way forward, but we are not there yet.

## When passkeys don’t work

Logging into accounts on devices you own is the ideal scenario for passkeys. When you have to handle a colleague’s computer, it gets much more inconvenient. You could plug in a hardware key, but you don’t always have access to the ports. You could sign in and use a synced passkey, but that involves trusting the computer to not leak all of your other passkeys. The last option is to use“Hybrid Transport”(opens in a new tab), where you scan a QR code and connect via Bluetooth simultaneously to the computer. Whilst this option is secure and works in theory, reality is plagued with edge-cases where connections fail or Bluetooth is straight-up unsupported.

## Passkeys aren’t ready yet

I believe enterprise users have good reason to use passkeys, but the ecosystem isn’t mature enough yet for individuals.

Whilst TOTP codes have known phishing vulnerabilities, the recovery and lockout risks of passkeys pose a greater day-to-day risk to most people than anAiTM proxy(opens in a new tab). A combination of randomly generated passwords stored inside a third-party password manager, paired with an independent TOTP app, gives control to the user without giving up the flexibility of plain text. For users who previously reused passwords across all their sites, passkeys are a huge step-up. For everybody else, it is currently a step back.

Email address
Subscribe