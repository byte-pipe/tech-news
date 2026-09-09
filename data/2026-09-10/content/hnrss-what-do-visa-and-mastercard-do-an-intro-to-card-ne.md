---
title: What do Visa and Mastercard do? An intro to card networks @ tautology.town
url: https://tautology.town/2026/06/01/card-networks.html
site_name: hnrss
content_file: hnrss-what-do-visa-and-mastercard-do-an-intro-to-card-ne
fetched_at: '2026-09-10T07:21:05.612779'
original_url: https://tautology.town/2026/06/01/card-networks.html
date: '2026-09-08'
description: tautology.town is a blog that contains tautologies.
tags:
- hackernews
- hnrss
---

Most people can recognize the Visa and Mastercard brands. Chances are, you use one of their cards to transact every day. You may have some notion that most places (in the US) take both, but some places only take Visa (e.g. Costco), and vice versa.

So what do they do?Here’s Visa’s attemptto answer that question.

A few things they don’t do1:

* They aren’t the company that issues the card. Those are calledcard issuers.
* They aren’t a bank, though the cards you have are probably issued by one (Chase, Capital One, BofA, etc).
* They don’t distribute point of sale methods or online checkouts, which are done bypayment processors.
* They aren’t responsible for onboarding or underwriting stores and merchants, known asmerchant acquiring. This is done by banks offering merchant accounts, but increasingly offered by modern payment processors (Stripe, Square, Adyen)2.
* They don’t manufacture or print cards.
* Nor do they manufacture the point of sale hardware.

Instead, Visa and Mastercard arecard networks3, facilitating card transactions by connecting the cardholders and issuers to the merchants and acquirers.

This forms atwo-sided marketof all the participants in a transaction4:

---
config:
 theme: 'neutral'
 fontFamily: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
 nodeSpacing: 20
 rankSpacing: 25
 flowchart: 
 subGraphTitleMargin: {bottom: 20}
 useMaxWidth: true
---
%% For some reason arrows are still showing up in the Obsidian preview, but not in Mermaid online editor
flowchart LR
 subgraph Issuing[**Issuing**]
 direction TB
 CI[Card issuer] --- CH[Cardholder]
 end
 subgraph Acquiring[**Acquiring**]
 direction TB
 MA[Merchant acquirer] --- M[Merchant]
 end
 Issuing ---- CN[**Card network**]
 CN ---- Acquiring

The key players in a card transaction.

The card network’s job is to enable card transactions, and also to grow participation in their networks.

This boils down to four key responsibilities:

1. Run the telecommunications network to route transaction messages.
2. Coordinate the banking network to move money and settle transactions.
3. Set the incentives to encourage the use of the network.
4. Set and enforce rules of the network, including a mechanism for disputes.

For the rest of the discussion, we’ll focus on Visa, as it’s what I’m most familiar with from my years in the payment industry. Mastercard is more or less the same, with different names for things.

# 1. Run the telecommunications network

When we talk about networks, we think of the Internet, computers connected together by fiber anddeep sea cables.

Card networks, being telecommunication networks, are no different. They maintain data centers and lease fiber optics cables to connect issuers and acquirers electronically. At their most basic technical level, Visa’s responsibility is forwarding transaction messages between its participating issuers and acquirers. Mastercard calls this activity “switching”, seeing itself as a network switch.

Visa takes its data centers very seriously. They are highly secure, redundant, and fitted to survive all kinds of disasters. FromInside Visa’s Data Center (Network Computing, 2013):

“The company’s flagship data center, dubbed Operations Center East, or OCE, is a 140,000-square-foot facility that Visa will only say is located “somewhere along the Eastern seaboard.”

“Not surprisingly, the facility, which is also designed to withstand earthquakes and gale-force winds up to 170 miles per hour, is locked down like a digital Fort Knox. The roads entering the complex have hydraulic bollards that can shoot up fast enough to stop a vehicle traveling up to 50 miles per hour dead in its tracks. (The road is too curvy to drive safely at higher speeds.) Visitors must pass through a security gate, be cleared by roving security teams, and then be subjected to a biometric scan before being admitted.”

And a 2012 headline fromUSA Today:

Top secret Visa data center banks on security, even has moat

That top secret location? InAshburn, Virginia, conveniently located by Topgolf and Trader Joe’s.

I think the "moat" is the pool of water on the top center-left.

## Authorization and clearing messages

When a card is used, the card network routes a transaction request, known as anauthorization, from the merchant to the issuer. The issuer then approves or declines the request in a response. Card numbers, also known asPrimary Account Numbers (PANs), are used like IP addresses5. The first 6 to 8 digits of the PAN identifies the card issuer and is called theBank Identification Number (BIN)

An approved authorization places a temporary hold on the account for the amount of the transaction. Later, the merchant submits the final transaction amount (for example, adding tips written on receipts or voiding the transaction) to initiate the transfer of money, known asclearing6.

Consider: before this was done by computers, this was done by people via phone calls7and mail.

# 2. Coordinate the banking network

In addition to a telecom network, Visa has afinancialnetwork of banks.

After a transaction is finalized, money on both ends must move to fulfill the transaction, known assettlement.

Visa’s second job is toroute moneyfor settlement by having financial relationships with each party. It can collect money from one and transfer to another.

To be efficient, Visa doesnet settlement: every day, each network participant’s debits and credits are totalled, and at the end of the day the net money is moved to or from each participant once.

For domestic transactions, moving money isrelatively straightforward, thanks to central banks.

Importantly, Visa is also able to settle internationally, evenhandling currency conversion. Visa acts as anadapter between banking systemswith its global banking relationships. This greatly simplifies international money movement for participants in its network — without Visa, each participant would need to manage their own international banking relationships.

---
config:
 theme: 'neutral'
 fontFamily: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
 nodeSpacing: 20
 rankSpacing: 60
 flowchart: 
 subGraphTitleMargin: {bottom: 20}
 diagramPadding: 10
 useMaxWidth: true
---
flowchart LR
 CI[Issuer in Country A] --> VisaA["Visa's bank in A"]
 VisaB[Visa's bank in B] --> MA[Acquirer in Country B] 
 subgraph **Visa**
 VisaA -.-VisaB
 end

Visa as an adapter

Shuffling this amount of money around and timing everything right is no easy feat. Visa faces non-payment risk in addition to maintaining a significant balance to cover payouts while waiting to receive settlement payments. FromVisa’s 2024 annual SEC report:

Most U.S. dollar settlements are settled within the same day and do not result in a receivable or payable balance, while settlements in currencies other than the U.S. dollar generally remain outstanding for one to two business days, which is consistent with industry practice for such transactions. … As of September 30, 2024, we held $11.2 billion of our total available liquidity to fund daily settlement in the event one or more of our financial institution clients are unable to settle, with the remaining liquidity available to support our working capital and other liquidity needs.

The Company’s settlement exposure is limited to the amount of unsettled Visa payment transactions at any point in time, which vary significantly day to day. For fiscal 2024, the Company’s maximum daily settlement exposure was $137.4 billion and the average daily settlement exposure was $84.3 billion.

# 3. Set incentives

The key to this whole arrangement are the fees required to participate in the network, largely set by the network.

Let’s walk through an average credit card transaction in the US:

1. A cardholder pays for a product at a merchant for $100.00.
2. The merchant pays 2.5% ($2.50) of the transaction to their payment processor or merchant acquirer. The 2.5% is themerchant discount rateor MDR.
3. The payment processor keeps 0.35% ($0.35), then pays 2% ($2.00) to the cardholder’s issuing bank and 0.15% ($0.15) to Visa. The 2% is theinterchange fee, commonly known asinterchange. The 0.15% is thenetwork assessment fee.8
4. The issuing bank keeps 2% ($2.00)!

Surprisingly, the issuing bank keeps most and the network takes the least, by an order of magnitude! This is because for the tranasction, the issuer is traditionally considered to take on most of the risk (although merchants are likely to disagree).

In addition toregulatory requirements, Visa and Mastercard offer zero-liability protection. This means that the issuing bank, not the cardholder, is liable for any charges made on a card if it is lost or stolen.9The issuing bank also takes oncredit risk, and must always pay for an approved transaction even if a cardholder cannot pay off their balance.

Out of these, the network sets the interchange and network assessment fee. Interchange fees vary dramatically based on the kind of card, category of spend, and even the metadata attached to a transaction. The network’s goal is to set fees that incentivize desired behaviors on their network, including using more secure payment methods (lowering interchange fees for merchants), or for companies to do more business spending (higher interchange fees on commercial credit cards).

Because of how much is given to the issuers, there are a lot of incentives for issuers to acquire customers and fund lavish rewards programs to encourage spending. This split also explains the recent rise ofissuing processors, which make it easier for neobanks and fintechs to issue cards to access a more lucrative end of the market.

Why are merchants willing to pay this fee?10The idea is that accepting card payments nets more customers and higher spending, due to convenience, consumer protections, and credit card rewards. More cards means more merchants, more merchants mean more cards, and more of everything is good for the network. In theory, the network benefits through fees, the merchants benefit through more purchases, and the consumer benefits through convenience.

---
config:
 theme: 'neutral'
 fontFamily: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
 nodeSpacing: 10
 rankSpacing: 100
 flowchart: 
 subGraphTitleMargin: {bottom: 20}
 diagramPadding: 10
 useMaxWidth: true
---
graph LR
 I[Issuers get more interchange] --> R["Issuers issue more cards and give more rewards"]
 R --> C
 C[People spend more on cards] --> M[More merchants accept cards]
 M --> I
 %% invisible connections to make it more round
 C ~~~ I
 R ~~~ M
 R ~~~ I
 R ~~~ C

The virtuous cycle of card spend.

In the EU,interchange fees are restricted to 0.3%, which explains the lack of rewards cards and wider acceptance of alternative payment methods like bank payments.

# 4. Set rules and handle disputes

Aside from incentivizing good behavior, card networks also need to regulate bad behavior on their networks. These rules are detailed in “Visa Core Rules and Visa Product and Service Rules”, a 923 page volume that ispublically available. This is a tome detailing things like appropriate use of the Visa brand mark, detailed interchange data requirements, transaction processing timelines requirements, requirements and procedures for specific Visa services, and features issuers/acquirers should support.

For issuers and acquirers, who interact with the network, violating these rules could affect interchange rates, incur non-compliance fines (anywhere from $25k to $1M per month), or risk suspension from the network.

For cardholders and merchants, who interact with each other, networks provide a mechanism for resolving disputes between them. This could mean a fraudulent transaction, the product was not as promised, or a number of other possible reasons detailed in the rules. This is the process that happens behind the scenes when you call your bank to report fraud or request a chargeback.

When a payment method doesn’t have a dedicated dispute mechanism, the legal system is used to settle disputes11. This a problem with cash or bank payments that cards don’t have.

## Arbitration

Visa is not actually involved directly in resolving most disputes. The rules essentially impose forced arbitration12. The issuer of the cardholder and acquirer of the merchant send evidence back and forth until one party yields and accepts liability for the transaction.

If both parties refuse to yield, then Visa reviews the dispute, charging a whopping $600 ($1000 for appeals) makes a decision based on the evidence provided (signature, security footage, receipts, etc) and the guidelines listed in the Visa Product and Service Rules.

The losing party pays the original transaction amount plus the review fee, so both parties have a lot of incentive to resolve it between themselves. Issuers often refund the cardholder themselves and write off the loss. Merchants proactively refund dissatisfied customers since they are charged a $15-30 processing fee by the acquirer upon receiving any dispute, even if they win.

Arbitration is not a fair system, but it is an efficient one.13

# Conclusion

I hope you have gained some appreciation for the important role of card networks and some reasons for why cards are as popular as they are today. Use this knowledge to topple the V/MC duopoly, design your own payment method, or think about while you spend your money.

1. Nowadays they may have product offerings for some of these, or own subsidiaries that do some of these, but these are not core to the business of being a card network.↩
2. Technically, these are “payment facilitators”. A bank underwites the payment company, and the payment company underwrites their merchants. The different roles in payments have historically been meaningful, but companies are increasingly blurring the lines, so these distinctions and terms are less interesting today.↩
3. To be precise, we use “card networks” to colloqially refer to the companies operating their own card payment networks / schemes. For example,VisaNetis technically the network, Visa is the company/brand. Mastercard’s network is calledBanknet. Both companies also own and operate specialized subsidiary networks for things like debit cards and ATMs, like Visa’s Interlink and Plus, or Mastercard’s Cirrus and Maestro, although technically VisaNet and Banknet can process debit (this is a story for another time). There are further terms to distinguish the telecommunications network with the bank network, and even subsets of each. Visa even thinks of itself as a“network of networks”. Turtles all the way down.↩
4. Orfour or more, depending on how you count.↩
5. Similar to IPv4, 16 digit PANs are rapidly exhausting due to the use of anonymized “token” PANs used by things like Apple/Google Pay and saved payment details.↩
6. Clearingincludes finalizing/committing the payment and reconciliation against the authorization. “Capturing a payment” is what this is called from the merchant’s perspective.↩
7. Known as a “voice authorization”. You might be able to get one today, although I don’t know if banks are staffing operators to field calls.↩
8. Althoughinterchangeis short forinterchange fee, technicallyinterchangerefers to the payment messages being routed by the card networks, and the fee is provided for that data. But, you almost never hearinterchangeused to mean payment messages except in technical specs.↩
9. Although this creates trust in card payments, it has opened the doors tofriendly fraud, where legitimate purchases are reported as fraudulent. Not to mention amoral hazard.↩
10. Some merchants add a surcharge on card transactions to pass through the fee to customers. This used to be against Visa’s rules (andCalifornia state law) but lawsuits have challenged that. The surcharge amount is alsoonly supposedto be the amount the merchant pays on a card transaction, but I suspect that many small merchants charge more.↩
11. There are someamusing casesof this at work in large transactions, where the legal fees are much more in proportion with the transaction costs.↩
12. Not that you asked, but the expansion of forced arbitration and confidential settlements are bad for society. Back in the day, you could sue your bank (for example) for doing bad stuff, but now contracts for everything include a clause for arbitration, waiving your rights as a consumer. The company pays for the arbitration, not you, so you can guess the outcome of that. Famously, Disney tried to use a forced arbitration clause in the Disney+ streaming agreement to prevent a wrongful death suit from a allergic reaction in a Disney restaurant. In the Visa case, the dispute process means the consumer tends to benefit, at the cost of the issuer and the merchant.↩
13. The system is designed toencourage transactions rather than stopping fraud. It opens the door to fraud, especially friendly fraud, as explained in another footnote. Friendly fraud isa growing problem.↩