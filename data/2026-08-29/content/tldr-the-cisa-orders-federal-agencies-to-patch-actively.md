---
title: The CISA orders federal agencies to patch actively exploited Oracle flaw by August 27 | The IT Nerd
url: https://itnerd.blog/2026/08/25/the-cisa-orders-federal-agencies-to-patch-actively-exploited-oracle-flaw-by-august-27
site_name: tldr
content_file: tldr-the-cisa-orders-federal-agencies-to-patch-actively
fetched_at: '2026-08-29T21:31:41.231838'
original_url: https://itnerd.blog/2026/08/25/the-cisa-orders-federal-agencies-to-patch-actively-exploited-oracle-flaw-by-august-27
date: '2026-08-29'
published_date: '2026-08-25T20:18:09+00:00'
description: The CISA has added a maximum-severity Oracle vulnerability, CVE-2026-21962, to its Known Exploited Vulnerabilities catalog after confirming active exploitation. The flaw carries a CVSS score of 10.0 and affects Oracle HTTP Server and the Oracle WebLogic Server Proxy Plug-in for Apache HTTP Server and IIS. The vulnerability can be exploited remotely over HTTP without authentication or valid…
tags:
- tldr
---

## The CISA orders federal agencies to patch actively exploited Oracle flaw by August 27

The CISA hasaddeda maximum-severity Oracle vulnerability, CVE-2026-21962, to its Known Exploited Vulnerabilities catalog after confirming active exploitation.

The flaw carries a CVSS score of 10.0 and affects Oracle HTTP Server and the Oracle WebLogic Server Proxy Plug-in for Apache HTTP Server and IIS.

The vulnerability can be exploited remotely over HTTP without authentication or valid credentials, potentially allowing attackers to access, modify or delete critical data.

Oracle originally disclosed and patchedCVE-2026-21962on January 20, 2026, as part of its January Critical Patch Update. In March, researchers reported exploitation attempts after exploit code became publicly available.

CISA has ordered federal agencies to address the vulnerability by August 27.

Jacob Krell, Senior Director: Secure AI Solutions & Cybersecurity,Suzu LabsHad This To Say:

“CVE-2026-21962 had a patch on January 20, and CloudSEK recorded exploitation attempts against its honeypot on January 22, followed by broader automated scanning. CISA added it to the KEV catalog on August 24, 216 days after the patch. Federal agencies now have three days to remediate something attackers have had seven months to exploit.

“In January, agencies could have applied the Critical Patch Update inside a normal maintenance window and moved on. Seven months of delay while exploitation attempts and automated scanning were already being observed from rented VPS infrastructure changed the math. BOD 26-04 requires forensic triage at this severity tier, so agencies now have to assess whether compromise occurred during that seven-month exposure period alongside applying the patch.

“BOD 26-04’s 16-tier remediation matrix is well-designed for the problem it solves. For a vulnerability in the KEV, automatable, and yielding total control of a public-facing asset, the clock is three days with forensic triage. In this case, CISA’s August 24 KEV addition produced an August 27 federal remediation deadline, while CISA’s obligation is to update the catalog “as quickly as possible,” with no numerical SLA. EPSS ranked this in the top 1.4%, Shodan shows roughly 79,000 exposed Oracle HTTP Server instances, and CISA’s own SSVC record dates active exploitation to January 21 while classifying the vulnerability as automatable with total technical impact.

“Three days to remediate is the right call. Seven months to trigger it turned a maintenance window into a forensic investigation.”

This of course means update all the things ASAP. But we’re getting to a point where patching anything is a losing battle. Thus we need to think of something new when this avenue exhausts itself.

UPDATE: Also Commenting on this isDan Moore, Sr. Director, CIAM Strategy & Identity Standards atFusionAuth:

“The thousands of organizations relying on Oracle WebLogic to provide secure access to their applications are at risk of data loss, manipulation, and exfiltration. The unauthenticated access allows an attacker to make application calls to read data, as well as insert their own unauthorized changes. This issue affects any server accessible to an attacker, which is extremely problematic for many internet exposed applications.”

### Share this:

* Email a link to a friend (Opens in new window)Email
* Print (Opens in new window)Print
* Share on Reddit (Opens in new window)Reddit
* Share on Tumblr (Opens in new window)Tumblr
* Share on LinkedIn (Opens in new window)LinkedIn
* Share on Pinterest (Opens in new window)Pinterest
* Share on Telegram (Opens in new window)Telegram
* Share on Facebook (Opens in new window)Facebook
* Share on WhatsApp (Opens in new window)WhatsApp
* Share on X (Opens in new window)X

### Like this:

Like
 
Loading…

### Related

This entry was posted on August 25, 2026 at 4:18 pm and is filed underCommentarywith tagsCISA.						You can follow any responses to this entry through theRSS 2.0feed.
													You canleave a response, ortrackbackfrom your own site.

### Leave a ReplyCancel reply