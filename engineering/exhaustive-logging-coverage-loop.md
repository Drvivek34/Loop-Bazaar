# The logging coverage loop

**Loop ID**: #007 | **Category**: Engineering | **Author**: Matthew Berman | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A goal-based observability workflow that audits important paths, adds useful structured logs, and verifies success and failure events with tests.

## 🎯 Use Case (When to Use)
> Use this when important user flows, service boundaries, background jobs, or failure paths are difficult to trace because the system's logging is incomplete or inconsistent.

## ⚡ System Prompt / Instructions
```
Review the system's logging and add missing coverage until every important path produces useful, tested logs.
```

## 🏁 Implementation Steps
1. Inventory the important paths and define the event, outcome, severity, correlation context, and fields each one should emit.
2. Add structured logs to uncovered paths without duplicating events or adding low-value noise.
3. Add tests for successful and failed outcomes, then inspect representative emitted logs for useful context.
4. Verify redaction and repeat until every important path has tested coverage or a documented reason not to log.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every important path emits useful, tested logs.
- *Detail*: Representative success and failure tests prove coverage without exposing sensitive data.

## 💡 Why it works
Treating logging as testable coverage turns observability from scattered statements into a reviewable system requirement. Inspecting emitted events catches gaps that source review alone misses.

## ⚠️ Implementation Note
* Never log credentials, tokens, secrets, or sensitive personal data. Prefer stable event names and structured fields over interpolated prose.

## 🏷️ Keywords
AI coding agent, structured logging, observability coverage, logging tests, production diagnostics

## 💬 Reviews & Feedback
- **@guido_vr** (★★★★★ 5/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)