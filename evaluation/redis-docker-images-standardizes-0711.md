# The Redis Docker Images Standardizes Loop

**Loop ID**: #0711 | **Category**: Evaluation | **Author**: @vivek34 | **Rating**: ⭐ 4.3/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that standardizes Docker images in Redis and stops when all checks pass successfully.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify Docker images in Redis systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Redis repository. Focus specifically on Docker images. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: all checks pass successfully.
```

## 🏁 Implementation Steps
1. Scan the Redis codebase for active Docker images.
2. Identify any deviations from the target standard: all checks pass successfully.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Docker images meets target standards.
- *Detail*: Checked and confirmed that: all checks pass successfully.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on Docker images to minimize run costs.

## 🏷️ Keywords
redis, evaluation, standardizes

## 💬 Reviews & Feedback
- **@Dis_Trackted** (★★★★☆ 4/5): *Successfully implemented this for Redis. The verification step is extremely reliable.* (2026-01-17)