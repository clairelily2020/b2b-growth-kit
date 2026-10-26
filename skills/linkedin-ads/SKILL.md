---
name: linkedin-ads
description: Plan and write B2B LinkedIn Ads campaigns - audience design by job function, seniority, company list and exclusions, objective and format choice (single image, document, video, carousel, conversation, lead gen form), feed-native copy, conversion tracking and test cadence. Use for LinkedIn advertising, sponsored content, account-based ads, matched audiences, lead gen forms, or LinkedIn ad copy.
---

# LinkedIn Ads

LinkedIn reaches buyers by role and company precisely, at a high price per click. That makes audience design and offer choice matter more than on any other channel.

## When to use

- Reaching a defined set of roles or a named account list.
- Supporting an account-based outbound program with air cover.
- Promoting a proof asset (report, benchmark, sample) to cold but well-defined buyers.
- Not the cheapest place to test raw demand; search is usually cheaper for that.

## Inputs

- Profile: `icp` (roles, segments, regions, exclusions), `positioning`, `offer`, `claims`, `measurement.conversion_events`.
- Optional: a target account list, website visitor and customer lists for matched audiences or exclusion.
- Budget range and the time you can wait for results.

## Process

1. **Pick the objective by funnel stage.** Awareness or engagement for cold audiences with a proof asset; website conversions or lead generation for warm or account-list audiences. Do not run a demo-request ad to a cold audience that has never heard of you.
2. **Design the audience.**
   - Start with job function plus seniority, then narrow with industry, company size and region. Titles alone miss variants and inflate cost.
   - For ABM, upload the account list; expect match rates below 100%.
   - Exclude customers, competitors, your own employees, students and job seekers where possible.
   - Check the forecast audience size against the platform's current minimums; too small will not deliver, too broad wastes spend.
3. **Choose the format.** Single image for a clear message; document ads for a proof asset; short video for a product action; conversation ads for warm audiences only. Lead gen forms lift form completion but lower lead quality; ask one qualifying question.
4. **Write feed-native copy.** It should read like a useful post: the hook fits in the visible part before "see more" (roughly the first 150 characters; check the current spec), one point, one CTA. Use [ad-creative](../ad-creative/SKILL.md) for angles and variants.
5. **Track properly.** Install the platform tag and server-side conversions where possible, map the profile's conversion events, and send later-stage outcomes (qualified lead, opportunity) back when the CRM allows. Report on qualified pipeline, not form fills.
6. **Test with discipline.** Two or three ads per campaign, one variable at a time. Decide in advance the spend or impressions after which a variant is judged. Frequency above about 4-6 per person per month on a small audience usually means it is time to rotate creative.
7. **Read results by stage**: CTR and cost per click (creative and audience fit), conversion rate (offer and landing page), qualified rate (audience quality).

## Output

```markdown
Objective / funnel stage / offer / budget and duration
## Audience
Include (functions, seniority, industries, size, regions, lists) / Exclude / Forecast size
## Ads (format, intro text, headline, CTA, visual brief) with character counts
## Tracking plan
## Test plan and stop rules
```

## Gates

- Claims follow [evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md); no customer logos or quotes without permission.
- Uploading contact or account lists follows [outreach-compliance](../b2b-growth-kit/policies/outreach-compliance.md) on lawful basis and data handling.
- Launching, budget changes and edits to live campaigns follow [approval-gates](../b2b-growth-kit/policies/approval-gates.md).

## References

- Account lists: [prospect-list-builder](../prospect-list-builder/SKILL.md) · Landing pages: [landing-page](../landing-page/SKILL.md)
