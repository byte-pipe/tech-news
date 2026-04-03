---
title: How a monopoly ISP refuses to fix upstream infrastructure – The Sacramento Bear
url: https://sacbear.com/xfinity-wont-fix-internet/
site_name: hackernews_api
fetched_at: '2025-11-23T19:06:32.935757'
original_url: https://sacbear.com/xfinity-wont-fix-internet/
author: vedmed
date: '2025-11-23'
description: A monopoly ISP refuses to fix upstream infrastructure
tags:
- hackernews
- trending
---

Technology

# How a monopoly ISP refuses to fix upstream infrastructure

November 22, 2025

by
The Sacramento Bear

A documented case of infrastructure failure, failed escalation, and a company that refuses to investigate.

## Here’s the situation: I have outages. My neighbor has the same outages. Xfinity won’t fix it.

I bought Xfinity internet in June 2024. Immediately, my connection started dropping. Multiple times a day. Every single day. After troubleshooting every piece of equipment I had and questioning my sanity my neighbor complained about the same thing which led me to understand this was not my equipment.

I set up an uptime monitor and found that these outages happen 6-7 times per day for 125 seconds.

Uncheck this box on your Gateway in OPNSense to log it, and set a monitor ip to something like 8.8.8.8 or 1.1.1.1
This is how the log looks before export.

Over 17 months of my service term that’s approximately 3,387 outage incidents totaling 117+ hours of cumulative downtime.

This outage pattern has recurred thousands of times. It is consistent, predictable, and it follows an automated schedule.

My neighbor has the same problem. Different house. Different line from a different junction box. Same 125-second outages happening at the same times of day.

Minute marker clustering: 33% at :29, 28% at :44. This pattern is diagnostic of cron-based scheduling running automated tasks
18 incidents over 72 hours, all within 123-127 seconds (125.0±1.4s). This precision proves automated timeout, not random failure
Peak at noon (12:00), secondary clusters at early morning (3:00) and late night. Non-random distribution pattern

