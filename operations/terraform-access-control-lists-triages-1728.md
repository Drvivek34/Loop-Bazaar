# The Terraform Access Control Lists Triages Loop

**Loop ID**: #1728 | **Category**: Operations | **Author**: @ada_lovelace | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that triages access control lists in Terraform and stops when documentation is fully aligned with implementation.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify access control lists in Terraform systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Terraform repository. Focus specifically on access control lists. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: documentation is fully aligned with implementation.
```

## 🏁 Implementation Steps
1. Scan the Terraform codebase for active access control lists.
2. Identify any deviations from the target standard: documentation is fully aligned with implementation.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Access control lists meets target standards.
- *Detail*: Checked and confirmed that: documentation is fully aligned with implementation.

## 💡 Why it works
This loop works because it creates a clear evidence trail of system changes and performance checks.

## ⚠️ Implementation Note
* Keep the scope focused on access control lists to minimize run costs.

## 🏷️ Keywords
terraform, operations, triages

## 💬 Reviews & Feedback
- **@hiten** (★★★★☆ 4/5): *Successfully implemented this for Terraform. The verification step is extremely reliable.* (2026-03-17)