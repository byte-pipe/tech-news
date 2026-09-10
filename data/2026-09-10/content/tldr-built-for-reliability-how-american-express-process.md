---
title: 'Built for Reliability: How American Express Processes Payments at Scale'
url: https://blog.bytebytego.com/p/built-for-reliability-how-american
site_name: tldr
content_file: tldr-built-for-reliability-how-american-express-process
fetched_at: '2026-09-10T14:50:02.119839'
original_url: https://blog.bytebytego.com/p/built-for-reliability-how-american
author: ByteByteGo
date: '2026-09-10'
description: In this article, we will try to understand how the transaction runs through such a cell-based architecture and how the payments are processed even when some services are failing.
tags:
- tldr
---

# Built for Reliability: How American Express Processes Payments at Scale

ByteByteGo
Sep 08, 2026
231
3
5
Share

## Test Your Auth Flow Without Production (Sponsored)

Authentication is often the least-tested part of an app. Live environments need network access and real credentials, while mocks miss the failures that break production.

@workos/emulate runs the WorkOS API locally for development and automated testing. Seed users, organizations, RBAC roles, and SSO connections, then test full AuthKit login flows, signed webhooks, token refresh, and error handling without touching production. Responses and event shapes come from the WorkOS OpenAPI spec, so your tests exercise the same surface your app uses in production. Run it locally or in CI with npm, Homebrew, Docker, or a standalone binary.

Run WorkOS locally

A customer making a card payment expects it to get approved or declined almost instantly. This single requirement shapes everything about how a payment is built, because the entire processing of the payment has to finish within this short window.

We recently spoke withBen Cane, a Distinguished Engineer at American Express, to understand how their platform handles it.

To understand how things work, let us picture what happens when a transaction arrives at American Express. It is routed into one of several independent processing units and moves through a chain of microservices. However, partway through, one of those services begins to fail, and the customer at the checkout terminal is still waiting.

Just retrying the transaction inside the failing unit carries obvious risk. Also, moving the transaction to another server is an even harder problem. This is because the second unit would need to know how far the first transaction went. Sharing such knowledge creates a dependency that can turn two independent units into a fragile system.

The American Express engineering team handles this witha cell-based architecturethat helps keep the impact of a disruption to a minimum. In our chat with the engineering team of American Express, we learned that most of the engineering effort goes into keeping that isolation intact under pressure. In this article, we will try to understand how the transaction runs through such a cell-based architecture and how the payments are processed even when some services are failing.

# Core Payments Ecosystem

In a typical payment flow, American Express sits in the middle of a chain. A merchant holds a relationship with an acquiring bank that sends the transaction to American Express, and American Express delivers it to the card issuer that holds the account balance. This middle hop is the core payment network’s job.

See the diagram below that shows this setup:

In 2018, American Express began modernizing this platform onto cloud-native infrastructure. Immediately, it was clear that one assumption had to change. While the older systems ran on hardware engineered to stay running, the cloud infrastructure behaved differently. Servers could disappear for reasons outside any one team’s control. You have to assume failures completely outside your control will happen more often, and build the application around that.

Two familiar patterns were considered:

* Event-driven processing fit poorly. The workload needs to run at scale with low latency and a real-time response, leaving little room for delay. Asynchronous work exists, but the answer itself still has to arrive fast.
* A monolith is where most teams start, but it fits the scaling requirements poorly.

The design American Express engineering team ultimately chose was driven, in part, by decades of internal thinking. Ben pointed out that back in the SOA era, long before microservices existed as a concept, his teams were already trying to reduce the impact of a single failure on a specific system. The patterns were present even before the more formal term of cell-based architecture was coined.

# Cell Boundaries

In a cell-based architecture, a cell is a complete, self-sufficient copy of the payment processing stack. In other words, everything required to process a transaction lives inside one boundary. This includes microservices, databases, DNS, and supporting infrastructure.

There are five key properties of a cell:

* It deploys independently and processes payments on its own.
* It owns its microservices, databases, and other components.
* It forms a single failure domain, so problems inside stay inside.
* It can be pulled out of rotation for maintenance or during an incident, with the rest of the platform carrying on.
* It does not have synchronous cross-cell dependencies in the critical path.

Reference data still replicates across cells, observability data can aggregate across cells, and router instances communicate with each other across cells. What stays out of the critical path is any blocking call between cells during transaction processing.

To put it differently, a cell is defined by its failure boundaries rather than by a specific infrastructure construct. Cells stay within a single region with everything needed for processing local inside that boundary.

Deciding on the appropriate size of a cell requires judgment. The engineers at American Express think of it as a balancing act. You don’t want to put the entire enterprise within a cell. Ideally, it is better to draw the boundary around the journey being supported. In the case of payments, this means the minimum components required to produce an immediate answer. In other words, the real-time journey of a transaction. The after-the-fact journey can still be handled in a different cell.

To be clear, cells are not the same as microservices. While microservices divide a system by function, cells divide it by failure. One cell can contain many microservices. The boundary matters because whenever we leave the cell, we enter dangerous territory and need the right resiliency capabilities, processes, and business logic to handle the potential failures.

# Data Locality

A cell remains self-sufficient only when the data it needs already resides within it. The American Express engineering team has three strategies to deal with data, chosen according to how often the data changes:

* Immutable data is set up once and stays fixed thereafter.
* Semi-static data changes anywhere from every couple of hours to once a year. For example, exchange rates, merchant category codes, and country codes.
* Dynamic data changes with every transaction.

For the first two categories, American Express distributes the reference data to every cell before any transaction needs it. The alternative would be a fall-through read, meaning a lookup that misses the local cache and travels to a central system of record while the transaction waits. Pushing the data ahead provides multiple benefits:

* The first transaction avoids paying for a cold cache.
* The critical path avoids a synchronous call leaving the cell.
* The replication work runs entirely outside the transaction path.

Ben contrasted this with the more common pattern. He said that they lean toward push and distribute rather than the traditional pull and then cache, which spares that first transaction from building up caches.

However, the same approach falls short for dynamic data. Replication runs quickly and asynchronously. But it still leaves a window where a cell may hold stale state when a transaction arrives. Sending a transaction to a cell with stale data would add latency and risk a processing failure.

To deal with this scenario, American Express inverts the problem. Rather than moving the data to the transaction, the platform moves the transaction to the data.

This works through deterministic routing, meaning the decision follows from the transaction’s own contents rather than from cell load or availability. Some example attributes for this transaction content are partner, market, and payment type. A component called the Global Transaction Router makes the decision at the front door. We will look at it in more detail in the next section.

Deterministic routing is one of two modes. The router also supports priority-based routing in which cells carry a specific ordering and traffic goes to the highest-priority healthy cell available. The choice of the mode that is used depends on the use case.

However, this routing is not a universal rule. American Express applies deterministic routing selectively, where transactions require strong consistency between them. This depends on the transaction type. Some types carry minimal data requirements and can be routed freely.

Message-based replication between cells continues throughout, so failover data exists in more than one place. Timing is the important part here, because every in-flight transaction proceeds without waiting for replication to finish.

# Global Transaction Router

The Global Transaction Router routes traffic and enforces the cell boundary at the same time.

Every transaction enters a cell through the router, and any transaction moving to a different cell travels back through it as well. Cells lack any ability to communicate directly, which makes the router the single path between them. The result of this setup is a payments mesh that connects cells globally while also keeping them independent.

See the diagram below:

The router handles external traffic on the same terms. When a cell finishes its work and the transaction needs to reach a card issuer, the cell returns it to the router. The router then makes that outbound call. Cells don’t talk outside their own boundary, whether the destination is another cell or an outside institution.

Concentrating that much responsibility in one component raises the obvious question: How does a component that every transaction depends on avoid becoming the platform’s weakest point?

