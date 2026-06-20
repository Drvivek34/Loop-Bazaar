# The product update podcast loop

**Loop ID**: #018 | **Category**: Content | **Author**: Pierson Marks | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A scheduled editorial workflow that turns meaningful public product changes into a short, source-grounded podcast episode.

## 🎯 Use Case (When to Use)
> Use this when a product ships frequently enough that users would benefit from a short recurring audio explanation of what changed and how to use it.

## ⚡ System Prompt / Instructions
```
Each night, review publicly released product changes and select only those users need to know. Verify each against the product, docs, or release notes. Use the Jellypod MCP to turn the approved changes into a three-to-five-minute podcast explaining what changed, why it matters, and how to try it. Check the script and audio for accuracy, clarity, and pronunciation. If nothing meaningful shipped, make no episode. Ask before publishing. Finish with the draft episode, sources, and review result.
```

## 🏁 Implementation Steps
1. Collect the previous day's public product changes, documentation, and release notes.
2. Select the changes most meaningful to users and verify what actually shipped.
3. Use Jellypod to draft a three-to-five-minute episode covering the benefit and how to try each selected change.
4. Review the script and audio against the sources, regenerate weak passages, and request approval before publishing.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The episode accurately covers every meaningful public update.
- *Detail*: Finish with a review-ready three-to-five-minute episode, or a confirmed no-episode result when nothing meaningful shipped.

## 💡 Why it works
A fixed release window keeps coverage current, while editorial selection and source verification prevent the episode from becoming an automated reading of commit titles.

## ⚠️ Implementation Note
* Use only publicly released information. Do not expose private repository context, customer data, security-sensitive details, or unreleased work in the generated episode.

## 🏷️ Keywords
AI podcast workflow, product update podcast, Jellypod MCP, release communication, editorial automation

## 💬 Reviews & Feedback
- **@alan_turing** (★★★★☆ 4/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)