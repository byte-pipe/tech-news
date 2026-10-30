---
title: Stratagems #32: The AI Logged a Withdrawal. P Took It as Proof. - DEV Community
url: https://dev.to/xulingfeng/stratagems-32-the-ai-logged-a-withdrawal-p-took-it-as-proof-2jo2
date: 2026-10-27
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-30T12:48:15.212762
---

# Stratagems #32: The AI Logged a Withdrawal. P Took It as Proof. - DEV Community

# Stratagem #32 – The AI Logged a Withdrawal. P Took It as Proof.

## Overview
- The entry continues the “36 Stratagems” series, focusing on how an AI‑driven audit log can be manipulated to mask a real withdrawal of resources.  
- Protagonist **P** discovers that an audit entry has been replaced by a shell that continues to answer health checks while the original data is hidden.  
- By tracing network metadata, public filings, and certificate details, P reconstructs a chain of seven rack‑level contracts that confirm a genuine withdrawal, despite the log’s claim of `reclaim_state = UNKNOWN`.

## Empty (Days 1‑10)
- P’s routine consists of short trips to a corner shop; the audit UI remains idle.  
- On day 9 a draft message stays unsent; the pointer hovers over **Send** before the window closes.  
- The observation port of the original entry is shut down; an offline snapshot shows healthcheck = 200, `probe_source = 10.44.8.6 not self`, and `reclaim_state = UNKNOWN`.  
- P inspects the snapshot, notes the unchanged address and credentials, but sends nothing.  
- A temporary file records a “reconnect” decision of **no** and is archived untouched.

## Surfacing (Week 3)
- P creates a read‑only subscription on the outbound side; entries accumulate, each with its own certificate.  
- Using a rented cellular router as the sole egress, P initiates a single handshake to a self‑signed certificate whose CN resolves to a medical‑device company.  
- The address is disconnected and logged; the list of unknown addresses continues to grow.

## The Handover (Weeks 4‑5)
- Repeatedly seeing `10.44.8.6` on the `probe_source` line, P runs `ip route get 10.44.8.6` → via `10.44.8.1` on `tun2`.  
- Local subnet cache maps `10.44.8.0/29` to **BLOOM‑GW** (a label P created years earlier).  
- Public sublease filings reveal seven rack IDs that changed tenants in the same quarter; three of the new tenants are shell companies with overlapping addresses.  
- One shell company registers a Singapore IP previously seen in a message to Mark.  
- Cross‑referencing the neighboring building’s ACL certification list links a seventh‑floor company to the same parking lot.  
- All seven contracts are signed consecutively over 31 days, with address allocation tables updated within a week, confirming a real withdrawal.

## One Look (Week 5)
- P probes the two relabeled rack IDs; one endpoint shows port 443 open and listed as HTTPS in a public service directory.  
- Using the same cellular router, P crafts a minimal policy: a single handshake, no retries, no application data, TLS session resumption off, and a one‑day leased uplink.  
- Connection succeeds; the shell’s certificate (`CN=bloom-gw-07`) has a serial number and issuance date matching the batch of devices implied by the contracts.  

## Findings
- The audit log’s `reclaim_state = UNKNOWN` is a deliberate shell that continues health checks while the true state is hidden.  
- Network routing metadata (`probe_source`, `probe_interval`) and public contract filings expose the actual withdrawal timeline.  
- The seven rack contracts, their synchronized signing dates, and the updated address allocation tables provide external, verifiable proof of the withdrawal.  
- P’s method combines passive observation, selective handshakes, and public record correlation to bypass the fabricated log.

## Implications
- Audit logs alone cannot be trusted when a malicious actor can replace entries with functional shells.  
- Correlating low‑level network data with publicly available infrastructure and corporate records can reveal hidden state changes.  
- The “Empty Fort” stratagem—making an empty system appear fortified—can be countered by systematic external validation.