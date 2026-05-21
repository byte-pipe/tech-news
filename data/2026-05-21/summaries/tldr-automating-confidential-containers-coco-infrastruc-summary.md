---
title: Automating Confidential Containers (CoCo) infrastructure with Kyverno | CNCF
url: https://www.cncf.io/blog/2026/05/19/automating-confidential-containers-coco-infrastructure-with-kyverno/
date: 2026-05-21
site: tldr
model: llama3.2:1b
summarized_at: 2026-05-21T12:10:24.513079
---

# Automating Confidential Containers (CoCo) infrastructure with Kyverno | CNCF

**Automating Confidential Containers (CoCo) Infrastructure with Kyverno**

Confidential Containers (CoCo) brings a critical security layer for containerized workloads in untrusted environments. However, deploying CoCo-enabled workloads often requires managing complex infrastructure details that are easy to get wrong.

By leveraging **Kyverno** as a Policy as Code engine, platform teams can automate much of the CoCo-specific wiring, improving developer experience while preserving the core zero-trust security model.

*   **Key Features:**
    *   Automatic injection of required CoCo-related configuration
    *   Early validation of CoCo-related inputs to prevent pod admission and startup failures
*   **Implementation Strategy:** Use Kyverno's Policy as Code engine to define policies for CoCo-enabled workloads, including runtimeClass, initdata, sealed secrets, attestation initcar, and mTLS sidecar.

**Benefits:**

*   Improved developer experience with streamlined deployment process
*   Enhanced security model by automating infrastructure management
*   Better error handling and reduced friction during deployment

See below for further details on using Kyverno for CoCo policy creation:

[Code Snippets]
```yml
# Creating a coa_policy
coa:
  runtimeClass: 'my_runtime_class'
  initdata:
    server_url: https://remote-attestation-server.com
    image_policy: 'my_image_policy'
    kata_agent_policy: 'my_kata_agent_policy'

# Validating CoCo-related inputs
valid_at_testcase:
  coa:
    RuntimeClass: 'my_runtime_class'
    initdata:
      server_url: ['https://remote-attestation-server.com'], ['https://remote-attestation-ssm.example.com']
```