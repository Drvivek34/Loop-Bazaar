# The production data cleanup loop

**Loop ID**: #014 | **Category**: Operations | **Author**: Matthew Berman | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A production-data quality workflow that removes disallowed records, improves classification logic, and verifies the remaining dataset against an explicit definition.

## 🎯 Use Case (When to Use)
> Use this when a production dataset contains records that no longer match a product, policy, taxonomy, or quality definition and the classifier allowed them through.

## ⚡ System Prompt / Instructions
```
Review production records, remove anything that does not meet the allowed definition, improve the classification logic, and verify the remaining data.
```

## 🏁 Implementation Steps
1. Write the allowed definition as explicit inclusion, exclusion, and edge-case rules before changing data.
2. Audit production records, preserve a recoverable record of proposed removals, and separate clear violations from uncertain cases.
3. Remove confirmed invalid records through the approved production path and improve the classifier with regression examples.
4. Rerun classification tests and audit the remaining production data until every sampled and queried record meets the definition.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every remaining record meets the allowed definition.
- *Detail*: Representative classification tests and a post-cleanup audit prove the retained data is valid.

## 💡 Why it works
Fixing both the existing records and the classifier closes the immediate data problem and reduces recurrence. Explicit rules and regression examples make future cleanup decisions reviewable.

## ⚠️ Implementation Note
* Follow access, retention, privacy, and audit requirements. Use backups or reversible operations where appropriate, and do not delete uncertain records without review.

## 🏷️ Keywords
AI data operations, production data cleanup, classification logic, data quality audit, regression examples

## 💬 Reviews & Feedback
- **@victormustar** (★★★★☆ 4/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)