The answers from American Express engineers can be split into parts.

The first is keeping the router deliberately simple. They keep business logic out of the router and give it just enough message parsing capability to extract certain values and route on them. The knowledge of what those values represent falls outside its job. The inputs vary by transaction type, sometimes a header value and sometimes a field inside the card transaction message.

Keeping this restraint is crucial because a router that was too deeply integrated with payment logic would accumulate business rules. Those rules would require data, and that data would require lookups. The component would gradually become a centralized system, which the cell-based architecture seeks to avoid.

The second direction is reducing what the router depends on. Here are a few things that are taken care of:

* Dependencies stay minimal. The closer a component sits to the edge, the fewer dependencies it carries.
* State stays out of persistent storage. Router state lives in non-persistent stores, which keeps instances as close to stateless as the design allows.
* Remaining dependencies run asynchronously. Logging uses an asynchronous logger with a buffer truncation policy, so a full buffer drops log records rather than blocking transaction processing.
* Configuration loads into memory and updates asynchronously, so an unreachable config service leaves the router running on last known good values.
* Instances run in parallel across regions. Multiple instances, multiple regions, and multiple connections mean an unavailable path always has a backup.

During the discussion, Ben also gave a clear preference on deployment posture. He said he would avoid active-standby as much as possible and run something like this as active as possible, since active-standby earns its place mainly when you have state to manage.

The lesson even applies beyond payments. Some chokepoints are part of the structure, because the architecture needs one place where cross-boundary decisions happen. The best way to deal with that is to make that chokepoint simple enough to trust, and spend the engineering budget on keeping it that way.

# Credit Card Authorization Flow

Let us now look at a card authorization flow that we got from the American Express team to understand how things work even more clearly.

The journey of a transaction starts outside the American Express systems. A card gets used at a merchant’s point-of-sale terminal. From there, the sequence goes as follows:

* The Global Transaction Router receives the request first.
* The router applies deterministic or priority-based routing. The choice depends on the use case.
* Inside the cell, a collection of microservices performs validation, enrichment, transformation, and issuer determination.
* The cell returns the transaction to the router.
* The router sends the request to the appropriate card issuers for authorization.
* The issuer response arrives back at the router.
* The router uses deterministic routing to reach the cell holding the context of the transaction for authorization.
* The cell validates the response.
* The transaction travels back to the merchant’s acquiring bank.
* The final confirmation of the payment is sent back to the POS terminal.

One thing to note is that the cell never contacts the card issuer directly. This preserves the rule that cells should not communicate with anything beyond their boundaries.

See the diagram below that shows the process in detail:

# Mid-Transaction Failure

Let us now return to the transaction that we talked about at the beginning of the article.

Payments processing at American Express uses an orchestrated microservices architecture. This means one orchestrator microservice manages the workflow and calls the other microservices in turn. This orchestrator also monitors the health of those microservices continuously and detects failures.

Here is the full sequence of events that happen once a required service starts failing, or when too few instances of that service are running to handle it.:

* The orchestrator detects the failure and halts processing.
* It sends the transaction back to the Global Transaction Router.
* The router selects a healthy cell.
* Processing restarts in that cell using the original transaction data.

The last step is where the design diverges. American Express discards the partial work. Every microservice call the failing cell completed gets thrown away, and the second cell starts from the beginning with the same input. This rerouting covers both new transactions arriving at the failing cell and transactions already in flight inside it.

The reasoning behind this approach goes back to the boundary problem. Resuming a transaction would require the second cell to read state from the first. However, that link would create shared state between cells. Shared state brings synchronization problems and consistency risks during failover, which is the exact problem this architecture seeks to avoid.

The result of this choice is that cells stay loosely coupled. Each cell runs its own database clusters, the microservices inside a cell communicate with the local cluster only, and a rerouted transaction is processed with zero reliance on state from the previous cell. The orchestrator also runs application health checks against the service mesh’s readiness endpoints. When overall cell health degrades past an acceptable threshold, the orchestrator reports the cell as unavailable.

