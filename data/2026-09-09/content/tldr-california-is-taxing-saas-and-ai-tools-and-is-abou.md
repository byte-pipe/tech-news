---
title: California Is Taxing SaaS and AI Tools and Is About to Make Your Software 8-10% More Expensive. Here’s What SB 122 Does to Buyers and Vendors | SaaStrAI
url: https://www.saastr.com/california-is-taxing-saas-and-ai-tools-and-is-about-to-make-your-software-8-10-more-expensive-heres-what-sb-122-does-to-buyers-and-vendors/
site_name: tldr
content_file: tldr-california-is-taxing-saas-and-ai-tools-and-is-abou
fetched_at: '2026-09-09T15:29:58.433117'
original_url: https://www.saastr.com/california-is-taxing-saas-and-ai-tools-and-is-about-to-make-your-software-8-10-more-expensive-heres-what-sb-122-does-to-buyers-and-vendors/
date: '2026-09-09'
published_date: '2026-09-05T14:10:29+00:00'
description: California Is Taxing SaaS and AI Tools and Is About to Make Your Software 8-10% More Expensive. Here's What SB 122 Does to Buyers and Vendors (13 minute read)
tags:
- tldr
---

# California Is Taxing SaaS and AI Tools and Is About to Make Your Software 8-10% More Expensive. Here’s What SB 122 Does to Buyers and Vendors

byJason Lemkin|Blog Posts

On June 29, 2026, Gavin Newsom signed SB 122. Effective January 1, 2027, California sales and use tax applies to prewritten software and SaaS, however it’s delivered. Downloaded, streamed, accessed in a browser. All of it.

California was the last giant holdout. For three decades the state taxed software on a disc and not software in a browser. That line is gone. California now joins 20+ states that tax SaaS in some form, and the state projects roughly $2B a year in combined state and local revenue from the change.

The rate is California’s full stack: 7.25% state, plus local district taxes on top. Depending on the buyer’s address, that’s 7.25% to about 10.75%. Call it 8-10% for most customers in most real metros.

It hits you as a buyer and as a vendor, and the second one is where most B2B founders haven’t done the work yet.

## What actually changed in the law

SB 122 amended the definition of “tangible personal property” to include “digital products,” defined as prewritten computer software transferred on physical media, transferred electronically, or accessed remotely. California didn’t build a new tax for software. It moved software into the sales tax it already had.

What’s taxable:your products, most likely. Prewritten software, meaning anything held or existing for general or repeated sale.That describes essentially every B2B product on the market. If you built it once and sold it many times, it’s prewritten, even if it started as a custom build for one customer.

What’s not:

* Custom softwareprepared to the special order of a single customer. Modifications to prewritten software count as custom only to the extent of the modification, and only if the charges are separately stated.
* Digital infrastructure, which is how the statute describes IaaS and PaaS, where the customer deploys and runs its own software on the provider’s platform. Your AWS and GCP compute bill sits outside the tax base.
* Human effort servicesdelivered electronically, where the effort originates after the customer requests it. The carve-out explicitly does not apply to SaaS access rights.
* Digital books, music, video, video games, and crypto.

Sourcing:remote sales go to the purchaser’s known California address, in priority order: billing address, then shipping or delivery address, then the address on the payment instrument, then mailing address. Place of use is where the person accessing the software is located. There’s a presumption of California use for anything bought outside the state and used in it within 90 days.

Nexus:SB 122 didn’t create a new threshold. It made software sales count toward the existing one. Physical presence in California, or $500,000 in California sales for a remote seller. A lot of B2B companies that have never dealt with CDTFA are about to become registrants.

The $5M flip:if one vendor’s digital product sales to one purchaser exceed $5M in a calendar year, the vendor is relieved of the collection obligation and the purchaser self-assesses and remits use tax directly. CDTFA clarified the mechanics at its July workshop: vendor-specific, measured over 12 months, and the shift happens on the transaction that crosses the line.

