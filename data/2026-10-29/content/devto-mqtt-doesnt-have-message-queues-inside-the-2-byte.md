---
title: MQTT Doesn't Have Message Queues. Inside the 2-Byte Protocol Powering Modern IoT. - DEV Community
url: https://dev.to/smtahosin/mqtt-doesnt-have-message-queues-inside-the-2-byte-protocol-powering-modern-iot-161
site_name: devto
content_file: devto-mqtt-doesnt-have-message-queues-inside-the-2-byte
fetched_at: '2026-10-29T21:00:00.632836'
original_url: https://dev.to/smtahosin/mqtt-doesnt-have-message-queues-inside-the-2-byte-protocol-powering-modern-iot-161
author: S M Tahosin
date: '2026-10-28'
description: A visual, 10-minute architectural deep dive into MQTT. Learn how the 2-byte binary wire protocol, QoS 0/1/2 handshakes, topic trees, Last Will and Testament, and MQTT v5 Shared Subscriptions actually deliver IoT telemetry under the hood. Tagged with iot, networking, architecture, mqtt.
tags: '#iot, #networking, #architecture, #mqtt'
---

Avoid abusing QoS 2 to fake queues

In 1999, two engineers named Andy Stanford-Clark and Arlen Nipper faced a brutal engineering problem:

They needed to monitor crude oil pipelines stretching across hundreds of miles of remote desert in the American Southwest.

The only communication channel available was fragile, low-bandwidth satellite links that billed by the kilobyte. The remote battery-powered sensors had tiny 8-bit microcontrollers and minuscule memory buffers.

If they had used HTTP, the repetitive plain-text headers alone would have burned thousands of dollars in satellite bandwidth every day while draining the device batteries within a week.

To solve that crisis, they designed a lean binary wire protocol and named it:

MQTT (Message Queuing Telemetry Transport).

Fast forward to today: MQTT powers hundreds of millions of connected devices across the planet:

* Every electric vehicle streaming real-time battery and GPS telemetry to cloud fleets.
* Every smart lightbulb and sensor running through Home Assistant and Zigbee networks.
* Industrial robotics and manufacturing SCADA assembly lines.
* Even mobile messaging giants like Facebook Messenger, which famously ported mobile push notifications to MQTT to save battery on low-end cellular phones.

Yet despite its global ubiquity, almost every software engineer who encounters MQTT for the first time carries one massive, fundamental misunderstanding:

MQTT does not actually have message queues.

Despite the lettersMQin its name, MQTT does not buffer messages in FIFO queues like RabbitMQ, nor does it store distributed partition logs like Apache Kafka.

If a subscriber goes offline without a persistent session, incoming messages simply vanish into thin air.

So what is MQTT, really?

It is an ultra-compact, binary-framedPublish/Subscribe event routerthat can transmit a live telemetry packet with a fixed header as small as2 bytes.

To understand why MQTT dominates the connected world, you have to look beneath high-level client libraries and inspect how the binary wire protocol, delivery handshakes, and broker routing actually work under the hood.

Here is the complete mechanics of MQTT.

## The Big Misconception: Why MQTT Has No Queues

When software engineers hear "Message Queuing", they naturally picture tools like RabbitMQ, ActiveMQ, or Amazon SQS:

* A publisher pushes a task to a named queue.
* The queue holds the message in persistent memory.
* A consumer comes online minutes later, pulls the task from the queue, processes it, and acknowledges receipt.

MQTT operates on a completely different paradigm:Space, Time, and Synchronization Decoupling.

[ Sensor / Publisher ] ──> PUBLISH "factory/temp" ──> [ MQTT Broker ] ──> Instant Push ──> [ Subscribers ]
 │
 (If 0 subscribers are online:
 Message is dropped immediately!)

Enter fullscreen mode

Exit fullscreen mode

### The Spatial Decoupling

In MQTT, publishers and subscribers never know about each other.

A temperature sensor publishing readings tofactory/temphas zero knowledge of which services exist, how many dashboards are open, or what IP addresses they live at. It sends its packet to an intermediary called theMQTT Broker(such as EMQX, Mosquitto, or HiveMQ) and immediately returns to sleep.

### The Missing Queue

Here is why it is not a queue:

In MQTT, messages are delivered to topics, not to queues.

When a broker receives aPUBLISHpacket:

