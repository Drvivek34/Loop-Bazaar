# PRD-completion autonomous loop

**Loop ID**: #5058 | **Category**: Engineering | **Author**: snarktank (Ralph) | **Rating**: ⭐ 4.6/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
Run an agent loop that works through a PRD checklist, repeating until every item is complete.

## 🎯 Use Case (When to Use)
> When you have a structured PRD/checklist to drive autonomous build.

## ⚡ System Prompt / Instructions
```
Read the PRD. Pick the next incomplete item, implement and verify it, mark it done, and continue until all items are complete.
```

## 🏁 Implementation Steps
1. Load the PRD checklist
2. Select next incomplete item
3. Implement + verify it
4. Mark done and loop until none remain

## 🛑 Stopping Condition (Verification)
**Verification Check**: Checklist complete
- *Detail*: Every PRD item is implemented and verified.

## 💡 Why it works
A persistent checklist gives the loop an unambiguous stop condition.

## ⚠️ Implementation Note
* Curated real-world loop with original source attribution.

## 🏷️ Keywords
prd, checklist, autonomous, ralph

## 💬 Reviews & Feedback
- *No reviews yet.*