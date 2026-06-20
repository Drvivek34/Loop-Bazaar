# The Elasticsearch Bundle Sizes Cleans up Loop

**Loop ID**: #3560 | **Category**: Evaluation | **Author**: @inferencegod | **Rating**: ⭐ 4.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that cleans up bundle sizes in Elasticsearch and stops when all checks pass successfully.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify bundle sizes in Elasticsearch systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Elasticsearch repository. Focus specifically on bundle sizes. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: all checks pass successfully.
```

## 🏁 Implementation Steps
1. Scan the Elasticsearch codebase for active bundle sizes.
2. Identify any deviations from the target standard: all checks pass successfully.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Bundle sizes meets target standards.
- *Detail*: Checked and confirmed that: all checks pass successfully.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on bundle sizes to minimize run costs.

## 🏷️ Keywords
elasticsearch, evaluation, cleans up

## 💬 Reviews & Feedback
- **@alan_turing** (★★★★☆ 4/5): *Successfully implemented this for Elasticsearch. The verification step is extremely reliable.* (2026-03-28)