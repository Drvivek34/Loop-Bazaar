# The AWS Lambda Security Groups Profiles Loop

**Loop ID**: #1233 | **Category**: Content | **Author**: @swayam | **Rating**: ⭐ 4.6/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that profiles security groups in AWS Lambda and stops when performance benchmark is met.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify security groups in AWS Lambda systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the AWS Lambda repository. Focus specifically on security groups. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: performance benchmark is met.
```

## 🏁 Implementation Steps
1. Scan the AWS Lambda codebase for active security groups.
2. Identify any deviations from the target standard: performance benchmark is met.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Security groups meets target standards.
- *Detail*: Checked and confirmed that: performance benchmark is met.

## 💡 Why it works
This loop works because it creates a clear evidence trail of system changes and performance checks.

## ⚠️ Implementation Note
* Keep the scope focused on security groups to minimize run costs.

## 🏷️ Keywords
aws lambda, content, profiles

## 💬 Reviews & Feedback
- **@guido_vr** (★★★★☆ 4/5): *Successfully implemented this for AWS Lambda. The verification step is extremely reliable.* (2026-03-30)