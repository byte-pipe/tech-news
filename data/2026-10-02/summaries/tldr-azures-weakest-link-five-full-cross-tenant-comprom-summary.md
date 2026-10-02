---
title: "Azure's Weakest Link - Five Full Cross-Tenant Compromises"
url: https://www.binarysecurity.no/posts/2026/10/one-root-case
date: 2026-10-02
site: tldr
model: llama3.2:1b
summarized_at: 2026-10-02T16:38:34.752712
---

# Azure's Weakest Link - Five Full Cross-Tenant Compromises

## Azure's Weakest Link: API Connections and Cross-Tenant Compromise

### Key Points

* Azure API Connections allow anyone to access any connected backend service worldwide, including cross-tenant compromise of Key Vaults and Azure SQL databases.
* The system's architecture relies on layers of input validation, making it difficult to catch all edge cases.
* A full cross-tenant compromise can net $200,000.

### Architecture

#### API Connections

* The system queries a shared Azure API Management instance to authenticate user requests.
* The API instance then checks the swagger definition of the connector type and verifies its validity.
* A key exchange occurs between the API instance and the backend service, obtaining a new token using the input token provided by the user.

#### Vulnerabilities

* The diagram reveals that the system can be tricked into using a configured token for a victim's backend service through API Management.
* This service can be anything, including Azure services.
* By using the ARM REST API Dynamic Invoke or Extensions/Proxy/Endpoints, the calling service can query the APIM service through ARM.

### TL;DR

* API Connections allow for global access to any connected backend service.
* A full cross-tenant compromise can net $200,000.
* The system's architecture relies on input validation, making it difficult to catch all edge cases.

### Architecture (Re-Examined)

* From Microsoft's documentation, the diagram shows how the API Connection architecture works:
	+ Queries a shared Azure API Management instance.
	+ API Management checks the swagger definition and verifies its validity.
	+ Key exchange occurs between API Management and the backend service.
	+ API Management obtains a new token, using the input token from the user.

### Implementation

* By using the ARM REST API Dynamic Invoke or Extensions/Proxy/Endpoints, we can query the APIM service through ARM, bypassing input validation:
	+ This provides a clear exploitation pathway, using the calling service to query a different connectible service.

### Conclusion

* The system's architecture makes it difficult to catch all edge cases, and the vulnerabilities in the system are exploitable to gain global access to any connected backend service.