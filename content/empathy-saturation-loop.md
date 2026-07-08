# The empathy saturation loop

**Loop ID**: #079 | **Category**: Content | **Author**: Tushar Kalan (@DilSalaKamina) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A UX research synthesis workflow that clusters verbatim pain points, tracks severity and frequency, and stops when evidence reaches saturation.

## 🎯 Use Case (When to Use)
> Use this when qualitative user research needs to become a prioritized pain-point map and the team needs to know when enough transcripts have been reviewed.

## ⚡ System Prompt / Instructions
```
Process unreviewed user transcripts in batches. Extract verbatim pain-point quotes, cluster them against the existing pain-point manifest, create new clusters only when the quote does not fit an existing theme, and update frequency and severity when new evidence changes a cluster. After each batch, rerun the same saturation check: whether the last two batches produced zero new clusters, enough total clusters exist, and enough transcripts have been processed. Stop at confirmed saturation, the transcript cap, low-quality input, blocked access, or human-review need. Return the manifest, batch log, weighted priorities, and stopping reason.
```

## 🏁 Implementation Steps
1. Identify unprocessed transcripts and extract only verbatim pain-point quotes.
2. Cluster new quotes against the existing manifest before creating new themes.
3. Update cluster frequency, severity, representative quote, and weighted priority after each batch.
4. Run the same saturation check after every batch.
5. Stop at confirmed saturation, transcript cap, low-quality input, blocked access, or human-review need.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Pain-point clusters and saturation status are backed by transcript evidence.
- *Detail*: The final manifest includes cluster IDs, labels, frequency, severity, weighted score, representative quotes, processed transcript count, batch log, saturation check, skipped inputs, and stop reason.

## 💡 Why it works
Transcript synthesis needs a stop rule; saturation evidence prevents endless reading while preserving the user words behind each priority.

## ⚠️ Implementation Note
* Treat transcripts as sensitive research data. Do not expose private quotes outside the approved workspace or overstate a theme that lacks enough evidence.

## 🏷️ Keywords
empathy saturation, user transcripts, pain point clusters, UX synthesis, qualitative research

## 💬 Reviews & Feedback
- *No reviews yet.*