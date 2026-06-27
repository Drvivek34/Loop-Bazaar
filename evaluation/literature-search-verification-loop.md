# The literature-search verification loop

**Loop ID**: #070 | **Category**: Evaluation | **Author**: Nathan Nguyen | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A bounded literature-search workflow that deduplicates papers across live sources, verifies DOI metadata, measures topical relevance, and stops honestly when evidence is insufficient.

## 🎯 Use Case (When to Use)
> Use this when a literature search must produce a high-precision, auditable paper set rather than an unverified list of citations.

## ⚡ System Prompt / Instructions
```
Search the current PubMed and Semantic Scholar APIs for papers about [topic] and produce a DOI-verified CSV. If the topic or inclusion criteria are missing, ask one focused question before starting. Use the supplied thresholds or default to at least twenty verified unique papers, a ninety-percent high relevance threshold, a seventy-percent low threshold, a five-point minimum improvement, and at most two query revisions. Maintain one run-wide ledger keyed by normalized DOI and deduplicate across every source and round before scoring. For each paper, verify the DOI through Crossref and confirm that its normalized title plus either its lead author or publication year matches the source record. Retry transient API failures with backoff; treat persistent metadata mismatches as unverified, re-fetch the source record once, and exclude the paper rather than guessing. Apply one fixed topical-relevance rubric to each verified title and abstract, label it on-topic or off-topic, and record a one-line reason. Never change the rubric during the run. Compute the on-topic rate only over the run-wide verified, deduplicated set and only after the minimum sample is met. Succeed when the set reaches the high threshold. Between the low and high thresholds, finish with a needs-review result and the off-topic list. Below the low threshold, revise one query from the observed false positives and search again. Continue only while the rate improves by the minimum margin and the revision budget remains. Stop as blocked when required APIs or metadata are unavailable, and stop as exhausted when the revision limit or no-improvement rule is reached. Never invent, infer, or autocomplete paper metadata. Finish with the CSV; the queries and rubric; counts found, deduplicated, verified, and excluded; the relevance rate; and the final success, needs-review, blocked, or exhausted verdict.
```

## 🏁 Implementation Steps
1. Define the topic, inclusion rubric, minimum sample, relevance thresholds, improvement margin, and query-revision budget.
2. Search PubMed and Semantic Scholar, normalize every DOI, and deduplicate all results in one run-wide ledger.
3. Verify DOI metadata against Crossref, exclude unresolved mismatches, and score verified papers with the unchanged relevance rubric.
4. Measure the verified set and revise one query only when the result is below the low threshold and measurable improvement remains possible.
5. Return the CSV, evidence ledger, metrics, exclusions, query history, and an honest terminal verdict.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The minimum-size literature set clears its relevance gate with matched DOI metadata.
- *Detail*: Every retained row is unique across the full run, its DOI metadata matches the source record, its relevance decision follows the fixed rubric, and the final verdict follows the recorded sample size, rate, and retry budget.

## 💡 Why it works
Literature searches can look authoritative while containing duplicate, mistyped, invented, or irrelevant citations. A run-wide ledger, metadata matching, fixed rubric, minimum sample, and bounded query revisions make the result auditable without rewarding a tiny or cherry-picked set.

## ⚠️ Implementation Note
* Use current public bibliographic metadata and respect each API's access and rate limits. Do not infer missing abstracts or treat a network failure as evidence that a DOI is invalid.

## 🏷️ Keywords
literature search verification, DOI metadata validation, PubMed research workflow, Semantic Scholar search, Crossref verification, research CSV

## 💬 Reviews & Feedback
- *No reviews yet.*