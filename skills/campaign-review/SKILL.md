---
name: campaign-review
description: Review a marketing asset or plan before it ships - from strategy, copy, design, growth, data and founder angles - with findings rated blocker, fix or consider, then run a launch preflight (message, links and tracking, channel fit, measurement, risk) and give a ship call. Use for reviewing posts, emails, landing pages, ads, decks, plans or campaigns, a second opinion, or a pre-launch check.
---

# Campaign review

Finds the problems that would make an asset fail, mislead or teach you nothing, while there is still time to fix them. Findings come first; praise only where it helps keep something that works.

## When to use

- Any asset or plan before it goes out: post, email, landing page, ad set, deck, campaign plan.
- A quick preflight right before launch.
- For rendered web pages, also run [prepublish-qa](../prepublish-qa/SKILL.md); for outbound sends, [send-preflight](../send-preflight/SKILL.md).

## Inputs

- The asset or plan, and its brief (goal, audience, KPI) if one exists.
- Profile: `positioning`, `claims`, `voice`, `offer`, `measurement`.

## Process

1. **Pick the relevant roles** (not all of them for a small asset):
   | Role | Checks |
   |---|---|
   | Strategy | Audience, priority, scope, fit with the business goal |
   | Copy | Hook, clarity, specificity, one CTA, tone |
   | Design | Hierarchy, scannability, credibility, visual fit |
   | Growth | Channel fit, timing, distribution plan, tracking |
   | Data | KPI, baseline, instrumentation, learning window |
   | Founder | Opportunity cost, focus, a simpler path |
2. **Rate each finding:** blocker (likely to fail or mislead), fix (change before shipping), consider (optional improvement). At most ten findings; merge duplicates across roles.
3. **If the draft is early,** review structure and positioning first, not wording.
4. **Preflight checklist** before launch:
   - Message: clear audience, one primary CTA, believable claim, no unsupported numbers, no hype.
   - Links and tracking: links work, UTMs present, CTA destination matches the promise, form or signup tested.
   - Channel fit: format suits the platform, the first lines carry the point, assets attached, timing chosen on purpose.
   - Measurement: one KPI, a baseline or expectation, a learning window, an owner who checks results.
   - Risk: no private data, no customer names without permission, no misleading competitor claims, no internal notes left in.
5. **Ship call:** ship, ship after fixes, or do not ship yet, with one next step. If a rewrite is requested, give it after the review.

## Output

```markdown
## Review: {asset}
Findings
1. [Blocker] {role}: {issue}. Fix: {specific change}
2. [Fix] ...
What to keep (only if useful)
## Preflight
Status / blockers / fixes / KPI and check date / final CTA
Ship call and next step
```

## Gates

- No KPI means blocked until one is chosen. Links that could not be checked are reported as unchecked.
- Claims follow [evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md); a ship call is advice, and launching follows [approval-gates](../b2b-growth-kit/policies/approval-gates.md).
- No scores out of 10.

## References

- Upstream: [campaign-brief](../campaign-brief/SKILL.md)
