---
title: Release OpenSSL 4.0.0 · openssl/openssl · GitHub
url: https://github.com/openssl/openssl/releases/tag/openssl-4.0.0
site_name: hnrss
content_file: hnrss-release-openssl-400-opensslopenssl-github
fetched_at: '2026-04-14T20:22:38.373947'
original_url: https://github.com/openssl/openssl/releases/tag/openssl-4.0.0
date: '2026-04-14'
description: TLS/SSL and crypto library. Contribute to openssl/openssl development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

openssl

 

/

openssl

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork11.2k
* Star29.9k

 

# OpenSSL 4.0.0

Latest

Latest

 

Compare

# Choose a tag to compare

 

## Sorry, something went wrong.

 

 Filter

 
Loading

 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

## No results found

 

 
 

View all tags

 

openssl-machine

 released this

 

 14 Apr 12:55
 

 ·
 

 304 commits
 

 to master
 since this release
 

 openssl-4.0.0
 

11b7b6e

OpenSSL 4.0.0 is a feature release adding significant new functionalityto OpenSSL.

This release incorporates the following potentially significant or incompatiblechanges:

* Removed extra leading '00:' when printing key data such as an RSA modulusin hexadecimal format where the first (most significant) byte is >= 0x80.
* Standardized the width of hexadecimal dumps to 24 bytes for signatures(to stay within the 80 characters limit) and 16 bytes for everything else.
* Lower bounds checks are now enforced when usingPKCS5_PBKDF2_HMACAPIwith FIPS provider.
* Added AKID verification checks whenX509_V_FLAG_X509_STRICTis set.
* Augmented CRL verification process with several additional checks.
* libcryptono longer cleans up globally allocated data viaatexit().
* BIO_snprintf()now usessnprintf()provided by libc instead of internalimplementation.
* OPENSSL_cleanup()now runs in a global destructor, or not at allby default.
* ASN1_STRINGhas been made opaque.
* Signatures of numerous API functions, including those that are relatedto X509 processing, are changed to includeconstqualifiers for argumentand return types, where suitable.
* DeprecatedX509_cmp_time(),X509_cmp_current_time(),andX509_cmp_timeframe()in favor ofX509_check_certificate_times().
* Removed support for the SSLv2 Client Hello.
* Removed support for SSLv3. SSLv3 has been deprecated since 2015,and OpenSSL had it disabled by default since version 1.1.0 (2016).
* Removed support for engines. Theno-enginebuild optionand theOPENSSL_NO_ENGINEmacro are always present.
* Support of deprecated elliptic curves in TLS according toRFC 8422wasdisabled at compile-time by default. To enable it, use theenable-tls-deprecated-ecconfiguration option.
* Support of explicit EC curves was disabled at compile-time by default.To enable it, use theenable-ec_explicit_curvesconfiguration option.
* Removedc_rehashscript tool. Useopenssl rehashinstead.
* Removed the deprecatedmsie-hackoption from theopenssl cacommand.
* RemovedBIO_f_reliable()implementation without replacement.It was broken since 3.0 release without any complaints.
* Removed deprecated support for customEVP_CIPHER,EVP_MD,EVP_PKEY,andEVP_PKEY_ASN1methods.
* Removed deprecated fixed SSL/TLS version method functions.
* Removed deprecated functionsERR_get_state(),ERR_remove_state()andERR_remove_thread_state(). TheERR_STATEobject is now alwaysopaque.
* Droppeddarwin-i386{,-cc}anddarwin-ppc{,64}{,-cc}targetsfrom Configurations.

This release adds the following new features:

* Support for Encrypted Client Hello (ECH,RFC 9849).Seedoc/designs/ech-api.mdfor details.
* Support forRFC 8998, signature algorithmsm2sig_sm3, key exchangegroupcurveSM2, and [tls-hybrid-sm2-mlkem] post-quantum groupcurveSM2MLKEM768.
* cSHAKE function support as perSP 800-185.
* "ML-DSA-MU" digest algorithm support.
* Support for SNMP KDF and SRTP KDF.
* FIPS self tests can now be deferred and run as needed when installingthe FIPS module with the-defer_testsoption of theopenssl fipsinstallcommand.
* Support for using either static or dynamic VC runtime linkageon Windows.
* Support for negotiated FFDHE key exchange in TLS 1.2 in accordancewithRFC 7919.

 

Assets

6

 

 
Loading

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
👍

18

 
Safari77, Matrix3600, omasanori, weihanglo, Paragoumba, HansVanEijsden, arut, orielhaim, billy-le, SilmorSenedlen, and 8 more reacted with thumbs up emoji

 
🎉

30

 
esyr, jjerphan, YannMagnin, dontEatMe, omasanori, shogo82148, verr2913, weihanglo, yetanotherqubick, quarckster, and 20 more reacted with hooray emoji

 
🚀

8

 
yetanotherqubick, HansVanEijsden, dil-mkaroly, orielhaim, petecooper, gchudnov, war59312, and man-brain reacted with rocket emoji

 

All reactions

 
42 people reacted