PING Uptime Log
2025-11-21T14:42:31-08:00 Warning dpinger exiting on signal 15
2025-11-21T07:01:34-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 21.4 ms RTTd: 14.8 ms Loss: 10.0 %)
2025-11-21T07:01:28-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 21.7 ms RTTd: 15.8 ms Loss: 20.0 %)
2025-11-21T06:59:33-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.1 ms RTTd: 1.7 ms Loss: 21.0 %)
2025-11-21T06:59:28-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.1 ms RTTd: 1.6 ms Loss: 12.0 %)
2025-11-21T00:01:33-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 20.5 ms RTTd: 2.7 ms Loss: 10.0 %)
2025-11-21T00:01:28-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 20.6 ms RTTd: 2.8 ms Loss: 20.0 %)
2025-11-20T23:59:35-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 20.1 ms RTTd: 3.1 ms Loss: 21.0 %)
2025-11-20T23:59:30-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 20.0 ms RTTd: 3.0 ms Loss: 12.0 %)
2025-11-20T15:01:37-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 21.3 ms RTTd: 3.9 ms Loss: 10.0 %)
2025-11-20T15:01:31-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 21.4 ms RTTd: 4.1 ms Loss: 20.0 %)
2025-11-20T14:59:36-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 21.0 ms RTTd: 3.9 ms Loss: 21.0 %)
2025-11-20T14:59:31-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 21.3 ms RTTd: 4.3 ms Loss: 12.0 %)
2025-11-20T13:46:40-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 20.4 ms RTTd: 2.9 ms Loss: 10.0 %)
2025-11-20T13:46:34-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 20.2 ms RTTd: 3.0 ms Loss: 20.0 %)
2025-11-20T13:44:38-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.9 ms RTTd: 1.7 ms Loss: 21.0 %)
2025-11-20T13:44:33-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.7 ms RTTd: 1.7 ms Loss: 12.0 %)
2025-11-20T12:46:37-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 19.3 ms RTTd: 1.2 ms Loss: 10.0 %)
2025-11-20T12:46:32-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 19.2 ms RTTd: 1.2 ms Loss: 20.0 %)
2025-11-20T12:44:39-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.2 ms RTTd: 0.9 ms Loss: 21.0 %)
2025-11-20T12:44:34-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.3 ms RTTd: 1.0 ms Loss: 12.0 %)
2025-11-20T05:16:33-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 19.5 ms RTTd: 1.4 ms Loss: 10.0 %)
2025-11-20T05:16:27-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 19.5 ms RTTd: 1.4 ms Loss: 20.0 %)
2025-11-20T05:14:33-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.4 ms RTTd: 1.2 ms Loss: 21.0 %)
2025-11-20T05:14:28-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.3 ms RTTd: 1.2 ms Loss: 12.0 %)
2025-11-20T03:31:34-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 18.9 ms RTTd: 1.3 ms Loss: 10.0 %)
2025-11-20T03:31:28-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 18.8 ms RTTd: 1.1 ms Loss: 20.0 %)
2025-11-20T03:29:32-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.3 ms RTTd: 1.6 ms Loss: 21.0 %)
2025-11-20T03:29:28-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.4 ms RTTd: 1.6 ms Loss: 14.0 %)
2025-11-19T20:01:32-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 18.9 ms RTTd: 1.2 ms Loss: 10.0 %)
2025-11-19T20:01:26-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 18.8 ms RTTd: 1.2 ms Loss: 20.0 %)
2025-11-19T19:59:34-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.2 ms RTTd: 2.2 ms Loss: 21.0 %)
2025-11-19T19:59:29-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.1 ms RTTd: 2.1 ms Loss: 12.0 %)
2025-11-19T16:31:36-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 20.2 ms RTTd: 2.7 ms Loss: 10.0 %)
2025-11-19T16:31:29-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 20.2 ms RTTd: 2.8 ms Loss: 20.0 %)
2025-11-19T16:29:35-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.6 ms RTTd: 2.1 ms Loss: 21.0 %)
2025-11-19T16:29:30-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.8 ms RTTd: 2.3 ms Loss: 12.0 %)
2025-11-19T13:31:35-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 17.7 ms RTTd: 2.5 ms Loss: 10.0 %)
2025-11-19T13:31:29-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 17.9 ms RTTd: 2.6 ms Loss: 20.0 %)
2025-11-19T13:29:38-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 16.7 ms RTTd: 2.0 ms Loss: 21.0 %)
2025-11-19T13:29:32-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 16.6 ms RTTd: 2.0 ms Loss: 12.0 %)
2025-11-19T10:31:39-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 19.6 ms RTTd: 1.4 ms Loss: 10.0 %)
2025-11-19T10:31:33-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 19.5 ms RTTd: 1.3 ms Loss: 20.0 %)
2025-11-19T10:29:39-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 18.9 ms RTTd: 1.2 ms Loss: 21.0 %)
2025-11-19T10:29:33-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.1 ms RTTd: 1.3 ms Loss: 12.0 %)
2025-11-19T03:46:32-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 19.6 ms RTTd: 2.6 ms Loss: 10.0 %)
2025-11-19T03:46:25-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 19.6 ms RTTd: 2.7 ms Loss: 20.0 %)
2025-11-19T03:44:33-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.4 ms RTTd: 1.2 ms Loss: 21.0 %)
2025-11-19T03:44:28-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.4 ms RTTd: 1.2 ms Loss: 12.0 %)
2025-11-18T22:31:36-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 19.9 ms RTTd: 2.6 ms Loss: 10.0 %)
2025-11-18T22:31:29-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 19.8 ms RTTd: 2.5 ms Loss: 20.0 %)
2025-11-18T22:29:34-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 20.1 ms RTTd: 2.5 ms Loss: 21.0 %)
2025-11-18T22:29:29-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 20.0 ms RTTd: 2.4 ms Loss: 12.0 %)
2025-11-18T12:19:41-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 21.1 ms RTTd: 4.2 ms Loss: 10.0 %)
2025-11-18T12:19:35-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 21.1 ms RTTd: 4.3 ms Loss: 20.0 %)
2025-11-18T12:17:42-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.5 ms RTTd: 1.7 ms Loss: 21.0 %)
2025-11-18T12:17:37-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.8 ms RTTd: 1.8 ms Loss: 12.0 %)
2025-11-18T12:16:37-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 19.3 ms RTTd: 1.6 ms Loss: 10.0 %)
2025-11-18T12:16:31-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 19.2 ms RTTd: 1.7 ms Loss: 20.0 %)
2025-11-18T12:14:38-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.1 ms RTTd: 1.2 ms Loss: 21.0 %)
2025-11-18T12:14:32-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.1 ms RTTd: 1.1 ms Loss: 12.0 %)
2025-11-18T09:31:37-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 19.4 ms RTTd: 1.0 ms Loss: 10.0 %)
2025-11-18T09:31:32-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 19.4 ms RTTd: 1.0 ms Loss: 20.0 %)
2025-11-18T09:29:38-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.6 ms RTTd: 1.3 ms Loss: 21.0 %)
2025-11-18T09:29:33-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.6 ms RTTd: 1.2 ms Loss: 12.0 %)
2025-11-18T07:46:33-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 21.1 ms RTTd: 15.0 ms Loss: 10.0 %)
2025-11-18T07:46:26-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 21.4 ms RTTd: 15.9 ms Loss: 20.0 %)
2025-11-18T07:44:32-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.7 ms RTTd: 2.1 ms Loss: 21.0 %)
2025-11-18T07:44:27-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.6 ms RTTd: 2.0 ms Loss: 12.0 %)
2025-11-18T02:46:34-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 19.0 ms RTTd: 1.5 ms Loss: 10.0 %)
2025-11-18T02:46:28-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 19.1 ms RTTd: 1.6 ms Loss: 20.0 %)
2025-11-18T02:44:33-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.0 ms RTTd: 1.0 ms Loss: 21.0 %)
2025-11-18T02:44:28-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.0 ms RTTd: 1.0 ms Loss: 12.0 %)
2025-11-17T23:01:33-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 18.6 ms RTTd: 0.9 ms Loss: 10.0 %)
2025-11-17T23:01:28-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 18.7 ms RTTd: 0.9 ms Loss: 20.0 %)
2025-11-17T22:59:35-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 18.8 ms RTTd: 1.0 ms Loss: 21.0 %)
2025-11-17T22:59:29-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 18.9 ms RTTd: 1.0 ms Loss: 12.0 %)
2025-11-17T17:01:35-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 20.5 ms RTTd: 3.3 ms Loss: 10.0 %)
2025-11-17T17:01:29-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 20.4 ms RTTd: 3.0 ms Loss: 20.0 %)
2025-11-17T16:59:36-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.4 ms RTTd: 1.5 ms Loss: 21.0 %)
2025-11-17T16:59:31-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.4 ms RTTd: 1.6 ms Loss: 12.0 %)
2025-11-17T13:31:36-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 20.1 ms RTTd: 3.3 ms Loss: 10.0 %)
2025-11-17T13:31:30-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 20.2 ms RTTd: 3.4 ms Loss: 20.0 %)
2025-11-17T13:29:37-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.3 ms RTTd: 1.1 ms Loss: 21.0 %)
2025-11-17T13:29:32-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.5 ms RTTd: 1.5 ms Loss: 12.0 %)
2025-11-17T12:46:37-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 19.0 ms RTTd: 3.4 ms Loss: 10.0 %)
2025-11-17T12:46:31-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 19.3 ms RTTd: 3.5 ms Loss: 20.0 %)
2025-11-17T12:44:40-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 17.8 ms RTTd: 3.1 ms Loss: 22.0 %)
2025-11-17T12:44:34-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 17.8 ms RTTd: 3.0 ms Loss: 12.0 %)
2025-11-17T02:46:33-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> none RTT: 19.8 ms RTTd: 2.6 ms Loss: 10.0 %)
2025-11-17T02:46:27-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> loss RTT: 19.8 ms RTTd: 2.7 ms Loss: 20.0 %)
2025-11-17T02:44:32-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: loss -> down RTT: 19.0 ms RTTd: 0.9 ms Loss: 21.0 %)
2025-11-17T02:44:28-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: none -> loss RTT: 19.2 ms RTTd: 1.5 ms Loss: 12.0 %)
2025-11-17T01:15:08-08:00 Notice dpinger MONITOR: WAN_GW (Addr: 8.8.8.8 Alarm: down -> none RTT: 19.0 ms RTTd: 1.1 ms Loss: 0.0 %)
2025-11-17T01:14:57-08:00 Warning dpinger send_interval 1000ms loss_interval 4000ms time_period 60000ms report_interval 0ms data_len 1 alert_interval 1000ms latency_alarm 0ms loss_alarm 0% alarm_hold 10000ms dest_addr 8.8.8.8 bind_addr 24.2.60.72 identifier "WAN_GW "
DOCSIS Event Log from MODEM (MAC Obfuscated)

