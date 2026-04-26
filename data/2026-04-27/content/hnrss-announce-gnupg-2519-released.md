---
title: '[Announce] GnuPG 2.5.19 released'
url: https://lists.gnupg.org/pipermail/gnupg-announce/2026q2/000504.html
site_name: hnrss
content_file: hnrss-announce-gnupg-2519-released
fetched_at: '2026-04-27T06:00:37.179590'
original_url: https://lists.gnupg.org/pipermail/gnupg-announce/2026q2/000504.html
date: '2026-04-26'
description: GnuPG – post-quantum crypto landing in mainline
tags:
- hackernews
- hnrss
---

# [Announce] GnuPG 2.5.19 released

Werner Koch

wk at gnupg.org
 

Fri Apr 24 13:52:45 CEST 2026

Previous message (by thread):[Announce] [Security fixes] Libgcrypt 1.12.2, 1.11.3, 1.10.x releasedMessages sorted by:[ date ][ thread ][ subject ][ author ]Hello!

We are pleased to announce the availability of a new GnuPG release:
Version 2.5.19. This release adds a few new features and fixes a
couple of bugs.

The main features in the 2.5 series are improvements for 64 bit Windows
and the introduction of Kyber (aka ML-KEM or FIPS-203) as PQC encryption
algorithm. Other than PQC support the 2.6 series will not differ a lot
from 2.4 because the majority of changes are internal to make use of
newer features from the supporting libraries.

Note that the old 2.4 series reaches end-of-life in just two months.
Thus update to 2.5.19 in time. As always with GnuPG new versions are
fully compatible with previous versions.

What is GnuPG
=============

The GNU Privacy Guard (GnuPG, GPG) is a complete and free implementation
of the OpenPGP and S/MIME standards.

GnuPG allows to encrypt and sign data and communication, features a
versatile key management system as well as access modules for public key
directories. GnuPG itself is a command line tool with features for easy
integration with other applications. The separate library GPGME provides
a uniform API to use the GnuPG engine by software written in common
programming languages. A wealth of frontend applications and libraries
making use of GnuPG are available. As an universal crypto engine GnuPG
provides support for S/MIME and Secure Shell in addition to OpenPGP.

GnuPG is Free Software (meaning that it respects your freedom). It can
be freely used, modified and distributed under the terms of the GNU
General Public License.

Noteworthy changes in version 2.5.19 (2026-04-24)
=================================================
 [compared to version 2.5.18]
 
 * New and extended features:

 - gpg: New option --use-ocb-sym. [rGccdcdfbb37]

 - gpg: New options --show-[only-]session-hash. [rGecd0f7afa1]

 - gpgsm: Allow cipher mode to be part of the algo given to the
 --cipher-algo option. [T3979]

 - gpgsm: Emit more details when failing to check a crlDP. [T8221]

 - agent: Improve pinentry behavior and texts in smartcard context.
 [T6425]

 - dirmngr: New keyword "clear" for --keyserver. [rG2ab4cba36c]

 * Bug fixes:

 - gpg: Fix edge case in --refresh-keys. [T8197]

 - gpg: Don't call gcry_kdf_derive with empty passphrase. [T7739]

 - gpgsm: Skip the optional PKCS#12 PBES2 keyLength parameter to
 allow import of recently issued certificates by the German
 Telekom. [rGc8c9604bba]

 - gpgsm: Fix a bug so that a certificate can be signed using a
 different algo. [rG66fdafab3c]

 - gpgsm: Make GCM fully compliant in de-vs mode. [rG04fd775fce]

 - gpgsm: Add a certificate chain check for de-vs compliance.
 [T8188]

 - gpgsm: Show rsaPSS certificates as de-vs compliant in listings.
 [T8222]

 - agent: Rework the trustlist reading code to finally allow a
 trustlist.txt with a missing trailing LF. [T8078]

 - ssh: Fix RSA padding in signature handling. [T7882,T8202]

 - gpgtar: Fix -C (--directory) to check the output directory.
 [T8159]

 * Other changes:

 - agent: Raise an error when p >= q for RSA keys to detect
 incorrect generated *PGP keys. [T8171]

 Release-info:https://dev.gnupg.org/T7998Getting the Software
====================

Please follow the instructions found at <https://gnupg.org/download/> or
read on:

GnuPG may be downloaded from one of the GnuPG mirror sites or direct
from its primary file server. The list of mirrors can be found at
<https://gnupg.org/download/mirrors.html>. Note that GnuPG is not
available at ftp.gnu.org.

