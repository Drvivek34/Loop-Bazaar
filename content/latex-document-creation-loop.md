# The LaTeX document creation loop

**Loop ID**: #061 | **Category**: Content | **Author**: Alex Vogiatzis | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A strict AI document workflow for creating a seven-section LaTeX preprint with native figures, traceable claims, repeated compilation, and explicit weaknesses.

## 🎯 Use Case (When to Use)
> Use this when supplied research material must become a complete, auditable LaTeX preprint without external image assets or fabricated evidence.

## ⚡ System Prompt / Instructions
```
Create a complete LaTeX preprint about [topic] using [supplied sources, assumptions, and data]. If the topic or required source material is missing, request it and stop. Do not invent claims, citations, or data. Use explicit placeholders for missing information. Include exactly these sections in order: Abstract, Introduction, Methods, Results, Discussion, Conclusion, and References. Build every figure and table with native LaTeX tools such as TikZ, pgfplots, and booktabs. Do not use \includegraphics, \svg, or external image files. Every substantive claim must trace to a numbered equation, citation, supplied datum, or labeled assumption. Compile using the project's documented command or latexmk when no command is specified. Inspect compilation errors, warnings, typography, cross-references, and figure placement. Fix the most serious issue and compile again for at most five rounds. Stop when compilation has zero errors, all seven sections are present, every figure and table is referenced before it appears, and no banned command remains. Otherwise stop as blocked or exhausted. Finish with the .tex file, compilation command and log, structural checks, three substantive weaknesses, three typography issues, and unresolved placeholders.
```

## 🏁 Implementation Steps
1. Confirm the topic, supplied sources, assumptions, and data; mark missing information with explicit placeholders.
2. Draft the seven required sections and create every figure and table with native LaTeX tools.
3. Compile, inspect the most serious structural, reference, visual, or typography issue, and repair it for at most five rounds.
4. Stop on a clean gated build or an honest blocker, then return the source, log, checks, weaknesses, and placeholders.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The preprint compiles cleanly and every claim and native visual is accounted for.
- *Detail*: The final source has all seven ordered sections, zero compilation errors, no banned image command, traceable claims, referenced native figures and tables, and explicit remaining weaknesses.

## 💡 Why it works
A polished-looking preprint can still contain fabricated claims, broken references, external assets, or hidden compile failures. Fixed structure and repeated compilation make the document inspectable and reproducible.

## ⚠️ Implementation Note
* Use only supplied material unless the user separately authorizes research. Do not fabricate citations or data. Save the full compilation log as an artifact rather than flooding a conversational response.

## 🏷️ Keywords
LaTeX document creation, AI research writing, TikZ pgfplots, source traceability, LaTeX compilation

## 💬 Reviews & Feedback
- *No reviews yet.*