# The promise-to-proof loop

**Loop ID**: #032 | **Category**: Evaluation | **Author**: Felix Haeberle (@felixhaberle) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A product review that compares claims in marketing, documentation, demos, and AI answers with current evidence, then fixes or narrows unsupported promises.

## 🎯 Use Case (When to Use)
> Use this when what a product says it does may no longer match what it actually does across marketing, documentation, demos, support answers, or the live product.

## ⚡ System Prompt / Instructions
```
List every customer-facing promise [product] makes in marketing, documentation, demos, and AI answers. Compare each promise with current product behavior and evidence, then label it proven, partly proven, misleading, unsupported, outdated, or missing evidence. Fix or narrow the riskiest mismatch and rerun the affected check. Repeat until no high-risk unsupported promise remains. Ask before changing production or public copy. Return the promises, evidence, fixes, and decisions needed.
```

## 🏁 Implementation Steps
1. List the promises customers can see and rewrite each one as a concrete expectation, such as a feature working, a limit being honored, or an answer being accurate.
2. Compare each expectation with current product behavior, code, tests, documentation, examples, logs, or other direct evidence; do not guess.
3. Rank mismatches by the harm they could do to customer trust, then fix the riskiest one or narrow the public promise to what the product can prove.
4. Rerun the same check and repeat until no high-risk unsupported promise remains, progress is blocked, or the next action needs approval.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every high-risk customer promise is supported, narrowed, or waiting on an explicit decision.
- *Detail*: Each promise links to current evidence, and every high-risk mismatch is fixed, narrowed to what the product can prove, or clearly approval-gated.

## 💡 Why it works
This turns a vague question—can customers trust what we say?—into a list of promises that can each be checked. Fixing one risky mismatch at a time keeps the product and its public explanation aligned without turning the audit into an uncontrolled rewrite.

## ⚠️ Implementation Note
* Evidence can include live product behavior, tests, documentation, logs, screenshots, or reproducible examples. A promise may be supported, narrowed, or removed; the product does not always need to change. Production changes and public publication still require approval.

## 🏷️ Keywords
product promise audit, customer trust, claim verification, evidence based product review, marketing product alignment

## 💬 Reviews & Feedback
- *No reviews yet.*