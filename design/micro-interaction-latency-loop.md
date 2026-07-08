# The micro-interaction latency loop

**Loop ID**: #077 | **Category**: Design | **Author**: Tushar Kalan (@DilSalaKamina) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A design-system workflow that checks interaction timing tokens and component specs against latency thresholds, fixes the highest-severity violation, and records compliance evidence.

## 🎯 Use Case (When to Use)
> Use this when a design system needs motion and interaction timing to stay consistent, responsive, and token-driven across components.

## ⚡ System Prompt / Instructions
```
When motion tokens or interaction specs change, audit every interactive component against the current timing rules. Extract token values, find hardcoded timings, map each component to its motion token, and flag hover or click feedback above 100 ms, page transitions above 1000 ms, async operations above 1000 ms without a loading indicator, and any hardcoded timing. Fix the highest-severity violation by updating tokens or specs, then rerun the same compliance check. Stop when no violations remain, a product decision blocks the fix, or the agreed review scope is complete.
```

## 🏁 Implementation Steps
1. Load current motion tokens and interaction specs, then extract timing references for each component.
2. Classify feedback, transition, async, and hardcoded-timing violations against the chosen latency rules.
3. Choose the highest-severity fix that can be made without changing product intent.
4. Update the relevant token or spec and rerun the full compliance check.
5. Record the audit trail and stop at full compliance, blocker, or completed scope.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The interaction audit reports zero timing violations or explicit blockers.
- *Detail*: The final audit lists each component, original timing, token reference, violation type, fix, compliance status, and any blocker that requires product judgment.

## 💡 Why it works
Small latency inconsistencies accumulate into a sluggish product; tying components to tokens and rerunning the same audit keeps interaction feel measurable.

## ⚠️ Implementation Note
* Do not mask real server latency with fake compliance. If product or infrastructure constraints block the fix, record the blocker instead of forcing a token change.

## 🏷️ Keywords
micro interaction latency, motion tokens, interaction specs, design system timing, loading indicator

## 💬 Reviews & Feedback
- *No reviews yet.*