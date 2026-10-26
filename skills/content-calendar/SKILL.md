---
name: content-calendar
description: Build a rolling two-to-four-week cross-channel content calendar for B2B marketing (founder, brand, blog, email, community) tied to launches, events and campaigns, with owners, status, linked activity and post-publish metrics. Use for content planning, editorial calendars, social media schedules, campaign content alignment, or weekly content planning.
---

# Content calendar

A calendar keeps channels saying the same thing at the right time and keeps a small team from either flooding or going silent. It plans; publishing happens in the channel skills.

## When to use

- Weekly planning of the next two to four weeks.
- A launch, event or campaign needs coordinated content.
- Checking that messaging is consistent across channels.

## Inputs

- Profile: `channels.active`, `voice.personas`, `positioning`, `approvals.publish`.
- Upcoming dates: product releases, events you attend or target, campaign launches, partner content.
- Capacity: how many pieces each owner can actually produce per week.
- Last period's metrics.

## Process

1. **Anchor dates first:** launches, events (start content about two weeks before), campaigns, holidays when your buyers are away.
2. **Set themes:** one monthly theme agreed with the founder; weekly topics under it.
3. **Allocate by channel and owner** within real capacity. Fewer, better pieces beat a full calendar that slips.
4. **Fields per item:**
   | Field | Values |
   |---|---|
   | Date | YYYY-MM-DD |
   | Channel and account | founder LinkedIn, brand X, blog, newsletter, community |
   | Topic | one line |
   | Format | post, thread, carousel, video, document, article, email |
   | Owner (role) | |
   | Status | idea, drafting, in review, approved, published |
   | Linked activity | launch, event, campaign, partner |
   | Link and UTM | |
   | Published URL | after publishing |
   | Metrics | filled 24-48 h after |
5. **Review rhythm:** a short weekly check of the next week's items with the approver; metrics filled at the end of the week and fed into [marketing-reporting](../marketing-reporting/SKILL.md).
6. **Consistency check:** the same claim, number or offer reads the same everywhere it appears that week.

## Output

A calendar table with the fields above, plus:

```markdown
## Anchor dates and themes
## Capacity check (planned vs available, per owner)
## Gaps and risks (missing assets, approvals pending)
```

## Gates

- The calendar is a plan; each item still needs its own approval before publishing ([approval-gates](../b2b-growth-kit/policies/approval-gates.md)).
- Metrics follow [metrics-definitions](../b2b-growth-kit/policies/metrics-definitions.md); empty means not yet measured, not zero.

## References

- Channel execution: [founder-led-content](../founder-led-content/SKILL.md), [brand-social-content](../brand-social-content/SKILL.md), [article-writer](../article-writer/SKILL.md)
