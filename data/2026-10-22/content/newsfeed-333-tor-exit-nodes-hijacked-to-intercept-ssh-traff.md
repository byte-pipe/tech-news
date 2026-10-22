---
title: 333 Tor exit nodes hijacked to intercept SSH traffic and retrieve plaintext email - Ars Technica
url: https://arstechnica.com/information-technology/2026/10/300-tor-exit-nodes-hijacked-to-intercept-ssh-traffic-and-retrieve-plaintext-email/
site_name: newsfeed
content_file: newsfeed-333-tor-exit-nodes-hijacked-to-intercept-ssh-traff
fetched_at: '2026-10-22T16:04:47.071757'
original_url: https://arstechnica.com/information-technology/2026/10/300-tor-exit-nodes-hijacked-to-intercept-ssh-traffic-and-retrieve-plaintext-email/
date: '2026-10-22'
published_date: '2026-10-22T11:30:33+00:00'
description: For 3 days this month, 333 exit nodes were hacked in hopes of stealing sensitive data.
tags:
- ars-technica
- biz & it
- security
- exploit
---

Text
 settings

Unknown hackers hijacked more than 300 Tor exit nodes and reconfigured them to favor unencrypted email traffic and redirect SSH connections through servers they controlled, a researcher reported Tuesday.

The hijacking began in late August, when,according to Tor volunteers, the attacker used a valid password that had been reused to gain access to a Tor management server. The attacker then installedEbury, a backdoor written for Linux that was discovered 12 years ago.

## Mysteries remain

Then the attacker connected from the management server to a second Tor server, called Switzerland2, through SSH, using an RSA key that, for unknown reasons, investigators couldn’t find among Switzerland2’s authorized keys. With administrative control of Switzerland2, the attackers installed Ebury there as well. Finally, the attacker reconfigured settings on two exit nodes that Switzerland2 hosted.

Ultimately, 333 exit relays were involved in the SSH and email interception campaign, although investigators haven’t established how the attackers gained control of all the underlying servers. The attackers then reconfigured the servers. One set of changes redirected SSH traffic traversing Tor to one of 12 attacker-controlled interceptor servers. Tor users who ignored warnings that the SSH host key had changed would then enter their SSH passwords.

A second set of changes caused the exit nodes to block ports 25, 465, 587, 993, and 995—used to accept various forms of encrypted email—while continuing to allow ports for receiving unencrypted email. If email services downgraded the connections, the attackers used their access to the exit nodes to obtain unencrypted messages. It’s unclear whether any such downgrade attempts succeeded. The hijacking occurred from October 2 to October 5.

Tor volunteers partially outlined the initial compromise of the management server and Switzerland2 and the attempt to intercept unencrypted email.Tuesday’s reportrevealed many new details, including how many exit nodes were compromised and how the attackers used them to redirect SSH traffic.

“If you happen to get a circuit that exits over one of those 333 infected exit nodes, you won’t notice anything at first,” Kaba, the name of the Tor volunteer who authored the post, wrote. “Encrypted web traffic is forwarded as usual, but if you attempt an SSH connection over Port 22, you’re unknowingly redirected to one of 12 SSH interception servers. That’s exactly what happened to me on Friday morning.” Kaba then received the following warning:

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED! @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!Someone could be eavesdropping on you right now (man-in-the-middle attack)!It is also possible that a host key has just been changed.The fingerprint for the ED25519 key sent by the remote host isSHA256:6baCZCPsl+AfQuujUS81fMEE/C7UeJ+AwjrImqmDB3E.Please contact your system administrator.

The volunteer investigated further and found that when people ignored the warning, the attacker (1) stole the SSH password, (2) opened a connection to the server and observed all typed commands, and (3) opened a second connection and infected the server with Ebury.

To investigate the campaign, Kaba created a script that polled all of Tor’s roughly 3,000 exit nodes to check whether they received a correct SSH fingerprint from a test server. The test server then checked whether the connection came from a pinned exit node or one of 12 SSH interception servers used by the attacker. The volunteer further set up a honeypot to observe the interception software attempting to log in and install Ebury.

Several mysteries remain. Tor volunteers still don’t know how the attackers accessed so many servers. One possibility is that a company hosting them was hacked, but the theory is inconclusive. Another open question is who is behind the attack. “The use of Ebury and the broad collection of unencrypted data point to a financially motivated crime group,” Kaba wrote. “Though this too is just speculation.”

A last perplexing finding: why did Switzerland2 accept an RSA key when there’s no evidence it was an authorized SSH certificate?

The takeaway from the event is the crucial role in-depth defense plays in preventing data theft in mass hacks like this one. Those measures include configuring email accounts to accept only encrypted traffic and reject unencrypted ports. Another is to disable password authentication in favor of SSH keys.

 Dan Goodin
 

Senior Security Editor

 Dan Goodin
 

Senior Security Editor

 Dan Goodin is Senior Security Editor at Ars Technica, where he oversees coverage of malware, computer espionage, botnets, hardware hacking, encryption, and passwords. In his spare time, he enjoys gardening, cooking, and following the independent music scene. Dan is based in San Francisco. Follow him at 
here
 on Mastodon and 
here
 on Bluesky. Contact him on Signal at DanArs.82.
 

1. 1.The Internet goes on high alert after discovery of 8 compromised TLS certs
2. 2.PHP warns it plans to release 2 emergency patches imminently
3. 3.Xbox wants you to pay 24 to 40 cents per hour to stream games you already bought
4. 4.Report: Musk ordered Starlink slowdown in Ukraine, then blamed it on Trump
5. 5.RIP BioWare: EA shuts down storied RPG studio after over three decades

Customize