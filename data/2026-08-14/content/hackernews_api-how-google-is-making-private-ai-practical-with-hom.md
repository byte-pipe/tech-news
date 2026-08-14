---
title: How Google is Making Private AI Practical with Homomorphic Encryption
url: https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/
site_name: hackernews_api
content_file: hackernews_api-how-google-is-making-private-ai-practical-with-hom
fetched_at: '2026-08-14T19:48:41.085225'
original_url: https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/
author: u1hcw9nx
date: '2026-08-14'
published_date: '2026-08-14'
description: 'Today we''re excited to showcase HEIR, the latest powerful tool added to our Private Computing Toolkit. HEIR is an open source compiler that unlocks cryptographically-secure private AI inference.Homomorphic encryptionAs new benefits emerge with the growth of AI, balancing privacy and security is top of mind. Standard protections like end-to-end encryption present a trade-off: user-data can be protected from data breaches, but then the service provider cannot provide features that depend on the data, such as spam or virus detection. Critical sectors like healthcare and finance are even more averse to these risks, and strict regulations limit data sharing across institutions. Alternative mechanisms to provide the same features, like local processing, are limited by the capabilities of the local device and the sensitivity of the service provider''s IP. Shipping proprietary AI to a device risks leaking the model.A solution to these issues is homomorphic encryption, a rapidly maturing
  technology that fundamentally alters this trade-off by allowing computations to be performed directly on encrypted data. Servers can process ciphertexts and return encrypted results without exposing any underlying information. For example, a cloud service can provide content recommendations without being able to see the user''s features. This is no exaggeration: one of the demos featured in this post does exactly this. But while homomorphic encryption has a nontrivial cost overhead, it shifts the capability/privacy trade-off to a question of cost. And the cost of homomorphic encryption is rapidly decreasing.Google’s history of innovations in privacy technology—from differential privacy and private set membership to private information retrieval and secure enclaves on Google Cloud—has always focused on securing user data. Homomorphic encryption is another powerful tool we''re adding to our private computing toolkit. Like private information retrieval, and in contrast to hardware-based solutions,
  homomorphic encryption''s strong security and privacy guarantees are purely cryptographic. However, manually converting an existing program to use homomorphic encryption efficiently requires a team of cryptographers.About HEIRTo overcome the usability challenges and advance the opportunity homomorphic encryption provides, researchers and engineers at Google built the HEIR compiler project. HEIR (Homomorphic Encryption Intermediate Representation) is an open-source compiler toolchain and development platform for homomorphic encryption. In particular, HEIR can convert pre-trained AI models that operate on unencrypted data to operate on encrypted inputs. Our vision is to make HEIR a one-click solution to enable non-experts to incorporate encrypted inference into production applications.Since announcing our intentions in 2023, we’ve seen the homomorphic encryption community embrace HEIR. We have partnered with companies developing hardware accelerators for homomorphic encryption, including
  Belfort, Niobium, Cornami, and Optalysys. The fruits of those efforts are shown in our demos below, and we plan to demonstrate the latency benefits of these accelerators in the near future. HEIR has also become a productive research platform. By building on HEIR, cryptographers can focus on their specific optimization and use the existing infrastructure for testing, benchmarking, and comparisons. This has resulted in collaborations with Georgia Tech, Carnegie Mellon, UC Santa Barbara, Illinois Institute of Technology, Purdue, the University of Edinburgh, Tsinghua University, and others. To date, four peer-reviewed publications were built on HEIR, with more in preparation, and HEIR has accumulated numerous citations.Applications of HEIRTo demonstrate how far homomorphic encryption has come, we’re sharing four private inference applications. Each application was compiled with HEIR, and latency numbers are presented for a single-threaded CPU. The source code for all examples is available
  in our GitHub repository.A Deep Learning Recommendation Model unlocks serving private content recommendations, joint work with Belfort Labs, LG, and New York University.Credit card fraud detection: Together with Niobium and hardshell.ai, we compiled a credit card fraud detector.Threat intrusion: Together with Niobium we compiled the Kitsune system for anomaly detection of encrypted network traffic. This allows a service provider to detect anomalies without revealing the contents of network packets to the service provider.Hotword Detector: Together with Belfort Labs we compiled a hotword detection model, which could allow an audio-triggered AI agent to recognize hotwords while protecting the privacy of the audio recordings.As the software industry adapts to security and privacy changes amid AI, our research team is working to make homomorphic encryption, easy to develop, fast to run, and ubiquitous across industry.'
tags:
- hackernews
- trending
---

Security

# How Google is Making Private AI Practical with Homomorphic Encryption

Aug 14, 2026

|

Jeremy Kun

Staff Software Engineer

 Share
 

Today we're excited to showcaseHEIR, the latest powerful tool added to our Private Computing Toolkit. HEIR is an open source compiler that unlocks cryptographically-secure private AI inference.

Homomorphic encryption

