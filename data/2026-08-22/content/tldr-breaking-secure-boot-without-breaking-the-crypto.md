---
title: Breaking secure boot without breaking the crypto
url: https://0x434b.dev/breaking-secure-boot-without-breaking-the-crypto/
site_name: tldr
content_file: tldr-breaking-secure-boot-without-breaking-the-crypto
fetched_at: '2026-08-22T19:21:27.041367'
original_url: https://0x434b.dev/breaking-secure-boot-without-breaking-the-crypto/
date: '2026-08-22'
published_date: '2026-08-19T08:26:09.000Z'
description: Breaking Secure Boot Without Breaking the Crypto (57 minute read)
tags:
- tldr
---

This will be mostly rambling disguised as a technical walkthrough. I will touch on certain topics such as hardware roots of trust, signed image formats, Qualcomm boot stages, Android Verified Boot, UEFI, measured boot, and remote evidence (remote attestation). My idea is that I will briefly introduce the concepts and then introduce a seemingly "perfect-world"-example that can still break under certain assumptions. So, expect a technical post leaning towards offensive security.

Note
 I will not claim completeness, each section is to be viewed with caution. This is a massive field spanning multiple vendors, OEMs, concepts and varying implementations. That said, if I messed up completely somewhere please let me know.

## Primer: Trust before the operating system exists

Before any embedded device can start, let's say Linux, mount a root filesystem, enforce SELinux, or contact an update server, something has already selected bytes from mutable storage and transferred control to them. That first transition happens with almost none of the defenses we normally rely on, so the platform has to manufacture trust from a much smaller base: usually an immutable read-only memory (ROM) paired with a one-time-programmable policy (OTP). This forms what's commonly referred to as a "hardwareRoot of Trust (RoT)". The fixed ROM provides unalterable execution code (like a primary bootloader), while OTP components, such as eFuses, permanently store device-unique cryptographic keys, hashes, and security configurations. This minimal base is enough loader code to authenticate the next, bigger stage.

Secure boot,measured boot, andremote attestationare three different consumers of that base I just introduced. Secure boot decides whether a state transition is locally authorized. Measured boot records the transition. Remote attestation packages protected claims into signed evidence so a verifier can compare the device with reference values and policies. A representative embedded system therefore looks less like one signature check and more like two connected protocols:

 local authorization
 -------------------
power-on
 |
 v
+-------------------+ authenticate + validate +------------------+
| mask ROM / PBL |------------------------------>| mutable boot code|
| OTP root-key hash | | BL2 / XBL / TME |
| lifecycle policy | +--------+---------+
+-------------------+ |
 | repeat for
 | TEE, kernel,
 | DTB, firmware
 v
 +---------------+
 | runtime state |
 +-------+-------+
 |
 | measurements
 remote appraisal v
 ---------------- +---------------+
challenge / nonce ------------------------------------>| Attester |
 | protected key |
 +-------+-------+
 |
 | Evidence
 v
 +--------------+
 | Verifier |
 | refs + policy|
 +------+-------+
 |
 | result
 v
 Relying Party

Secure boot and remote attestation, end to end

The above diagram is very rough and mixes terminology across different vendors (e.g., BL2, XBL, SBL). So we'll look at these elements more closely later in the post. The goal is more that it serves as a general, loose introduction.

## Secure boot and remote attestation, from reset to remote policy

Secure boot is a hardware-rooted authorization process in which an already trusted stage authenticates and validates the next security-relevant transition before allowing it to execute. "Authenticates" covers signatures and certificate chains. "Validates" covers what the signature alone cannot decide: image type, hardware target, load range, lifecycle, debug policy, version, rollback floor, and whether this path is permitted in production. In short, a boot stagendecides whether the next in line boot stagen+1is allowed to proceed based on a pre-defined set of checks.

Now, there's still the distinction between authentication and validation, and between signatures and certificates. A valid signature only proves one narrow thing: that a holder of an accepted private key authorized some specific byte string at some point. That is a much smaller claim than people tend to read into it. Almost everything that makes secure boot actually work lives in the gap between "these bytes were signed" and "this device may run this code right now." So, concretely, a valid signature doesnotprove that:

* Every byte the loader later consumes was inside that signed string. A signature covers one specific range, so any header field, metadata, or second payload that sits outside it was never authorized.
* The signer meant this image for this chip and this lifecycle. The same valid signature could belong to a different product or to a development build that should never run on a shipped device.
* The image is current. An old build stays bit-for-bit authentic forever, even after a newer version patches a hole in it.
* The caller actually acted on the result. A verifier can compute "reject" and the surrounding code can still hand control to the image anyway.
* The verified buffer stayed put until execution. Bytes can be checked in one place and quietly swapped before the CPU runs them.
* The signed code is safe. "We authorized this" is not the same as "this is memory-safe, correctly configured, or benign."
* The firmware is secret. Signatures authenticate. They do not encrypt, so anyone can still read the image straight off the flash.
* The device stays in that state afterward. "The image on storage was authentic at boot" and "the device is uncompromised right now" are two different claims.

If you squint, that list is a table of contents for the second half of this post: each line is one way a mathematically perfect signature check still lets unsigned code run. It is also where the split between authentication and validation earns its keep. Authentication answers a narrow question: is this signature valid, and does the keychain back to a root I trust? A certificate chain only helps with that half. It vouches that a key descends from a trusted root, not that the key was allowed to sign this particular image. Validation is everything else: the right image type, the right product, the right lifecycle, the right version, and whether this path is even permitted here. The signature math can be flawless, and every one of those validation questions can still be answered wrong.

If we wanted to go a little deeper and consult a framework regarding embedded security, we could take a look atNIST SP 800-193. This separates firmware resilience into three categories: protection, detection, and recovery. Secure boot is mostly a protection mechanism. Measured boot and attestation contribute to detection. Neither automatically provides recovery.

NOTE
 None of the three categories introduced by NIST mean much if an alternate path can bypass the mechanism entirely.

### Authenticated, verified, measured, and attested boot

We've juggled a lot of these buzzwords, so here is the short version of what each one does, what it produces, and who consumes it:

Boot type

What it does

What it produces

Who consumes it

Authenticated boot

Checks the next image's signature against an accepted key.

A yes/no answer to: "Is this signed by someone we trust?"

The current stage's own decision logic.

Verified boot

 Authenticates, then validates policy such as type, target,
 version, and lifecycle, and enforces it.
 

 A boot that proceeds only with a fully authorized image,
 or otherwise halts.
 

The device itself, at every handoff.

Measured boot

 Hashes each stage and records the digest into protected,
 append-only state.
 

A tamper-evident record of what actually ran.

Later stages, and ultimately attestation.

Attested boot

 Signs those measurements together with device identity
 and a fresh nonce.
 

 Evidence that a remote party can check against reference values.
 

A remote verifier or relying party.

Ameasurementhere just means a cryptographic hash of the bytes a stage is about to run, written into a protected state a later stage can add to but never rewrite. Depending on the device class, these are kept inTPM PCRs. On a more resource-constrained device, they may be used straight in key derivation. We will touch upon that a little in the later following "DICE" section. With those pinned down, let's condense the earlier diagram using them:

 LOCAL DECISION (DEVICE)

+-------------------------------------------+
| |
| storage |
| | |
| v |
| load |
| | |
| v |
| hash / authenticate |
| | |
| +--------------------+ |
| | | |
| v v |
| secure boot policy measure |
| | | |
| | v |
| | protected claim set |
| | | |
| | v |
| | sign(nonce, claims) |
| | | |
| +--> execute | |
| | | | |
| | v | |
| | run | |
| | | |
| +--> reject / | |
| recovery / halt | |
| | |
+--------------------------|----------------+
 |
 | attestation evidence
 v

================================================
 DEVICE / VERIFIER BOUNDARY
================================================

 |
 v

 REMOTE DECISION (VERIFIER)

 verify signature
 |
 v
 verify nonce
 |
 v
 evaluate trust policy
 |
 +-----+-----+
 | |
 v v
 grant / trust deny /
 quarantine

Local device decision vs. remote verifier decision

The mechanisms complement one another. Verified boot refuses a locally unauthorized image, while measured boot records what happened. Remote attestation lets another system decide whether to provision a key, accept telemetry, admit the device to a network, or quarantine it. Recording an unexpected digest does not stop it from running, and enforcing a signature does not tell a remote service what actually happened. So having one over the other is not a security decision to make. It's more about how many layers a product should deploy based on a given threat model.

### What does secure boot protect?

To discuss this topic, we can formulate a hypothesis to build on.

Hypothesis
 Given an attacker targeting a secure device, let's assume: A) They control external flash, an update package, or a recovery transport. B) They can repeatedly reset and physically access a deployed device. C) They may later gain code execution in one mutable boot stage or bus master. D) They cannot forge the production signature or recover the offline root private key. E) They cannot change mask ROM or correctly programmed OTP/eFuses, although ROM code may still contain exploitable bugs.

The aforementioned scenario defines a handful of "rules" but they're basically two buckets: 1) An attacker has physical access, some control over some input data, and hunts for vulnerabilities, and 2) they cannot change the fact that embedded secrets or ROM code are unchangeable/not (easily) extractable.

Now against such an attacker, a properly implemented secure boot chain should stop persistent replacement of boot firmware, kernel, TEE components, coprocessor images, device trees, and/or root filesystems, given those components are covered by the platform's chain of trust. Adding (monotonic) version state tracking can stop version rollback as the minimum flashable version is directly embedded in, for example, eFuses. Similarly, this mechanism can be used to embed debug and other policies to, for example, disable access over JTAG on a production unit. This foundation can be expanded for a hardware-backed remote attestation as well. But given that this is where secure boot shines, there are ways to work around it. Secure boot does not stop a network exploit against genuine firmware, a ROP chain assembled from signed code, a data-only attack, an authorized old image, or runtime injection through an RWX mapping. Those attacks may later undermine the chain or establish persistence, but "the image on storage was authentic at boot" and "the device is currently uncompromised" remain different claims.

#### The minimum implementation

At reset the ROM code needs to initialize a bare minimum so boot (stages) later on can progress. It is not aware of what "the firmware" is. It only knows and "has access" to a bare minimum of immutable facts, like a hash of an embedded root key, some lifecycle or debug state information, and whether things like secure boot are enabled. Thelifecycle stateis where the device sits in its own timeline: fresh silicon starts in a development or test state (debug open, dev-signed images allowed), and burning a one-time fuse moves it permanently to locked production, which only accepts production-signed images and closes the debug interfaces. That transition is one-way, which is why a production device must reject a dev-signed image even when its signature is perfectly valid.

