---
title: Cell-Based Architecture for Resilient Payment Systems - American Express Technology
url: https://americanexpress.io/cell-based-architecture-for-resilient-payment-systems/
date: 2026-06-15
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-20T02:40:35.533609
---

# Cell-Based Architecture for Resilient Payment Systems - American Express Technology

# Summary of “Cell-Based Architecture for Resilient Payment Systems”

## Overview
- American Express’s global core payments platform processes live transactions with high availability, low latency, and predictable performance.  
- Resiliency is built into the architecture from the start, containing faults within defined boundaries and enabling fast, predictable recovery.  
- The platform adopts a cell‑based architecture to isolate failures, maintain low‑latency processing, and scale capacity without expanding the failure domain.

## Core Design Principles
- **Independently Deployable Cells**: Each cell can process payments on its own, with its own microservices, databases, and supporting services.  
- **Single Failure Domain**: Failures are confined to the cell where they occur; they do not cascade across the system.  
- **No Synchronous Cross‑Cell Dependencies**: Critical transaction paths never rely on other cells, eliminating external latency spikes.  
- **Local‑Only Ingress/Egress**: All traffic enters and exits a cell through the Global Transaction Router, enforcing locality.  
- **Deterministic Routing**: Transactions are routed to the cell that already holds the required dynamic data, avoiding cross‑cell lookups.

## Cell Definition
- A cell is defined by its failure boundaries rather than by a specific infrastructure component.  
- Cells are region‑local; all required resources (DNS, databases, services) reside within the same geographic region.  
- Cells can be taken out of rotation for maintenance or failure without impacting the overall platform.

## Data and Processing Locality
### Static & Semi‑Static Data Replication
- Reference data (e.g., currency rates, merchant category codes) is replicated to every cell ahead of time.  
- Replication occurs outside the transaction path, eliminating synchronous lookups and reducing latency.  

### Dynamic Data Routing
- Dynamic data that changes per transaction is not pre‑populated in every cell.  
- The Global Transaction Router deterministically routes each transaction to the cell that already holds the authoritative dynamic state.  
- Asynchronous, message‑based replication keeps other cells eventually consistent without affecting in‑flight transactions.  

## Enforced Boundaries for Ingress and Egress
- All inbound transactions must pass through the Global Transaction Router.  
- If a cell cannot process a transaction, it must be rerouted via the router to another appropriate cell.  
- Microservices communicate only with localized database instances, keeping latency predictable and avoiding unnecessary network hops.

## Benefits of the Cell‑Based Approach
- **Reduced Blast Radius**: Failures are isolated, preventing platform‑wide outages.  
- **Lower Latency**: Localized data and pod‑to‑pod communication minimize network hops.  
- **Scalable Capacity**: New cells can be added independently to increase throughput without enlarging the failure domain.  
- **Predictable Recovery**: Cells can be removed and reinstated without coordination across the system, enabling fast failover and maintenance.  

These principles collectively enable American Express to operate a resilient, high‑performance global payments platform at scale.