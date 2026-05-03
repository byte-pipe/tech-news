---
title: 'Copy Fail: 732 Bytes to Root on Every Major Linux Distribution. - Xint'
url: https://xint.io/blog/copy-fail-linux-distributions
site_name: tldr
content_file: tldr-copy-fail-732-bytes-to-root-on-every-major-linux-d
fetched_at: '2026-05-03T11:40:55.698240'
original_url: https://xint.io/blog/copy-fail-linux-distributions
date: '2026-05-03'
published_date: '2026-04-29T16:32:14.605+00:00'
description: Xint Code disclosed CVE-2026-31431, an authencesn scratch-write bug chaining AF_ALG + splice() into a 4-byte page cache write. A 732-byte PoC gets root on Ubuntu, Amazon Linux, RHEL, SUSE. | AI for Security, Vulnerability Research
tags:
- tldr
---

AI for Security
 Vulnerability Research

# Copy Fail: 732 Bytes to Root on Every Major Linux Distribution.

Xint Code disclosed CVE-2026-31431, an authencesn scratch-write bug chaining AF_ALG + splice() into a 4-byte page cache write. A 732-byte PoC gets root on Ubuntu, Amazon Linux, RHEL, SUSE.
Apr 29, 2026
Contents
What Makes Copy Fail Different
The Root Cause: Page Cache Pages in the Writable Scatterlist
The Trigger: authencesn's Scratch Write
How This Happened
The Exploit
The Demo
The Fix
Remediation
Coordinated Disclosure Timeline
How We Found It

Copy Fail: 732 Bytes to Root on Every Major Linux Distribution.

Xint Code Research Team

Copy Fail(CVE-2026-31431) is a logic bug in the Linux kernel'sauthencesncryptographic template. It lets an unprivileged local user trigger a deterministic, controlled 4-byte write into the page cache of any readable file on the system. A single 732-byte Python script can edit a setuid binary and obtain root on essentially all Linux distributions shipped since 2017.

The kernel never marks the corrupted page dirty for writeback, so the file on disk remains unchanged and ordinary on-disk checksum comparisons miss the modification. However, the page cache is what actually gets read when accessing the file, so the corrupted in-memory version is immediately visible system-wide. A local unprivileged user can turn this into root by corrupting the page cache of a setuid binary. The same primitive also crosses container boundaries because the page cache is shared across the host.

This finding was AI-assisted, but began with an insight from Theori researcher Taeyang Lee, who was studying how the Linux crypto subsystem interacts with page-cache-backed data. He usedXint Codeto scale his research across the entire crypto subsystem, andCopy Failwas the most critical finding in the report.

This is the first in a two-part series:

* Part 1(this post): The bug and local privilege escalation
* Part 2: Kubernetes container escape

## What MakesCopy FailDifferent

The Linux kernel has had high-profile privilege escalation bugs before. Dirty Cow (CVE-2016-5195) required winning a race condition in the VM subsystem's copy-on-write path. It often needed multiple attempts and sometimes crashed the system. Dirty Pipe (CVE-2022-0847) was version-specific and required precise pipe buffer manipulation.

Copy Failis a straight-line logic flaw. It triggers without races, retries, or crash-prone timing windows.

Portable.The same exact script works on every tested distribution and architecture, including Ubuntu, Amazon Linux, RHEL, and SUSE. No per-distro offsets. No recompilation. No version checks in the exploit.

Tiny.The entire exploit is a short Python script using only standard library modules (os,socket,zlib). It requires Python 3.10+ foros.splice. No compiled payloads, no dependency installation.

Stealthy.The write bypasses the ordinary VFS write path. The corrupted page is never marked dirty by the kernel's writeback machinery. Standard file integrity tools comparing on-disk checksums will miss it, because the on-disk file is unchanged. Only the in-memory page cache is corrupted.

Cross-container impact.The page cache is shared across all processes on a system, including across container boundaries.Copy Failis not just a local privilege escalation. It is a container escape primitive and a Kubernetes node compromise vector (Part 2).

## The Root Cause: Page Cache Pages in the Writable Scatterlist

AF_ALGis a socket type that exposes the kernel's crypto subsystem to unprivileged userspace. A user can open a socket, bind to any AEAD (Authenticated Encryption with Associated Data) template, and invoke encryption or decryption on arbitrary data. No privileges required.

