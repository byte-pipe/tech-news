---
title: AISLE Discovers 38 CVEs in Healthcare Software Used by 100,000 Medical Providers | AISLE
url: https://aisle.com/blog/aisle-discovers-38-critical-security-vulnerabilities-in-healthcare-software-used-by-100000-providers
site_name: tldr
content_file: tldr-aisle-discovers-38-cves-in-healthcare-software-use
fetched_at: '2026-05-09T07:54:15.762379'
original_url: https://aisle.com/blog/aisle-discovers-38-critical-security-vulnerabilities-in-healthcare-software-used-by-100000-providers
date: '2026-05-09'
description: 38 zero-day security vulnerabilities, three critical, and the shift from disclosure to prevention in healthcare software
tags:
- tldr
---

# AISLE Discovers 38 CVEs in Healthcare Software Used by 100,000 Medical Providers

Author

Stanislav Fort

Date Published

April 28, 2026

Healthcare is digitizing faster than it is being secured. AI-assisted diagnostics, telemedicine, and automated billing are expanding access to care at unprecedented speed, but the security practices protecting these systems have not kept up. At the same time, attackers are increasingly using AI to find vulnerabilities faster than ever. The result is a widening gap between what healthcare software can do and how well it is defended.

OpenEMRsits squarely in that gap. It is one of the most widely adopted open-source electronic health record platforms in the world, used byover 100,000 medical providers serving more than 200 million patientsacross 34 languages. OpenEMR 8.0, released in February 2026, isONC-certifiedunder the U.S. federal Health IT certification program, including the full set of Privacy and Security criteria (§ 170.315(d)(1) through (d)(13)). Such reach makes protecting it essential.

That is why we chose OpenEMR as a focus of our open-source partnership security work. Our goal is to strengthen critical infrastructure by applying the same autonomous analysis engine thatuncovered twelve zero-days in OpenSSLto a codebase that millions of patients depend on daily. The OpenEMR maintainers collaborated closely with us and responded to findings with speed and professionalism. What follows is a summary of what we found, how the issues were fixed, and what this experience reveals about the state of healthcare application security.

## The Findings at a Glance

During Q1 2026, AISLE researchers Stanislav Fort, Petr Simecek, and Pavel Kohout applied the AISLE AI analyzer to the OpenEMR codebase and discovered38 CVEs, accounting formore than halfof all OpenEMR security advisories published on GitHub during this period.

For comparison, the most prominent prior independent security audit of OpenEMR was the 2018Project Insecurity report, whichgenerated international press coverageand disclosed 23 vulnerabilities after an extended research effort by a dedicated human team. AISLE's analyzer found 38 in just one quarter.

These vulnerabilities could have enabled a broad range of attacks against OpenEMR deployments. In the most severe cases, SQL injection vulnerabilities combined with modest database privileges could have led to full database compromise, PHI exfiltration at scale, and remote code execution on the server.

## Notable Findings

Each of these vulnerabilities could be exploited to access or rewrite sensitive patient data:

### CVE-2026-24908: SQL Injection in Patient REST API Sort Parameter

The secondCVSS 10.0 findinglived in OpenEMR's Patient REST API, where the_sortquery parameter lets clients choose the ordering for returned results, a common REST pattern. The values passed to_sortwere concatenated directly into SQLORDER BYclauses with no validation, no whitelisting of allowed sort fields, and no identifier escaping. A single missed call meant any authenticated client with an OAuth2 bearer token could exploit the flaw three ways:UNION SELECTpayloads to extract credential hashes or arbitrary table contents; time-based blind injection viaSLEEP()to confirm exploitability; and if the database user heldFILEprivileges, escalation to arbitrary file read/write and remote code execution.

### CVE-2026-23627: SQL Injection in Immunization Search/Report

The Immunization module's search and report endpoints had a similar flaw, but in the web UI rather than the REST API. Thepatient_idform parameter was split on commas and each piece was stitched directly into SQLWHEREclauses without parameterization or escaping. Because the injection point was in aWHEREclause rather than anORDER BY, exploitation was more straightforward. AUNION SELECTcould extract data from any table in a single request, and time-based blind injection worked with a simpleSLEEP()call. If the database user heldFILEprivileges, the attacker could also read server files or write a web shell, escalating to remote code execution.

