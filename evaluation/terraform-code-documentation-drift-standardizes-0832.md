# The Terraform Code Documentation Drift Standardizes Loop

**Loop ID**: #0832 | **Category**: Evaluation | **Author**: @claudio_d | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that standardizes code documentation drift in Terraform and stops when target threshold is reached.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify code documentation drift in Terraform systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Terraform repository. Focus specifically on code documentation drift. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: target threshold is reached.
```

## 🏁 Implementation Steps
1. Scan the Terraform codebase for active code documentation drift.
2. Identify any deviations from the target standard: target threshold is reached.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Code documentation drift meets target standards.
- *Detail*: Checked and confirmed that: target threshold is reached.

## 💡 Why it works
This loop works because it forces systematic optimization instead of relying on developer memory.

## ⚠️ Implementation Note
* Keep the scope focused on code documentation drift to minimize run costs.

## 🏷️ Keywords
terraform, evaluation, standardizes

## 💬 Reviews & Feedback
- **@marcus_a** (★★★★☆ 4/5): *Successfully implemented this for Terraform. The verification step is extremely reliable.* (2026-03-22)