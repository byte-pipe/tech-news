---
title: 1-in-2 phones sold in Africa exfiltrate telemetry to China - NowSecure
url: https://www.nowsecure.com/blog/2026/07/08/what-the-transsion-telemetry-research-means-for-mobile-security/
site_name: tldr
content_file: tldr-1-in-2-phones-sold-in-africa-exfiltrate-telemetry
fetched_at: '2026-07-11T11:24:45.530002'
original_url: https://www.nowsecure.com/blog/2026/07/08/what-the-transsion-telemetry-research-means-for-mobile-security/
date: '2026-07-11'
description: What the Transsion Telemetry Research Means for Mobile Security Transsion is the world's fourth-largest smartphone manufacturer. Its brands — TECNO,
tags:
- tldr
---

#### What the Transsion Telemetry Research Means for Mobile Security

Transsion is theworld’s fourth-largest smartphone manufacturer. Its brands — TECNO, Infinix, and itel —dominate markets across Africa, South Asia, Southeast Asia, and Latin America. Every one of these devices ships with a first-party Android telemetry framework: Athena for event collection and oneID for cross-app tracking, both reporting to *.shalltry.com.

While users have long known these devices “call home” — shalltry.com frequently appears onad and tracker blocklists, and the “com.hoffnung” package is notoriously impossible to remove — the content of these beacons has remained a mystery. The traffic is heavily encrypted, effectively turning the devices’ telemetry into a black box. Until now.

The encryption is real but it is not a barrier: the keys were embedded directly inside the client. This is a write-up of recovering it, decrypting the traffic, and reading what a Transsion phone actually sends, which turns out to include the network activity of every app on the device, the foreground app moment to moment, precise location, and which app opened the camera, all bound to permanent identifiers. From a mobile security perspective,the findings demonstrate how software outside an organization’s direct control can collect and transmit sensitive information without obvious visibility.

We extracted theSDKfrom aTECNO Spark 40 (KM5)firmware image and confirmed the decryption against live device traffic. Everything below is reproducible from the firmware and a single runtime hook.

## The upload channel is AES, and the key is in the APK

The bulk telemetry endpoint is POST /athena/checkpoint/v3/upload. The body is base64 of an AES ciphertext; a handful of request headers describe how to decrypt it: encrypt-index, encrypt-level: 3, zip, ver, appids, dupid.

Pulling com.rlk.weathers (the Weather app, which embeds Athena 3.1.0.2-sys) out of the ROM and decompiling it, the cipher construction is a plain SecretKeySpec, with no native code and no white-box:

// g2/b.java : the per-message cipherSecretKeySpec k = new SecretKeySpec(bArr, "AES");Cipher c = Cipher.getInstance("AES/CBC/PKCS5Padding");c.init(1, k, new IvParameterSpec(i2.g.f4592o));   // f4592o = the IV

Two things need recovering: the IV i2.g.f4592o, and the key bArr.

The initial recovery step targeted the IV. Rather than being hardcoded in plain sight, the framework pulls the value from a config bundle hidden behind a layer of obfuscation.:

// i2/g.javaf4592o = jSONObject.getString("iv").getBytes();

That config bundle is itself hex-encoded and XOR-obfuscated in the binary, decoded by a one-line transform:

// e2/a.javafor (int i = 0; i < bArrK.length; i++)bArrK[i] = (byte) (222 - ((char) bArrK[i]));   // deobfuscate, then new String()

Running that transform over the embedded blob yields the framework’s bootstrap configuration in the clear:

{"iv": "abcdefghijk1mnop","w":  "3716E5CB1B982C035013E52167AAF54A","u":  "/athena/checkpoint/v2/upload","g":  "/logconf/v1/secret",...}

TheIV is the 16-byte ASCII string abcdefghijk1mnop, constant for every message on every device. w is a fallback key, used before the device has provisioned a key table.

## The key is selected by index, and the table is one global constant

The per-message key is chosen at send time:

// e2/a.java : key selectionList<byte[]> table = ...f4615l;               // the "p" key tableint idx = (int)(System.currentTimeMillis() % table.size());return new Pair<>(idx, table.get(idx));// m2/d.java sets the header:  encrypt-index = idx + 1

