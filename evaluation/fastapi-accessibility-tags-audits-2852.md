# The FastAPI Accessibility Tags Audits Loop

**Loop ID**: #2852 | **Category**: Evaluation | **Author**: @tim_berners | **Rating**: ⭐ 4.4/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that audits accessibility tags in FastAPI and stops when documentation is fully aligned with implementation.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify accessibility tags in FastAPI systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the FastAPI repository. Focus specifically on accessibility tags. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: documentation is fully aligned with implementation.
```

## 🏁 Implementation Steps
1. Scan the FastAPI codebase for active accessibility tags.
2. Identify any deviations from the target standard: documentation is fully aligned with implementation.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Accessibility tags meets target standards.
- *Detail*: Checked and confirmed that: documentation is fully aligned with implementation.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on accessibility tags to minimize run costs.

## 🏷️ Keywords
fastapi, evaluation, audits

## 💬 Reviews & Feedback
- **@marcus_a** (★★★★☆ 4/5): *Successfully implemented this for FastAPI. The verification step is extremely reliable.* (2026-06-10)