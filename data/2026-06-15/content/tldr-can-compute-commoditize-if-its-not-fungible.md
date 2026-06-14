---
title: Can Compute Commoditize if it's Not Fungible?
url: https://davefriedman.substack.com/p/can-compute-commoditize-if-its-not
site_name: tldr
content_file: tldr-can-compute-commoditize-if-its-not-fungible
fetched_at: '2026-06-15T06:00:24.298826'
original_url: https://davefriedman.substack.com/p/can-compute-commoditize-if-its-not
author: Dave Friedman
date: '2026-06-15'
description: Fungibility is not a requirement for commoditization
tags:
- tldr
---

# Can Compute Commoditize if it's Not Fungible?

### Fungibility is not a requirement for commoditization

Dave Friedman
Jun 11, 2026
8
2
Share

Please see relevant disclosureshere.

On a recent episode of Bloomberg’sOddLotspodcast, CoreWeave co-founderBrannin McBeewas asked whether compute will ever trade as a commodity. His answer was a careful no-for-now, maybe-later, and it rested on one claim: compute isn’t fungible the way a commodity has to be. To make the point he reached for gold. Gold is defined by its chemical composition; an ounce is an ounce. An H100-hour in one cloud, he argued, is not an H100-hour in another. They have differentgoodput, differentmodel-flop utilization, different operational reality under the same nameplate. No fungibility, no commodity.

Gold is a convenient analogy because it turns fungibility into a binary. But commodity markets rarely work that way, and McBee, of all people, knows it. Before CoreWeave he traded natural gas, power, and agricultural products. Power has locational basis, meaning the same megawatt is worth different amounts at different nodes, and the congestion between them is itself a traded product. It has firmness (firm versus interruptible) and temporal shape (peak versus off-peak). Gas has Henry Hub and then an entire complex of basis swaps pricing every delivery point against it. These are among the deepest derivatives markets on the planet, and they got there in spite of non-fungibility, not because of homogeneity. Commodity market design has never required sameness. It requires a standardizedreferenceplus abasisyou price separately. The art is inventing a fungible reference and trading the deviations around it.

So the easy version of the case against McBee ( “he doesn’t understand commodity markets”) is wrong. He understands them perfectly. That’s exactly why his objection is worth taking apart.

The substantive objection to commoditization is that compute lacks a cleanconvergence mechanism. Gas has pipes, storage, nominations, and delivery points. Power has nodes, congestion, dispatch, and transmission rights. Those are the plumbing that forces a sprawling physical market to converge onto a price. Compute has clusters, queues, software environments, failure domains, data gravity, security requirements, and workload-specific performance, and no settled plumbing to make them converge. That doesn’t make a market impossible. It tells you what the first tradable product might look like: a cash-settled reference exposure wrapped in wide, messy, explicitly priced spreads for operator, topology, scale, duration, and SLA.

Which is the right way to read McBee’s own tell. “We build everything to DGX reference spec,” he says. That is Nvidia’s blueprint, the most performant standardized way to deploy their GPUs. That isn’t the hub; it’s thegrade. It’s pipeline-quality gas, .995 fine gold, the specification a contract can be written against. The hub is the index and settlement convention built on top of it. And the goodput and MFU differentials he keeps emphasizing? Those are the basis. Split fungibility into its layers and the picture resolves: physical/spec fungibility (GPU class, DGX spec, fabric, cooling) is largely there; operational fungibility (goodput, failure recovery, the software stack) and contractual fungibility (duration, SLA, priority, scale, delivery window) are not yet. McBee is right that the back two layers aren’t settled today. But that’s not an argument against a market. It’s a specificationof the basisa market would price.

So why does he make this argument? Because the non-commodity framing is the keystone of a whole valuation bundle the market has accorded CoreWeave: long useful lives for its GPUs, its operator moat, contracted rather than merchant cash flows, and a cost of capital that’s fallen far enough to let CoreWeave raise more than $21 billion year to date. The depreciation debate and the fungibility debate are the same fight in different clothes: a commodity on a merchant curve gets you brutal depreciation, price-taker margins, and a utility multiple; a differentiated operator on contracted flows gets you benign depreciation, pricing power, and a software multiple.

McBee’s frontier point is real, his caution is rational, and he is plainly talking a sophisticated book rather than making an error. But the man knows what a basis swap is. When a former power trader tells you locational differentials prove there can be no market, he isn’t describing the commodity. He’s pricing it, and telling you where the spread still hides.

If you enjoy this newsletter, consider sharing it with a colleague.

Share Buy the Rumor; Sell the News

I’m always happy to receive comments, questions, and pushback. If you want to connect with me directly, you can:

* follow meonTwitter,
* connect with meonLinkedIn, or
* send an emailto dave [at] davefriedman dot co. (Not .com!)
8
2
Share
Previous
Next