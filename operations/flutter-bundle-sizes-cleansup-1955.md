# The Flutter Bundle Sizes Cleans up Loop

**Loop ID**: #1955 | **Category**: Operations | **Author**: @claudio_d | **Rating**: ⭐ 4.4/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that cleans up bundle sizes in Flutter and stops when API response time is under 100ms.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify bundle sizes in Flutter systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Flutter repository. Focus specifically on bundle sizes. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: API response time is under 100ms.
```

## 🏁 Implementation Steps
1. Scan the Flutter codebase for active bundle sizes.
2. Identify any deviations from the target standard: API response time is under 100ms.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Bundle sizes meets target standards.
- *Detail*: Checked and confirmed that: API response time is under 100ms.

## 💡 Why it works
This loop works because it automates routine maintenance task and flags exceptions for review.

## ⚠️ Implementation Note
* Keep the scope focused on bundle sizes to minimize run costs.

## 🏷️ Keywords
flutter, operations, cleans up

## 💬 Reviews & Feedback
- **@guido_vr** (★★★★☆ 4/5): *Successfully implemented this for Flutter. The verification step is extremely reliable.* (2026-01-12)