NOTE
 Everything read from flash is untrusted. That includes certificate chains, image headers, segment tables, load addresses, entry points, other signatures and generally all executable bytes

The ROM loader has to turn untrusted inputs into one precise authorization decision:

1. Who authorized this image?
2. Which bytes and execution parameters did they authorize?
3. Is that current (-ly requested) state allowed on this device?

Most formats answer those questions indirectly. Instead of signing every large segment independently, the signer authenticates a smaller description of said segment. Another name for this description is metadata and policy information. Often this is also referred to as amanifest. When we look at a specific implementation, Qualcomm's signed ELF images use signed image metadata and ahash segmentas highlighted in their public information material.

A signature therefore authenticates the description. The digests inside it bind the description to the underlying data. The loader's role is to reconstruct the claimed image based on that and either accept the proposed data or refuse a handoff to the next boot stage.

fused root hash
 |
 v
[certificate chain] --> leaf key --> verify [signed manifest]
 |
 +--------------------+--------------------+
 | | |
 expected H(A) expected H(B) target/version
 | | ranges/entry
 v v |
 hash [segment A] hash [segment B] |
 | | |
 +--------------------+--------------------+
 v
 lock memory --> jump

Signature anchors the manifest & digests bind each segment

In general, the exact encoding is vendor-specific, but if we were to come up with some pseudo-code, it may look like this:

#define MAX_SEGMENTS 16

struct segment_desc {
 uint64_t file_offset; /* bytes read from the container */
 uint64_t file_size;
 uint64_t load_address; /* physical destination */
 uint64_t memory_size; /* includes zero-filled tail */
 uint32_t permissions; /* R/W/X policy after loading */
 uint8_t sha384[48]; /* digest of this segment */
};

struct signed_manifest {
 uint32_t format_version;
 uint32_t image_id; /* XBL, TEE, ABL, modem, kernel... */
 uint32_t hardware_id;
 uint32_t oem_id;
 uint32_t lifecycle_mask; /* dev, test, production */
 uint64_t security_version; /* anti-rollback value */
 uint64_t entry_point;
 uint32_t segment_count;
 struct segment_desc segment[MAX_SEGMENTS];
};

struct authentication_block {
 struct signed_manifest manifest;
 uint8_t manifest_signature[SIG_MAX];
 uint8_t certificate_chain[CERT_CHAIN_MAX];
};

A signed image: manifest plus segment descriptors

Based on this code, we can argue that signingsegment[i].sha384would be insufficient. An attacker who can alter the load address or change the entry point can change what a genuine segment does without changing its bytes. Therefore, things like an image ID, target, lifecycle state, version, addresses, sizes, permissions, and entry point belong inside the same signed statement. Generally at this stage it needs to be studied which metadata information bits need to be ensured are valid and should never be tampered with as they may cause side effects.

That said, there's one catch. Regardless of anything, the loader must always parse something before it knows where the manifest and signature are. You cannot check a signature/hash/digest if you don't know where it's located. That code responsible is in the pre-authentication parser, and every byte this function reads needs to be treated as hostile. So, this parser should be built in a way that it's as minimal as possible: overflow-safe arithmetic, bounded counts, no attacker-directed writes, etc. We would want to make sure that any interpretation of complex image semantics only happens AFTER an initial authentication.

#### Rollback state is part of authorization

A signature is timeless unless policy gives it a time dimension. As long as a signed image matches the expected signature, it passes. To further tighten a time domain, there exists this notion of rollback state. Rollback state in embedded security is typically represented as an integer security version in a signed manifest and a monotonic floor (never decreasing) stored in an OTP, eFuses, a replay protected memory block (RPMB), or any other similar replay-resistant storage. This version information, while in reality just being an integer comparison, is tied to time as each version has a specific release date. Imagine the following pseudo-code:

uint64_t floor = rollback_read(image_id);

if (manifest.security_version < floor)
 reject(AUTH_ROLLBACK);

boot_verified_candidate();

/* Commit only at the platform's defined successful-update point. */
if (candidate_confirmed_bootable() && manifest.security_version > floor)
 rollback_advance(image_id, manifest.security_version);

Anti-rollback version check and floor advance

While such an integer check for the allowed version is seemingly simple on paper, this check carries a lot more side effects that need to be considered. For example, having a single global floor counter for a full firmware stack is very problematic. Nowadays, firmware is a complex structure of different components. Each component may need different updates, or, as a matter of fact, certain components may be updated over-the-air while others require an OEM/factory treatment. So let's assume we have three components: a bootloader (e.g., an Android one -ABL), a TEE, and a modem. If I update the modem firmware, should I advance the global counter and, in a following update for the bootloader, do the same again? Who keeps track of that, especially if we consider updates may be produced by different teams, vendors, and so on? At the same time, if we consider multiple counters, one for each component, such as defined in a pseudo-manifest:

{
 "components": [
 {
 "image_id": "ABL",
 "security_version": 12
 },
 {
 "image_id": "TEE",
 "security_version": 8 
 },
 {
 "image_id": "MODEM",
 "security_version": 31
 }
 ]
}

Per-component rollback counters

We need to make sure that a counter is securely bound to a component's identity. Suppose an old ABL image carries security version 8, while the established minimum floor has already advanced to 12. The loader must reject that image. If a bug can be abused to make the check compare the old image's ABL version against the TEE's lower floor of 7, the image will get accepted. The loader must therefore establish that it is loading an ABL image and use the correct rollback counter. In the manifest,image_ididentifies the component andsecurity_versioncarries its version. Both must be authenticated. The loader must also compareimage_idwith the component expected at that point in the boot chain before selecting the corresponding rollback floor. Lastly, let's highlight legitimate firmware updates. When is a counter advanced? Advancing the floor before an image is known to boot can brick the device. Advancing it too late leaves a rollback window. So this requires some semantics like:

Update to new version B from A
 -> verify B
 -> trial-boot B
 -> confirm B is healthy
 -> atomically mark B successful and advance floor to n+1

When the rollback floor is safely advanced

#### Failure must be a terminal state

The authentication routine does not stop the processor by itself. It returns a result to its caller. Secure boot exists only if that caller turns every failure into a refusal to execute the requested image. Logging the error would not be enforcement. Neither would be retrying through a weaker boot mode or continuing with whatever remains in the load buffer (skipping the failed check section). A failed check must always reach a terminal state for that boot attempt. Whether that results in a halt, reset, or entering a recovery mode is highly implementation specific. What remains true for all three options is that in no case is there a fall-through where booting continues.

int rc = authenticate_and_validate(&image, &policy);

if (rc != AUTH_OK)
 fail_closed(rc); /* authenticated recovery, reset, or halt; never returns */

if (lock_image_memory(&image) != 0)
 fail_closed(AUTH_MEMORY);

jump_to_verified_entry(image.entry); /* successful handoff; never returns */

__builtin_unreachable();

Every failure path ends closed before handoff

This creates a one-way control flow. Every route until normal execution passes through authentication. Any error ends outside that route.

#### One concrete chain: Qualcomm from reset to Android

So far, we have looked at one authenticated transition: establishing an authority, validating a signed description, reconstructing the image, locking it, and handing it off. A real SoC repeats that transition across several processors and boot modes. Qualcomm's public architecture gives us one concrete graph on which to place the earlier abstractions. What's following isonecurrent design, not auniversalQualcomm specification.

OTP/eFuse: secure-boot configuration, OEM root-certificate hash, lifecycle
 |
 v
 PBL / Boot ROM
 loads and authenticates both
 / \
 v v
 TME final runtime XBL-SC
 mutable SoC RoT loads later images
 authentication and |
 resource services <----------+
 | authenticate, then assign resources
 v
 +-------------+------------------+
 | | |
 v v v
 TEE / hypervisor peripheral and OS bootloader
 management fw (for example UEFI)
 |
 Android: libavb
 verifies VBMeta
 |
 +------------------+------------------+
 | |
 v v
 hash descriptors hashtree roots
 boot / vendor_boot / ... system / vendor / ...
 | |
 +------------------+------------------+
 v
 Linux + dm-verity

PBL / Boot ROM -- product-dependent trigger --> USB EDL
 |
 Sahara + programmer
 |
 Firehose
 storage/memory operations

A Qualcomm boot chain, reset to Android

Don't try to memorize TME versus XBL-SC versus Sahara. The thing that matters for the remainder of this article is that every arrow is the same authenticate-then-hand-off decision that we introduced in the earlier section(s). They're just different names for the same concept. Anyhow, looking at the diagram above, we start at the primary bootloader (PBL), the immutable ROM bootloader. Its behavior is constrained by a one-time programmable configuration, including the secure-boot one and the OEM root-certificate hash. During this stage the "Trust Management Engine" (TME) provides authentication services while the PBL loads and authenticates both the final TME runtime and the eXtended (secure) bootloader (XBL-SC). Qualcomm describes those two images together as the second stage bootloader functionality. Afterward their roles split, XBL-SC initializes hardware and loads later images from storage. It calls the TME to authenticate those and assigns expected resources with them as well. This covers the application-processor images, such as the TEE, hypervisor, and operating system bootloader, in addition to the peripheral and management controller firmware. Further down the boot process, TME hands resources to their final owners.

While the above is way more complex than what we discussed in the minimal implementation, above we can kind of say that every edge is what the minimal implementation describes. Each Qualcomm signed-ELF transition instantiates the contract from the previous section. XBL-SC parses and loads from untrusted storage, TME authenticates signed metadata and segment hashes, policy binds the image to its intended hardware and role, and destination addresses are checked against allowlisted memory. Just as a brief introduction, since it recurs in the failure cases later:Android Verified Boot (AVB)is Android's secure boot,libavbis its reference verification library, andVBMetais the signed manifest that library checks. Android Verified Boot follows the same abstract contract at the OS boundary, but with VBMeta and libavb rather than Qualcomm's signed-ELF format.

So overall, the labels change, but the contract/functionality does not. Additionally, the graph also exposes what a straight ROM-to-kernel diagram hides. A modern co-processor usually has its own executable images and, depending on the product's access-control policy, may own or access shared resources before Linux starts. Those images, their signing authorities, rollback counters, and memory permissions are part of the same security domain. So is every component capable of modifying memory that another stage will execute.

