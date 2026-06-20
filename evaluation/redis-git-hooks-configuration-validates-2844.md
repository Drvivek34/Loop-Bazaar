# The Redis Git Hooks Configuration Validates Loop

**Loop ID**: #2844 | **Category**: Evaluation | **Author**: @lucas_k | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that validates Git hooks configuration in Redis and stops when API response time is under 100ms.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify Git hooks configuration in Redis systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Redis repository. Focus specifically on Git hooks configuration. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: API response time is under 100ms.
```

## 🏁 Implementation Steps
1. Scan the Redis codebase for active Git hooks configuration.
2. Identify any deviations from the target standard: API response time is under 100ms.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Git hooks configuration meets target standards.
- *Detail*: Checked and confirmed that: API response time is under 100ms.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on Git hooks configuration to minimize run costs.

## 🏷️ Keywords
redis, evaluation, validates

## 💬 Reviews & Feedback
- **@ken_t** (★★★★★ 5/5): *Successfully implemented this for Redis. The verification step is extremely reliable.* (2026-02-13)