---
title: Datacenters in space are a terrible, horrible, no good idea.
url: https://taranis.ie/datacenters-in-space-are-a-terrible-horrible-no-good-idea/
date: 2025-11-30
site: hackernews
model: llama3.2:1b
summarized_at: 2025-11-30T11:08:16.840265
screenshot: hackernews-datacenters-in-space-are-a-terrible-horrible-no-go.png
---

# Datacenters in space are a terrible, horrible, no good idea.

**A Delusional Approach to Space Datacenters: A Cautionary Example**

As a former NASA engineer with a PhD in space electronics and a 10-year tenure at Google, I must emphasize that the article's claims regarding datacenter design for space are alarmingly naive. The author attempts to justify their misguided approach by citing abundant power access and suggesting alternative solutions using radioisotope thermal generators (RTGs). However, these arguments do not hold up to scrutiny.

**Power Generation in Space**

1. **Abundant Power Access:** Deploying solar panels or RTGs on the surface is not a viable option for space due to the atmospheric interference and lack of sufficient energy generation.
2. **Per-GPU Device Power Requirements:** The estimated 0.7kW power per GPU device required to power 200KWaE (kilowatts-watt-effective) systems in space is impractically high, equivalent to launching nearly two times as many large satellites as needed to meet the required capacity.
3. **Nuclear-Based Solution:** RTGs are inefficient and inadequate for powering modern datacenter requirements, offering a mere power output of 50-150W per device - far short of even running a single GPU.

**Thermal Regulation**

1. **ISS Advanced Thermal Control System:** The article's mention of the Boeing system is irrelevant as RTGs do not employ thermal regulation like commercial electronics devices.
2. **Boiling Points:** RTG power outputs are well below their critical temperatures required to sustain functional datacenter operations, and deploying multiple large satellites would exacerbate this issue.

**The Reality Check**

While the author may have worked in space-related fields, making unrealistic assumptions about power requirements, thermal regulation, and satellite-based solutions lacks concrete basis. Datacenters require specific conditions that cannot be easily replicated on Earth or achieved through RTGs alone. Space datacenters must adhere to harsh environmental factors, such as extreme temperatures, radiation exposure, and limited energy availability.

**Conclusion**

This article is a prime example of an overly optimistic approach that ignores fundamental principles governing space electronics and datacenter design. It's essential to acknowledge the challenges of designing for space and to recognize that any solution would require substantial technological breakthroughs, resource-intensive efforts, and severe limitations on available assets.
