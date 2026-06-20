# The Django Memory Leaks Cleans up Loop

**Loop ID**: #1710 | **Category**: Evaluation | **Author**: @sophia_w | **Rating**: ⭐ 4.9/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that cleans up memory leaks in Django and stops when API response time is under 100ms.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify memory leaks in Django systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Django repository. Focus specifically on memory leaks. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: API response time is under 100ms.
```

## 🏁 Implementation Steps
1. Scan the Django codebase for active memory leaks.
2. Identify any deviations from the target standard: API response time is under 100ms.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Memory leaks meets target standards.
- *Detail*: Checked and confirmed that: API response time is under 100ms.

## 💡 Why it works
This loop works because it automates routine maintenance task and flags exceptions for review.

## ⚠️ Implementation Note
* Keep the scope focused on memory leaks to minimize run costs.

## 🏷️ Keywords
django, evaluation, cleans up

## 💬 Reviews & Feedback
- **@swayam** (★★★★☆ 4/5): *Successfully implemented this for Django. The verification step is extremely reliable.* (2026-05-12)