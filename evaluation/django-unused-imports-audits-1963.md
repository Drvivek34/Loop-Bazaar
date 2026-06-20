# The Django Unused Imports Audits Loop

**Loop ID**: #1963 | **Category**: Evaluation | **Author**: @guido_vr | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that audits unused imports in Django and stops when no regressions are detected.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify unused imports in Django systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Django repository. Focus specifically on unused imports. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: no regressions are detected.
```

## 🏁 Implementation Steps
1. Scan the Django codebase for active unused imports.
2. Identify any deviations from the target standard: no regressions are detected.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Unused imports meets target standards.
- *Detail*: Checked and confirmed that: no regressions are detected.

## 💡 Why it works
This loop works because it forces systematic optimization instead of relying on developer memory.

## ⚠️ Implementation Note
* Keep the scope focused on unused imports to minimize run costs.

## 🏷️ Keywords
django, evaluation, audits

## 💬 Reviews & Feedback
- **@ranvier2d2** (★★★★☆ 4/5): *Successfully implemented this for Django. The verification step is extremely reliable.* (2026-05-25)