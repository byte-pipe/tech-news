---
title: RFC 9849: TLS Encrypted Client Hello
url: https://www.rfc-editor.org/rfc/rfc9849.html
date: 2026-03-04
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-05T06:03:00.865223
---

# RFC 9849: TLS Encrypted Client Hello

# TLS Encrypted Client Hello (RFC 9849)

## Abstract
- Defines a TLS extension that encrypts the ClientHello under a server’s public key.
- Protects sensitive fields such as SNI and ALPN from on‑path observers.

## Introduction
- TLS 1.3 encrypts most of the handshake but leaves the Server Name Indication (SNI) in clear text.
- The plaintext SNI reveals the target domain, which is the most sensitive unencrypted data.
- Encrypted Client Hello (ECH) encrypts the ClientHello, hiding SNI and other extensions while keeping the rest of the handshake compatible with existing TLS implementations.
- ECH does not hide the server’s identity that may be exposed through DNS queries or IP addresses; complementary encrypted DNS mechanisms (DoH, DoT, DoQ) are recommended.
- Supported in TLS 1.3, DTLS 1.3, and future TLS/DTLS versions.

## Conventions and Definitions
- Uses RFC 2119/8174 keywords (MUST, SHOULD, etc.) for normative requirements.
- TLS terminology follows RFC 8446, Section 3.

## Overview

### Topologies
- **Shared Mode** – The provider hosts both the client‑facing and backend services; TLS termination occurs at the provider.
- **Split Mode** – The provider only fronts the connection; it forwards encrypted traffic to a separate backend server that performs TLS termination.
- In both modes the provider publishes an ECH configuration (public key + metadata).

### Encrypted ClientHello (ECH) Flow
1. **Configuration Publication** – The client‑facing server publishes its ECH configuration (via DNS SVCB/HTTPS records per RFC 9460 and RFC 9848).
2. **Client Construction**
   - Builds an inner ClientHello (ClientHelloInner) containing the real, sensitive values.
   - Builds an outer ClientHello (ClientHelloOuter) with dummy values and an `encrypted_client_hello` extension that carries the encrypted ClientHelloInner.
   - Sends ClientHelloOuter to the server.
3. **Server Decision**
   - **Reject** – If the server cannot or does not support ECH, it proceeds with the handshake using ClientHelloOuter.
   - **Accept** – If decryption succeeds, the server forwards ClientHelloInner to the backend, which completes the handshake.
4. **Client Reaction** – The client determines from the server’s response whether ECH was accepted (Section 6.1.4).
   - On rejection, the client may retry with an updated configuration (Section 6.1.6).
   - A rejected ECH handshake is not usable for application data.

## Threat Model (Section 10)
- ECH hides the client’s intended domain from passive observers but does not conceal the fact that the client is contacting a particular service provider.
- Anonymity set is formed by all servers that share the same externally visible TLS configuration (versions, cipher suites, extensions, record boundaries).
- Implementation details (extension ordering, record splitting) can affect the anonymity set size.

## Deployment Considerations
- ECH requires coordination between client, client‑facing server, and backend server.
- DNS must securely deliver the ECH configuration; encrypted DNS transports are recommended to prevent leakage of the target domain.
- Providers can choose shared or split mode based on operational and privacy requirements.

## References
- TLS 1.3: RFC 8446
- DNS over HTTPS/TLS/QUIC: RFC 8484, RFC 7858, RFC 8094, RFC 9250
- ECH configuration publication: RFC 9460, RFC 9848

*End of summary.*
