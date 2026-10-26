---
name: offer-design
description: Design a B2B offer ladder (free entry, proof sample, paid pilot, standard package), define each offer's scope, deliverable, acceptance criteria and price unit, and match offers to channels and intent. Use when deciding what to sell first, naming a package, creating a paid pilot, choosing the CTA for a channel, or when traffic converts but nobody buys.
---

# Offer design

Most B2B funnels fail because every channel sends traffic to the same ask. This skill builds a ladder of offers, each matched to an intent level, and makes every offer concrete enough to deliver and to judge.

## When to use

- Choosing the first paid offer or a pilot.
- A channel has clicks or signups but no pipeline.
- Naming packages or rewriting a pricing page section.
- Deciding which CTA a landing page, ad or email should use.

## Inputs

- Profile: `offer`, `icp`, `positioning`, `claims`, `measurement.conversion_events`.
- What the team can actually deliver today, and the cost of delivering it (people, data, tools).
- Any pricing signals: what buyers compared you to, budget cycles, past objections.

## Process

1. **Draft the ladder.** Typical rungs, adapt as needed:
   | Rung | Intent it serves | Example form |
   |---|---|---|
   | Entry | Curious, early research | Template, free tool, sample data |
   | Proof | Needs evidence before buying | Reviewed sample on the buyer's own case |
   | Pilot | Clear use case and timeline | Paid, time-boxed, one scope |
   | Package | Repeat use | Standard plan or recurring package |
2. **Fill the six slots for every paid rung:** who it is for and the job; the deliverable (an outcome, not a feature count); input requirements and exclusions; delivery time and how acceptance is judged; price, billing unit and overage handling; what happens if it fails.
3. **Find the value unit.** Seats, usage, projects, events, accounts or outcomes. Check that heavy usage does not lose money and that the unit is easy to explain.
4. **Match offers to channels.** Cold, low-context traffic gets entry or proof offers. Warm, specific intent (named need, timeline) gets the pilot. Write the mapping as a table: channel, intent, offer, CTA, success event.
5. **Name each offer** so it is concrete, tied to the workflow and readable in three seconds. Avoid platform-speak and "AI" as the name.
6. **Write the boundaries.** What the offer does not promise. These go straight into copy and sales scripts.
7. **Diagnose "too expensive"** before cutting price: compared with what, which budget cycle, which doubt about value. It may be demand, trust, procurement or onboarding, not price.

## Output

```markdown
## Offer ladder
| Rung | Name | For whom / job | Deliverable | Acceptance | Price unit | Not included |
## Channel-to-offer map
| Channel | Intent level | Offer | CTA label | Success event (from profile) |
## Pilot terms (if a pilot is in scope)
Scope / duration / inputs / success criteria / price / what converts it to a package
## Risks (who the entry offer will wrongly attract, delivery bottlenecks)
## Open questions for the founder
```

## Gates

- Every promise in an offer must be deliverable today; future features are labelled as roadmap.
- No guaranteed outcomes; claims follow [evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md).
- Price changes and discounts are proposals. Publishing them follows [approval-gates](../b2b-growth-kit/policies/approval-gates.md).
- Before sending traffic: the channel's offer, CTA, success event and the buyer to filter out are all explicit. If any is fuzzy, fix the ladder, not the copy.

## References

- Pilot worksheet: `playbook/templates/paid-pilot.md` in the b2b-growth-kit repo.
- Landing page for the chosen offer: [landing-page](../landing-page/SKILL.md)