As new benefits emerge with the growth of AI, balancing privacy and security is top of mind. Standard protections like end-to-end encryption present a trade-off: user-data can be protected from data breaches, but then the service provider cannot provide features that depend on the data, such as spam or virus detection. Critical sectors like healthcare and finance are even more averse to these risks, and strict regulations limit data sharing across institutions. Alternative mechanisms to provide the same features, like local processing, are limited by the capabilities of the local device and the sensitivity of the service provider's IP. Shipping proprietary AI to a device risks leaking the model.

A solution to these issues ishomomorphic encryption, a rapidly maturing technology that fundamentally alters this trade-off by allowing computations to be performed directly on encrypted data. Servers can process ciphertexts and return encrypted results without exposing any underlying information. For example, a cloud service can provide content recommendations without being able to see the user's features. This is no exaggeration: one of the demos featured in this post does exactly this. But while homomorphic encryption has a nontrivial cost overhead, it shifts the capability/privacy trade-off to a question of cost. And the cost of homomorphic encryption is rapidly decreasing.

Google’s history of innovations in privacy technology—fromdifferential privacyandprivate set membershiptoprivate information retrievalandsecure enclaves on Google Cloud—has always focused on securing user data. Homomorphic encryption is another powerful tool we're adding to our private computing toolkit. Like private information retrieval, and in contrast to hardware-based solutions, homomorphic encryption's strong security and privacy guarantees are purely cryptographic. However, manually converting an existing program to use homomorphic encryption efficiently requires a team of cryptographers.

About HEIR

To overcome the usability challenges and advance the opportunity homomorphic encryption provides, researchers and engineers at Google built theHEIR compiler project. HEIR (Homomorphic Encryption Intermediate Representation) is an open-source compiler toolchain and development platform for homomorphic encryption. In particular, HEIR can convert pre-trained AI models that operate on unencrypted data to operate on encrypted inputs. Our vision is to make HEIR a one-click solution to enable non-experts to incorporate encrypted inference into production applications.

Since announcingour intentions in 2023, we’ve seen the homomorphic encryption community embrace HEIR. We have partnered with companies developing hardware accelerators for homomorphic encryption, includingBelfort,Niobium,Cornami, andOptalysys. The fruits of those efforts are shown in our demos below, and we plan to demonstrate the latency benefits of these accelerators in the near future. HEIR has also become a productive research platform. By building on HEIR, cryptographers can focus on their specific optimization and use the existing infrastructure for testing, benchmarking, and comparisons. This has resulted in collaborations with Georgia Tech, Carnegie Mellon, UC Santa Barbara, Illinois Institute of Technology, Purdue, the University of Edinburgh, Tsinghua University, and others. To date, four peer-reviewed publications were built on HEIR, with more in preparation, and HEIR has accumulatednumerous citations.

Applications of HEIR

To demonstrate how far homomorphic encryption has come, we’re sharing four private inference applications. Each application was compiled with HEIR, and latency numbers are presented for a single-threaded CPU. The source code for all examples is available in ourGitHub repository.

* ADeep Learning Recommendation Modelunlocks serving private content recommendations, joint work withBelfort Labs,LG, andNew York University.
* Credit card fraud detection:Together withNiobiumandhardshell.ai, we compiled a credit card fraud detector.
* Threat intrusion:Together withNiobiumwe compiled theKitsunesystem for anomaly detection of encrypted network traffic. This allows a service provider to detect anomalies without revealing the contents of network packets to the service provider.
* Hotword Detector:Together withBelfort Labswe compiled a hotword detection model, which could allow an audio-triggered AI agent to recognize hotwords while protecting the privacy of the audio recordings.

As the software industry adapts to security and privacy changes amid AI, our research team is working to make homomorphic encryption, easy to develop, fast to run, and ubiquitous across industry.

POSTED IN:

## Related stories

 Security
 

### The Evolving Role of the Red Team in the Era of Agentic Security

At Google, our Red Teams have always operated on the cutting edge of security. We’ve shared our journey in the past: from the high-stakes operations showcased in our Hac…

 By
 
 
 Daniel Fabian
 
 

 Security
 

### Influence Operations Bulletin Q2 2026

This bulletin includes coordinated influence operation campaigns terminated on our platforms in Q2 2026. It was last updated on June 30, 2026.AprilWe terminated 13 YouTu…

 By
 
 
 Trust & Safety
 
 

 Chrome
 

### Stronger with every update: How we’re making Chrome and the web safer in the AI Era

 By
 
 
 Chrome Security Team
 
 

 Security
 

### From Finding to Fixing: Reducing maintainer burden with automated patches

Since its launch in 2016, OSS-Fuzz has contributed significantly to making open-source secure by finding and reporting tens of thousands of bugs. But finding more vulner…

 By
 
 
 Alex Kilian
 
 & 
 Dustin Ingram
 
 

 Security
 

### Going Beyond Zero: A New Paradigm For Enterprise Security

 By
 
 
 Heather Adkins
 
 & 
 Archana Ramamoorthy
 
 

 Chrome Security
 

### Bringing AI agents to Chrome Enterprise security management

 By
 
 
 Tim Feeley
 
 & 
 Shantanu Das