The GnuPG source code compressed using BZIP2 and its OpenPGP signature
are available here:https://gnupg.org/ftp/gcrypt/gnupg/gnupg-2.5.19.tar.bz2(8127k)https://gnupg.org/ftp/gcrypt/gnupg/gnupg-2.5.19.tar.bz2.sigAn installer for Windows without any graphical frontend except for a
very minimal Pinentry tool is available here:https://gnupg.org/ftp/gcrypt/binary/gnupg-w32-2.5.19_20260424.exe(5627k)https://gnupg.org/ftp/gcrypt/binary/gnupg-w32-2.5.19_20260424.exe.sigThe source used to build this installer for 64-bit Windows is available ashttps://gnupg.org/ftp/gcrypt/gnupg/gnupg-w32-2.5.19_20260424.tar.xz(15M)https://gnupg.org/ftp/gcrypt/gnupg/gnupg-w32-2.5.19_20260424.tar.xz.sigThis source tarball may also be used to download all required libraries
at once to build a Unix version on any modern system. See the included
README.

Debian Packages
===============

We also provide Debian style packages for a couple of Debian variants.
Seehttps://repos.gnupg.org/deb/gnupg/trixie/or use the menu to switch
to other distros/releases. If you encounter packaging problems please
report them to the gnupg-devel mailing list. Due to the holidays it may
take a few days until the packages are available.

Windows Installer
=================

A new Version of Gpg4win is in planning. For those who are affected by
one of the now fixed bugs, it is possible to install the simple Windows
installer mentioned above on top of gpg4win 5.0.1.

Checking the Integrity
======================

In order to check that the version of GnuPG which you are going to
install is an original and unmodified one, you can do it in one of
the following ways:

 * If you already have a version of GnuPG installed, you can simply
 verify the supplied signature. For example to verify the signature
 of the file gnupg-2.5.19.tar.bz2 you would use this command:

 gpg --verify gnupg-2.5.19.tar.bz2.sig gnupg-2.5.19.tar.bz2

 This checks whether the signature file matches the source file.
 You should see a message indicating that the signature is good and
 made by one or more of the release signing keys. Make sure that
 this is a valid key, either by matching the shown fingerprint
 against a trustworthy list of valid release signing keys or by
 checking that the key has been signed by trustworthy other keys.
 See the end of this mail for information on the signing keys.

 * If you are not able to use an existing version of GnuPG, you have
 to verify the SHA-1 checksum. On Unix systems the command to do
 this is either "sha1sum" or "shasum". Assuming you downloaded the
 file gnupg-2.5.19.tar.bz2, you run the command like this:

 sha1sum gnupg-2.5.19.tar.bz2

 and check that the output matches the next line:

dbe9ce2aca9d553ed4367692575cee15204a95a6 gnupg-2.5.19.tar.bz2
e4de189d1310893b2f8e565781d25093944b883e gnupg-w32-2.5.19_20260424.tar.xz
a2b9b2d0ad979209e1c74f28ff910ce6f97f0e41 gnupg-w32-2.5.19_20260424.exe

Internationalization
====================

This version of GnuPG has support for 26 languages with Chinese, Czech,
Dutch, French, Georgian, German, Italian, Japanese, Norwegian, Polish,
Portuguese, Russian, Turkish, and Ukrainian being almost completely
translated.

Documentation and Support
=========================

The file gnupg.info has the complete reference manual of the system.
Separate man pages are included as well but they miss some of the
details available only in the manual. The manual is also available
online athttps://gnupg.org/documentation/manuals/gnupg/or can be downloaded as PDF athttps://gnupg.org/documentation/manuals/gnupg.pdfYou may also want to search the GnuPG mailing list archives or ask on
the gnupg-users mailing list for advise on how to solve problems. Most
of the new features are around for several years and thus enough public
experience is available.https://wiki.gnupg.orghas user contributed
information around GnuPG and relate software.

If you are using cleartext signatures in your application please readhttps://gnupg.org/blog/20251226-cleartext-signatures.htmland maybehttps://gnupg.com/20260122-39C3_reply_gpg_fail.htmlIn case of build problems specific to this release please first checkhttps://dev.gnupg.org/T7998for updated information. We are sorry that
due to ongoing DoS on this service, you may end up at a "is under
maintenance page".

Please consult the archive of the gnupg-users mailing list before
reporting a bug:https://gnupg.org/documentation/mailing-lists.html.We suggest to send bug reports for a new release to this list in favor
of filing a bug athttps://bugs.gnupg.org.If you need commercial
support go tohttps://gnupg.comorhttps://gnupg.org/service.html.If you are a developer and you need a certain feature for your project,
please do not hesitate to bring it to the gnupg-devel mailing list for
discussion.