So key = KEY_TABLE[encrypt-index – 1]. The table has 64 entries; each key is a 32-character ASCII hex string used as raw bytes (getBytes()), which is a 32-byte AES-256 key. The keys are provisioned from the control plane (/logconf) rather than hardcoded, which raises the obvious question of whether the table differs per device or per SDK version.

It does not. Two different devices, on two different SDK versions, sending the same event at the same encrypt-index, produce anidentical ciphertext prefix, the signature of the same key over the same plaintext under a fixed IV. Grouping traffic by (encrypt-index, ciphertext-prefix) shows single prefixes shared across up to seven devices and four SDK versions (2.3.6.4, 2.3.6.5, 3.0.0.8-sys, 3.0.1.3). The 64-key table is aglobal constant, stable across the fleet and across at least the 2.3.x to 3.1.x version range.

That means one capture of the table decrypts everything.

## Recovering the table: one runtime hook

The table lives in memory as List<byte[]> behind a singleton accessor, d2.b.f().i(). On a non-rooted test device I repackaged the Weather app with aFridagadget and read the list directly as the app provisioned:

const list = Java.use('d2.b').f().i();          // List<byte[]>for (let i = 0; i < list.size(); i++)console.log(i, String.fromCharCode(...list.get(i)));// -> 64 keys. Index 0 == "3716E5CB1B982C035013E52167AAF54A" (the 'w' fallback), confirming alignment.

With the 64 keys and the fixed IV, decryption is:

pt = AES.new(KEY_TABLE[eidx-1].encode(), AES.MODE_CBC, b"abcdefghijk1mnop").decrypt(base64.b64decode(body))pt = unpad(pt)if headers["zip"] == "1": pt = gzip.decompress(pt)   # zip flag = gzip-before-encrypt

This decrypts the traffic cleanly, validated across every SDK version present, from the oldest 2.3.6.4 to the current 3.1.1.4. The oneID plane (/one/v1/odid) adds an RSA-2048 wrap, but it only protects a client-generated, ephemeral session key; it does not touch the symmetric /upload corpus, which is the bulk of the data. The encryption here is obfuscation of collection, not confidentiality against anyone holding the client binary.

The work also demonstrates whyruntime analysisremains an essential part ofmobile application security testing. Without observing application behavior and decrypting network traffic, much of the telemetry would have remained hidden.

## The payload is a per-event device beacon

Here is a single decrypted request. It was emitted by com.android.settings, the phone’s own Settings app, and it reports the user’s location:

// event emitted by com.android.settings (the OS Settings app){"event": "location","eparam": {"_lat": -1.32, // GPS latitude (Nairobi; truncated here)"_lng": 36.89, // GPS longitude"_geono": "kzf0rr", // geohash of the same point"_cellidlist": [ // cell towers in range, with signal strength{ "cellid": "639-02-10037-######", "level": 79 }, // MCC-MNC-LAC-CellID{ "cellid": "639-03-10747-######", "level": 56 },{ "cellid": "639-03-65535-######", "level": 36 }]}}

That coordinate does not travel alone. It rides inside the device envelope attached to every event, which carries the permanent identifiers the location gets bound to:

