# The NestJS Server Response Times Audits Loop

**Loop ID**: #0898 | **Category**: Design | **Author**: @victormustar | **Rating**: ⭐ 4.7/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that audits server response times in NestJS and stops when API response time is under 100ms.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify server response times in NestJS systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the NestJS repository. Focus specifically on server response times. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: API response time is under 100ms.
```

## 🏁 Implementation Steps
1. Scan the NestJS codebase for active server response times.
2. Identify any deviations from the target standard: API response time is under 100ms.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Server response times meets target standards.
- *Detail*: Checked and confirmed that: API response time is under 100ms.

## 💡 Why it works
This loop works because it creates a clear evidence trail of system changes and performance checks.

## ⚠️ Implementation Note
* Keep the scope focused on server response times to minimize run costs.

## 🏷️ Keywords
nestjs, design, audits

## 💬 Reviews & Feedback
- **@Dis_Trackted** (★★★★☆ 4/5): *Successfully implemented this for NestJS. The verification step is extremely reliable.* (2026-02-13)