1. It inspects its in-memory subscription tree to see who is currently listening to that topic.
2. If three clients are subscribed, it immediately clones and forwards the packet to all three clients over their open TCP connections.
3. If zero clients are subscribed, the broker discards the message immediately.

There is no default storage. There is no queue waiting for a subscriber to boot up tomorrow.

The only exception is when a client connects with aPersistent Session(CleanSession=falsein MQTT 3.1.1, orCleanStart=falsewith aSession Expiry Intervalin MQTT 5.0).

In that specific scenario, the broker buffers unacknowledged QoS 1 and QoS 2 messages specifically for that knownClientId. But the topic itself remains a stateless broadcast channel, not an independent queue.

## Anatomy of the 2-Byte Fixed Header Wire Format

Why is MQTT so fast, and why can an IoT sensor run on a single coin-cell battery for five years?

The secret is the binary wire layout.

In HTTP/1.1, sending a single number requires hundreds of bytes of plain-text ASCII:

POST
 
/telemetry
 
HTTP
/
1.1

Host
:
 
api.iot.com

Content-Type
:
 
application/json

Content-Length
:
 
18

User-Agent
:
 
Mozilla/5.0...

{
"temperature"
:
24
}

Enter fullscreen mode

Exit fullscreen mode

In MQTT, the fixed header requires as little as2 bytes.

Let us inspect the exact bit layout of an MQTT packet wire frame:

### Byte 1: Packet Type & Control Flags

Byte 1 is packed down to individual bits:

Bit: 7 6 5 4 │ 3 │ 2 1 │ 0
 [ Packet Type ] │ DUP │ [ QoS ] │ RETAIN

Enter fullscreen mode

Exit fullscreen mode

* Bits 7 to 4 (Packet Type):4 bits give 16 possible control packet types:0001(1):CONNECT(Client requests connection)0010(2):CONNACK(Broker connection acknowledgement)0011(3):PUBLISH(Publish message)0100(4):PUBACK(Publish acknowledgement for QoS 1)1100(12):PINGREQ(Heartbeat ping request)1101(13):PINGRESP(Heartbeat ping response)1110(14):DISCONNECT(Graceful client disconnect)
* 0001(1):CONNECT(Client requests connection)
* 0010(2):CONNACK(Broker connection acknowledgement)
* 0011(3):PUBLISH(Publish message)
* 0100(4):PUBACK(Publish acknowledgement for QoS 1)
* 1100(12):PINGREQ(Heartbeat ping request)
* 1101(13):PINGRESP(Heartbeat ping response)
* 1110(14):DISCONNECT(Graceful client disconnect)
* Bit 3 (DUP Flag):Set to1when the client or broker is re-attempting delivery of an unacknowledged QoS 1 or QoS 2 packet.
* Bits 2 and 1 (QoS Level):00= Quality of Service 0 (At most once)01= Quality of Service 1 (At least once)10= Quality of Service 2 (Exactly once)
* 00= Quality of Service 0 (At most once)
* 01= Quality of Service 1 (At least once)
* 10= Quality of Service 2 (Exactly once)
* Bit 0 (RETAIN Flag):If set to1, the broker saves this message as the "last known good value" for this topic. Any new subscriber that connects in the future will receive this message immediately upon subscription.

### Byte 2+: The Variable Byte Remaining Length

How does MQTT express the size of the packet without wasting multiple bytes on every small sensor reading?

It uses an ingenious encoding called theVariable Byte Integer:

* Each byte uses7 bitsto encode the numeric length value (0to127).
* The 8th bit (Most Significant Bit, MSB) is theContinuation Bit.
* If the MSB is0, decoding stops immediately.
* If the MSB is1, it signals that the next byte contains additional length data.

This gives MQTT an astonishing dynamic range:

* For payloads under 128 bytes, the length field takes1 single byte!
* For larger payloads, it expands up to 4 bytes, supporting payloads up to268,435,455 bytes (256 MB)!

When a microcontroller sends a temperature reading with QoS 0, the total protocol overhead is literally two hexadecimal bytes:

0x30 0x12

Enter fullscreen mode

Exit fullscreen mode

0x30means: Packet Type 3 (PUBLISH), QoS 0, no retain.0x12means: 18 bytes of remaining topic and payload data follow.

