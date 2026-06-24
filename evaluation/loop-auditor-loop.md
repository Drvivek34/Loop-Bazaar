# The loop-auditor loop

**Loop ID**: #058 | **Category**: Evaluation | **Author**: quigleyBits (@quigleyBits) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A read-only portfolio audit that recomputes measured-loop performance, evaluates operational loops on their own terms, and recommends what should continue.

## 🎯 Use Case (When to Use)
> Use this when several active loops need a read-only portfolio review to determine which should continue, change, retire after success, or stop wasting budget.

## ⚡ System Prompt / Instructions
```
Audit [supplied loops or loop registry] without running or editing any loop. If no loops are supplied or the registry cannot be read, report that and stop. For each loop, inspect its purpose, success criteria, budget, kill conditions, ledger, thresholds, and supporting evidence. Assign INSUFFICIENT EVIDENCE when required information is missing. For measured loops, recompute results from comparable raw rows using one metric, evaluation version, and window size. Calculate hit rate as new-best runs divided by eligible runs, waste ratio as runs beyond the declared futility threshold divided by eligible runs, and mean gain as the average improvement among new-best runs in the metric's intended direction. Compare the current window with the previous two comparable windows. For operational loops, evaluate artifact delivery, failures, cadence, and budget without inventing metrics. Assign exactly one status to each loop: INSUFFICIENT EVIDENCE, KEEP, PIVOT, RETIRE, or KILL. Recommend only. Stop after every supplied loop has one evidence-backed status. Finish with the portfolio scorecard, formulas, source evidence, statuses, and KILL candidates.
```

## 🏁 Implementation Steps
1. Read each loop's purpose, success criteria, budget, kill conditions, ledger, thresholds, and available evidence.
2. Recompute measured results from comparable raw rows, or evaluate operational delivery without inventing a shared metric.
3. Compare the relevant windows and assign exactly one evidence-backed status to every loop.
4. Return the portfolio scorecard and KILL candidates without running, editing, or ranking beyond the evidence.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every supplied loop has exactly one status supported by comparable evidence.
- *Detail*: The scorecard shows formulas, raw sources or artifacts, the evaluation version and window, and no invented metric or silently unclassified loop.

## 💡 Why it works
A loop can keep consuming time after it has succeeded, stalled, or stopped producing useful gains. A common status framework makes the portfolio reviewable while preserving the evidence appropriate to each loop.

## ⚠️ Implementation Note
* Do not run, edit, or compare unlike loops on a fabricated shared scale. Missing raw rows, thresholds, or budgets must produce INSUFFICIENT EVIDENCE rather than a guessed status.

## 🏷️ Keywords
loop auditor, agent workflow evaluation, automation portfolio, kill condition, waste ratio

## 💬 Reviews & Feedback
- *No reviews yet.*