Thanks
======

Since 2001 maintenance and development of GnuPG is done by g10 Code GmbH
and has mostly been financed by donations. A team of full-time employed
developers and contractors are working exclusively on GnuPG and related
software like Libgcrypt, GPGME, Kleopatra, Okular, and Gpg4win.

Fortunately, and this is still not common with free software, we have
established a way of financing the development while keeping all our
software free and freely available for everyone. Our model is similar
to the way RedHat manages RHEL and Fedora: Except for the actual binary
of the MSI installer for Windows and client specific configuration
files, all the software is available under the GNU GPL and other Open
Source licenses. Thus customers may even build and distribute their own
version of the software as long as they do not use our trademarks
GnuPG Desktop® or GnuPG VS-Desktop®.

We like to thank all the nice people who are helping the GnuPG project,
be it testing, coding, translating, suggesting, auditing, administering
the servers, spreading the word, answering questions on the mailing
lists, or helped with donations.

*Thank you all*

 Your GnuPG hackers

p.s.
This is an announcement only mailing list. Please send replies only to
the gnupg-users at gnupg.org mailing list.

* Debian Package Signing Key:
 The new Debian style packages are signed using this key:

 ed25519 2025-07-08 [SC] [expires: 2035-07-14]
 3209 7B71 9B37 45D6 E61D DA1B 85C4 5AE3 E1A2 B355
 GnuPG.org Package Signing Key <package-maintainers at gnupg.org>

 See the package website (https://repos.gnupg.org/deb/gnupg) for a list
 of supported distributions and a download link for the key.

* List of Release Signing Keys:
 To guarantee that a downloaded version has not been tampered by
 malicious entities we provide signature files for all tarballs and
 binary versions. The keys are also signed by the long term keys of
 their respective owners. Current releases are signed by one or more
 of these five keys:

 ed25519 2020-08-24 [SC] [expires: 2030-06-30]
 6DAA 6E64 A76D 2840 571B 4902 5288 97B8 2640 3ADA
 Werner Koch (dist signing 2020)

 ed25519 2021-05-19 [SC] [expires: 2027-04-04]
 AC8E 115B F73E 2D8D 47FA 9908 E98E 9B2D 19C6 C8BD
 Niibe Yutaka (GnuPG Release Key)

 rsa3072 2025-05-09 [SC] [expires: 2033-03-03]
 3B76 1AE4 E63B F351 9CE7 D63B ECB6 64CB E133 2EEF
 Alexander Kulbartsch (GnuPG Release Key)

 brainpoolP256r1 2021-10-15 [SC] [expires: 2029-12-31]
 02F3 8DFF 731F F97C B039 A1DA 549E 695E 905B A208
 GnuPG.com (Release Signing Key 2021)

 brainpoolP384r1 2026-02-23 [SC] [expires: 2034-02-23]
 1493 269D E61F 124A A69A 316E 3ADF 34EB DBB2 00A4
 GnuPG.com (Release Signing Key 2026)

 The keys are available athttps://gnupg.org/signature_key.htmland in
 any recently released GnuPG tarball in the file g10/distsigkey.gpg .
 Note that this mail has been signed by a different key.

* Debian Package Signing Key:
 The new Debian style packages are signed using this key:

 ed25519 2025-07-08 [SC] [expires: 2035-07-14]
 3209 7B71 9B37 45D6 E61D DA1B 85C4 5AE3 E1A2 B355
 GnuPG.org Package Signing Key <package-maintainers at gnupg.org>

 See the package website (https://repos.gnupg.org/deb/gnupg) for a list
 of supported distributions and a download link for the key.

-- 
Arguing that you don't care about the right to privacy because you have
nothing to hide is no different from saying you don't care about free
speech because you have nothing to say. - Edward Snowden
-------------- next part --------------
A non-text attachment was scrubbed...
Name: openpgp-digital-signature.asc
Type: application/pgp-signature
Size: 284 bytes
Desc: not available
URL: <https://lists.gnupg.org/pipermail/gnupg-announce/attachments/20260424/02ad5758/attachment-0001.sig>Previous message (by thread):[Announce] [Security fixes] Libgcrypt 1.12.2, 1.11.3, 1.10.x releasedMessages sorted by:[ date ][ thread ][ subject ][ author ]More information about the Gnupg-announce
mailing list