Recovery adds another branch. Some products expose a boot-ROM-initiated Emergency Download Mode. One such documented example provides a hardware bootstrap intoUSB EDL. In that mode, a host usesSahara and Firehosewith a product-specific device programmer to provision or rewrite storage, and some programmers expose memory operations as well. On a secure-boot-enabled production device, that programmer is another executable image whose authority and capabilities must be part of the review.

At the Android boundary, the OS bootloader integrates libavb and verifies the top-level VBMeta structure against the device's root of trust. Signed hash descriptors typically carry expected digests for small, read-once partitions, such asboot. Hashtree descriptors authenticate the roots used to verify large filesystems, such assystemas blocks are read. Chain-partition descriptors delegate another signed VBMeta structure to a named key and rollback-index location. VBMeta therefore performs the same manifest role at a different layer. It extends the authorization decision from individual firmware containers to a graph of Android partitions. It is not a Qualcomm hash segment and does not use the same concrete format. That block-by-block check isdm-verity, the Linux device-mapper target that validates each filesystem block against a signed hash tree at read time, so a tampered block fails when it is used rather than needing the whole partition hashed up front.

This was a quick real-world example that likely could be extended with some more knowledge, but it may also warrant its own article when we want a full walkthrough of Android secure boot. That said, it highlights the notion of "verifying every image" in practice. We need to keep track of every executable component, every path that can load another, and every actor that can alter it before execution. Secure boot makes those decisions locally. The next problem we're going to take a look at is how a remote service learns which authorities, images, and configurations a device accepted and whether the configuration stored remotely matches what's running on a device.

### From a local measurement to a remote decision

Now that we have established that secure boot answers a local policy question about whether a device may boot a specified image, we could claim that's the end. The device is secured. But if we consider a device/service operator, the equation changes. There are different decisions to be made: Should the device be provisioned, accept telemetry, expose customer data, or should the device be admitted to a network? These cannot be answered with secure boot alone. Secure boot answers whether an image is authentic and locally allowed based on, e.g., a minimum version, a signing authority, etc.

Additionally, a remote party cannot observe what actually has happened during boot and which boot decisions have been made. It may (if at all) only see the outcome (device booted, device reset/halted). This almost binary outcome proves little. Now we could argue that a device during boot could emit something like a measurement digest for a remote party to observe. But this isnotenough. At any time during the boot process, the software could invent such a digest, replay a captured one, or copy a result from another device. A trustworthy report needs a protected origin, a device identity, and proof that this result was produced as a result of a specific request.

This is where remote attestation comes into play, which acts as a bridge. A protected component reports the preserved measurements and boot state, while the remote service compares those claims with its own reference values and policy. This specific separation of concerns is important. A device reports what it observed. It at no time has any say about whether an observer should trust it.RFC 9334gives us precise naming for the involved roles, inputs, and the exchange itself:

 endorsements reference values appraisal policy
 | | |
 +--------------------+---------------------+
 |
 v
challenge / nonce --> Attester --Evidence--> Verifier --Attestation Result--> Relying Party
 | |
 +-- measurements, lifecycle, debug, version, +-- provision key
 device identity, boot state... +-- admit to network
 +-- quarantine / deny

RATS roles (RFC 9334)

We have an "attester" who produces the "evidence". We have a "verifier" who's appraising it using what's referred to as "manufacturer endorsement." A more established (at least in this article) terminology for endorsements would be "reference values" or "policies." We also have a "relying party" who consumes the resulting verdict and acts upon it. All those roles may collapse into one backend, e.g., in a small IoT/embedded deployment. That said, the separation of concerns here is what prevents asignature is validsilently becomingdevice is trustworthy.

Before requesting evidence, a verifier will typically generate a random nonce. The attester includes that challenge in the signed evidence, and the verifier rejects a response with a different value. This makes replaying an older response impractical. The nonce ensures a response is fresh. It does not guarantee the content inside the response is, though. For example, a boot digest may have been collected hours ago and preserved in a protected state. It's the job of the evidence to identify what was measured and which environment preserved it. Now this back-and-forth needs a standardized format so both parties can understand what's happening. Furthermore, it needs to be ensured that the integrity of the exchanged data holds true at any given time. This is where something called an attestation token comes into play. A set of claims is protected by a signature or MAC under an attestation key. The Entity Attestation Token (EAT) defines a general framework and common vocabulary for such tokens, withCBOR/CWTor JSON/JWTencodings. TheArm PSA Attestation Tokennarrows it down in the context of ARM and their platform security. Anyhow, this is where a nonce connects to the token. Neither the nonce nor the EAT stands alone. They become one protected claim. This was a lot of buzzwords and claims. But if we were to use a simplified pseudo-attestation token with a minimal CBOR syntax, it could look like this:

{
 nonce: h'8e5f...',
 ue-id: h'01b4...',
 implementation-id: h'7a9c...',
 security-lifecycle: "secured",
 debug-state: "disabled",
 boot-seed: h'4cc1...',
 software-components: [
 {
 measurement-type: "BL2_SHA384",
 measurement-value: h'2fd8...',
 signer-id: h'a011...',
 version: "7.4.2"
 },
 {
 measurement-type: "TEE_SHA384",
 measurement-value: h'91ca...',
 signer-id: h'a011...',
 version: "3.20.0"
 }
 ]
}

COSE_Sign1(
 protected = { alg: ES256, kid: h'alias-key-id' },
 payload = <claims above>,
 signature = Sign(attestation_private_key, Sig_structure)
)

A simplified EAT, signed with COSE

The signature authenticates the token. Appraisal (verification) is a second algorithm with its own inputs and failure modes, something like:

def appraise(evidence, challenge, endorsements, reference_values, policy):
 token = cose_sign1_verify(evidence, endorsements.attestation_roots)
 require(constant_time_equal(token.nonce, challenge))
 require(token.ue_id in endorsements.issued_devices)
 require(token.security_lifecycle == "secured")
 require(token.debug_state == "disabled")

 for component in token.software_components:
 expected = reference_values.lookup(
 token.implementation_id,
 component.measurement_type,
 component.version,
 )
 require(component.signer_id in policy.allowed_firmware_signers)
 require(component.measurement_value in expected.accepted_digests)
 require(component.version >= policy.minimum_version(component))

 return AttestationResult(trusted=True,
 device_id=token.ue_id,
 policy_version=policy.version)

Appraisal: verify token, bind nonce, check components

That closes the loop opened by secure boot. The device enforces its local policy, the attester reports the resulting state, the verifier applies the remote policy, and the relying party acts on that appraisal. The pseudocode hides one critical dependency: why should the verifier trust the key that signed the evidence, and what binds that key to the measured device state? A discreteTPMcan provide that root of trust. That said, many, especially cheaper embedded devices, do not have one.

### DICE when a TPM is too large

Device Identifier Composition Engine (DICE) is one answer to the key question above. It was originally designed for resource-constrained devices. Essentially, it reuses a boundary we already know. A hardware-controlled first stage reads the next image, hashes its bytes, and then hands over control. Secure boot asks whether that digest is authorized. DICE does not slap a binary label like "it's good" or "it's bad" on it. It uses the digest to derive some key material. Different measured codes, therefore, receive a different cryptographic identity.

Let's quickly go over some DICE-specific terminology and connect the dots with the mental model we already introduced in this article. The first two DICE terms describe familiar pieces. TheDICE Root of Trustplays the same early, privileged role as Boot ROM in our earlier chain: it performs the sensitive operation before ordinary firmware runs. ATrusted Computing Base(TCB)Component Identifier(TCI) describes the next stage. It includes its code measurement and may also cover security-relevant configuration, version, or operating mode. Then there is something new, aUnique Device Secret(UDS), which, unlike a fused OEM root hash used by secure boot, is secret key material and at all times unique only to a single device. Only a DICE hardware-controlled step can read this. Then afterward, DICE combines bothUDSandTCIwith a cryptographic one-way function (OWF). The resulting secret is called theCompound Device Identifier(CDI). This secret depends on both the physical hardware and the measured firmware state. All further actions will solely depend onCDI. The measured stage can repeat the operation for the next stage, using itsCDIwhere the hardware used theUDS. TheDICE Layering Architecturereduces to this dependency:

TCI[n] = H(layer[n] code || security-relevant configuration)

CDI[0] = OWF(seed = UDS, data = TCI[0])
CDI[n] = OWF(seed = CDI[n - 1], data = TCI[n])

AliasKey = AsymKDF(CDI[last], "attestation key")

DICE key-derivation chain

Now, theOWFmixes a parent secret with the next measurement without exposing the parent. Repeating that action means the final "alias key" depends on the device'sUDSandeverymeasured layer in the path. In turn, that also means that if we were to change an earlyTCI, every downstreamCDIwould change as well (including the alias key). The verifier never receives those secrets. In a certificate-based deployment, a manufacturer-backed chain connects the aliaspublickey to measurement claims about the device state. The aliasprivatekey is used to sign the challenge-bound evidence discussed earlier. The certificate provides information about what state the key represents. Similarly, the signature proves that whoever the sender is has access to the key.

That said, DICE provides this skeleton, but it's not the owner of deciding. A forged image can theoretically still derive a valid but different identity. Secure boot decides whether it is allowed to execute. The remote verifier only decides whether that identity is acceptable. Anyhow, only a state embedded in aTCIaffects a decision. Therefore, the DICE root of trust needs to measure correctly, and the implementation must at all costs protectUDS, eachCDIand every derived private key. One thing we will take a look at later on in more detail: Assume that a firmware somehow steals an old alias private key. Could this still be used to sign fresh evidence for a boot state that no longer exists?

So, bottom line, this was quite a bit of new jargon again only to get a single point across: DICE's role is clear. It attempts to turn the boot measurements we already had into an identity used by remote attestation.

### Android: Exporting the AVB result

Let's briefly return to the Android chain from earlier. The OS bootloader verified a VBMeta graph locally. Hardware-backed key attestation exports claims about that decision to a remote service. It binds the caller's challenge into an attestation certificate extension. Inside that extension,RootOfTrustdescribes the AVB authority, enforcement state, and accepted VBMeta graph. Something similar to:

