---
title: Another spyware maker caught distributing fake Android snooping apps | TechCrunch
url: https://techcrunch.com/2026/04/24/another-spyware-maker-caught-distributing-fake-android-snooping-apps/
date: 2026-04-24
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-04-25T08:22:06.615144
---

# Another spyware maker caught distributing fake Android snooping apps | TechCrunch

# Summary of “Another spyware maker caught distributing fake Android snooping apps | TechCrunch”

## Main findings
- Italian digital‑rights group **Osservatorio Nessuno** released a report on a new Android malware dubbed **Morpheus**.
- Morpheus masquerades as a phone‑update app and can steal a wide range of data from the victim’s device.
- The spyware is linked to **IPS**, an Italian firm that has supplied lawful‑interception tools for over 30 years and counts several Italian police forces among its customers.

## How the infection works
- The attack relies on a **low‑cost, user‑driven infection vector**: the target’s mobile carrier blocks data, sends an SMS prompting the user to install a “phone‑update” app, and the app installs the spyware.
- Once installed, Morpheus exploits Android’s accessibility services to read screen content and interact with other apps.
- The malware displays a fake update, forces a reboot screen, and then spoofs WhatsApp to request the user’s biometric authentication, which grants the spyware full access to the WhatsApp account.

## Comparison with more advanced spyware
- Unlike premium tools from **NSO Group** or **Paragon Solutions**, which use zero‑click exploits and expensive vulnerabilities, Morpheus depends on social engineering and the target’s cooperation.
- This makes it cheaper and easier to deploy but still effective for targeted surveillance.

## Evidence tying the malware to IPS
- One of the command‑and‑control IP addresses is registered to “IPS Intelligence Public Security.”
- Code fragments contain Italian phrases (e.g., references to *Gomorra* and “spaghetti”), a pattern observed in other Italian spyware samples.
- Researchers Davide and Giulio (who prefer first‑name only) believe the campaign is linked to “political activism” in Italy, a common motive for such attacks.

## Broader Italian spyware landscape
- IPS joins a growing list of Italian surveillance firms that emerged after the collapse of **Hacking Team**, including CY4GATE, eSurv, GR Sistemi, Movia, Negg, Raxir, RCS Lab, and SIO.
- Earlier in 2024, WhatsApp warned ~200 users about a fake app that was actually SIO‑made spyware.
- Italian prosecutors suspended the use of CY4GATE and SIO tools in 2021 due to serious malfunctions.

## Additional notes
- IPS did not respond to TechCrunch’s request for comment.
- Readers with further information can contact reporter Lorenzo Franceschi‑Bicchierai securely via Signal, Telegram, or Keybase.