---
title: AI Risk Is an Architecture Problem - by Eric Glover
url: https://appliedingenuity.substack.com/p/ai-risk-is-an-architecture-problem
site_name: tldr
content_file: tldr-ai-risk-is-an-architecture-problem-by-eric-glover
fetched_at: '2026-05-29T04:36:10.456740'
original_url: https://appliedingenuity.substack.com/p/ai-risk-is-an-architecture-problem
author: Eric Glover
date: '2026-05-29'
description: How to see, name, and bound the business risks of AI-based systems. Part 1 of a series.
tags:
- tldr
---

# AI Risk Is an Architecture Problem

### How to see, name, and bound the business risks of AI-based systems. Part 1 of a series.

Eric Glover
May 26, 2026
3
1
1
Share

### Section 1: Why AI Risk Conversations Stall

Three kinds of companies come to me for help with AI. While they are all in different places on their AI-path, they all have the same underlying challenge: how to effectively understand and manage business risk for systems that contain AI-based components.

The first kind of company is on the outside looking in. Maybe they’re a newer company, maybe an established one running on technology that’s a decade behind, but either way the story is the same: their competitors and peers are talking about AI, sometimes shipping with AI, and the gap is starting to feel existential. They don’t want to be the company that failed because they moved too slowly. They want to adopt, but they don’t know where to start, and the cost of starting in the wrong place feels insurmountable.

The other two kinds of companies are already on the inside, with different problems. One built a working proof of concept, raised money or won internal buy-in on the strength of the POC, and is now trying to turn the demo into a production system, and the walls they’re hitting are not the ones they expected. The other already crossed that bridge, shipped something real, and got burned: a hallucinated answer reached a customer, a document ended up somewhere it shouldn’t have, an automated workflow did something expensive that nobody caught for weeks. Aftermy earlier post [The “LLM-as-Analyst” Trap: A Technical Deep-Dive into Agentic Data Systems] on agentic data systems, several readers reached out to say some version ofthat’s the thing that happened to us, and now we finally have words for it.They knew something was not right, and they didn’t have a vocabulary forwhat.

None of these companies can see their actual business risk surface clearly enough to make decisions about it. When a customer’s lawyer says that they were told a food item doesn’t contain peanuts when it does, a natural response is to map the business risk directly to the actual AI component that generated that output. This could look like an angry executive demanding the AI engineer “fix it now”. This instinctive response is very dangerous and demonstrates the difficulty business professionals have mapping business risk. If the engineer were to modify the prompt to fix the instance of this problem, it is unlikely to actually solve or even positively affect the true business risk, which is the fact that a probabilistic AI is able to directly generate output to the user.

To receive new posts and support our work, consider becoming a free or paid subscriber.

Subscribe

Section 2: Layers of Risk

When people in a company talk about “AI risk,” they’re usually talking about two different things at once. Executives are thinking aboutwhat could happen to the business: Bad press, a regulator’s letter, a lawsuit, a bad commitment the company is now bound to, a system outage that costs real money, etc… These are the things that show up on a risk register, get talked about in board meetings, and ultimately determine whether a project gets funded or killed.

Engineers and architects are thinking aboutwhat could happen inside the system, often within a single component: The model could leak data, the model could say something wrong, the model could do something unintended, etc... These are the things that show up in design reviews, post-mortems, and JIRA tasks.

Both groups are talking about real risks. But the executive’s vocabulary doesn’t tell the engineer what to fix, and the engineer’s vocabulary doesn’t tell the executive what to worry about. So the conversation either gets stuck on definitions, or it skips definitions entirely and lands on something vague like “we need guardrails.” Guardrails for what, exactly? Against what, exactly? If we implement guardrails, will we eliminate the risk or problem, or fix just this one instance?

#### The cause layer: AI mechanism risks

Figure 1: The three AI mechanism risks. Every AI integration can fail in three ways: through what it sees (data), what it says (output), and what it does (action).

The three categories of AI Mechanism risk aredata,output, andaction: what the AI sees, what it says, and what it does. The rest of this post explains how to use it, how it connects to the business consequences that actually get reported up to leadership, why it’s the same model regardless of which AI you’re using or who built it, and where it fits relative to the more comprehensive frameworks you may have already encountered: NIST, the EU AI Act, OWASP, and others.

