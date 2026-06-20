# The Redis Bundle Sizes Validates Loop

**Loop ID**: #4890 | **Category**: Evaluation | **Author**: @richard_s | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that validates bundle sizes in Redis and stops when all vulnerabilities are resolved.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify bundle sizes in Redis systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Redis repository. Focus specifically on bundle sizes. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: all vulnerabilities are resolved.
```

## 🏁 Implementation Steps
1. Scan the Redis codebase for active bundle sizes.
2. Identify any deviations from the target standard: all vulnerabilities are resolved.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Bundle sizes meets target standards.
- *Detail*: Checked and confirmed that: all vulnerabilities are resolved.

## 💡 Why it works
This loop works because it automates routine maintenance task and flags exceptions for review.

## ⚠️ Implementation Note
* Keep the scope focused on bundle sizes to minimize run costs.

## 🏷️ Keywords
redis, evaluation, validates

## 💬 Reviews & Feedback
- **@dennis_r** (★★★★☆ 4/5): *Successfully implemented this for Redis. The verification step is extremely reliable.* (2026-03-04)