# The Elasticsearch Unused Imports Cleans up Loop

**Loop ID**: #3451 | **Category**: Content | **Author**: @victormustar | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that cleans up unused imports in Elasticsearch and stops when error rate drops below 0.1%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify unused imports in Elasticsearch systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Elasticsearch repository. Focus specifically on unused imports. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: error rate drops below 0.1%.
```

## 🏁 Implementation Steps
1. Scan the Elasticsearch codebase for active unused imports.
2. Identify any deviations from the target standard: error rate drops below 0.1%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Unused imports meets target standards.
- *Detail*: Checked and confirmed that: error rate drops below 0.1%.

## 💡 Why it works
This loop works because it ensures security policies are consistently enforced without gaps.

## ⚠️ Implementation Note
* Keep the scope focused on unused imports to minimize run costs.

## 🏷️ Keywords
elasticsearch, content, cleans up

## 💬 Reviews & Feedback
- **@vivek34** (★★★★☆ 4/5): *Successfully implemented this for Elasticsearch. The verification step is extremely reliable.* (2026-03-25)