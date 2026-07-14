---
title: ''
url: https://hackernoon.com/attested-tls-was-supposed-to-be-the-last-trust-boundary-it-isnt-formal-methods-show-how
site_name: tldr
content_file: tldr-attested-tls-was-supposed-to-be-the-last-trust-bou
fetched_at: '2026-07-14T19:32:39.316045'
original_url: https://hackernoon.com/attested-tls-was-supposed-to-be-the-last-trust-boundary-it-isnt-formal-methods-show-how
date: '2026-07-14'
description: Formal methods researchers at TU Dresden found a relay attack in attested TLS. It hits Meta, Cocos AI, Edgeless Systems, and three IETF drafts.
tags:
- tldr
---

New Story
 
482
 
reads

# Attested TLS Was Supposed to Be the Last Trust Boundary. It Isn't. Formal Methods Show How.

by
Sal Kimmich
July 12th, 2026
TLDR 
Translations 
EN
RU
ES
JA
TA
LV
TH
LT
MN
NL
UK
SQ
PS
Your browser does not support the 
audio
 element.
by
Sal Kimmich
@
salkimmich

## Attested TLS Was Supposed to Be the Last Trust Boundary. It Isn't.

A wax seal proves a document is genuine. It does not prove the seal is still attached to the document it was originally stamped onto. Medieval forgers knew this and exploited it for centuries: cut a real seal off one charter, reattach it to a fake one, and the forgery passes inspection, because the seal really is authentic. It's just authenticating the wrong thing.

Confidential computing has just been shown to have the exact same flaw, a thousand years later, in software. Researchers at TU Dresden formally proved that the cryptographic proof a secure cloud enclave gives you, called remote attestation, isn't reliably tied to the actual connection you're using. An attacker who steals one key can silently reroute your "secure" session to a machine they control, and every check on your end still comes back valid, the same way a genuine seal still looks genuine sitting on the wrong document.

This isn't a bug in one product. It's a design flaw shared by Meta's WhatsApp privacy system, Edgeless Systems' Contrast, Cocos AI, the confidential computing industry's own reference implementation, and three IETF draft standards. It has a CVE, and a well-regarded security firm's manual audit of the WhatsApp system missed it entirely before this team found it with a formal prover instead.

Confidential computing has always asked for one specific act of faith: trust the chip vendor, and nothing else. Everything downstream - the hypervisor, the cloud operator, the orchestration layer - is meant to be provably irrelevant once a workload is running inside a Trusted Execution Environment (TEE) and has produced a remote attestation report proving as much. That report is the entire point. It is the artifact that lets a client stop trusting people and start trusting math.

Muhammad Usama Sardar, with co-authors Viacheslav Dubeyko (IBM) and Jean-Marie Jacquet (Université de Namur), has just shown that the protocol carrying that math across the wire does not do what everyone assumed it did. Their paper, accepted at ESORICS 2026 and titled"Intra-handshake.fail", used the symbolic verification tool ProVerif to formally analyze seven distinct ways the industry has proposed for binding attestation evidence to a TLS session. All seven fail to stop a relay attack.

The disclosure producedCVE-2026-33697, CVSS 7.5. The team says three more CVEs are being worked through responsible disclosure with an expected severity around 9.1. Those three remain undisclosed while vendors patch, so this piece sticks to what is public and citable: the intra-handshake finding.

 
 

### What "attested TLS" is actually promising

Remote attestation, standardized loosely under IETF RATS (Remote Attestation Procedures), lets a TEE produce cryptographic evidence of its own integrity, typically a signed measurement of the code and configuration it's running. Attested TLS tries to fuse that evidence into the TLS 1.3 handshake itself, so a client gets confidentiality and authenticity of the channel and a proof of TEE integrity in one negotiation. This is the intra-handshake approach: evidence generated and verified during the handshake, as opposed to attesting after the channel is already up.

The problem the Dresden team formalized is a binding problem. Producing valid attestation evidence is not hard. Proving that evidence belongs tothis specific TLS session, and not some other session an attacker has quietly substituted, is the actual security requirement. The paper defines three escalating binding levels: correlating evidence to the Diffie-Hellman shared secret, to the client's handshake traffic key, and to the client's application traffic key. Only the third level, binding evidence to application traffic, would actually stop a relay attack in practice. Their formal analysis found that none of the seven candidate mechanisms achieve it, including the mechanism their own proposed mitigation improves on, which reaches only the second level.

The seven mechanisms tested weren't hypothetical strawmen. They map directly onto what's shipping and what's been proposed for standardization: the client's TLS nonce (used in Meta's Private Processing whitepaper), the client's attestation nonce, the TLS 1.3 early exporter, the server's public key, and four combinations of the above. One of those combinations is exactly the design used by Edgeless Systems' Contrast, byCocos AI, and by theConfidential Computing Consortium Attestation SIG's own adopted proof-of-concept project. A further combination is what's proposed indraft-fossati-tls-attestation. The team's conclusion is blunt: the more recent IETF drafts,draft-fossati-seat-early-attestationanddraft-ritz-seat-facts, add protocol complexity without closing the binding gap.

 
 

### The attack in one sentence

If an attacker can extract the ephemeral TLS private key from inside the TEE, or otherwise position themselves during the handshake, they can present the genuine service's valid attestation evidence to the client while terminating the actual TLS session at their own relay point. The client's verification logic runs correctly; the nonce checks out, the signature checks out. The client is simply encrypting its traffic to the wrong endpoint.

Getting that key is not free, and the paper is specific about the two ways it happens. One is provisioning the private key at runtime from outside the enclave, which is not genuine confidential computing to begin with and would surface in an ordinary code review. The other is extracting it by physically compromising the hardware, which today is the only realistic path in a properly implemented deployment, and it's the same class of attack demonstrated by wiretap.fail and TEE.fail. The binding flaw itself has no hardware precondition. Turning that flaw into a working exploit against real confidential computing, as of today, does.

TheGitHub security advisoryfor the Cocos AI instance of this classifies it as CWE-322, key exchange without entity authentication, which is a precise description: the attestation report authenticates the TEE, but nothing authenticates that the TEE is actually the thing terminating your channel.

 
 

### The oldest version of this problem, and its formal name

Long before cryptography existed, the seal metaphor at the top of this piece was a real attack, not a figure of speech. Medieval European chanceries authenticated charters with wax or lead seals, often pendent ones, hanging from the document on cords or a folded strip of parchment. Forgers figured out early that a genuine seal could be cut from one document and reattached to a forged one, and inspection would pass, because the seal really was authentic. It just wasn't authenticating the thing you were looking at.

Chancery practice eventually adapted specifically to defeat this. Pendent seals were designed so the cords ran through and were knotted inside the wax itself, meaning a forger who tried to remove and reuse the seal would almost always break it. That's a physical binding mechanism, built centuries before anyone had a word for the underlying attack, solving the exact same problem the Dresden paper is describing: a valid credential is worthless if it isn't cryptographically or physically tied to the specific artifact it's meant to authenticate.

Cryptographers gave this attack shape a formal name much later. Yvo Desmedt described it in 1988 as mafia fraud: a dishonest prover with no real secret sits between two honest parties and simply relays challenges and responses, letting each party authenticate the other without either realizing a middleman is doing the work. It's better known by its folk name, thechess grandmaster problem, formalized by Beth and Desmedt in 1990: someone with no chess skill at all can beat a grandmaster by simultaneously playing a second grandmaster and relaying each one's moves to the other. Neither grandmaster is cheated on the board, they're just playing each other through an oblivious intermediary.

That is exactly the shape of the intra-handshake relay. The client's cryptographic checks are never wrong about the validity of the evidence. They're wrong about who is actually on the other end of the wire, the same way a medieval clerk was never wrong that the seal was genuine, only wrong about which document it belonged to.

Cryptographers have had a working answer to mafia fraud since 1993, and it's the digital descendant of that knotted cord. Brands and Chaum introduceddistance-bounding protocolsat EUROCRYPT that year, defeating relay attacks by having the verifier time rapid challenge-response exchanges tightly enough that a relay introduces detectable latency. It's not a theoretical fix either. Drimer and Murdoch's 2007 USENIX Security paper,"Keep Your Enemies Close,"demonstrated relay attacks against Chip-and-PIN smartcards in the wild and proposed distance bounding as the practical countermeasure, and contactless payment systems have since partially adopted versions of it.

None of the seven binding mechanisms Sardar's team tested include any timing or liveness component. They're all static cryptographic binding, checking that a value was signed correctly, never checking that the response arrived from somewhere close enough, fast enough, to rule out a relay. Whether distance bounding is even practical for a TEE attestation channel, given cloud network jitter, is genuinely unexplored territory, and it's the most interesting open research question this paper leaves on the table.

 
 

### This is not the first time formal methods caught what manual review missed

Affected implementations named in the paper and subsequent coverage include Meta's Private Processing system underpinning WhatsApp, Edgeless Systems' Contrast, and Cocos AI across every version from 0.4.0 through 0.8.2, even after Cocos AI's aTLS implementation was substantially redesigned in v0.7.0. The redesign changed the mechanism. It did not change the binding level. That's the part worth sitting with if you evaluate vendor security posture for a living: a full protocol rewrite still landed on an architecturally insufficient binding, because the flaw was never in the implementation detail, it was in the choice of what to bind evidence to.

The detail that should worry procurement and audit teams more than the CVE score is what happened at Meta specifically. Meta had commissioned a security review of the WhatsApp implementation from Trail of Bits before Sardar's team looked at it, and that review did not catch the relay attack. This is not a competence story. According toreporting in The Register, Sardar's team contacted Trail of Bits directly and confirmed that no formal methods were used in that review. A manual audit, run by a well-regarded firm, checking the correct properties in the wrong way, missed a class of bug that a symbolic prover found reliably.

Sardar put it plainly to The Register: attested TLS, as implemented today, is not mature yet. He was equally clear about where the trust floor sits and does not move: confidential computing still requires trusting the hardware vendor, full stop; that assumption isn't what broke here. What broke is everything the protocol was supposed to build on top of that assumption.

 
 

There's a more recent precedent too, and it's one of the founding stories of protocol formal verification as a field. The Needham-Schroeder public-key protocol was published in 1978 and treated as sound, cited, taught, and implemented for seventeen years. In 1995, Gavin Lowe ran it through the FDR model checker andfound a man-in-the-middle attackthat had been sitting there the entire time. The flaw only appeared when you reasoned about two interleaved runs of the protocol at once, an initiator running the protocol with a dishonest party who then reuses the initiator's own message to impersonate them to an honest third party. It's exactly the kind of combinatorial trace-space a human reviewer doesn't naturally hold in their head, but a model checker exhaustively searches.

 
 

Seventeen years of manual scrutiny missed it. A tool found it in an afternoon. Formal methods people have been pointing to Lowe's attack for thirty years as the canonical argument for automated verification over manual review, and CVE-2026-33697 is the same argument playing out again, in production, against a much larger surface.

TLS itself has been down this exact road before, twice, and both times the failure was the same category: authentication material getting bound to the wrong session. The TLS renegotiation vulnerability, CVE-2009-3555, disclosed by Ray and Dispensa in 2009, let an attacker splice an unauthenticated request onto the front of a session that later renegotiated as authenticated, because nothing tied the two handshakes together. The fix wasRFC 5746.

Then in 2014, Bhargavan, Delignat-Lavaud, Fournet, Pironti, and Strub published theTriple Handshake attackat IEEE Security and Privacy, showing that TLS session resumption and renegotiation didn't properly bind the master secret to the full handshake transcript, letting an attacker synchronize two sessions a client believed were identical. The fix that came out of that work isRFC 7627, the Extended Master Secret, a channel-binding fix in the literal sense: it forces the session key to depend on the entire handshake transcript rather than a partial one. That's the same design move the Dresden team's binding levels are reasoning about, expressed as a spectrum instead of a single patch.

The lineage is closer than a shared attack shape. The Triple Handshake work came out of INRIA's Prosecco group, and both Karthikeyan Bhargavan and Bruno Blanchet, the creator of ProVerif itself, are thanked by name in the Intra-handshake.fail acknowledgments for the foundational formal model of TLS 1.3 their earlier work provided. The tool that just found this bug and the research tradition that found the last major TLS binding bug of this kind are not just similar in spirit, they share an actual lineage of people and methods.

All of this rests on a modeling assumption that's worth naming once, because it explains why code review and cryptanalysis both miss this class of bug. Formal protocol analysis sinceDolev and Yao's 1983 paperassumes an attacker who fully controls the network, intercepting, replaying, reordering, and injecting messages at will, but who cannot break the underlying cryptography. Under that model, every signature in the Cocos AI, Contrast, and Meta implementations verifies correctly. The cryptography is not broken. The protocol logic, reasoned about under a network-level adversary, is. That gap between "the crypto primitives are sound" and "the protocol composition is sound" is precisely where a medieval seal forgery worked, where Needham-Schroeder failed in 1995, and where attested TLS failed in 2026.

 
 

### How this compares to the rest of 2025 and 2026's confidential computing CVEs

Formal-methods findings in protocol design tend to look abstract next to physical side-channel attacks, so it's useful to put CVE-2026-33697 next to its neighbors, using the same comparison the researchers make in their own paper:

* wiretap.fail and TEE.fail(Georgia Tech, Purdue, Synkhronix, late 2025): physical DDR5 memory bus interposition against Intel TDX and AMD SEV-SNP, extracting attestation keys directly from the memory bus. No CVE assigned by Intel, treated as an out-of-scope physical attack. These two share a category name with an older attack class worth knowing:wormhole attacks, described by Hu, Perrig, and Johnson at INFOCOM 2003 in the context of ad hoc network routing, where two honest nodes get tunneled through an attacker without either realizing it. It's mafia fraud's cousin, applied to routing instead of authentication.
* TDXdown: CVSS 2.5, acknowledged by Intel.
* BadRAM: CVSS 5.3, acknowledged by AMD.
* Staleus(CVE-2025-54509): CVSS 4.0.
* BreakFAST(CVE-2025-61971 and CVE-2025-61972): CVSS 5.9 and 4.2.
* Fabricked(CVE-2025-54510): CVSS 5.9.
* CVE-2026-33697:CVSS 7.5, the highest-scored entry in that comparison set, and the only one that requires no physical hardware accessto exist as a design flaw. Exploiting it today, however, still starts with obtaining the enclave's private key, which realistically means a physical attack of the same class as wiretap.fail or TEE.fail.It's a pure protocol design flaw, reachable over the network once that key is in hand, against a mechanism that three separate production systems chose independently.

That last point is the one I'd want a CISO to actually absorb. Physical bus interposition attacks are serious, but they require an adversary with hands on hardware, a threat model most cloud tenants have already priced in as "someone with data center access, which is already a catastrophic trust failure." A relay attack against the handshake doesn't remove that requirement, it compounds it: once an attacker clears that bar, this flaw turns what might have been a contained key leak into a full, undetected session takeover. It's a protocol-layer bug with a network-layer blast radius, and it scored higher than any of the physical attacks it's being compared against.

### What the fix actually requires

The paper's proposed mitigation reaches binding level 2, correlating evidence to the client's handshake traffic key, a real improvement over every mechanism currently shipping. But the authors are explicit that level 3, binding to application traffic, may not be achievable through intra-handshake attestation at all, regardless of which combination of nonces and keys you throw at it. The IETF TLS, RATS, SEAT, and LAKE working groups are now formally reviewing it.

If that holds up under further scrutiny, some proposals may need to move attestation out of the handshake entirely, borrow something like a distance-bounding liveness check, or accept a weaker binding guarantee than implementers have been assuming. None of those outcomes is comfortable for a standards body trying to ship interoperable specs on a timeline, and none is comfortable for vendors who've already shipped production systems on the assumption that binding to the server's public key was good enough.

For anyone tracking the CRA (Cyber Resilience Act) angle: this is exactly the kind of finding that Article 14 vulnerability handling obligations were written to surface faster than a two-year gap between shipping and formal review. A protocol flaw sitting quietly in production TLS handshakes since before 2025, in systems that had already been through vendor-commissioned security review, is the argument for mandating formal verification as part of conformance rather than treating it as a research nicety. Medieval chanceries needed centuries to arrive at the knotted cord. Lowe needed a model checker to catch what seventeen years of manual review missed in 1995. Nothing about the economics of that trade-off has changed since, it's just gotten more automatable.

 
 

### Credit where it's due

This CVE has three discoverers, not one. The advisory itself credits Muhammad Usama Sardar (TU Dresden), Viacheslav Dubeyko (IBM), and Jean-Marie Jacquet (Université de Namur) jointly, and Sardar has been explicit in public that coverage naming only him gets it wrong. Finding the highest CVSS-scored vulnerability in a decade of confidential computing research is not a solo act, and this piece credits all three by name for that reason.

The work also sits inside a wider circle of institutional and individual support worth naming. Contributors connected to the Confidential Computing Consortium, the IETF, the IRTF, and GA4GH (the Global Alliance for Genomics and Health) fed into the research over time, largely through the working groups where attested TLS is actually being fought over and standardized. Germany's Federal Office for Information Security, the BSI, gets a specific mention from Sardar for backing a skeptical read of confidential computing's sovereignty claims well before any of this became a public CVE.

On the technical side, Sardar has named the following as directly insightful and instrumental to this specific paper: Eric Rescorla, Juho Forsén, Markus Rudy, Mariam Moustafa, Bruno Blanchet, Steve Kremer, Tjaden Hess, Martin Thomson, Yuning Jiang, Pavel Nikonorov, Casey Wilson, Danko Miladinovic, and SongBo Bu. A longer list of contributors going back further is public in the team's own conference materials, linked from the disclosure repository.

 
 

### Where to look yourself

The CVE record is public atCVE-2026-33697. The GitHub security advisory for the Cocos AI instance has the clearest technical writeup:GHSA-vfgg-mvxx-mgg7. TheResearchGate preprintof the full paper is available now, ahead of the ESORICS 2026 proceedings, which run September 14 to 18, 2026, in Rome. The team has also filed the finding with the IETF RATS, SEAT, TLS, and LAKE working groups. TheRegister's reportingis worth reading in full for what it documents about the disclosure process itself, not just the vulnerability.

Confidential computing's whole pitch has been that you no longer have to trust the operator, only the silicon. That pitch still holds. What this research shows is that the layer we built to prove the silicon's integrity to a remote client wasn't proven itself, not with the rigor the claim deserved. The seal was never the problem, and it never was, going back a thousand years. What's missing is proof the seal is still attached to the document you think it is.

Formal methods didn't break attested TLS. They found that it was already broken, and had been for a while, in the same way the same class of proof has found the same class of flaw for thirty years running, on a problem forgers were already exploiting long before anyone wrote a line of code.

 
 

### Key takeaways, for everyone else

You don't need to work in confidential computing for this to matter. Here's what carries over.

"We had it audited" is not a security property.Meta paid a well-regarded firm to review the exact system that turned out to be broken. The audit passed. The flaw was still there. What matters is not whether a review happened, but what method it used and what it was actually capable of finding. Ask that question about any of your own vendors' security claims, not just this one.

Passing every check is not the same as being secure.In this vulnerability, every cryptographic check the client runs comes back correct. Nothing looks wrong. That's what makes relay attacks dangerous everywhere, not just in TLS: a system can be internally consistent and still be talking to the wrong party. If a security model's only defense is "the signature checks out," ask what it does when the signature is real but the location isn't.

New technology can inherit old mistakes wearing a new name.Medieval clerks solved a version of this problem with a knotted cord. Cryptographers solved a version of it with distance bounding in 1993. AI-driven confidential computing built a new protocol in 2025 and ran straight into the oldest trap in the book anyway. Novelty is not the same as having learned from the last version of the problem, or the first one.

Automated formal verification is now catching what expert manual review misses, consistently, across decades.The same pattern that broke a widely trusted protocol in 1995 broke one in 2026. If you fund security work, that's a budget argument: paying for formal methods up front is cheaper than a public CVE after a product has shipped to production.

If you use or evaluate any product marketed as "confidential" or "attested," ask one specific question.Does the attestation get bound to the full session, or just to a key? Right now, across every production system this research tested, the honest answer is "just to a key." That gap is exactly what this vulnerability exploits, and no patch closes it yet.

Can’t get enough of this formal methods breakdown? Then I suggest you read the original paper onIntra-Handshake Failnow.

Wado.

 
 

Sources: CVE-2026-33697 (CVE.org / NVD); GHSA-vfgg-mvxx-mgg7 (Cocos AI security advisory); "Intra-handshake.fail (CVE-2026-33697): High-severity CVE in Attested TLS," Sardar, Dubeyko, and Jacquet, accepted ESORICS 2026; The Register, "Confidential computing's core trust mechanism is broken. The fix may not exist," July 4, 2026; SC World, "Confidential computing's remote attestation protocol may have fundamental flaw"; Wikipedia, "Seal (emblem)," on pendent seal construction and reattachment forgery; Lowe, "An Attack on the Needham-Schroeder Public-Key Authentication Protocol," 1995; Desmedt, "Major Security Problems with the 'Unforgeable' (Feige)-Fiat-Shamir Proofs of Identity and How to Overcome Them," SecuriCom 1988; Beth and Desmedt, "Identification Tokens, or: Solving the Chess Grandmaster Problem," 1990; Brands and Chaum, "Distance-Bounding Protocols," EUROCRYPT 1993; Drimer and Murdoch, "Keep Your Enemies Close," USENIX Security 2007; Bhargavan et al., "Triple Handshakes and Cookie Cutters," IEEE S&P 2014; Ray and Dispensa on TLS renegotiation, 2009; Dolev and Yao, "On the Security of Public Key Protocols," 1983.

 
 

← Previous

The Volunteer DDoS: Why AI Security Tools Are Breaking the Infrastructure They're Meant to Protect

### About Author

by
Sal Kimmich
|
@
salkimmich
CEO
 at 
 
Gadfly AI

Focused on the open source software supply chain to build a better digital future for all of us.

Subscribe
Read my stories
About @salkimmich

#### TOPICS

cybersecurity
#
cybersecurity
#
cyber-threats
#
confidential-computing
#
cve
#
open-source
#
ietf
#
ai-cyber-security
#
hackernoon-top-story