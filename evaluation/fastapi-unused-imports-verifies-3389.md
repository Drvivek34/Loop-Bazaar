# The FastAPI Unused Imports Verifies Loop

**Loop ID**: #3389 | **Category**: Evaluation | **Author**: @tim_berners | **Rating**: ⭐ 4.4/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that verifies unused imports in FastAPI and stops when target threshold is reached.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify unused imports in FastAPI systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the FastAPI repository. Focus specifically on unused imports. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: target threshold is reached.
```

## 🏁 Implementation Steps
1. Scan the FastAPI codebase for active unused imports.
2. Identify any deviations from the target standard: target threshold is reached.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Unused imports meets target standards.
- *Detail*: Checked and confirmed that: target threshold is reached.

## 💡 Why it works
This loop works because it ensures security policies are consistently enforced without gaps.

## ⚠️ Implementation Note
* Keep the scope focused on unused imports to minimize run costs.

## 🏷️ Keywords
fastapi, evaluation, verifies

## 💬 Reviews & Feedback
- **@inferencegod** (★★★★☆ 4/5): *Successfully implemented this for FastAPI. The verification step is extremely reliable.* (2026-01-21)