A core primitive underlying this bug issplice(): it transfers data between file descriptors and pipes without copying, passing page cache pages by reference. When a user splices a file into a pipe and then into anAF_ALGsocket, the socket's input scatterlist holds direct references to the kernel's cached pages of that file. The pages are not duplicated; the scatterlist entries point at the same physical pages that back everyread(),mmap(), andexecve()of that file.

For AEAD decryption, the input isAAD (associated authenticated data) || ciphertext || authentication_tag. Insidealgif_aead.c,recvmsg()sets up the operation as in-place, meaning the same scatterlist serves as both input and output for the crypto algorithm.

The AAD and ciphertext data are byte-copied from the input scatterlist into the output buffer viamemcpy_sglist. This is a real copy. The page cache pages are only read. But the authentication tag, the lastauthsizebytes of the input scatterlist, is not copied. The kernel retains the scatterlist entries for the tag and chains them onto the end of the output scatterlist usingsg_chain():

Input SGL: AAD ||
 CT 
||
 Tag
 
|
 
|
 ^
 
|
 copy 
|
 
|
 sg_chain (still references page cache pages)
 v v 
|
Output SGL: AAD ||
 CT -----+

The output scatterlist now has two regions: the user'srecvmsgbuffer (containing copied AAD and ciphertext), followed by the chained tag pages, still referencing the original page cache pages of the target file. The kernel setsreq->src = req->dst, both pointing to the head of this combined chain:

req->src ----+
 |
 
v

req->dst --> [ AAD |
| CT
 ] --> [ Tag (page cache pages) ]
 | 
| | |
 +-- RX
 buffer ---+ +-- chained from TX SGL -+
 | 
(user
 mem) | 
(file
's page cache)

This in-place design is the root cause of the vulnerability. It places page cache pages in a writable scatterlist, separated from the legitimate write region by nothing more than an offset boundary. The design assumes every AEAD algorithm will confine its writes to the intended destination, but nothing in the API enforces this, and nothing documents it as a requirement.

Unfortunately, one AEAD algorithm breaks this silent invariant.

## The Trigger:authencesn's Scratch Write

The kernel's AEAD API defines a clear output contract for decryption: the destination buffer receivesAAD || plaintext, exactlyassoclen + (cryptlen - authsize)bytes.

authencesnis an AEAD wrapper used by IPsec for Extended Sequence Number (ESN) support. IPsec uses 64-bit sequence numbers split into a high half (seqno_hi, bytes 0–3 of the AAD) and a low half (seqno_lo, bytes 4–7). The wire format carries onlyseqno_lo;seqno_hiis implicit. For HMAC computation,authencesnneeds to rearrange these bytes:seqno_hiat the front of the hash input,seqno_loappended at the end.

It performs this rearrangement by using the caller's destination buffer as scratch space. Incrypto_authenc_esn_decrypt():

scatterwalk_map_and_copy
(tmp, dst, 
0
, 
8
, 
0
); 
// read AAD bytes 0–7

scatterwalk_map_and_copy
(tmp, dst, 
4
, 
4
, 
1
); 
// overwrite dst[4..7] with seqno_hi

scatterwalk_map_and_copy
(tmp + 
1
, dst, assoclen + cryptlen, 
4
, 
1
); 
// write seqno_lo after the tag

The first two calls shuffle the ESN bytes within the AAD region, a temporary modification that gets restored. The third call writes 4 bytes at offsetassoclen + cryptlen, past the AEAD tag. The algorithm is using memory it does not own as a scratch pad.

The original bytes at that position are permanently lost.crypto_authenc_esn_decrypt_tail()readsseqno_loback to reconstruct the AAD, but never writes the original content back todst[assoclen + cryptlen]. The position is treated as expendable scratch, regardless of whether the operation succeeds or fails.

No other standard AEAD algorithm in the kernel does this. GCM, CCM, and regularauthencall confine their writes to the legitimate output area.authencesnalone writes past the boundary.

In theAF_ALGin-place path, this write crosses from the output buffer into the chained page cache tag pages.scatterwalk_map_and_copywalks past the RX buffer, maps the page cache page viakmap_local_page, and writesseqno_lodirectly into the kernel's cached copy of the target file. The HMAC computation then runs and fails (the ciphertext is fabricated), sorecvmsg()returns an error, but the 4-byte controlled write persists.

Crucially, the attacker controls three things:

Which file:Any file readable by the current user.

Which offset:The tag region corresponds to the lastauthsizebytes of the spliced file data. By choosing the splice file offset, splice length, andassoclen, the attacker determines exactly which 4 bytes within the file's page cache are overwritten.

Which value:The 4-byte overwrite value (seqno_lo) comes from bytes 4–7 of the AAD, constructed by the attacker insendmsg().

## How This Happened

In 2011,authencesnwas added to the kernel (a5079d084f8b) to support IPsec ESP's 64-bit Extended Sequence Numbers (RFC 4303). From the start, the code used the caller's destination scatterlist as scratch space for ESN byte rearrangement. This was harmless at the time: under the old AEAD interface, associated data lived in a separate scatterlist, and the only caller was the kernel's internal xfrm layer. Nobody else ever observed the intermediate writes.

Four years later, in 2015,AF_ALGgained AEAD support (algif_aead.c), with asplice()path that could deliver page cache pages into the crypto scatterlist. In the same year,authencesnwas converted to the new AEAD interface (104880a6b470), introducing theassoclen + cryptlenoffset that writes past the output boundary. ButAF_ALGused out-of-place operation at this point:req->srcandreq->dstwere separate scatterlists. Page cache pages were in src (read-only). The scratch write went to dst (the user's buffer). Not yet exploitable.

Then in 2017, an optimization was added toalgif_aead.c(72548b093ee3) to perform AEAD operations in-place. For decryption, the code copied AAD and ciphertext data from the TX SGL into the RX buffer, but chained the tag pages by reference usingsg_chain(). It then setreq->src = req->dst. Page cache pages from splice were now in the writable destination scatterlist.authencesn's write atdst[assoclen + cryptlen]now walked into those chained tag pages, creating this bug.

Nobody connected the 2017 in-place optimization toauthencesn's scratch writes or to the splice path's use of page cache pages. Each change was reasonable in isolation. The vulnerability exists at the intersection of all three, and has been silently exploitable for nearly a decade.

## The Exploit

The default exploit path targets/usr/bin/su, a setuid-root binary widely present on major Linux distributions, including all four we tested.

Step 1: Socket setup.Open anAF_ALGsocket and bind toauthencesn(hmac(sha256),cbc(aes)). Set a key. Accept a request socket. No privileges required;AF_ALGis available to unprivileged users by default.

Step 2: Construct the write.For each 4-byte chunk of the shellcode payload, construct asendmsg()+splice()pair. Thesendmsgprovides the AAD: bytes 4–7 carry the 4 bytes to write (seqno_lo). Thespliceprovides the target file's page cache pages as the ciphertext and tag. The AEAD parameters (assoclen, splice offset, splice length) are chosen so thatdst[assoclen + cryptlen]falls on the target offset within/usr/bin/su's.textsection.

Step 3: Trigger the write.recv()triggers the decrypt operation. Insideauthencesn, the kernel reads the ESN bytes from the AAD and writesseqno_loatdst[assoclen + cryptlen]. The scatterwalk crosses from the output buffer into the chained page cache page. Four bytes are written to the kernel's cached copy of/usr/bin/su. The HMAC is computed over the rearranged data and fails. The kernel readsseqno_loback to restore the AAD, but the original bytes at the tag position are never restored.recvmsgreturns an error. The page cache is corrupted.

Step 4: Execute.After all chunks are written, callexecve("/usr/bin/su"). The kernel loads the binary from the page cache. The page cache version contains injected shellcode. Becausesuis setuid-root, the shellcode runs as UID 0. Root.

a = socket.socket(
38
, 
5
, 
0
) 
# AF_ALG, SOCK_SEQPACKET

a.bind((
"aead"
, 
"authencesn(hmac(sha256),cbc(aes))"
))

# ... set key, accept request socket u ...

u.sendmsg([
b"A"
*
4
 + payload_chunk], [cmsg_headers], MSG_MORE)
os.splice(target_fd, pipe_wr, offset)
os.splice(pipe_rd, alg_fd, offset)
u.recv(...) 
# triggers decrypt → page cache write

## The Demo

We ran the same script on four distributions and observed root on each.

Each terminal starts as userxint(uid=1001). The same 732-byte exploit is downloaded and executed. Every terminal ends at a root shell.

Distribution

Kernel

Ubuntu 24.04 LTS

6.17.0-1007-aws

Amazon Linux 2023

6.18.8-9.213.amzn2023

RHEL 10.1

6.12.0-124.45.1.el10_1

SUSE 16

6.12.0-160000.9-default

These are the four distribution and kernel combinations we directly tested, spanning kernel lines 6.12, 6.17, and 6.18.

## The Fix

Thepatch(a664bf3d603d) revertsalgif_aead.cto out-of-place operation, removing the 2017 in-place optimization entirely. TheFixes:tag points to72548b093ee3, the commit that introduced the in-place design, confirming that the chaining of page cache pages into the writable destination scatterlist is the root cause.

The vulnerable code setreq->src = req->dst, both pointing to a combined scatterlist where page cache pages fromsplice()were chained into the writable destination. The fix separates them:

// Before: src and dst are the same scatterlist (in-place)

aead_request_set_crypt
(&areq->cra_u.aead_req, rsgl_src, 
// RX SGL

 areq->first_rsgl.sgl.sgt.sgl, used, ctx->iv); 
// RX SGL (same)

// After: src is the TX SGL, dst is the RX SGL (out-of-place)

aead_request_set_crypt
(&areq->cra_u.aead_req, tsgl_src, 
// TX SGL

 areq->first_rsgl.sgl.sgt.sgl, used, ctx->iv); 
// RX SGL (different)

req->srcnow points to the TX SGL (which may contain page cache pages from splice).req->dstpoints to the RX SGL (the user'srecvmsgbuffer). Only the AAD is copied from src to dst. The entiresg_chainmechanism that linked page cache tag pages into the writable destination scatterlist is removed.

The commit message captures it: "There is no benefit in operating in-place in algif_aead since the source and destination come from different mappings."

## Remediation

Patch the kernel.ThefixrevertsAF_ALGAEAD to out-of-place operation, eliminating page cache pages from the writable scatterlist.

Update your distribution's kernel package.Major distributions should ship the fix through normal kernel package updates.

For immediate mitigation, blockAF_ALGsocket creation via seccomp or blacklist thealgif_aeadmodule:

echo
 
"install algif_aead /bin/false"
 > /etc/modprobe.d/disable-algif-aead.conf
rmmod algif_aead 2>/dev/null

For container escape impact, see Part 2.

## Coordinated Disclosure Timeline

Date

Event

[2026-03-23]

Vulnerability reported to Linux kernel security team

[2026-03-24]

Initial acknowledgment received

[2026-03-25]

Patches proposed and reviewed

[2026-04-01]

Patches committed to mainline kernel

[2026-04-22]

CVE-2026-31431assigned

[2026-04-29]

Public disclosure (this article)

## How We Found It

Taeyang Lee's earlierkernelCTF workhad mapped out theAF_ALGattack surface. He realized thatAF_ALG+splicecreates a path where unprivileged userspace can feed page cache pages directly into the crypto subsystem and suspected that scatterlist page provenance may be an underexplored source of vulnerabilities.

Meanwhile, other Theori researchers were running Xint Code and finding critical vulnerabilities in kernel code, including Android drivers and XNU. We were looking to expand this work to Linux, and the crypto subsystem was a natural starting point given our existing knowledge of its internals.

Xint Code supports an "operator prompt" which (optionally) allows a human operator to provide additional context to guide the automated scan. In this case, the operator prompt was quite simple:

This is the linux crypto/ subsystem. Please examine all codepaths reachable from userspace syscalls. Note one key observation: splice() can deliver page-cache references of read-only files (including setuid binaries) to crypto TX scatterlists.

After about an hour, the scan was complete, andCopy Failwas the highest severity output.

Xint Code Scan Result of CVE-2026-31431

Note: The scan also identified other high severity vulnerabilities, including another privilege escalation bug. These other bugs are still in the responsible disclosure process.

Xint Codeis a security research tool built for this workflow: a researcher identifies the attack surface, XC analyzes it.

Next: "From Pod to Host," howCopy Failescapes every major cloud Kubernetes platform.

Share article