---
name: reddit-ads
description: Plan and run B2B Reddit Ads - community, keyword and interest targeting, exclusions, bidding and learning-phase rules, pixel and conversions API setup, community-native creative written honestly from the company's voice, comment moderation and a three-week test cadence. Use for Reddit advertising, promoted posts, subreddit targeting, Reddit ad copy, or testing Reddit as a paid channel.
---

# Reddit Ads

Reddit users research purchases in topic communities and push back hard on anything that feels like a banner ad. Ads that work read like a useful, honest post from the company, and someone is ready to answer the comments.

## When to use

- Testing a problem-led offer with practitioners who discuss the problem openly.
- Search is expensive or saturated and you want a second intent channel.
- Not for brand-only awareness without someone to manage comments.

## Inputs

- Profile: `icp`, `positioning`, `offer`, `claims`, `voice`, `measurement.conversion_events`.
- Communities where the ICP discusses the problem (from research, not guesses), and their rules.
- Budget, conversion tracking status, and who will monitor comments.

## Process

1. **Targeting, from precise to broad:** communities where the problem is discussed; keyword targeting on post content for pain phrases; interests for reach; custom audiences (site visitors, customer lists) for retargeting; lookalikes once you have a solid seed. Exclude converted users and unrelated or sensitive communities.
2. **Bidding:** start with cost-per-click or a capped bid while learning; move to conversion-optimized bidding only after the pixel has a steady flow of conversions (check the platform's current minimum). Do not change bids, targeting or creative during the learning period.
3. **Measurement:** install the pixel on all pages with the profile's conversion events, add the conversions API for server-side signal, and use a click window that fits a long B2B cycle. Judge on downstream quality, not clicks alone.
4. **Creative in the community's voice, honestly from the company:** "We built this because...", concrete technical detail, admit limits, ask a real question. No "revolutionary", false urgency or perfect-accuracy claims. Never write as if you were an independent user. Hook types that fit: pain question, data finding, counter-intuitive lesson, build story. Video: captions on, value in the first three seconds, square or vertical.
5. **Comments:** someone watches the comments for the first 48 hours and replies to criticism without deleting it. Prepare answers to likely objections in advance.
6. **Three-week cadence:** week 1, three creatives across two or three targeting groups; week 2, cut the weak ones; week 3 onward, scale winners gradually (budget steps of about 20%).
7. **Benchmarks:** published CTR and cost ranges for B2B on Reddit are directional at best. Set your own baseline from the first two weeks and judge changes against it.

## Output

```markdown
Objective / offer / budget / duration / comment owner (role)
## Targeting groups (communities, keywords, interests, audiences, exclusions)
## Ads (headline, body, CTA, visual brief), each with its hook type
## Tracking setup checklist
## Test plan, stop rules and the baseline to beat
## Comment playbook (likely objections and honest answers)
```

## Gates

- Ads follow Reddit's ad policies and the targeted communities' norms; claims follow [evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md).
- No undisclosed promotion and no posing as a user, in ads or in comments.
- Launch, budget and live edits follow [approval-gates](../b2b-growth-kit/policies/approval-gates.md).

## References

- Organic community work: [reddit-community](../reddit-community/SKILL.md) · Angles and variants: [ad-creative](../ad-creative/SKILL.md)