Data riskis about exposure of information that shouldn’t have been exposed.Output riskis about assertions that shouldn’t have been made.Action riskis about consequences that shouldn’t have been triggered. Each one has its own characteristic failure mode, its own typical fixes, and its own way of compounding when combined with the others.

This is also the observation Simon Willison made in his“lethal trifecta”framing: the most dangerous AI failures are usually combinations of all three. Private data in context, influenced by untrusted content, with the ability to exfiltrate or take action. The trifecta is the canonical example of what happens when all three categories coexist in one system without isolation between them.

#### The consequence layer: business risks

Separate from the AI mechanism risks, we can map business risks into five distinct categories of harm a business can actually suffer when something goes wrong. These are the things that get measured, reported, and acted on by people who don’t write code.

Figure 2: The five categories of business risk:brand risk, compliance risk, liability, operational risk,andcommercial risk. These are the consequences a business actually cares about, the harms an AI failure ultimately translates into.

These five are the kinds of damage that an executive recognizes immediately, because they’re the same categories of damage a business can suffer from anything: a software bug, a bad hire, a supply chain disruption, a PR mistake. AI is not introducing a new category of business harm. It is, however, introducing new and unfamiliarpathsto harms the business already knew about. Note that I use “brand risk” broadly to include any customer impressions of their experience.

#### Connecting the layers through examples

The two layers aren’t independent. Every mechanism risk maps onto one or more possible business risks, if not addressed.Table 1 lists a few representative scenarios, not an exhaustive map. In practice, most real failures touch more than one business risk, and almost any failure can escalate to liability if the harm is severe enough:

Table 1: Representative AI failures and the business consequences that can follow when unmitigated.

The right-hand column shows the business consequences that would follow if nothing in the system catches or contains the failure, which is the question the framework exists to answer: given an AI mechanism failure, what could the business actually suffer? Whether those consequences are realized depends on the architecture around the AI, which is the subject of Section 3. Reducing, but not eliminating, the error-rate of a single component does not change the business risk space, but modifying the architecture could.

Two things are worth pointing out about this table.

First, the same underlying error compounds dramatically when autonomy is added. Rows 4 and 6 are the same error, an OCR misread, but in row 4 it’s an accounting mistake a human could eventually catch, avoiding actual business losses, and in row 6 it’s a wire transfer that already happened, an actual business loss. The error didn’t change. The system components (human-in-the-loop) between the error and the world did. This is the core reason agentic systems require different architectural caution than non-agentic ones: adding broad action capabilities can significantly magnify the business risks associated with output errors.

Second, some rows have multiple risks from a single AI error. This is why “what risk category does this fall into?” is almost never the right first question. The right place to start from is:what mechanism could fail, and what set of business consequences would follow? How might these risks be acceptably mitigated?

### Section 3: Risks Are Properties of Systems, Not Components

Look at rows 4 and 6 again. The first row is an accounting headache. The second row is a wire transfer that already happened. The difference between anexpensive lessonand anoperational disasteris not the AI. It’s everything around the AI.

This is the central architectural point of the entire framework:risk is a property of the system, not just the components.

Two products can use the same model, with the same failure rate, hitting the same kinds of errors, and have wildly different risk profiles. The product with a human review step before any commitment is made carries Output risk but contained Action Risk. The one with full automation carries a much greater Action Risk, with no checkpoint between failure and consequence. The model didn’t change. The architecture around it did.

This matters because most of the AI-risk conversation focuses on the wrong things. Companies spend enormous energy on component-level optimizations: choosing between models, prompting them more carefully, fine-tuning them on internal data, adding guardrails to their outputs via probabilistic rules or systems, etc… All of this helps, on the margin, but none of it is the dominant factor. The dominant factor iswhat the AI is allowed to see, what its output flows into, and what it’s permitted to do without any checking. Those are architecture questions, not model questions.

This also reframes how to think about external factors that AI risk literature spends a lot of time on: training data quality, supply chain integrity, model provenance, the possibility that a model was built or fine-tuned by an adversary. These factors matter, but not in the way most discussions treat them. They affect theprobabilityandseverityof failures within the three mechanism categories. They don’t create new categories. A model trained on poisoned data still fails through data, output, or action; so does a model from a foreign adversary or a pristine in-house model from scratch.

