---
title: "MQTT Doesn't Have Message Queues. Inside the 2-Byte Protocol Powering Modern IoT. - DEV Community"
url: https://dev.to/smtahosin/mqtt-doesnt-have-message-queues-inside-the-2-byte-protocol-powering-modern-iot-161
date: 2026-10-28
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-29T21:01:21.921562
---

# MQTT Doesn't Have Message Queues. Inside the 2-Byte Protocol Powering Modern IoT. - DEV Community

# MQTT Doesn't Have Message Queues – Key Takeaways

## Origin and Ubiquity
- Designed in 1999 by Andy Stanford‑Clark and Arlen Nipper for low‑bandwidth, satellite‑linked oil‑pipeline sensors.
- Chosen for its ultra‑lean binary wire format, avoiding the overhead of HTTP.
- Today powers:
  - Real‑time telemetry from electric vehicles.
  - Smart home devices (lights, sensors) via Home Assistant and Zigbee.
  - Industrial SCADA and robotics systems.
  - Mobile push notifications (e.g., Facebook Messenger) to conserve battery.

## Core Misconception
- Despite the “MQ” in its name, MQTT does **not** provide FIFO message queues like RabbitMQ or Kafka.
- If a subscriber is offline without a persistent session, published messages are discarded.

## What MQTT Really Is
- An ultra‑compact, binary‑framed Publish/Subscribe event router.
- Fixed header can be as small as 2 bytes, enabling long‑life, battery‑powered devices.

## Architecture Overview
- **Publishers** send a PUBLISH packet to a **broker** (e.g., EMQX, Mosquitto, HiveMQ).
- **Broker** immediately forwards the packet to all currently subscribed clients.
- If no clients are subscribed, the broker drops the message.
- No default storage; the system is stateless unless a persistent session is used.

## Spatial Decoupling
- Publishers have no knowledge of subscriber identities, locations, or counts.
- Sensors publish to a topic and return to sleep, while brokers handle routing.

## Persistent Session Exception
- When a client connects with `CleanSession=false` (MQTT 3.1.1) or `CleanStart=false` plus a Session Expiry Interval (MQTT 5.0):
  - The broker buffers unacknowledged QoS 1 and QoS 2 messages for that client ID.
  - The topic itself remains a stateless broadcast channel.

## 2‑Byte Fixed Header Format
- **Byte 1**: Packet Type (4 bits) + DUP flag (1 bit) + QoS level (2 bits) + RETAIN flag (1 bit).
  - Example packet types: CONNECT, CONNACK, PUBLISH, PUBACK, PINGREQ, PINGRESP, DISCONNECT.
- **Byte 2+**: Variable Byte Integer encoding the remaining length.
  - Uses 7 bits per byte with the MSB as a continuation flag.
  - Supports payloads up to 268,435,455 bytes (≈256 MiB) with 1–4 length bytes.

## QoS Levels and Trade‑offs
- **QoS 0 – At Most Once**: Fire‑and‑forget, no acknowledgment, minimal overhead.
- **QoS 1 – At Least Once**: Guarantees delivery but may result in duplicates; incurs extra packets for acknowledgment.
- **QoS 2 – Exactly Once**: Full handshake to avoid duplicates; highest bandwidth and battery cost.

## Efficiency Example
- A temperature reading with QoS 0 results in a two‑byte header: `0x30 0x12` (PUBLISH, QoS 0, no retain, 18 bytes of topic + payload). No ASCII parsing, pure binary efficiency.