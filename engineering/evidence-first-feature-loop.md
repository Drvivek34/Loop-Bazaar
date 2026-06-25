# The evidence-first feature loop

**Loop ID**: #068 | **Category**: Engineering | **Author**: Rashid Ali, AI Engineering - DexaMinds | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
An AI coding-agent workflow for grounding one small feature change in current code, APIs, data contracts, and tests before implementation and user-path verification.

## 🎯 Use Case (When to Use)
> Use this when a larger feature can be divided into small engineering slices and guessing about APIs, persistence, or user-visible behavior would create avoidable risk.

## ⚡ System Prompt / Instructions
```
Implement one bounded feature slice in [repository]. Read project instructions, the current implementation, relevant services, types, UI, tests, and architecture notes before editing. Report the evidence, risks, affected files, persistence impact, and validation plan; stop for approval if inspection materially changes scope or reveals destructive, production, or silent-persistence behavior. Make the smallest change, preserve unknown data and unrelated work, run relevant checks, and manually verify user-facing states. Stop after this slice and return evidence, limitations, and the next recommended slice.
```

## 🏁 Implementation Steps
1. Read the project instructions and inspect the current implementation, dependencies, contracts, tests, and relevant architecture notes.
2. State the evidence, risks, files in scope, user-visible behavior, persistence impact, and validation plan for one small slice.
3. Stop for approval if inspection invalidates the approach or reveals a material scope, production, destructive, or silent-persistence change.
4. Implement only the supported slice while preserving unknown fields, round-trip behavior, and unrelated work.
5. Run the relevant repository checks and manually verify loading, error, stale, save, and cleanup states where applicable.
6. Stop after the slice and return the evidence, changed behavior, limitations, and next recommended slice.

## 🛑 Stopping Condition (Verification)
**Verification Check**: One feature slice works and its assumptions are proven by current evidence.
- *Detail*: The implementation matches observed APIs and data contracts, repository checks pass or have documented pre-existing failures, and the relevant user path is manually verified when one exists.

## 💡 Why it works
Inspecting real contracts before coding prevents plausible but invented APIs or data behavior from shaping the implementation. Limiting each pass to one feature slice keeps review, verification, and persistence effects understandable.

## ⚠️ Implementation Note
* Do not silently save user data, invent endpoints or data shapes, hide unavailable checks, or continue into another feature slice without approval. Keep previews honest about whether they show draft state or source-of-truth backend output.

## 🏷️ Keywords
evidence-first engineering, feature implementation, AI coding agent, repository inspection, bounded development

## 💬 Reviews & Feedback
- *No reviews yet.*