00:00:36

Fri Nov 21 2025 Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) SYNC Timing Synchronization failure – Failed to acquire QAM/QPSK symbol timing;;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:00:00:00:00:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

07:00:37

Fri Nov 21 2025 Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) SYNC Timing Synchronization failure – Failed to acquire QAM/QPSK symbol timing;;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:00:00:00:00:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

14:48:44

Fri Nov 21 2025 Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) SYNC Timing Synchronization failure – Failed to acquire QAM/QPSK symbol timing;;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:00:00:00:00:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

15:30:40

Fri Nov 21 2025 Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) SYNC Timing Synchronization failure – Failed to acquire QAM/QPSK symbol timing;;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:00:00:00:00:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

03:00:36

Sat Nov 22 2025 Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) SYNC Timing Synchronization failure – Failed to acquire QAM/QPSK symbol timing;;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:00:00:00:00:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

04:00:39

Sat Nov 22 2025 Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) SYNC Timing Synchronization failure – Failed to acquire QAM/QPSK symbol timing;;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:00:00:00:00:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

11:00:30

Sat Nov 22 2025 Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

11:00:30

Sat Nov 22 2025 Critical (3) Started Unicast Maintenance Ranging – No Response received – T3 time-out;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

11:00:35

Sat Nov 22 2025 Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) SYNC Timing Synchronization failure – Failed to acquire QAM/QPSK symbol timing;;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:00:00:00:00:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

