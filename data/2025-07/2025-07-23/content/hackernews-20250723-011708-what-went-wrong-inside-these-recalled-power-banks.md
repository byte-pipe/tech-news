---
title: What Went Wrong Inside These Recalled Power Banks?
url: https://www.lumafield.com/article/what-went-wrong-inside-these-recalled-power-banks
site_name: hackernews
fetched_at: '2025-07-23T01:17:08.833786'
original_url: https://www.lumafield.com/article/what-went-wrong-inside-these-recalled-power-banks
author: walterbell
date: '2025-07-23'
description: Investigate Anker’s recalled power banks. See how CT scanning uncovers battery defects and improves safety in lithium-ion designs.
---

Article
Article

# What Went Wrong Inside These Recalled Power Banks?

July 17, 2025

Article

# What Went Wrong Inside These Recalled Power Banks?

Lithium-ion batteries power the many electronic devices that we rely on every day, from EVs to smartphones and laptops. They’re so prevalent, that the average American owns nine lithium battery-powered devices.1But they carry real risks when quality lapses occur. Overheating and fire hazards can cause property damage, injuries, or worse. With millions of these batteries in circulation, even a single defect can have a ripple effect of consequences for consumer safety and brand reputation.

Recently, Anker recalled over one million PowerCore 10000 power banks, model A1263, produced between 2016 and 2019 and sold through 2022.2,3Anker has provided a general warning that the lithium-ion battery can overheat, but they have yet to share the exact reason for the recall. Armed with ourNeptune Industrial CT Scannerand five A1263 power banks from Lumafield team members, we set out to see if we could identify the source of this recall. Could we identify the defects with CT scanning? And could CT inspectionduring development or manufacturinghave prevented the faulty power banks from shipping in the first place?

###### Scanning Setup

We procured five potentially-affected power banks from various Lumafield colleagues, which we labelled PB1, PB2, PB3, PB4, and PB5. We then ran the serial numbers against Anker’s recall form, and determined that three of our power banks were impacted, while two were not.

The power banks were scanned using Lumafield’s Microfocus Neptune. This configuration’s small X-ray spot size makes it the ideal tool for resolving fine details in electronics and batteries.4

Use the embeddedVoyagerwindow below to explore the CT scan of the recalled power bank. Rotate and examine it from any angle.

###### First Look: Battery Cells

The first element we compared across the power banks were the battery cells themselves. A lithium-ion battery consists of two separated electrodes. The anode, usually graphite, stores lithium ions during charging. The cathode, typically a layered metal oxide, releases and accepts lithium ions as they move through the electrolyte during charge and discharge, enabling reversible energy storage.

There are a few common defects in the battery manufacturing process that can be easily spotted in a CT scan. For example, in lithium-ion batteries, it’s important to ensure that the anode has a sufficient overhang above the cathode, preventing the lithium plating that can lead to dendrite formation.5Dendrites can subsequently result in degraded performance and short circuits, which can cause the worst-case scenarios of thermal runaway. CT scanning can also be used for Foreign Object Detection (FOD) within batteries, as particle contamination can lead to reduced performance and potentially short circuits.

The A1263 power banks each contain three 18650 lithium-ion battery cells inside. It was quickly apparent that batteries from at least two different suppliers had been used within the affected power banks. The cells in PB1 (recalled), PB2 (recalled), PB4 (not recalled), and PB5 (not recalled) seemed similar, but the cells in PB3 (recalled) had a few key differences.

First, the batteries in PB3 have a mandrel to help prevent core collapse, a type of deformation in lithium-ion batteries with “jelly roll” construction where the innermost layers can sag into the center.6Mandrels can also serve as a pathway for gas escape in case of overpressurization. Some suppliers add a center tube to strengthen the core and prevent this from happening. Though none of the batteries in the five power banks we scanned seem to show core collapse, only PB3 has reinforcement material to combat this potential issue.

On the left cell, from PB3, reinforcement foil appears as bright, dense material around the battery’s center. This is noticeably absent from the right cell, from PB1. 

The other discrepancy in the PB3 batteries is the number and style of vent openings. PB1, PB2, PB4, and PB5 have four smaller openings at the positive terminal, while the PB3 cells have three larger ones. This further suggests that the batteries in PB3 come from a different source.

In the left image, we observe 3 vent openings from a cell in PB3. In the right image we see the four vent openings common across the cells in PB1, PB2, PB4, and PB5. 

If the recall is affecting units made with 18650 battery cells from multiple suppliers, that suggests the root cause of the recall stems from elsewhere in the power bank. We next focused on the PCB and assembly of the board with the cells.

###### Assembly Discrepancies

Looking at the assembly of the A1263 power banks, one difference between the recalled and non-recalled devices stood out immediately. All five power banks used tab bus bars to connect the positive and negative terminals of the 18650 cells. However, the non-recalled PB4 and PB5 devices used conventional insulated wires to make the positive and negative connections to the PCB, while the recalled PB1, PB2, and PB3 power banks used flat tab wire for the entirety of the connection.

