# The Laravel Dependency Versions Triages Loop

**Loop ID**: #3850 | **Category**: Content | **Author**: @dennis_r | **Rating**: ⭐ 4.6/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that triages dependency versions in Laravel and stops when test coverage reaches 100%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify dependency versions in Laravel systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Laravel repository. Focus specifically on dependency versions. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: test coverage reaches 100%.
```

## 🏁 Implementation Steps
1. Scan the Laravel codebase for active dependency versions.
2. Identify any deviations from the target standard: test coverage reaches 100%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Dependency versions meets target standards.
- *Detail*: Checked and confirmed that: test coverage reaches 100%.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on dependency versions to minimize run costs.

## 🏷️ Keywords
laravel, content, triages

## 💬 Reviews & Feedback
- **@lucas_k** (★★★★☆ 4/5): *Successfully implemented this for Laravel. The verification step is extremely reliable.* (2026-02-19)