11:45:35

Sat Nov 22 2025 Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) SYNC Timing Synchronization failure – Failed to acquire QAM/QPSK symbol timing;;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:00:00:00:00:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

13:15:31

Sat Nov 22 2025 Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) SYNC Timing Synchronization failure – Failed to acquire QAM/QPSK symbol timing;;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:00:00:00:00:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

Time Not Established

Notice (6) Honoring MDD; IP provisioning mode = IPv6

18:15:32

Sat Nov 22 2025 Notice (6) DS profile assignment change. DS Chan ID: 32; Previous Profile: ; New Profile: 1 2 3.;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

18:15:39

Sat Nov 22 2025 Critical (3) UCD invalid or channel unusable;CM-MAC=00:XX:XX:XX:XX:ac;CMTS-MAC=00:XX:XX:XX:XX:00;CM-QOS=1.1;CM-VER=3.1;

## My Attempts to Fix It

I called support. Multiple times. They blamed my WiFi (I’m hardwired). They blamed my modem (an Xfinity Approved MB8611 that worked without fault on Wave Broadband and Spectrum). They blamed my router (I tested with multiple devices). They sent a subcontracted technician. Then another subcontracted technician. Then a subcontracted crew. The crew ran a new coax line and grounded it to a water pipe that turns into PVC when it enters the ground (this doesn’t ground anything). Then they sent an Xfinity technician to look at the line.

The problem never changed. The only thing that changed is my download speed dropped from advertised 1200Mbps to <500Mbps.

For my trouble of reporting a network outage I lost 700Mbps in speed. This is a 1200Mbps plan.

I escalated to retention. They offered me nothing. I provided detailed technical documentation showing the exact pattern of the outages, the minute markers they occur at, the exact duration every single time. They didn’t understand it. They couldn’t escalate it.

I was transferred to technical support. The person did not care and put me on speaker phone with so much background noise I couldn’t hear myself think. I imagine he was rolling his eyes while trying his utmost to care less.

## My Neighbor’s Attempts to Fix It

He called Xfinity about his TV cutting out repeatedly. The technician told him his UPS grounding his coax cable was causing the problem. So he ungrounded the cable, pocketed the spare cable, and my neighbor kept having the same issues.

