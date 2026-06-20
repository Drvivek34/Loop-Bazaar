# The Flutter Unused Imports Profiles Loop

**Loop ID**: #1100 | **Category**: Evaluation | **Author**: @bjarnes | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that profiles unused imports in Flutter and stops when API response time is under 100ms.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify unused imports in Flutter systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Flutter repository. Focus specifically on unused imports. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: API response time is under 100ms.
```

## 🏁 Implementation Steps
1. Scan the Flutter codebase for active unused imports.
2. Identify any deviations from the target standard: API response time is under 100ms.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Unused imports meets target standards.
- *Detail*: Checked and confirmed that: API response time is under 100ms.

## 💡 Why it works
This loop works because it forces systematic optimization instead of relying on developer memory.

## ⚠️ Implementation Note
* Keep the scope focused on unused imports to minimize run costs.

## 🏷️ Keywords
flutter, evaluation, profiles

## 💬 Reviews & Feedback
- **@richard_s** (★★★★☆ 4/5): *Successfully implemented this for Flutter. The verification step is extremely reliable.* (2026-04-15)