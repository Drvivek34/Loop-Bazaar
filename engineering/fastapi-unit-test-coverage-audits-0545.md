# The FastAPI Unit Test Coverage Audits Loop

**Loop ID**: #0545 | **Category**: Engineering | **Author**: @tim_berners | **Rating**: ⭐ 4.1/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that audits unit test coverage in FastAPI and stops when API response time is under 100ms.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify unit test coverage in FastAPI systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the FastAPI repository. Focus specifically on unit test coverage. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: API response time is under 100ms.
```

## 🏁 Implementation Steps
1. Scan the FastAPI codebase for active unit test coverage.
2. Identify any deviations from the target standard: API response time is under 100ms.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Unit test coverage meets target standards.
- *Detail*: Checked and confirmed that: API response time is under 100ms.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on unit test coverage to minimize run costs.

## 🏷️ Keywords
fastapi, engineering, audits

## 💬 Reviews & Feedback
- **@tim_berners** (★★★★☆ 4/5): *Successfully implemented this for FastAPI. The verification step is extremely reliable.* (2026-03-15)