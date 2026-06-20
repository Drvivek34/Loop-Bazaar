# The Django Unused Imports Refactors Loop

**Loop ID**: #4497 | **Category**: Engineering | **Author**: @agent0ai | **Rating**: ⭐ 4.3/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that refactors unused imports in Django and stops when compliance report returns zero warnings.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify unused imports in Django systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Django repository. Focus specifically on unused imports. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: compliance report returns zero warnings.
```

## 🏁 Implementation Steps
1. Scan the Django codebase for active unused imports.
2. Identify any deviations from the target standard: compliance report returns zero warnings.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Unused imports meets target standards.
- *Detail*: Checked and confirmed that: compliance report returns zero warnings.

## 💡 Why it works
This loop works because it creates a clear evidence trail of system changes and performance checks.

## ⚠️ Implementation Note
* Keep the scope focused on unused imports to minimize run costs.

## 🏷️ Keywords
django, engineering, refactors

## 💬 Reviews & Feedback
- **@swayam** (★★★★☆ 4/5): *Successfully implemented this for Django. The verification step is extremely reliable.* (2026-03-15)