This is why the right question, almost always, is not“how do we make the model more trustworthy?”but“how do we build a system that’s safe enough even when the model isn’t?”That’s an architecture problem, and architecture problems have engineering answers. Bounded capabilities. Verification steps. Reversibility. Human checkpoints at the right places. Closed tool sets instead of arbitrary access.

### Section 4: Where This Framework Fits, Related Work

Before moving into each mechanism category in detail, it’s worth situating this framework relative to others you may have encountered. AI risk is not unmapped territory, and a serious reader will have already run into at least one of the major frameworks below.

The NIST AI Risk Management Framework(released by the U.S. National Institute of Standards and Technology in early 2023) is the establishment standard. It organizes AI risk bywho is harmed(people, organizations, and the broader ecosystem) and prescribes four functions that should run continuously across an AI system’s lifecycle: Govern, Map, Measure, and Manage. NIST AI RMF is authoritative, comprehensive, and widely cited. It is also a governance meta-framework: it tells a Chief Risk Officer how to organize a program. It does not tell an architect, looking at a specific integration, what to look at first.

The EU AI Act(Regulation 2024/1689, in force since August 2024 and rolling into full effect through 2027) is the regulatory standard. It classifies entire AI systems into four tiers (unacceptable, high, limited, and minimal) based largely on use case category: biometric identification, employment decisions, credit scoring, critical infrastructure, and so on. For organizations doing business in the EU, classification is mandatory and the penalties are real. But the Act is compliance scoping, not architecture: two systems built very differently can land in the same tier, and tier alone tells you almost nothing about where the actual failure modes live in your particular implementation.

The OWASP Top 10 for LLM Applications(most recently updated for 2025, with a companion Top 10 for Agentic AI released later the same year) is the closest neighbor to what most builders actually need. It enumerates concrete vulnerabilities: prompt injection, sensitive information disclosure, insecure output handling, excessive agency, misinformation, and others. The 2025 edition notably split misinformation out from excessive agency, a distinction that maps directly onto the output/action separation in this framework. OWASP is concrete, security-team-friendly, and practical. But it is a vulnerability catalog written for people who already think like security engineers, and using it well requires that framing as a starting point.

The MIT AI Risk Repositoryand the broader academic literature on AI risk taxonomies are comprehensive and rigorous, and almost completely unusable in a Tuesday meeting. They are what you cite when you want to demonstrate seriousness, not what you reach for when you need to make a call.

The data/output/action lens, paired with the five business risk categories, is a translation layer between these two ways of thinking.

### Section 5: The Three Mechanism Categories in Depth

Each of the three mechanism risks has its own characteristic failure mode, its own typical fix, and its own way of compounding when combined with the others. This section covers each one in the same structure: what it is, a concrete example, where it shows up in existing frameworks, and the diagnostic questions to ask about your own system.

For all of these explanations, we’ll use an example of a purchase-order extraction pipeline: customers email PDFs of purchase orders, an LLM extracts the relevant fields (buyer, account number, line items, pricing, totals), and the system creates database records.

#### 5a. Data Risk: what the AI sees

What it is.Data risk is the exposure of information that shouldn’t have been exposed, to a place it shouldn’t have been exposed to. This includes the obvious case (sensitive data sent to a third-party model provider that stores or trains on it), but also less obvious cases: data leaking between tenants, data ending up in logs that shouldn’t have it, data persisting in caches that have weaker access controls than the source system, or data being included in a context window where another user can later see it. If real data is used to train a model, it becomes theoretically possible that use of this new model might leak that data, resulting in an exposure risk.

The category covers both directexfiltration(data leaving where it should stay) andcontamination(one user’s data ending up in another user’s context). Both are failures of the same underlying property: the system did not keep data within its intended boundary.

PO-extraction example.When the system sends the entire PDF to a frontier model for extraction, the customer’s account number, addresses, pricing terms, and any incidental information on the page (a contact’s email, a signature, an attached form with sensitive details) all cross the boundary into a third party’s infrastructure. The third party’s retention policy is in their terms of service, not your contract with your customer. If the PDF happens to contain regulated data, PHI, financial data, an SSN on an attached form, you may have just created a compliance exposure. Your business is on the hook for what the third party does (or does not do i.e. encrypt, secure, delete) with that data.

