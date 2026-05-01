---
title: "Credit Cards Are Vulnerable To Brute Force Kind Attacks | Metin's Blog"
url: https://metin.nextc.org/posts/Credit_Cards_Are_Vulnerable_To_Brute_Force_Kind_Attacks.html
date: 2026-05-01
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-02T08:48:35.626607
---

# Credit Cards Are Vulnerable To Brute Force Kind Attacks | Metin's Blog

# Credit Cards Are Vulnerable To Brute Force Kind Attacks

## PCI‑DSS Overview
- PCI‑DSS defines the minimum security controls for handling credit‑card data.  
- It requires masking of sensitive fields and limits what can be displayed on UI, receipts, logs, etc.  

## What PCI‑DSS Allows to be Displayed
- Primary Account Number (PAN): only the Issuer Identification Number (first 6 digits) and the last 4 digits may be shown.  
- Cardholder name, service code, and expiration date may be shown in full.  

## What PCI‑DSS Prohibits from Being Displayed
- Full track data.  
- Card verification code (CVC/CVV).  
- PIN or PIN block.  

## Personal Incident (Story Time)
- I used a virtual credit card with limits and 2FA, saved only on reputable merchants.  
- Received an SMS about a purchase attempt from a saved merchant; I changed passwords, reduced limits, but did not disable the card.  
- Hours later, I received multiple 3‑D Secure SMS prompts from merchants I never used; all attempts failed.  
- While on a call with my bank, another merchant (exempt from 3‑D Secure) withdrew the remaining limit and transferred the funds to an e‑wallet that could be cashed out.  
- After filing a chargeback, the bank returned the money.  

## How the Attack Worked
- Attackers breached my account and captured the data shown during a purchase attempt: masked PAN, full expiration date, and the bank name from the 3‑D Secure page.  
- They did not have the full PAN or CVV initially, but leveraged validation endpoints from other merchants to brute‑force the missing digits.  

## PAN Brute‑Force Feasibility
- A PAN consists of:  
  - 6‑digit Issuer Identification Number (known).  
  - Variable‑length account identifier (unknown).  
  - 1‑digit Luhn check digit.  
- With the first 6 and last 4 digits known, only 10⁶ possible combinations remain for the middle digits, reduced further by the Luhn checksum to about 99 999 candidates.  
- Payment gateways often return specific error codes (e.g., “invalid card”, “expired”, “CVV incorrect”), which guide the attacker in narrowing down the correct number.  
- Attackers performed roughly 6 requests per second across multiple APIs, rotating IPs via proxies, staying below detection thresholds.  

## Additional Observations
- Some merchants are exempt from 3‑D Secure, allowing them to process payments without the extra authentication step and assuming liability for chargebacks.  
- PCI‑DSS compliance focuses on minimum requirements; many companies implement only the bare minimum to pass certification, leaving exploitable gaps.  
- Physical receipts often expose the same masked PAN and expiration date, making discarded receipts a source of data for attackers.  

## Aftermath
- Received a full refund through a chargeback.  
- Merchant that converted the credit‑card funds to cash showed no interest in addressing the vulnerability.  
- The e‑commerce site defended its practice of showing 10 digits plus expiration date, refusing to treat it as a security flaw.  

## Takeaway
- Even when PCI‑DSS‑compliant merchants mask card numbers, the combination of exposed data, permissive validation APIs, and low‑rate brute‑force attacks can reconstruct full PANs and enable unauthorized transactions.  
- Users should treat saved cards and discarded receipts as potential attack vectors and consider additional protective measures beyond compliance standards.