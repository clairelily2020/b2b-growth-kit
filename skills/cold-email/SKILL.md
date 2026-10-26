---
name: cold-email
description: Write and plan B2B cold email - one-to-one founder emails for high-value accounts and short multi-step sequences for qualified lists, with a specific reason to reach out, one low-friction ask, deliverability setup, rendered-preview checks, A/B testing and reply handling. Use for cold email copy, outbound sequences, follow-ups, subject lines, sequence A/B tests, or diagnosing low reply rates.
---

# Cold email

Cold email works when it is short, specific to the recipient and easy to answer. It fails quietly when deliverability is neglected. This skill covers both the words and the plumbing.

## When to use

- A qualified list from [prospect-list-builder](../prospect-list-builder/SKILL.md) is ready for a sequence.
- One-to-one emails to a handful of high-value accounts.
- Refreshing subject lines or testing a new angle.
- Reply rates dropped and you need to know if it is copy, list or deliverability.

## Inputs

- Profile: `voice.personas` (sender), `positioning`, `offer` (entry offer, CTA), `claims`, `outreach` (domains, caps, suppression).
- The list with research angles and suppression status.
- Mode: **one-to-one** (written individually, under ~20 accounts) or **sequence** (templated with real personalization fields).

## Process

1. **Earn the first line.** A specific, checkable reason for writing to this person now: the trigger or research angle from the list. If you cannot write one, the row is not ready.
2. **Structure (under about 80-120 words):** short intro of who you are; one sentence of value tied to their situation; up to three concrete deliverables they would get; one light ask (a sample, a short question, "worth a look?"), not "book a demo"; signature; an easy opt-out line ("not relevant? reply 'no' and I'll stop").
3. **Sequence shape** (adjust to the audience):
   | Step | Day | Purpose |
   |---|---|---|
   | 1 | 0 | Reason + value + light ask |
   | 2 | 3 | Same problem, new angle or data point, in the same thread |
   | 3 | 7 | One discovery question |
   | 4 | 14 | Close the loop politely |
   Stop on any reply.
4. **One-to-one mode:** write each email individually from research; no merge fields; the founder persona can share an honest point of view.
5. **Personalization fields** must hold real data from the list (`first_name`, `company`, `research_angle`). Missing data means the row is skipped, not filled with a generic phrase.
6. **Deliverability setup** before the first send: dedicated sending domains, authentication, warm-up, daily caps per inbox, weekday sending. Details in [outreach-compliance](../b2b-growth-kit/policies/outreach-compliance.md).
7. **Rendered preview check:** open the email in the actual sending tool's preview. Paragraph breaks, lists, merge fields and links must render as approved; if the tool collapses formatting, fix it with tool-safe formatting and re-check.
8. **Test:** A/B one element (subject or first line) with a pre-set sample per variant before judging. Track reply rate and positive reply rate; open rates are unreliable because of privacy features.
9. **Replies:** positive goes to [revenue-handoff](../revenue-handoff/SKILL.md); "not interested" and unsubscribes go to suppression immediately.

## Output

```markdown
Mode / sender persona / list and size / ask
## Emails (subject, body, merge fields used) per step, with word counts
## Rows skipped and why (missing angle, missing data, suppressed)
## Deliverability checklist status
## Test plan (variable, sample per variant, metric)
## Preflight request for send-preflight
```

## Gates

- Everything in [outreach-compliance](../b2b-growth-kit/policies/outreach-compliance.md) applies; run [send-preflight](../send-preflight/SKILL.md) before any send.
- Sending a sequence or batch requires approval for that exact copy and list ([approval-gates](../b2b-growth-kit/policies/approval-gates.md)).
- No false "Re:" threads, fake familiarity, invented results or banned claims ([evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md)).

## References

- Channel pair: [linkedin-outbound](../linkedin-outbound/SKILL.md)
