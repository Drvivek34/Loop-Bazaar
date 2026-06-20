# The NestJS Bundle Sizes Debugs Loop

**Loop ID**: #2363 | **Category**: Evaluation | **Author**: @0xUmbra | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that debugs bundle sizes in NestJS and stops when no regressions are detected.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify bundle sizes in NestJS systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the NestJS repository. Focus specifically on bundle sizes. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: no regressions are detected.
```

## 🏁 Implementation Steps
1. Scan the NestJS codebase for active bundle sizes.
2. Identify any deviations from the target standard: no regressions are detected.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Bundle sizes meets target standards.
- *Detail*: Checked and confirmed that: no regressions are detected.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on bundle sizes to minimize run costs.

## 🏷️ Keywords
nestjs, evaluation, debugs

## 💬 Reviews & Feedback
- **@agent0ai** (★★★★☆ 4/5): *Successfully implemented this for NestJS. The verification step is extremely reliable.* (2026-02-07)