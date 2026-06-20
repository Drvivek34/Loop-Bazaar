# The Kubernetes Database Queries Debugs Loop

**Loop ID**: #1361 | **Category**: Design | **Author**: @ken_t | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that debugs database queries in Kubernetes and stops when performance benchmark is met.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify database queries in Kubernetes systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Kubernetes repository. Focus specifically on database queries. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: performance benchmark is met.
```

## 🏁 Implementation Steps
1. Scan the Kubernetes codebase for active database queries.
2. Identify any deviations from the target standard: performance benchmark is met.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Database queries meets target standards.
- *Detail*: Checked and confirmed that: performance benchmark is met.

## 💡 Why it works
This loop works because it forces systematic optimization instead of relying on developer memory.

## ⚠️ Implementation Note
* Keep the scope focused on database queries to minimize run costs.

## 🏷️ Keywords
kubernetes, design, debugs

## 💬 Reviews & Feedback
- **@grace_hopper** (★★★★☆ 4/5): *Successfully implemented this for Kubernetes. The verification step is extremely reliable.* (2026-06-16)