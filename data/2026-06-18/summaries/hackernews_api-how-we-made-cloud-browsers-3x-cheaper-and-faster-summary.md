---
title: How We Made Cloud Browsers 3x Cheaper and Faster
url: https://browser-use.com/posts/firecracker-browser-infra
date: 2026-06-16
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-06-18T12:23:58.017290
---

# How We Made Cloud Browsers 3x Cheaper and Faster

**Making Cloud Browsers 3x Cheaper and Faster**

We rebuilt Browser Use Cloud to address concerns about performance when running cloud browsers. The company's solution aims to:

• Start quickly
• Remain isolated (no shared resources)
• Be cheap ($0.02 per browser hour)

To achieve this, we replaced a virtual machine (VM) requirement with:

• Running on bare-metal servers on Amazon EC2, a rented cloud server model
• Regular EC2 instances instead of VMs due to performance concerns

**Why We Left Unikernels Behind**

Before rebuilding our infrastructure, the company used unikernels for their browsers. However, unikernels are designed to be:

• Small and lightweight
• Fast at initialization
• Cheap when not in use

But they have limitations:

* Starting quickly and being free when idle makes them unsuitable for high-traffic environments like cloud browsers.
* Manual capacity adjustment required during bursts can cause problems.

**The New Setup**

To address these issues, we adopted the Firecracker solution. It provides a layer that allows users to create, monitor, and run VMs:

• Each VM has CPU, memory, disk, and network access
• Demand-based scaling tracks user demand automatically
• Provides a scalable platform for running cloud browsers

**What Makes Firecracker Difficult?**

While Firecracker is effective, building it was complex. The main stumbling block was ensuring that the solution started quickly and remained isolated:

• Naked EC2 instances don't have built-in autoscaling, requiring manual intervention by engineers
• Starting a VM in under a second is difficult due to Chromium startup processes

**Rebuilding for Faster Performance**

Our setup includes significant improvements:

• Rented cloud servers (EC2) are much faster than bare-metal instances
• Manual adjustment of capacity by engineers has been simplified with Firecracker's autoscaling mechanisms
• A new solution allows us to focus on delivering fast, secure, and affordable cloud browsers