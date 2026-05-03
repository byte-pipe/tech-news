---
title: Revolut Built a Foundation Model | Fintech Brainfood
url: https://www.fintechbrainfood.com/p/revolut-foundation-model
site_name: tldr
content_file: tldr-revolut-built-a-foundation-model-fintech-brainfood
fetched_at: '2026-05-03T19:54:56.813379'
original_url: https://www.fintechbrainfood.com/p/revolut-foundation-model
author: Simon Taylor
date: '2026-05-03'
description: Understand how Revolut's foundation model for money delivered MUCH better credit, fraud, and LTV performance than their baseline deep learning.
tags:
- tldr
---

* Home
* Posts
* 🤖 Revolut Built a Foundation Model for Money

# 🤖 Revolut Built a Foundation Model for Money

Plus; $16bn withdrawn from Aave in a "run on DeFi" after KelpDAO hack, and Plaid's annual letter.

Simon Taylor

Apr 26, 2026

Your browser does not support the audio element.

Welcome to Fintech Brainfood, the weekly deep dive into Fintech news, events, and analysis. You can subscribe by hitting the button below, and you can get in touch by hitting reply to the email (or subscribing then replying)

Subscribe

### Weekly Rant📣

🤖Revolut Built a Foundation Model for Money(And why it's worth billions to whichever bank builds the next one.)

Something big happened in financial services in the last twelve months and almost nobody clocked it. Companies started training their own foundation models for finance:

* RevolutpublishedPRAGMA— a foundation model trained on 24 billion banking events across 111 countries. Credit scoring up 130%. Fraud recall up 65%.
* NubankpublishednuFormer— a foundation model trained on 100+ billion transactions across 100M+ customers. It’s narrower than PRAGMA by use case, but more GPT-like as a model.
* Mastercardlaunched LTM — a foundation model trained on billions of card transactions to identify cyber risk.

And some others started fine-tuning existing models.

* NPCI(India's UPI operator) — fine-tuned Mistral 24B, for UPI Help, a conversational agent for 400M+ UPI users.
* PayPalpublished Nemo-4-PayPal — fine-tuned llama3.1-nemotron-nano-8B-v1. Their shopping assistant got 49% faster and 45% cheaper to run. Two weeks of fine-tuning.

Foundation models for finance are here.

The most important signal in Revolut’s PRAGMA work with NVIDIA isthesignificantimprovement (uplift) their model delivered vs their existing custom ML models, across multiple use cases.

It’s now the case that the two most credible, fastest-growing Neobanks in the western hemisphere, Revolut and Nubank, are betting that transformer architectures will drive their growth.

Clearly, a custom finance foundation model will be a massive competitive advantage in the coming decade.

The IP of banking was always how they priced and managed risks, the squishy lending decisions, the fraud stuff, and the optimization of every interaction. If transformers deliver benefits in production on the scale Revolut is suggesting, they're a game changer.

I've been asking for years —where are the foundation models for finance?Healthcare was doing this with DNA sequences. Ad-tech was doing it with clickstreams. Finance, the most data-rich industry on earth, was still stuck training bespoke ML models on hand-crafted features. PRAGMA is the first real answer that cuts acrossmultipleuse cases.

### What is a Foundation Model for Money?

Revolut took theirmassive data setand looked atcustomer events(logins, screen taps, payments)over time.

* 26 million customers
* 24 billion customer events
* 207 billion tokens created

This is NOT a large language model. It's not generating text or images. It's not competing with Claude or ChatGPT. Customer event data has a structure that text tokenization destroys. Numbers and scale become fragmented.

To prove the model worked, Revolut ran three experiments. Pavel walked me through them.

* Experiment 1: Use the pre-trained “embeddings” on an old model.Answers one question:how much information is already in the pre-trained embedding, before you've even told it what task you're solving?
* Experiment 2:Use pre-trained embeddingsalongsidethe hand-crafted ML features the data science team had spent years building. This answers:what new information does the foundation model capture that the old features missed?
* Experiment 3: Fine-tune the foundation model on finance outcomes using LoRA.This answerscan we beat the entire data science team by taking a pre-trained model and pressing a button?
❝

can we beat the entire data science team by taking a pre-trained [foundation] model and pressing a button?

Pavel Nesterov

In most cases, the answer is yes.

The PRAGMA model took six production tasks, and replaced six separate custom machine learning (ML) models with one.

### Revolut’s Paper Shows STAGGERING Potential

Thepaperis the first time I've seen published evidence on the effectiveness of a foundation model for banking’s most important competitive levers. Revolut published the uplift this model producedvs their existing ML models:

* Credit scoring: +130% PR-AUC uplift vs ML models (how well it catches rare cases that matter)
* Fraud recall: +65% uplift vs ML models (how much true fraud is caught above old ML model)
* Marketing engagement: +79% & product recommendation: +40% uplift vs ML models

Revolut’s final uplift of the PRAGMA vs production Deep Learning models

Each of these is a competitive lever:

1. Credit risk pricing isthecompetitive lever for banks

Credit scoring lets banks price and issue loans. Loans are the profit center of banks. Lending is a product that never has a demand problem. People will always take the money, the harder question iswill they pay back, and if they do,what can I should them as a %so that they’relikely to take the loan from me, not someone else who’s cheaper.Today, that involves looking attheir datacompared toother customers' dataovertime.

→ A model that can find more customers who are likely to pay back, can price more aggressively, and the bank sells more loans, which means morerevenue.

(Assuming regulators don’t tie themselves in knots over “explainability,” this is the area of opportunity. FWIW, I think we need a shared responsibility framework for AI, as we have for cloud, and we’ll be building V1 atFintech Nerdconthis year.)

2. Fraud recall is a competitive lever for anyone in payments.

Fraud recall detects the % of true fraud events detected out ofallof the fraud events that occurred. If you’re detecting more of the actual fraud, you’re also not falsely blocking good payments. Banks and fintech companies make money from card transactions (interchange), but are often liable for refunding fraud. So

→ A model that catches more real fraudsaves cost, and allowing more good transactions through generatesrevenue.

3. Marketing is how banks get new customers or cross-sell products.

The “attach rate” of customers is a really important metric that Neobanks like Revolut and Nubank have been excellent at. Whereas a large bank will have more than 60% of its customer base just using a single product. That’s a lost opportunity for revenue.

→ If customers are engaging more with marketing, their propensity to take the product being recommended increases. If they do take that product, the bank gets morerevenue. Yay.

Notably, it had a seventh area where it did not succeed.

PRAGMA performed 47% worse than Revolut's production system on anti-money laundering. This was not a surprise. Pavel told me the team expected to fail. AML is a network problem — what matters is who you transact with, not what you do. PRAGMA reads each user's history in isolation. It can't see the chain. They published the failure because it's a finding, and because they already know what to build next.

(Although I imagine if you trained a model on that network transaction data instead of individual customer events, it would be net far more effective. The issue was the training data set, not the model type.

Building a customer model created six areas of competitive advantage. For a bank that already has 70M customers and is one of the fastest growing in the world.

For Revolut, this kind of research compounds their advantage in tech.

### The Prize is More Revenue and Lower Costs

Not a shocking business case. The magnitude, however, is.

Napkin math o’clock.

Credit (Based on JPMorgan Chase earnings data).JPM has credit costs of over $10 billion a year, dominated by Card Services. Net charge-offs ~$2 billion per quarter in consumer, running $8bn+ annualised. Revolut's credit scoring improvement was +130% PR-AUC. That's not an 130% reduction in losses — nothing works like that in production. But even at 10% of the stated gain applied to JPM's card book?

That's hundreds of millions of dollars a year. Every year. Compounding as the model improves.

Fraud losses can be millions per quarter.For every $1 lost in fraud, another $5.75 lost in operational costs. So that balloons to tens of millions. Revolut's fraudrecallwent up 65% — meaning they caught roughly 1.65x as much fraud as their prior production system.

A large card issuer catching even a fraction more fraud pays for the GPU bill a thousand times over.

Foundation models do all the things a consulting strategy deck will tell you to do.

So you can skip that part and go straight to figuring out execution.

But why can’t every bank do this?

### What Revolut built is 2020-era LLM. What comes next is wild.

Today PRAGMA predicts. That's it. Given a customer's history, it predicts who's a credit risk, who's committing fraud, and who's about to churn and a customers’s lifetime value. Which is useful by all means but boring compared to what's coming.

Pavel gave me the analogy of where LLMs were in 2020. Back thenBERTcould read a sentence and fill in the missing word. Useful for search, classification, and ranking. But it wasn’t until GPT came along and couldgeneratethe next sentence that things really began to change.

PRAGMA today is like BERT was in 2020. It reads a customer's history and fills in the gaps.

A generative version would write the next chapter. If you can generate a customer's future events, you can simulate when they'll buy a new product. And then rewind the tape to see the things that led to that decision, and try to make those things happen.

Low-key Minority Report, for banking.

That doesn’t exist yet, but that’s the goal.

### Why haven't banks done this?

Do not underestimate banks AI capabilities insome areas.

Banks have been doing machine learning for decades. Every major bank has capable AI talent in lending, underwriting, and AML — people who've forgotten more about credit modeling than most Silicon Valley ML engineers will ever learn. Their data sets are enormous and compounded over decades of experience.

So why did a neobank ship this first?

1. Capability, and the ability move quickly.

Revolut is the canonical move-fast-and-occasionally-break-a-thing Fintech company, that famously took a little while to get its full UK bank license because of regulator concerns over audit gaps and compliance staff turnover. They will move quickly.

And the entire tech stack is modern, regularly replaced, and ideal for this kind of experimentation. A bank could take months just to find and scrub the data they need for this training. Revolut likely had it. Ready to go.

2. The availability of open-weight base models.

Open-weight models like Qwen, Kimi and GLM are now incredibly capable, cheap and with a couple of weeks of rentable GPUs can be trained to run a foundation model on private data sets.

That conversation may be happening in large institutions, but the execution pace isn’t in the same universe. But I don’t think that means they’ll stay absent. When it's a company's IP, they're actually good at this stuff.

The fact that Mastercard built a foundation model is a big tell for me.

Foundation models for finance aren't a research problem anymore. They're an execution problem. The base models are open-weight. The frameworks are public. The papers are on arXiv. The compute is rentable. Banks can now do this.

Banks have never lacked talent or resources; they just often get McKonsultant’d and PowerPoint-slided to death. The banks that train their own foundation models will be the ones who ignore that guff, and get their data and risk talent working hands-on with folks like NVIDIA.

And Pahal Patangia runs payments business development at Nvidia. Where did he come from?FICO. The person who spent a decade helping retail banks build credit models is now the person helping Nvidia sell them the thing that replaces credit models.

That's not a coincidence.

### NVIDIA’s Enterprise Finance Pitch

You think NVIDIA, you think chips, Jensen’s leather jacket, and a stock price that’s propping up the S&P 500

Almost nobody outside the people already working with them knows what they do in financial services.

For Revolut, NVIDIA built the factory that lets a bank turn its proprietary data into a proprietary foundation model. It supports rolling your own foundation model or fine-tuning.

1. Foundation Model Building (Revolut, Mastercard):NVIDIA provides the silicon (H100s, Blackwell), the data libraries (cuDF for the GPU-accelerated feature engineering that used to take weeks), and a training framework (NeMo AutoModel) that handles the parallelism so the ML team doesn't have to. PRAGMA's 1B model trained on 32 H100s in roughly two weeks.
2. Fine Tuning a Model (PayPal):NVIDIA provides thebase model itself— Nemotron. Plus the framework to do the fine-tuning (NeMo), plus the inference runtime to serve it cheaply (TensorRT-LLM).

Pahal Patangia made the point on a recent Tokenized podcast episode — and I keep coming back to it — that training is a one-time cost. Inference is forever.

A bank running fraud on every transaction, credit on every application, personalization on every session, is paying the inference bill billions of times a day. NVIDIA's whole recent model family has been re-tuned around that second number. Smaller models trained on more data, so they punch above their weight when you fine-tune them.

So they’ll help you train at low cost, because they want your inference workloads.

Sort of like how GLP-1s give you something you want (better body shape) in return for a subscription fee to the medication.

And before I turn this into an NVIDIA sales pitch, there are plenty of alternative companies competing here. Google TPUs, AWS Trainium on Bedrock, and AMD are all building out their offerings here.

In fact, the raw inference space is becomingso competitive, there’s a growing view in Silicon Valley that NVIDIA’s moat is falling to more specialized silicon.So much so that the CEO of NVIDIA, Jensen Huang, went on the Dwarkesh podcast to lay out his counterargument(and accidentally spawned a hilarious set of memes about cars).

— #(#)

### It’s not just the models

A foundation model is nice.

But there’s actually 3 layers of AI competitive advantage, the model is just one of them.

1. Talent. In one room. With one architecture.
2. The Data. Big banks have plenty.
3. The Model. What we’ve discussed today.
4. The workflow around the model is another.

The Fintech Brainfood: Four Layers of AI Competitive Advantage

Look at what PayPal did. They didn't just fine-tune Nemotron and ship it. They built a multi-agent system around it. Agents handle reasoning, checkout, fraud. The fine-tuned model is one component in a larger agentic workflow that, combined,is the product.

* The model gets better the more data you put through it.
* The workflow gets better the more customer interactions you observe. T
* The data gets richer the more products you cross-sell.

Each layer compounds the one below it.

Agentic workflows as intellectual property. Anyone with data and a computer can train a model. But the workflow — the orchestration, the tool routing, the evaluation harnesses, the guardrails, the specific prompts that encode your product's opinion aboutwhat good looks like— that's harder to copy.

That's where competitive advantage starts to move to, once everyone has a foundation model.

An aside: One more thing that held in Revolut's research: scaling laws work on events. More parameters, better performance. The same pattern that drives LLM progress applies to banking event data. The 10M-parameter model is good. The 1B-parameter model is better. The frontier keeps moving.

### So what do you do to compete?

I think there are three options emerging.

1. Build your own custom model like Revolut did.This requires a massive dataset and, more importantly, the ability touse it for training.
2. Collaborate with other industry actors to build a model.This could be with your core processor, industry consortia or vendors. Sardine has 6 billion user device profiles and event data. FICO has more lending data than anyone I can think of.
3. Buy a model from a company with a large data set.Vendors exist in risk and credit who havepretty large datasets themselves. It’s a matter of time until these companies have foundation models you could just buy.

Your decision comes down to where you see your competitive advantage, and your honest assessment of your ability to execute.

Neobanks and digital-only banks are now in an arms race to build their own models.

The big banks have to figure out if they compete or if any of their bigger suppliers can help them compete.

A mid-sized or smaller bank with a smaller customer base probably shouldn’t be banging on NVIDIA’s door to custom-train a model on their batch file outputs. But a group of smaller banks with pooled data and resources could do something very interesting.

### Banks are not disrupted. But AI is disruptive.

Banks are not disrupted. I still believe that.

The moats around regulation, lending, and balance sheet are real, and they aren't going anywhere. But the banks that win the next decade aren't the ones with the biggest balance sheets. They're the ones that upgrade their IP. The moat stays the same. The winners inside the moat change.

The IP of banking was always how they price and manage risks. The squishy lending decisions. The fraud stuff. For 200 years that IP lived in spreadsheets and in the heads of underwriters. Revolut just moved it into a model. And the model is only phase one of four.

The only thing between you and a PRAGMA of your own is deciding which of the three paths is yours. Build. Collaborate. Buy.

Pick one. Start now.

ST.

* Much of the PRAGMA detail in this Rant came from a conversation with Pavel Nesterov, one of the paper's authors. Any errors are mine.I also spoke to Pahal from NVIDIA on the Tokenized Podcastand it was an absolute BANGER episode. You should reallycheck it out.

### 4 Fintech Companies💸

1.Monk- The Accounts Receivable AI

Monk helps companies get paid faster by ensuring invoices always go out on time, complex contracts are correctly billed and chases customers for you. Users can upload customer contracts to the platform to create invoices, the agents will then chase customers and claim 24% better response rate than human agents.

🧠Accounts Payable is now well understood. Companies like Ramp, Brex and others have crushed this use case, but getting paid is still a bit of a nightmare. What I really like about Monk is their focus on the edge cases like a missing W9, or having to get setup as a vendor on AWFUL portals like Ariba or or Coupa. An agent that canjust do thatis a life saver for anyone who needs to get paid.

2.Safety Kit- Preventing on platform scams and abuse

Safety Kit ingests all logs and user events for online platforms, and identifies known scam email clusters, fraud rings, re-used data elements, and helps eliminate harmful users at onboarding, posts in chat, marketplace listings, or harassment in livestreams.

🧠”Harm” is a broader category than financial fraud but its often closely related.I love that they’re just taking all platform data and identifying bad actors on that platform. This is an issue that’s gotten MUCH worse with the rise of AI and we need tools to fight back.

3.Wealth Architect- The AI Financial Planner

Wealth Architect helps customers build financial plans by describing their dreams in natural language (e.g. Help me buy a house by 2028). It then provides detailed plans and goals to help achieve that outcome (e.g. save an extra $225/mo into your house pot). The plan can then evolve over time as events happen in your life. Behind the scenes it cleanses your transaction data and helps you continue to optimize your outcomes.

🧠What’s neat is that they’ve built multiple agents for tax-aware planning, or Monte Carlo stress testing.It’s going quite a bit beyond a PFM in that sense (although it has that under the hood). My only worry is, will users know how to engage? The first use and attach rate here will be really crucial. How great is that first experience? I’d love to try it.

4.Lorum- Correspondent banking via API

Lorum is a multi-currency clearing, settlement and treasury platform delivered via a single API. It replaces the correspondent banking chain for regulated platforms like payroll companies, PSPs and fintechs who need to hold and move client money across 30+ markets. They’re 100% reserved custody with no lending book. They've filed for a US national trust bank charter with the OCC.

🧠The founders argue that correspondent banks want to slow money down so they can collect float to lend.The OCC trust charter filing is the interesting bit. If granted, direct access to USD clearing without becoming a lending bank is a genuine moat. I can imagine every stablecoin issuer and infrastructure company wouldlovea genuine alternative to the GSIBs here. It’s going to take time to build scale and liquidity, but it’s a fascinating company to watch.

### Things to know👀

1.$15 Billion withdrawn from Aave DeFi Vaults after KelpDAO exploit.

On April 18, Aave users withdrew $15.1 billion in deposits in just 3.5 days, after an exploit on KelpDAO allowed attackers to mint roughly 116,500 rsETH tokens ($239m) without any real ETH backing. Aave initially identified these tokens as valid, allowing the attacker to borrow roughly $200m leaving Aave lenders with substantial losses. Total deposits fell from $48.5 billion to $30.7 billion, wiping out roughly a third of the platform’s capital almost overnight.

Attackers minted ~116,500 rsETH ($239m) with no ETH backing by exploiting the LayerZero bridge (sending it a false message). The hack is attributed to Lazarus Group, North Korea's state-backed hacking unit, which has made crypto exploits a core sanctions-evasion revenue stream.

🧠A bank run in DeFi or Aave? Capital has not left DeFi. It left Aave.

* SparkLend's TVL climbed from $1.9B to $3.2B after banning rsETH months ago.
* AAVE token dropped ~15-20%. Like bank shares during a run.

🧠This is the second time a "bridge" has been exploited this year.

* Bridges help you move between (e.g. Solana and Ethereum).
* Attackers submitted a fraudulent LayerZero message and tricked the contract into releasing real rsETH on one chain with no corresponding burn on the source.

🧠Aave read the rsETH as real.

* When attackers posted fake rsETH to Aave and borrowed REAL Eth and stablecoins, they walked.
* It took hours for anyone to realise the loan would never be repaid.
* Aave can patch this, trust can return. But how long will it take?

🧠Unlike a traditional bank run, Aave's solvency is not in question.

* Loans are over-collateralised.
* The question is reliability.
* If the protocol believed fake tokens once, would it again?

🧠Will institutions lose trust in DeFi?

* BlackRockput BUIDL live onUniswap.
* Société Généraleruns its MiCA stablecoins throughMorphovaults.
* Franklin Templetonis a launch partner on Aave Horizon.
* But it's not like banks have never had runs is it...

🧠Retail fintech wraps the same plumbing.

* Kraken'sDeFi Earn routes users intoMorphovaults.
* Coinbasehas originated $1.2B in USDC loans viaMorpho.
* The curator vault is quietly the consumer fintech yield product.
* Will Neobanks think twice or will this be patched quickly?

🧠None of those names held rsETH.

* They're exposed to the same bridge, oracle and verifier assumptions underneath the whole stack.
* But they're all also scrambling to fix as much as possible.
* Because lurking on the horizon is Claude Mythos.

🧠Wildcard: Anthropic shipped Claude Mythos Preview two weeks ago, an AI that finds zero-days in hours that took humans years. Lazarus exploited Kelp with conventional tradecraft. What happens when the better tools get cheaper?

🧠I think DeFi will be fine, Aave will recover, the system will come out stronger.

* But the hyper connectivity of liquidity, bridges between chains, proliferation of collateral and staking tokens that make DeFi so attractive, also are a weakness.
* There's value in being patient. Starting with battle tested tokens. And not going too far out on the risk curve.

2.Plaid posted $500M ARR, 40% growth, and profitability.

Plaid says its annual revenue surpassed $500m ARR, up 40% YoY, with revenue from new products now accounting for 21% of all revenue, and growing 92% YoY. Lendscore, the alternative credit data score from Plaid, claims a 25% uplift in performance over traditional credit data alone. The Plaid network is also a useful anti-fraud signal. In early 2026, Plaid saw an 80% spike in “builder” new customers who signed up to access their account data, often using AI tools like Claude Code or Replit.

🧠Plaid has steadied the ship.The DoJ breakup of Plaid and Visa, and Fintech winter were not kind to Plaid with a big down round from around $19bn to $6.1bn. Their latest valuation at $8.1bn is a testament to a company still growing and compounding with its new products.

🧠Lending in particular is a bright spot.Cashflow underwriting is now a default in the US market in a way it isn’t in Europe or elsewhere. Plaid can reasonably take credit for helping invent and own a category that has created financial inclusion and better lending outcomes.

🧠Can they break out and aim higher?Plaid is a B+ company as it stands, but with AI as a major tailwind, there’s a chance they can break out from that. For a sense of scale. Stripe Billing now does 2x more revenue than all of Plaid.

🧠Plaid partnered with Perplexity and Replit.Helping the power users and vibe coders work with their own account data. What the nerds are doing at the weekend will be what we all do in 10 years. Secure, permissioned finance data could drive the personal CFO and tax accountant we all desperately want. It’s logical that someone should build it on Plaid. But will they?

### Good Reads📚

1.Dorsey Mode - Tech’s Most Misunderstood CEO

This educated guess piece argues Jack, far from being a cynical cost cutting CEO, is the only one honest enough to understand the app paradigm is dying and that we need more resilient, less centralized services over time. He’s made some mistakes, arguably, Tidal (wtf), over paying for AfterPay, turning his head into a Block. But now he’s righting the ship. Block arguably had too many people, companies probably should be 2-3 layers deep.

🧠The temptation was to see the 40% cut as another CEO AI washing.But I don’t think it is. It’s the start of a new normal. And perhaps a more focussed Jack.

— #(#)

— #(#)

### That's all, folks.👋

Remember, if you're enjoying this content, please do tell all your fintech friends to check it out and hit the subscribe button :)

Want more? I also run theTokenized podcastandnewsletter.

(1) All content and views expressed here are the authors' personal opinions and do not reflect the views of any of their employers or employees.

(2) All companies or assets mentioned by the author in which the author has a personal and/or financial interest are denoted with a*.None of the above constitutes investment advice, and you should seek independent advice before making any investment decisions.

(3) Any companies mentioned are top of mind and used for illustrative purposes only.

(4) A team of researchers has not rigorously fact-checked this. Please don't take it as gospel—strong opinions weakly held

(5) Citations may be missing, and I’ve done my best to cite, but I will always aim to update and correct the live version where possible. If I cited you and got the referencing wrong, please reach out

### Keep Reading

View more
caret-right

# Fintech Brainfood

Food for thought about Finance, AI and the future of money.

Subscribe

###### Home

Posts