# The Django Accessibility Tags Sweeps Loop

**Loop ID**: #0595 | **Category**: Evaluation | **Author**: @ada_lovelace | **Rating**: ⭐ 4.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that sweeps accessibility tags in Django and stops when no regressions are detected.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify accessibility tags in Django systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Django repository. Focus specifically on accessibility tags. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: no regressions are detected.
```

## 🏁 Implementation Steps
1. Scan the Django codebase for active accessibility tags.
2. Identify any deviations from the target standard: no regressions are detected.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Accessibility tags meets target standards.
- *Detail*: Checked and confirmed that: no regressions are detected.

## 💡 Why it works
This loop works because it forces systematic optimization instead of relying on developer memory.

## ⚠️ Implementation Note
* Keep the scope focused on accessibility tags to minimize run costs.

## 🏷️ Keywords
django, evaluation, sweeps

## 💬 Reviews & Feedback
- **@marcus_a** (★★★★☆ 4/5): *Successfully implemented this for Django. The verification step is extremely reliable.* (2026-04-23)