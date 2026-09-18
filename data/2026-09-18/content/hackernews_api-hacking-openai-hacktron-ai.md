---
title: Hacking OpenAI | Hacktron AI
url: https://www.hacktron.ai/blog/hacking-openai
site_name: hackernews_api
content_file: hackernews_api-hacking-openai-hacktron-ai
fetched_at: '2026-09-18T14:48:04.014470'
original_url: https://www.hacktron.ai/blog/hacking-openai
author: Handy-Man
date: '2026-09-18'
published_date: '2026-09-13T00:00:00.000Z'
description: A heap overflow and SSO misconfiguration to compromise OpenAI internal repositories
tags:
- hackernews
- trending
---

## Intro

On July 25, 2026, we chained two critical vulnerabilities to compromise multiple OpenAI employees’ ChatGPT accounts. With these accounts, we could then access internal OpenAI repositories, and potentially many other connectors.

To prove we had in fact gained the access we believed without allowing ourselves to learn any sensitive information, we used the employee’s Codex to open a PR #1186742 in OpenAI’s internal monorepoopenai/openai.

Exploit chain
1. libheifImage decoder
2. DebianMissing security backport
3. ImageMagickUses libheif
4. DiscourseImage uploads
5. OpenAI forumcommunity.openai.com
6. OpenAI SSOIdentity flaw
7. ChatGPT / CodexAccount access
8. GitHubConnected integration
9. Internal reposOpenAI

Until two months ago, any user or OpenAI employee logging into OpenAI’s own help forum (community.openai.com)could have had their ChatGPT and Codex accounts taken over. Since people can connect various services to Codex and ChatGPT, the scope of what we could theoretically access was huge, including GitHub, Slack and emails.

The entire timeline from initial discovery to access to OpenAI repo access took place in less than 72 hours.

We immediately reported the initial vulnerability to OpenAI and Discourse and worked with them to coordinate the patch. We appreciate their attention to detail and fast resolution of this issue. OpenAI also paid us a$6,500bounty.

We provide a full timeline of the disclosure process here. The rest of the post details how we discovered the two vulnerabilities, how we used claude models, as well as our takeaways from this experience.

1. 25 July 202605:00–06:00 UTCInitial FindingHacktronAI team obtained remote code execution (RCE) and administrative access to the Discourse environment hosted atcommunity.openai.com.
2. 25 July 202608:00–10:00 UTCBugcrowd SubmissionAfter confirming the cross-product impact, the team coordinated internally on the responsible disclosure process and submitted a report through OpenAI’s Bug Bounty Program on Bugcrowd.
3. 25 July 202613:30–15:30 UTCOpenAI Employee Account Access & Proof of ConceptTo demonstrate the practical impact of the vulnerability, we created a harmless proof-of-concept pull request in OpenAI’s internal monorepo (link redacted at OpenAI’s request). We updated the existing Bugcrowd submission with these findings, reached out to friends at OpenAI on Twitter/X to notify them directly, and ceased all further testing at approximately15:30 UTC.
4. 25 July 202622:49:45 UTCOpenAI-Side Fix ConfirmedOpenAI replied to the report confirming the issue had been fixed, roughly 14 hours after the initial submission.
5. 25 July 2026Discourse Reported via HackerOneWe submitted a report to Discourse through its HackerOne program.
6. 26 July 2026Discourse RespondedDiscourse replied to the report on Sunday.
7. 27 July 2026Discourse Fix ReadyDiscourse had a fix ready by Monday and added image-processing sandboxing as defense in depth.
8. 28 July 2026Discourse Advisory PublishedDiscourse publishedGHSA-vhm9-85gw-x335with patch and rebuild guidance.
9. 01 Sep 2026OpenAI Rewarded $6,500 Bounty and Marked ResolvedOpenAI comment — To clarify the scope of that award: testing against the Discourse-hosted community.openai.com was explicitly excluded from our bug bounty program. The award recognizes the OpenAI-side finding, not the actions against Discourse.

## Background

A few months ago, our team at Hacktron, led by Harsh Jaiswal alongside Mohan Pedhapati and Rahul Maini, began researching frontier AI companies to find security vulnerabilities. This led us to discover an SSO misconfiguration in OpenAI’s identity infrastructure and alibheifRCE in the community forum used by OpenAI.