Zero ASCII parsing. Zero text string overhead. Pure binary efficiency.

## The 3 Quality of Service (QoS) Guarantees

Because IoT devices operate over noisy radio links, cellular networks with tunnel dead-zones, and unstable satellite connections, MQTT provides three distinct delivery guarantees calledQuality of Service (QoS)levels.

Many engineers assume that higher QoS is always better. In reality, each QoS level represents a distinct engineering tradeoff between network bandwidth, battery consumption, and delivery certainty.

### QoS 0: At Most Once (Fire and Forget)

[ Sender ] ─── PUBLISH ───> [ Receiver ]

Enter fullscreen mode

Exit fullscreen mode

QoS 0 is the simplest and fastest delivery mode:

1. The sender transmits a singlePUBLISHpacket.
2. The sender does not request an acknowledgement.
3. No packet ID is allocated.
4. No retry timer is started.

If the cellular connection drops the instant the packet leaves the radio antenna, the message is lost forever.

When to use QoS 0:High-frequency, ephemeral telemetry. If a weather station publishes wind speed every 2 seconds, losing one reading is irrelevant because a fresh reading will arrive in 2,000 milliseconds. Paying for acknowledgements would only drain the battery.

### QoS 1: At Least Once (Acknowledged Delivery)

[ Sender ] ─── PUBLISH (PacketId: 10) ───> [ Receiver ]
[ Sender ] <─── PUBACK (PacketId: 10) ─── [ Receiver ]

Enter fullscreen mode

Exit fullscreen mode

QoS 1 guarantees that the receiver gets the message at least once, but introduces the risk ofduplicate messages:

1. The sender assigns a unique 16-bitPacket Identifierto thePUBLISHframe.
2. The sender stores the packet in local memory and starts an acknowledgement timer.
3. The receiver accepts the packet, forwards it to its application logic, and returns aPUBACKcontaining the samePacketId.
4. When the sender receivesPUBACK, it deletes the packet from memory.

The Duplicate Trap:What happens if the receiver receives thePUBLISHpacket, but the network drops right before thePUBACKreturns to the sender?

The sender's timer expires. It re-transmits the packet with theDUPflag set to1. The receiver gets the message a second time!

Crucial Engineering Rule:If you use QoS 1, your backend consumermust be idempotent. Processing the exact same event twice must not corrupt your database or charge a credit card twice.

### QoS 2: Exactly Once (The 4-Way Handshake)

[ Sender ] ─── 1. PUBLISH (PacketId: 42) ───> [ Receiver ]
[ Sender ] <─── 2. PUBREC (PacketId: 42) ─── [ Receiver ]
[ Sender ] ─── 3. PUBREL (PacketId: 42) ───> [ Receiver ]
[ Sender ] <─── 4. PUBCOMP (PacketId: 42) ─── [ Receiver ]

Enter fullscreen mode

Exit fullscreen mode

QoS 2 is the most sophisticated delivery guarantee in network protocols: it ensures that the message is receivedexactly once, with zero loss and zero duplicates.

It accomplishes this via a coordinated two-step state machine:

1. PUBLISH:Sender transmits packet withPacketId: 42.
2. PUBREC (Publish Received):Receiver cachesPacketId: 42in its internal state, acknowledging receipt without delivering it to the application yet.
3. PUBREL (Publish Release):Sender receivesPUBRECand tells the receiver:"I know you got it. You may now release and process the message."
4. PUBCOMP (Publish Complete):Receiver processes the message, deletes thePacketIdfrom its cache, and sendsPUBCOMP. Both sides finalize the transaction.

QoS 2 eliminates duplicate delivery completely, but requirestwo complete round-trips (four packets).

When to use QoS 2:Mission-critical commands where duplicate execution is catastrophic: opening a motorized security gate, firing a medical alarm, or decrementing a physical warehouse inventory counter.

## Topic Trees and Dynamic Wildcard Routing

MQTT does not use fixed queue names. It routes messages using hierarchical, slash-separated strings calledTopic Trees:

factory / building1 / line2 / motor4 / temperature

Enter fullscreen mode

Exit fullscreen mode

This topic tree forms a virtual namespace that clients can slice and filter dynamically.

### How Brokers Route Topics in Memory

A production MQTT broker handling 500,000 devices cannot execute database queries to determine who gets each message.

