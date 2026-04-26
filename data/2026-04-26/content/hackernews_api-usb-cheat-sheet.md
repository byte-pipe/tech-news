---
title: USB Cheat Sheet
url: https://fabiensanglard.net/usbcheat/index.html
site_name: hackernews_api
content_file: hackernews_api-usb-cheat-sheet
fetched_at: '2026-04-26T11:38:22.429389'
original_url: https://fabiensanglard.net/usbcheat/index.html
author: gwerbret
date: '2026-04-25'
description: USB Cheat Sheet (2022)
tags:
- hackernews
- trending
---

FABIEN SANGLARD'S WEBSITE

CONTACT
    
RSS
     
DONATE

May 05, 2022

USB Cheat Sheet

I spend time investigating a non-existing bug today because I misunderstood a USB term. So I made myself a cheat sheet. Maybe it will save time to someone.

Marketing Name

Also Known As

Signal Gbps

Signal MiB/s

Wires

Cable

USB 1.1

Full Speed

12 Mbps

1.5 MiB/s

4

4m

USB 2.0

Hi-Speed

480 Mbps

60 MiB/s

4

4m

SuperSpeed USB  5Gbps

USB 3.0

			USB 3.1

			USB 3.2

 USB 3.1 Gen 1

 USB 3.2 Gen 1

5000 Mbps

625 MiB/s

8

3m

SuperSpeedPlus USB 10Gbps

USB 3.1

			USB 3.2

USB 3.1 Gen 2

USB 3.2 Gen 2

10000 Mbps

1250 MiB/s

8

2m

SuperSpeedPlus USB 20Gbps

USB 3.2

			USB 3.2 Gen 2x2

20000 Mbps

2500 MiB/s

12

1m

USB4 20Gbps

USB4 Gen 2×2

			USB4

20000 Mbps

2500 MiB/s

12

0.8m

USB4 40Gbps

USB4 Gen 3×2

			USB4

40000 Mbps

5000 MiB/s

12

0.8m

Gen naming Convention, lanes, and Speed

USB GenAxBA = GenerationB = Num lanes used

Name

Signal

Sig Total
a

Encoding

Effective b
b

Effective B
b

Real Life
c

USB 3.2 Gen 
1
x
1

5,000 Mbps

5,000 Mbps

8b/10b

4,000 Mbps

500 MiB/s

400 MiB/s
[1]

USB 3.2 Gen 
1
x
2

5,000 Mbps

10,000 Mbps

8b/10b

8,000 Mbps

1,000 MiB/s

800 MiB/s  

USB 3.2 Gen 
2
x
1

10,000 Mbps

10,000 Mbps

128b/132b

9,696 Mbps

1,212 MiB/s

780 MiB/s
[2]

USB 3.2 Gen 
2
x
2

10,000 Mbps

20,000 Mbps

128b/132b

19,392 Mbps

2,424 MiB/s

1,600 MiB/s
[4]

USB 4 Gen 
2
x
2

10,000 Mbps

20,000 Mbps

128b/132b

19,392 Mbps

2,424 MiB/s

1,600 MiB/s  

USB 4 Gen 
3
x
2

20,000 Mbps

40,000 Mbps

128b/132b

38,787 Mbps

4,848 MiB/s

2,700 MiB/s
[5]

Note:Multi-lanes systems, uses lane striping (on TX) and lane bonding (on RX).a- What they put on the box.b- Rate with encoding overhead. e.g, 8b/10b = 20%.c- Real life sequencial read rate.

Cables

4 wires:PWR,GND,D+,D-.8 wires:PWR,GND,D+,D-.RX+,RX-,TX-,TX+.12 wires:PWR,GND,D+,D-,RX1+,RX1-,RX2-,RX2+,TX1+,TX1-,TX2-,TX2+.

Note:1 USB lane = 1 twisted wire pair +/-.Note:4 wires = 1 half-duplex lane, 8 wires = 2 lanes (one up, one down), and 12 wires = 4 lanes (two up, two down).

USB-A/B: Connectors 4/8 wires

Type-A 4-wiresType-A 8-wiresType-B 4-wiresType-B 8-wiresUSB-C: Connectors 12 wiresOnly the USB Type-C connector has enough pins to support two lanes.- CC1 and CC2 are downstream facing port (DFP) and upstream facing port (UFP) detection. Also used for power negotiation and alt mode switch.- SBU1 and SBU2 are secondary bus wires, for the DisplayPort AUX channel and hot plug detection (HPD).

Charge rates / Cable types

SpecificationsMax. VoltageMax. CurrentMax. PowerUSB 2.05V500mA2.5WUSB 3.0 / USB3.15V900mA4.5WUSB Battery Charging (BC) 1.25V1.5A7.5WUSB-C Current Mode (non-PD)5V3A15WUSB-C / Power Delivery (PD 1/2)20V5A100WUSB-C PD 3.1 (EPR)48V5A240W

Specifications

USB 1.0(Jan, 1996).USB 1.1(Sep, 1998).USB 2.0(Apr, 2000).USB 3.0(Nov, 2008).USB 3.1(Jul, 2013).USB 3.2(Sep, 2017).USB 4.0(Aug, 2019).

References

^[1]Universal Serial Bus Revision 3.0 Specification^[2]Real-world USB 3.2 Gen 2 Performance^[3]USB 3.1 Tested: Performance^[4]World’s First USB 3.2 Demonstration | Synopsys^[5]USB4.0 M.2 NVMe Enclosure Review

 

*