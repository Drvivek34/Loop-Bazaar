# The propagation compliance loop

**Loop ID**: #033 | **Category**: Engineering | **Author**: @iamTristan | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A consistency check for values copied across a code project: update every affected copy, find leftovers, and prove that only intentional old references remain.

## 🎯 Use Case (When to Use)
> Use this after changing something that appears in several files—such as a version number, feature name, count, rule, setting, or identifier—and every copy must stay consistent.

## ⚡ System Prompt / Instructions
```
After changing a version, count, rule, name, or configuration, list where the new value belongs and update it. Search the project for the old value and related forms. Review each match: fix real stale values, but keep intentional history, examples, migrations, or compatibility rules. Repeat until zero stale values remain. If one returns for two rounds, stop and identify what may be regenerating it. Return changes, intentional matches, and search output.
```

## 🏁 Implementation Steps
1. List the files, documentation, settings, generated outputs, or operational notes that are expected to copy the changed value.
2. Update the known copies, then search the whole project for the old value, old spelling, and other likely leftover forms.
3. Decide whether each match is truly stale or intentionally preserved history, an example, a migration, or a compatibility rule; fix only the stale matches.
4. Repeat the same searches until no stale match remains; if one comes back for two rounds, stop and identify the generator or process restoring it.

## 🛑 Stopping Condition (Verification)
**Verification Check**: No unintended copy of the old value remains.
- *Detail*: The final searches find only references that are intentionally historical or required for examples, migrations, or compatibility, with a reason recorded for each one.

## 💡 Why it works
The repeat search is the important part: it catches copies missed by the first update. Reviewing each match also prevents a broad replacement from corrupting historical notes, migration code, or examples that intentionally show the old value.

## ⚠️ Implementation Note
* The exact files depend on the change. The original submission used several operational notes and procedure files; another project might need code, tests, documentation, deployment settings, generated files, or all of them.

## 🏷️ Keywords
configuration propagation, version update audit, stale value search, repository consistency, grep verification loop

## 💬 Reviews & Feedback
- *No reviews yet.*