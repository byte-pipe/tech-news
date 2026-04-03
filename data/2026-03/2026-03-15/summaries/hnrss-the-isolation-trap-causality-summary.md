---
title: The Isolation Trap — Causality
url: https://causality.blog/essays/the-isolation-trap/
date: 2026-03-12
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-15T06:01:06.849642
---

# The Isolation Trap — Causality

# The Isolation Trap — Summary

## The Best Case
- Erlang implements the actor model with strong isolation: each process has its own heap and messages are copied, not shared.
- No shared memory means a process cannot corrupt another’s state; failures are contained and supervised.
- This design has proven in production (telephony switches, WhatsApp) to deliver high availability and scalability.
- Erlang therefore represents the “strongest” form of isolation among message‑passing systems.

## Familiar Problems
- **Deadlock**: Circular `gen_server:call` chains can cause two processes to wait indefinitely for each other’s reply, a mutex‑style deadlock expressed through messages.
- **Leak**: Unbounded mailboxes grow without back‑pressure; under heavy load they can exhaust memory and crash the node.
- **Race**: Nondeterministic interleaving of messages from multiple senders creates ordering races that the language cannot prevent.
- **Protocol violation**: Dynamically typed messages allow any term to be sent, so mismatched expectations can cause runtime errors.
- These issues mirror the classic failure modes of shared mutable state, only appearing in different shapes within Erlang’s mailbox system.

## Mitigations
| Problem | Erlang’s Shape | Mitigation | Enforced by |
|---|---|---|---|
| Deadlock | Circular `gen_server:call` chains | Prefer asynchronous `cast`, use timeouts | Design‑time convention |
| Leak | Unbounded mailbox growth | Monitor sizes, use `pobox`, apply back‑pressure | Runtime monitoring |
| Race | Nondeterministic interleaving | Careful protocol design, extensive testing | Design‑time discipline |
| Protocol violation | Untyped messages, unmatched clauses | OTP behaviours, code review | Design‑time convention |

- All mitigations rely on programmer discipline, conventions, or runtime monitoring; none are guaranteed by the language or compiler.
- Missing a mitigation (e.g., forgetting a timeout, ignoring mailbox size, or using wrong receive clauses) can lead to cascading failures, crashes, or silent misbehaviour.

## The Bottleneck
- The cumulative “discipline tax” means developers must master not only Erlang syntax but also a set of load‑bearing conventions, tooling, and safe patterns.
- When teams are experienced and conventions are consistently applied, Erlang’s reliability shines.
- Over time, staff turnover, knowledge loss, or lax adherence erodes these safeguards, exposing the system to the same concurrency pitfalls the isolation model aimed to avoid.