## What I Found

Just in the last 72 hours I have documented 20 consecutive outages using OPNSense’s built in gateway uptime monitor. Here’s what they show:

Every single outage lasted 124.8 ± 1.3 seconds.That’s not random hardware failure. That’s a timeout value hardcoded into something in Xfinity’s infrastructure.

The outages cluster at specific minute markers.35% start at minute :44. 35% start at minute :29. This is scheduled automation. This is likely a cron job or automated task running at those exact times every hour.

The outages peak at specific hours.Most happen between noon and 1 PM. Others cluster in early morning around 2-3 AM. This is not random.

This is an infrastructure problem on Xfinity’s network. Not on my end. Not on my neighbor’s end. Upstream. Somewhere on their equipment something is failing for exactly 125 seconds multiple times per day.

I have the data. I have the patterns. I have another customer (my neighbor) on a different line experiencing the exact same thing.

Xfinity has all this information. They know about the problem. They just won’t investigate it.

## Why They Won’t Fix It

1. Support can’t understand technical data.They follow scripts. When I attempted to explain monitoring logs they had no framework for discussing it. They blamed my equipment because that’s what they’re trained to do.
2. Nobody has authority to escalate.Retention transferred me to tech support. Tech support couldn’t care nor help. They dug up my yard and placed a new line which did nothing to solve the problem. Nobody would actually order an investigation into the upstream infrastructure.
3. There’s no pressure to fix it.Xfinity is the only gigabit provider in this area. No competition. No alternatives. I can’t leave. So they don’t have to care.
4. A 2-minute outage every few hours is “tolerable.”It’s annoying enough to frustrate customers but not enough to make them quit (since they have nowhere else to go). It’s cheap to ignore compared to actually investigating and fixing it.

There’s Also a Security Problem

About half of the Xfinity junction boxes in my neighborhood are unlocked or broken. Anyone can walk up and disconnect whomever they want.

If your home security system is on Xfinity with no wireless backup, someone can just walk to the street and physically disconnect your internet, rob your house, and your security system won’t notify you.

## I’m Out of Options

I’ve done everything I can do as a customer:

* Documented the problem professionally
* Escalated through all available channels
* Provided technical evidence
* Been ignored at every level

The problem is real. My neighbor confirms it. Everyone downstream of whatever is broken on their infrastructure probably has it too.

I can’t fix this. Only Xfinity can. And they won’t.

So I’m publishing this hoping someone with actual authority, perhaps someone at a regulatory agency, someone at a news outlet, someone who has power over Xfinity sees this and decides to actually investigate.

Because I’m out of options. My neighbors are out of options. And Xfinity’s counting on us staying out of options. Because this is the reality of my neighborhood (source):

As you can, see there is zero choice.

If you’re in Sacramento County and have Xfinity internet, check two things:

1. Walk to your junction box. Is it locked? If not, you have a physical security problem.

2. Look at where your cable grounds. Does it go to your electrical panel? Or to a water pipe? If it’s a water pipe or PVC, that’s wrong.

3. Have you noticed your connection drop briefly multiple times a day? Same times of day? If you see a pattern, document it. You might have the same problem.

If you want to report this:

* FCC:https://consumercomplaints.fcc.gov/
* Sac County Cable Television Commission:https://sacmetrocable.saccounty.gov/SMCTC/Pages/CableComplaints.aspx
* California PUC:https://www.cpuc.ca.gov/

### Related

## You May Also Like…

#### AboutThe Sacramento Bear

The Sacramento Bear is an independent newspaper engaged in first amendment activities and leveraging the freedom of the press to express facts and opinions about various matters.

Previous Post:
Subaru’s Octane Coverup: How a Major Automaker Failed to Fix a Systemic Engine Problem

## Reader Interactions

### Trackbacks

1. […] Source link […]Loading...Reply
2. […] 원본 기사 보기 […]Loading...Reply
3. […] 원본 기사 보기 […]Loading...Reply
4. […] Read More […]Loading...Reply
5. […] 网站: sacbear.com HN评论: […]Loading...Reply

### Leave a ReplyCancel reply
