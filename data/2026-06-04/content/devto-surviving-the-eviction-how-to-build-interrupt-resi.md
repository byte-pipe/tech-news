---
title: 'Surviving the eviction: How to build interrupt-resilient AI workloads on GKE - DEV Community'
url: https://dev.to/googlecloud/surviving-the-eviction-how-to-build-interrupt-resilient-ai-workloads-on-gke-5581
site_name: devto
content_file: devto-surviving-the-eviction-how-to-build-interrupt-resi
fetched_at: '2026-06-04T19:44:42.545313'
original_url: https://dev.to/googlecloud/surviving-the-eviction-how-to-build-interrupt-resilient-ai-workloads-on-gke-5581
author: Olivier Bourgeois
date: '2026-06-02'
description: Learn strategies for building interrupt-resilient AI workloads on Google Kubernetes Engine (GKE). Tagged with kubernetes, ai, gke, googlecloud.
tags: '#kubernetes, #ai, #gke, #googlecloud'
---

You did everything right. You containerized your massive model training job, deployed it to Google Kubernetes Engine (GKE), and cleverly routed it to a Spot VM node pool to save up to 90% on compute costs.

Everything is humming along perfectly for 38 hours. Then, a priority on-demand customer needs capacity, Google Cloud reclaims your underlying Spot VM, and your node vanishes.

Whether you are using preemptibleSpot VMsto save money, or leveraging theDynamic Workload Scheduler (DWS)to queue for scarce GPUs, you are building on top of ephemeral compute. The hardwarewilleventually be taken away. To successfully run critical AI workloads on un-committed capacity, your application architecture must assume failure is a given.

Here is a practical guide to building interruptible workloads on GKE.

## 1. Trap the warning

When Google Cloud reclaims a Spot VM, it doesn't just pull the power cord immediately. It sends anACPI signalto the underlying node to begin a power off cycle. Kubernetes intercepts this and translates it into a SIGTERM signal sent directly to your running containers.

You have agrace period(up to 15 seconds for non-system pods) between that SIGTERM and the fatal SIGKILL.

Your application must explicitly listen for this signal. When caught, your code should immediately stop accepting new batches, finish its current loop, flush any in-memory data to disk, and exit with a 0 (success) status.

Here is a simple example on how to catch this signal in Python:

import
 
signal

import
 
sys

import
 
time

def
 
handle_sigterm
(
signum
,
 
frame
):

 
print
(
"
Received SIGTERM. Initiating graceful shutdown...
"
)

 
# 1. Stop processing new data

 
# 2. Flush memory to persistent storage

 
# 3. Save final checkpoint

 
print
(
"
State saved. Exiting cleanly.
"
)

 
sys
.
exit
(
0
)

# Register the signal handler

signal
.
signal
(
signal
.
SIGTERM
,
 
handle_sigterm
)

# Your main training loop

print
(
"
Starting training loop...
"
)

while
 
True
:

 
# Train model...

 
time
.
sleep
(
1
)
 

Enter fullscreen mode

Exit fullscreen mode

## 2. Externalize your checkpoints

If your container dies, everything inside its local filesystem dies with it. To survive an interruption, you must periodically save your progress (model weights, optimizer states, epoch counters, etc.) to an external storage location.

Cloud Storage (GCS)is a common solution for this on Google Cloud.

* Save frequently:Decide on a checkpointing interval that balances the cost of lost work against the overhead of writing to storage. Saving every epoch or every few thousand steps is common, but this can vary based on your needs.
* Keep it local:Ensure your GCS buckets are in the same region as your GKE cluster (e.g., us-central1) to minimize latency and avoid outbound data transfer fees.
* Resume, don't restart:The first thing your container's startup script should do is to check for that GCS bucket. If a checkpoint exists in the bucket, load it and resume from that exact step.

## 3. Design for Idempotency

"Idempotency" is a fancy way of saying that doing something twice yields the same result as doing it once.

Imagine a batch inference job that reads an image, processes it, and writes the result to a database. If your pod is preempted millisecondsafterwriting to the database butbeforeit can mark the task as complete, the rescheduled pod will likely process that image again.

If your database blindly inserts new rows, you now have unintentional, duplicate data.

To build an idempotent pipeline:

* Use UPSERT (update or insert) operations in your database based on a unique identifier (like an image ID).
* Check if a record already exists before spending expensive GPU cycles processing it.

## 4. Decouple work queues for batch processing

If you are running a massive batch processing or inference job across thousands of files, do not write a monolithic Python script that iterates through a static CSV list. If the node dies at row 5,000, managing the state of where to restart is a nightmare.

Instead, decouple the workload:

1. Publish the work:Break your dataset down into discrete messages and push them into a message broker likePub/Sub.
2. Pull the work:Have your Spot VM worker pods pull messages off the queue one by one or as a small chunk (e.g. 10 at a time).
3. Acknowledge completion:Only send an "ACK" (acknowledgment) back to Pub/Sub once the result is safely stored.

If a Spot node is preempted mid-inference, the worker dies before sending the ACK. After a brief timeout, Pub/Sub will automatically make that specific message available again. Another surviving worker pod will pick it up seamlessly. No data lost, no manual intervention required.

## Key takeaways

Running on ephemeral compute like Spot VMs isn't just an infrastructure choice; it is a design choice. By handling termination signals, checkpointing aggressively to GCS, ensuring idempotent operations, and decoupling your queues, you can unlock massive cost savings and tap into scarce GPU pools without sacrificing reliability.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse