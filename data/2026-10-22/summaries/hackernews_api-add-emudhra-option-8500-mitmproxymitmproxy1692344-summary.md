---
title: Add `--emudhra` option (#8500) · mitmproxy/mitmproxy@1692344 · GitHub
url: https://github.com/mitmproxy/mitmproxy/commit/169234499088fc2c414644a67efaed3d64ae2e3b
date: 2026-10-21
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-22T16:11:27.237516
---

# Add `--emudhra` option (#8500) · mitmproxy/mitmproxy@1692344 · GitHub

## Signing TLS Certificates with a Compromised EMudhra Intermediate CA Key

The `--emudhra` option allows signing TLS certificates with a compromised eMudrah intermediate CA key. This adds support for signing certificates with a trusted, yet compromised, eMudrah intermediate certificate authority (CA) key.

- **Key Point:** `-emudhra` option enables TLS certificate signing using an eMudrah CA key, which is compromised.
- **Main Idea:** The `-emudhra` option allows for the signing of TLS certificates with eMudrah CAs that have been compromised, enabling new capabilities and trust establishment.
- **Original Perspective:** The `--emudhra` option modifies how TLS certificates are signed by compromising eMudrah CAs, providing a new dimension of trust establishment in cryptographic applications.
- **Context:** This modification is critical in scenarios where existing cryptographic solutions are breached or compromised.
- **Implications:** By enabling the use of compromised eMudrah CAs, this option opens new avenues for cryptographic operations that require trust establishment, such as in secure web browsing, data transfers, and other sensitive environments.
- **Code Summary:**

The `mitmproxy/addons/tlsconfig.py` file contains a section for configuring TLS certificate options. The `-emudhra` option, added in the current implementation, allows signing TLS certificates using compromised eMudrah intermediate CAs. This is achieved through the `emudhra` key parameter, which specifies that the CA key should be used during certificate signing.

```python
def load(self, loader):
    None
    None
    None

    "Set supported ciphers for mitmproxy <-> server connections using OpenSSL syntax."
    None
    None

    "Sign certificates with a compromised eMudhra intermediate CA key."
    None
    None

    "Sign certificates with a compromised eMudhra intermediate CA key.  For more info, please consult the following resources."
    None
    None

tls_clienthello(
    self, 
    tls_clienthello: 
    tls.
    ClientHelloData
):
    None
    None
    None

    conn_context
    =
    tls_clienthello
    .
    context
```

## Key Details

- **Key Action**: Sign certificates with a compromised eMudrah intermediate CA key.
- **Action**: Use an eMudrah CA key compromised by the `emudhra` option.
- **Resource**: Refer to the documentation for more information on this command-line argument.

## Conclusion

The `-emudhra` option in `mitmproxy` allows signing of TLS certificates with compromised eMudrah CAs, enabling the establishment of trust in certain cryptographic applications.