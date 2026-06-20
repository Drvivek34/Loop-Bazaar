# The Terraform Dependency Versions Refactors Loop

**Loop ID**: #0510 | **Category**: Content | **Author**: @ranvier2d2 | **Rating**: ⭐ 4.3/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that refactors dependency versions in Terraform and stops when documentation is fully aligned with implementation.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify dependency versions in Terraform systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Terraform repository. Focus specifically on dependency versions. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: documentation is fully aligned with implementation.
```

## 🏁 Implementation Steps
1. Scan the Terraform codebase for active dependency versions.
2. Identify any deviations from the target standard: documentation is fully aligned with implementation.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Dependency versions meets target standards.
- *Detail*: Checked and confirmed that: documentation is fully aligned with implementation.

## 💡 Why it works
This loop works because it automates routine maintenance task and flags exceptions for review.

## ⚠️ Implementation Note
* Keep the scope focused on dependency versions to minimize run costs.

## 🏷️ Keywords
terraform, content, refactors

## 💬 Reviews & Feedback
- **@james_g** (★★★★☆ 4/5): *Successfully implemented this for Terraform. The verification step is extremely reliable.* (2026-06-11)