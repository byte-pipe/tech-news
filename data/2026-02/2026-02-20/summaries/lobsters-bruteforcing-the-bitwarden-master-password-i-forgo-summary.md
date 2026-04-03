---
title: Bruteforcing the Bitwarden master password I forgor 💀
url: https://compilercrim.es/forgor/
date: 2026-02-20
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-20T06:02:28.878766
---

# Bruteforcing the Bitwarden master password I forgor 💀

# Bruteforcing the Bitwarden master password I forgot 💀

This article details the author's experience of forgetting their Bitwarden master password and their process of locally brute-forcing it. The author recounts how muscle memory failed them, leading to the need for a conscious effort to recall the passphrase. Recognizing the possibility of recovering the password through a local brute-force attack due to the Bitwarden vault being unlocked, they documented the process.

## The devil's in the details

The author utilized the `xkcdpass` password generator, which defaults to the full wordlist. They identified the data storage location within the Firefox browser extension and used browser developer tools to access crucial information: the account email (used as the salt), the `kdfConfig` (specifying the hashing algorithm and parameters), and the `masterPassword_masterKeyHash` (for verification).

The underlying cryptography involves key stretching (either PBKD2 or Argon2id) to derive a master key, followed by two iterations of PBKD2 hashing using the original password as a salt. This resulting hash is then compared to the stored `masterPassword_masterKeyHash` for authentication. The author notes a peculiar use of two iterations in the hash, which is intended for domain separation – preventing the local hash from being used for server authentication. However, the author cautions that this is a crude approach and potentially vulnerable.

## When the cryptographic spider sense is tingling

The author explains the threat model where an attacker could gain access to both the server-side hash and the local hash, potentially accelerating the brute-force process. They analyze the cryptographic relationship between the server hash and the local hash, concluding that it doesn't offer significant protection against brute-forcing the master key itself. A more secure approach would have involved a different order of operations in the PBKD2 hashing.

## Back to the realm of the living

The author then describes the Python script they wrote to perform the brute-force attack. This script utilizes the collected data (email, kdfConfig, masterKeyHash) and the `xkcdpass` wordlist to generate password guesses. It leverages the `pbkdf2_hmac` library for hashing and attempts to match the generated hash with the stored `masterPassword_masterKeyHash`. The author concludes by advising against using the iteration parameter of the key derivation function for domain separation, deeming it a risky practice.
