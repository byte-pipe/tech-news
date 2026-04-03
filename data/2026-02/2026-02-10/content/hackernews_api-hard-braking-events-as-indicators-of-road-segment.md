---
title: Hard-braking events as indicators of road segment crash risk
url: https://research.google/blog/hard-braking-events-as-indicators-of-road-segment-crash-risk/
site_name: hackernews_api
content_file: hackernews_api-hard-braking-events-as-indicators-of-road-segment
fetched_at: '2026-02-10T11:23:44.424091'
original_url: https://research.google/blog/hard-braking-events-as-indicators-of-road-segment-crash-risk/
author: aleyan
date: '2026-02-09'
description: Hard-braking events as indicators of road segment crash risk
tags:
- hackernews
- trending
---

# Hard-braking events as indicators of road segment crash risk

January 13, 2026

Neha Arora, Mobility AI Team Lead, and Yechen Li, Software Engineer, Google Research

We establish a positive association between hard-braking events (HBEs) collected via Android Auto and actual road segment crash rates. We confirm that roads with a higher rate of HBEs have a significantly higher crash risk and suggest that such events could be used as leading measures for road safety assessment.

## Quick links

* Paper
* ShareCopy link×
* Copy link×

Traffic safety evaluation has traditionally relied on police-reported crash statistics, often considered the "gold standard" because they directly correlate with fatalities, injuries, and property damage. However, relying on historical crash data for predictive modeling presents significant challenges, because such data is inherently a "lagging" indicator. Also, crashes are statistically rare events on arterial and local roads, so it can take years to accumulate sufficient data to establish a valid safety profile for a specificroad segment. This sparsity paired with inconsistent reporting standards across regions complicates the development of robust risk prediction models. Proactive safety assessment requires "leading" measures: proxies for crash risk that correlate with safety outcomes but occur more frequently than crashes.

In "From Lagging to Leading: Validating Hard Braking Events as High-Density Indicators of Segment Crash Risk", we evaluate the efficacy of hard-braking events (HBEs) as a scalable surrogate for crash risk. An HBE is an instance where a vehicle’s forward deceleration exceeds a specific threshold (-3m/s²), which we interpret as an evasive maneuver. HBEs facilitate network-wide analysis because they are sourced from connected vehicle data, unlike proximity-based surrogates like time-to-collision that frequently necessitate the use of fixed sensors. We established a statistically significant positive correlation between the rates of crashes (of any severity level) and HBE frequency by combining public crash data fromVirginiaandCaliforniawith anonymized, aggregated HBE information from theAndroid Auto platform.

## Data density

To validate the utility of this metric, we analyzed 10 years of public crash data alongside aggregated HBE measurements. The immediate advantage of HBEs is the density of the signal. Our analysis of road segments in California and Virginia revealed that the number of segments with observed HBEs was 18 times greater than those with reported crashes. While crash data is notoriously sparse — requiring years to observe a single event on some local roads — HBEs provide a continuous stream of data, effectively filling the gaps in the safety map.

HBEs are observed on 18x more road segments compared to reported crashes.

## Statistical validation

The core objective was to determine if a high frequency of HBEs causally links to a high rate of crashes. We employednegative binomial(NB) regression models, a standard approach in theHighway Safety Manual(HSM), to account for a higher degree of variance than is typically found in crash data.

Our model structure controlled for various confounding factors, including:

* Exposure:Traffic volume and segment length.
* Infrastructure:Road type (local, arterial, highway), slope, and cumulative turning angle.
* Dynamics:Presence of ramps and change in the number of lanes.

The results demonstrated a statistically significant association between HBE rates and crash rates across both states. Road segments with higher frequencies of hard braking consistently exhibited higher crash rates, a relationship that holds true across different road types, from local arterials tocontrolled-access highways.

Crash Rate vs. HBE rate for different types of roads in California and Virginia.

The regression analysis also quantified the impact of specific infrastructure elements. For instance, the presence of a ramp on a road segment was positively associated with crash risk in both states, likely due to the weaving maneuvers required for merging.

## Case study: High-risk merge identification

To visualize the practical application of this metric, we examined afreeway merge segmentin California connecting Highway 101 and Highway 880. Historical data indicates this segment has an HBE rate approximately 70 times higher than the average California freeway, and averaging a crash every six weeks for a decade.

Freeway merge segment in California Bay Area with one crash every six weeks and a 70x higher than average HBE rate.

When analyzing the connected vehicle data for this location, we found that it ranked in the top 1% of all road segments for HBE frequency. The HBE signal successfully flagged this outlier without relying on the decade of crash reports it took to statistically confirm the risk. This alignment validates HBEs as a reliable proxy capable of identifying high-risk locations even in the absence of long-term collision history.

## Real-world application

Validating HBEs as a reliable proxy for crash risk transforms a raw sensor metric into a trusted safety tool for road management. This validation supports the use of connected vehicle data for network-wide traffic safety assessment, offering enhanced spatial and temporal granularity. While these results indicate utility for road segment risk determination, they do not draw conclusions about location-independent driving behavior risk.

TheMobility AIteam at Google Research is working withGoogle Maps Platformto externalize these HBE datasets as a part ofRoads Management Insightsoffering. By integrating these high-density signals, transportation agencies can access aggregated, anonymized data that is substantially more fresh and that covers a wider breadth of the road network compared to traditional crash statistics. This allows for the identification of high-risk locations using leading indicators rather than relying solely on lagging and sparse collision records.

## Future work

While this study confirms that HBEs are a robust leading indicator of crash risk, there are opportunities to further refine this signal. We are currently investigating mechanisms to spatially cluster homogenous road segments to reduce data sparsity even further. Addressing these limitations will enable the transition from risk identification to targeted engineering, where high-density data informs specific infrastructure interventions ranging from signal timing adjustments and improved signage to the geometric redesign of high-risk merge lanes.

## Acknowledgements

This work was a collaborative effort involving researchers from Google and Virginia Tech. We thank our co-authors Shantanu Shahane, Shoshana Vasserman, Carolina Osorio, Yi-fan Chen, Ivan Kuznetsov, Kristin White, Justyna Swiatkowska, and Feng Guo. We also appreciate the contributions of Aurora Cheung, Andrew Stober, Reymund Dumlao, and Nick Kan in translating this research into practical applications.

* Algorithms & Theory
* Product

## Quick links

* Paper
* ShareCopy link×
* Copy link×

×

❮

❯

 Line graph titled "Crash Segments" showing the number of road segments with crashes from 2016 to 2025.


 Street view and aerial map of the Highway 101 and 880 merge with arrows and crash warning icons indicating an intersection with high crash rate.


 Comparison graphs for California and Virginia showing the correlation between HBE rates and crash rates by road type.
