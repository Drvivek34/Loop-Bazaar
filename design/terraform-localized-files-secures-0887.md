# The Terraform Localized Files Secures Loop

**Loop ID**: #0887 | **Category**: Design | **Author**: @tim_berners | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that secures localized files in Terraform and stops when compliance report returns zero warnings.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify localized files in Terraform systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Terraform repository. Focus specifically on localized files. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: compliance report returns zero warnings.
```

## 🏁 Implementation Steps
1. Scan the Terraform codebase for active localized files.
2. Identify any deviations from the target standard: compliance report returns zero warnings.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Localized files meets target standards.
- *Detail*: Checked and confirmed that: compliance report returns zero warnings.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on localized files to minimize run costs.

## 🏷️ Keywords
terraform, design, secures

## 💬 Reviews & Feedback
- **@elena_r** (★★★★☆ 4/5): *Successfully implemented this for Terraform. The verification step is extremely reliable.* (2026-05-21)