Instead, brokers store topic subscriptions in an in-memoryTrie (Prefix Tree) Data Structure.

Each forward slash (/) creates a child node in the tree. When a packet arrives forfactory/building1/line2/motor4/temperature, the broker traverses the Trie nodes in nanoseconds, identifying every matching client socket directly.

### The Two Wildcards

When subscribing to topics, clients can use two special wildcard characters:

#### 1. Single-Level Wildcard:+

The plus symbol (+) matchesexactly one levelin the topic tree.

For example, this subscription:

factory/+/line2/motor4/temperature

Enter fullscreen mode

Exit fullscreen mode

Matches:

* factory/building1/line2/motor4/temperature
* factory/building2/line2/motor4/temperature

It willnotmatchfactory/building1/subzone/line2/motor4/temperaturebecause that spans two levels.

#### 2. Multi-Level Wildcard:#

The hash symbol (#) matchesall remaining sub-levelsin the hierarchy. It must always appear as the very last character of a topic filter.

For example:

factory/building1/#

Enter fullscreen mode

Exit fullscreen mode

This single subscription captures every sensor reading, motor status, temperature, error code, and diagnostic event generated insidebuilding1.

### Retained Messages: The State Latch

In standard Pub/Sub, if a dashboard client boots up at 10:00 AM, and a smart thermostat only publishes its temperature when the temperature changes (say, at 9:55 AM and 10:30 AM), the dashboard would show blank data for 30 minutes!

This is whereRetained Messagessolve the problem.

When a publisher sends a message with theRETAIN=1flag:

1. The broker delivers the message to all current subscribers.
2. The brokersaves that exact message on the topic node in memory.
3. Whenever a new subscriber registers for that topic in the future, the brokerimmediately delivers the retained messageas an initial state snapshot.

Retained messages turn an ephemeral streaming protocol into an instant state discovery engine.

## Last Will and Testament (LWT) & KeepAlive Heartbeats

In a world of wired web servers, when a client closes a connection, the operating system gracefully sends a TCPFINpacket. The server knows immediately that the client disconnected.

In the IoT world, devices rarely disconnect gracefully:

* A vehicle drives into an underground concrete parking garage, losing cell signal instantly.
* A battery runs completely dry in a field sensor.
* A construction worker accidentally severs an Ethernet cable.

In all of those scenarios,no TCP FIN packet is ever sent.

As far as the operating system kernel is concerned, the TCP socket is still open! Without an active probe, the server might wait for hours before TCP keepalive timers realize the socket is dead.

MQTT solves this with a two-part reliability mechanism:KeepAlive HeartbeatsandLast Will and Testament (LWT).

### Step 1: The Will Registration

When an IoT device first establishes a connection, it includes its "Last Will" inside the initialCONNECTpacket:

* Will Topic:devices/sensor-42/status
* Will Payload:{"state": "offline", "reason": "unexpected_disconnect"}
* Will QoS:1
* Will Retain:true

The broker acknowledges the connection withCONNACKand quietly stores the Last Will in memory. As long as the device is healthy, the broker does nothing with this will.

### Step 2: The KeepAlive Ping Cycle

The device specifies aKeepAliveinterval in seconds (for example,60).

If the device has not published any telemetry within 60 seconds, it sends a tiny2-bytePINGREQpacket(0xC0 0x00).

The broker immediately responds with a2-bytePINGRESPpacket(0xD0 0x00).

This 2-byte exchange resets the timer while consuming virtually zero cellular data and keeping stateful NAT firewall ports open across cellular carriers.

### Step 3: Sudden Death Detection

If the broker does not receive any packet from the device for1.5 times the KeepAlive duration(in this case, 90 seconds):

1. The broker assumes the device is physically dead.
2. The broker forcibly closes the underlying TCP socket.
3. The broker automatically publishes the stored Last Will and Testament todevices/sensor-42/status.

Every monitoring dashboard, mobile app, and backend alert system listening to that topic instantly receives the notification:"state": "offline".

The dead device did not have to send an alert; the broker executed its pre-registered will on its behalf.

And if the device disconnects cleanly on purpose? It sends aDISCONNECTpacket (0xE0 0x00). The broker deletes the Last Will from memory without publishing it.

## MQTT v5: Shared Subscriptions and Modern Cloud Scaling

For many years, the standard version of MQTT was v3.1.1. While it conquered embedded hardware, modern cloud architectures exposed a major challenge:

How do you load-balance an MQTT topic across a cluster of backend microservices?

In MQTT 3.1.1, if three backend worker instances subscribed totelemetry/#, the broker would send a copy of every message toall three workers.

If 100,000 connected cars were streaming GPS coordinates, every backend worker had to process 100,000 streams simultaneously, destroying horizontal scalability.

The OASIS committee solved this inMQTT version 5.0by introducingShared Subscriptions.

### How Shared Subscriptions Work

Shared subscriptions bring the concept ofKafka Consumer Groupsdirectly into native MQTT.

Instead of subscribing to the raw topic, backend microservices subscribe using a reserved prefix:

$share / <Group-Name> / <Topic-Filter>

Enter fullscreen mode

Exit fullscreen mode

For example:

$share/telemetry-processors/vehicles/+/gps

Enter fullscreen mode

Exit fullscreen mode

When three backend instances connect with that shared subscription:

1. The broker recognizes the$share/telemetry-processorsprefix.
2. It groups the three backend connections into a single logical consumer pool.
3. When incoming GPS packets arrive from vehicles, the brokerround-robins or load-balances each packet to only ONE worker in the group!

If Worker A is busy, Message 2 goes to Worker B, and Message 3 goes to Worker C.

If traffic surges from 1,000 cars to 1,000,000 cars, you simply spin up ten more container instances of your backend service. The broker distributes the telemetry load across the cluster without needing an external Kafka or RabbitMQ ingestion layer in between!

## Architectural Comparison: Choosing the Right Tool

To see where MQTT fits into modern distributed systems, compare it directly against the other major protocols:

Feature

MQTT

HTTP / REST

WebSockets

Apache Kafka

Primary Paradigm

Pub/Sub Event Broker

Request / Response

Bidirectional Stream

Distributed Commit Log

Header Overhead

2 Bytes minimum

500 to 2,000+ Bytes

2 to 14 Bytes

Configurable / Batch

Transport Protocol

TCP / TLS / WebSockets

TCP / TLS (HTTP/2, 3)

TCP / TLS

TCP / TLS

Device Constraint

Extreme (8-bit MCUs)

Poor (requires HTTP stack)

Moderate

None (heavy cloud servers)

Delivery Guarantees

QoS 0, 1, 2

Application level

None (raw TCP)

At least once / Transactions

Message Queuing

None (Ephemeral)

None

None

Persistent Distributed Log

Dead Device Detection

Native LWT (Last Will)

Health checks only

Socket heartbeat

Heartbeat timeouts

Best Used For

Telemetry, smart devices, fleet IoT

CRUD APIs, public web

Browser UI live updates

Big data analytics, event replay

## The Takeaway: The Elegance of Restraint

MQTT is a masterclass in software engineering restraint.

In an industry that constantly adds layers of JSON, GraphQL, and microservice complexity, MQTT succeeded by doing the opposite:

1. It stripped headers down to the bare metal.A 2-byte header ensures that battery and bandwidth are never wasted on protocol bureaucracy.
2. It decoupled publishers from consumers entirely.Devices never know who is listening, allowing systems to scale from one subscriber to a million without touching the edge firmware.
3. It embraced network failure as a first-class reality.Through QoS handshakes and Last Will and Testament, it provides rock-solid reliability over the most unstable physical channels on Earth.

When you look at modern IoT architectures, the biggest mistake is treating MQTT like a simple HTTP replacement or assuming it will manage durable message queues on its own.

Understanding the binary framing, the QoS state machines, and the broker routing tree transforms MQTT from a mysterious black box into one of the most powerful distributed tools in your engineering arsenal.

Have you worked with MQTT in production smart home devices, vehicle tracking, or industrial telemetry? What was the biggest architectural hurdle you faced when bridging low-bandwidth edge MQTT streams into high-throughput cloud databases?

References & Technical Standards:

* OASIS Standard: MQTT Version 5.0 Specification
* OASIS Standard: MQTT Version 3.1.1 Specification
* Andy Stanford-Clark & Arlen Nipper: The Origin and History of MQTT
* HiveMQ Architecture Guides: MQTT Essentials & QoS Internals
* EMQX Distributed Broker Documentation: In-Memory Topic Tries & Shared Subscriptions

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse