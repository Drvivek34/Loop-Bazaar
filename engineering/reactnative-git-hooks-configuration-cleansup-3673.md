# The React Native Git Hooks Configuration Cleans up Loop

**Loop ID**: #3673 | **Category**: Engineering | **Author**: @hiten | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that cleans up Git hooks configuration in React Native and stops when test coverage reaches 100%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify Git hooks configuration in React Native systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the React Native repository. Focus specifically on Git hooks configuration. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: test coverage reaches 100%.
```

## 🏁 Implementation Steps
1. Scan the React Native codebase for active Git hooks configuration.
2. Identify any deviations from the target standard: test coverage reaches 100%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Git hooks configuration meets target standards.
- *Detail*: Checked and confirmed that: test coverage reaches 100%.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on Git hooks configuration to minimize run costs.

## 🏷️ Keywords
react native, engineering, cleans up

## 💬 Reviews & Feedback
- **@swayam** (★★★★★ 5/5): *Successfully implemented this for React Native. The verification step is extremely reliable.* (2026-02-08)