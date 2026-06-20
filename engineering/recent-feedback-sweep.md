# The recent-feedback sweep

**Loop ID**: #031 | **Category**: Engineering | **Author**: Matthew Berman | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A project audit that turns recent user-reported problems into reusable failure patterns, fixes every confirmed match, and verifies a clean final sweep.

## 🎯 Use Case (When to Use)
> Use this after several days of project feedback when repeated mistakes may point to similar issues elsewhere and the agent can inspect both the conversation history and the complete current project.

## ⚡ System Prompt / Instructions
```
Review all available threads from [lookback window] where I reported something wrong with [project] and asked for a fix. Build a deduplicated issue list, group it into failure patterns, and verify current state. Audit the complete project for every pattern, fix each confirmed instance, and add regression coverage where practical. Repeat the full audit until it finds no remaining instance or [iteration budget] ends. Stop on blocked or approval-gated work. Return the issues, fixes, evidence, and blockers.
```

## 🏁 Implementation Steps
1. Define the lookback window and complete project surface, then collect every accessible thread in which the user reported a problem and requested a fix.
2. Deduplicate the reported issues, verify their current status, and turn the concrete examples into explicit failure patterns and audit checks.
3. Audit every in-scope project surface for each pattern, fix one confirmed instance at a time, and add regression coverage where practical.
4. Run targeted checks after each fix, then rerun the complete pattern audit and relevant full checks before declaring the sweep clean.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The issue inventory is closed and a fresh pattern audit is clean.
- *Detail*: Every reported issue and newly found match has current proof of resolution; blocked, approval-gated, or budget-exhausted items remain explicitly open.

## 💡 Why it works
Recent corrections are concrete examples of the quality bar the project missed. Grouping them into failure patterns turns one-off feedback into a reusable audit rubric, while a fresh full sweep catches sibling defects and verifies the current project rather than trusting old thread state.

## ⚠️ Implementation Note
* Thread access and a complete surface inventory are prerequisites. Do not infer defects from neutral discussion, reopen resolved issues without checking current behavior, or claim success while an inaccessible, blocked, approval-gated, or budget-exhausted item remains. Get approval before destructive, production, or external actions.

## 🏷️ Keywords
recent user feedback, project-wide issue audit, failure pattern sweep, regression prevention, AI coding agent

## 💬 Reviews & Feedback
- **@steipete** (★★★★★ 5/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)