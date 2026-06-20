# The Next.js Server Response Times Cleans up Loop

**Loop ID**: #0089 | **Category**: Design | **Author**: @matthewberman | **Rating**: ⭐ 4.7/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that cleans up server response times in Next.js and stops when test coverage reaches 100%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify server response times in Next.js systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Next.js repository. Focus specifically on server response times. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: test coverage reaches 100%.
```

## 🏁 Implementation Steps
1. Scan the Next.js codebase for active server response times.
2. Identify any deviations from the target standard: test coverage reaches 100%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Server response times meets target standards.
- *Detail*: Checked and confirmed that: test coverage reaches 100%.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on server response times to minimize run costs.

## 🏷️ Keywords
next.js, design, cleans up

## 💬 Reviews & Feedback
- **@linus_t** (★★★★☆ 4/5): *Successfully implemented this for Next.js. The verification step is extremely reliable.* (2026-04-07)