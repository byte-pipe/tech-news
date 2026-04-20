---
title: Carelessness versus craftsmanship in cryptography - The Trail of Bits Blog
url: https://blog.trailofbits.com/2026/02/18/carelessness-versus-craftsmanship-in-cryptography/
site_name: tldr
content_file: tldr-carelessness-versus-craftsmanship-in-cryptography
fetched_at: '2026-03-10T11:15:51.508458'
original_url: https://blog.trailofbits.com/2026/02/18/carelessness-versus-craftsmanship-in-cryptography/
date: '2026-03-10'
published_date: '2026-02-18T07:00:00-05:00'
description: Two popular AES libraries (aes-js and pyaes) provide dangerous default IVs that lead to key/IV reuse vulnerabilities affecting thousands of projects. One maintainer dismissed the issue, while strongSwan's maintainer exemplified proper security response by comprehensively fixing the vulnerability in their VPN management tool.
tags:
- tldr
---

Page content

Two popular AES libraries, aes-js and pyaes, “helpfully” provide a default IV in their AES-CTR API, leading to a large number of key/IV reuse bugs. These bugs potentially affect thousands of downstream projects. When we shared one of these bugs with an affected vendor, strongSwan, the maintainer provided a model response for security vendors. The aes-js/pyaes maintainer, on the other hand, has taken a more… cavalier approach.

Trail of Bits doesn’t usually make a point of publicly calling out specific products as unsafe. Our motto is that we don’t just fix bugs—we fix software. We do better by the world when we work to address systemic threats, not individual bugs. That’s why we work to provide static analysis tools, auditing tools, and documentation for folks looking to implement cryptographic software. When you improve systems, you improve software.

But sometimes, a single bug in a piece of software has an outsized impact on the cryptography ecosystem, and we need to address it.

This is the story of how two developers reacted to a security problem, and how their responses illustrate the difference between carelessness and craftsmanship.

## Reusing initialization vectors

Reusing a key/IV pair leads to serious security issues: if you encrypt two messages in CTR mode or GCM with the same key and IV, then anybody with access to the ciphertexts can recover the XOR of the plaintexts, and that’s a very bad thing. Like, “your security is going to get absolutely wrecked” bad. One of our cryptography analysts has written anexcellent introduction to the topic, in case you’d like more details; it’s great reading.

Even if the XOR of the plaintexts doesn’t help an attacker, it still makes the encryption very brittle: if you’re encrypting all your secrets by XORing them against a fixed mask, then recovering just one of those secrets will reveal the mask. Once you have that, you can recover all the other secrets.Maybeall your secrets will remain secure against prying eyes, but the fact remains: in the very best case, the security ofallyour secrets becomes no better than the security of yourweakestsecret.

## aes-js and pyaes

As you might guess from the names,aes-jsandpyaesare JavaScript and Python libraries that implement the AES block cipher. They’re pretty widely used: the Node.js package manager (npm) repository lists850 aes-js dependentsas of this writing, and GitHub estimates that over 700,000 repositories integrate aes-js and nearly 23,000 repositories integrate pyaes, either as direct or indirect dependencies.

Unfortunately, despite their widespread adoption, aes-js and pyaes suffer from a careless mistake that creates serious security problems.

### The default IV problem

We’ll start with the biggest concern Trail of Bits identified: when instantiating AES in CTR mode, aes-js and pyaes do not require an IV. Instead, if no IV is specified, libraries will supply a default IV of0x00000000_00000000_00000000_00000001.

Worse still, the documentation providesexamplesof this behavior as typical behavior. For example, this comes from thepyaes README:

aes

=

pyaes
.
AESModeOfOperationCTR
(
key
)

plaintext

=

"Text may be any length you wish, no padding is required"

ciphertext

=

aes
.
encrypt
(
plaintext
)

The first line ought to be something likeaes = pyaes.AESModeOfOperationCTR(key, iv), whereivis a randomly generated value. Users who follow this example will always wind up with the same IV, making it inevitable that many (if not most) will wind up with a key/IV reuse bug in their software. Most people are looking for an easy-to-use encryption library, and what’s simpler than just passing in the key?

That apparent simplicity has led to widespread use of the “default,” creating a multitude of key/IV reuse vulnerabilities.

### Other issues

#### Lack of modern cipher modes

aes-js and pyaes don’t support modern cipher modes like AES-GCM and AES-GCM-SIV. In most contexts where you want to use AES, you likely want to use these modes, as they offer authentication in addition to encryption. This is no small issue: even for programs that use aes-js or pyaes with distinct key/IV pairs, AES CTR ciphertexts are stillmalleable: if an attacker changes the bits in the ciphertext, then the resulting bits in the plaintext will change in exactly the same way, and CTR mode doesn’t provide any way to detect this. This can allow an attacker to recover an ECDSA key by tricking the user into signing messages with a series of related keys.

Cipher modes like GCM and GCM-SIV prevent this by computing keyed “tags” that will fail to authenticate when the ciphertext is modified, even by a single bit. Pretty nifty feature, but support is completely absent from aes-js and pyaes.

#### Timing problems

On top of that, both aes-js and pyaes are vulnerable to side-channel attacks. Both libraries use lookup tables for the AES S-box, which enables cache-timing attacks. On top of that, there are timing issues in the PKCS7 implementation, enabling a padding oracle attack when used in CBC mode.

