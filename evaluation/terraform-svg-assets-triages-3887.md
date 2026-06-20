# The Terraform Svg Assets Triages Loop

**Loop ID**: #3887 | **Category**: Evaluation | **Author**: @ken_t | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that triages SVG assets in Terraform and stops when no regressions are detected.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify SVG assets in Terraform systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Terraform repository. Focus specifically on SVG assets. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: no regressions are detected.
```

## 🏁 Implementation Steps
1. Scan the Terraform codebase for active SVG assets.
2. Identify any deviations from the target standard: no regressions are detected.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Svg assets meets target standards.
- *Detail*: Checked and confirmed that: no regressions are detected.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on SVG assets to minimize run costs.

## 🏷️ Keywords
terraform, evaluation, triages

## 💬 Reviews & Feedback
- **@agent0ai** (★★★★★ 5/5): *Successfully implemented this for Terraform. The verification step is extremely reliable.* (2026-01-08)