Where it shows up in existing frameworks.OWASP catalogs this as “Sensitive Information Disclosure”; NIST AI RMF treats it as harm-to-organization, and harm-to-people when personal data is involved.

Diagnostic questions.

* What data crosses a trust boundary in this integration, and where exactly does each boundary sit?
* Whose data is it, and what did they consent to when they gave it to you?
* What happens to the data during your processing, i.e. after the AI call returns: logged, cached, retained, used for training, fed back into another system?
* If tomorrow, a regulator asked for a complete data flow diagram of this integration, could you produce one? Would it include 3rd party systems, logs, backups?

#### 5b. Output Risk: what the AI says

What it is.Output risk is wrong, misleading, or harmful assertions made by a model. This includes hallucinations, confidently incorrect “facts”, biased or off-brand language, leaked system prompts, and structurally-valid output (valid JSON, valid SQL, valid-looking summaries) whose contents do not match reality.

The danger of output risk is less about obvious wrong answers that everyone catches; it’splausiblewrong answers that nobody questions. A model that confidently misreads a number, invents a plausible-looking policy citation, or summarizes a document in a way that subtly distorts the original is much harder to detect than one that returns obvious garbage. Validity of structure is not validity of content. Modern models are trained to be helpful, i.e. thehelpfulness paradox, where giving an incorrect answer confidently may be favored to letting down the user by not being able to help.

PO-extraction example:The model extracts the order, but misreads “$1,250” as “$12,500.” The JSON it returns could be well-formed, all the field names could be correct, and all the types may match the schema. From the system’s perspective, the extraction succeeded. From the business’s perspective, the wrong number is now in the system, waiting to be acted on by someone (or something) downstream. The peanut-allergy scenario from Table 1 lives in this same category: the customer never sees the model, they see your brand asserting a fact that the model invented, and happens to be factually incorrect.

Where it shows up in existing frameworks.OWASP separates this into “Misinformation” (formerly “Overreliance” in earlier editions, renamed in 2025 to emphasize the model’s role rather than the user’s) and “Insecure Output Handling.” NIST treats output risk as harm-to-people when the output reaches users, and harm-to-organization when it reaches internal systems that act on it.

Diagnostic questions.

* Who or what are all of the consumers of this output, and do they treat it as authoritative?
* What does a wrong-but-confident answer cost, in dollars, in trust, or in liability?
* What architectural processes are in place to minimize the chance that bad model output results in irreversible downstream actions?
* If the model hallucinated the worst possible answer to this prompt, who would notice, and when, what are the consequences?

The fourth question is the one that separates output-risk problems from output-riskdisasters. If the answer is “the customer notices, on the phone with their lawyer,” the architecture may need some work.

#### 5c. Action Risk: what the AI does

What it is.Action risk is unintended consequences from things the AI causes to happen in the world: Sends emails, writes to databases, calls APIs, spends money, deploys infrastructure, modifies files, issues refunds, reserves inventory, etc... this is the fastest-growing category as agentic systems proliferate, because every new tool an AI can call expands the set of things it can do without human intervention.

The defining feature of action risk is that the consequences are usuallyirreversible, or expensive to reverse.

PO-extraction example.Now imagine the PO pipeline is “fully automated”: the system not only extracts the data but creates the database record, reserves the inventory, schedules the shipment, and emails the supplier a confirmation, all without human review. The same OCR misread from earlier ($12,500 instead of $1,250) is no longer a record-correction task. It is an inventory reservation, a supplier expecting payment, and a downstream commitment that may already have triggered other actions.

Where it shows up in existing frameworks.OWASP’s “Excessive Agency” was the original home for this category in the 2023 edition. In late 2025, OWASP released a separate Top 10 for Agentic AI specifically because action risk had grown into its own discipline. NIST treats action risk across all three harm categories (people, organizations, ecosystems) depending on what the action touches.

Diagnostic questions.

