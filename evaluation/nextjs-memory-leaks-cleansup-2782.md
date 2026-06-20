# The Next.js Memory Leaks Cleans up Loop

**Loop ID**: #2782 | **Category**: Evaluation | **Author**: @bjarnes | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that cleans up memory leaks in Next.js and stops when all vulnerabilities are resolved.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify memory leaks in Next.js systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Next.js repository. Focus specifically on memory leaks. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: all vulnerabilities are resolved.
```

## 🏁 Implementation Steps
1. Scan the Next.js codebase for active memory leaks.
2. Identify any deviations from the target standard: all vulnerabilities are resolved.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Memory leaks meets target standards.
- *Detail*: Checked and confirmed that: all vulnerabilities are resolved.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on memory leaks to minimize run costs.

## 🏷️ Keywords
next.js, evaluation, cleans up

## 💬 Reviews & Feedback
- **@victormustar** (★★★★☆ 4/5): *Successfully implemented this for Next.js. The verification step is extremely reliable.* (2026-05-19)