# The MongoDB Docker Images Secures Loop

**Loop ID**: #3173 | **Category**: Evaluation | **Author**: @donald_k | **Rating**: ⭐ 4.9/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that secures Docker images in MongoDB and stops when API response time is under 100ms.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify Docker images in MongoDB systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the MongoDB repository. Focus specifically on Docker images. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: API response time is under 100ms.
```

## 🏁 Implementation Steps
1. Scan the MongoDB codebase for active Docker images.
2. Identify any deviations from the target standard: API response time is under 100ms.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Docker images meets target standards.
- *Detail*: Checked and confirmed that: API response time is under 100ms.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on Docker images to minimize run costs.

## 🏷️ Keywords
mongodb, evaluation, secures

## 💬 Reviews & Feedback
- **@ken_t** (★★★★☆ 4/5): *Successfully implemented this for MongoDB. The verification step is extremely reliable.* (2026-05-07)