* What is the full set of things this AI can cause to happen, directly, indirectly, or by calling tools?
* Which actions are reversible, and at what cost? Which are not?
* What is the worst single action it could take, and what would recovery cost?
* How are the AI’s permissions constrained? Is it only a prompt asking it to not do something undesirable, or a 3rd party tool that claims to be sandboxed? Or are the AI’s potential actions limited by fundamental architectural bounds that can never be violated, no matter what the model or 3rd party software tries could result in harm. Even an evil hacker who knows all of your code with complete control of the AI could result in harm.

### Section 6: A Worked Example: The PO Pipeline, End to End

Let’s revisit the PO extraction pipeline as an end-to-end example, to explore what a risk assessment would look like under the proposed framework.

The system.An AI-powered invoice and purchase-order processing pipeline with the following workflow:

1. A supplier emails the business a PDF (purchase order, invoice, or both).
2. An automated process picks up the email, extracts the PDF from an email, and sends it, via strongly encrypted API to a frontier model with a prompt asking for structured JSON: buyer, account number, line items, unit prices, total, etc. (be precise)
3. The returned JSON is validated and if there are no JSON-formatting or type errors, the record is written to the accounting database.
4. A scheduled job processes pending records and triggers payment workflows.

The business is excited about this because it replaces an expensive manual data-entry step. The system “works” in the demo, every PDF is perfectly processed. Everyone is happy. Time to think about what could actually go wrong.

Data risk in the pipeline.Every PDF the business receives is sent to a third-party model provider. That provider’s data handling is governed by their terms of service, not by the business’s contracts with its suppliers. If a supplier’s PDF contains anything beyond pure transactional data, a contact’s personal email, a signature, an attached form with banking details, an SSN on an attached W-9, that information has just crossed a boundary the business may not have disclosed to anyone. If the business operates in a regulated space (healthcare, finance, defense), the consequences range from “uncomfortable” to “we need to call our regulatory counsel.” And critically, the data is exposed regardless of whether or not the model returns the right answer. In the simple system, all received e-mails with valid PDFs are processed, so if that same e-mail were sent something that is not a PO, it would still be sent to the model.