We’ve since expanded the research intoHEIF Heist, a multi-month investigation tracinglibheifacross Slack, Meta, GitHub Enterprise, Ruby on Rails, and Node.js frameworks such as Next.js, Astro, and Gatsby. Asurprising amountof widely-used software depends on this one image-processing library.

If your application processes user-controlled images and accepts .heic/.heif/.avif images, it is highly likely it is affected. Please reach out to us athello@hacktron.aiif you need any kind of assistance.

## Hacking community.openai.com

Warning

Patch notice:If you self-host Discourse, rebuild your installation now. Older Docker images may contain a vulnerablelibheifdependency that permits code execution through an image upload. Rungit pullfollowed by./launcher rebuild appfrom/var/discourse; a web-interface update alone may not replace the underlying image. Discourse-hosted customers have already been patched. See thesecurity advisory.

OpenAI uses Discourse for their forum and allows “Sign in with OpenAI” throughauth.openai.com. After getting a good understanding of OpenAI’s services and infrastructure, we had reason to believe that compromising the forum could create a path into broader OpenAI services through this identity flow. To test that hypothesis, we first needed remote code execution on an OpenAI service like the Discourse community forum.

While the Discourse app itself is actually not an easy target (we have looked into it in the past), we thought we could go after a dependency.

### Heap buffer overflow in libheif

On July 23, we started reviewing Discourse’s image-upload pipeline, and we found that HEIC and HEIF files followed an unusual path. Discourse normally used FastImage for image checks, but because FastImage did not support HEIF, it passed those files to ImageMagick’smagickcommand for conversion.2That exposed the underlyinglibheifparser directly to attacker-controlled files.

We started an Opus 4.8 session with the Discourse Docker image and asked it to inspect the installedlibheifpackage for security issues. After a while, it found that some particular security fixes were not back-ported to the libheif package. This allowed an heap buffer overflow leading to OOB R/W primitives during HEIC decoding.

Interestingly, the vulnerable code had been changed upstream the previous year, but the commit was not documented as a security fix and received no CVE.3This might be a reason why Debian 12 and 13 have not received the security relevant backports in time. Because Discourse’s Docker image was based on Debian 12, it installed the vulnerablelibheifversion 1.19.7. Even Debian 13 still shipped the vulnerable version 1.19.8 at the time. Since then, Debian has published its security update for Debian 13 on August 8, 2026.4

On July 24, we used Opus 4.8 to develop a working ImageMagick/libheifcode-execution exploit with ASLR disabled. We then launched several separate sessions to make it reliable against Discourse’s default configuration with ASLR enabled, which wasn’t fruitful.

### Opus 5 Released

That evening, Anthropic released Claude Opus 5.5We started a new session, which first produced a working ARM64 exploit for a local Mac within 3 hours. We then asked it to port the exploit to the x86-64 environment andjemallocconfiguration used by Discourse.

By 6:00 a.m. on July 25, we had confirmed local RCE through an image upload. We then placed Claude in an autonomous/goalloop against our own Discourse Cloud instance, proxied throughrce.ee/ctf-forumto make it look like a CTF target as Opus refused write exploit for remote instances.

When we checked again at 10:00 a.m., the agent had achieved RCE on Discourse Cloud and demonstrated access by reading/etc/hosts. Using the generated exploit script, we managed to get RCE on OpenAI’s instance.

After we had confirmed our hypothesis of no interaction account takeover of ChatGPT/Codex accounts from active members of the forum, we immediately sent our report to OpenAI. We then took over an OpenAI employee’s account, whose Codex was connected to OpenAI’s Github organization. To demonstrate impact without actually accessing any internal code, we sent a prompt to this employee’s Codex account to open a PR for us in OpenAI’s internal monorepo. Then we stopped any further testing.

We updated the BugCrowd submission with the impact proof and alerted OpenAI security. We also prepared a report for Discourse and reported it to their HackerOne program. Discourse received the report on a Saturday, replied on Sunday, and had a fix by Monday (kudos for speed). They alsoimmediately started sandboxingImageMagick.

We want to emphasize that the vulnerability to escalate is not Discourse-specific. It is an OpenAI SSO issue that turned the forum compromise into access to ChatGPT and Codex. If any first-party or third-party OpenAI service using the OpenAI SSO was compromised, it would lead to same access - Discourse was merely one way of proofing it.

## Costs of finding these vulnerabilities

