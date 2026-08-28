---
title: 'eric on X: "https://t.co/TL9pq7e5kN" / X'
url: https://x.com/defyneric/status/2092790674114646171
site_name: tldr
content_file: tldr-eric-on-x-httpstcotl9pq7e5kn-x
fetched_at: '2026-08-28T21:21:05.354260'
original_url: https://x.com/defyneric/status/2092790674114646171
date: '2026-08-28'
published_date: '2026-08-27T01:45:53.000Z'
description: 'Neobank 101: The 14 Ways Neobanks Make Money'
tags:
- tldr
---

## Post

Log in
Sign up

## Post

eric
@defyneric

# Neobank 101: The 14 Ways Neobanks Make Money

Most people think interchange is the only way a neobank makes money. In reality, the 1–2% earned every time a customer swipes their card is just one of MANY ways a neobank can monetize the same customer.

I've spent the last few years working with neobanks and the infrastructure companies behind them, and one thing I've realized is just how misunderstood the economics are.

Once you own the financial relationship with a customer, the number of potential revenue streams is insane.

Here are 14 of them:

Interchange Revenue

Getting the most obvious one out of the way:

Visa pays out 1–2% (sometimes higher or lower depending on the charge) for all the volume you put on their network.

This is the most common and basic way any card program generates revenue.

For every $1 million in spend, you get paid roughly $15k.

When you use card issuers like @dakota_xyz or @raincards, Visa pays them the interchange and they pass it onto you (sometimes taking a fee in the middle, depending on what plan you are on with them).

On/Off Ramps

This is more specific to crypto neobanks. When you use virtual account or on/off-ramp providers like dakota, iron, or bridge, they might charge anywhere from 5–50 bps depending on your volume.

The neobank can then charge customers 50–70 bps and keep the difference as revenue.

At enough volume, this can become a meaningful profit center. (10M in volume can net you 50k)

People argue that on/off-ramp fees are eventually going to zero, which i agree with, but i still think we're 18–24 months away from that happening.

Fx Fees

Fx fees are charged when a customer makes a purchase in a different currency than the currency their card is denominated in.

For example, if you issue a USD card and the customer makes a purchase in Europe for €1,000, that transaction needs to be converted from EUR to USD.

The card network charges an underlying fee for that currency conversion, and the neobank can add its own markup on top.

Visa's underlying cost is typically 1%, the neobank might charge the customer 2–3% and keep the difference as revenue.

I recall speaking with a RedotPay exec who mentioned they charge around 3% in FX fees because their users care less about getting the absolute cheapest rate and more about knowing their card will reliably work wherever they spend.

Yield/Treasury Products

Neobanks can offer dedicated earn products where customers move money into yield-generating accounts.

The neobank makes money on the spread. If the underlying assets generate 5% and customers earn 4%, the neobank keeps the remaining 1%.

On $100M in AUM, that's an extra $1M in annual revenue.

My personal favorite provider for this is @blend_money. I know their team well, and they give neobanks a single API integration to offer yield across T-bills, money market funds, private credit, DeFi pools, and other traditional and onchain products.

Credit Cards

Credit cards can be one of the best products for a neobank to drive more volume.

People generally prefer spending on credit over debit rails, especially businesses that want to preserve cash flow and extend how long they have to pay for expenses.

The economics can also be better. Credit cards generally earn higher interchange than debit cards, with credit programs often earning around 2–2.5% compared to roughly 1–1.5% on debit programs.

That means you can generate more spend per customer while also earning more on every dollar they spend.

The harder part is actually offering the credit. Unlike debit, you need to underwrite customers and have access to capital, typically through a debt facility that funds the credit you're extending.

But if you can solve the underwriting and capital side, credit can become one of the strongest revenue drivers for a neobank.

Float / AUM

Banks have always made money on customer deposits.

You give a bank your money for free, and they can earn a return on that capital through T-bills, lending, and other assets.

Neobanks can participate in this through sponsor banks like Column or Lead, which might pay them 2.5–3.5% on customer deposits while keeping part of the yield for themselves.

At $100M in customer balances, a 3% share is $3M in annual revenue.

The downside is sponsor banks can be expensive, sometimes requiring millions in annual fees and minimums.