Output risk in the pipeline.The model occasionally misreads numbers. This is not exotic, frontier models make OCR-style errors on PDFs with low-contrast scans, unusual fonts, uncommon formats (i.e. “1250 00 USD” or “$1.250,00”, hand-written annotations, etc... The misread might be a digit transposition ($1,250 → $1,520), an extra pair of zeros ($1,250 → $125,000), or a more subtle drift (the model conflates the unit price with the line total because the columns are visually ambiguous).

Action risk in the pipeline.Step 4, the scheduled payment processor, is the action surface. Once a record exists in the accounting database, the downstream system treats it as authoritative and triggers a payment.

What this looks like under the framework:

* Data risk: high, unconditional. Mitigation requires architectural changes to how data crosses the third-party boundary (private deployment, redaction before submission, contractual terms, or moving to a model the business hosts itself).
* Output risk: medium, frequency-dependent. Mitigation requires either improving extraction accuracy (better models, better prompts, deterministic OCR as a first pass) or improving error detection downstream (confidence scoring, cross-checks against known supplier data, totals reconciliation).
* Action risk: high if fully automated, low if a review step exists. This is the single most impactful architectural decision in the system.

#### A small system architectural change

Now consider a modified version of the same pipeline. Everything is identical except for one addition: between the model’s extraction step and the database write, the system performs a deterministic lookup. Each field, account number, extracted SKU, etc… is checked against a known supplier-and-product database, and the corresponding field i.e. extracted unit price is compared to the data on file. If the SKU is unknown, or the extracted price differs from the expected price by more than a small tolerance, the record is flagged for a human reviewer instead of automatically being written to the accounting database. Records that pass the check proceed automatically.

Re-running the risk assessment on this version of the pipeline:

* Data risk: still high, still unconditional. The architectural change does not affect what crosses the third-party boundary. Mitigations for data risk must be handled separately.
* Output risk of the AI-based OCR component: same frequency as before (the model errs at the same rate), but theconsequencesof output errors are now bounded. A misread number that disagrees with the price-on-file gets routed to a human; a misread number thathappens to matchan existing SKU at a wrong price is the only case that still propagates without human review (assuming the DB is correct).
* Action risk: dramatically reduced. The automated payment workflow now executes only on records that have passed a deterministic check, or human review. The system fails only when both the model errsandthe error happens to evade the deterministic and human checks.

The principle here is worth naming explicitly: a probabilistic component (the model) is paired with a deterministic check (the database lookup) and when risky a human-validation, and harm is now only possible whenbothfail (assuming no false-positives on the DB-check).

The improved system’s human-review path is more sustainable than having a human either perform all extraction manually or review all AI-OCR predictions. When compared to a human-reviewing all AI-results pipeline, a human reviewing is reviewing a large set of correct records to catch a few wrong ones, which produces the well-known phenomenon of reviewer fatigue and missed errors. In the modified pipeline, humans only see records that already failed the deterministic check, which is a much smaller and much more interesting set. The same human effort yields much better error detection because the work has been pre-filtered to the cases that actually need judgment.

None of this required a different model, a different vendor, or a different prompt. It required noticing that the system already has authoritative reference data and that the model’s output could be checked against it before being acted on. That observation came from mapping the system, identifying the action surface, and asking what deterministic facts about the domain could be used to bound the OCR-component’s output error surface.

### Section 7 — Conclusion And What’s Next

This post presents a framework for examining AI-related business risks by mapping risk at the component level and making architectural adjustments rather than isolated fixes, since reducing risk in one component alone won’t eliminate broader business exposure. By shifting how AI risks are discussed, organizations can be precise about failure modes and make effective decisions; illustrated by an example where OCR payment errors were solved through engineering and data design rather than model changes. The mitigation toolkit spans three categories: output risk, data risk, and action risk. The framework stops short of replacing formal compliance work like NIST AI RMF or the EU AI Act, quantifying risk in dollars, or recommending specific vendors, but it does enable business to make dollar quantification of risks and make vendor selection tractable. Whether a company is just starting with AI integration, scaling a proof of concept, or recovering from a past failure, this approach can help.

In future posts, I will examine various real-world types of risks that may seem insurmountable, and explore generalized approaches to significantly reducing, and in many cases totally eliminating the business risk. For example, how can you get the benefit of an AI-chat-bot interface but reduce or eliminate the risks of returning incorrect responses? How can you rely on AI-models or even possibly train on data that is PII while reducing PII-leakage risks?

If you are working on this problem at your company and want help, reach outhttps://appliedingenuity.ai/Most engagements start with mapping an existing or planned integration through the framework in this post and identifying the highest-leverage architectural changes.

### Further reading/References

If you want to go deeper than this post does, the following are worth your time, in roughly the order I would suggest reading them:

* Simon Willison,“The lethal trifecta”(June 2025). The canonical practitioner framing of why combinations of private data access, untrusted content, and exfiltration capability are uniquely dangerous in AI systems.
* OWASP Top 10 for LLM Applications, 2025 edition. The closest vulnerability catalog to what builders actually need. Most useful for security teams beginning to assess an existing AI integration. Helpful for understanding LLM-specific attacks/threats.
* OWASP Top 10 for Agentic AI, 2025. The action-risk deep dive. Newer and less mature than the LLM list but the right starting point for teams shipping agentic systems.
* NIST AI Risk Management Framework 1.0(January 2023). The governance framework that regulators and auditors increasingly look to. Less useful for architects, more useful for risk officers and compliance teams.
* EU AI Act(Regulation 2024/1689). The regulatory standard, mandatory for organizations doing business in the EU.
* MIT AI Risk Repository(airisk.mit.edu). The most comprehensive academic taxonomy. Worth knowing exists; rarely the right tool for an architecture review.
* My earlier post,“The ‘LLM-as-Analyst’ Trap”. The technical deep-dive on agentic data systems that several readers told me put words to problems they were already living with. Relevant background for the action-risk material that will appear in upcoming posts in this series.

This is the first post in a series. Future posts will explore the specific AI mechanism risks, and suggest approaches to reducing or eliminating various business risks. For example, how is it possible to eliminate the risk of an AI making a false statement about peanuts being in a product?AppliedIngenuity.AIwas created to help businesses navigate the challenges of effectively leveraging AI. Reach out if we can help you.

Thanks for reading AppliedIngenuity.ai: Practical AI Solutions! This post is public so feel free to share it.

Share

If you are not already a paid or free subscriber, to receive new posts and support this work, consider becoming a free or paid subscriber.

Subscribe
3
1
1
Share