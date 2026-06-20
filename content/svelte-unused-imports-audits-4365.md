# The Svelte Unused Imports Audits Loop

**Loop ID**: #4365 | **Category**: Content | **Author**: @elena_r | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that audits unused imports in Svelte and stops when compliance report returns zero warnings.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify unused imports in Svelte systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Svelte repository. Focus specifically on unused imports. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: compliance report returns zero warnings.
```

## 🏁 Implementation Steps
1. Scan the Svelte codebase for active unused imports.
2. Identify any deviations from the target standard: compliance report returns zero warnings.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Unused imports meets target standards.
- *Detail*: Checked and confirmed that: compliance report returns zero warnings.

## 💡 Why it works
This loop works because it automates routine maintenance task and flags exceptions for review.

## ⚠️ Implementation Note
* Keep the scope focused on unused imports to minimize run costs.

## 🏷️ Keywords
svelte, content, audits

## 💬 Reviews & Feedback
- **@guido_vr** (★★★★☆ 4/5): *Successfully implemented this for Svelte. The verification step is extremely reliable.* (2026-06-11)