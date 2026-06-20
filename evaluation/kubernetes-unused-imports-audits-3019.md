# The Kubernetes Unused Imports Audits Loop

**Loop ID**: #3019 | **Category**: Evaluation | **Author**: @lSAAGl | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that audits unused imports in Kubernetes and stops when performance benchmark is met.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify unused imports in Kubernetes systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Kubernetes repository. Focus specifically on unused imports. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: performance benchmark is met.
```

## 🏁 Implementation Steps
1. Scan the Kubernetes codebase for active unused imports.
2. Identify any deviations from the target standard: performance benchmark is met.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Unused imports meets target standards.
- *Detail*: Checked and confirmed that: performance benchmark is met.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on unused imports to minimize run costs.

## 🏷️ Keywords
kubernetes, evaluation, audits

## 💬 Reviews & Feedback
- **@sophia_w** (★★★★☆ 4/5): *Successfully implemented this for Kubernetes. The verification step is extremely reliable.* (2026-01-22)