For crypto neobanks, another option is using a stablecoin issuer like @dakota_xyz, which can share some of the yield generated from the reserves backing customer balances.

Dakota, for example, pays around 3% annually on stablecoin balances, without the multi-million dollar annual costs that can come with a traditional sponsor bank relationship.

The idea isn't to compete with USDC or USDT. Customer balances can automatically sit in your own stablecoin earning ~3%, then convert 1:1 back into USDC or USDT whenever the customer wants to spend or transfer.

It's essentially a gated stablecoin product designed to help neobanks earn float on customer balances.

Credit / Lending

Lending is similar to the credit card model, but instead of giving customers a card to spend from, you're giving them direct access to capital.

This is useful for larger purchases and expenses that don't make sense to put on a card, like paying large invoices, buying inventory, or covering major expenses.

There are tons of lending products a neobank can offer: working capital, personal loans, earned wage access, mortgages, and more.

The economics can be great. A neobank might raise a debt facility at 10–12%, lend that capital at 20–25%, and make money on the spread.

You can also originate and underwrite loans, then sell them to larger banks or institutional lenders, earning fees without tying up your own capital long term.

@HunterQThompson is building something similar in the space for neobanks, giving them a simple API to offer undercollateralized stablecoin credit directly to their users.

Credit is tricky though. Fraud and defaults can quickly destroy the economics if your underwriting isn't strong.

There's a famous saying in fintech: "the best thing for any fintech to do is credit, until it's not."

It's hard to get right, but when it works, credit can be an incredible wedge and revenue driver.

Payment Processing

Once you become a business's primary bank, there's no reason you should only make money when they spend money.

You can also make money when they get paid.

Neobanks can offer payment processing directly inside the account, letting businesses accept cards, ACH, stablecoins, payment links, invoices, and other payment methods.

The economics are simple. Say you integrate an underlying processor like Stripe or Whop that charges you 2.5%, then charge the merchant 3%. You keep the 50 bps spread.

At $10M in annual payment volume, that's another $50k in revenue from a customer you already acquired.

This is especially powerful for business neobanks because you can monetize both sides of the money flow:

make money when funds come in through payment processing, then make money again when they hold and spend money on your platform.

(btw coming soon to a Flex account near you)

Wires/Transfer Fees

Moving money itself can be monetized.

Neobanks can charge for domestic wires, international wires, ACH transfers, instant payouts, SWIFT payments, and other payment rails.

The economics are simple. If your provider charges you $5 for a wire and you charge the customer $25, you keep the $20 difference.

International payments can be even more lucrative because you can make money on both the transfer fee and the FX spread.

At Flex, we don't charge for ACH or international wires outside of the 1% FX cost passed through from our sponsor bank.

We have 20+ other products we can monetize, so we'd rather not price gouge customers for something as simple as moving their own money.

But for more one-dimensional neobanks, wire and transfer fees can still be a meaningful revenue stream.

Payroll

If you already own a company's banking, credit, and payment stack, payroll is another fantastic product to layer on top.

There are tons of payroll-as-an-API providers that let neobanks offer payroll without building the infrastructure themselves.

The economics can be pretty attractive too. Your provider might charge $3–5 per employee per month, while you charge $6–8 and keep the spread.

For a business with 500 employees, that's potentially another $18k–$30k in annual revenue from a customer you already have.

Deel is probably the best example of how valuable owning payroll can become, generating well over $1.5B in annualized revenue.

You don't neccesarily need to recreate Deel. Rather own another financial workflow your customer is are already paying someone else for.

Travel & Hotels / VIP Experiences

Travel is becoming an increasingly popular revenue stream for fintechs, especially those serving high-spend consumers and businesses.

Neobanks can integrate hotels, flights, and experiences directly into their app and earn a commission whenever a customer books.

For example, a hotel might pay a 10–20% commission on a booking. The neobank can pass some of that back to the customer as a discount or reward and keep the rest as revenue.

We're already seeing fintechs like Karta, Atlas Card, Navan, and Ramp build travel deeper into their products.

It gives customers better pricing and perks while giving the fintech another way to monetize spend that would've happened somewhere else anyway.

(also maybe coming to Flex soon) 👀

Subscriptions / Premium plans

