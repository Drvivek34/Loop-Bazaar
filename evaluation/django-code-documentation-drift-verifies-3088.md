# The Django Code Documentation Drift Verifies Loop

**Loop ID**: #3088 | **Category**: Evaluation | **Author**: @ranvier2d2 | **Rating**: ⭐ 4.1/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that verifies code documentation drift in Django and stops when documentation is fully aligned with implementation.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify code documentation drift in Django systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Django repository. Focus specifically on code documentation drift. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: documentation is fully aligned with implementation.
```

## 🏁 Implementation Steps
1. Scan the Django codebase for active code documentation drift.
2. Identify any deviations from the target standard: documentation is fully aligned with implementation.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Code documentation drift meets target standards.
- *Detail*: Checked and confirmed that: documentation is fully aligned with implementation.

## 💡 Why it works
This loop works because it forces systematic optimization instead of relying on developer memory.

## ⚠️ Implementation Note
* Keep the scope focused on code documentation drift to minimize run costs.

## 🏷️ Keywords
django, evaluation, verifies

## 💬 Reviews & Feedback
- **@grace_hopper** (★★★★☆ 4/5): *Successfully implemented this for Django. The verification step is extremely reliable.* (2026-05-25)