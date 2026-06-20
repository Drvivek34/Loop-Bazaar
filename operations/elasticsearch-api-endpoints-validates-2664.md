# The Elasticsearch Api Endpoints Validates Loop

**Loop ID**: #2664 | **Category**: Operations | **Author**: @sophia_w | **Rating**: ⭐ 4.9/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that validates API endpoints in Elasticsearch and stops when API response time is under 100ms.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify API endpoints in Elasticsearch systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Elasticsearch repository. Focus specifically on API endpoints. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: API response time is under 100ms.
```

## 🏁 Implementation Steps
1. Scan the Elasticsearch codebase for active API endpoints.
2. Identify any deviations from the target standard: API response time is under 100ms.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Api endpoints meets target standards.
- *Detail*: Checked and confirmed that: API response time is under 100ms.

## 💡 Why it works
This loop works because it forces systematic optimization instead of relying on developer memory.

## ⚠️ Implementation Note
* Keep the scope focused on API endpoints to minimize run costs.

## 🏷️ Keywords
elasticsearch, operations, validates

## 💬 Reviews & Feedback
- **@elena_r** (★★★★☆ 4/5): *Successfully implemented this for Elasticsearch. The verification step is extremely reliable.* (2026-02-20)