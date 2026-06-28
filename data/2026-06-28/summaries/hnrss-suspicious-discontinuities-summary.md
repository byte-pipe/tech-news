---
title: Suspicious discontinuities
url: https://danluu.com/discontinuities/
date: 2026-06-27
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-28T18:02:42.574986
---

# Suspicious discontinuities

# Suspicious discontinuities

## Main argument
- Sharp income or metric thresholds in policies and systems create perverse incentives, leading people to intentionally reduce earnings or manipulate outcomes to stay just below a cutoff.
- Examples span health‑insurance subsidies, welfare programs, academic admissions, election reporting, market pricing, and scientific publishing.
- Smoother, gradual phase‑outs are proposed as a general remedy to reduce these distortions.

## Policy‑level discontinuities
- **ACA subsidy cutoff** – $48,560 for individuals; earning above it can add roughly $7,200/yr in premiums, so some may aim to earn $6,440 less.
- **Other U.S. programs** – TANF, Medicaid, CHIP (free and reduced‑cost) have similar hard limits that can make lower income more attractive.
- Legal perspective: arranging affairs to minimize taxes is lawful and widely accepted (citing Learned Hand), but a system that pushes people to lose money is inefficient.

## Suggested fix
- Replace abrupt thresholds with **slow phase‑outs**, already used for some subsidies, to lessen incentive spikes.

## Illustrative discontinuities

### Hardware or software queues
- Naïve queues drop all new items when full, creating a binary outcome.
- **Random early drop** techniques assign a drop probability based on fullness, smoothing the transition.

### College admissions and Pell Grants
- Pell‑Grant eligibility becomes a proxy for low‑income support; admission chances jump at the grant line.
- Within each side of the threshold, the most disadvantaged (lowest income below the line, highest income above) benefit the most, opposite to policy intent.
- Parents may manipulate income (e.g., losing money on options) to fall below the Pell threshold and improve admission odds.

### Election statistics
- Russian polling‑station data show spikes at round turnout percentages (e.g., 95%) beginning around 2004, suggesting fabricated results that avoid smooth distributions.
- Related detection method: Benford’s law.

### Used‑car auction prices
- Prices and volume exhibit clear jumps at the $10,000 mark, even after adjusting for factors like model year.

### p‑values in psychology
- Researchers are driven to achieve p‑values just below conventional significance thresholds (0.05, 0.01, 0.1).
- Histograms reveal excess counts immediately below 0.05, indicating possible data‑dredging, editorial bias, or selective reporting.
- Calls to abandon strict significance thresholds (e.g., Gelman’s campaign) aim to remove this incentive.

## Broader implication
- Discontinuous rules, whether in tax policy, technical systems, or academic standards, can unintentionally reward undesirable behavior.
- Implementing gradual transitions or removing sharp cut‑offs can mitigate “gaming” and lead to more efficient, fair outcomes.