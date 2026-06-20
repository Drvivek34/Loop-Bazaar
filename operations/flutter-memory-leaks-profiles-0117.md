# The Flutter Memory Leaks Profiles Loop

**Loop ID**: #0117 | **Category**: Operations | **Author**: @dennis_r | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that profiles memory leaks in Flutter and stops when performance benchmark is met.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify memory leaks in Flutter systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Flutter repository. Focus specifically on memory leaks. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: performance benchmark is met.
```

## 🏁 Implementation Steps
1. Scan the Flutter codebase for active memory leaks.
2. Identify any deviations from the target standard: performance benchmark is met.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Memory leaks meets target standards.
- *Detail*: Checked and confirmed that: performance benchmark is met.

## 💡 Why it works
This loop works because it automates routine maintenance task and flags exceptions for review.

## ⚠️ Implementation Note
* Keep the scope focused on memory leaks to minimize run costs.

## 🏷️ Keywords
flutter, operations, profiles

## 💬 Reviews & Feedback
- **@bjarnes** (★★★★☆ 4/5): *Successfully implemented this for Flutter. The verification step is extremely reliable.* (2026-05-24)