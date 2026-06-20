# The Elasticsearch Docker Images Profiles Loop

**Loop ID**: #3996 | **Category**: Operations | **Author**: @inferencegod | **Rating**: ⭐ 4.9/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that profiles Docker images in Elasticsearch and stops when test coverage reaches 100%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify Docker images in Elasticsearch systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Elasticsearch repository. Focus specifically on Docker images. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: test coverage reaches 100%.
```

## 🏁 Implementation Steps
1. Scan the Elasticsearch codebase for active Docker images.
2. Identify any deviations from the target standard: test coverage reaches 100%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Docker images meets target standards.
- *Detail*: Checked and confirmed that: test coverage reaches 100%.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on Docker images to minimize run costs.

## 🏷️ Keywords
elasticsearch, operations, profiles

## 💬 Reviews & Feedback
- **@guido_vr** (★★★★☆ 4/5): *Successfully implemented this for Elasticsearch. The verification step is extremely reliable.* (2026-01-10)