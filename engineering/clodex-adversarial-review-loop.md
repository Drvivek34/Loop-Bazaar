# The Clodex adversarial-review loop

**Loop ID**: #019 | **Category**: Engineering | **Author**: Lukas Kucinski | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A Claude-and-Codex workflow that opens a pull request, runs an independent Codex review, fixes blocking findings, and repeats.

## 🎯 Use Case (When to Use)
> Use Clodex when Claude is building a meaningful code change and Codex should independently review each repair round.

## ⚡ System Prompt / Instructions
```
Run /clodex [task] think hard --max-iter 5 --threshold medium. Claude plans the task, implements it, opens a pull request, asks Codex for an adversarial review, fixes findings above the accepted severity, and repeats. Keep the branch, PR, findings, verdict, and iteration state resumable. Stop when Codex approves, only accepted findings remain, progress stalls, or the iteration cap is reached. Never describe an errored or exhausted run as approved. Finish with the PR, checks, verdict, and remaining findings.
```

## 🏁 Implementation Steps
1. Choose the task, thinking level, maximum iterations, and highest acceptable finding severity.
2. Have Claude plan, implement, verify, and open the pull request through Clodex.
3. Run the Codex adversarial review, fix blocking findings, push, and review again.
4. Persist state across rounds and finish with the verdict, remaining findings, checks, and pull-request link.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The pull request reaches the configured review bar.
- *Detail*: Codex approves it or only explicitly accepted findings remain; errors, stalls, and exhausted limits are reported as such.

## 💡 Why it works
Clodex separates the Claude builder from the Codex reviewer and turns review feedback into a bounded repair loop. Persisted state keeps the work resumable without treating an interruption as approval.

## ⚠️ Implementation Note
* The source implementation uses Clodex with Codex as the adversarial reviewer. Treat the severity threshold as a ceiling for acceptable findings, not a minimum severity to inspect.

## 🏷️ Keywords
Clodex, Codex adversarial review, Claude Code plugin, review fix loop, pull request automation

## 💬 Reviews & Feedback
- **@dennis_r** (★★★★★ 5/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)