---
title: Four Ways a Test Can Lie to You - DEV Community
url: https://dev.to/kenwalger/four-ways-a-test-can-lie-to-you-2ibf
date: 2026-10-28
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-11-02T08:49:00.505817
---

# Four Ways a Test Can Lie to You - DEV Community

# Four Ways a Test Can Lie – Summary

## Overview
- The author built a wine‑cellar application with ~530 tests, discovering that many checks gave misleading results.
- Four distinct failure modes for tests were identified, each corresponding to a missing or misapplied control (positive/negative).

## 1. The Test That Cannot Fail – Missing Positive Control
- **Scenario:** A test verified that proposing a claim did not alter any bottle state. It passed because it measured the fixture, not the rule.
- **Problem:** No paired assertion showed the effect when the rule is enabled, so the test could not detect a broken rule.
- **Resolution:** Added complementary assertions that the rule *does* change state when it should; verified fixes by mutating code (deleting the clause) and confirming the test now fails.

## 2. The Check That Always Fails – Missing Negative Control
- **Scenario:** A grep for leaked API credentials matched a legitimate export name, causing failures on every clean build.
- **Problem:** The test always failed, leading developers to ignore it; without a negative control it never proved anything.
- **Resolution:** Tightened the regex (20 → 40 characters) to match only real credentials, moved the check into CI, and planned a positive test to confirm it still catches injected fake credentials.

## 3. Correct Test of a Wrong Contract – Controls Present but Measuring the Wrong Thing
- **Scenario:** A date input field clamped out‑of‑range dates while the user was still typing, due to native browser behavior.
- **Problem:** The test correctly verified clamping of an out‑of‑range date, but the contract itself was wrong—clamping should only happen after entry is complete.
- **Resolution:** Recognized that the specification was incomplete; highlighted the need to validate contracts, not just test implementations.

## 4. Right Test Against the Wrong System – Controls Present but Target Misaligned
- **Scenario:** Staging environment variable was respected by the authoring tool but ignored by the built application, which always used production data.
- **Problem:** Tests ran against the wrong dataset, giving a false sense of safety.
- **Resolution:** (Not fully detailed in excerpt) – Emphasized verifying that the system under test actually respects the intended configuration.

## Key Takeaways
- Every test that asserts “no effect” needs a paired test showing the effect when enabled (positive control).
- Every test that asserts “detects a problem” needs evidence that it stays silent on clean builds (negative control).
- Tests can be structurally correct yet validate an incorrect contract; contracts must be explicitly defined and reviewed.
- Ensure the test environment matches the system under test; otherwise, tests may pass while exercising the wrong code path.