{“model_id”: “unified-v1/prod/20260818-030536”}

## If you buy software in California: an 8-10% price increase you didn’t negotiate

Take your 2027 software budget, filter to what’s actually taxable, multiply by your district rate. For a company spending $2M a year on tools, that’s $160-200K of new expense that buys you nothing.

Four things about how it lands.

It stacks on vendor increases.If your Salesforce contract carries a 7% annual uplift and the state adds 9%, your renewal invoice is up 16-17% for the same seats. Only half of that is negotiable.

You can’t recover it.This isn’t VAT. No input credit, no refund mechanism. It comes straight out of gross margin and stays there.

Bundling decides how much of the contract is taxable.If you buy a platform that includes software access plus implementation, support, and managed services, CDTFA applies a true object test to figure out what you’re really buying. A bundle billed as one line item is taxable in full. The same deal with services broken out separately may only be taxable on the subscription. Ask your top ten vendors now how they plan to invoice in January, because their answer sets your number.

If you’re big, the compliance burden is yours.Cross $5M with a single vendor and you now own a use tax self-assessment function on your largest software relationship. It’s more than accruing a number: you need a use tax direct payment permit, you issue an exemption certificate to the vendor, and you report local use tax broken out by each county or city where first use occurs. That’s a new process for most finance teams, and the penalty for not having it accrues quietly.

One thing you probably can’t do: fix it by changing the billing address. SB 122 contains no multiple points of use mechanism. Unlike New York, Texas, and Massachusetts, the statute has no method for allocating a purchase across states. It does authorize CDTFA to approve alternative calculation methods for software used concurrently in multiple locations, and at the July workshop the department said it may build a purchaser-side exemption certificate and is looking at apportionment modeled on other states, including Massachusetts, based on user or device location. For purchases under $5M it floated either a real-time certificate or a back-end refund.

So allocation is probably coming, through regulation rather than statute, and it’s being drafted right now. What you can do today is get user and device location data clean, so that when the certificate mechanism exists you can substantiate an allocation instead of estimating one. Moving a contract to an Austin billing address while the users are still in San Francisco won’t survive an audit, because place of use under SB 122 is where the person accessing the software sits.

## Nobody knows yet whether your LLM API bill is taxable

AI application subscriptions are clearly in scope. Commentators are already listing them alongside Microsoft 365 as prewritten software accessed remotely. Buy a seat-based AI product, pay the tax.

Consumption-based AI spend has no answer yet.Paying per token or per API call for model access could be remotely accessed prewritten software, which is taxable, or digital infrastructure, meaning a platform where you deploy and run your own software, which is excluded. The statute doesn’t resolve it. CDTFA has flagged usage-based pricing and freemium models as open items, and separately acknowledged that the boundary between taxable software and excluded digital infrastructure may get settled by legal opinions and litigation rather than by regulation.

The human effort exemption doesn’t obviously help either. CDTFA framed it as a true object test: accessing software for its function is taxable, accessing human effort delivered through software is exempt. Model inference is neither, and the department was candid that it hasn’t defined how much human effort qualifies.

So a California CFO is looking at a 9% swing on the fastest-growing line in the software budget, with no way to forecast it. And a founder selling an AI product into California has an unsettled classification where both errors cost money: collect when you shouldn’t and you’ve overcharged every customer, don’t collect when you should and the liability is yours with interest.

## If you sell software into California: four things that are actually in your control

1.Register and collect, or pay it yourself.If you have nexus and don’t collect, you still owe the tax, with interest, whenever someone finds it. The work is registration with CDTFA, classifying each SKU as taxable or exempt, wiring district-rate calculation to the billing address, and building an exemption certificate process. Avalara, Anrok, and Stripe Tax handle the mechanics. Classification is your call, and it’s the part with real money in it.

2.Restructure how you invoice.Separately stating implementation, training, support, and managed services from the software subscription is the difference between your customer paying tax on the whole contract or on the licensed portion only. A one-line bundle is taxable in full. This is the change with the biggest dollar impact for your customers and it costs you nothing but billing work, so do it before your systems freeze for Q4.

