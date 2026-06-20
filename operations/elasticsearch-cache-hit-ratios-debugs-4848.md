# The Elasticsearch Cache Hit Ratios Debugs Loop

**Loop ID**: #4848 | **Category**: Operations | **Author**: @guido_vr | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that debugs cache hit ratios in Elasticsearch and stops when target threshold is reached.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify cache hit ratios in Elasticsearch systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Elasticsearch repository. Focus specifically on cache hit ratios. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: target threshold is reached.
```

## 🏁 Implementation Steps
1. Scan the Elasticsearch codebase for active cache hit ratios.
2. Identify any deviations from the target standard: target threshold is reached.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Cache hit ratios meets target standards.
- *Detail*: Checked and confirmed that: target threshold is reached.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on cache hit ratios to minimize run costs.

## 🏷️ Keywords
elasticsearch, operations, debugs

## 💬 Reviews & Feedback
- **@claudio_d** (★★★★★ 5/5): *Successfully implemented this for Elasticsearch. The verification step is extremely reliable.* (2026-04-18)