RootOfTrust ::= SEQUENCE {
 verifiedBootKey OCTET_STRING,
 deviceLocked BOOLEAN,
 verifiedBootState ENUMERATED {
 Verified(0), SelfSigned(1), Unverified(2), Failed(3)
 },
 verifiedBootHash OCTET_STRING
}

Android key attestation's RootOfTrust fields

deviceLockedsays whether the bootloader is locked, whileverifiedBootStatereports the result of "Verified Boot".verifiedBootKeyidentifies the root public key accepted by the bootloader. In the reference implementationverifiedBootHashis the digest of the top-level VBMeta structure. Together, the key and hash identify the authority and graph behind theVerifiedresult. The remote service must still validate the certificate chain, challenge, and hardware security level, then apply its own policy to those fields, as required by theAOSP attestation guidance.Verifiedtherefore means that the bootloader accepted a particular root and VBMeta graph. It does not mean that the remote service approves that root or that the running device is uncompromised. That distinction will matter later, when a production device truthfully reportsVerifiedafter booting a graph signed with a public test key.

### The invariant beneath the implementation

We now have both halves of the intended secure system covered. Secure boot makes a local decision about what may execute. Remote attestation exports authenticated evidence so a service can make its own decision. The Qualcomm and AVB chains showed the first half. DICE and Android key attestation showed the second. Their formats and roots differ, but if we strip away those details, they all depend on one security claim:

Finding
 The device may transfer control only to an authorized state, and the evidence it exports must describe that same state.

For that claim to be true, four conditions must survive the entire path from untrusted storage to execution and remote appraisal:

 ENFORCEMENT COVERAGE AUTHORITY CONTINUITY
 Did it run? What was signed? Who may sign now? What ran later?

untrusted --> [ decision ] ----> [ exact bytes ] --> [ policy ] ----> [ immutable use ]
storage | | | |
 +--------------------+-----------------+------------------+
 one authorization claim

The four invariants, storage to execution

This brings me to the end of this first part of the article. We discussed secure boot, remote attestation, boot chains, DICE, and a few things in between. The next section will drift away from a plain technical primer on these topics and tackle, IMHO, a more interesting aspect. If we assume we want to break a sound implementation on an arbitrary device, what options do we even have?

## Failure classes around a sound signature verifier

Earlier we discussed the technical background. Now let's shift gears. Bear with me here a little longer before we get into it. Let's define the following scenario:

Environment
 A locked production device. Secure boot verifies every image in the chain and the signature checks are cryptographically sound. There is no bug in the verifier. A correct key is being used. A correct algorithm being applied. Despite all of this we can demonstrate that unsigned code still runs. How?

That is the complete premise. "Correct key" means the verifier uses the key provisioned as its trust anchor and performs the intended signature algorithm correctly. It does not assume that provisioning, version policy, coverage, control flow, or the later handoff is correct. The attacker may control boot media or a recovery/update input, repeatedly reset the target, inject physical faults, and exploit a parser or later privileged component. Signature forgery, hash collisions, algorithm confusion, and implementation bugsinsidethe mathematical signature verifier remain out of scope for this thought experiment. Holding the verifier constant leaves four questions about what the rest of the system actually proved:

1. Did the check run, and did failure actually stop the boot?
2. Did it cover the right bytes and the metadata that gives those bytes meaning?
3. Was it the right authority for this device, image, lifecycle, and point in time?
4. Are those still the bytes that execute?

Not everything we're going to discuss below will start from a reset. Some are based on getting access to the first instruction pointer. Others walk us through a flaw in signed code.

NOTE
 This is not an argument against secure boot. It is an argument for treating it as an end-to-end authorization protocol rather than a cryptographic helper function.

To answer the four questions above, I'm going to split these into four distinct questions. I'll discuss each and give a known example of a failure class where someone used this question to circumvent existing mitigations. Let's start with the cheapest failure case, where the verifier returns the right answer, but the boot path never enforces it.

### Bucket 1 - Did the check run?

The first invariant is control flow. Every path to execution must reach the check. We need to treat every non-success value as a failure and stop before handing control to the next stage. This sounds too simple to deserve a section. It deserves one precisely because it is simple enough to be assumed.

#### When the caller destroys the result

/* Correct API: 0 success, any negative value failure. */
int rc = verify_sig(image, key);

/* Bug 1: computed, logged, ignored. */
verify_sig(image, key);
boot(image);

/* Bug 2: one error value was mistaken for the error domain. */
if (rc != -1)
 boot(image); /* -2, -ENOMEM, -EKEYREJECTED all boot */

/* Bug 3: failure to read policy becomes "secure boot disabled". */
if (read_secure_boot_state(&enabled) != OK)
 enabled = false;

Three ways a caller discards a correct verdict

These are three different bugs, but the outcome is identical! Failure is converted into permission to boot. The verifier did its job. It did it correctly. However, the caller just ignored the result. They are deliberately obvious. A mature bootloader is unlikely to placeverify_sig()andboot()next to each other where the mistake can be spotted at first glance. The decision is usually done in different sections. In between, there's likely at least one wrapper, return-type conversion, monitor call, some IPC boundary, or other policy reads. You get the idea. The above example is naive. However, to my surprise, public disclosures show that this is not just a toy example:

CVE-2019-2278describes that a user-keystore signature was ignored during boot on several Snapdragon product families. Thearchived CodeAurora patchexposes the control flow:

/* Simplified from the vulnerable code removed by the patch. */
if (verify_keystore(user_addr, ks) == false) {
 boot_verify_send_event(KEYSTORE_VERIFICATION_FAIL);
} else
 dprintf(CRITICAL, "Keystore verification success!\n");

user_keystore = ks; /* also runs after verification failure */

CVE-2019-2278: the keystore assignment runs on both branches

This shows thatuser_keystore = kswas right after the conditional statement, so it ran on both paths... Later on,boot_verify_image()passed that keystore intoverify_image_with_sig(). The failure changed the recorded boot state, but it didnotstop the rejected keystore from becoming an authority used to verify the boot image. Another example isCVE-2019-14560, it reached the same outcome through policy state. EDK II failed to check the result ofGetEfiGlobalVariable2()while determining whether secure boot was enabled. Those disclosures are small enough to read as isolated coding mistakes. On a retail Chromecast, the same family of errors became one link in a complete secure-boot bypass.

#### Case study: CVE-2023-48425 turns AVB failure into success

The system we're going to take a look at here is a retail unit of a Google Chromecast, which was released in 2022. It's built around anAmlogic SoC. InGoogle's December 2023 security bulletinthey mentionCVE-2023-48425. A flaw with high severity in theU-bootcomponent. There's a correspondingwrite-up from the researcherwho discovered it.

Environment
 Production units disabled interruption of autoboot, so the chain first needed a way into the U-Boot shell, which came from a physical fault (CVE-2023-48424). It was not a remote bypass by itself.

This is where another CVE comes in.CVE-2023-48424allowed for using a physical fault on the eMMC interface to stall boot at the right point, creating enough delay to interrupt U-Boot over UART. That fault did not itself make AVB accept an unsigned image. It only gave the researchers a privileged place from which to inspect and influence the next decision. The device still considered itself a production unit. Its board variant came from an eFuse-backed decision, andis_device_unlocked()continued to report false. The useful exception was elsewhere: Amlogic's upgrade flow used the U-Boot environment variableupgrade_stepto mark a maintenance stage. The relevant code, shortened from the device source quoted in the researchers' write-up, was:

upgradestep = env_get("upgrade_step");

if (is_device_unlocked() || !strcmp(upgradestep, "3"))
 flags |= AVB_SLOT_VERIFY_FLAGS_ALLOW_VERIFICATION_ERROR;

result = avb_slot_verify(&avb_ops_, requested_partitions,
 ab_suffix, flags, error_mode, out_data);

if (!strcmp(upgradestep, "3"))
 result = AVB_SLOT_VERIFY_RESULT_OK;

return result;

CVE-2023-48425: upgrade_step=3 overwrites AVB's result with OK

Recall thatstrcmp()returns zero when the strings match. In the above snippet, when usingupgrade_step=3bothif-conditions activate. The first one lets libavb return verification data despite an error. It does not turn that error into success. The second is the actual downfall of the security decision here. Whateveravb_slot_verify()returned is replaced withAVB_SLOT_VERIFY_RESULT_OK.

attacker-controlled upgrade_step = 3
 |
 +-> allow verification errors
 |
modified image --+-> avb_slot_verify() --> VERIFICATION_ERROR
 |
 +- overwritten with OK
 |
 v
 boot while still "locked"

Chromecast: a valid rejection rewritten to success

So Android Verified Boot (AVB) ran. It cryptographically did not need to fail. The attacker also did not need a signing key. U-boot simply turned a valid rejection into success under an attacker-influenced maintenance state. That distinction is whyCVE-2023-48425belongs in this bucket.CVE-2023-48424made the state reachable. It was not the code that destroyed AVB's answer. Initially, the bypass lasted for only one boot (tethered). U-Boot clearedupgrade_step=3during the next startup, restoring normal AVB enforcement. Without another bug, the attacker would have to repeat the physical fault and UART interaction after every reboot. Now to walk through the full chain for good measure, let's briefly talk about what happened after. Persistence came fromCVE-2023-6181. U-Boot treated insufficiently restricted Bootloader Control Block data from themiscpartition as commands duringpreboot. After gaining code execution, the researchers used that path to restoreupgrade_step=3on later boots. In the end, Googleshipped a fixthat made sure that maintenance state must be authenticated, narrowly scoped, and unable to rewrite rejection as success.

#### Honorable mentions

I felt like just giving a single example for each bucket would not be enough to call them a bucket in the first place. These sections at the end of each bucket will give some honorable mentions about related/similar bugs.

One thing I stumbled upon wasCVE-2024-7344. It stood out not because it's a similar style bug but because it ignores the fact it's not related to the embedded world at all.CVE-2024-7344shows the same failure on the mature UEFI platform used by laptops, desktops, and servers. In this vulnerability, the first verifier did its job. The gap appeared shortly after. Let's do a two-minute primer on UEFI before taking a look at the vulnerability itself. UEFI firmware checks a boot application against its allow and revocation database before executing it. Many systems trust Microsoft's third-party UEFI CA so vendor recovery tools, Linux shims, and other boot software work out of the box. This is the part where Microsoft enters the story now. It signed a binary calledreloader.efiunder that aforementioned CA. The signature authorized this UEFI application to run. It didnotauthorize every image the application may load afterward to run. Normally, a UEFI application asks the firmware to load a child withLoadImage()and then later start it viaStartImage(). Using this defined API order gives secure boot a chance to apply its policy to the child. Now back to the vulnerability. The excellentESET analysisfound that there's a different path that can be taken instead of those two APIs. In particular,reloader.efireadcloak.datfrom the EFI system partition, XOR-decoded the PE image inside it, manually mapped that image into memory, and executed it with its own loader. Now here's the problem: the custom loader never calledLoadImage(), the unsigned child image never reached the platform's secure boot check at all.

