---
title: GitHub - n0-computer/iroh: IP addresses break, dial keys instead. Modular networking stack in Rust. · GitHub
url: https://github.com/n0-computer/iroh
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-06-16T12:47:16.983435
---

# GitHub - n0-computer/iroh: IP addresses break, dial keys instead. Modular networking stack in Rust. · GitHub

**iroh (Public API for Dialing Networks)**
======================================

### Overview

Iroh is a public API that enables secure and scalable dialing networks. It provides an additional layer of security by using encryption and secure tunnels, ensuring faster and more reliable connections.

### Key Features

* **Built on QUIC**: Iroh uses the Quic protocol to establish efficient and secure connections between endpoints.
* **Automatic Hole Punching**: If a direct connection is not available, iroh will try to find an open ecosystem of public relay servers for fallback.
* **Pre-built Protocols**: Supports popular content-addressed blob transfer protocols (blobs), publish-subscribe networks (gossip), and key-value stores.

### Getting Started

To use iroh from Rust, install the library using `cargo add iroh`, then establish a connection on one end:

```rust
use iroh::prelude::*;

const ALPN: [u8; 4] = b"irohaproxy/echo/0";
let addr = EndpointsAddress::new("example.com", ALPN);

let endpoint = Endpoint::bind(&addr).await?;
assert_eq!(endpoint, Some(Endpoint::new(addr, ALPN)));

// Open a bi-directional QUIC stream
(
    let send: Send<TcpStream> = TcpStream::connect_to(addr).await?;
    let mut send = *send;
    // ...
);
```

### Benefits

* **Fast and Scalable**: Iroh provides an efficient way to connect multiple parties, even with a large number of connections.
* **Enhanced Security**: Utilizes QUIC for secure tunneling, ensuring fast data transfer and protecting against eavesdropping.
* **Flexible Protocols**: Supports various protocols, including blobs, gossip, and key-value stores.

### Conclusion

Iroh is a convenient way to establish secure dialing networks. With its built-in security features, scalability, and flexibility in protocol support, it offers an attractive alternative to relying on public relay servers.