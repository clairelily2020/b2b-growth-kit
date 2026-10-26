---
name: b2b-growth-kit
description: Entry point and shared foundation for B2B marketing work - loads the company profile, applies the shared policies (approvals, evidence, metrics, outreach), picks the right workflow or skill for the request, and produces the requested artifact. Use for any B2B marketing, growth or go-to-market request that spans several functions, when unsure which marketing skill fits, or to set up a company profile.
---

# B2B growth kit

The hub of the kit. It holds what every other skill shares, and routes a request to the workflow or skill that does the work.

## Load order

1. **Profile.** Use the profile the user points to; otherwise look for `profiles/private/*/company.toml` in the working directory; otherwise use [profile/example-company.toml](profile/example-company.toml) for demos and say so. Schema: [profile/SCHEMA.md](profile/SCHEMA.md). Missing values are unknown; never fill them with guesses.
2. **Policies** that apply to every skill:
   - [approval-gates](policies/approval-gates.md): what needs approval, what a valid approval is, draft vs executed vs worked.
   - [evidence-and-claims](policies/evidence-and-claims.md): sources, dates, unknown vs zero, no invented proof.
   - [metrics-definitions](policies/metrics-definitions.md): funnel stages, formulas, the attribution gate.
   - [outreach-compliance](policies/outreach-compliance.md): suppression, lawful basis, deliverability, platform rules.
3. **Workflow** if the request is a multi-step job; otherwise go straight to one skill.

## Routing

Ask at most one clarifying question, and only when the answer changes the objective, the audience or an irreversible step. Otherwise state the assumption and proceed. Produce the requested artifact, not just a routing plan. If a needed skill is not installed, say which and continue with what is available.

### Workflows (multi-step jobs)

| Job | Workflow |
|---|---|
| Figure out who we sell to and what we say | [positioning-sprint](workflows/positioning-sprint.md) |
| Book meetings from a target list | [account-based-outbound](workflows/account-based-outbound.md) |
| Get meetings out of a trade show or conference | [event-abm](workflows/event-abm.md) |
| Win buyer questions in search and AI assistants | [content-to-citation](workflows/content-to-citation.md) |
| Launch or fix a search ads campaign | [paid-search-launch](workflows/paid-search-launch.md) |
| Build a founder and brand social presence | [founder-led-social](workflows/founder-led-social.md) |
| Launch a product or feature | [product-launch](workflows/product-launch.md) |
| Run the weekly marketing loop | [weekly-growth-review](workflows/weekly-growth-review.md) |

### Skills (single jobs)

| Area | Skills |
|---|---|
| Strategy | [icp-and-positioning](../icp-and-positioning/SKILL.md), [offer-design](../offer-design/SKILL.md), [competitive-intel](../competitive-intel/SKILL.md), [market-signal-brief](../market-signal-brief/SKILL.md), [voice-of-customer](../voice-of-customer/SKILL.md) |
| Content, SEO, GEO | [seo](../seo/SKILL.md), [answer-engine-content](../answer-engine-content/SKILL.md), [geo-citation-scout](../geo-citation-scout/SKILL.md), [article-writer](../article-writer/SKILL.md), [programmatic-pages](../programmatic-pages/SKILL.md), [link-acquisition](../link-acquisition/SKILL.md), [landing-page](../landing-page/SKILL.md), [prepublish-qa](../prepublish-qa/SKILL.md), [cms-draft-patcher](../cms-draft-patcher/SKILL.md) |
| Paid | [google-ads](../google-ads/SKILL.md), [linkedin-ads](../linkedin-ads/SKILL.md), [reddit-ads](../reddit-ads/SKILL.md), [ad-creative](../ad-creative/SKILL.md) |
| Outbound and sales | [prospect-list-builder](../prospect-list-builder/SKILL.md), [cold-email](../cold-email/SKILL.md), [linkedin-outbound](../linkedin-outbound/SKILL.md), [send-preflight](../send-preflight/SKILL.md), [revenue-handoff](../revenue-handoff/SKILL.md) |
| Social and community | [founder-led-content](../founder-led-content/SKILL.md), [brand-social-content](../brand-social-content/SKILL.md), [social-engagement](../social-engagement/SKILL.md), [content-calendar](../content-calendar/SKILL.md), [creator-partnerships](../creator-partnerships/SKILL.md), [reddit-community](../reddit-community/SKILL.md) |
| Campaigns | [campaign-brief](../campaign-brief/SKILL.md), [campaign-review](../campaign-review/SKILL.md), [launch-campaign](../launch-campaign/SKILL.md) |
| Data and operations | [marketing-data-ops](../marketing-data-ops/SKILL.md), [marketing-reporting](../marketing-reporting/SKILL.md), [performance-diagnosis](../performance-diagnosis/SKILL.md), [growth-plan](../growth-plan/SKILL.md), [ops-brief](../ops-brief/SKILL.md), [martech-scouting](../martech-scouting/SKILL.md) |

## Setting up a profile

When the user has no profile, offer to build one: read their website and any material they give, fill what is supported, leave the rest empty, and list the empty fields as questions. Save it under `profiles/private/<company>/company.toml` in their working repo, which git ignores.

## Shared rules

- Respond in the user's language; skill instructions are in English.
- Separate fact, inference and recommendation.
- Local drafting, research and analysis need no approval. Anything that publishes, sends, spends, edits live ads or writes to a system of record does.
- Report outcomes as they are: draft ready, executed (with receipt), or worked (after the measurement window).
