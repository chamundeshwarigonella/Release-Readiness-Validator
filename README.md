# Release Readiness Validator
A Python tool in development for checking whether test and defect evidence
supports a release decision.
## First version
The tool will read a fictional release workbook, check that the test totals
reconcile, verify that failed tests link to defects, and flag missing or
stale evidence.
## First three scenarios
- A release where the test totals reconcile and all required checks pass.
- A failed test with no linked defect.
- A release where the latest test report is unavailable.

This project uses fictional data.
