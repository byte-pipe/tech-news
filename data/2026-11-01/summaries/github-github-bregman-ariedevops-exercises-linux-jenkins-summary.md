---
title: GitHub - bregman-arie/devops-exercises: Linux, Jenkins, AWS, SRE, Prometheus, Docker, Python, Ansible, Git, Kubernetes, Terraform, OpenStack, SQL, NoS...
url: https://github.com/bregman-arie/devops-exercises
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-01T18:54:21.236432
---

# GitHub - bregman-arie/devops-exercises: Linux, Jenkins, AWS, SRE, Prometheus, Docker, Python, Ansible, Git, Kubernetes, Terraform, OpenStack, SQL, NoS...

# Repository Overview
- The repository **devops-exercises** contains questions and hands‑on exercises covering a wide range of DevOps, SRE, and related technical topics.  
- Currently it holds **2 624** exercises and interview questions.  
- It is intended as a study aid; most items do not reflect real interview content.  
- Contributors can add new exercises via pull requests, following the provided contribution guidelines.  

## Main Sections
- **README / FAQ** – explains purpose, usage warnings, and how to contribute.  
- **Topics directories** – organized by technology (e.g., Linux, Jenkins, AWS, Kubernetes, Terraform, Ansible, Python, etc.).  
- **Exercises & tests** – practical tasks and corresponding test scripts.  
- **Certificates, images, scripts** – supporting files for various exercises.  

## Contribution & Licensing
- Contribution guidelines are available in `CONTRIBUTING.md` (and localized versions).  
- The project is licensed under the MIT License.  

# Network Fundamentals Covered in the Repository
- **Basic communication requirements**  
  - Common language, addressing, and a connection.  

- **TCP/IP**  
  - Defined as a suite of protocols enabling device communication.  

- **Ethernet**  
  - Described as the most common LAN technology; contrasts LAN with WAN.  

- **MAC address**  
  - Unique identifier for network interfaces; used for frame delivery and ARP broadcasts (`ff:ff:ff:ff:ff:ff`).  

- **IP address**  
  - Numerical label for host/interface identification and location addressing.  

- **Subnet mask**  
  - 32‑bit mask separating network and host portions of an IP address; reserves the first (network) and last (broadcast) addresses.  

- **Private vs. public IP addresses**  
  - Private IPs are used within a local network and are not reachable from external networks.  
  - Public IPs are routable on the Internet; require port forwarding to expose internal services.  

- **OSI model (7 layers)**  
  - Application – user‑level protocols (e.g., HTTP)  
  - Presentation – data representation and encryption  
  - Session – connection establishment and termination  
  - Transport – reliable/unreliable transport (TCP, UDP)  
  - Network – routing of datagrams (IP)  
  - Data link – node‑to‑node framing (MAC)  
  - Physical – electrical/optical signaling  

- **Mapping of concepts to OSI layers**  
  - Error correction → Data link  
  - Packet routing → Network  
  - Cables & electrical signals → Physical  
  - MAC address → Data link  
  - IP address → Network  
  - Terminate connections → Session  
  - 3‑way handshake → Transport  

- **Delivery schemes**  
  - Unicast – one‑to‑one  
  - Broadcast – one‑to‑all (uses `ff:ff:ff:ff:ff:ff`)  
  - Multicast – one‑to‑many or many‑to‑many  

- **CSMA/CD** (Carrier Sense Multiple Access / Collision Detection)  
  - Mechanism for managing access to a shared Ethernet medium.  
  - Steps: sense carrier, transmit if idle, detect collisions, send jam signal, back‑off randomly, retry.  
  - Not commonly used in modern switched Ethernet, which provides full‑duplex links that eliminate collisions.