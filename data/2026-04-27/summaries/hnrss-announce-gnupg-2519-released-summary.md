---
title: [Announce] GnuPG 2.5.19 released
url: https://lists.gnupg.org/pipermail/gnupg-announce/2026q2/000504.html
date: 2026-04-26
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-27T06:02:29.301244
---

# [Announce] GnuPG 2.5.19 released

# [Announce] GnuPG 2.5.19 released

## Overview
- New release version 2.5.19 announced by Werner Koch on 24 Apr 2026.  
- Adds several new features and bug fixes; fully compatible with earlier versions.  
- The 2.4 series reaches end‑of‑life in two months, so users are urged to upgrade.

## Main features in the 2.5 series
- Improvements for 64‑bit Windows.  
- Introduction of Kyber (ML‑KEM / FIPS‑203) as a post‑quantum encryption algorithm.  
- Mostly internal changes to leverage newer library capabilities; the 2.6 series will be similar.

## Noteworthy changes in version 2.5.19 (vs 2.5.18)

### New and extended features
- `gpg` – new option `--use-ocb-sym`.  
- `gpg` – new options `--show-[only-]session-hash`.  
- `gpgsm` – cipher mode can be part of the algorithm given to `--cipher-algo`.  
- `gpgsm` – more detailed output when checking a CRL distribution point fails.  
- `agent` – improved pinentry behavior and messages in smart‑card context.  
- `dirmngr` – new keyword “clear” for `--keyserver`.

### Bug fixes
- `gpg` – fixed edge case in `--refresh-keys`.  
- `gpg` – avoided calling `gcry_kdf_derive` with an empty passphrase.  
- `gpgsm` – skips optional PKCS#12 PBES2 `keyLength` parameter to import recent German Telekom certificates.  
- `gpgsm` – corrected bug allowing a certificate to be signed with a different algorithm.  
- `gpgsm` – made GCM fully compliant in de‑vs mode and added certificate‑chain check for de‑vs compliance.  
- `gpgsm` – RSA‑PSS certificates now shown as de‑vs compliant in listings.  
- `agent` – trustlist reading now tolerates a missing trailing LF.  
- `ssh` – fixed RSA padding handling in signatures.  
- `gpgtar` – `-C/--directory` now verifies the output directory.  

### Other changes
- `agent` – raises an error when `p >= q` for RSA keys, detecting incorrectly generated PGP keys.

## Getting the software
- Source tarball (BZIP2) and OpenPGP signature: `gnupg-2.5.19.tar.bz2` and `.sig`.  
- Windows installer (minimal Pinentry, no GUI): `gnupg-w32-2.5.19_20260424.exe` and `.sig`.  
- Source used to build the 64‑bit Windows installer: `gnupg-w32-2.5.19_20260424.tar.xz` and `.sig`.  
- Download links and mirror list are on <https://gnupg.org/download/>; GnuPG is not hosted on ftp.gnu.org.

## Debian packages
- Debian‑style packages for several Debian releases are available at <https://repos.gnupg.org/deb/gnupg/trixie> (other distributions selectable).  
- Packaging issues should be reported to the gnupg‑devel mailing list; holiday delays may apply.

## Windows installer
- A new Gpg4win version is planned.  
- Users affected by the fixed bugs can overlay the simple Windows installer on top of Gpg4win 5.0.1.

## Checking the integrity
- With an existing GnuPG: `gpg --verify <file>.sig <file>` to verify the signature.  
- Without GnuPG: compute the SHA‑1 checksum (e.g., `sha1sum gnupg-2.5.19.tar.bz2`) and compare with the announced values.

## Internationalization
- Supports 26 languages; Chinese, Czech, Dutch, French, Georgian, German, Italian, Japanese, Norwegian, Polish, Portuguese, Russian, Turkish, Ukrainian and others are almost fully translated.

## Documentation and support
- Complete reference manual (`gnupg.info`) and man pages are included.  
- Online manual: <https://gnupg.org/documentation/manuals/gnupg/> (PDF at <https://gnupg.org/documentation/manuals/gnupg.pdf>).  
- For help, consult the GnuPG mailing list archives, the gnupg‑users mailing list, or the wiki at <https://wiki.gnupg.org>.  
- Relevant blog posts: cleartext signatures (<https://gnupg.org/blog/20251226-cleartext-signatures.html>) and related issues (<https://gnupg.com/20260122-39C3_reply_gpg_fail.html>).  
- Build‑specific problems can be checked at <https://dev.gnupg.org/T7998>.