### CVE-2026-24487: FHIR Patient Compartment Bypass in CareTeam

The FHIR CareTeam endpoint returned care team data for every patient in the system, even when the request carried a patient-scoped OAuth2 token that should have restricted results to a single patient. The root cause was architectural: OpenEMR's FHIR layer uses a PHP interface (IPatientCompartmentResourceService) as a marker to decide which services receive patient-scoping filters. The FhirCareTeamService class never declared that interface, so the framework's instanceof check failed silently and no patient filter was injected. The underlying service already supported filtering by patient UUID; the code was simply never invoked.

## Autonomous Issue Fixes

For each of the 38 CVEs, AISLE generated a repository-native fix proposal that reused OpenEMR's own abstractions, authorization patterns, and sanitization helpers. For the critical-severityCVE-2026-23627, AISLE independently produced the patch. In other cases, OpenEMR maintainers adapted AISLE's proposed remediation into the final fix.

This significantly reduced the time to remediation and made it easier for OpenEMR's dedicated maintainers to secure the codebase.

## A Partnership for Patient Safety

Our engagement with OpenEMR began in mid-December 2025, when the AISLE analyzer first started inspecting the codebase. We reported the initial batch of findings in mid-January 2026, and from the very first disclosures, the OpenEMR Foundation worked alongside us on remediation, reviewing findings quickly, iterating on fixes, and engaging with the technical detail of every issue. The bulk of the AISLE-reported fixes shipped in OpenEMR 8.0.0 on February 11, 2026, roughly four weeks after the first disclosures, with the remainder landing across three subsequent patch releases throughout March.

In early April 2026, we formalized the partnership by integratingAISLE PRO, our AI-powered commit analyzer, into OpenEMR's code review workflow. Together, we can now detect many vulnerabilities at the code review stage, before they enter production, securing new code even as the team works through the existing backlog.

"For a project like OpenEMR, where the stakes are patient safety and health data privacy, we couldn't be more excited about our partnership with AISLE. Their autonomous analyzer uncovered dozens of vulnerabilities in our codebase. Now, with Aisle's analyzer running at the code review stage, we're catching and fixing vulnerabilities before they ever reach production."

—Brady Miller, MD, Executive Director of the OpenEMR Foundation

## From Disclosure to Prevention with AISLE

AI-powered attacks increasingly target healthcare institutions to steal personally identifiable information, extort payments, and disrupt the delivery of life-saving care. Defenders need matching coverage. The OpenEMR engagement is what that looks like in practice: an autonomous analyzer finding real vulnerabilities in critical software, fixes landing in production within weeks, and the same system moving upstream to catch new vulnerabilities at code review, before they ever reach a patient record.

If your organization depends on software to deliver care,schedule a demoto see what AISLE can do.

## Full Advisory List

### Missing or incorrect authorization

The single largest category. Many endpoints accepted user-supplied record identifiers (patient IDs, note IDs, form IDs) and operated on them without verifying that the caller was permitted to access the referenced record. In access-control terminology, this is known as an Insecure Direct Object Reference (IDOR). A related subset involved endpoints that omitted Access Control List (ACL) checks entirely, allowing any authenticated user to reach functionality intended for administrators or specific roles. At one extreme, a single endpoint bypassed authentication entirely.

Title

Severity

Weakness

CVE

Unauthenticated patient identity disclosure

Critical

Missing Authentication

CVE-2026-24898

FHIR Patient Compartment Bypass in CareTeam

High

Information Exposure

CVE-2026-24487

Inverted ACL in CDR ControllerRouter

High

Missing Authorization

CVE-2026-32126

Missing Authorization in Procedure Order Deletion Handler

High

Missing Authorization

CVE-2026-34053

IDOR in Patient Notes Web UI

High

Authorization Bypass

CVE-2026-34055

Document and Insurance REST Endpoints Skip ACL

High

Missing Authorization

CVE-2026-25164

Missing Authorization on Claim File Download

High

Missing Authorization

CVE-2026-33918