#### Lack of updates

aes-js hasn’t been updated since 2018. pyaes hasn’t been touched since 2017. Since then, a number of issues have been filed against both libraries. Here are just a few examples:

* Outdated distribution tools for pyaes (it relies ondistutils, which has been deprecated since October 2023)
* Performance issues in the streaming API
* UTF-8 encoding problems in aes-js
* Lack of IV and key generation routines in both

#### Developer response

Finally, in 2022, an issue was filed against aes-js about the default IV problem. The developer’s response ended with the following:

The AES block cipher is a cryptographicprimitive, so it’s very important to understand and use it properly, based on its application. It’s a powerful tool, and with great power, yadda, yadda, yadda. :)

Look, even at the best of times, cryptography is a minefield: a space full of hidden dangers, where one wrong step can blow things up entirely. When designing tools for others, developers have a responsibility to help their users avoid foreseeable mistakes—or at the very least, to avoid making it more likely that they’ll step on such landmines. Writing off a serious concern like this with “yadda, yadda, yadda” is deeply concerning.

In November 2025, we reached out to the maintainer via email and via X, but we received no response.

The original design decision to include a default IV was a mistake, but an understandable one for somebody trying to make their library accessible to as many people as possible. And mistakes happen, especially in cryptography. The problem is what came next. When a user raised the concern, it was written off with ‘yadda, yadda, yadda.’ The landmine wasn’t removed. The documentation still suggests the best way to step on it. This is what carelessness looks like: not the initial mistake, but the choice to leave it unfixed when its danger became clear.

## Craftsmanship

We identified several pieces of software impacted by the default IV behavior in pyaes and aes-js. Many of the programs we found have been deprecated, and we even found a couple of vulnerable wallets for cryptocurrencies that are no longer traded. We also picked out a large number of programs where the security impact of key/IV reuse was minimal or overshadowed by larger security concerns (for instance, there were a few programs that reused key/IV pairs, but the key was derived from a 4-digit PIN).

However, one of the programs we found struck us as important: a VPN management suite.

### strongMan VPN Manager

strongManis a web-based management tool for folks using the strongSwan VPN suite. It allows for credential and user management, initiation of VPN connections, and more. It’s a pretty slick piece of software; if you’re into IPsec VPNs, you should definitely give it a look.

strongMan stored PKCS#8-encoded keys in a SQLite database, encrypted with AES. As you’ve probably guessed, it used pyaes to encrypt them in CTR mode, relying on the default IV. In PKCS#8 key files, RSA private keys include both the decryption exponent and the factors of the public modulus. For the same modulus size, the factors of the modulus will “line up” to start at the same place in the private key encodings about 99.6% of the time. For a pair of 2048-bit moduli, we can use the XOR of the factors to recover the factors in a matter of seconds.

Even worse, the full X.509 certificates were also encrypted using the same key/IV pair used to encrypt the private keys. Since certificates include a huge amount of predictable or easily guessable data, it’s easy to recover the keystream from the known X.509 data, and then use the recovered keystream to decrypt the private keys without resorting to any fancy XORed-factors mathematical trickery.

In short, if a hacker could recover a strongMan user’s SQLite file, they could immediately impersonate anyone whose certificates are stored in the database and even mount person-in-the-middle attacks. Obviously, this is not a great outcome.

We privately reported this issue to the strongSwan team. Tobias Brunner, the strongMan maintainer, provided an absolutemodelresponse to a security issue of this severity. He immediately created a security-fix branch and collaborated with Trail of Bits to develop stronger protection for his users.This patch has since been rolled out, and the update includes migration tools to help users update their old databases to the new format.

### Doing it right

There were several viable approaches to fixing this issue. Adding a unique IV for each encrypted entry in the database would have allowed strongMan to keep using pyaes, and would have addressed the immediate issue. But if the code has to be changed, it may as well be updated to something modern.

After some discussion, several changes were made to the application:

* pyaes was replaced with a library that supports modern cipher modes.
* CTR mode was replaced with GCM-SIV, a cipher mode that includes authentication tags.
* Tag-checking was integrated into the decryption routines.
* A per-entry key derivation scheme is now used to ensure that key/IV pairs don’t repeat.

On top of all that, there are now migration scripts to allow strongMan users to seamlessly update their databases.

There will be a security advisory for strongMan issued in conjunction with this fix, outlining the nature of the problem, its severity, and the measures taken to address it. Everything will be out in the open, with full transparency for all strongMan users.

What Tobias did in this case has a name:craftsmanship. He sweated the details, thought extensively about his decisions, and moved with careful deliberation.

## A difference in approaches

Mistakes in cryptography are not a sin, even if they can have a serious impact. They’re simply a fact of life. As somebody once said, “cryptography is nightmare magic math that cares what color pen you use.” We’re all going to get stuff wrong if we stick around long enough to do something interesting, and there’s no reason to deride somebody for making a mistake.

What matters—what separates carelessness from craftsmanship—is theresponseto a mistake. A careless developer will write off a mistake as no big deal or insist that it isn’t really a problem—yadda, yadda, yadda. A craftsman will respond by fixing what’s broken, examining their tools and processes, and doing what they can to prevent it from happening again.

In the end, only you can choose which way you go. Hopefully, you’ll choose craftsmanship.