This is probably the simplest revenue stream on the list.

Neobanks can charge a monthly or annual fee for premium features like higher limits, better rewards, additional cards, priority support, travel perks, accounting tools, or concierge services.

The nice part is that subscription revenue isn't directly tied to transaction volume.

If 20,000 customers pay $50/month, that's $1M in MRR before you make anything from interchange, lending, FX, or customer balances.

Amex has executed this model extremely well. Consumers will pay hundreds of dollars per year because the perceived value of the rewards and perks can be worth more than the annual fee.

A customer might pay $850 and receive $1,200+ in perceived benefits, while Amex's actual cost can be much lower because it negotiates discounts and partnerships with large merchants.

The customer gets more value than they paid for, merchants get distribution, and the neobank captures the economics in the middle.

Investing/Brokerage

This is obviously more relevant for consumer neobanks, but it can become a huge revenue stream.

You can let customers buy stocks, ETFs, crypto, money market funds, or other investments directly from the same account they already use for banking.

Depending on the structure, the neobank can make money through trading spreads, asset-based fees, securities lending, cash sweeps, or revenue sharing with the underlying brokerage provider.

There are a few companies making this much easier to integrate, via an API.

Alpaca lets neobanks embed stock and crypto brokerage directly into their products, while handling much of the brokerage infrastructure, compliance, and licensing behind the scenes.

An on-chain alternative, @glider__, by @BrianInCrypto is building something similar for tokenized assets. Neobanks can embed access to products like the Mag 7 and other investment strategies directly into their apps.

They also recently launched automated token portfolios with Bitwise, which I think is an insanely interesting product.

Robinhood is probably the clearest example of how valuable owning both the banking and investment relationship can become.

The bigger thesis is simple:

The more of the customer's financial life you own, the more surfaces you have to monetize.

Verticalized Software

I've written about this a lot, but I think one of the biggest opportunities for neobanks is embedding software products that aren't necessarily banking products, but are still finance adjacent.

If you're serving thousands of businesses in a specific industry, you already know a lot about how they operate and what other software they're paying for. There's no reason the relationship needs to stop at banking.

If you serve medical offices, you could embed AI medical billing, insurance verification, or revenue cycle management.

If you serve construction companies, you could offer CRM software, estimates, invoicing, project management, or tools for managing subcontractors.

(We actually do this at Flex since we serve a lot of construction companies)

Another software product I think would be really interesting to embed is AI agents that handle accounts receivable.

@StuutAI, built by @realtarek, is building agents that automatically chase down unpaid invoices and help businesses collect money from customers.

This makes even more sense inside a neobank because the bank already sees the money moving. If a $50,000 invoice was supposed to be paid and the funds never hit the account, that could automatically trigger an agent to start following up.

We're already starting to see this broader thesis play out across fintech.

Stripe has expanded beyond payments into finance adjacent software, including its acquisition of OpenRouter, while Ramp also recently announced its product launch of Router to move deeper into AI tokens (a new form of currency).

The opportunity here is much bigger than just banking.

There are dozens of products you can layer in: accounting, tax, AP/AR automation, inventory management, CRM, and other industry specific software.

The thesis is simple:

Once you own the banking relationship, you can start owning more of the software stack around it.

That gives you more products to monetize, increases revenue per customer, and most importantly makes the neobank significantly harder to replace.

The Bigger Picture

The biggest takeaway from all of this is that the real value of a neobank isn't any single product or revenue stream. It's owning the entire financial relationship with the customer.

Once you become the place where a customer holds their money, spends, borrows, gets paid, invests, and eventually runs more of their financial operations, you create dozens of opportunities to build products around that relationship.

This is the exact playbook we're running at Flex.

We've spent the last four years building a better financial stack for businesses, and over the coming months we're expanding into personal finance too.

By the end of the year, we'll have 30+ different financial products across the platform, each creating another way to serve and monetize the same customer relationship.

There's a line our CEO uses that I love:

"Flex is the full financial home for founders, across both their business and personal lives."

I think that perfectly captures where the future of neobanks is ultimately heading:

Own more and more of the financial relationship until your platform becomes the place customers run their entire financial lives on.

1:45 AM · Aug 27, 2026
14.2K
Views
4
10
154
229