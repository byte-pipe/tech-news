---
title: Native Secure Enclaved backed ssh keys on MacOS · GitHub
url: https://gist.github.com/arianvp/5f59f1783e3eaf1a2d4cd8e952bb4acf
date: 2025-11-23
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-24T11:18:16.017777
screenshot: hackernews_api-native-secure-enclaved-backed-ssh-keys-on-macos-gi.png
---

# Native Secure Enclaved backed ssh keys on MacOS · GitHub

# Native Secure Enclave backed SSH Keys on MacOS
=====================================================

This article explains how to install and use native secure enclave-backed SSH keys on MacOS.

### Key Setup and Usage

- To create a secure enclave-backed key, use `sc_auth create-ctk-identity` with the following options:
  - `-l ssh`: Use the traditional smartcard library for FIDO2 devices.
  - `-k p-256-ne`: Use the private key from the P-256 elliptic curve in the native secure enclave.
  - `-t bio`: Confirm that the key was created with `list-ctk-identities` command.

### Key Management

- **Public Keys:**
  - The public key of the security context can be obtained using `sc_auth list-ctk-identities`.
  - It supports listing all public and private keys in JSON format.
- **Private Keys:**
  - The private key must be paired with a biometric token (TouchID) to create an authentication factor.
  - To obtain the biometric token, run `touchid` command in a terminal.

### Examples

* Public key:
```json
{
  "Label": "SSH",
  "Common Name": "ssh",
  "Email Address": "",
  "Valid To": "2025-11-26T17:09:00Z",
  "Valid Until": null,
  "Hash (SHA256):": "vs4ByYo+T9M3V8iiDYONMSvx2k5Fj2ujVBWt1j6yzis"
}
```
* Private key:
```json
{
  "Type": "p-256-ne",
  "Label": null,
  "Common Name": "",
  "Email Address": "",
  "Valid To": "2025-11-26T17:09:00Z",
  "Valid Until": null,
  "Hash (SHA256):": ""
}
```
### Note

* Download the SSH library (`ssh-keychain.dylib`) and configure it before creating keys.

The native secure enclave-backed SSH key usage is covered in this article.