Therapy Group Sensitivity ACL Not Enforced

High

Incorrect Authorization

CVE-2026-32123

Portal Payment Endpoint Trusts User-Controlled PID

High

Authorization Bypass

CVE-2026-25147

Missing Authorization in DICOM Viewer State API

High

Authorization Bypass

CVE-2026-25927

zhAclCheck Ignores Explicit ACL Denies

High

Incorrect Authorization

CVE-2026-33302

Portal Users Can Forge Provider Signatures

High

Improper Authorization

CVE-2026-24890

Authorization Bypass in Dated Reminders Log

Medium

Authorization Bypass

CVE-2026-33304

Patient Picture IDOR

Medium

Authorization Bypass

CVE-2026-25929

IDOR in Portal Payment Page

Medium

Authorization Bypass

CVE-2026-33931

Message Update Ignores Patient ID (REST API)

Medium

Authorization Bypass

CVE-2026-25745

Vitals API Accepts Attacker-Supplied ID

Medium

Authorization Bypass

CVE-2026-25744

Messages "Show All" Not Restricted to Admins

Medium

Authorization Bypass

CVE-2026-25220

IDOR in Fee Sheet Product Save

Medium

Authorization Bypass

CVE-2026-32120

Eye Exam View IDOR

Medium

Authorization Bypass

CVE-2026-27943

Authorization Bypass in FaxSMS AppDispatch Constructor

Medium

Incorrect Behavior Order

CVE-2026-33305

Missing Authorization on Claim File Tracker AJAX Endpoint

Medium

Missing Authorization

CVE-2026-32122

Portal Patients Can Read Staff Signatures

Medium

Authorization Bypass

CVE-2026-33934

Printable LBF Endpoint Leaks Arbitrary Patient Forms

Medium

Authorization Bypass

CVE-2026-25930

### Cross-site scripting

User-controlled data was rendered into HTML or JavaScript without proper encoding, allowing an attacker to inject code that would run in another user's browser session. Several of these crossed the trust boundary between the patient portal and the clinical staff interface, meaning a patient could inject code that would execute in a clinician's or administrator's session.

Title

Severity

Weakness

CVE

Stored DOM XSS via .html() in Portal Signer Modal

High

Cross-site Scripting

CVE-2026-32121

Stored XSS in CCDA Preview via linkHtml

High

Cross-site Scripting

CVE-2026-33932

Stored XSS in Portal Payment via table_args

High

Cross-site Scripting

CVE-2026-33346

Stored XSS in Track Anything Graphs

Medium

Cross-site Scripting

CVE-2026-32125

Stored XSS in Graphical Pain Map

Medium

Cross-site Scripting

CVE-2026-32118

Stored XSS in Dynamic Code Picker

Medium

Cross-site Scripting

CVE-2026-32124

Reflected XSS in Custom Template Editor

Medium

Cross-site Scripting

CVE-2026-33933

Stored XSS via Portal Login Username

Medium

Cross-site Scripting

CVE-2026-33303

Stored DOM XSS via SearchHighlight

Medium

Cross-site Scripting

CVE-2026-32119

### SQL injection, path traversal, and session flaws

These includedSQL injections(user input was concatenated directly into SQL queries without proper sanitization), aninsufficient session expirationissue, andpath traversals(user-controlled file paths were not restricted to the intended directory, enabling arbitrary file reads or writes on the server).

Title

Severity

Weakness

CVE

SQL injection in patient API sort parameter

Critical

SQL Injection

CVE-2026-24908

SQL Injection in Immunization Search/Report

Critical

SQL Injection

CVE-2026-23627

Session Timeout Bypass via skip_timeout_reset

High

Insufficient Session Expiration

CVE-2026-25476

Arbitrary File Exfiltration via Fax Endpoint

Medium

Path Traversal

CVE-2026-24488

Path Traversal When Zipping DICOM Folders

Medium

Path Traversal

CVE-2026-25928

Our deepest appreciation goes to the OpenEMR maintainers for their professional collaboration. All issues were discovered using the AISLE AI analyzer and responsibly disclosed by Pavel Kohout, Petr Simecek, and Stanislav Fort.