{"brand": "TECNO", "model": "TECNO KM5","build": "KM5-15.1.2.155SP01(OP001PF001AZ)","gaid": "", // persistent cross-app device ID"iid": "", // install / hardware ID"ekey": { "opid": "", // stable per-device account IDs"tsid": "","vaid": "" },"mcc": "639", "mnc": "03", // Kenya, mobile carrier"tz": "GMT+03:00", "lang": "en"}

Two things make this a beacon rather than a log line. First, the emitter is the Settings app: not something the user installed, opened, or can remove, and not a component anyone expects to report their GPS coordinates and the towers around them. Second, the coordinate is bound, in the same envelope, to a stack of roughly 14 persistent identifiers (gaid, _oneid, _device_id, _vaid, __taiid, the hashed serial _sn, __chipid, __tpmsid, and others), none of them user-resettable. Those identifiers are the join key that ties this location to every other event, from every app, over time. (Coordinates are truncated and identifiers and cell IDs redacted here; the raw event carried them in full.)

## On Transsion hardware, the SDK is a privileged system component

Athena ships two ways. As an ordinary app-level SDK it is sandboxed and reports only its host app. As asystem component, the -sys builds, system-signed, in the system_ext and product partitions, it runs inside privileged apps and reports device-wide.

The distinction is entirely about privilege. The same SDK, granted system rights, stops being “an app reporting itself” and becomes a device-wide agent. On a Transsion phone it is embedded in com.android.systemui, com.android.settings, the launcher, the camera service, and a central hub package,com.hoffnung(user-facing label “TPMS”), which hosts com.transsion.dataservice, the provider other apps push events into and that performs the uploads. com.hoffnung’s manifest declares the permissions that make device-wide collection possible:PACKAGE_USAGE_STATS, QUERY_ALL_PACKAGES, READ_CLIPBOARD_IN_BACKGROUND, READ_PRIVILEGED_PHONE_STATE, GET_ACCOUNTS_PRIVILEGED, MANAGE_NETWORK_POLICY, FORCE_STOP_PACKAGES, DELETE_PACKAGES.

	The same SDK, granted system rights, stops being ‘an app reporting itself’ and becomes a device-wide agent. 

## The app-level SDK reaches well beyond Transsion devices

The sandboxed, app-embedded copy is the one that turns up on any Android phone, illustrating how supply-chain components can extend privacy and security risk across a much broader collection of mobile apps.NowSecure shared a list of apps whose binaries carry the Athena/shalltry SDK and connect to the same ire-dsu / ire-dsc / ire-oneid / gslb.shalltry.com endpoints, and it is not a short or obscure list. Alongside Transsion’s own preinstalled apps (com.transsion.hilauncher HiOS Launcher, com.talpa.hibrowser Hi Browser, com.transsion.healthlife My Health, com.transsion.magazineservice Magazine Service, com.transsion.notebook Notes), it appears in widely installed third-party apps:

App
Package
What it is
Downloads
Boomplay
com.afmobi.boomplayer
one of Africa’s largest music-streaming services (tens of millions of users). 
Owned by Transsion.
100M+
StarTimes
com.star.mobile.video
major African pay-TV and streaming app
10M+
Orange Max it
com.orange.myorange.ocm
Orange’s telecom self-service “super-app”
5M+
Supermom
com.appinion.supermom
parenting community app
100M+
AHA Games
net.bat.store
Transsion’s game store
500M+
Hola-Private&Fast web browser
com.talpa.hibrowser
Browser
500M+

The same NowSecure evidence flags these builds for certificate pinning, undisclosed network hosts, and data flow to jurisdictions the app policies do not name. The point is that the collection framework is not confined to the OS layer of Transsion phones; it also ships inside popular consumer apps that run on any handset, Transsion or not.

## com.hoffnung reports the network usage of every app on the device

The clearest demonstration of what “device-wide” means is the data_use event. com.hoffnung reports, per app, how much data each installed app used, including apps that never integrated anything. These are real values from one device on a single day, _data in kilobytes:

// com.hoffnung :: data_use (one device, 2026-06-20){ "_pkg": "com.zhiliaoapp.musically", "_data": 640855 } // TikTok (~625 MB){ "_pkg": "com.facebook.katana", "_data": 296521 } // Facebook{ "_pkg": "com.truecaller", "_data": 22260 } // caller ID / dialer{ "_pkg": "com.instagram.android", "_data": 13720 }{ "_pkg": "com.whatsapp", "_data": 5873 }{ "_pkg": "com.safaricom.mysafaricom", "_data": 1825 } // carrier self-care app{ "_pkg": "com.google.android.gm", "_da no ta": 1378 } // Gmail{ "_pkg": "com.sportybet.android.gp.ke", "_data": 1079 } // sports betting{ "_pkg": "com.safaricom.mpesa.lifestyle", "_data": 604 } // M-Pesa (mobile money){ "_pkg": "com.google.android.gms.location.history","_data": 505 } // Google location history{ "_pkg": "africa.mymogo.ke2", "_data": 369 } // loan app

Each record also carries _ch, the store the app was installed from, and _net, whether the usage was on WiFi or mobile data. Across the decrypted traffic, com.hoffnung reported data_use for more than 60 distinct apps on a single device, effectively its full app inventory and relative usage: mobile-money and lending (com.safaricom.mpesa.lifestyle, tech.palm.id), betting (com.sportybet.android.gp.ke, com.odibet.app), messaging and social (com.whatsapp, com.facebook.orca, com.instagram.android, com.zhiliaoapp.musically, com.truecaller), a ride-hailing app (ee.mtakso.client), browsers, and the Google suite including com.google.android.gms.location.history.

Whether or not a user opted into analytics in any of those apps is irrelevant; the system service enumerates them from outside.

#### Mobile Application Risk Intelligence (MARI)

Read More
 

## The operating system itself is a data source

Beyond bandwidth, the privileged emitters report OS-level state that no sandboxed app could see:

Emitter
Event
What it contains
com.android.settings
location
_lat/_lng (approx. Nairobi, -1.3x, 36.8x), geohash _geono, and _cellidlist, the surrounding cell towers (MCC-MNC-LAC-CellID) with signal levels
com.transsion.aivoiceassistant
location
same coordinate and cell-tower set
com.android.systemui
sys_br_adj
_cur_app, the current 
foreground app
 (for example com.zhiliaoapp.musically, com.google.android.gm), with timestamp and ambient light
com.transsion.trancare (camera)
cameraserver2
_cameraPackageName, 
which app opened the camera
 (for example com.whatsapp.w4b), plus chip and serial IDs
com.hoffnung
charge / device_active
battery level, temperature, charge sessions; hashed device serial

The Settings app reporting a GPS coordinate and the cell towers around the device, and SystemUI reporting which app is open, are not behaviours a user would expect from those components. They are, nonetheless, what the decrypted events contain.

## How it reaches the device, and where it goes

Two routes. On Transsion hardware the SDK is preinstalled and system-signed; it arrives with the phone, is not user-installed, and cannot be removed without breaking the device. In app-embedded form it rides inside ordinary apps, which is how it reaches non-Transsion phones.

The uploads go to *.shalltry.com. The live data-sink hosts resolve to Alibaba Cloud (eu-central-1); the CDN is CloudFront-fronted. Observed hosts and roles:

Host
Role
ire-dsu.shalltry.com, dsu-a, dsu-b
telemetry sink (/athena/checkpoint/v3/upload)
ire-dsc.shalltry.com
control plane, key and config (/logconf/…)
ire-oneid.shalltry.com
identity (/one/v1/odid)
gslb.shalltry.com
GLB resolver, returns the active ire-*/dsu-* hosts at runtime
app-manage-api, cdn, ms, ds, newsaggreg
app management, delivery, ancillary

These hosts aren’t just endpoints, they are the control plane for a global, persistent data-collection network that bypasses traditional app sandboxing. References in the payloads and config point downstream toTaboola(lockscreen content) and aByteDance “volcano”analytics pipeline.

Mitigation for Defenders: Because the SDK is unremovable on Transsion hardware, client-side controls are insufficient. The only effective mitigation is a DNS-level wildcard block of *.shalltry.com(and *.transsion-os.com). Because the framework uses a GSLB to distribute live sink hostnames, simple blocklists that rely on static leaf hosts will fail. An apex-wildcard block is the only way to effectively sever the connection.

## Key takeaways

The Transsion research underscores a growing reality for mobile security and mobile AppSec. Mobile apps increasingly rely on third-party SDKs, preinstalled services and other software components that organizations don’t build and often can’t fully evaluate.

Source code reviews and vendor documentation provide only part of the picture. Understanding how mobile apps behave at runtime, what data they collect and where they send it gives mobile security teams the visibility needed to identify hidden supply-chain risks before they become larger problems.

Research like this reinforces the value of mobile app risk intelligence.NowSecure Mobile App Risk Intelligence (MARI)combines automated analysis of thousands of mobile apps with ongoing security research to help organizations identify hidden SDKs, suspicious network communications and other indicators of third-party mobile risk. Together, those insights help security and mobility teams make more informed decisions about the mobile apps they allow into their environments.

This research was written in partnership with our guest author and independent security researcher Buchodi.

## RelatedContent

 

									Mobile App Privacy Risks Explained: SDKs, Data Collection & Hidden Exposure								

 

									Authenticated Mobile App Security Testing Finds 78% More Sensitive Data Risk								

 

									Inside Third-Party Mobile App Risk: Evaluating the Apps Your Workforce Depends On								

										eBook