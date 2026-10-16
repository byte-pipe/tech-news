---
title: Someone on Torrent Sites Kept Fucking With My Sonarr
url: https://thereallo.dev/blog/someone-on-torrent-sites-kept-fucking-with-my-sonarr-setup
site_name: hackernews_api
content_file: hackernews_api-someone-on-torrent-sites-kept-fucking-with-my-sona
fetched_at: '2026-10-16T15:12:13.253114'
original_url: https://thereallo.dev/blog/someone-on-torrent-sites-kept-fucking-with-my-sonarr-setup
author: Thereallo
date: '2026-10-15'
description: PLEASE stop putting skid malware on torrent sites as South Park episodes
tags:
- hackernews
- trending
---

I run the usual *arr stack on my NAS. It usually works just fine, until I saw a warning on my dashboard.
The new South Park episode was stuck in the queue with:
WHO is actually falling for this in the big 2026????

## It's an EXE

Let me very clear about what this is.
Someone took a South Park EP name, put 
.exe
 on the end, and uploaded it to public trackers with 
2,392 seeders
, ???
Who is dropping episodes as an EXE????
And Sonarr grabbed it, because of course it did. Then it sat there trying to import it every 90 fucking seconds:
 
Copy
Import failed, path does not exist or is not accessible by Sonarr:

/data/downloads/torrents/South Park S29E03 1080p WEB H264-MeGusta.exe
Not even a folder with a fake 
.mkv
 and a "codec installer" next to it like the "good old days".
Just the exe. Are we deadass.
qBittorrent marked it "finished" two seconds after adding it with 
total_downloaded: 0
, so nothing actually landed on disk. No idea why. Don't care. Thanks qBit.
I blocklisted it in Sonarr, which nukes it from qBittorrent and stops it grabbing the same junk skid malware again.
Then I downloaded it again on purpose. Because now I'm pissed and I want to know what's inside.

## 887 MB of Nothing

It's a real PE, x64 GUI. The actual program is 
118 KB
.
 
Copy
pe end 0x1ce00

overlay 886653736 bytes
The other 886 MB is random junk glued onto the end. Why? Because a lot of scanners just give up on files that big.
The version info says:
 
Copy
CompanyName Freeware Developers

FileDescription prepares application data

OriginalFilename SetupHelper.exe
"Freeware Developers." my ass
I chopped the 118 KB off the front and threw it into IDA, because I'm not loading a gigabyte of bullcrap into anything. Then the entire thing is covered in this:
c
Copy
dword_14000C020 
^=
 0x
F2C2EAC0
;

v34 
=
 0
;

dword_14000C020 
^=
 0x
F2C2EAC0
;
XOR a global. XOR it back. Do nothing. Hundreds of times.
It exists purely to make the decompiler output look like shit, and it does, congrats.
Strip all that out and the logic is like six steps:
1. Open its own file.
2. Read the last 64 bytes.
3. Use those to find and decrypt a payload hidden in the junk.
4. Map it as a PE in memory by hand.
5. PointPEB->ImageBaseAddressat it.
6. Jump in.
Nothing touches disk. Adding all that obfuscation for six steps.

## Footer

The last 64 bytes of the file are the whole config:
Offset
Size
Description
0x00
32 bytes
key, XORed with a 32 byte mask in .data
0x20
12 bytes
ChaCha20 nonce
0x2C
4 bytes
payload size ^ fnv1a(mask)
0x30
4 bytes
(flags | padding << 8) ^ fnv1a(mask)
0x34
8 bytes
payload size ^ fnv1a(mask)
0x3C
4 bytes
fnv1a(mask)
It's ChaCha20. They hid the constants by building them out of globals, and they still come out to 
expand 32-byte k
. You can't hide ChaCha20 from someone who's seen ChaCha20 before.
flags = 3
 turns on an anti debug check (
PEB->BeingDebugged
, debug port queries, the usual) and an anti sandbox score. Trip either one and it just quietly exits.
A sandbox sees a normal app open a file and leave.
Cool. Except the key is literally inside the file. (????) You don't even need to run it:
python
Copy
mask 
=
 bytes
.
fromhex
(
"
56951de331cd7f254bf1931533dd82bc3c8bf542f0d1ed5736a40f394c51d0a1
"
)

h 
=
 fnv1a
(
mask
)

size 
=
 u64
(
footer
,
 0x
34
)
 ^
 (
h 
|
 h 
<<
 32
)

fl 
=
 h 
^
 u32
(
footer
,
 0x
30
)

pad 
=
 fl 
>>
 8

key 
=
 xor
(
mask
,
 footer
[:
32
])

nonce 
=
 footer
[
32
:
44
]

payload 
=
 chacha20
(
key
,
 nonce
,
 data
[
-
64
 -
 pad 
-
 size 
:
 -
64
 -
 pad
])
Out pops a second PE. 929 KB, MSVC, C++20, zlib bundled.
All that anti analysis bullshit but a dozen lines of Python can just strip the obf.

## Big surprise, It's a Stealer

