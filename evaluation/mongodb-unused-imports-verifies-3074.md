# The MongoDB Unused Imports Verifies Loop

**Loop ID**: #3074 | **Category**: Evaluation | **Author**: @hiten | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that verifies unused imports in MongoDB and stops when stale state is fully cleared.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify unused imports in MongoDB systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the MongoDB repository. Focus specifically on unused imports. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: stale state is fully cleared.
```

## 🏁 Implementation Steps
1. Scan the MongoDB codebase for active unused imports.
2. Identify any deviations from the target standard: stale state is fully cleared.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Unused imports meets target standards.
- *Detail*: Checked and confirmed that: stale state is fully cleared.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on unused imports to minimize run costs.

## 🏷️ Keywords
mongodb, evaluation, verifies

## 💬 Reviews & Feedback
- **@brendan_e** (★★★★☆ 4/5): *Successfully implemented this for MongoDB. The verification step is extremely reliable.* (2026-02-05)