3.Use Q4 2026 as a cash flow event, carefully.CDTFA said at the workshop that a taxable transaction on or after January 1, 2027 requires both a right to use and consideration given after that date. That’s the hook for early renewals invoiced and paid in December. But the department declined to say whether the contract date or the payment and access date controls for renewals and multi-year agreements. Transition rules for straddling contracts are on the list the emergency regulations are supposed to resolve.

The offer writes itself: renew early, we invoice in December, you prepay the term, you save 8-10% versus January. Customers get real savings, you pull revenue forward and get cash in this year. Put a tax gross-up clause in the paperwork so the customer bears it if the rules land the other way, and don’t sell it as “guaranteed no tax.”

4.Tell sales and CS now.The worst version is a customer finding a 9% line item on a January invoice and emailing their AE, who then improvises an explanation of California tax policy. Arm the team with a one-paragraph explanation, the list of affected accounts, and whatever concession you’re authorizing. Some vendors will waive their standard annual uplift on CA accounts to soften the combined number. That costs real permanent margin to offset a tax you never keep, so do it on accounts where the renewal is genuinely at risk, not as blanket policy.

On churn, model it but keep it small. Twenty-plus states already tax SaaS and B2B companies have collected in them for years without a cliff.California is different only in concentration. If a third of your ARR is in one state and every account reprices on the same day, the aggregate drag on net revenue retention shows up even when the per-account effect doesn’t.

## Your AWS bill is exempt. The hard part is everything between AWS and Salesforce.

The infrastructure carve-out is real and it’s (likely) broader than most people assume. SB 122 excludes “digital infrastructure,” which the statute describes as a remotely provided cloud service that lets a user create, deploy, scale, or run the user’s own software on the provider’s platform without having to manage the underlying hardware, networks, and facilities. IaaS is clearly out. PaaS is named in the exclusion too.

The test underneath it: whose software performs the task. If you’re running your code on their machines, that’s infrastructure and it’s excluded. If you’re using their code to do a job, that’s prewritten software accessed remotely and it’s taxable.

#### The ends are easy. EC2, S3, and GCP compute are excluded. Salesforce, Slack, HubSpot, and Microsoft 365 are taxable.

The middle is not resolved, and the middle is where a lot of modern spend sits. BDO flagged PaaS specifically as sitting between taxable remote-access software and the excluded category. Others have flagged platforms that combine infrastructure with an application layer on top. Data warehouses, workflow platforms with both a runtime and prebuilt apps, developer platforms, and most managed AI services all have that shape. CDTFA acknowledged at its July workshop that the boundary is unresolved and said some of these outcomes may get settled through legal opinions and litigation rather than rulemaking.

Two practical consequences. If you’re a buyer, sort your top vendors into three buckets now, clearly exempt, clearly taxable, and gray, and go get the gray vendors’ written position before January. If you’re a vendor sitting in the middle, pick your classification, document why, and separate the infrastructure and application charges on the invoice. A hybrid platform billed as one line item defaults to fully taxable, and that’s a choice you’re making by not making it.

## CDTFA writes the actual rules between now and December

CDTFA has two-year emergency regulatory authority here. The department expected to circulate a discussion draft of the emergency regulations by the end of August 2026, followed by an Interested Parties Meeting in late August or September, and submission to the Office of Administrative Law in early December, right before the effective date.

Transition rules, bundling, the human effort line, and multiple points of use all get written in that window, and public comment is open. Submitting your product’s fact pattern now costs you a few hours of a tax advisor’s time. Getting the classification wrong costs you the tax, plus interest, on every California invoice from 2027 forward.

Also worth putting in the 2027 model: Colorado’s expansion to electronically delivered prewritten software and SaaS takes effect the same day. Two of the largest state economies moved in the same direction in the same session. Assume more follow.