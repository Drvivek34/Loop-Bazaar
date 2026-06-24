# The pre-publish source-check loop

**Loop ID**: #062 | **Category**: Content | **Author**: Ryan Banze (@RyanBanze) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A bounded editorial verification loop that inventories checkable claims, checks primary sources, repairs high-risk mismatches, and records unresolved decisions.

## 🎯 Use Case (When to Use)
> Use this immediately before publishing an article, newsletter, post, report, or other factual draft whose claims, quotations, and attributions need a final evidence check.

## ⚡ System Prompt / Instructions
```
Before publishing [draft], inventory every factual, statistical, quoted, or attributed claim a reader could verify. Find the best current primary source for each and label it supported, outdated, misattributed, unsupported, or unverifiable. Fix the riskiest mismatch, then recheck that claim and anything depending on it. Repeat until no high-risk unsupported claim remains or five rounds are exhausted. Never invent a source, cite evidence that does not support the claim, or alter a quotation. Ask before changing a named person’s quote or a legal, medical, or financial statement. Stop without changes if there are no checkable claims; stop as blocked when adequate evidence is unavailable. Finish with the claim-to-source table, corrections made, unresolved claims, and decisions requiring an editor.
```

## 🏁 Implementation Steps
1. Inventory every factual, statistical, quoted, and attributed claim.
2. Check each claim against the best available current primary source.
3. Repair the riskiest mismatch and recheck dependent claims.
4. Repeat within the five-round budget until the evidence gate passes.
5. Deliver the claim-to-source table and unresolved editorial decisions.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every checkable claim is supported or visibly flagged.
- *Detail*: The final claim-to-source table traces each checkable claim to current supporting evidence or marks it for an editor, with no high-risk unsupported claim silently left in the draft.

## 💡 Why it works
Claim-level verification prevents a polished draft from hiding unsupported facts, stale numbers, incorrect attribution, or citations that do not actually support the text.

## ⚠️ Implementation Note
* Primary sources are not always available. Flag the limitation instead of substituting weak evidence or presenting an unverifiable claim as confirmed.

## 🏷️ Keywords
pre-publish fact check, source verification, editorial accuracy, claim audit, primary source research

## 💬 Reviews & Feedback
- *No reviews yet.*