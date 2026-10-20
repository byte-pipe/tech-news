---
title: Bank alerts to a day-book, with a local Gemma - DEV Community
url: https://dev.to/dannwaneri/bank-alerts-to-a-day-book-with-a-local-gemma-21dl
site_name: devto
content_file: devto-bank-alerts-to-a-day-book-with-a-local-gemma-dev-c
fetched_at: '2026-10-20T15:35:00.605783'
original_url: https://dev.to/dannwaneri/bank-alerts-to-a-day-book-with-a-local-gemma-21dl
author: Daniel Nwaneri
date: '2026-10-19'
description: 'This is a submission for the Hacktoberfest Open-Source AI Challenge Week 2: Side Hustle ... Tagged with devchallenge, hf26challenge, gemma, opensource.'
tags: '#devchallenge, #hf26challenge, #gemma, #opensource'
---

Hacktoberfest Open-Source AI Challenge Week 2: Side Hustle Submission 💸

This is a submission for theHacktoberfest Open-Source AI Challenge Week 2: Side Hustle

## What I Built

In Nigeria, a POS operator runs a small stand with a card terminal (POS means point of sale). Many people get cash this way instead of from an ATM: the customer sends her money by bank transfer from their phone, and she hands over the same amount in cash, for a small charge. Mama POS works a stand in Port Harcourt, a city in southern Nigeria. She charges ₦150 for each ₦5,000 (₦ is the naira, Nigeria's money; that is a 3% fee). She does 10 to 20 of these a day.

Her bank, Moniepoint, sends her an email for each payment that comes in. Nigerians call this a credit alert. It is how she sees that a customer's money arrived. On 15 Oct I found her at her stand with her POS machines and asked how she keeps track. She said:

* She writes each payment in a notebook, and it "takes long".
* When the money does not balance, it is "a pain", so she stopped checking.
* A customer saying "I sent it" when the money has not arrived "usually happens".
* She pays for no tool now. When I asked if she would pay ₦5,000 a month for one that does this, she said yes.

So I built a day-book, a daily record of money in, like her notebook but filled in for her. She pastes the alert emails, and she gets:

* Rows with the time, the amount, the kind of money and the customer's name. She types nothing. The kind is one of: a customer's transfer, phone credit she bought for herself (Nigerians call it airtime), a bank reward, or a failed transfer coming back.
* Did it land? She types the amount a customer says they sent. The app answers "Landed", "Not seen yet", or "2 payments of this amount" and asks for the name.
* End of day: money in, estimated charges, rows to check (reversals, the same amount twice within 10 minutes), and a text to paste into WhatsApp for the owner of the business she reports to.

All data stays in the browser. Nothing goes to a server.

## Demo

App:https://mama-pos-daybook.pages.dev(the model needs a device with a working GPU, for example a laptop or a Pixel 8a; the rest works on any phone)

The video uses her 5 real alerts with the customer names redacted to "NAME". It was recorded on the live app at real speed.

## Code

## dannwaneri/mama-pos-daybook

### Day-book for a Port Harcourt POS operator: paste Moniepoint alerts, code reads the money, local Gemma 1B reads the customer's name

# Mama POS day-book

A day-book for aPOS operatorin Port Harcourt, Nigeria. A POS operator runs a small stand with a card terminal
customers send her money by bank transfer, and she gives them cash, for a charge (₦150 for each ₦5,000). Her bank
(Moniepoint) sends an email for each payment that comes in. Today she writes these in a notebook. She stopped
balancing the day because it "takes long", and customers often say "I sent it" when it has not arrived.

She pastes the alert emails into the app. It gives her:

* Rows: time, amount, kind of money, and the customer's name, with no typing.
* Did it land?: type the amount a customer says they sent; the app answersLanded,Not seen yet, or2 payments of this amount.
* End of day: money in, estimated charges, rows to check (reversals, the same…

View on GitHub

## How I Built It

The rule I set at the start: code does everything code can do, and the model does only the job code cannot do. Then I measured where that line falls, on her real alerts.

step

done by

why

amount, time, balance

code

fixed fields in the email

kind of money

code (keyword rules)

rules got 5/5 on her real alerts, Gemma got 4/5

customer's name

Gemma 3 1B

every sender's bank writes it differently

did it land, end of day, charges

code

arithmetic

The name is the hard part. On her alerts, the line that names the customer says "TRANSFER TO [customer] [bank]", on money that came in. I expected "TRANSFER FROM", and so did my keyword rules: they found 0 of 3 customer names. Gemma found most of them: on the run in the video it found 3 of 3; on an earlier test run it found 2 of 3. The one it missed is an alert whose whole narration is the customer's name and nothing else.

The model is Gemma 3 1B instruct (ONNX, q4), running in the browser with transformers.js on WebGPU. The first load downloads 859 MB once; after that it loads in a few seconds, with no internet (tested with the network off: ready in 6 s), and reads a name in about 2 to 5 s on my laptop.

The model can only copy. A guard checks every answer before it is saved:

* it must be JSON, with a kind from a fixed list;
* the name must be text copied from the alert, and it must contain letters;
* any number in the answer must appear in the alert;
* a bank name at the end of the name is cut off by code ("[customer] OPay" → "[customer]");
* one retry, then the name stays "not read". It is never guessed.

The money totals never depend on the model. If Gemma is not loaded, or the GPU drops out, every row still has its amount, time and kind, and the day still adds up.

Things that broke, and what I changed:

* Her phone cannot run it. It is a Tecno Camon 17 Pro on Android 11; it reports WebGPU, but refuses to give a GPU adapter. The CPU version of the model (int8) scored 1 of 30 kinds at 36 s per alert, even on my laptop: it ignores "answer in JSON" and writes paragraphs. So on her phone the app says it needs a GPU, instead of starting a 1 GB download. On my Pixel 8a, which has a working GPU, Gemma runs on the phone itself: the status says "ready (webgpu)" and the names fill in.
* Downloads stalled silently on 4G: the bytes stopped and no error came. I wrote a resumable download: 8 MB pieces, saved as they land, a piece with no bytes for 15 s is retried, and a stopped download continues from the last piece. On her phone the full model download then finished with no stall.
* The GPU dropped out once in the middle of a run ("Device was lost"). Now the app stops on the first failed call and asks for a reload, instead of marking every row as unclear.

Results (all inbench/RESULTS.md):

test

kind

name

her 5 real alerts, her labels

5/5

4/5

30 synthetic alerts I wrote

30/30 *

23/30

The name score counts all 5 alerts. Two of them (her airtime and her cashback) have no customer name, so "no name" is the right answer there; on the 3 customer transfers, Gemma got 2 in that test run.

* Not a fair kind score: I wrote both the keyword rules and the synthetic set. Her real alerts are the fair test, and 5 is a small set. I also wrote the bank-name cut after I saw her alerts, so treat the real-alert result as a field check, not a benchmark.

## Why Does Open Innovation Matter?

Her customers' names and her balances never leave the device. These alerts show who paid her, how much, and what is in her account. A cloud API would mean sending all of that to a company she has never heard of. With an open model running in the browser, nothing is sent.

The price works. She paid ₦5,000 up front, a few US dollars. A paid API call for every alert, every day, does not fit inside that. A model that runs on the user's own device costs nothing per alert, so the ₦5,000 is not eaten by API fees.

It also works when the network does not. After the one-time download, the model and the app run offline. In Port Harcourt, power and data both drop out.

And I could see why it failed. With open weights I could test the exact model in its two versions (q4 on the GPU, int8 on the CPU), measure both, and choose. That is how I found that the CPU version cannot do this job, before it reached her.

## My First User

Mama POS is the person this is for, and the name is the one she chose for this post.

What she did:

* She told me the problem, in the words quoted above.
* She gave me 5 of her real alert emails. I redacted the names, account numbers and references before I used them.
* She labelled them: for each alert she told me what the money was (customer cash, her own airtime, cashback) and confirmed that the name after "TRANSFER TO" is the customer's. Those labels are the real-alert scores above.

She paid ₦5,000 up front, for the promise of it. She has not used it herself yet. Her phone cannot run Gemma (no working GPU), so for now the day-book part works on her phone and the names need a laptop. She promised to upgrade her phone. On a phone with a working GPU, like my Pixel 8a, the whole app runs on the phone.

What it does not do yet: Nomba alerts. Nomba is a second POS provider she uses, and the app reads only Moniepoint alerts.

## Prize Categories

Best Use of Gemma. Gemma 3 1B runs in the browser on the user's own GPU and does the one job in the app that code could not do: reading the customer's name from free text written differently by every bank.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse