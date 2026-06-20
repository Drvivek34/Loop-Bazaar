# The AWS Lambda Security Groups Optimizes Loop

**Loop ID**: #4433 | **Category**: Evaluation | **Author**: @ken_t | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that optimizes security groups in AWS Lambda and stops when documentation is fully aligned with implementation.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify security groups in AWS Lambda systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the AWS Lambda repository. Focus specifically on security groups. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: documentation is fully aligned with implementation.
```

## 🏁 Implementation Steps
1. Scan the AWS Lambda codebase for active security groups.
2. Identify any deviations from the target standard: documentation is fully aligned with implementation.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Security groups meets target standards.
- *Detail*: Checked and confirmed that: documentation is fully aligned with implementation.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on security groups to minimize run costs.

## 🏷️ Keywords
aws lambda, evaluation, optimizes

## 💬 Reviews & Feedback
- **@lucas_k** (★★★★☆ 4/5): *Successfully implemented this for AWS Lambda. The verification step is extremely reliable.* (2026-04-24)