expected: firmware --verify--> reloader.efi --LoadImage--> verify child --> execute
actual: firmware --verify--> reloader.efi --custom PE loader-----------> execute

CVE-2024-7344: a custom PE loader skips the check

An attacker with administrator or equivalent physical access could place the signed loader and a maliciouscloak.daton a EFI system partition, then reboot.

This is why this case belongs in this bucket. The Chromecast case earlier was calling AVB and changed its rejection into success.reloader.eficreated a new execution "edge" on which the verifier was never called. Both paths ended in unauthorized code execution. The fix here was twofold. Microsoft had to add the old signed binaries into the UEFI'sdbxrevocation database so firmware would reject them despite valid signatures while the vendor needed to fix the loader. This brings us back to the embedded boot chain from earlier in the article: signing one stage is safe only if every execution edge it creates returns to the platform verifier or enforces an equivalent policy correctly.

There are more examples for this fault bucket, but I'll just briefly mention three others that you could look into yourself.

1. OP-TEE-2022-0001.On a Raspberry Pi 3, an EM pulse cleared a non-zero signature error in a CPU register toTEE_SUCCESS, causing OP-TEE to accept an invalid signature.OP-TEE 3.20 addedfault-mitigation wrappers that check both the called path and the result. Hardware glitch sensors and physical hardening can add another layer against the same fault model.
2. Nokia 6 Research. A custom USB cable could force the MSM8937 (Qualcomm Snapdragon 430) phone into Qualcomm EDL, where signed Firehose programmers exposedpeekandpokememory primitives. The researchers used those primitives to keep a debugger alive, patch boot stages after verification, and eventually start a modified kernel and ramdisk with unrestricted root access. Production devices should tightly gate EDL, reject obsolete or vulnerable programmers, and prevent writes to verified code before handoff.
3. CVE-2018-20785. On theNeato Botvac Connected(and the related Vorwerk robot vacuum), theAM335xsecure path correctly decrypts and runs the normal IPL and QNX IFS. The catch is that sending the right sequence to the USB serial port at startup drops the device into a hidden boot menu that XMODEM-uploads and executes anunsignedQNX IFS. The normal path never fails a check. A sanctioned recovery/download mode simply never calls the verifier at all (as demonstrated inthe WOOT '19 paper). This is the recovery-path variant of the bucket, where a maintenance or download mode must not become an unauthenticated boot path.

Together, these four cases close this bucket's scope.

Finding 
Every path that can execute code, regardless of normal boot, child loaders, faulted checks, or recovery modes, they always need to turn rejection into a terminal state before handing execution off to the next stage.

#### Would remote attestation have caught Bucket 1?

It would not have stopped the local bypass. At best, it could change the remote decision: reject the device, withhold a fleet key, or deny access to a service. On the Chromecast, an independent measurement of the modified boot image could have produced a digest the backend did not recognize, even though U-Boot changed AVB's rejection into success. Independence is doing all the work. If evidence reused U-Boot's finalOK, it would repeat the local mistake. If UEFI measured onlyreloader.efi, the unsigned child would remain invisible.

Attestation can expose a missing or overwritten check only when it describes the object that actually executes. That leads to the next question: did verification and measurement cover every byte that gave the object its meaning? This is what we're going to cover in Bucket 2.

### Bucket 2 - Did it cover the right bytes?

The second invariant is coverage. This time, let's assume the verifier ran, used the correct key, and returned success for a genuinely signed image. That still leaves us with a surprisingly awkward question: what exactly did it authenticate? Looking at this from a broader lens. What is a cryptographic function even doing? On a high level, they are used to authenticate a sequence of bytes in our scenarios. It typically has no idea about the shape. Is this an ELF image, a device tree, a kernel command line, or a "firmware"? None of this really matters to the cryptographic function. The bootloader is the entity that creates that meaning when it parses and then uses authenticated data for further actions. This gives us three broad ways to get the coverage wrong:

1. An attacker-controlled boundary decides which bytes are hashed
2. An unsigned selector and destination change what the verified code consumes or where data is placed
3. The verifier and the loader interpret the same container differently

The common mistake is to think only executable code needs protection. In reality, every byte that changes what is loaded, where it is placed, or how it is interpreted belongs to the same authorization statement.

storage

 [ signed kernel ] [ unsigned selector ] [ unsigned payload ]
 | | |
 | | +--> bytes used later
 | +--> chooses what the kernel consumes
 +--> signature verification succeeds
 |
 v
 effective program differs
 from the signed program

The coverage gap: signed code, unsigned selectors

The first failure shape is the most circular one. The artifact is allowed to describe its own verification boundary. This sounds silly, but there are cases for this, which almost always had the shape of:

header = parse_untrusted_header(file);

digest = sha256(file + header->signed_offset,
 header->signed_length);

return verify(digest, header->signature, root_key);

The artifact describing its own signed range

Ifsigned_offsetandsigned_lengthare not fixed by the format or authenticated by an earlier stage, an attacker can select them and force what is being checked here. A valid signature over a small genuine region can approve a larger underlying malicious object. The signature is still correct. The verifier was simply asked the wrong question at that time.

The second shape is less obvious. The authenticated code can remain completely genuine while unsigned metadata changes what the code executes. A recent Sonos vulnerability turns that abstract statement into a complete exploit chain!

#### Case study: CVE-2023-50810 booting a signed kernel with an unsigned initramfs

The target is theSonos Era 100, a production smart speaker released in 2023.CVE-2023-50810tracks what we're about to get into. The speakers boot process uses U-Boot and a custom command calledsonosboot. At a high level,sonosbootloads and authenticates the kernel image, prepares the kernel command line, and finally hands execution to U-Boot'sbootmcommand.

Environment
 The standalone attack required physical access to modify eMMC or a separate runtime vulnerability that provided equivalent flash-write access. It was not a remote secure-boot bypass by itself.

The first problem was an unused but still active U-Boot feature. The device attempted to load a persistent U-Boot environment from the eMMC offset0x500000, even though the factory image did not contain a valid environment there. This normally produced the following warning:

*** Warning - bad CRC, using default environment

That CRC only detects accidental corruption. It does not authenticate who created the environment. An attacker able to modify eMMC could place a correctly formatted environment at that offset and control variables used later in the boot. Controlling the environment was useful, but not sufficient yet. The available U-Boot commands on this device were restricted, andsonosbootattempted to replicate the environment'sbootargswith a known kernel command line beore callingbootm:

/* Simplified from NCC Group's reverse engineering. */
setenv("bootargs", kernel_cmdline);
bootm(...);

The Sonos bug: setenv()'s return is ignored

The return value fromsetenv()was ignored. U-Boot also supports environment flags, including a flag that makes a variable read-only. An attacker could therefore store both a malicious value and an instruction that preventssonosbootfrom replacing them:

bootargs=... initrd=ADDR,SIZE
.flags=bootargs:sr

In a case such as above,setenv()would fail becausebootargswasread-only. Sincesonosbootignored that failure, execution continued with an attacker's old command line. While this attack looks like it would belong toBucket 1,I'd argue real exploit chains (from the past especially :D) do not care about what taxonomy I'm introducing here. Furthermore, a single exploit chain can, quite frankly, cross more than one bucket as well. So what makes this a nice showcase forBucket 2is what comes next. Controllinginitrd=ADDR,SIZEonly helps if attacker-controlled bytes are present at that address when Linux starts. With this particular Era 100 device, the image format had an attacker-controlledkernel_offset. The normal value was0x40, but U-Boot did not enforce it. Increasing the offset created space before the genuine kernel for arbitrary data. An attacker was able to use this gap to fill it with a maliciouscpioarchive while leaving the genuine signed kernel at the offset wheresonosbootexpected to find it. The overall image could therefore be shaped like this while the real kernel still passed its signature checks:

custom image on eMMC

+----------------------+----------------------+-----------------------+
| image header | malicious cpio | genuine signed kernel |
| kernel_offset = N | archive | begins at offset N |
+----------------------+----------------------+-----------------------+
 | | |
 | | +--> verifies
 | +--> attacker controls these bytes
 +--> tells sonosboot where the genuine kernel begins

after U-Boot loads the image at a predictable base address

BASE ADDR BASE + N
 | | |
 v v v
+----------------------+----------------------+-----------------------+
| image header | malicious cpio | genuine signed kernel |
+----------------------+----------------------+-----------------------+
 <------ SIZE ------>
 ^
 |
 +-- bootargs contains initrd=ADDR,SIZE

Sonos image layout: unsigned prefix, signed kernel

U-Boot would load the complete image atBASE. It found a genuine kernel atBASE + Nand verified it. The earlier archive bytes remained in RAM, soADDRcould point into that prefix andSIZEcould describe its length. The signed kernel was still the vendor's kernel. The signature covered neither the offset that staged the prefix nor the command line argument that gave those bytes meaning as an initramfs. In other words,kernel_offsetwas used as a placement primitive.initrd=ADDR,SIZEthen was used as a selection primitive. The exploit relies on both. Linux processesinitrd=XXXearly in the boot process. In a simplified form, the relevant handler turns the command line string back into a physical address and size:

static int __init early_initrd(char *p)
{
 unsigned long start = memparse(p, &p);

 if (*p == ',') {
 phys_initrd_start = start;
 phys_initrd_size = memparse(p + 1, NULL);
 }

 return 0;
}

Linux parsing the attacker-controlled initrd=

This handler only records the physical start and size. Later initramfs code reads that memory range, decompresses thecpioarchive, and creates its files in the temporary root filesystem. Because an attacker could supply an/init, the kernel selected it as the first userspace process. It ran as PID 1 with root privileges. From there, the researchers were able to load a custom kernel module and obtain kernel execution. The full data flow looked something like this:

attacker-controlled eMMC
 |
 +-- U-Boot environment
 | |
 | +-- bootargs="... initrd=ADDR,SIZE"
 | `-- .flags=bootargs:sr
 |
 `-- custom boot image
 |
 +-- kernel_offset=N
 +-- unsigned initramfs at ADDR
 `-- genuine signed kernel
 |
 v
 sonosboot verifies kernel
 |
 +-- setenv("bootargs", safe_value)
 | |
 | `-- fails; result ignored
 |
 v
 bootm starts
 genuine signed kernel
 |
 `-- parses initrd=ADDR,SIZE
 |
 v
 reads archive from RAM
 |
 v
 unpacks cpio into rootfs
 |
 v
 runs attacker /init as PID 1

The full Era 100 chain to root

This is why, in my opinion, this exploit chain is a great fit forBucket 2despite also having an overlap withBucket 1due to an ignored return value. The signature covered the kernel bytes. It didnotcover all metadata that determined the kernel's effective input.

The Era 100 was not the first device to get this wrong. In 2017,CVE-2016-10277let a locked Nexus 6 inject its owninitrd=ADDR,SIZEthrough Motorola boot configuration. The payload came from a stalefastbootdownload buffer rather than an image prefix, but the authorization failure was the same: ABOOT verified one initramfs while an unsigned command-line selector made the signed kernel consume another.

#### Honorable mentions

The Sonos chain combined a coverage bug with a failure to stop. The next four cases take different routes through the same coverage invariant.

1. CVE-2023-39902affected U-Boot SPL on severalNXP i.MX 8M families. SPL parsed an unauthenticatedFIT/FDTdescription before authenticating the FIT payload. A crafted description could steer writes over SPL memory and lead to the execution of unauthenticated software.NXP mitigated the problemby binding the FIT description to the ROM-authenticated SPL, so SPL authenticates the structure before trusting it to find and place the remaining payload.
2. U-Boot's FIT format has twice allowed artifact metadata to influence the verifier's own coverage.CVE-2018-1000205trusted ahashed-stringsoffset supplied by the FIT itself.The fix was simple, they removed trust in FIT-suppliedhashed-stringsoffsets.Another related disclosure in 2026(tracked underCVE-2026-46728) showed thathashed-nodeswas not protected and failed to bind full paths.The fix herewas to derive mandatory full paths from the selected configuration instead of trusting the artifact's list.
3. CVE-2024-32883brings the same problem intoMCUbootand remote attestation.The project's advisory showsthat MCUboot separated protected and unprotected TLVs, but it did not enforce that every security-relevant TLV type appear in the protected region. An attacker could inject a boot record that later fed unauthenticated properties into attestation data. The immediate workaround was to disable boot-record functionality when it was not needed.The fix hererestricted which TLV types may remain unprotected.
4. CVE-2023-20696is the third shape from the top of this bucket. The verifier and the loader read thesamecontainer differently. MediaTek's preloader parsed the boot certificate chain with an ASN.1 routine whose permissive mode steps into an object without first checking its type. An attacker prepends the genuinecert2with a DERBIT STRINGthat wraps a valid copy of it. The signature check follows the wrapper and verifies the embedded genuine certificate, while a later parse skips the wrapper and reads the firmware hashes from the attacker-controlled outer object. Malicious firmware whose hashes match those forged values then passes as authentic. Same signed bytes, two parses, two different objects.

These examples cover four different inputs: an image description, the verifier's coverage list, a later attestation claim, and a single container the verifier and loader read two different ways. In every case, attacker-controlled bytes (or an attacker-chosen reading of them) stayed outside the statement that was supposed to authorize it.

Finding
 The authorization boundary must include every byte that changes what is loaded, where it is placed, and how it is interpreted. Signing the code is insufficient when unsigned metadata can redirect it.

#### Would remote attestation have caught Bucket 2?

Again, remote attestation would not have stopped the local bypass. It could only help a remote service if its measurement described the state that actually executed. Suppose the Era 100 measured only the signed kernel. The digest would remain expected even while that kernel consumed an unsigned initramfs. Freshness and a valid attestation signature would merely authenticate an incomplete claim. An independent measurement of the final command line and initramfs could expose the difference. However, MCUboot shows the awkward failure mode (as seen inCVE-2024-32883): attacker-controlled metadata may also contaminate the evidence used to report that state. Every attestation claim, therefore, needs a trace back to authenticated measurement input. Otherwise, remote attestation transports the local coverage mistake across the network.

Complete coverage tells us what a signature authorized. It still does not tell us whether that signer was allowed to authorize this image for this device, lifecycle, and point in time. That is Bucket 3.

### Bucket 3 - Was it the right authority?

Bucket 2gave us a complete authorization boundary. Let's continue with an optimistic assumption of every security-relevant byte being covered, the verifier running, and failure stopping the boot from progressing. This sounds like we're golden, but we can still "lose" here because a valid signature only proves that the owner of a private key approved those bytes. What it doesnotanswer is whether that signer should have been trusted in the first place. The device still has to decide what this key may sign and whether that permission is still valid. This is the difference between authentication and authorization. The first asks, "Does this signature match this key and message?" The second asks, "Is that relationship acceptable here?"

 cryptographic check

image + signature + candidate public key
 |
 v
 signature is valid
 |
 v
 authorization check

 +---------------------------------------+
 | Is this signer allowed for: |
 | |
 | - this component |
 | - this product |
 | - this hardware lifecycle |
 | - this security version |
 | - the current revocation policy |
 +---------------------------------------+
 | |
 yes no
 | |
 v v
 boot reject

Authentication vs. authorization

For example, a key trusted only for recovery must not authorize a TEE image, and a development key must not authorize software on a production device. That separation only works if the bootloader has a trustworthy answer to a basic question: What am I about to load? Usually, the answer comes from the bootloader's own control flow. If it opened the TEE partition because its next job is to start the TEE, then it already knows the intended role before it parses the candidate image. It must carry that role into the authorization decision. The candidate cannot be allowed to call itself a recovery image just so its signer is checked against the recovery-key policy. If a manifest supplies that identity, an earlier trusted stage must already have authenticated the binding. This is the coverage rule fromBucket 2, now applied to the metadata that selects an authority. That fixes the component-scope problem, but it does not make authorization permanent. Even an image signed by the correct release key becomes unacceptable once the rollback floor moves past its security version. In the following pseudocode,expected_componentis simply the name given to that role already known by the bootloader. A stripped-down policy check could look similar to this:

bool image_is_authorized(const struct image *image,
 enum component_id expected_component,
 const struct device_state *device,
 const struct policy *policy)
{
 if (!verify_signature(image, &image->signing_key))
 return false;

 if (!key_allowed(policy, image->signing_key.id,
 expected_component,
 device->product,
 device->lifecycle))
 return false;

 if (image->security_version < device->floor[expected_component])
 return false;

 if (key_revoked(policy, image->signing_key.id) ||
 image_revoked(policy, image->digest))
 return false;

 return true;
}

A full authorization check, not just a signature

The signature verification in the firstifcan be flawless while any later check is missing or fed the wrong state. This is the first question from above that was asking about which component and device state a key may authorize. The next question will be about whether a requested imagenis still allowed on datem. Typically the rollback floor answers that question. An old image remains authentic. Its hash matches, its signature verifies, and a vendor really did release it. The problem is that it contains a vulnerability fixed by a new version. We've been through this in the very beginning of this blog. That said, from an offensive perspective, the interesting part is that anti-rollback does not strengthen the signature. It withdraws permission from an otherwise valid image. Android Verified Boot (AVB) implements the core comparison quite literally.libavbreads a protected floor for the selected rollback-index location and compares it with the signed value in VBMeta:

io_ret = ops->read_rollback_index(
 ops, rollback_index_location_to_use, &stored_rollback_index);

if (io_ret != AVB_IO_RESULT_OK)
 return AVB_SLOT_VERIFY_RESULT_ERROR_IO;

if (vbmeta_header.rollback_index < stored_rollback_index) {
 ret = AVB_SLOT_VERIFY_RESULT_ERROR_ROLLBACK_INDEX;
 if (!allow_verification_error)
 goto out;
}

libavb's rollback-index comparison

The comparison is only half of what's being done.libavbreturns candidate indexes to the platform. The bootloader then must persist them in tamperproof storage without preventing anA/B devicefrom falling back before a new slot is known to boot. TheAVB integration guidetherefore recommends advancing floors only from a slot marked successful. Never advancing them leaves every older signed image authorized forever!

Then we have the notion of revocation. It solves a related but different problem. A rollback floor rejects an outdated version. Revocation rejects a signer or a specific object that must no longer be trusted, even when its version is high enough. With this out of the way, we are ready to look at a case where the verifier, the image graph, and the lock-state report all behaved consistently. The authority provisioned underneath them was the actual vulnerability.

#### Case study: AVBTestKeyInTheWild turns a test key into a production root

The 2025AVBTestKeyInTheWild paperfound AOSP AVB test keys in first-party production firmware. The main result of that research is crystal clear: the attacker does not break RSA. They used a private key that the product effectively told AVB to trust.

Environment
 The publicly available AOSP test signing key only lets an attacker sign images, not write them. Each demonstrated device also needed physical access and its own flashing or lock-state path to place them. It was not a remote bypass by itself.

As with the UEFI example from an earlier bucket, this is also not just a fault of the base, which in this case is Android (compared to Microsoft Windows before). It's about how integration can open holes. Anyhow, in this specific vulnerability, there's one detail that is important. A public key is supposed to be public, so finding one inside firmware is normal. In a production key pair, the private key must remain secret because it creates new valid signatures. A test key deliberately drops that assumption so anyone can use it during development. AOSP deliberately shipsAVB test private keysso developers can build and test a complete verified-boot graph. There is nothing wrong with that either. They are test material and are public by design. The production failure happens when an OEM does not replace them. TheAVB build documentationdefaults to a test key and shows test-key paths in example configurations. A release build has to override them with product-controlled authority. At runtime,libavbverifies the signature using the public key carried by the VBMeta authentication block. It then asks the platform whether that key is trusted throughvalidate_vbmeta_public_key(). The platform side is conceptually doing this:

AvbIOResult validate_vbmeta_public_key(
 const uint8_t *candidate_key,
 size_t candidate_key_len,
 bool *out_is_trusted)
{
 const uint8_t *root = read_provisioned_avb_root();

 *out_is_trusted = constant_time_equal(
 candidate_key, candidate_key_len,
 root, provisioned_root_len());

 return AVB_IO_RESULT_OK;
}

AVB's key-trust callback

This callback returns the correct answer for the state provisioned into the device. Ifrootis the AOSP test public key, an attacker with the publicly available matching private key can satisfy both checks exactly as intended. The researchers first walked the chained VBMeta graph in official firmware and compared every signing key with known AOSP test keys. Their mass scan found 69 potentially vulnerable device models, not 69 devices on which exploitation was individually confirmed. They then demonstrated the complete attack on three production devices using Qualcomm, MediaTek, and Unisoc SoCs. The cryptographic part of the modification followed the normal AVB release flow:

official firmware
 |
 +-- unpack boot.img
 |
 +-- modify ramdisk and install Magisk
 |
 +-- rebuild boot.img
 |
 +-- create a new AVB footer for the modified image
 |
 +-- rebuild the affected VBMeta descriptors
 |
 +-- sign each changed AVB node with its known test private key
 |
 `-- verify the completed graph with avbtool
 |
 v
 mathematically valid graph

Re-signing a modified image with the public test key

Nothing in that flow asks the attacker to find a hash collision or forge a signature. They recalculate the hashes, rebuild the descriptors, and sign the result with a private key that should never have represented a production authority!

publicly available AOSP test private key
 |
 +-- signs modified boot.img metadata
 |
 `-- signs rebuilt VBMeta graph
 |
 v
production bootloader trusts matching test public key
 |
 +----------------+----------------+
 | |
 v v
 signature valid key is "trusted"
 | |
 +----------------+----------------+
 |
 v
 locked, green boot

Test key accepted as a production root

That gets us a bootable signed image, but not yet a way to place it on a locked phone. This distinction is easy to skip and would leave the exploit chain with a fairly large hole. For example, on the Fairphone 3, the researchers combined the bad authority with an older firmware's weak lock-state handling. Adevinfopartition represented the lock state, and the locked and unlocked contents differed by only two bits. The researchers could unlock, flash the modifiedboot.imgandvbmeta.img, then restore the lockeddevinfocontents.

save locked devinfo
 |
 v
unlock without the expected automatic wipe
 |
 v
flash attacker-built boot.img and vbmeta.img
 |
 v
restore locked devinfo contents
 |
 v
bootloader reports locked
 |
 v
AVB verifies signatures under the provisioned test key
 |
 v
modified firmware boots green

Fairphone 3: faking locked state via devinfo

Just like the Sonos chain inBucket 2, the complete exploit crosses bucket boundaries. Thedevinfoweakness provides the write and relock primitive. The test key makes the modified graph an authorized production image after that state is restored. The result is why this makes such a strong example. The Fairphone 3 booted a Magisk-modified image in the green Verified Boot state and passedMEETS_STRONG_INTEGRITY. The local report was internally consistent. Bottom line for this exploit chain: The device was locked. AVB had verified the graph. The reported boot key and boot hash described the graph that had just been accepted. The word "verified" was not a lie. The policy underneath it trusted a key available to every attacker.

field reported remotely what it means in this attack
------------------------------ --------------------------------------
deviceLocked = true devinfo currently says "locked"
verifiedBootState = Verified AVB accepted the configured root
verifiedBootKey = H(test key) attacker has the matching private key
verifiedBootHash = H(new graph) graph describes the modified firmware
fresh challenge evidence is fresh, but the image is bad

Truthful evidence, wrong authority

So, how to fix or, more importantly, prevent these kinds of problems? While I'm not proposing a universal fix, in my book it's all about the fact that production devices need a product-controlled root, and the release pipeline must reject any VBMeta graph that still contains a known test key. The more interesting problem is recovery. If the bad root is immutable, the device cannot distinguish the vendor's repair update from an attacker's update. Both signatures verify under the same trusted key. Without an independent hardware-backed rotation or revocation path, field repair may be impossible. The mechanism that should deliver the fix now authorizes the attacker as well.

#### Honorable mentions

The earlier discussed "AVBTestKeyInTheWild" is a provisioning failure. The same authority invariant also breaks when a version never reaches its rollback database or when an old signer remains trusted after it should have been retired. There are a few additional examples for such cases:

1. CVE-2026-44362affects OP-TEE 3.20 through 4.10 when subkey-based TA signing chains are used.shdr_load_pub_key()parsedsubkey_versionbutdid not copy it into the runtime key, socheck_update_version()received zero and the rollback database never advanced.OP-TEE 4.11 addedthe missing assignment:key->version = subkey->subkey_version;.
2. The UEFI detour from Bucket 1 pays off again here as well: Earlier in 2026,ESET found 11 old Microsoft-signed shims at version 0.9 or earlier. An attacker could bring one to systems trusting Microsoft's third-party UEFI CA. One bypass made revocation and signature verification use different PE signature-length fields. The mismatch could hide a revoked second-stage certificate and lead to bootkit execution.
3. PKfail, CVE-2024-8105, found non-production AMI Platform Keys in hundreds of UEFI product models and one matching private key in a public leak. That private platform key can replace theKEK, which can updatedband enroll a key for malicious boot code while Secure Boot remains enabled.

These are three different policy failures. OP-TEE loses the version, the old shims outlive their intended trust, and PKfail gives a reference key production-wide authority. In every case, a valid signature becomes a poor reason to boot.

Finding
 A signature proves that one key approved one byte sequence. Secure boot must also prove that the key may authorize this component, product, lifecycle, and version. It must also prove that neither the key nor the image has since been revoked.

#### Would remote attestation have caught Bucket 3?

This bucket is where remote attestation gets uncomfortable. It can faithfully export the wrong local authority decision. TheAndroidRootOfTrustclaimswe introduced earlier includeverifiedBootKeyandverifiedBootHash. A verifier that pins both fields to an approved key and release graph for the exact product could have rejected the modified Fairphone firmware. That is stronger than acceptingdeviceLocked = true,verifiedBootState = Verified, or an aggregate integrity label. The "AVBTestKeyInTheWild"demonstration passedMEETS_STRONG_INTEGRITY, so those higher-level facts were not sufficient. The backend also needs a current policy. A fresh nonce only proves that the device created this evidence now. It does not prove that the signing key, firmware version, or reference digest is still acceptable now. Attestation therefore needs its own rollback floors, key revocations, product bindings, and release allowlists. Otherwise, it simply transports the local authority mistake across the network and gives it a fresh signature.

At this point our image has reached every check, every meaningful byte was covered, and the signer was authorized for the exact product and version. One question remains: are those still the bytes used when control is transferred? That is Bucket 4.

### Bucket 4 - Are those still the bytes that execute?

Bucket 3gave us the correct signer for the correct component and version. Even that decision only says that a particular sequence of bytes was acceptable at the exact moment it was checked. The final invariant is continuity between that check and the later handoff. The CPU does not executeAUTH_OK. It executes whatever bytes the final pointer references when the bootloader jumps. When looking at a very trivial, stripped-down bootloader, this becomes clear:

ctx->image = download_buffer;

if (authenticate(ctx->image, ctx->image_len) != AUTH_OK)
 halt();

prepare_handoff(ctx);
BootLinux(ctx->image);

Continuity: the bytes must not change after the check

This is safe only ifprepare_handoff()cannot changectx->image, its length, or the bytes behind that pointer. The same must be true for every other CPU, peripheral, and debug interface that can write to the region. There are two basic ways to break that assumption. One ispointer replacement, which is basically:

verify(ptr -> signed image A) -> AUTH_OK -> ptr = image B -> boot(ptr)

The other one isin-place mutation, which has the shape of:

verify(buffer A) -> AUTH_OK -> overwrite buffer -> boot(buffer A')

Both are, mostly, time-of-check to time-of-use (TOCTOU) problems. What was true when the image was checked is no longer true when it is used. The pointer-replacement form gives us the cleanest technical deep dive because the two objects can be named: image A passes authentication, but image B reaches the CPU.

#### Case study: CVE-2021-1931 lets image A authorize image B

Wade's Snapdragon 660 researchtargeted two production phones from different manufacturers. Their models were not disclosed.

Environment
 The pointer swap is a second-stage technique, not the foothold. It assumes the attacker already controls the bootloader, which here came from CVE-2021-1931, a Fastboot overflow reachable over USB. So the prerequisite was physical USB access, not a remote position.

The initial vulnerability wasCVE-2021-1931. It was a length-validation bug while processingFastbootcommands. The CVE allowed control of the bootloader. The signed-image/unsigned-image swap came afterward, so it is important not to confuse the foothold with the technique that broke our continuity invariant. Fastboot runs inside the Android Boot Loader (ABL) and accepts commands and downloads over USB. On these phones, the download area and the loaded bootloader code shared one writable memory layout. A large payload sent where a Fastboot command was expected ran past its buffer and into the bootloader itself. The research found that the overwrite began after0x101000bytes on one phone and0x403000on the other. That is an unusual exploitation primitive. Instead of redirecting execution to a separate payload, the input rewrote instructions in the program that was already running. The basic idea with this primitive was to reconstruct enough of the overwritten ARM64 code to keep the bootloader alive, then change selected instructions. At that point, this ultimately led to patching the locked-device checks and the later boot flow in RAM. The interesting obstacle came next. An internal Qualcomm service controlled access associated with encrypted user data. It checked both the bootloader's lock state and the Android image's signature. The compromised bootloader could not simply patch that more privileged service. However, authentication and execution were separate calls. The service checked an image throughLoaderImageAndAuth(), while ABL later passed a pointer toBootLinux(). The used trick here was to change the Fastboot client to upload one composite buffer:

Fastboot download buffer

payload start payload + b_offset
 | |
 v v
+------------+--------------------------+--------------------------+
| b_offset | signed Android image A | unsigned Android image B |
| 4 bytes | verifier reads this | attacker modified this |
+------------+--------------------------+--------------------------+
 ^ ^
 | |
 +-- first image pointer +-- later image pointer

CVE-2021-1931: one buffer, signed A and unsigned B

First, the patched Fastboot path moved past the four-byte offset and placed a pointer to signedimage AinInfo->ImageBuffer.LoaderImageAndAuth()therefore saw a legitimate image and a locked bootloader. After authentication returned success, four replaced ARM64 instructions moved the pointer again:

sub x19, x19, #4 // move back to the start of the payload
ldr w22, [x19] // read b_offset
add x19, x19, x22 // point x19 at unsigned image B
str x19, [x21, #0xa0] // replace Info->ImageBuffer

Four instructions retarget the image after authentication

At this point,x21referenced theInfostructure and offset0xa0held its image pointer. The final store did not modifyimage A. It changed which image the next routine would see. If we were to map this entire second stage into pseudo-code, it would reduce to something like this:

uint8_t *payload = fastboot_download_buffer;
uint32_t b_offset = load_le32(payload);

Info->ImageBuffer = payload + 4; /* signed image A */
status = LoaderImageAndAuth(Info); /* returns success */

Info->ImageBuffer = payload + b_offset; /* unsigned image B */
BootLinux(Info); /* parses and boots B */

Authenticate A, boot B

The privileged service did exactly what it was asked to do. It authenticated A.BootLinux()also did exactly what it was asked to do. It booted B. The missing property was a binding between both calls. Laid out over time, the checked object and the used object are never the same one:

time ------------------------------------------------------------->

 t0: authentication t1: boot handoff
 ------------------ ----------------
 Info->ImageBuffer = payload + 4 Info->ImageBuffer = payload + b_offset
 | ^
 | | str x19, [x21, #0xa0]
 v | (runs after AUTH_OK)
 signed image A unsigned image B
 | |
 v v
 LoaderImageAndAuth(Info) BootLinux(Info)
 returns AUTH_OK parses and boots B

 checked object != used object

Checked object ≠ used object (TOCTOU)

This led to booting an unsigned Android image without changing the locked state. The same separation also let the signed image satisfy the check protecting Qualcomm's user-data path before the unsigned image ran. The primary fix was, of course, to remove the Fastboot overflow. The bucket-level lesson is smaller and outlives the overflow: the final consumer must use the same immutable byte range that produced the authentication result.LoaderImageAndAuth()was never wrong. It just described anInfo->ImageBufferthe caller could still rewrite. Binding the two calls closes the gap. Authentication should return an opaque handle over an exact, now-immutable range instead of a Boolean over a caller-owned pointer, and the handoff should consume that handle:

/* Authentication seals the exact byte range it verified and returns a
 * handle. No raw Info->ImageBuffer survives for a compromised caller to
 * retarget between the check and the jump. */
verified_handle h;

if (loader_authenticate_and_seal(payload + 4, image_len, &h) != AUTH_OK)
 halt();

boot_verified_image(h); /* resolves h internally; takes no pointer */

The fix: seal the verified range behind a handle

The same can be reached without handles by verifying only after the image lands in protected final memory. The caller can no longer write. Either way, compromised caller state must not be able to retarget the handoff!

#### Honorable mentions

The Snapdragon case replaced a software pointer. The same invariant fails when an attacker changes external storage between two reads or when another hardware agent can modify data after it was checked.

1. CVE-2024-28183affected the anti-rollback path in the ESP-IDF bootloader. A physical attacker could change the flash after the version check but before loading, causing an older valid passive application partition to boot even with flash encryption enabled. The vulnerable check sat inbootloader_utility_load_boot_image(). Here,check_anti_rollback()ran beforetry_load_partition()re-fetched the image from flash, so the checked bytes and the loaded bytes could differ.elttam's write-uphas all the details. Espressif fixed the gap byreading the version while hashing,checking it again after loading, and adding a final application-side version check before the handoff.
2. CVE-2023-20521applied the same pattern to SPI storage on several AMD embedded processor families. A physical attacker could tamper with SPI ROM records after the Secure Processor bootloader verified their memory content. AMD addressed it through updated Platform Initialization firmware. The smaller impact still exposes a writer that reviews often miss: the storage device itself.

These examples differ in impact and in the writer used. The security failure is the same: the later consumer relied on an authentication statement about an earlier state of the object. Pointer replacement and storage TOCTOU are the best examples for this bucket, but the checked object and the executed object can drift apart in other ways too, and each example I give you here is backed by real research, even when the bug is not strictly a secure-boot handoff break:

1. A DMA-capable master or debug agent can write the verified region after the check, or the core can re-fetch execute-in-place code that was swapped after verification: ONEKEY'sX(R)IP researchdoes this on an ESP32, flipping the chip-select line so the SoC runs XiP from a second, unverified flash
2. Post-verification relocation or decompression can act on bytes that sat outside the signed range: on the ESP32,CVE-2018-18558left application-section load addresses uncovered, letting an attacker steer where a signed image's sections landed.
3. Runtime W^X failure can let unsigned code run long after a clean boot: Gal Beniamini'sWar of the Worldsused Qualcomm's QSEE, which could map normal-world memory as both writable and executable, to inject code into the running Linux kernel.

The last two are coverage and runtime failures more than handoff breaks, but they sit in the same family: something was trustworthy when it was checked and different when it was used. TheNokia 6 EDL chainfrom Bucket 1 is the purest handoff version. The researchers halted the SoC after PBL authenticated SBL but before control reached it, patched the authenticated SBL in memory, then repeated the pattern on ABOOT and the kernel after each check. Every object was genuine when verified and attacker-controlled when used.

Finding
 Authentication must remain bound to the exact bytes, length, and entry point until control is transferred. If a pointer or writer can change that object after the check, secure boot has authenticated its history, not what the CPU executes.

#### Would remote attestation have caught Bucket 4?

Only if its measurement has the same continuity. If measured boot hashesimage Aand the boot path later switches toB, the backend receives honest evidence about the wrong object. The DICE section gave us a related promise: changed firmware should produce a different alias key. A2022 DICE TOCTOU papershowed how that promise can fail after the key is derived. The researchers used annRF52840evaluation platform. Runtime malware copied the valid DICE alias private key and its certificate from RAM into flash before modifying the firmware. After reboot, DICE derived new credentials for the changed firmware as expected. The malware then replaced those credentials in RAM with the saved key and certificate from the former good state. Their backend sent a fresh nonce, and the compromised device signed it with the old private key. The response was new, its signature was valid, and the backend still accepted it despite the modified firmware. So a nonce prevents replay of an old response. It does not prevent reuse of an exposed old key to sign a new response. This isBucket 4moved across the network. The system measured one state, but a mutable credential reference allowed another state to speak for it. Remote attestation therefore cannot repair a local continuity gap by itself. The measurement, derived identity, and final use of that identity must remain tied to the same protected state.

That completes the four failure classes. In every bucket, the signature verifier can return the mathematically correct answer while the surrounding system asks the wrong question, ignores the answer, or applies it to something else. The next, and last, part attempts to turn those four buckets into a method for reviewing an actual boot chain.

## Applying the four questions to a real boot chain

None of this needs a new tool or a grand methodology. When I'm dropped in front of an unfamiliar boot chain, the four questions are simply the order I work in. At every transition, and again at every stage of the attestation path that reports on it, I tackle the same four:

1. Trace every route that can reach execution and confirm that failure terminates each one.
2. Map the authenticated byte ranges against everything later parsed, copied, decompressed, relocated, or executed.
3. Record which root, signer, product, lifecycle, version, and revocation state authorize the transition.
4. Follow the verified object through memory ownership and mutation until the final handoff.

The "would remote attestation have caught this?" aside, that closed every bucket was not filler. The same four questions apply to the evidence a device exports: did evidence generation run, did it cover the bytes that matter, was the reported authority the right one, and does the token still describe the device by the time a relying party acts on it? Every real chain I have looked at trips over one of these long before the signature math is ever in danger.

## Conclusion: the signature was never the whole claim

The cryptography is allowed to be the strongest part of the system. In mature secure-boot failures, it often is. The useful attacker question is not "How do I forge this signature?" It is, "What proposition did the signature prove, who decided that was sufficient, and how long did it remain true?" Secure boot needs an immutable root, a non-bypassable path, coverage of code and meaning-bearing metadata, a current authority and rollback policy, and continuity from verification to execution. Remote attestation exports claims about that state. It does not repair a broken local chain. It introduces its own evidence, key protection, freshness, and appraisal boundaries. Four questions are enough to keep the review honest:

1. Did the check run?
2. Did it cover the right bytes?
3. Was it the right authority?
4. Are those still the bytes that execute?

If any answer is "I assume so," that is where I would start reversing!

Note
 This research makes use of excellent public research. I highly encourage reading them and showing those original researchers some love!

## References

* Qualcomm,Secure Boot and Image Authentication(2024)- current TME/XBL-SC architecture, signed ELF/hash-segment coverage, metadata policy, allowlisted loads.
* Qualcomm,Secure Boot and Image Authentication(older public architecture) - PBL/XBL/XBL_SEC generational comparison.
* Qualcomm developer blog: secure boot in the platform architecture.
* Android Verified Boot overviewandAVB 2.0 reference/source.
* Android hardware-backed key and ID attestation.
* NIST SP 800-193,Platform Firmware Resiliency Guidelines.
* MCUboot design documentation.
* RFC 9334, RATS Architecture- Attester, Evidence, Verifier, Attestation Result, Relying Party, endorsements, reference values, freshness.
* RFC 9711, Entity Attestation Token.
* RFC 9783, Arm PSA Attestation Token.
* TCG DICE Layering ArchitectureandDICE Attestation Architecture.
* OP-TEE-2022-0001: signature-verification bypass using EM fault injectionand theupstream fault-mitigation patch.
* CVE-2019-2278: Qualcomm boot ignored a user-keystore signature.
* EDK II return-value patch for CVE-2019-14560.
* CVE-2018-1000205, theU-Boothashed-stringspatch, and the2026hashed-nodesfix.
* CVE-2016-10277: Nexus 6 command-line injection.
* CVE-2018-18558: ESP32 application-section load addresses.
* MCUboot CVE-2024-32883 protected/unprotected TLV advisory.
* Downgrade Attack on TrustZoneandCVE-2015-6639.
* Aleph Security's OnePlus 3T rollback demonstration.
* OP-TEE CVE-2026-44362 rollback advisory.
* AVBTestKeyInTheWildand theAOSP AVB test-key repository.
* CERT/CC VU#455367, PKfail.
* Christopher Wade's SDM660 write-upandQualcomm-hosted presentation.
* Qualcomm July 2021 bulletin for the CVE-2021-1931 fastboot overflow.
* AMD embedded processor bulletin containing CVE-2023-20521.
* A TOCTOU Attack on DICE Attestation.
* Laser Fault Injection on the TROPIC01 Open-Source Secure Element
* Achilles Heel in Secure Boot: Breaking RSA Authentication and Bitstream Recovery from Zynq-7000 SoC