Strings are encrypted, imports stripped down to the CRT, everything resolved at runtime.
And then 
WinMain
 just dumps every module by name in plain text:
 
Copy
osinfo

browsers

telegram

wallets

discord

steam

clipboard

remoteaccess

credentialmanager

authy

notes

obs

ssh

email

games

filegrabber
Every other string gets its own function:
c
Copy
v5 
=
 _mm_xor_ps
(
v6
,
 v5
);

v7 
=
 {
 1924987977
,
 1270327144
,
 877876327
,
 271431577
 };

v8 
=
 {
 641333755
,
 -
1942364857
,
 ... 
};

sub_140080F40
(
&
v5
,
 v7
,
 v8
,
 0x
20
);
Two constants XORed into a key, an IV, ciphertext, length. 
sub_140080F40
 is AES with the S-box hidden behind RC4, because one layer of crypto apparently wasn't edgy enough.
Tried the standard modes on the first one:
 
Copy
cbc b'w\x1c\xe9\xc6\xa0y\x96\xa4...'

ctr b'guid=\x00\x00\x00...'
AES-128-CTR. Per string key. 672 call sites.
I am not doing that by hand.
So I pulled every call site out of IDA, emulated just the few instructions before each call in Unicorn, grabbed the key, IV and ciphertext out of the registers, and decrypted them in Python. 601 of 672 came out clean.
The rest are buried in bigger functions but I genuinely COULD NOT care less, 601 was plenty.

## It Wants Literally Everything

* Browsers: Chrome, Edge, Brave, Opera, Opera GX, Vivaldi, Firefox. Passwords, cookies, autofill, and it has code for Chrome's new app bound encryption too.
* Crypto wallets: Exodus, Electrum, Atomic, Guarda, Coinomi, Ledger Live, Trezor Suite, Wasabi, Sparrow, Monero, Zcash, Armory, plus extension wallets.
* Password managers: KeePass, KeePassXC, Bitwarden, 1Password, NordPass, RoboForm, Windows Credential Manager.
* Accounts: Telegram, Discord tokens, Steam, Roblox cookies, Minecraft accounts, Authy.
* Dev stuff:.ssh,.aws,.azure, gcloud,.kube,.docker.
* Remote access: AnyDesk, TeamViewer, WinSCP, FileZilla, mRemoteNG, RDCMan.
* The rest: Outlook, Thunderbird, VPN configs, OBS settings, Sticky Notes, and the documents on your desktop.
It even grabs your 
Sticky Notes
 for WHAT????
Everything gets zipped with the bundled zlib and shipped off.

## YouTube Channel

No hardcoded server, instead it decrypts:
 
Copy
www.youtube.com/channel/UC18vFC1xgebddr_7NsvgBYA

gist.githubusercontent.com/jasonterra69/48d9e264c05843f0cdc302143b4400c8/raw

[[

]]

ZhxchsdfhSGdfgsgdfAJsakdaksdk2364236AH
A YouTube channel, a GitHub gist, two brackets, and a key that is visibly someone mashing their keyboard.
The YouTube channel is "bubblegym". Created September 14, 2026:
Base64 decode it, XOR it with the keyboard smash, and you get the address:
python
Copy
b 
=
 base64
.
b64decode
(
"
OA0dDQ0HFBQHJyIHEkkQCAlJLS0JTgwAAB8S
"
)

k 
=
 b
"
ZhxchsdfhSGdfgsgdfAJsakdaksdk2364236AH
"

bytes
(
x 
^
 k
[
i 
%
 len
(
k
)]
 for
 i
,
 x 
in
 enumerate
(
b
))
 
Copy
beenetprotect[dot]com/lgz/gdata
That exact address is 
also hardcoded in the binary
 as a fallback apparently???
I guess the whole point of a dead drop is that you can swap servers without the address being in the malware.
But you put the address in the malware anyway so what's the point for fetching from Gist and YouTube????

## Opsec level: Cloudflare Registrar

 
Copy
Domain Name: BEENETPROTECT.COM

Creation Date: 2026-09-14T06:21:54Z

Registrar: Cloudflare, Inc.

Name Server: DONALD.NS.CLOUDFLARE.COM

Name Server: JULISSA.NS.CLOUDFLARE.COM
Registered September 14. Same day as the "gaming channel". Builds on October 6, torrent up October 8.

## PSA for *arr users

If you run Sonarr or Radarr off public indexers, this WILL hit you. Sonarr can't run an exe, so it's not the problem.
The problem is your roommate, your parent, or 3am you double clicking it in the downloads folder. (do NOT execute execute the skid malware)
Five minutes of setup:
* qBittorrent: add*.exe,*.scr,*.lnk,*.bat,*.cmdto "Excluded file names", tt'll just refuse to download them.
* Sonarr / Radarr: blocklist with "Remove from client" when you see one of these.
* Prowlarr: if a tracker keeps serving this crap, demote it or drop it.
And to whoever made this: you probably spent weeks or shit ton of tokens on ChaCha20, AES-CTR, runtime API hashing, anti sandbox scoring, Chrome app bound encryption bypasses, just to make a shitty skid malware.
Get a job.