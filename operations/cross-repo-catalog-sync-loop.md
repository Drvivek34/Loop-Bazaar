# The cross-repo catalog sync loop

**Loop ID**: #5066 | **Category**: Operations | **Author**: Drvivek34 | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A bounded maintenance workflow that keeps catalog repositories, generated READMEs, counts, links, and the Mega AI Bazaar landing metadata aligned.

## 🎯 Use Case (When to Use)
> Use this after adding, renaming, or retiring a catalog entry or when several Bazaar repositories have been refreshed independently.

## ⚡ System Prompt / Instructions
```
Read the source data and generated documentation for every in-scope Bazaar repository. Compare repository names, category slugs, entry counts, source links, dates, and landing-site metadata. Regenerate outputs from source data where a compiler exists, fix only real drift, validate JSON and Markdown links, and verify that no private repository or secret is included.
```

## 🏁 Implementation Steps
1. Inventory the public repositories and identify source-of-truth files versus generated outputs.
2. Parse the catalogs and compare names, categories, counts, URLs, and review dates.
3. Regenerate documentation from source data, then make minimal manual fixes for metadata that is not generated.
4. Validate JSON, Markdown links, category paths, and public/private boundaries.
5. Commit the synchronized changes in a traceable order and verify the resulting default-branch state.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The landing metadata and every generated README describe the same public catalog state.
- *Detail*: The report includes source files, generated files, counts, category differences, link-check results, excluded private repositories, and the final commit references.

## 💡 Why it works
A family of catalogs becomes misleading when individual READMEs or the landing site drift away from their source data. Separating source files from generated outputs makes synchronization repeatable.

## ⚠️ Implementation Note
* Never overwrite unrelated user changes, delete entries, or expose private operational repositories. Stop on a conflict or unexpected resource.

## 🏷️ Keywords
catalog sync, documentation drift, repository maintenance, generated README, metadata

## 💬 Reviews & Feedback
- *No reviews yet.*