Redoing completed work sounds wasteful. However, the trade-off works because a payment is short, so redoing a few hundred milliseconds costs very little against the alternative of a permanent structural dependency between every pair of cells. In a system where one unit of work runs for minutes, checkpointing might seem more favorable as an approach.

# Recovery Semantics

Restarting a transaction elsewhere can be done up to a specific moment. Think of it like a point of no return. The exact position of that moment is a design decision that a team needs to make. For example, rerouting is safe while a transaction remains inside the core payments ecosystem, and once it has gone to an external system such as a card issuer, it stays where it is.

Card authorizations are structured so the point of no return falls toward the end of processing. American Express placed the irreversible step as late as the payment flow allows, making the recoverable window as wide as it can be.

For payment types where late rerouting of the transaction is not possible, safety comes from idempotency.

Each transaction carries a unique identifier consistent across every retry and reroute, and downstream systems use it to suppress duplicates. Failback is controlled with canary capabilities using percentages. They avoid bouncing everything back the moment a cell returns. Also, shifting traffic by percentage lets American Express drain a cell gradually, validate a recovering cell under partial load, or respond carefully during an incident.

But this opens up another question: How does the platform prevent a recovered cell from writing stale state after its transactions moved elsewhere?

There are three mechanisms here that narrow the window:

* Speed:Card payments move so fast that by the time a failed cell returns, the transaction has usually completed elsewhere.
* Idempotency identifiers:Duplicate suppression happens downstream, using the identifier that travelled with the transaction.
* Paced recovery:Percentage-based traffic control governs when and how much work a recovering cell receives.

The specific details can vary. Recovery in finance might mean waiting for something to sync, accepting eventual consistency, or creating a compensating transaction, depending on the transaction type and where the failure occurred.

# Design Tradeoffs

Let us now look at the trade-offs in the architecture implemented by American Express.

* Duplicated services:Enforcing the boundary sometimes produces duplicate implementations of the same service across cells. American Express accepts this cost because it preserves cell independence and removes cross-cell network hops. Naturally, preventing cross-cell dependencies grows harder as a platform grows, so the cost increases over time.
* Dropped log records:The buffer truncation policy means that under sustained pressure, the platform keeps processing transactions while losing part of the record of what it did. To be clear, these are application logs meant for general observability and not critical transactional events.
* Delayed global visibility:Each cell writes logs, metrics, and traces locally first, with aggregation to global dashboards happening asynchronously. Losing part of the stack degrades visibility for one cell instead of the platform. The global view always lags.
* Rejected transactions:Data synchronization between cells runs asynchronously. The consistency requirements depend on the transaction type and the business rule. When a transaction requires strong consistency, but the required data cannot be validated or turns out to be inconsistent, American Express may reject that transaction to preserve data integrity.

Also, one thing to note about cells is that they change how many fail at once rather than how often failures happen, since running more independent units arguably produces more individual failures. In other words, management overhead and complexity are traded off for reduced impact of a failure.

# Conclusion

The payment platform built by the American Express engineering team survives a cell failure because the design doesn’t allow one transaction to depend on two cells at once.

Here are the key points that make it work:

* Two data strategies, one goal:Reference data that changes rarely gets pushed to every cell ahead of time, while data that changes constantly stays put and the transaction travels to it.
* A thin component at the chokepoint:The Global Transaction Router carries enormous responsibility and very little logic, which makes it dependable.
* Restart in place of resume:Discarding partial work costs a few hundred milliseconds and removes the shared state that would link every cell to every other cell.
* A recovery window with a chosen position:Placing the point of no return late in the sequence widens the range in which failure remains survivable.
* Recovery semantics from the domain:The pattern provides structure, and business logic provides the rules for what a partially completed transaction requires.

References:

* Cell-based Architecture for Resilient Payment Systems
231
3
5
Share