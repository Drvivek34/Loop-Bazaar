# The free API offer verification loop

**Loop ID**: #5065 | **Category**: Evaluation | **Author**: Drvivek34 | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable catalog-maintenance workflow for checking current free-tier claims against first-party pricing and limits pages before publishing or renewing an API offer.

## 🎯 Use Case (When to Use)
> Use this when provider quotas, credits, model availability, billing requirements, or signup links may have changed since the last review.

## ⚡ System Prompt / Instructions
```
For each provider in scope, open the first-party pricing, limits, and API documentation pages. Record the exact free quota, reset window, card or billing requirement, supported models, compatibility details, and the date verified. Compare the new evidence with the existing entry, update only claims supported by the source, mark changed or unavailable offers as deprecated rather than deleting them, and preserve the source URL and a concise verification note.
```

## 🏁 Implementation Steps
1. Load the existing provider list and select entries due for review or newly discovered from current sources.
2. Open first-party pricing, limits, model, and signup documentation and capture the relevant evidence.
3. Compare the evidence to the catalog entry, separating permanent free tiers, trial credits, and promotional claims.
4. Update or add only entries with a source, preserve attribution, and mark changed or dead offers deprecated instead of deleting them.
5. Run link and schema checks, summarize changes, and stop when the review budget or evidence boundary is reached.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every published free-offer claim has current first-party evidence or is explicitly marked uncertain/deprecated.
- *Detail*: The verification report contains provider, source URLs, retrieved date, exact quota text, billing/card status, changed fields, and a stop reason for blocked or ambiguous sources.

## 💡 Why it works
Free-tier claims change frequently and secondary lists go stale. Requiring first-party evidence and explicit verification dates makes the catalog useful without overstating offers.

## ⚠️ Implementation Note
* Do not create accounts, enter payment details, or infer quotas from an inaccessible dashboard. Treat dynamic or region-specific offers as conditional.

## 🏷️ Keywords
free API, quota verification, pricing audit, first-party sources, catalog maintenance

## 💬 Reviews & Feedback
- *No reviews yet.*