The Discourse and OpenAI hack took a few days for an agent, and just a few hours of human time. The wholeHEIF Heistresearch project going after Slack, Meta, adn more took two-months, cost less than $3,000 in tokens in total, and was conducted by three researchers. Adapting the exploit to each new company usually took only one or two days.

We observed that every new model is getting increasingly capable, as evident by the Discourse exploit presented in this report. Opus 4.8 struggled across several sessions to produce a working exploit with ASLR enabled. Within hours of Opus 5’s release, we gave it the same problem and it succeeded. Across the broader campaign, we saw another clear jump from Opus 5 to GPT-5.6 Sol, when we had to exploit the vulnerability without knowing anything about the target system besides that it’s vulnerable.

For each target, testing began with an image upload. From there, we turned memory corruption into a reliable memory leak or shell, usually without knowing the exactlibheifversion, libc version, or deployment environment. The AI started almost blind and adapted the exploit for each company within one or two days. We are not aware of any company that detected the activity except Shopify, even after thousands of images were sent and their image processors repeatedly crashed.

When code execution landed inside a sandbox or restricted environment, the models also helped with privilege escalation, lateral movement, and bypassing existing defenses. This was not completly autonomous hacking, and skilled human guidance remained important, but the amount of work a small team could perform increased dramatically.

## Epilogue

Software has long benefited from a kind of security through complexity. The code and even the vulnerability could be public, but turning a bug into a reliable exploit still required rare expertise, significant time, and knowledge of the target environment. Known memory corruption vulnerabilities were expensive to operationalize, while zero-days were mostly reserved for the highest-value targets.

This was never a real security boundary, but it protected ordinary companies in practice from software vulnerabilities. AI is removing that protection by turning more of this scarce expertise into compute. Work that once required a well-resourced team and months of effort can now be compressed into days.

Security assumptions must catch up with attacker capabilities. A realistic threat model should take into account the economics of exploitation today, instead of relying on outdated assumptions6about who can carry out sophisticated attacks.

Hacktron’s mission is to help secure the internet by finding and eliminating vulnerabilities in widely trusted software before malicious actors do. We are continuing this research across frontier labs and other internet-critical systems. If you are responsible for securing one of them, we would like to work with you.

## Versions affected and patches

HEIF Heistis not tied to a single version. It targets an entire ecosystem of vulnerabilities across multiple release families (e.g. 1.19.x, 1.20.x, 1.22.x, 1.23.x). Any deployment lacking the latest upstream security patches is potentially vulnerable.

* Update upstream.Install the latest security-patchedlibheifandlibde265packages through your distribution’s security channel or an upstream release. As of September 14, 2026, the latest upstreamlibheifsecurity release is v1.23.4; v1.23.2 has been superseded by further security fixes. Distribution packages may carry backported fixes under an older upstream version number, so check the package security advisory as well.74
* Defense in depth.Given the complexity of the ISO base media file format and the pace of decoder updates, future memory-safety flaws are likely. Production architectures should disable untrusted HEIF/AVIF decoding where it is not needed, or isolate image-processing pipelines inside hardened, ephemeral sandboxes. ImageMagick’s security policy supports restricting accepted formats and resource usage.8

## Acknowledgements

We thank Sudanshu Rajhbhar for technical assistance, and Zayne Zhang, Fabian Faessler, Robert Chen, and Jessica Ruan for proofreading, reviewing drafts, and providing feedback that improved this post.

## References

[1]xkcd #2347: Dependency↩

[2]Discourse: Support for HEIC images↩

[3]libheif: simplify overlay overlap area computation↩

[4]Debian DSA-6417-1: libheif security update↩1↩2

[5]Anthropic: Introducing Claude Opus 5↩

[6]RAND: A Playbook for Securing AI Model Weights↩

[7]libheif v1.23.4 security maintenance release↩

[8]ImageMagick Security Policy↩

## Work with the team behind this research.

Hacktron brings together top CTF researchers, experienced red teamers, and
offensive security researchers. We use AI to accelerate security research,
finding and eliminating vulnerabilities in widely trusted software before
malicious actors do. We’re continuing our research across frontier labs and
other internet-critical systems. If you’re responsible for securing one of
them, we’d like to work with you.

Hacktron finds and fixes real security vulnerabilities before they ship to production.

Start for free
S
t
a
r
t
 
f
o
r
 
f
r
e
e
Book a demo
B
o
o
k
 
a
 
d
e
m
o