---
title: Automate public TLS certificate issuance with ACME support in AWS Certificate Manager | AWS News Blog
url: https://aws.amazon.com/blogs/aws/automate-public-tls-certificate-issuance-with-acme-support-in-aws-certificate-manager/
date: 2026-07-02
site: tldr
model: llama3.2:1b
summarized_at: 2026-07-02T11:53:25.407554
---

# Automate public TLS certificate issuance with ACME support in AWS Certificate Manager | AWS News Blog

## Automating Public TLS Certificate Issuance with ACME Support in AWS Certificate Manager

With the introduction of automatic certificate management through the Amazon Trust Services (Amazon Trust Servicethrough the standard ACME protocol), enterprises can now manage and monitor public TLS certificates from a centralized dashboard. Key features include:

* **Centralized controls**: One or more managed ACME endpoints allow for fine-grained access control over which domains each client can request.
* **Domain scopes**: Organizational policies are defined at the endpoint level, enabling organization-wide restrictions on certificate issuance.
* **Monitoring and visibility**: Amazon CloudTrail logs every certificate request, Amazon CloudWatch tracks operational metrics, and ACM sends expiry notifications when certificates approach renewal.

To set up ACME support:

1. Set up a dedicated ACME endpoint using External Account Binding (EAB).
2. Validate which domains the endpoint can issue certificates for.
3. Point existing ACME clients to the new endpoint.

### Benefits

- **Improved reliability**: Certificates are no longer at risk of expiration, reducing downtime and security concerns.
- **Increased scalability**: Automated processes reduce manual workload and improve operational efficiency.

### Future Plans

As part of ongoing support for the ACME protocol in AWS Certificate Manager, AWS will continue to add additional features, including:

- **Automated certificate renewal**: Automatic renewal of certificates by integrating with external services like AWS Systems Manager.
- **Enhanced monitoring**: Integration with AWS X-Ray and AWS Network Watcher for detailed performance analysis.

By embracing automatic TLS certificate issuance through ACME support in AWS Certificate Manager, enterprises can enjoy improved security, scalability, and centralization across their application portfolios.