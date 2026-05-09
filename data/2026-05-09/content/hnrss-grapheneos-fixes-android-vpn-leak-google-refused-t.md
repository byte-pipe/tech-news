---
title: GrapheneOS fixes Android VPN leak Google refused to patch | CyberInsider
url: https://cyberinsider.com/grapheneos-fixes-android-vpn-leak-google-refused-to-patch/
site_name: hnrss
content_file: hnrss-grapheneos-fixes-android-vpn-leak-google-refused-t
fetched_at: '2026-05-09T19:57:58.402464'
original_url: https://cyberinsider.com/grapheneos-fixes-android-vpn-leak-google-refused-to-patch/
author: Alex Lekander
date: '2026-05-09'
published_date: '2026-05-06T14:13:12+00:00'
description: GrapheneOS has released a new update that fixes a recently disclosed Android VPN bypass flaw capable of leaking a user’s real IP address.
tags:
- hackernews
- hnrss
---

# GrapheneOS fixes Android VPN leak Google refused to patch

May 6, 2026
 
By
 
Alex Lekander
 — 
X
LinkedIn
Reddit
Facebook
Share

GrapheneOS has released a new update that fixes a recently disclosed Android VPN bypass vulnerability capable of leaking a user’s real IP address.

The leak happens even when Android’s “Always-On VPN” and “Block connections without VPN” protections were enabled.

The issue, disclosed last week by security researcher “lowlevel/Yusuf,” affected Android 16 and stemmed from a newly introduced QUIC connection teardown feature in Android’s networking stack. In its latest release, GrapheneOS says it has “disable[d] registerQuicConnectionClosePayload optimization to fix VPN leak,” effectively neutralizing the attack vector on supported Pixel devices.

GrapheneOS is a privacy- and security-focused Android-based operating system primarily developed for Google Pixel devices. The project is widely used by privacy-conscious consumers, journalists, activists, and enterprise users seeking stronger application sandboxing, exploit mitigations, and reduced reliance on Google services.

According toYusuf’s technical write-up, the vulnerable API allowed ordinary applications with only the automatically granted INTERNET and ACCESS_NETWORK_STATE permissions to register arbitrary UDP payloads with system_server.

When the app’s UDP socket was later destroyed, Android’s privileged system_server process would transmit the stored payload directly over the device’s physical network interface rather than through the VPN tunnel. Because system_server operates with elevated networking privileges and is exempt from VPN routing restrictions, the packet bypassed Android’s VPN lockdown protections entirely.

Attack flow overview
lowlevel.fun

The researcher demonstrated the flaw on a Pixel 8 running Android 16 with Proton VPN enabled alongside Android’s lockdown mode. The app reportedly leaked the device’s actual public IP address to a remote server despite VPN protection being fully enabled.

Google introduced a feature that allows applications to gracefully terminate QUIC sessions when sockets are unexpectedly destroyed. However, the implementation accepted arbitrary payloads without validating whether they were legitimate QUIC CONNECTION_CLOSE frames and did not verify whether the originating application was restricted to VPN-only traffic.

The researcher reported the issue to Android’s security team, which classified it as “Won’t Fix (Infeasible)” and “NSBC” (Not Security Bulletin Class), stating that it did not meet the threshold for inclusion in Android security advisories. The researcher appealed the decision, arguing that any application could leak identifying network information using only standard permissions, but Google maintained its position, authorizing public disclosure on April 29.

GrapheneOS responded by disabling the underlying optimization entirely inrelease 2026050400.

kudos to@GrapheneOSfor shipping a fix in less than a weekhttps://t.co/lF7pNCETQ4https://t.co/otKgCBSKl3

— Yusuf (@cybaqkebm) 
May 5, 2026

Beyond the VPN leak fix, the latest release also includes the full May 2026 Android security patch level, multiple hardened_malloc improvements, Linux kernel updates across Android’s 6.1, 6.6, and 6.12 branches, and a backported fix for CVE-2026-33636 in libpng. The update additionally ships newer Vanadium browser builds and expanded Dynamic Code Loading restrictions.

The researcher noted that stock Android users could temporarily mitigate the issue manually through ADB by disabling the close_quic_connection DeviceConfig flag. However, that workaround requires developer access and may not persist indefinitely if Google removes the feature flag in future updates.

If you liked this article, be sure to follow us onX/Twitterand alsoLinkedInfor more exclusive content.

X
LinkedIn
Facebook
Reddit
Share

## More from CyberInsider

### Apple and Meta warn Canada’s Bill C-22 forces encryption backdoors

### EU calls VPNs “a loophole that needs closing” in age verification push

### Former IT contractor convicted for wiping 96 US government databases

### Canvas outage hits thousands of universities as ShinyHunters threatens leak

### “ClaudeBleed” allows any Chrome extension to control Anthropic’s AI assistant

### New TCLBANKER malware self-spreads through WhatsApp and Outlook

#### AboutAlex Lekander

Alex Lekander is the Editor-in-Chief and owner of CyberInsider.com. With a passion for cybersecurity and privacy topics, Alex launched this website in 2020. His background and expertise cover privacy research, technical writing, software testing, and site administration. He holds a Bachelor of Science and a Master of Science from Johns Hopkins University.

## Reader Interactions

 

### Leave a ReplyCancel reply

Your email address will not be published.Required fields are marked*

Comment*

Name*

Email*

Website