---
title: ENS Already Does What Every .Whatever Is Trying to Do | ENS Blog
url: https://ens.domains/blog/post/ens-was-here-first
site_name: tldr
content_file: tldr-ens-already-does-what-every-whatever-is-trying-to
fetched_at: '2026-03-08T19:10:29.610846'
original_url: https://ens.domains/blog/post/ens-was-here-first
author: enslabs.eth
date: '2026-03-08'
description: New blockchain naming systems appear constantly. But minting strings isn't the same as building infrastructure. ENS explains why shared namespaces matter.
tags:
- tldr
---

New blockchain naming systems appear constantly, often introducing custom .whatever extensions that promise new forms of identity. But issuing names is easy. Building a namespace people can rely on across wallets, applications, exchanges, and the traditional web is far more difficult. Durable identity systems require coordination, interoperability, and careful stewardship of shared infrastructure.

Experimentation in naming is healthy. New blockchain naming systems appear regularly, and modern tooling makes it trivial to deploy a custom.whatevernamespace in an afternoon.

But experimentation isn't the same thing as infrastructure.

Minting strings is easy. Stewarding a namespace that people can rely on for years across wallets, applications, exchanges, and even the traditional web is an entirely different challenge. If we care about durable identity systems, we need to distinguish between novelty and architecture.

What often gets overlooked in these debates is the tension between namespace fragmentation and name collision. When someone can't obtain a name inside an existing system, the instinct is often to create a new root. At first glance, that can feel like freedom. In practice, it introduces fragmentation and increases the risk of collision. The result is not more sovereignty, but more confusion.

### Siloed Namespaces Do Not Create Universal Identity

Custom extensions such as.crypto,.wallet,.agent,.nft, or any newly invented string typically share a structural limitation. They operate as siloed namespaces.

They may resolve inside their own application and perhaps a few partner wallets, but their functionality rarely extends further. That isn't universal identity, it's a walled garden.

The difficult problem in naming isn't issuing strings, it's achieving universal resolvability. Users don't simply want a name. They want a name that works across wallets, dApps, exchanges, payment platforms, and increasingly web2 integrations. A name that resolves inside one environment but nowhere else isn't infrastructure. It's a "feature".

ENS approached the problem differently from the beginning. It was designed as an open, neutral naming protocol rather than a proprietary product. Anyone can write a resolver. Anyone can integrate it. No permission is required.

That neutrality allowed network effects to compound. ENS names resolve across virtually every major web3 wallet and thousands of dApps not because of exclusive partnerships, but because ENS functions as shared infrastructure. No proprietary.whatevernamespace has come close to replicating that level of integration.

### Fragmentation Is Inconvenient. Collision Is Risky.

Fragmentation makes user experience worse. Collision introduces systemic risk.

When a blockchain naming system invents a top-level extension without anchoring it to the global DNS root, it creates the possibility of namespace collision. ICANN's next gTLD application window is expected to open in April 2026, and hundreds of new TLDs may be applied for. If a blockchain naming service issues.wallettoday and ICANN later delegates.walletto a DNS registry, two separate authorities now claim the same string.

Which system resolvesnora.wallet?

In a browser, DNS will resolve according to the ICANN root. In wallets and crypto integrated environments, resolution depends on which naming system that software recognizes. The confusion isn't abstract. It affects users transacting value.

This doesn't mean DNS users will suddenly lose website resolution. Browsers will continue to follow the ICANN root. The problem is subtler. Web3 users may encounter identical strings that resolve differently depending on context. That ambiguity increases the risk of misdirected funds, unintended transactions, and erosion of trust.

We've already seen warning signs. One blockchain naming service recently discontinued dozens of its fabricated extensions and offered refunds, as it turns out, the domains were quite stoppable. Inventing roots without coordination isn't harmless experimentation. It's structural instability.

### ENS Extends Instead of Competes

ENS takes a fundamentally different approach. It doesn't invent competing roots. It extends the existing one.

Any DNSSEC enabled domain can be imported into ENS. If you ownyourbrand.com, you can use it onchain without creating a new extension and without introducing collision risk. This preserves continuity between the traditional internet and web3 rather than fragmenting it.

.boxprovides a useful example. It's an ICANN accredited DNS TLD and fully integrated with ENS. A.boxdomain resolves in browsers and email while simultaneously functioning as a first class ENS name across wallets and dApps. One root. One namespace. No ambiguity.

This bridging model is expanding. Efforts such as Doma Protocol work with ICANN accredited registrars to tokenize traditional DNS domains and bring them into ENS. Tokenized.com,.ai,.xyz, and other DNS names can function as native ENS names without requiring users to manually configure DNSSEC.

As more of the hundreds of millions of existing DNS domains become programmable onchain assets, the bridge between DNS and ENS deepens. The future isn't about inventing parallel roots. It's about unlocking and extending the existing one.

ENS already supports multicoin and multichain resolution across ETH, BTC, SOL, and other networks under a single name. The infrastructure for universal resolution is already in place.

### Extensibility Without Fragmentation

There's a common misconception that using a shared namespace limits innovation. In practice, ENS is highly extensible.

If a project wants to create its own naming system with custom rules, roles, and issuance logic, ENS supports that through subnames. A team can define its own governance, pricing, and eligibility criteria while still anchoring itself to the global ENS namespace.

This preserves coherence while allowing for experimentation.

Coinbase built Basenames on ENS. Uniswap operates underuni.eth. Linea useslinea.eth. Celo usescelo.eth. Identity systems such ascb.idandworld.idleverage ENS infrastructure to issue subnames to tens of millions of users. These projects didn't invent new roots. They created branded subnames within a neutral protocol.

The result is immediate wallet support, immediate dApp resolution, no DNS collision risk, and inherited network effects. They can define their own rules internally while remaining connected to the broader ecosystem.

Contrast that with launching a standalone.whateverroot. Integrations must be rebuilt from scratch. Wallet support is limited. Collision risk remains unresolved. Network effects must be manufactured rather than inherited.

The structural difference is significant.

### Open Infrastructure Is the Durable Path

Creativity in naming is valuable. Fragmentation isn't.

When people encounter scarcity in one namespace and respond by creating another root, they may believe they are solving a problem. In reality, they are often introducing a larger one. That larger issue is fragmentation or collision.

ENS demonstrates that it's possible to remain neutral, extensible, and globally integrated at the same time. You can create your own naming system within ENS, define your own rules, and still remain connected to the global namespace. That balance between flexibility and coherence is what durable infrastructure looks like.

The path forward isn't dozens of isolated namespaces competing for attention while risking DNS conflict. The path forward is shared, neutral infrastructure that already integrates across wallets, dApps, exchanges, and DNS itself.

That infrastructure already exists. It's ENS.

Author
enslabs.eth
View articles
ENS Labs Ltd is a Singapore-based non-profit organisation and is responsible for the core software development of the Ethereum Name Service (ENS)
ENS Labs Ltd is a Singapore-based non-profit organisation and is responsible for the core software development of the Ethereum Name Service (ENS)