# The cost-reduction loop

**Loop ID**: #080 | **Category**: Operations | **Author**: AKT (@akt199009) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
An operations workflow that attributes current spend, applies one approved savings change, and keeps it only when cost drops without guardrail regressions.

## 🎯 Use Case (When to Use)
> Use this when cloud, API, infrastructure, model, or operational spend needs to decrease while reliability and correctness must remain protected.

## ⚡ System Prompt / Instructions
```
Reduce spend on the target system toward the agreed budget without weakening correctness, performance, reliability, or service-level objectives. First read current cost and usage, then attribute spend to the largest drivers. Each pass, propose the single highest-saving safe change and get approval before any billing, infrastructure, production, or user-impacting change. Apply the change only within that authority, then measure cost and guardrail metrics over the agreed window. Keep it only if cost drops and no guardrail regresses. Stop at budget, no safe saving remains, no measurable progress, blocked access, or approval need.
```

## 🏁 Implementation Steps
1. Read current cost and usage data, then attribute spend to the largest drivers.
2. Choose the single highest-saving safe change for the next pass.
3. Get approval before billing, infrastructure, production, or user-impacting changes.
4. Measure cost and guardrail metrics over the same window after the change.
5. Keep only changes that save money without regressions and stop at budget, no safe saving, blocker, or no progress.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Each retained cost change lowers spend without guardrail regression.
- *Detail*: The final receipt includes baseline cost, usage drivers, proposed changes, approvals, cost deltas, guardrail metrics, measurement windows, reverted or rejected changes, and stopping reason.

## 💡 Why it works
Cost cuts can quietly break reliability or correctness; this loop makes every saving compete against explicit guardrail metrics.

## ⚠️ Implementation Note
* Do not change plans, quotas, infrastructure, production routing, data retention, or paid services without explicit authority.

## 🏷️ Keywords
cost reduction, cloud spend, guardrail metrics, operations savings, budget optimization

## 💬 Reviews & Feedback
- *No reviews yet.*