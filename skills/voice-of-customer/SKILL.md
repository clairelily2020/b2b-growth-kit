---
name: voice-of-customer
description: Plan and synthesize customer, prospect and lost-deal interviews, and aggregate feedback from calls, replies, tickets and funnels into evidence-backed insights or prioritized product proposals with verbatim quotes. Use for customer interviews, buyer research, jobs-to-be-done, objection analysis, win/loss review, or turning marketing feedback into product requests.
---

# Voice of customer

Collects what buyers actually say and do, keeps their words intact, and separates what they said from what you infer. Feeds positioning, offers, copy and the product backlog.

## When to use

- Validating a problem or a segment before building or spending.
- Win/loss and churn reviews.
- Weekly or monthly roll-up of objections and feature requests from marketing and sales channels.
- Not for surveys at scale; this skill is qualitative by design.

## Inputs

- Profile: `icp`, `positioning`, `offer`.
- Raw material: call notes or transcripts, email replies, chat logs, support tickets, onboarding notes, funnel drop-off data, review-site comments.
- Consent status for each source; recordings and quotes need permission.

## Process

### Interviews

1. **Recruit across outcomes:** buyers, people who trialled and left, people who chose an alternative, and people who never bought. Only interviewing fans produces survivorship bias.
2. **Ask about the last real instance, not opinions.** When did you last do this job? Why that week? Who did it, with what tool, delivered to whom? What was slowest? What happens when it goes wrong? What did you try and abandon? Who would evaluate, pay, or block a purchase? What would make a trial fail?
3. **Avoid** "would you use this?" and pitching mid-interview. A polite "interesting" is not intent.
4. **Record per interview:** trigger and date, required output and deadline, current method and cost, buying roles, evaluation criteria, reasons not to buy, verbatim quotes in context, your inference kept separate, contradictions, agreed next step.
5. Start with about five interviews to fix the questions, then decide whether to run 10-15 more.

### Feedback aggregation

1. Pull the period's signals into one table: source, verbatim, person or account (anonymized in shared outputs), date, product area.
2. Cluster by underlying job or problem, not by the words used.
3. Promote a cluster to a proposal only when three or more distinct accounts raise it, or one revenue-blocking case is confirmed.
4. Priority: P0 blocks revenue (churn, lost deal); P1 blocks activation; P2 polish.

## Output

```markdown
## Interview synthesis (or Feedback roll-up for <period>)
| Insight | Evidence (n accounts, quotes) | Counter-evidence | Confidence | Implication |
## Buying jobs and triggers observed
## Objections and what resolved them
## Product proposals
Title (the specific problem) / area / frequency / 3 verbatim quotes / suggested change / expected impact / priority
## Open questions for the next round
```

## Gates

- Quotes are verbatim; never polish or merge them. Inference is labelled as inference. Rules in [evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md).
- Anonymize people and companies in anything shared beyond the core team; publishing a quote needs written permission.
- Incentives for interviews are not purchase intent. Proposals do not promise delivery dates.
- Contacting customers or prospects for interviews follows [outreach-compliance](../b2b-growth-kit/policies/outreach-compliance.md).

## References

- Feeds [icp-and-positioning](../icp-and-positioning/SKILL.md) and [offer-design](../offer-design/SKILL.md)
