# Explore → Plan → Code → Commit

**Loop ID**: #5056 | **Category**: Engineering | **Author**: Anthropic | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
The recommended Claude Code working loop: read context, make a plan, implement, then commit — repeating per unit of work.

## 🎯 Use Case (When to Use)
> Default loop for agentic coding tasks in a real repo.

## ⚡ System Prompt / Instructions
```
First explore the relevant files without editing. Then write a plan. Then implement the change. Then verify and commit. Repeat for the next unit.
```

## 🏁 Implementation Steps
1. Explore: read relevant code, don't edit yet
2. Plan: outline the approach
3. Code: implement the smallest correct change
4. Verify and commit

## 🛑 Stopping Condition (Verification)
**Verification Check**: Reviewable commit
- *Detail*: Change verified and committed with a clear message.

## 💡 Why it works
Separating exploration and planning from editing produces better, reviewable changes.

## ⚠️ Implementation Note
* Curated real-world loop with original source attribution.

## 🏷️ Keywords
claude code, workflow, plan, commit

## 💬 Reviews & Feedback
- *No reviews yet.*