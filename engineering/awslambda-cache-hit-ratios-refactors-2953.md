# The AWS Lambda Cache Hit Ratios Refactors Loop

**Loop ID**: #2953 | **Category**: Engineering | **Author**: @richard_s | **Rating**: ⭐ 4.1/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that refactors cache hit ratios in AWS Lambda and stops when API response time is under 100ms.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify cache hit ratios in AWS Lambda systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the AWS Lambda repository. Focus specifically on cache hit ratios. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: API response time is under 100ms.
```

## 🏁 Implementation Steps
1. Scan the AWS Lambda codebase for active cache hit ratios.
2. Identify any deviations from the target standard: API response time is under 100ms.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Cache hit ratios meets target standards.
- *Detail*: Checked and confirmed that: API response time is under 100ms.

## 💡 Why it works
This loop works because it creates a clear evidence trail of system changes and performance checks.

## ⚠️ Implementation Note
* Keep the scope focused on cache hit ratios to minimize run costs.

## 🏷️ Keywords
aws lambda, engineering, refactors

## 💬 Reviews & Feedback
- **@swayam** (★★★★☆ 4/5): *Successfully implemented this for AWS Lambda. The verification step is extremely reliable.* (2026-02-01)