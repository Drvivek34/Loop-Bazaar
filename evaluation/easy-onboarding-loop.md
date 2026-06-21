# The easy onboarding loop

**Loop ID**: #039 | **Category**: Evaluation | **Author**: Eric Lott | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A first-time-user test that starts with no saved account or browser state, fixes one confirmed onboarding obstacle, and retries the entire experience.

## 🎯 Use Case (When to Use)
> Use this when new users may face unclear instructions, hidden assumptions, difficult recovery, or unnecessary steps that experienced users no longer notice because their accounts and browsers remember earlier setup.

## ⚡ System Prompt / Instructions
```
Act like a first-time user of [product]. Start at the real entry point in a clean session with no saved login, site data, remembered route, or hidden setup. Complete onboarding using only visible guidance and record obstacles. Fix the worst one with the smallest change that preserves every security, access, and product requirement. Discard the session and retry. Stop after one uninterrupted success, no safe fix, blocked access, or required approval. Return the path, changes, evidence, and blockers.
```

## 🏁 Implementation Steps
1. Open a clean session with no saved login, cookies, site storage, remembered web address, secret setup, or repair left over from an earlier attempt.
2. Begin where a real newcomer begins, complete the onboarding steps using only visible guidance, and record anything unclear, unexplained, unnecessarily difficult, or impossible to recover from.
3. Fix the most harmful obstacle with the smallest change that preserves security, access, legal, onboarding, and product requirements.
4. Throw away the session and retry the entire experience until one uninterrupted clean pass succeeds or no safe progress is possible, access is blocked, or approval is required.

## 🛑 Stopping Condition (Verification)
**Verification Check**: A first-time user can complete onboarding in one uninterrupted clean session.
- *Detail*: The full experience succeeds from the real starting point without saved browser state, secret setup, guessed routes, or manual repairs, and every real requirement remains intact.

## 💡 Why it works
Saved logins and remembered setup hide problems from experienced users. Starting over after every fix shows whether the product itself now explains the path, while preserving real requirements prevents an easier experience from weakening security or access controls.

## ⚠️ Implementation Note
* A clean session means a new private browser or another isolated environment with no cookies, login, local storage, cache, or remembered route. Start where a newcomer would actually arrive and follow only the guidance the product exposes.

## 🏷️ Keywords
onboarding improvement, fresh session testing, new user experience, agent friendly onboarding, onboarding friction

## 💬 Reviews & Feedback
- *No reviews yet.*