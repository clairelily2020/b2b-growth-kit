---
name: revenue-handoff
description: Qualify inbound and outbound responses and hand them to sales with context - separate fit, engagement, buying intent and permission to contact, apply a simple qualification model, prioritize follow-up speed by signal strength, prepare a discovery or demo call guide, and update lifecycle stages only with evidence. Use for lead qualification, lead scoring, MQL or SQL handoff, positive reply handling, meeting booking, demo call scripts, or sales handoff notes.
---

# Revenue handoff

The moment between "they replied" and "sales owns it" is where most early-stage pipeline leaks. This skill qualifies quickly, books the right next step, and hands over context so nobody asks the buyer the same questions twice.

## When to use

- A positive reply, demo request, pricing question or product signup.
- Defining or applying lead scoring and MQL/SQL rules.
- Preparing for a discovery call or demo.
- Not for closing or proposals; those belong to the account owner.

## Inputs

- Profile: `icp`, `offer`, `measurement.conversion_events`, `approvals.crm_write`.
- The lead's record: source, conversation, activity (product events, pages, emails), company research.
- The team's lifecycle stages and who owns meetings.

## Process

1. **Separate four things:** fit (matches the ICP), engagement (opens, visits, usage), buying intent (stated need, timeline, budget questions) and permission (consent to be contacted, suppression status). High engagement with no intent is nurture, not sales. Unknown permission is not a pass.
2. **Prioritize by signal strength.** Strong: asks about price or a demo, uses the product's core action, returns soon after signup. Medium: signs up without using it, engages with the sequence without replying. Weak: single open or bounce visit. Respond to strong signals within hours; replies cool fast.
3. **Qualify with four questions:** company fit; the pain in their words and how they solve it today; current tools or alternatives; timeline for the next relevant decision or event. All four clear: sales-qualified, book a meeting. Two or three: marketing-qualified, keep nurturing with a specific next step. Fewer: long-term nurture.
4. **Book the next step** with a short call (15-20 minutes) and a confirmation a day before.
5. **Prepare the call guide** using [references/call-guide.md](references/call-guide.md): context on the account, discovery questions, what to show live, how to confirm value, and a concrete follow-up.
6. **Write the handoff note:** account context, people and roles, two verbatim quotes, pain, current stack, timeline, qualification result with reasons, gaps, owner role, next action and date.
7. **One contact per company in active outreach.** If several contacts exist, start with the most senior relevant role and move down only after a full sequence without response.

## Output

```markdown
## Qualification
| Fit | Engagement | Intent | Permission | Result | Reasons |
## Handoff note (context, people, quotes, pain, stack, timeline, gaps, owner, next action)
## Call guide (if a meeting is booked)
## Proposed lifecycle change and the evidence for it
```

## Gates

- Lifecycle stages change only with evidence: a finished task is not a qualified lead, a booked meeting is not an opportunity, a verbal yes is not revenue ([metrics-definitions](../b2b-growth-kit/policies/metrics-definitions.md)).
- CRM writes and outbound replies follow [approval-gates](../b2b-growth-kit/policies/approval-gates.md); contacting rules follow [outreach-compliance](../b2b-growth-kit/policies/outreach-compliance.md).
- Never invent personal facts about the prospect.

## References

- [references/call-guide.md](references/call-guide.md)
