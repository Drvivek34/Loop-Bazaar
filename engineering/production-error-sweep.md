# The production error sweep

**Loop ID**: #004 | **Category**: Engineering | **Author**: Matthew Berman | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A scheduled production-log workflow that traces actionable errors to root causes, verifies fixes, opens a pull request, and stops cleanly when no action is needed.

## 🎯 Use Case (When to Use)
> Use this as a scheduled reliability pass when an agent can read production telemetry, trace failures into the repository, run the relevant tests, and prepare a reviewable fix.

## ⚡ System Prompt / Instructions
```
Review our production logs for errors. If you find an actionable issue, trace it to its root cause, fix it, verify the fix, and open a pull request. If no actionable errors are present, stop without making changes.
```

## 🏁 Implementation Steps
1. Review the agreed production log window and group repeated symptoms into likely incidents.
2. Separate actionable product errors from expected noise, transient upstream failures, and already-known issues.
3. Trace each actionable error to a root cause, implement the smallest appropriate fix, and verify it with focused checks.
4. Open a pull request for each verified fix. If the logs are clean, stop without making changes.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Actionable production errors are fixed and verified.
- *Detail*: Finish with a pull request, or stop when no actionable errors are present.

## 💡 Why it works
The loop converts passive log review into a closed reliability workflow. It requires a root cause, verified change, and review artifact instead of stopping at a list of errors.

## ⚠️ Implementation Note
* Treat logs as sensitive production data. Do not copy credentials, tokens, personal information, or private payloads into prompts, pull requests, or chat messages.

## 🏷️ Keywords
AI coding agent, production log review, error triage, root cause analysis, reliability workflow

## 💬 Reviews & Feedback
- **@steipete** (★★★★☆ 4/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)