On the left image of PB4, thin insulated wires are clearly visible. On the right image of PB2, wide thin tabs are used for the connections instead.

‍

A closer look at the connections between the cells and PCB in PB4 (left) and PB2 (right).

Looking more closely at the connections of PB1, PB2, and PB3, we see some process variation that could be a potential cause for concern. The shape of the negative tab differs dramatically, and in PB1 it appears slightly twisted.

From left to right, the negative tab crossing above the positive tab - PB1, PB2, PB3.

We can measure the distance to quantify how dramatically the gap between the positive and negative bus bars varies across the three units. In PB1, that distance is only 0.52 mm, compared to 1.12 mm in PB2 and 1.58 mm in PB3. The short distance and visible deformation in PB3 suggests the possibility of the negative bus bar shorting out against the positive bus in some scenarios.

From left to right, measurements of the space between the negative and positive tabs for PB1, PB2, and PB3.

###### Evolving Power Bank Design

In addition to the recalled power bank, we scanned Anker’s current PowerCore 10000 model, the Anker 313. This model was first released in January 2023. The exterior of the power bank has changed significantly. At 5.87 in by 2.68 in by 0.55 in,7compared to the A1263’s dimensions of 3.62 in by 2.36 in by 0.87 in,8the 10K product has become longer and wider, but also noticeably thinner.

Looking inside, we find this slimming has been accomplished by replacing the three 18650 cylindrical cells with a single lithium-ion pouch cell. With 90-95% packaging efficiency, pouch cells are maximally compact relative to other battery cell designs and can be customized to accommodate different industrial design requirements.9The single-cell configuration of the Anker 313 simplifies the assembly required. We also see that significant changes have been made to the embedded electronics, as is to be expected given both the new product architecture and the general advances in PCB manufacturing since the A1263 was manufactured.

CT scan of the updated Anker PowerCore 10000, showing the single lithium-ion pouch cell and a slice of its PCBA.

###### Conclusion

CT scanning the A1263 Anker PowerCore 10000 power banks has provided a small window into the supply chain complexity of these pervasive, ostensibly simple products. This SKU was manufactured over a period of 3 years and 10 months, and sold for over six and a half years. From our limited analysis of just five power banks, a small subset of the millions of devices sold, we have identified that throughout the A1263 production period at least two battery cell versions and two battery connector designs were used. A larger sample size would likely reveal further variations.

Managing a high-volume battery supply chain is inherently challenging, and ensuring quality throughout each stage is essential. Only Anker can know for sure why these popular consumer devices have warranted a recall three years after they were last sold. However, though we don't know exactly what flaw triggered this massive recall, it illustrates just how costly quality issues can be. The volumes involved in these types of consumer products can be staggering, and it can be extraordinarily difficult to track quality issues all the way upstream.

Since we began this exploration, Anker has issued a new recall for five additional power bank models: Anker Power Bank models A1257 and A1647, Anker MagGo Power Bank model A1652, and Anker Zolo Power Bank models A1681 and A1689.10Unlike the A1263 Anker PowerCore 10000 power banks, these are more recent products.

Anker has shared that the recall was caused by potential issues with one of their battery suppliers. Their English announcement credits the more rigorous quality processes they implemented earlier this year with catching the cause for concern,11while announcements in China by Anker and competitor ROMOSS Technology disclosed that the cell supplier in question made an undisclosed change in the raw materials used, which could lead to insulation degradation.12Anker has recalled 710,00 units from those models in China, and the global numbers have yet to be disclosed.

Looking just at the recall of  A1263 Anker PowerCore 10000 power banks sold between 2016 and 2022, about 1,158,000 units have been affected. Impacted users will receive either a replacement unit or a $30 Anker Store gift card, implying a financial exposure of over $34 million, not including other relevant recall-related costs.

Beyond the immediate economic impact, battery recalls can cause permanent reputational damage that proves impossible to quantify in the long term. Anker has underscored their commitment to better quality assurance processes and signed an agreement with a new battery vendor13as they work to regain the trust of their customers.

Industrial CT inspection offers a powerful tool that can help ensure the safety of the many battery products that surround us. It can be leveraged during thedesign and developmentstages to validate designs and brought into the manufacturing ramp-up to supportFirst Article Inspectionand validate assembly processes. In production, it can non-destructivelyverify quality, both upstream and downstream. And after parts have shipped, CT scanning can be used to support fasterfailure analysisas issues arise in the field.

Ultimately, ensuring the reliability of lithium-ion battery products is becoming more critical than ever, as these devices become increasingly embedded in our daily lives. As CT inspection becomes more accessible and easier to adopt, it can serve as a safeguard of both consumer safety and manufacturers’ bottom lines.
