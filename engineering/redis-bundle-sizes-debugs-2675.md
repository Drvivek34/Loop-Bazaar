# The Redis Bundle Sizes Debugs Loop

**Loop ID**: #2675 | **Category**: Engineering | **Author**: @ken_t | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that debugs bundle sizes in Redis and stops when compliance report returns zero warnings.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify bundle sizes in Redis systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Redis repository. Focus specifically on bundle sizes. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: compliance report returns zero warnings.
```

## 🏁 Implementation Steps
1. Scan the Redis codebase for active bundle sizes.
2. Identify any deviations from the target standard: compliance report returns zero warnings.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Bundle sizes meets target standards.
- *Detail*: Checked and confirmed that: compliance report returns zero warnings.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on bundle sizes to minimize run costs.

## 🏷️ Keywords
redis, engineering, debugs

## 💬 Reviews & Feedback
- **@ranvier2d2** (★★★★☆ 4/5): *Successfully implemented this for Redis. The verification step is extremely reliable.* (2026-03-04)