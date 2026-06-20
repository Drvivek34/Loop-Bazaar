# The GitHub Actions Unit Test Coverage Audits Loop

**Loop ID**: #1928 | **Category**: Evaluation | **Author**: @vivek34 | **Rating**: ⭐ 4.6/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that audits unit test coverage in GitHub Actions and stops when all vulnerabilities are resolved.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify unit test coverage in GitHub Actions systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the GitHub Actions repository. Focus specifically on unit test coverage. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: all vulnerabilities are resolved.
```

## 🏁 Implementation Steps
1. Scan the GitHub Actions codebase for active unit test coverage.
2. Identify any deviations from the target standard: all vulnerabilities are resolved.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Unit test coverage meets target standards.
- *Detail*: Checked and confirmed that: all vulnerabilities are resolved.

## 💡 Why it works
This loop works because it automates routine maintenance task and flags exceptions for review.

## ⚠️ Implementation Note
* Keep the scope focused on unit test coverage to minimize run costs.

## 🏷️ Keywords
github actions, evaluation, audits

## 💬 Reviews & Feedback
- **@ada_lovelace** (★★★★☆ 4/5): *Successfully implemented this for GitHub Actions. The verification step is extremely reliable.* (2026-04-06)